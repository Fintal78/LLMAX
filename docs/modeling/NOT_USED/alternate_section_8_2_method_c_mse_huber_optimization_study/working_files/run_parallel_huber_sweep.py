import sys
import os
import math
import time
import json
import numpy as np
from scipy.optimize import differential_evolution, minimize
from concurrent.futures import ProcessPoolExecutor

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from benchmark_devices import BENCHMARK_DEVICES, T_MIN_BENCHMARK, T_MAX_BENCHMARK

PARAM_BOUNDS = [
    (0.00, 1.00),   # 0: eta_CCCV
    (0.00, 3.00),   # 1: C_thresh
    (0.00, 3.00),   # 2: s_low
    (0.00, 1.00),   # 3: eta_arch_single
    (0.00, 1.00),   # 4: eta_cp
    (0.00, 1.00),   # 5: eta_pps
    (0.00, 1.00),   # 6: eta_pd
    (0.00, 1.00),   # 7: eta_5v
    (0.00, 1.00),   # 8: eta_apple
    (0.00, 3.00),   # 9: k
    (0.00, 3.00),   # 10: p
]

PARAM_NAMES = [
    "eta_CCCV", "C_thresh", "s_low",
    "eta_arch_single", "eta_cp", "eta_pps", "eta_pd", "eta_5v", "eta_apple",
    "k", "p"
]

T_HANDSHAKE = 0.5000  # Fixed physical protocol handshake intercept (mins)

def predict_single(dev, params):
    eta_CCCV, C_thresh, s_low, eta_arch_single, eta_cp, eta_pps, eta_pd, eta_5v, eta_apple, k, p = params
    wh = dev["battery_wh"]
    p_peak = dev["peak_power_w"]
    arch = dev["architecture"]
    proto = dev["protocol"]
    
    C_rate = p_peak / wh
    
    # 1. CC/CV Efficiency
    if C_rate <= C_thresh:
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)
    else:
        eff_eta_CCCV = eta_CCCV
    eff_eta_CCCV = max(0.001, min(1.00, eff_eta_CCCV))
    
    # 2. Architecture Efficiency
    eta_arch = 1.0000 if arch == "dual" else eta_arch_single
    
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
        
    # 4. Thermal Decay Kinetics (Model B: Stretched Exponential Decay)
    if C_rate > C_thresh:
        diff = C_rate - C_thresh
        eta_thermal = math.exp(-k * (diff ** p))
    else:
        eta_thermal = 1.0000
    eta_thermal = max(0.001, min(1.00, eta_thermal))
    
    # 5. Effective Power
    p_eff = p_peak * eff_eta_CCCV * eta_arch * eta_proto * eta_thermal
    p_eff = max(0.01, min(p_peak, p_eff))
    
    # 6. Duration
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

def huber_loss_calc(r, delta):
    abs_r = abs(r)
    if abs_r <= delta:
        return 0.5 * (r ** 2)
    else:
        return delta * (abs_r - 0.5 * delta)

def loss_evaluator(params, loss_type="mse", delta=10.0):
    total = 0.0
    for dev in BENCHMARK_DEVICES:
        res = predict_single(dev, params)
        r = res["t_pred"] - dev["t_actual_min"]
        if loss_type == "mse":
            total += r ** 2
        elif loss_type == "mae":
            total += abs(r)
        elif loss_type == "huber":
            total += huber_loss_calc(r, delta)
    return total / len(BENCHMARK_DEVICES)

def compute_metrics(params):
    diffs_T = []
    diffs_S2 = []
    
    for dev in BENCHMARK_DEVICES:
        res = predict_single(dev, params)
        tp = res["t_pred"]
        ta = dev["t_actual_min"]
        sa = dev["s_actual"]
        
        dT = tp - ta
        diffs_T.append(dT)
        
        # Strategy 2 (aligned benchmark bounds [9.0, 241.0])
        s2 = 10.0 * (math.log(T_MAX_BENCHMARK / tp) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))
        s2 = min(10.0, max(0.0, s2))
        dS2 = s2 - sa
        diffs_S2.append(dS2)
        
    diffs_T = np.array(diffs_T)
    diffs_S2 = np.array(diffs_S2)
    
    mse_T = float(np.mean(diffs_T ** 2))
    rmse_T = float(np.sqrt(mse_T))
    mae_T = float(np.mean(np.abs(diffs_T)))
    mean_dT = float(np.mean(diffs_T))
    
    mae_S = float(np.mean(np.abs(diffs_S2)))
    mean_dS = float(np.mean(diffs_S2))
    
    return {
        "MSE_T": mse_T,
        "RMSE_T": rmse_T,
        "MAE_T": mae_T,
        "Mean_dT": mean_dT,
        "MAE_S": mae_S,
        "Mean_dS": mean_dS
    }

def run_single_opt(args):
    loss_type, delta = args
    # Run DE with seed=42, popsize=30, maxiter=2500, polish=True
    res = differential_evolution(
        loss_evaluator,
        bounds=PARAM_BOUNDS,
        args=(loss_type, delta),
        strategy='best1bin',
        maxiter=2500,
        popsize=30,
        tol=1e-8,
        seed=42,
        polish=True,
        workers=1
    )
    
    # Try a secondary L-BFGS-B polish to be 100% sure
    res_lbfgs = minimize(
        loss_evaluator,
        x0=res.x,
        args=(loss_type, delta),
        bounds=PARAM_BOUNDS,
        method='L-BFGS-B'
    )
    best_x = res_lbfgs.x if res_lbfgs.fun < res.fun else res.x
    best_fun = res_lbfgs.fun if res_lbfgs.fun < res.fun else res.fun
    
    m = compute_metrics(best_x)
    param_dict = {name: round(val, 4) for name, val in zip(PARAM_NAMES, best_x)}
    
    return {
        "loss_type": loss_type,
        "delta": delta,
        "loss_val": float(best_fun),
        "params": param_dict,
        "raw_params": [float(x) for x in best_x],
        "metrics": m
    }

def main():
    deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]
    tasks = [("huber", d) for d in deltas]
    
    print(f"Starting parallel execution of {len(tasks)} Huber tasks...")
    t0 = time.time()
    
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(run_single_opt, tasks))
        
    elapsed = time.time() - t0
    print(f"Completed in {elapsed:.2f} seconds.")
    
    print("\n--- RESULTS TABLE ---")
    for r in results:
        d = r["delta"]
        m = r["metrics"]
        print(f"| **`delta = {d:4.1f} mins`** | `{m['MSE_T']:6.2f} mins^2` | `{m['RMSE_T']:5.2f} mins` | `{m['MAE_T']:5.2f} mins` | `{m['Mean_dT']:+5.2f} mins` | `MAE_S = {m['MAE_S']:.4f} pts` |")
        
    with open("scratch/parallel_huber_sweep.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
