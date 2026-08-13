import math
import json
from optimize_method_c import BENCHMARK_DEVICES, BASELINE_PARAMS, PARAM_KEYS

# Test fixing T_handshake = 0.50 mins exactly as defined in scoring_rules.md (line 4912)
# and optimizing the remaining 11 physical scalar parameters.

PARAM_BOUNDS_FIXED_HS = [
    (0.80, 3.00),    # C_threshold: [0.8, 3.0]
    (0.01, 0.50),    # k: [0.01, 0.50]
    (0.10, 1.00),    # p: [0.10, 1.00]
    (0.35, 0.65),    # eta_base: [0.35, 0.65]
    (0.10, 0.60),    # s_low: [0.10, 0.60]
    (0.50, 0.50),    # T_handshake: FIXED AT 0.50 MINS (per scoring_rules.md)
    (0.95, 1.35),    # F_charge_pump: [0.95, 1.35]
    (0.90, 1.25),    # F_pps: [0.90, 1.25]
    (0.80, 1.15),    # F_fixed_pd: [0.80, 1.15]
    (0.70, 1.05),    # F_legacy_5v: [0.70, 1.05]
    (0.70, 1.05),    # F_apple: [0.70, 1.05]
    (1.00, 1.50),    # F_arch: [1.00, 1.50]
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
            if lo == hi:
                continue
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

def check_interiority(params, bounds):
    issues = []
    for j, val in enumerate(params):
        lo, hi = bounds[j]
        if lo == hi:
            continue
        span = hi - lo
        margin_lo = (val - lo) / span
        margin_hi = (hi - val) / span
        if margin_lo < 0.02 or margin_hi < 0.02:
            side = "LOWER" if margin_lo < 0.02 else "UPPER"
            issues.append(f"  !! {PARAM_KEYS[j]} = {val:.4f} at {side} boundary [{lo}, {hi}]")
    return issues

print("=== TESTING FIXED T_HANDSHAKE = 0.50 MINS ===")
p_mse, l_mse = coordinate_descent("mse", BASELINE_PARAMS, PARAM_BOUNDS_FIXED_HS)
p_mae, l_mae = coordinate_descent("mae", BASELINE_PARAMS, PARAM_BOUNDS_FIXED_HS)
p_hub, l_hub = coordinate_descent("huber", BASELINE_PARAMS, PARAM_BOUNDS_FIXED_HS, delta=10.0)

print("\n--- PARAMETER FITTING TABLE ---")
print(f"{'Parameter':<25} {'Baseline':>8} {'PureMSE':>8} {'PureMAE':>8} {'Huber10':>8}  {'Bounds':<16}")
print("-" * 85)
for j, name in enumerate(PARAM_KEYS):
    lo, hi = PARAM_BOUNDS_FIXED_HS[j]
    print(f"{name:<25} {BASELINE_PARAMS[j]:>8.4f} {p_mse[j]:>8.4f} {p_mae[j]:>8.4f} {p_hub[j]:>8.4f}  [{lo:.2f}, {hi:.2f}]")

print("\n--- INTERIORITY CHECK ---")
for label, p in [("Pure MSE", p_mse), ("Pure MAE", p_mae), ("Huber 10", p_hub)]:
    issues = check_interiority(p, PARAM_BOUNDS_FIXED_HS)
    if issues:
        print(f"  {label} Warnings:")
        for iss in issues:
            print(iss)
    else:
        print(f"  {label}: ALL PARAMETERS INTERIOR — PERFECT OK!")

print("\n--- DURATION METRICS ---")
for label, p in [("Baseline", BASELINE_PARAMS), ("Pure MSE", p_mse), ("Pure MAE", p_mae), ("Huber 10", p_hub)]:
    tm = compute_t_metrics(p)
    print(f"  {label:<12}: RMSE_T={tm['RMSE_T']:>5.2f}m, MAE_T={tm['MAE_T']:>5.2f}m, Mean_dT={tm['Mean_dT']:>+5.2f}m, T_min={tm['T_min_C']}m, T_max={tm['T_max_C']}m")
