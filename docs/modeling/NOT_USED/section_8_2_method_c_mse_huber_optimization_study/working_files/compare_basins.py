import sys
import os
import math
import numpy as np
from scipy.optimize import minimize, differential_evolution

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from benchmark_devices import BENCHMARK_DEVICES, T_MIN_BENCHMARK, T_MAX_BENCHMARK
from verify_complete_document_alignment import predict_single, evaluate_model

BOUNDS = [
    (0.00, 1.00), # eta_CCCV
    (0.00, 3.00), # C_thresh
    (0.00, 3.00), # s_low
    (0.00, 1.00), # eta_arch_single
    (0.00, 1.00), # eta_cp
    (0.00, 1.00), # eta_pps
    (0.00, 1.00), # eta_pd
    (0.00, 1.00), # eta_5v
    (0.00, 1.00), # eta_apple
    (0.00, 3.00), # k
    (0.00, 3.00)  # p
]

def huber_loss_objective(params, delta):
    total = 0.0
    for dev in BENCHMARK_DEVICES:
        res = predict_single(dev, params)
        err = res["t_pred"] - dev["t_actual_min"]
        abs_err = abs(err)
        if abs_err <= delta:
            total += 0.5 * (err ** 2)
        else:
            total += delta * (abs_err - 0.5 * delta)
    return total / len(BENCHMARK_DEVICES)

deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]

# Basin A init (Pure MSE / Option 3 like)
init_A = [0.7533, 0.4026, 2.2493, 0.9688, 1.0000, 1.0000, 0.9043, 0.9938, 0.7196, 0.3933, 0.1808]
# Basin B init (Pure MAE / low eta_CCCV like)
init_B = [0.6172, 0.4474, 3.0000, 0.9972, 1.0000, 0.8653, 0.8276, 0.9723, 0.6344, 0.1013, 0.5638]

print(f"{'Delta':<6} | {'Basin A Loss':<12} | {'Basin A MSE_T':<13} | {'Basin A MAE_S':<13} | {'Basin B Loss':<12} | {'Basin B MSE_T':<13} | {'Basin B MAE_S':<13}")
print("-" * 95)

results = {}

for d in deltas:
    # Optimize in Basin A
    res_A = minimize(huber_loss_objective, init_A, args=(d,), method='L-BFGS-B', bounds=BOUNDS, options={'ftol': 1e-12, 'gtol': 1e-12, 'maxiter': 5000})
    # Optimize in Basin B
    res_B = minimize(huber_loss_objective, init_B, args=(d,), method='L-BFGS-B', bounds=BOUNDS, options={'ftol': 1e-12, 'gtol': 1e-12, 'maxiter': 5000})
    
    # Calculate metrics for A
    diffs_T_A = [predict_single(dev, res_A.x)["t_pred"] - dev["t_actual_min"] for dev in BENCHMARK_DEVICES]
    mse_T_A = float(np.mean(np.array(diffs_T_A)**2))
    mae_T_A = float(np.mean(np.abs(np.array(diffs_T_A))))
    rmse_T_A = math.sqrt(mse_T_A)
    mean_dT_A = float(np.mean(np.array(diffs_T_A)))
    
    diffs_S2_A = []
    for dev in BENCHMARK_DEVICES:
        tp = predict_single(dev, res_A.x)["t_pred"]
        sa = dev["s_actual"]
        s2 = min(10.0, max(0.0, 10.0 * (math.log(T_MAX_BENCHMARK / tp) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))))
        diffs_S2_A.append(s2 - sa)
    mae_S_A = float(np.mean(np.abs(np.array(diffs_S2_A))))
    
    # Calculate metrics for B
    diffs_T_B = [predict_single(dev, res_B.x)["t_pred"] - dev["t_actual_min"] for dev in BENCHMARK_DEVICES]
    mse_T_B = float(np.mean(np.array(diffs_T_B)**2))
    mae_T_B = float(np.mean(np.abs(np.array(diffs_T_B))))
    rmse_T_B = math.sqrt(mse_T_B)
    mean_dT_B = float(np.mean(np.array(diffs_T_B)))
    
    diffs_S2_B = []
    for dev in BENCHMARK_DEVICES:
        tp = predict_single(dev, res_B.x)["t_pred"]
        sa = dev["s_actual"]
        s2 = min(10.0, max(0.0, 10.0 * (math.log(T_MAX_BENCHMARK / tp) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))))
        diffs_S2_B.append(s2 - sa)
    mae_S_B = float(np.mean(np.abs(np.array(diffs_S2_B))))
    
    results[d] = {
        "A": {"loss": res_A.fun, "mse_T": mse_T_A, "rmse_T": rmse_T_A, "mae_T": mae_T_A, "mean_dT": mean_dT_A, "mae_S": mae_S_A, "params": res_A.x.tolist()},
        "B": {"loss": res_B.fun, "mse_T": mse_T_B, "rmse_T": rmse_T_B, "mae_T": mae_T_B, "mean_dT": mean_dT_B, "mae_S": mae_S_B, "params": res_B.x.tolist()}
    }
    
    print(f"{d:<6.1f} | {res_A.fun:<12.4f} | {mse_T_A:<13.2f} | {mae_S_A:<13.4f} | {res_B.fun:<12.4f} | {mse_T_B:<13.2f} | {mae_S_B:<13.4f}")

import json
with open("scratch/basin_comparison.json", "w") as f:
    json.dump(results, f, indent=2)
