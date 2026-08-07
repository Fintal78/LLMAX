import sys
import os
import math
import numpy as np
from scipy.optimize import minimize, differential_evolution

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from benchmark_devices import BENCHMARK_DEVICES, T_MIN_BENCHMARK, T_MAX_BENCHMARK
from verify_complete_document_alignment import predict_single

# Basin A bounds (realistic physical bounds around Basin A)
# eta_CCCV: [0.65, 0.85], C_thresh: [0.30, 0.60], s_low: [1.5, 2.8], etc.
BOUNDS_A = [
    (0.65, 0.85), # eta_CCCV
    (0.30, 0.60), # C_thresh
    (1.50, 2.80), # s_low
    (0.90, 1.00), # eta_arch_single
    (0.90, 1.00), # eta_cp
    (0.90, 1.00), # eta_pps
    (0.80, 1.00), # eta_pd
    (0.90, 1.00), # eta_5v
    (0.60, 0.85), # eta_apple
    (0.20, 0.60), # k
    (0.10, 0.40)  # p
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

print("Exact Independent Basin A Optimization Points across deltas:")
print(f"| {'Huber Threshold (`delta`)':<25} | {'`MSE_T` (`mins^2`)':<18} | {'`RMSE_T` (`mins`)':<17} | {'`MAE_T` (`mins`)':<16} | {'`Mean_dT` (`mins`)':<18} | {'Derived Score Metric (`Strategy 2`)':<35} |")
print("| :" + "-"*23 + " | :" + "-"*16 + ": | :" + "-"*15 + ": | :" + "-"*14 + ": | :" + "-"*16 + ": | :" + "-"*33 + " |")

for d in deltas:
    res = differential_evolution(
        huber_loss_objective,
        BOUNDS_A,
        args=(d,),
        seed=42,
        popsize=30,
        maxiter=2000,
        tol=1e-7,
        polish=True
    )
    p = res.x
    diffs_T = [predict_single(dev, p)["t_pred"] - dev["t_actual_min"] for dev in BENCHMARK_DEVICES]
    mse_T = float(np.mean(np.array(diffs_T)**2))
    rmse_T = math.sqrt(mse_T)
    mae_T = float(np.mean(np.abs(np.array(diffs_T))))
    mean_dT = float(np.mean(np.array(diffs_T)))
    
    diffs_S2 = []
    for dev in BENCHMARK_DEVICES:
        tp = predict_single(dev, p)["t_pred"]
        sa = dev["s_actual"]
        s2 = min(10.0, max(0.0, 10.0 * (math.log(T_MAX_BENCHMARK / tp) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))))
        diffs_S2.append(s2 - sa)
    mae_S = float(np.mean(np.abs(np.array(diffs_S2))))
    
    print(f"| **`delta = {d:4.1f} mins`**   |  `{mse_T:6.2f} mins^2`   |    `{rmse_T:5.2f} mins`   |   `{mae_T:5.2f} mins`   |    `{mean_dT:+5.2f} mins`    | `MAE_S = {mae_S:.4f} pts`                |")

