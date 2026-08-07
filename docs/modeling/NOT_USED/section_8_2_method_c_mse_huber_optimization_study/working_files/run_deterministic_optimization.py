import math
import numpy as np
from scipy.optimize import differential_evolution
import json
import time
from benchmark_devices import BENCHMARK_DEVICES

# Model B Forward Simulation
T_HANDSHAKE = 0.5000  # Fixed physical protocol handshake intercept (mins)

def predict_duration(dev, params):
    eta_CCCV, C_thresh, s_low, s_high, k, p, eta_arch_single, eta_cp, eta_pps, eta_pd, eta_5v, eta_apple = params
    
    wh = dev["battery_wh"]
    p_peak = dev["peak_power_w"]
    arch = dev["architecture"]
    proto = dev["protocol"]
    
    C_rate = p_peak / wh
    
    # 1. CC/CV Efficiency
    if C_rate <= C_thresh:
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)
    else:
        eff_eta_CCCV = eta_CCCV + s_high * (C_thresh - C_rate)
    eff_eta_CCCV = max(0.05, min(1.00, eff_eta_CCCV))
    
    # 2. Architecture Efficiency
    if arch == "dual":
        eta_arch = 1.0000
    else:
        eta_arch = eta_arch_single
        
    # 3. Protocol Efficiency
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
        
    # 4. Thermal Decay Efficiency
    if C_rate > C_thresh:
        diff = C_rate - C_thresh
        eta_thermal = math.exp(-k * (diff ** p))
    else:
        eta_thermal = 1.0000
    eta_thermal = max(0.05, min(1.00, eta_thermal))
    
    # 5. Effective Power
    p_eff = p_peak * eff_eta_CCCV * eta_arch * eta_proto * eta_thermal
    p_eff = max(0.1, min(p_peak, p_eff))
    
    # 6. Duration
    t_pred = (wh / p_eff) * 60.0 + T_HANDSHAKE
    return t_pred, eff_eta_CCCV, eta_arch, eta_proto, eta_thermal, p_eff

PARAM_BOUNDS = [
    (0.30, 0.95),   # eta_CCCV
    (0.50, 3.00),   # C_thresh
    (0.00, 1.50),   # s_low
    (0.00, 1.00),   # s_high
    (0.0001, 1.00), # k
    (0.50, 3.00),   # p
    (0.60, 1.00),   # eta_arch_single
    (0.70, 1.00),   # eta_cp
    (0.60, 1.00),   # eta_pps
    (0.50, 0.95),   # eta_pd
    (0.50, 0.95),   # eta_5v
    (0.50, 0.95),   # eta_apple
]

PARAM_NAMES = [
    "eta_CCCV", "C_thresh", "s_low", "s_high", "k", "p",
    "eta_arch_single", "eta_cp", "eta_pps", "eta_pd", "eta_5v", "eta_apple"
]

def huber_element(r, delta):
    abs_r = abs(r)
    if abs_r <= delta:
        return 0.5 * (r ** 2)
    else:
        return delta * (abs_r - 0.5 * delta)

def loss_func(params, loss_type="mse", delta=10.0):
    total_loss = 0.0
    N = len(BENCHMARK_DEVICES)
    for dev in BENCHMARK_DEVICES:
        t_pred, _, _, _, _, _ = predict_duration(dev, params)
        t_actual = dev["t_actual_min"]
        r = t_pred - t_actual
        if loss_type == "mse":
            total_loss += (r ** 2)
        elif loss_type == "mae":
            total_loss += abs(r)
        elif loss_type == "huber":
            total_loss += huber_element(r, delta)
    return total_loss / N

