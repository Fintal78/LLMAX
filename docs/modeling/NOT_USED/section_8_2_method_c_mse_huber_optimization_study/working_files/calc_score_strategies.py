import math
import numpy as np

# 44 devices benchmark data from scoring_rules / study
devices = [
    # name, Wh, P_peak, T_A, S_A, arch, proto
    ("Realme GT3", 17.71, 240.0, 9.6, 9.80, "dual", "charge_pump"),
    ("Redmi Note 12 Explorer", 16.56, 210.0, 9.0, 10.00, "dual", "charge_pump"),
    ("iQOO 11 Pro", 18.10, 200.0, 12.0, 9.12, "dual", "charge_pump"),
    ("Motorola Edge 50 Pro", 17.33, 125.0, 18.0, 7.89, "single", "charge_pump"),
    ("Xiaomi 13 Pro", 18.56, 120.0, 19.0, 7.73, "dual", "charge_pump"),
    ("Xiaomi 12T Pro", 19.25, 120.0, 19.0, 7.73, "dual", "charge_pump"),
    ("Poco F4 GT", 18.10, 120.0, 17.0, 8.07, "dual", "charge_pump"),
    ("Vivo X100 Pro", 20.79, 100.0, 31.0, 6.24, "dual", "charge_pump"),
    ("OnePlus 12", 20.79, 100.0, 26.0, 6.77, "dual", "charge_pump"),
    ("OnePlus 11", 19.25, 100.0, 25.0, 6.89, "dual", "charge_pump"),
    ("Xiaomi 14", 17.71, 90.0, 35.0, 5.87, "single", "charge_pump"),
    ("Honor Magic 6 Pro", 21.56, 80.0, 36.0, 5.78, "single", "pps"),
    ("OnePlus 12R", 21.17, 80.0, 32.0, 6.14, "single", "charge_pump"),
    ("Motorola Edge 40", 17.33, 68.0, 44.0, 5.17, "single", "pps"),
    ("Xiaomi 13", 17.33, 67.0, 42.0, 5.31, "single", "pps"),
    ("Honor Magic 5 Pro", 19.64, 66.0, 48.0, 4.91, "single", "pps"),
    ("Asus ROG Phone 7", 23.10, 65.0, 42.0, 5.31, "single", "pps"),
    ("Samsung Galaxy S24 Ultra", 19.25, 45.0, 59.0, 4.28, "single", "pps"),
    ("Samsung Galaxy S23 Ultra", 19.25, 45.0, 59.0, 4.28, "single", "pps"),
    ("Samsung Galaxy S22 Ultra", 19.25, 45.0, 59.0, 4.28, "single", "pps"),
    ("Nothing Phone (2)", 18.10, 45.0, 55.0, 4.49, "single", "pps"),
    ("Google Pixel 9 Pro XL", 19.25, 37.0, 79.0, 3.39, "single", "pps"),
    ("Google Pixel 8 Pro", 19.25, 30.0, 81.0, 3.32, "single", "pps"),
    ("Apple iPhone 16 Pro Max", 18.04, 30.0, 107.0, 2.47, "single", "apple_legacy"),
    ("Apple iPhone 14 Pro Max", 16.64, 29.0, 112.0, 2.33, "single", "apple_legacy"),
    ("Apple iPhone 15 Pro Max", 17.10, 27.0, 109.0, 2.41, "single", "apple_legacy"),
    ("Apple iPhone 13 Pro Max", 16.75, 27.0, 106.0, 2.50, "single", "apple_legacy"),
    ("Samsung Galaxy S24", 15.40, 25.0, 75.0, 3.55, "single", "pps"),
    ("Samsung Galaxy S23", 15.02, 25.0, 72.0, 3.67, "single", "pps"),
    ("Samsung Galaxy A55", 19.25, 25.0, 85.0, 3.17, "single", "pps"),
    ("Samsung Galaxy A54", 19.25, 25.0, 82.0, 3.28, "single", "pps"),
    ("Samsung Galaxy A34", 19.25, 25.0, 84.0, 3.21, "single", "pps"),
    ("Google Pixel 7 Pro", 19.25, 23.0, 109.0, 2.41, "single", "pps"),
    ("Apple iPhone 11 Pro Max", 15.04, 18.0, 120.0, 2.12, "single", "apple_legacy"),
    ("LG G7 ThinQ", 11.55, 18.0, 108.0, 2.44, "single", "fixed_pd"),
    ("Apple iPhone XS Max", 12.08, 15.0, 131.0, 1.85, "single", "apple_legacy"),
    ("Apple iPhone X", 10.43, 15.0, 125.0, 2.00, "single", "apple_legacy"),
    ("Samsung Galaxy S10", 13.09, 15.0, 108.0, 2.44, "single", "fixed_pd"),
    ("Samsung Galaxy S9", 11.55, 15.0, 107.0, 2.47, "single", "fixed_pd"),
    ("Samsung Galaxy S8", 11.55, 15.0, 100.0, 2.68, "single", "fixed_pd"),
    ("Apple iPhone 8", 7.01, 5.0, 148.0, 1.48, "single", "legacy_5v"),
    ("Apple iPhone 7 Plus", 11.17, 5.0, 241.0, 0.00, "single", "legacy_5v"),
    ("Nokia 2.4", 17.33, 5.0, 215.0, 0.35, "single", "legacy_5v"),
    ("Samsung Galaxy A03 Core", 19.25, 7.8, 205.0, 0.49, "single", "legacy_5v")
]

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

