import math
import json
import numpy as np
from scipy.optimize import minimize, differential_evolution

from optimize_method_c import BENCHMARK_DEVICES, BASELINE_PARAMS, PARAM_KEYS

# Physical search domains (unconstrained, non-zero width for all optimizable parameters)
# Let's also include T_handshake in [0.0, 1.5] or [0.1, 1.0] if needed, or keep bounds reasonable.
PARAM_BOUNDS_FULL = [
    (0.80, 3.00),    # C_threshold
    (0.01, 0.50),    # k
    (0.10, 1.00),    # p
    (0.35, 0.65),    # eta_base
    (0.10, 0.60),    # s_low
    (0.10, 1.50),    # T_handshake (physical 6s to 90s range)
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

print("=== TESTING SCIPY OPTIMIZATION (Nelder-Mead, Powell, L-BFGS-B) ===")

initial_loss = loss_func(BASELINE_PARAMS, "huber")
print(f"Initial Huber Loss (Baseline): {initial_loss:.4f}")

# Method 1: Powell
res_powell = minimize(lambda p: loss_func(p, "huber"), BASELINE_PARAMS, method='Powell', bounds=PARAM_BOUNDS_FULL)
print(f"\nPowell Loss: {res_powell.fun:.4f}")

# Method 2: L-BFGS-B
res_lbfgs = minimize(lambda p: loss_func(p, "huber"), BASELINE_PARAMS, method='L-BFGS-B', bounds=PARAM_BOUNDS_FULL)
print(f"L-BFGS-B Loss: {res_lbfgs.fun:.4f}")

# Method 3: Nelder-Mead
res_nm = minimize(lambda p: loss_func(p, "huber"), BASELINE_PARAMS, method='Nelder-Mead', bounds=PARAM_BOUNDS_FULL)
print(f"Nelder-Mead Loss: {res_nm.fun:.4f}")

# Method 4: Differential Evolution (global search)
res_de = differential_evolution(lambda p: loss_func(p, "huber"), bounds=PARAM_BOUNDS_FULL, seed=42, maxiter=200)
print(f"Differential Evolution Loss: {res_de.fun:.4f}")

print("\n--- PARAMETER COMPARISON (Huber Loss) ---")
print(f"{'Parameter':<25} {'Baseline':>8} {'SciPy DE':>8} {'SciPy LBFGS':>8} {'Bounds':<16}")
print("-" * 75)
for j, name in enumerate(PARAM_KEYS):
    lo, hi = PARAM_BOUNDS_FULL[j]
    print(f"{name:<25} {BASELINE_PARAMS[j]:>8.4f} {res_de.x[j]:>8.4f} {res_lbfgs.x[j]:>8.4f}  [{lo:.2f}, {hi:.2f}]")

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

tm_de = compute_t_metrics(res_de.x)
print(f"\nDE Metrics: RMSE_T={tm_de['RMSE_T']}m, MAE_T={tm_de['MAE_T']}m, Mean_dT={tm_de['Mean_dT']:+}m")
