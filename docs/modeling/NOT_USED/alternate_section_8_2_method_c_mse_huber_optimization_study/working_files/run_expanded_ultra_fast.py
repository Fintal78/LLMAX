import math
import json
import random
import scipy.optimize as opt
import numpy as np

from optimize_method_c import BENCHMARK_DEVICES

PARAM_KEYS_EXPANDED = [
    "eta_CCCV", "C_threshold", "s_low", "eta_arch_single",
    "eta_proto_cp", "eta_proto_pps", "eta_proto_fpd", "eta_proto_5v", "eta_proto_app",
    "k", "p", "T_handshake"
]

PARAM_BOUNDS_EXPANDED = [
    (0.30, 1.00),    # Param 1: eta_CCCV [0.30, 1.00]
    (0.50, 2.50),    # Param 2: C_threshold [0.50, 2.50]
    (0.01, 3.00),    # Param 3: s_low [0.01, 3.00]
    (0.70, 1.00),    # Param 4: eta_arch_single [0.70, 1.00]
    (0.50, 1.00),    # Param 5: eta_proto_cp [0.50, 1.00]
    (0.50, 1.00),    # Param 6: eta_proto_pps [0.50, 1.00]
    (0.50, 1.00),    # Param 7: eta_proto_fpd [0.50, 1.00]
    (0.50, 1.00),    # Param 8: eta_proto_5v [0.50, 1.00]
    (0.50, 1.00),    # Param 9: eta_proto_app [0.50, 1.00]
    (0.01, 2.00),    # Param 10: k [0.01, 2.00]
    (0.10, 1.20),    # Param 11: p [0.10, 1.20]
    (0.50, 0.50),    # Param 12: T_handshake [0.50, 0.50]
]

BASELINE_PARAMS_LOSS = [
    0.72, 1.50, 0.15, 0.94,
    0.98, 0.95, 0.91, 0.83, 0.88,
    0.20, 0.45, 0.50
]

def predict_duration_expanded(wh, p_peak_w, arch_type, protocol_type, params):
    (eta_CCCV, C_thresh, s_low, eta_arch_s,
     eta_cp, eta_pps, eta_fpd, eta_5v, eta_app,
     k, p, T_handshake) = params

    E_supply = wh
    C_rate = p_peak_w / max(0.01, E_supply)
    eta_a = eta_arch_s if arch_type == 'single' else 1.00

    proto_map = {
        'charge_pump': eta_cp,
        'pps': eta_pps,
        'fixed_pd': eta_fpd,
        'legacy_5v': eta_5v,
        'apple_legacy': eta_app,
    }
    eta_proto = proto_map.get(protocol_type, 0.90)

    if C_rate > C_thresh:
        delta_C = max(1e-9, C_rate - C_thresh)
        eta_thermal = math.exp(-k * math.pow(delta_C, p))
        eff_eta_CCCV = eta_CCCV
    else:
        eta_thermal = 1.0
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)

    eff_eta_CCCV = max(0.05, min(1.00, eff_eta_CCCV))
    P_effective = p_peak_w * eff_eta_CCCV * eta_a * eta_proto * eta_thermal
    P_effective = max(0.1, P_effective)

    return (E_supply / P_effective) * 60.0 + T_handshake

def predict_all_expanded(params):
    return [predict_duration_expanded(d[0], d[1], d[2], d[3], params) for d in BENCHMARK_DEVICES]

def compute_loss_expanded(params, loss_type="mse", delta=10.0):
    T_C = predict_all_expanded(params)
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

def run_scipy_opt(loss_type, delta=10.0, seed=42):
    random.seed(seed)
    np.random.seed(seed)
    
    def obj(x):
        return compute_loss_expanded(x, loss_type=loss_type, delta=delta)

    # Multi-start L-BFGS-B
    best_x = list(BASELINE_PARAMS_LOSS)
    best_val = obj(best_x)

    # Generate 500 initial guesses
    starts = [BASELINE_PARAMS_LOSS]
    for _ in range(500):
        guess = []
        for j, (lo, hi) in enumerate(PARAM_BOUNDS_EXPANDED):
            if lo == hi:
                guess.append(lo)
            else:
                guess.append(random.uniform(lo, hi))
        starts.append(guess)

    for st in starts:
        res = opt.minimize(obj, st, method='L-BFGS-B', bounds=PARAM_BOUNDS_EXPANDED, options={'maxiter': 500, 'ftol': 1e-9})
        if res.fun < best_val:
            best_val = res.fun
            best_x = list(res.x)

    return best_x, best_val

def compute_t_metrics_expanded(params):
    T_C = predict_all_expanded(params)
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

def map_score_s1_exp(T_C):
    t_min = min(T_C)
    t_max = max(T_C)
    log_min = math.log(max(1.0, t_min))
    log_max = math.log(max(2.0, t_max))
    denom = log_max - log_min
    if denom <= 0:
        denom = 1.0
    return [max(0.0, min(10.0, 10.0 * (log_max - math.log(max(1.0, tc))) / denom)) for tc in T_C]

def map_score_s2_exp(T_C, T_min_A=9.00, T_max_A=241.0):
    log_min = math.log(T_min_A)
    log_max = math.log(T_max_A)
    denom = log_max - log_min
    return [max(0.0, min(10.0, 10.0 * (log_max - math.log(max(1.0, tc))) / denom)) for tc in T_C]

