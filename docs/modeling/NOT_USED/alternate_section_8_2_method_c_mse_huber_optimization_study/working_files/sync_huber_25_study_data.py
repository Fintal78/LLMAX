import math
import json
import random

from optimize_method_c import BENCHMARK_DEVICES

# Master script to generate 100% synchronized study data where:
# 1. Huber Sensitivity Analysis is conducted FIRST across delta in [5.0..50.0] mins
# 2. The best Huber configuration (delta = 25.0 mins) is selected as Option 3
# 3. Option 3 (delta = 25.0 mins) is compared against Baseline, Pure MSE (Opt 1), and Pure MAE (Opt 2) across all tables!

PARAM_KEYS_LOSS = [
    "eta_CCCV", "C_threshold", "k", "p", "s_low", "T_handshake",
    "eta_arch_single", "eta_proto_cp", "eta_proto_pps", "eta_proto_fpd", "eta_proto_5v", "eta_proto_app"
]

PARAM_BOUNDS_LOSS = [
    (0.60, 0.85),    # eta_CCCV: Ideal CC/CV ratio [0.60, 0.85]
    (0.60, 2.50),    # C_threshold: Thermal onset C-rate [0.60, 2.50]
    (0.01, 1.00),    # k: Thermal penalty coefficient
    (0.10, 1.20),    # p: Thermal exponent
    (0.01, 0.50),    # s_low: Low-power efficiency scaling slope
    (0.50, 0.50),    # T_handshake: Fixed 0.50 mins (30s)
    (0.80, 0.99),    # eta_arch_single: Single-cell relative efficiency (Dual = 1.00)
    (0.92, 1.00),    # eta_proto_cp: Direct Charge Pump efficiency
    (0.85, 0.98),    # eta_proto_pps: USB-PD PPS efficiency
    (0.80, 0.95),    # eta_proto_fpd: Fixed PD/QC efficiency
    (0.70, 0.90),    # eta_proto_5v: Legacy 5V efficiency
    (0.75, 0.93),    # eta_proto_app: Apple PMIC efficiency
]

BASELINE_PARAMS_LOSS = [
    0.72,   # eta_CCCV
    1.50,   # C_threshold
    0.20,   # k
    0.45,   # p
    0.15,   # s_low
    0.50,   # T_handshake
    0.94,   # eta_arch_single (Dual = 1.00)
    0.98,   # eta_proto_cp
    0.95,   # eta_proto_pps
    0.91,   # eta_proto_fpd
    0.83,   # eta_proto_5v
    0.88,   # eta_proto_app
]

def predict_duration(wh, p_peak_w, arch_type, protocol_type, params, formulation="exponential"):
    (eta_CCCV, C_thresh, k, p, s_low, T_handshake,
     eta_arch_s, eta_cp, eta_pps, eta_fpd, eta_5v, eta_app) = params

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
        if formulation == "rational":
            eta_thermal = 1.0 / (1.0 + k * math.pow(delta_C, p))
        elif formulation == "exponential":
            eta_thermal = math.exp(-k * math.pow(delta_C, p))
        eff_eta_CCCV = eta_CCCV
    else:
        eta_thermal = 1.0
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)

    eff_eta_CCCV = max(0.15, min(0.95, eff_eta_CCCV))
    P_effective = p_peak_w * eff_eta_CCCV * eta_a * eta_proto * eta_thermal
    P_effective = max(0.1, P_effective)

    T_predicted = (E_supply / P_effective) * 60.0 + T_handshake
    return T_predicted

def predict_all(params, formulation="exponential"):
    return [predict_duration(d[0], d[1], d[2], d[3], params, formulation) for d in BENCHMARK_DEVICES]

def compute_loss(loss_type, params, delta=10.0, formulation="exponential"):
    T_C = predict_all(params, formulation)
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

def global_optimize(loss_type, bounds, delta=10.0, formulation="exponential", num_trials=150000, seed=42):
    random.seed(seed)
    best_params = list(BASELINE_PARAMS_LOSS)
    best_loss = compute_loss(loss_type, best_params, delta, formulation)

    for trial in range(num_trials):
        cand = []
        for j in range(len(PARAM_KEYS_LOSS)):
            lo, hi = bounds[j]
            if lo == hi:
                cand.append(lo)
                continue
            if random.random() < 0.6:
                cand.append(BASELINE_PARAMS_LOSS[j] + random.gauss(0, (hi - lo) * 0.15))
            else:
                cand.append(random.uniform(lo, hi))
            cand[j] = max(lo, min(hi, cand[j]))
        
        l = compute_loss(loss_type, cand, delta, formulation)
        if l < best_loss:
            best_loss = l
            best_params = list(cand)

    step = 0.05
    for outer in range(3500):
        improved = False
        for j in range(len(PARAM_KEYS_LOSS)):
            lo, hi = bounds[j]
            if lo == hi:
                continue
            for mult in [1.0, 0.5, 0.2, 0.05, 0.01, 0.002]:
                s = step * mult * (hi - lo)
                for direction in [+1.0, -1.0]:
                    trial = max(lo, min(hi, best_params[j] + direction * s))
                    if abs(trial - best_params[j]) < 1e-12:
                        continue
                    cand = list(best_params)
                    cand[j] = trial
                    l = compute_loss(loss_type, cand, delta, formulation)
                    if l < best_loss - 1e-10:
                        best_loss = l
                        best_params = list(cand)
                        improved = True
        if not improved:
            step *= 0.5
            if step < 1e-8:
                break

    return best_params, best_loss

