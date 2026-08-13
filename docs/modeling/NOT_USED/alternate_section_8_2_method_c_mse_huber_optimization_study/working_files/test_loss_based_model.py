import math
import json
import random

from optimize_method_c import BENCHMARK_DEVICES

# ============================================================================
# NEW LOSS-BASED PHYSICAL MODEL ARCHITECTURE (All Multipliers <= 1.0)
# ============================================================================
# P_effective = P_peak * eta_CCCV * eta_arch * eta_protocol * eta_thermal
#
# Reference baseline parameter values (Loss-based, strictly <= 1.0):
# eta_CCCV      : [0.60, 0.85] (Ideal average CC/CV power fraction, baseline ~0.72)
# C_threshold   : [0.60, 2.50] (Thermal onset C-rate)
# k             : [0.01, 1.00] (Thermal penalty coefficient)
# p             : [0.10, 1.20] (Thermal exponent)
# s_low         : [0.01, 0.50] (Low-power scaling slope)
# T_handshake   : [0.50, 0.50] (Fixed 0.50 mins / 30s)
# eta_arch_single: [0.80, 0.99] (Single-cell relative efficiency vs dual-cell 1.00)
# eta_proto_cp  : [0.92, 1.00] (Direct Charge Pump: 98% efficiency)
# eta_proto_pps : [0.85, 0.98] (USB-PD PPS: 95% efficiency)
# eta_proto_fpd : [0.80, 0.95] (Fixed PD/QC: 91% efficiency)
# eta_proto_5v  : [0.70, 0.90] (Legacy 5V: 83% efficiency)
# eta_proto_app : [0.75, 0.93] (Apple Legacy/PD: 88% efficiency)

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

def predict_duration_loss(wh, p_peak_w, arch_type, protocol_type, params, formulation="rational"):
    (eta_CCCV, C_thresh, k, p, s_low, T_handshake,
     eta_arch_s, eta_cp, eta_pps, eta_fpd, eta_5v, eta_app) = params

    E_supply = wh
    C_rate = p_peak_w / max(0.01, E_supply)

    # Architecture efficiency (Dual-cell is 1.00 reference state, single-cell < 1.0)
    eta_a = eta_arch_s if arch_type == 'single' else 1.00

    proto_map = {
        'charge_pump': eta_cp,
        'pps': eta_pps,
        'fixed_pd': eta_fpd,
        'legacy_5v': eta_5v,
        'apple_legacy': eta_app,
    }
    eta_proto = proto_map.get(protocol_type, 0.90)

    # Thermal tapering factor <= 1.0
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

def predict_all_loss(params, formulation="rational"):
    return [predict_duration_loss(d[0], d[1], d[2], d[3], params, formulation) for d in BENCHMARK_DEVICES]

def compute_loss(loss_type, params, delta=10.0, formulation="rational"):
    T_C = predict_all_loss(params, formulation)
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

def global_optimize_loss(loss_type, bounds, delta=10.0, formulation="rational", num_trials=100000, seed=42):
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
    for outer in range(2500):
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

def compute_t_metrics_loss(params, formulation="rational"):
    T_C = predict_all_loss(params, formulation)
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

print("=== EVALUATING LOSS-BASED PHYSICAL MODEL ARCHITECTURE (ALL MULTIPLIERS <= 1.0) ===")

print("\n--- 1. BASELINE MODEL EVALUATION (UNOPTIMIZED PROPOSED BASELINE) ---")
tm_base_rat = compute_t_metrics_loss(BASELINE_PARAMS_LOSS, "rational")
sm_base_rat = compute_s_metrics(map_score_s2(predict_all_loss(BASELINE_PARAMS_LOSS, "rational")))
print(f"Proposed Rational Baseline:    MSE_T={tm_base_rat['MSE_T']:>7.2f}  RMSE_T={tm_base_rat['RMSE_T']:>6.2f}  MAE_T={tm_base_rat['MAE_T']:>6.2f}  Mean_dT={tm_base_rat['Mean_dT']:>+6.2f}  MAE_S={sm_base_rat['MAE_S']:>6.4f}")

tm_base_exp = compute_t_metrics_loss(BASELINE_PARAMS_LOSS, "exponential")
sm_base_exp = compute_s_metrics(map_score_s2(predict_all_loss(BASELINE_PARAMS_LOSS, "exponential")))
print(f"Proposed Exponential Baseline: MSE_T={tm_base_exp['MSE_T']:>7.2f}  RMSE_T={tm_base_exp['RMSE_T']:>6.2f}  MAE_T={tm_base_exp['MAE_T']:>6.2f}  Mean_dT={tm_base_exp['Mean_dT']:>+6.2f}  MAE_S={sm_base_exp['MAE_S']:>6.4f}")

print("\n--- 2. GLOBAL OPTIMIZATION: RATIONAL DECAY (F_thermal = 1 / (1 + k*(C - C0)^p)) ---")
p_rat_hub, _ = global_optimize_loss("huber", PARAM_BOUNDS_LOSS, delta=10.0, formulation="rational", seed=101)
tm_rat = compute_t_metrics_loss(p_rat_hub, "rational")
sm_rat = compute_s_metrics(map_score_s2(predict_all_loss(p_rat_hub, "rational")))
print(f"Rational Huber 10:   MSE_T={tm_rat['MSE_T']:>7.2f}  RMSE_T={tm_rat['RMSE_T']:>6.2f}  MAE_T={tm_rat['MAE_T']:>6.2f}  Mean_dT={tm_rat['Mean_dT']:>+6.2f}  MAE_S={sm_rat['MAE_S']:>6.4f}")

print("\n--- 3. GLOBAL OPTIMIZATION: STRETCHED EXPONENTIAL (F_thermal = exp(-k*(C - C0)^p)) ---")
p_exp_hub, _ = global_optimize_loss("huber", PARAM_BOUNDS_LOSS, delta=10.0, formulation="exponential", seed=202)
tm_exp = compute_t_metrics_loss(p_exp_hub, "exponential")
sm_exp = compute_s_metrics(map_score_s2(predict_all_loss(p_exp_hub, "exponential")))
print(f"Exponential Huber 10: MSE_T={tm_exp['MSE_T']:>7.2f}  RMSE_T={tm_exp['RMSE_T']:>6.2f}  MAE_T={tm_exp['MAE_T']:>6.2f}  Mean_dT={tm_exp['Mean_dT']:>+6.2f}  MAE_S={sm_exp['MAE_S']:>6.4f}")

print("\n--- 4. PARAMETER COMPARISON: PROPOSED BASELINE VS CALIBRATED OPTIMA ---")
print(f"{'Parameter':<22} {'Proposed Baseline':>18} {'Rational Opt (Huber)':>22} {'Exponential Opt (Huber)':>25}")
print("-" * 90)
for j, name in enumerate(PARAM_KEYS_LOSS):
    print(f"{name:<22} {BASELINE_PARAMS_LOSS[j]:>18.4f} {p_rat_hub[j]:>22.4f} {p_exp_hub[j]:>25.4f}")
