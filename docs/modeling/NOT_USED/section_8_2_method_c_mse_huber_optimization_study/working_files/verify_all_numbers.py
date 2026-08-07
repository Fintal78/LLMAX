import math
import numpy as np
from benchmark_devices import BENCHMARK_DEVICES

# Baseline parameter set
params_baseline = {
    "eta_CCCV": 0.7200, "C_threshold": 1.5000, "s_low": 0.1500,
    "eta_arch_single": 0.9400, "eta_proto_cp": 0.9800, "eta_proto_pps": 0.9500,
    "eta_proto_fpd": 0.9100, "eta_proto_5v": 0.8300, "eta_proto_app": 0.8800,
    "k": 0.2000, "p": 0.4500, "T_handshake": 0.5000
}

# Opt 1: Pure MSE
params_opt1 = {
    "eta_CCCV": 0.7536, "C_threshold": 0.4026, "s_low": 2.2398,
    "eta_arch_single": 0.9822, "eta_proto_cp": 1.0000, "eta_proto_pps": 0.9905,
    "eta_proto_fpd": 0.8755, "eta_proto_5v": 0.9783, "eta_proto_app": 0.7206,
    "k": 0.3969, "p": 0.1982, "T_handshake": 0.5000
}

# Opt 2: Pure MAE
params_opt2 = {
    "eta_CCCV": 0.6172, "C_threshold": 0.4474, "s_low": 3.0000,
    "eta_arch_single": 0.9972, "eta_proto_cp": 1.0000, "eta_proto_pps": 0.8653,
    "eta_proto_fpd": 0.8276, "eta_proto_5v": 0.9723, "eta_proto_app": 0.6344,
    "k": 0.1013, "p": 0.5638, "T_handshake": 0.5000
}

# Opt 3: Huber delta=10
params_opt3 = {
    "eta_CCCV": 0.7533, "C_threshold": 0.4026, "s_low": 2.2493,
    "eta_arch_single": 0.9688, "eta_proto_cp": 1.0000, "eta_proto_pps": 1.0000,
    "eta_proto_fpd": 0.9043, "eta_proto_5v": 0.9938, "eta_proto_app": 0.7196,
    "k": 0.3933, "p": 0.1808, "T_handshake": 0.5000
}

def predict_T_C(d, p):
    Wh = d["battery_wh"]
    P_peak = d["peak_power_w"]
    arch = d["architecture"]
    proto = d["protocol"]
    
    C_rate = P_peak / Wh
    if C_rate > p["C_threshold"]:
        eff_eta_CCCV = p["eta_CCCV"]
    else:
        eff_eta_CCCV = min(1.0, p["eta_CCCV"] + p["s_low"] * (p["C_threshold"] - C_rate))
    
    eta_arch = 1.0 if arch == "dual" else p["eta_arch_single"]
    
    proto_map = {
        "charge_pump": p["eta_proto_cp"],
        "pps": p["eta_proto_pps"],
        "fixed_pd": p["eta_proto_fpd"],
        "legacy_5v": p["eta_proto_5v"],
        "apple_legacy": p["eta_proto_app"]
    }
    eta_proto = proto_map[proto]
    
    if C_rate > p["C_threshold"]:
        eta_thermal = math.exp(-p["k"] * ((C_rate - p["C_threshold"]) ** p["p"]))
    else:
        eta_thermal = 1.0
        
    P_eff = P_peak * eff_eta_CCCV * eta_arch * eta_proto * eta_thermal
    T_pred = (Wh / P_eff) * 60.0 + p["T_handshake"]
    return T_pred

models = {
    "Baseline Model": params_baseline,
    "Opt 1: Pure MSE Model": params_opt1,
    "Opt 2: Pure MAE Model": params_opt2,
    "Opt 3: Huber Model (delta=10.0)": params_opt3
}

print("=== Extreme Bounds (T_min,C and T_max,C) ===")
for name, p in models.items():
    T_preds = [predict_T_C(d, p) for d in BENCHMARK_DEVICES]
    min_idx = np.argmin(T_preds)
    max_idx = np.argmax(T_preds)
    print(f"{name}:")
    print(f"  T_min,C = {T_preds[min_idx]:.2f} mins ({BENCHMARK_DEVICES[min_idx]['name']}: {BENCHMARK_DEVICES[min_idx]['peak_power_w']}W)")
    print(f"  T_max,C = {T_preds[max_idx]:.2f} mins ({BENCHMARK_DEVICES[max_idx]['name']}: {BENCHMARK_DEVICES[max_idx]['peak_power_w']}W)")

print("\n=== Duration Metrics (dT = T_C - T_A) ===")
for name, p in models.items():
    T_preds = np.array([predict_T_C(d, p) for d in BENCHMARK_DEVICES])
    T_A = np.array([d["t_actual_min"] for d in BENCHMARK_DEVICES])
    dT = T_preds - T_A
    mse_t = np.mean(dT ** 2)
    rmse_t = np.sqrt(mse_t)
    mae_t = np.mean(np.abs(dT))
    mean_dt = np.mean(dT)
    print(f"{name}: MSE_T = {mse_t:.2f}, RMSE_T = {rmse_t:.2f}, MAE_T = {mae_t:.2f}, Mean_dT = {mean_dt:+.2f}")

print("\n=== Score Normalization Metrics (dS = S_C - S_A) ===")
for name, p in models.items():
    T_preds = np.array([predict_T_C(d, p) for d in BENCHMARK_DEVICES])
    T_min_C = np.min(T_preds)
    T_max_C = np.max(T_preds)
    S_A = np.array([d["s_actual"] for d in BENCHMARK_DEVICES])
    
    # Strategy 1: Dynamic Bounds
    S_C_strat1 = 10.0 * (np.log(T_max_C / T_preds) / np.log(T_max_C / T_min_C))
    dS_strat1 = S_C_strat1 - S_A
    mse_s_1 = np.mean(dS_strat1 ** 2)
    rmse_s_1 = np.sqrt(mse_s_1)
    mae_s_1 = np.mean(np.abs(dS_strat1))
    mean_ds_1 = np.mean(dS_strat1)
    
    # Strategy 2: Benchmark Aligned Bounds [9.0, 241.0] with clipping [0.0, 10.0]
    raw_strat2 = 10.0 * (np.log(241.0 / T_preds) / np.log(241.0 / 9.0))
    S_C_strat2 = np.clip(raw_strat2, 0.0, 10.0)
    dS_strat2 = S_C_strat2 - S_A
    mse_s_2 = np.mean(dS_strat2 ** 2)
    rmse_s_2 = np.sqrt(mse_s_2)
    mae_s_2 = np.mean(np.abs(dS_strat2))
    mean_ds_2 = np.mean(dS_strat2)
    
    print(f"\n{name}:")
    print(f"  Strategy 1: MSE_S = {mse_s_1:.4f} pts^2, RMSE_S = {rmse_s_1:.4f} pts, MAE_S = {mae_s_1:.4f} pts, Mean_dS = {mean_ds_1:+.4f} pts")
    print(f"  Strategy 2: MSE_S = {mse_s_2:.4f} pts^2, RMSE_S = {rmse_s_2:.4f} pts, MAE_S = {mae_s_2:.4f} pts, Mean_dS = {mean_ds_2:+.4f} pts")