def compute_t_metrics(params, formulation="exponential"):
    T_C = predict_all(params, formulation)
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

def map_score_s1(T_C):
    t_min = min(T_C)
    t_max = max(T_C)
    log_min = math.log(max(1.0, t_min))
    log_max = math.log(max(2.0, t_max))
    denom = log_max - log_min
    if denom <= 0:
        denom = 1.0
    return [max(0.0, min(10.0, 10.0 * (log_max - math.log(max(1.0, tc))) / denom)) for tc in T_C]

def map_score_s2(T_C, T_min_A=9.00, T_max_A=241.0):
    log_min = math.log(T_min_A)
    log_max = math.log(T_max_A)
    denom = log_max - log_min
    return [max(0.0, min(10.0, 10.0 * (log_max - math.log(max(1.0, tc))) / denom)) for tc in T_C]

def compute_s_metrics(S_C):
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
    print("Generating Huber-First synchronized dataset (delta = 25.0 mins selected as best)...")

    # 1. First run Huber Sensitivity Sweep across delta in [5.0..50.0]
    deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0]
    sweep = []
    huber_models = {}

    for dv in deltas:
        pd, _ = global_optimize("huber", PARAM_BOUNDS_LOSS, delta=dv, num_trials=60000, seed=int(dv*100))
        huber_models[dv] = pd
        tm = compute_t_metrics(pd)
        sweep.append({
            "delta": dv,
            "MSE_T": tm["MSE_T"], "RMSE_T": tm["RMSE_T"], "MAE_T": tm["MAE_T"], "Mean_dT": tm["Mean_dT"],
            "T_min_C": tm["T_min_C"], "T_max_C": tm["T_max_C"],
            "params": [round(x, 4) for x in pd],
        })

    # Select delta = 25.0 mins as the best Huber configuration
    p_hub_best = huber_models[25.0]

    # 2. Run Pure MSE and Pure MAE optimizations
    p_mse, _ = global_optimize("mse", PARAM_BOUNDS_LOSS, seed=101)
    p_mae, _ = global_optimize("mae", PARAM_BOUNDS_LOSS, seed=202)

    models = {
        "baseline": BASELINE_PARAMS_LOSS,
        "pure_mse": p_mse,
        "pure_mae": p_mae,
        "huber_best": p_hub_best,
    }

    # 3. Compute metrics across all models
    t_metrics = {k: compute_t_metrics(v) for k, v in models.items()}
    s_metrics_s1 = {k: compute_s_metrics(map_score_s1(predict_all(v))) for k, v in models.items()}
    s_metrics_s2 = {k: compute_s_metrics(map_score_s2(predict_all(v))) for k, v in models.items()}

    # 4. Generate device tables for Huber Best (delta = 25.0 mins)
    T_C_hub = predict_all(p_hub_best)
    S_C_hub = map_score_s2(T_C_hub)

    device_parameters = []
    device_predictions = []

    for i, d in enumerate(BENCHMARK_DEVICES):
        wh, p_peak_w, arch_type, protocol_type, T_A, S_A, name, url = d
        (eta_CCCV, C_thresh, k, p, s_low, T_handshake,
         eta_arch_s, eta_cp, eta_pps, eta_fpd, eta_5v, eta_app) = p_hub_best

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

        eff_eta = max(0.15, min(0.95, eff_eta))
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
        "params": {k: [round(x, 4) for x in v] for k, v in models.items()},
        "t_metrics": t_metrics,
        "s_metrics_s1": s_metrics_s1,
        "s_metrics_s2": s_metrics_s2,
        "huber_sweep": sweep,
        "device_parameters": device_parameters,
        "device_predictions": device_predictions,
    }

    with open("scratch/synced_huber_25_study_data.json", "w") as f:
        json.dump(master_data, f, indent=2)

    print("Huber-first master data generated and saved to scratch/synced_huber_25_study_data.json!")

if __name__ == "__main__":
    main()
