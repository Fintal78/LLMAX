import math
import json
import random

from optimize_method_c import BENCHMARK_DEVICES, BASELINE_PARAMS, PARAM_KEYS

PARAM_BOUNDS_WIDE = [
    (0.80, 2.50),    # C_threshold
    (0.01, 0.50),    # k
    (0.10, 0.80),    # p
    (0.35, 0.65),    # eta_base
    (0.10, 0.60),    # s_low
    (0.10, 1.50),    # T_handshake
    (0.95, 1.35),    # F_charge_pump
    (0.90, 1.25),    # F_pps
    (0.80, 1.15),    # F_fixed_pd
    (0.70, 1.05),    # F_legacy_5v
    (0.70, 1.05),    # F_apple
    (1.00, 1.50),    # F_arch
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

def loss_func(params, loss_type="huber", delta=10.0):
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

print("=== 1D PARAMETER SENSITIVITY SWEEP (Varying 1 param at a time from Baseline) ===")

base_loss = loss_func(BASELINE_PARAMS)
print(f"Baseline Huber Loss: {base_loss:.4f}\n")

for j, name in enumerate(PARAM_KEYS):
    lo, hi = PARAM_BOUNDS_WIDE[j]
    best_val = BASELINE_PARAMS[j]
    min_l = base_loss
    steps = 40
    for s in range(steps + 1):
        v = lo + s * (hi - lo) / steps
        test_p = list(BASELINE_PARAMS)
        test_p[j] = v
        l = loss_func(test_p)
        if l < min_l - 1e-6:
            min_l = l
            best_val = v
    print(f"  {name:<25}: Baseline={BASELINE_PARAMS[j]:.4f} -> Best 1D={best_val:.4f} (Loss: {base_loss:.4f} -> {min_l:.4f})")

print("\n=== MULTI-START RANDOM SEARCH + STEEPEST DESCENT (50,000 trials) ===")
best_overall_params = list(BASELINE_PARAMS)
best_overall_loss = base_loss

random.seed(42)

for trial in range(50000):
    # Perturb all parameters
    cand = []
    for j in range(len(PARAM_KEYS)):
        lo, hi = PARAM_BOUNDS_WIDE[j]
        # Mix baseline with random perturbation
        if random.random() < 0.5:
            cand.append(BASELINE_PARAMS[j] + random.gauss(0, (hi - lo) * 0.1))
        else:
            cand.append(random.uniform(lo, hi))
        cand[j] = max(lo, min(hi, cand[j]))
    
    l = loss_func(cand)
    if l < best_overall_loss:
        best_overall_loss = l
        best_overall_params = list(cand)

print(f"Best Random Search Huber Loss: {best_overall_loss:.4f}")

# Now fine-tune best_overall_params with fine coordinate descent
for it in range(1000):
    for j in range(len(PARAM_KEYS)):
        lo, hi = PARAM_BOUNDS_WIDE[j]
        step = (hi - lo) * 0.01
        for d in [+1, -1, +0.1, -0.1, +0.01, -0.01]:
            cand = list(best_overall_params)
            cand[j] = max(lo, min(hi, cand[j] + d * step))
            l = loss_func(cand)
            if l < best_overall_loss - 1e-8:
                best_overall_loss = l
                best_overall_params = list(cand)

print(f"Fine-tuned Huber Loss: {best_overall_loss:.4f}")

print("\n--- FINAL GLOBAL OPTIMA PARAMETER TABLE ---")
print(f"{'Parameter':<25} {'Baseline':>8} {'Global Opt':>10}  {'Bounds':<16}")
print("-" * 65)
for j, name in enumerate(PARAM_KEYS):
    lo, hi = PARAM_BOUNDS_WIDE[j]
    print(f"{name:<25} {BASELINE_PARAMS[j]:>8.4f} {best_overall_params[j]:>10.4f}  [{lo:.2f}, {hi:.2f}]")

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
    }

tm_global = compute_t_metrics(best_overall_params)
print(f"\nGlobal Opt Metrics: RMSE_T={tm_global['RMSE_T']}m, MAE_T={tm_global['MAE_T']}m, Mean_dT={tm_global['Mean_dT']:+}m")
