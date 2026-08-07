import sys
import os
import math
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from benchmark_devices import BENCHMARK_DEVICES
from verify_complete_document_alignment import predict_single

params_huber_10 = [0.7533, 0.4026, 2.2493, 0.9688, 1.0000, 1.0000, 0.9043, 0.9938, 0.7196, 0.3933, 0.1808]
params_pure_mse = [0.7536, 0.4026, 2.2398, 0.9822, 1.0000, 0.9905, 0.8755, 0.9783, 0.7206, 0.3969, 0.1982]

errors_huber = []
errors_mse = []

for dev in BENCHMARK_DEVICES:
    res_h = predict_single(dev, params_huber_10)
    err_h = res_h["t_pred"] - dev["t_actual_min"]
    errors_huber.append((dev["name"], dev["t_actual_min"], res_h["t_pred"], err_h, abs(err_h)))
    
    res_m = predict_single(dev, params_pure_mse)
    err_m = res_m["t_pred"] - dev["t_actual_min"]
    errors_mse.append((dev["name"], dev["t_actual_min"], res_m["t_pred"], err_m, abs(err_m)))

errors_huber.sort(key=lambda x: x[4], reverse=True)
errors_mse.sort(key=lambda x: x[4], reverse=True)

print("Top 10 Largest Residuals under Huber delta=10.0:")
for dev, t_act, t_pred, err, abs_err in errors_huber[:10]:
    print(f"  {dev:<30}: T_actual = {t_act:5.1f} min | T_pred = {t_pred:5.1f} min | residual dT = {err:+6.2f} min | abs_err = {abs_err:5.2f} min")

print("\nTop 10 Largest Residuals under Pure MSE:")
for dev, t_act, t_pred, err, abs_err in errors_mse[:10]:
    print(f"  {dev:<30}: T_actual = {t_act:5.1f} min | T_pred = {t_pred:5.1f} min | residual dT = {err:+6.2f} min | abs_err = {abs_err:5.2f} min")
