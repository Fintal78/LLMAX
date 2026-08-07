import math
import json
import random

from optimize_method_c import BENCHMARK_DEVICES
from generate_full_loss_based_study import PARAM_BOUNDS_LOSS, global_optimize, compute_t_metrics

print("=== EXTENDING HUBER DELTA SWEEP BEYOND 20 MINUTES ===")

deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0]
sweep_extended = []

for dv in deltas:
    pd, l_val = global_optimize("huber", PARAM_BOUNDS_LOSS, delta=dv, num_trials=50000, seed=int(dv*100))
    tm = compute_t_metrics(pd)
    sweep_extended.append({
        "delta": dv,
        "MSE_T": tm["MSE_T"],
        "RMSE_T": tm["RMSE_T"],
        "MAE_T": tm["MAE_T"],
        "Mean_dT": tm["Mean_dT"],
        "T_min_C": tm["T_min_C"],
        "T_max_C": tm["T_max_C"],
        "params": [round(x, 4) for x in pd],
    })
    print(f"  delta={dv:>5.1f} mins | MSE_T={tm['MSE_T']:>7.2f} | RMSE_T={tm['RMSE_T']:>6.2f} | MAE_T={tm['MAE_T']:>6.2f} | Mean_dT={tm['Mean_dT']:>+6.2f}")

with open("scratch/huber_sweep_extended.json", "w") as f:
    json.dump(sweep_extended, f, indent=2)

print("Extended sweep complete!")
