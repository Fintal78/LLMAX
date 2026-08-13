import math
import json

from optimize_method_c import BENCHMARK_DEVICES
from sync_huber_25_study_data import PARAM_BOUNDS_LOSS, global_optimize, compute_t_metrics

print("Evaluating delta = 22.5 mins and delta = 27.5 mins...")

for dv in [22.5, 27.5]:
    pd, _ = global_optimize("huber", PARAM_BOUNDS_LOSS, delta=dv, num_trials=60000, seed=int(dv*100))
    tm = compute_t_metrics(pd)
    print(f"delta = {dv:>4.1f} mins: MSE_T = {tm['MSE_T']:>6.2f} mins^2 | RMSE_T = {tm['RMSE_T']:>5.2f} mins | MAE_T = {tm['MAE_T']:>4.2f} mins | Mean_dT = {tm['Mean_dT']:>+5.2f} mins")
