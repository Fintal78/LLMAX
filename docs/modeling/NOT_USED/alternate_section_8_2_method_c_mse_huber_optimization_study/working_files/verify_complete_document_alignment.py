import sys
import os
import math
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from benchmark_devices import BENCHMARK_DEVICES, T_MIN_BENCHMARK, T_MAX_BENCHMARK

T_HANDSHAKE = 0.5000

def predict_single(dev, params):
    eta_CCCV, C_thresh, s_low, eta_arch_single, eta_cp, eta_pps, eta_pd, eta_5v, eta_apple, k, p = params
    wh = dev["battery_wh"]
    p_peak = dev["peak_power_w"]
    arch = dev["architecture"]
    proto = dev["protocol"]
    
    C_rate = p_peak / wh
    
    if C_rate <= C_thresh:
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)
    else:
        eff_eta_CCCV = eta_CCCV
    eff_eta_CCCV = max(0.001, min(1.00, eff_eta_CCCV))
    
    eta_arch = 1.0000 if arch == "dual" else eta_arch_single
    
    if proto == "charge_pump":
        eta_proto = eta_cp
    elif proto == "pps":
        eta_proto = eta_pps
    elif proto == "fixed_pd":
        eta_proto = eta_pd
    elif proto == "legacy_5v":
        eta_proto = eta_5v
    elif proto == "apple_legacy":
        eta_proto = eta_apple
    else:
        eta_proto = 0.70
        
    if C_rate > C_thresh:
        diff = C_rate - C_thresh
        eta_thermal = math.exp(-k * (diff ** p))
    else:
        eta_thermal = 1.0000
    eta_thermal = max(0.001, min(1.00, eta_thermal))
    
    p_eff = p_peak * eff_eta_CCCV * eta_arch * eta_proto * eta_thermal
    p_eff = max(0.01, min(p_peak, p_eff))
    
    t_pred = (wh / p_eff) * 60.0 + T_HANDSHAKE
    return {
        "t_pred": t_pred,
        "C_rate": C_rate,
        "eff_eta_CCCV": eff_eta_CCCV,
        "eta_arch": eta_arch,
        "eta_proto": eta_proto,
        "eta_thermal": eta_thermal,
        "p_eff": p_eff
    }

def evaluate_model(name, params, delta=None):
    diffs_T = []
    t_preds = []
    
    for dev in BENCHMARK_DEVICES:
        res = predict_single(dev, params)
        tp = res["t_pred"]
        ta = dev["t_actual_min"]
        diffs_T.append(tp - ta)
        t_preds.append(tp)
        
    diffs_T = np.array(diffs_T)
    mse_T = float(np.mean(diffs_T ** 2))
    rmse_T = float(np.sqrt(mse_T))
    mae_T = float(np.mean(np.abs(diffs_T)))
    mean_dT = float(np.mean(diffs_T))
    
    t_min_C = float(np.min(t_preds))
    t_max_C = float(np.max(t_preds))
    
    # Loss val
    if delta is not None:
        loss_val = 0.0
        for r in diffs_T:
            abs_r = abs(r)
            if abs_r <= delta:
                loss_val += 0.5 * (r ** 2)
            else:
                loss_val += delta * (abs_r - 0.5 * delta)
        loss_val /= len(diffs_T)
    elif "MSE" in name:
        loss_val = mse_T
    elif "MAE" in name:
        loss_val = mae_T
    else:
        loss_val = 0.0
        
    # Scores
    diffs_S1 = []
    diffs_S2 = []
    for tp, dev in zip(t_preds, BENCHMARK_DEVICES):
        sa = dev["s_actual"]
        s1 = 10.0 * (math.log(t_max_C / tp) / math.log(t_max_C / t_min_C))
        diffs_S1.append(s1 - sa)
        
        s2 = 10.0 * (math.log(T_MAX_BENCHMARK / tp) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))
        s2 = min(10.0, max(0.0, s2))
        diffs_S2.append(s2 - sa)
        
    diffs_S1 = np.array(diffs_S1)
    diffs_S2 = np.array(diffs_S2)
    
    s1_mse = float(np.mean(diffs_S1 ** 2))
    s1_rmse = float(np.sqrt(s1_mse))
    s1_mae = float(np.mean(np.abs(diffs_S1)))
    s1_bias = float(np.mean(diffs_S1))
    
    s2_mse = float(np.mean(diffs_S2 ** 2))
    s2_rmse = float(np.sqrt(s2_mse))
    s2_mae = float(np.mean(np.abs(diffs_S2)))
    s2_bias = float(np.mean(diffs_S2))
    
    print(f"\n================ {name} ================")
    print(f"MSE_T:   {mse_T:.2f} mins^2 | RMSE_T: {rmse_T:.2f} mins | MAE_T: {mae_T:.2f} mins | Mean_dT: {mean_dT:+.2f} mins")
    print(f"Loss:    {loss_val:.4f}")
    print(f"Bounds:  T_min,C = {t_min_C:.2f} mins, T_max,C = {t_max_C:.2f} mins")
    print(f"Strat 1: MSE_S = {s1_mse:.4f} pts^2 | RMSE_S = {s1_rmse:.4f} pts | MAE_S = {s1_mae:.4f} pts | Mean_dS = {s1_bias:+.4f} pts")
    print(f"Strat 2: MSE_S = {s2_mse:.4f} pts^2 | RMSE_S = {s2_rmse:.4f} pts | MAE_S = {s2_mae:.4f} pts | Mean_dS = {s2_bias:+.4f} pts")

# Opt 1: Pure MSE
params_mse = [0.7536, 0.4026, 2.2398, 0.9822, 1.0000, 0.9905, 0.8755, 0.9783, 0.7206, 0.3969, 0.1982]
evaluate_model("Opt 1: Pure MSE", params_mse)

# Opt 2: Pure MAE
params_mae = [0.6172, 0.4474, 3.0000, 0.9972, 1.0000, 0.8653, 0.8276, 0.9723, 0.6344, 0.1013, 0.5638]
evaluate_model("Opt 2: Pure MAE", params_mae)

# Opt 3: Huber delta=10.0 (Basin A)
params_huber10 = [0.7533, 0.4026, 2.2493, 0.9688, 1.0000, 1.0000, 0.9043, 0.9938, 0.7196, 0.3933, 0.1808]
evaluate_model("Opt 3: Huber delta=10.0", params_huber10, delta=10.0)
