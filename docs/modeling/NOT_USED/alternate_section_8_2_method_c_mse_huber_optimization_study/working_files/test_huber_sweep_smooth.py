import math
from optimize_method_c import BENCHMARK_DEVICES

PARAM_KEYS_LOSS = [
    "eta_CCCV", "C_threshold", "s_low", "eta_arch_single",
    "eta_proto_cp", "eta_proto_pps", "eta_proto_fpd", "eta_proto_5v", "eta_proto_app",
    "k", "p", "T_handshake"
]

PARAM_BOUNDS_LOSS = [
    (0.30, 1.00),    # eta_CCCV: Ideal CC/CV ratio
    (0.50, 2.50),    # C_threshold: Thermal onset C-rate
    (0.01, 3.00),    # s_low: Low-power scaling slope
    (0.70, 1.00),    # eta_arch_single: Single-cell relative efficiency
    (0.50, 1.00),    # eta_proto_cp: Direct Charge Pump efficiency
    (0.50, 1.00),    # eta_proto_pps: USB-PD PPS efficiency
    (0.50, 1.00),    # eta_proto_fpd: Fixed PD/QC efficiency
    (0.50, 1.00),    # eta_proto_5v: Legacy 5V efficiency
    (0.50, 1.00),    # eta_proto_app: Apple PMIC efficiency
    (0.01, 2.00),    # k: Thermal penalty coefficient
    (0.10, 1.20),    # p: Thermal exponent
    (0.50, 0.50),    # T_handshake: Fixed 0.50 mins (30s)
]

HUBER_10_PARAMS = [
    0.5818, 0.5000, 1.9774, 0.9876,
    1.0000, 0.9305, 0.8398, 0.9611, 0.6671,
    0.0845, 0.7441, 0.5000
]

def predict_duration(wh, p_peak_w, arch_type, protocol_type, params):
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

    eff_eta_CCCV = max(0.15, min(0.95, eff_eta_CCCV))
    P_effective = p_peak_w * eff_eta_CCCV * eta_a * eta_proto * eta_thermal
    P_effective = max(0.1, P_effective)

    T_predicted = (E_supply / P_effective) * 60.0 + T_handshake
    return T_predicted

def predict_all(params):
    return [predict_duration(d[0], d[1], d[2], d[3], params) for d in BENCHMARK_DEVICES]

def compute_huber_loss(params, delta):
    T_C = predict_all(params)
    N = len(BENCHMARK_DEVICES)
    total = 0.0
    for i, d in enumerate(BENCHMARK_DEVICES):
        err = d[4] - T_C[i]
        ae = abs(err)
        if ae <= delta:
            total += 0.5 * ae * ae
        else:
            total += delta * ae - 0.5 * delta * delta
    return total / N

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

def local_pattern_search(init_params, delta, max_outer=50):
    best_p = list(init_params)
    best_l = compute_huber_loss(best_p, delta)
    step = 0.02
    for outer in range(max_outer):
        improved = False
        for j in range(len(PARAM_KEYS_LOSS)):
            lo, hi = PARAM_BOUNDS_LOSS[j]
            if lo == hi:
                continue
            for mult in [1.0, 0.3, 0.05, 0.01]:
                s = step * mult * (hi - lo)
                for direction in [+1.0, -1.0]:
                    trial = max(lo, min(hi, best_p[j] + direction * s))
                    if abs(trial - best_p[j]) < 1e-12:
                        continue
                    cand = list(best_p)
                    cand[j] = trial
                    l = compute_huber_loss(cand, delta)
                    if l < best_l - 1e-8:
                        best_l = l
                        best_p = list(cand)
                        improved = True
        if not improved:
            step *= 0.5
            if step < 1e-6:
                break
    return best_p, best_l

deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]

print("=== METHOD 1: EVALUATING FIXATED HUBER-10 PARAMETER SET ACROSS VARIOUS DELTA LOSSES ===")
for dv in deltas:
    hl = compute_huber_loss(HUBER_10_PARAMS, dv)
    tm = compute_t_metrics(HUBER_10_PARAMS)
    print(f"delta={dv:>5.1f} | HuberLoss={hl:>7.2f} | MSE_T={tm['MSE_T']:>7.2f} | RMSE_T={tm['RMSE_T']:>6.2f} | MAE_T={tm['MAE_T']:>6.2f} | Mean_dT={tm['Mean_dT']:>+6.2f}")

print("\n=== METHOD 2: CONTINUOUS WARM-STARTED LOCAL OPTIMIZATION FROM HUBER-10 OPTIMUM FOR EACH DELTA ===")
curr = list(HUBER_10_PARAMS)
for dv in deltas:
    opt_p, opt_l = local_pattern_search(curr, dv)
    tm = compute_t_metrics(opt_p)
    print(f"delta={dv:>5.1f} | HuberLoss={opt_l:>7.2f} | MSE_T={tm['MSE_T']:>7.2f} | RMSE_T={tm['RMSE_T']:>6.2f} | MAE_T={tm['MAE_T']:>6.2f} | Mean_dT={tm['Mean_dT']:>+6.2f}")
    curr = list(opt_p)
