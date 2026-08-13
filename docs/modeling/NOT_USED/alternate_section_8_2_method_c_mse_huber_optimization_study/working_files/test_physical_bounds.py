import math
import json

# Import dataset from optimize_method_c
from optimize_method_c import BENCHMARK_DEVICES, BASELINE_PARAMS, PARAM_BOUNDS, PARAM_KEYS

# Let's test fixing T_handshake at 0.50 mins (or bounding T_handshake to [0.1, 1.0])
# and optimizing the remaining physical parameters.

PARAM_BOUNDS_PHYSICAL = [
    (0.80, 3.00),    # C_threshold: [0.8, 3.0]
    (0.01, 0.50),    # k: [0.01, 0.50]
    (0.10, 1.00),    # p: [0.10, 1.00]
    (0.35, 0.65),    # eta_base: [0.35, 0.65]
    (0.10, 0.60),    # s_low: [0.10, 0.60]
    (0.10, 1.00),    # T_handshake: PHYSICAL BOUND [0.10, 1.00] mins (10s to 60s)
    (0.95, 1.25),    # F_charge_pump: [0.95, 1.25]
    (0.90, 1.20),    # F_pps: [0.90, 1.20]
    (0.80, 1.10),    # F_fixed_pd: [0.80, 1.10]
    (0.70, 1.05),    # F_legacy_5v: [0.70, 1.05]
    (0.70, 1.05),    # F_apple: [0.70, 1.05]
    (1.00, 1.45),    # F_arch: [1.00, 1.45]
]

def predict_duration(wh, p_peak_w, arch_type, protocol_type, params):
    (C_thresh, k, p, eta_base, s_low, T_handshake,
     F_cp, F_pps, F_fpd, F_5v, F_app, F_arch_param) = params

    E_supply = wh
    C_rate = p_peak_w / max(0.01, E_supply)

    F_a = F_arch_param if arch_type == 'dual' else 1.0

    proto_map = {
        'charge_pump': F_cp,
        'pps': F_pps,
        'fixed_pd': F_fpd,
        'legacy_5v': F_5v,
        'apple_legacy': F_app,
    }
    F_proto = proto_map.get(protocol_type, 1.0)

    if C_rate > C_thresh:
        F_Crate = 1.0 / (1.0 + k * math.pow(max(1e-9, C_rate - C_thresh), p))
        eff_eta = eta_base
    else:
        F_Crate = 1.0
        eff_eta = eta_base + s_low * (C_thresh - C_rate)

    eff_eta = max(0.15, min(0.95, eff_eta))
    P_effective = p_peak_w * eff_eta * F_a * F_proto * F_Crate
    P_effective = max(0.1, P_effective)

    T_predicted = (E_supply / P_effective) * 60.0 + T_handshake
    return T_predicted

def predict_all(params):
    return [predict_duration(d[0], d[1], d[2], d[3], params) for d in BENCHMARK_DEVICES]

def compute_loss(loss_type, params, delta=10.0):
    T_C = predict_all(params)
    N = len(BENCHMARK_DEVICES)
    total = 0.0
    for i, d in enumerate(BENCHMARK_DEVICES):
        err = d[4] - T_C[i]
        ae = abs(err)
        if loss_type == "mse":
            total += err * err
        elif loss_type == "mae":
            total += ae
        elif loss_type == "huber":
            if ae <= delta:
                total += 0.5 * ae * ae
            else:
                total += delta * ae - 0.5 * delta * delta
    return total / N

def coordinate_descent(loss_type, initial_params, bounds, delta=10.0, max_iters=2000):
    params = list(initial_params)
    n = len(params)
    step = 0.02
    min_step = 1e-8
    best_loss = compute_loss(loss_type, params, delta)

    for iteration in range(max_iters):
        improved = False
        for j in range(n):
            lo, hi = bounds[j]
            cur_best_val = params[j]
            cur_best_loss = best_loss

            for mult in [1.0, 0.5, 0.25, 0.1, 0.05]:
                s = step * mult
                for d in [+1.0, -1.0]:
                    trial = max(lo, min(hi, params[j] + d * s))
                    if abs(trial - cur_best_val) < 1e-12:
                        continue
                    params[j] = trial
                    trial_loss = compute_loss(loss_type, params, delta)
                    if trial_loss < cur_best_loss - 1e-12:
                        cur_best_loss = trial_loss
                        cur_best_val = trial
                        improved = True
            params[j] = cur_best_val
            best_loss = cur_best_loss

        if not improved:
            step *= 0.5
            if step < min_step:
                break

    return params, best_loss

def compute_t_metrics(params):
    T_C = predict_all(params)
    N = len(BENCHMARK_DEVICES)
    e = [BENCHMARK_DEVICES[i][4] - T_C[i] for i in range(N)]
    mse = sum(x**2 for x in e) / N
    return {
        "MSE_T":   round(mse, 2),
        "RMSE_T":  round(math.sqrt(mse), 2),
        "MAE_T":   round(sum(abs(x) for x in e) / N, 2),
        "Mean_dT": round(sum(e) / N, 2),
        "T_min_C": round(min(T_C), 2),
        "T_max_C": round(max(T_C), 2),
    }

print("=== TESTING PHYSICAL T_HANDSHAKE BOUND [0.10, 1.00] MINS ===")
p_hub, l_hub = coordinate_descent("huber", BASELINE_PARAMS, PARAM_BOUNDS_PHYSICAL, delta=10.0)

print("\nFitted parameters:")
for j, name in enumerate(PARAM_KEYS):
    lo, hi = PARAM_BOUNDS_PHYSICAL[j]
    print(f"  {name:<25}: {p_hub[j]:.4f}  (bounds [{lo:.2f}, {hi:.2f}])")

tm = compute_t_metrics(p_hub)
print(f"\nMetrics: RMSE_T={tm['RMSE_T']}m, MAE_T={tm['MAE_T']}m, Mean_dT={tm['Mean_dT']:+}m")

print("\nFast charging devices check:")
T_C = predict_all(p_hub)
for i in range(10):
    d = BENCHMARK_DEVICES[i]
    print(f"  {d[6]:<28} P={d[1]:>5.0f}W  T_A={d[4]:>5.1f}m  T_C={T_C[i]:>5.1f}m  dT={d[4]-T_C[i]:>+5.1f}m")