def compute_metrics(params):
    N = len(BENCHMARK_DEVICES)
    diffs_T = []
    diffs_S = []
    t_preds = []
    
    for dev in BENCHMARK_DEVICES:
        t_pred, _, _, _, _, _ = predict_duration(dev, params)
        t_actual = dev["t_actual_min"]
        s_actual = dev["s_actual"]
        
        diff_T = t_pred - t_actual
        diffs_T.append(diff_T)
        t_preds.append(t_pred)
        
    diffs_T = np.array(diffs_T)
    t_preds = np.array(t_preds)
    
    mse_T = np.mean(diffs_T ** 2)
    rmse_T = np.sqrt(mse_T)
    mae_T = np.mean(np.abs(diffs_T))
    mean_dT = np.mean(diffs_T)
    
    t_min_C = np.min(t_preds)
    t_max_C = np.max(t_preds)
    
    # Strategy 1 (Dynamic Bounds) Scores
    diffs_S1 = []
    # Strategy 2 (Benchmark Aligned Bounds [9.0, 241.0]) Scores
    diffs_S2 = []
    
    for idx, dev in enumerate(BENCHMARK_DEVICES):
        tp = t_preds[idx]
        s_actual = dev["s_actual"]
        
        # S1: dynamic
        s1 = 10.0 * (math.log(t_max_C / tp) / math.log(t_max_C / t_min_C))
        diffs_S1.append(s1 - s_actual)
        
        # S2: aligned
        s2 = 10.0 * (math.log(241.0 / tp) / math.log(241.0 / 9.0))
        diffs_S2.append(s2 - s_actual)
        
    diffs_S1 = np.array(diffs_S1)
    diffs_S2 = np.array(diffs_S2)
    
    sm1 = {
        "MSE_S": float(np.mean(diffs_S1 ** 2)),
        "RMSE_S": float(np.sqrt(np.mean(diffs_S1 ** 2))),
        "MAE_S": float(np.mean(np.abs(diffs_S1))),
        "Mean_dS": float(np.mean(diffs_S1))
    }
    sm2 = {
        "MSE_S": float(np.mean(diffs_S2 ** 2)),
        "RMSE_S": float(np.sqrt(np.mean(diffs_S2 ** 2))),
        "MAE_S": float(np.mean(np.abs(diffs_S2))),
        "Mean_dS": float(np.mean(diffs_S2))
    }
    
    return {
        "MSE_T": float(mse_T),
        "RMSE_T": float(rmse_T),
        "MAE_T": float(mae_T),
        "Mean_dT": float(mean_dT),
        "T_min_C": float(t_min_C),
        "T_max_C": float(t_max_C),
        "Strategy_1": sm1,
        "Strategy_2": sm2
    }

def run_optimization(loss_type="mse", delta=10.0, seed=42):
    t0 = time.time()
    res = differential_evolution(
        loss_func,
        bounds=PARAM_BOUNDS,
        args=(loss_type, delta),
        strategy='best1bin',
        maxiter=1500,
        popsize=20,
        tol=1e-7,
        mutation=(0.5, 1.0),
        recombination=0.9,
        seed=seed,
        polish=True
    )
    elapsed = time.time() - t0
    params = res.x.tolist()
    param_dict = {name: round(val, 4) for name, val in zip(PARAM_NAMES, params)}
    metrics = compute_metrics(params)
    return {
        "loss_type": loss_type,
        "delta": delta if loss_type == "huber" else None,
        "loss_val": float(res.fun),
        "params": param_dict,
        "metrics": metrics,
        "elapsed_sec": round(elapsed, 2)
    }

if __name__ == "__main__":
    print("Testing Deterministic Global Optimization (seed=42)...")
    
    print("\n--- Running Pure MSE (Option 1) ---")
    opt_mse = run_optimization(loss_type="mse", seed=42)
    print(f"MSE_T: {opt_mse['metrics']['MSE_T']:.4f} mins^2 | RMSE_T: {opt_mse['metrics']['RMSE_T']:.4f} mins | MAE_T: {opt_mse['metrics']['MAE_T']:.4f} mins | Mean_dT: {opt_mse['metrics']['Mean_dT']:+.4f} mins | Time: {opt_mse['elapsed_sec']}s")
    
    print("\n--- Running Pure MAE (Option 2) ---")
    opt_mae = run_optimization(loss_type="mae", seed=42)
    print(f"MSE_T: {opt_mae['metrics']['MSE_T']:.4f} mins^2 | RMSE_T: {opt_mae['metrics']['RMSE_T']:.4f} mins | MAE_T: {opt_mae['metrics']['MAE_T']:.4f} mins | Mean_dT: {opt_mae['metrics']['Mean_dT']:+.4f} mins | Time: {opt_mae['elapsed_sec']}s")
    
    print("\n--- Running Huber Loss (Option 3, delta=10.0) ---")
    opt_huber_10 = run_optimization(loss_type="huber", delta=10.0, seed=42)
    print(f"MSE_T: {opt_huber_10['metrics']['MSE_T']:.4f} mins^2 | RMSE_T: {opt_huber_10['metrics']['RMSE_T']:.4f} mins | MAE_T: {opt_huber_10['metrics']['MAE_T']:.4f} mins | Mean_dT: {opt_huber_10['metrics']['Mean_dT']:+.4f} mins | Time: {opt_huber_10['elapsed_sec']}s")