def compute_s_metrics_exp(S_C):
    N = len(BENCHMARK_DEVICES)
    e = [BENCHMARK_DEVICES[i][5] - S_C[i] for i in range(N)]
    mse = sum(x**2 for x in e) / N
    return {
        "MSE_S":   round(mse, 4),
        "RMSE_S":  round(math.sqrt(mse), 4),
        "MAE_S":   round(sum(abs(x) for x in e) / N, 4),
        "Mean_dS": round(sum(e) / N, 4),
    }

def main():
    print("=== HIGH-PRECISION SCIPY EXPANDED SEARCH DOMAIN OPTIMIZATION ===")

    deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]
    sweep = []
    huber_models = {}

    for dv in deltas:
        pd, _ = run_scipy_opt("huber", delta=dv, seed=int(dv*100))
        huber_models[dv] = pd
        tm = compute_t_metrics_expanded(pd)
        sweep.append({
            "delta": dv,
            "MSE_T": tm["MSE_T"], "RMSE_T": tm["RMSE_T"], "MAE_T": tm["MAE_T"], "Mean_dT": tm["Mean_dT"],
            "T_min_C": tm["T_min_C"], "T_max_C": tm["T_max_C"],
            "params": [round(x, 4) for x in pd],
        })
        print(f"  delta={dv:>4.1f} mins | MSE_T={tm['MSE_T']:>6.2f} | RMSE_T={tm['RMSE_T']:>5.2f} | MAE_T={tm['MAE_T']:>4.2f} | Mean_dT={tm['Mean_dT']:>+5.2f}")

    best_huber_entry = min(sweep, key=lambda x: x["MSE_T"])
    best_delta = best_huber_entry["delta"]
    p_hub_best = huber_models[best_delta]
    print(f"\nBest Huber delta threshold under expanded domain: delta = {best_delta} mins (MSE_T = {best_huber_entry['MSE_T']})")

    print("Running Pure MSE optimization...")
    p_mse, _ = run_scipy_opt("mse", seed=101)
    print("Running Pure MAE optimization...")
    p_mae, _ = run_scipy_opt("mae", seed=202)

    models = {
        "baseline": BASELINE_PARAMS_LOSS,
        "pure_mse": p_mse,
        "pure_mae": p_mae,
        "huber_best": p_hub_best,
    }

    t_metrics = {k: compute_t_metrics_expanded(v) for k, v in models.items()}
    s_metrics_s1 = {k: compute_s_metrics_exp(map_score_s1_exp(predict_all_expanded(v))) for k, v in models.items()}
    s_metrics_s2 = {k: compute_s_metrics_exp(map_score_s2_exp(predict_all_expanded(v))) for k, v in models.items()}

    T_C_hub = predict_all_expanded(p_hub_best)
    S_C_hub = map_score_s2_exp(T_C_hub)

    device_parameters = []
    device_predictions = []

    for i, d in enumerate(BENCHMARK_DEVICES):
        wh, p_peak_w, arch_type, protocol_type, T_A, S_A, name, url = d
        (eta_CCCV, C_thresh, s_low, eta_arch_s,
         eta_cp, eta_pps, eta_fpd, eta_5v, eta_app,
         k, p, T_handshake) = p_hub_best

        C_rate = p_peak_w / max(0.01, wh)
        eta_a = eta_arch_s if arch_type == 'single' else 1.00
        proto_map = {'charge_pump': eta_cp, 'pps': eta_pps, 'fixed_pd': eta_fpd, 'legacy_5v': eta_5v, 'apple_legacy': eta_app}
        eta_proto = proto_map.get(protocol_type, 0.90)

        if C_rate > C_thresh:
            delta_C = max(1e-9, C_rate - C_thresh)
            eta_th = math.exp(-k * math.pow(delta_C, p))
            eff_eta = eta_CCCV
        else:
            eta_th = 1.0
            eff_eta = eta_CCCV + s_low * (C_thresh - C_rate)

        eff_eta = max(0.05, min(1.00, eff_eta))
        P_eff = max(0.1, p_peak_w * eff_eta * eta_a * eta_proto * eta_th)

        dT = T_A - T_C_hub[i]
        dS = S_A - S_C_hub[i]

        device_parameters.append({
            "name": name, "wh": wh, "p_peak": p_peak_w, "c_rate": round(C_rate, 2),
            "arch": arch_type, "protocol": protocol_type,
            "eta_arch": round(eta_a, 4), "eta_proto": round(eta_proto, 4),
            "eta_thermal": round(eta_th, 4), "eff_eta_CCCV": round(eff_eta, 4),
            "p_effective": round(P_eff, 2), "t_handshake": round(T_handshake, 4)
        })

        device_predictions.append({
            "name": name, "power_w": p_peak_w,
            "T_A": T_A, "T_C": round(T_C_hub[i], 1),
            "S_A": S_A, "S_C": round(S_C_hub[i], 2),
            "dS": round(dS, 2), "dT": round(dT, 1),
            "url": url
        })

    master_data = {
        "best_delta": best_delta,
        "bounds": PARAM_BOUNDS_EXPANDED,
        "params": {k: [round(x, 4) for x in v] for k, v in models.items()},
        "t_metrics": t_metrics,
        "s_metrics_s1": s_metrics_s1,
        "s_metrics_s2": s_metrics_s2,
        "huber_sweep": sweep,
        "device_parameters": device_parameters,
        "device_predictions": device_predictions,
    }

    with open("scratch/expanded_domain_study_data.json", "w") as f:
        json.dump(master_data, f, indent=2)

    print("\nSUCCESS: Ultra-fast expanded domain master data saved to scratch/expanded_domain_study_data.json!")

if __name__ == "__main__":
    main()