def predict_T_C(dev, p):
    name, Wh, P_peak, T_A, S_A, arch, proto = dev
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
    T_preds = [predict_T_C(d, p) for d in devices]
    min_idx = np.argmin(T_preds)
    max_idx = np.argmax(T_preds)
    print(f"{name}:")
    print(f"  T_min,C = {T_preds[min_idx]:.2f} mins ({devices[min_idx][0]}: {devices[min_idx][2]}W)")
    print(f"  T_max,C = {T_preds[max_idx]:.2f} mins ({devices[max_idx][0]}: {devices[max_idx][2]}W)")

print("\n=== Strategy 1 vs Strategy 2 Metrics ===")
for name, p in models.items():
    T_preds = np.array([predict_T_C(d, p) for d in devices])
    T_min_C = np.min(T_preds)
    T_max_C = np.max(T_preds)
    
    S_A = np.array([d[4] for d in devices])
    
    # Strategy 1: Dynamic Bounds
    # S_C = 10 * log(T_max_C / T_C) / log(T_max_C / T_min_C)
    S_C_strat1 = 10.0 * (np.log(T_max_C / T_preds) / np.log(T_max_C / T_min_C))
    dS_strat1 = S_C_strat1 - S_A
    mse_s_1 = np.mean(dS_strat1 ** 2)
    rmse_s_1 = np.sqrt(mse_s_1)
    mae_s_1 = np.mean(np.abs(dS_strat1))
    mean_ds_1 = np.mean(dS_strat1)
    
    # Strategy 2: Benchmark Aligned Bounds (9.0, 241.0 with clamping)
    # S_C = min(10, max(0, 10 * log(241.0 / T_C) / log(241.0 / 9.0)))
    raw_strat2 = 10.0 * (np.log(241.0 / T_preds) / np.log(241.0 / 9.0))
    S_C_strat2 = np.clip(raw_strat2, 0.0, 10.0)
    dS_strat2 = S_C_strat2 - S_A
    mse_s_2 = np.mean(dS_strat2 ** 2)
    rmse_s_2 = np.sqrt(mse_s_2)
    mae_s_2 = np.mean(np.abs(dS_strat2))
    mean_ds_2 = np.mean(dS_strat2)
    
    print(f"\n{name}:")
    print(f"  Strategy 1: MSE_S = {mse_s_1:.4f}, RMSE_S = {rmse_s_1:.4f}, MAE_S = {mae_s_1:.4f}, Mean_dS = {mean_ds_1:+.4f}")
    print(f"  Strategy 2: MSE_S = {mse_s_2:.4f}, RMSE_S = {rmse_s_2:.4f}, MAE_S = {mae_s_2:.4f}, Mean_dS = {mean_ds_2:+.4f}")
