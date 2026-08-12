import numpy as np
from scipy.optimize import differential_evolution
import sys

sys.stdout.reconfigure(encoding='utf-8')

devices = [
    # --- DUAL-CELL 2S SERIES ULTRA FAST-CHARGERS ---
    {"name": "Realme GT3", "arch": "Dual", "P_peak": 240.0, "E_supply": 17.71, "T_A": 9.6, "vendor_T_limit": 40.0, "stability_pct": 63.5},
    {"name": "Redmi Note 12 Explorer", "arch": "Dual", "P_peak": 210.0, "E_supply": 16.56, "T_A": 9.0, "vendor_T_limit": 40.0, "stability_pct": 59.8},
    {"name": "iQOO 11 Pro", "arch": "Dual", "P_peak": 200.0, "E_supply": 18.10, "T_A": 12.0, "vendor_T_limit": 40.0, "stability_pct": 58.0},
    {"name": "Motorola Edge 50 Pro", "arch": "Dual", "P_peak": 125.0, "E_supply": 17.33, "T_A": 18.0, "vendor_T_limit": 40.0, "stability_pct": 99.1},
    {"name": "Xiaomi 13 Pro", "arch": "Dual", "P_peak": 120.0, "E_supply": 18.56, "T_A": 19.0, "vendor_T_limit": 40.0, "stability_pct": 68.2},
    {"name": "Xiaomi 12T Pro", "arch": "Dual", "P_peak": 120.0, "E_supply": 19.25, "T_A": 19.0, "vendor_T_limit": 40.0, "stability_pct": 62.4},
    {"name": "Poco F4 GT", "arch": "Dual", "P_peak": 120.0, "E_supply": 18.10, "T_A": 17.0, "vendor_T_limit": 40.0, "stability_pct": 53.0},
    {"name": "Vivo X100 Pro", "arch": "Dual", "P_peak": 100.0, "E_supply": 20.79, "T_A": 31.0, "vendor_T_limit": 40.0, "stability_pct": 52.6},
    {"name": "OnePlus 12", "arch": "Dual", "P_peak": 100.0, "E_supply": 20.79, "T_A": 26.0, "vendor_T_limit": 40.0, "stability_pct": 55.4},
    {"name": "OnePlus 11", "arch": "Dual", "P_peak": 100.0, "E_supply": 19.25, "T_A": 25.0, "vendor_T_limit": 40.0, "stability_pct": 54.1},
    {"name": "OnePlus 12R", "arch": "Dual", "P_peak": 80.0, "E_supply": 21.17, "T_A": 32.0, "vendor_T_limit": 40.0, "stability_pct": 65.5},
    {"name": "Asus ROG Phone 7", "arch": "Dual", "P_peak": 65.0, "E_supply": 23.10, "T_A": 42.0, "vendor_T_limit": 40.0, "stability_pct": 79.2},

    # --- SINGLE-CELL 1S HIGH-END & MID-RANGE ANDROID ---
    {"name": "Xiaomi 14", "arch": "Single", "P_peak": 90.0, "E_supply": 17.71, "T_A": 35.0, "vendor_T_limit": 40.0, "stability_pct": 58.5},
    {"name": "Honor Magic 6 Pro", "arch": "Single", "P_peak": 80.0, "E_supply": 21.56, "T_A": 36.0, "vendor_T_limit": 40.0, "stability_pct": 64.0},
    {"name": "Motorola Edge 40", "arch": "Single", "P_peak": 68.0, "E_supply": 17.33, "T_A": 44.0, "vendor_T_limit": 40.0, "stability_pct": 78.5},
    {"name": "Xiaomi 13", "arch": "Single", "P_peak": 67.0, "E_supply": 17.33, "T_A": 42.0, "vendor_T_limit": 40.0, "stability_pct": 72.0},
    {"name": "Honor Magic 5 Pro", "arch": "Single", "P_peak": 66.0, "E_supply": 19.64, "T_A": 48.0, "vendor_T_limit": 40.0, "stability_pct": 68.0},
    {"name": "Samsung Galaxy S24 Ultra", "arch": "Single", "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0, "vendor_T_limit": 40.0, "stability_pct": 59.0},
    {"name": "Samsung Galaxy S23 Ultra", "arch": "Single", "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0, "vendor_T_limit": 40.0, "stability_pct": 58.2},
    {"name": "Samsung Galaxy S22 Ultra", "arch": "Single", "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0, "vendor_T_limit": 40.0, "stability_pct": 54.8},
    {"name": "Nothing Phone (2)", "arch": "Single", "P_peak": 45.0, "E_supply": 18.10, "T_A": 55.0, "vendor_T_limit": 40.0, "stability_pct": 72.1},
    {"name": "Google Pixel 9 Pro XL", "arch": "Single", "P_peak": 37.0, "E_supply": 19.48, "T_A": 79.0, "vendor_T_limit": 40.0, "stability_pct": 58.0},
    {"name": "Google Pixel 8 Pro", "arch": "Single", "P_peak": 30.0, "E_supply": 19.44, "T_A": 81.0, "vendor_T_limit": 40.0, "stability_pct": 53.5},
    {"name": "Samsung Galaxy S24", "arch": "Single", "P_peak": 25.0, "E_supply": 15.40, "T_A": 75.0, "vendor_T_limit": 40.0, "stability_pct": 58.4},
    {"name": "Samsung Galaxy S23", "arch": "Single", "P_peak": 25.0, "E_supply": 15.02, "T_A": 80.0, "vendor_T_limit": 40.0, "stability_pct": 62.1},
    {"name": "Samsung Galaxy A55", "arch": "Single", "P_peak": 25.0, "E_supply": 19.25, "T_A": 85.0, "vendor_T_limit": 40.0, "stability_pct": 99.4},
    {"name": "Samsung Galaxy A54", "arch": "Single", "P_peak": 25.0, "E_supply": 19.25, "T_A": 82.0, "vendor_T_limit": 40.0, "stability_pct": 99.2},
    {"name": "Samsung Galaxy A34", "arch": "Single", "P_peak": 25.0, "E_supply": 19.25, "T_A": 84.0, "vendor_T_limit": 40.0, "stability_pct": 99.3},
    {"name": "Google Pixel 7 Pro", "arch": "Single", "P_peak": 23.0, "E_supply": 19.25, "T_A": 109.0, "vendor_T_limit": 40.0, "stability_pct": 64.2},
    {"name": "Samsung Galaxy S10", "arch": "Single", "P_peak": 15.0, "E_supply": 13.09, "T_A": 108.0, "vendor_T_limit": 40.0, "stability_pct": 74.5},
    {"name": "Samsung Galaxy S9", "arch": "Single", "P_peak": 15.0, "E_supply": 11.55, "T_A": 107.0, "vendor_T_limit": 40.0, "stability_pct": 78.0},
    {"name": "Samsung Galaxy S8", "arch": "Single", "P_peak": 15.0, "E_supply": 11.55, "T_A": 100.0, "vendor_T_limit": 40.0, "stability_pct": 82.0},
    {"name": "Nokia 2.4", "arch": "Single", "P_peak": 5.0, "E_supply": 17.33, "T_A": 215.0, "vendor_T_limit": 40.0, "stability_pct": 99.8},
    {"name": "Samsung Galaxy A03 Core", "arch": "Single", "P_peak": 7.8, "E_supply": 19.25, "T_A": 205.0, "vendor_T_limit": 40.0, "stability_pct": 99.6},

    # --- APPLE IPHONES & LG ---
    {"name": "Apple iPhone 16 Pro Max", "arch": "Single", "P_peak": 30.0, "E_supply": 18.04, "T_A": 117.0, "vendor_T_limit": 35.0, "stability_pct": 68.0},
    {"name": "Apple iPhone 14 Pro Max", "arch": "Single", "P_peak": 29.0, "E_supply": 16.64, "T_A": 112.0, "vendor_T_limit": 35.0, "stability_pct": 68.4},
    {"name": "Apple iPhone 15 Pro Max", "arch": "Single", "P_peak": 27.0, "E_supply": 17.02, "T_A": 109.0, "vendor_T_limit": 35.0, "stability_pct": 65.8},
    {"name": "Apple iPhone 13 Pro Max", "arch": "Single", "P_peak": 27.0, "E_supply": 16.75, "T_A": 106.0, "vendor_T_limit": 35.0, "stability_pct": 73.5},
    {"name": "Apple iPhone 11 Pro Max", "arch": "Single", "P_peak": 18.0, "E_supply": 15.04, "T_A": 120.0, "vendor_T_limit": 35.0, "stability_pct": 75.0},
    {"name": "LG G7 ThinQ", "arch": "Single", "P_peak": 18.0, "E_supply": 11.55, "T_A": 108.0, "vendor_T_limit": 35.0, "stability_pct": 61.2},
    {"name": "Apple iPhone XS Max", "arch": "Single", "P_peak": 15.0, "E_supply": 12.08, "T_A": 131.0, "vendor_T_limit": 35.0, "stability_pct": 72.0},
    {"name": "Apple iPhone X", "arch": "Single", "P_peak": 15.0, "E_supply": 10.43, "T_A": 125.0, "vendor_T_limit": 35.0, "stability_pct": 70.0},
    {"name": "Apple iPhone 8", "arch": "Single", "P_peak": 5.0, "E_supply": 7.01, "T_A": 148.0, "vendor_T_limit": 35.0, "stability_pct": 85.0},
    {"name": "Apple iPhone 7 Plus", "arch": "Single", "P_peak": 5.0, "E_supply": 11.17, "T_A": 241.0, "vendor_T_limit": 35.0, "stability_pct": 88.0}
]

for d in devices:
    d["base_power_ratio"] = (d["stability_pct"] / 100.0) ** 3

def predict_time(d, eta_low, C0_single, C0_dual, k, p, alpha):
    C_rate = d["P_peak"] / d["E_supply"]
    f_th = (d["base_power_ratio"]) ** alpha
    f_skin = 1.0
    C0_base = C0_dual if d["arch"] == "Dual" else C0_single
    C0_eff = C0_base * f_th * f_skin
    
    if C_rate <= C0_eff:
        F_sys = eta_low
    else:
        denom = 1.0 + k * ((C_rate - C0_eff) ** p)
        F_sys = min(1.0, eta_low / denom)
        
    P_eff = d["P_peak"] * F_sys
    T_pred = (d["E_supply"] / P_eff) * 60.0
    return T_pred

delta = 100.0

def objective_5param(params):
    eta_low, C0_single, C0_dual, k, p = params
    alpha = 1.0
    total_loss = 0.0
    for d in devices:
        res = predict_time(d, eta_low, C0_single, C0_dual, k, p, alpha) - d["T_A"]
        total_loss += 0.5 * (res ** 2)
    return total_loss / len(devices)

def objective_6param(params):
    eta_low, C0_single, C0_dual, k, p, alpha = params
    total_loss = 0.0
    for d in devices:
        res = predict_time(d, eta_low, C0_single, C0_dual, k, p, alpha) - d["T_A"]
        total_loss += 0.5 * (res ** 2)
    return total_loss / len(devices)

print("Running optimization for Delta = 100.0 (MSE regime)...")

bounds_5 = [(0.50, 1.00), (0.00, 15.00), (0.00, 15.00), (0.00, 10.00), (0.01, 5.00)]
res_5 = differential_evolution(objective_5param, bounds=bounds_5, seed=42, popsize=40, maxiter=1000)

bounds_6 = [(0.50, 1.00), (0.00, 15.00), (0.00, 15.00), (0.00, 10.00), (0.01, 5.00), (0.10, 5.00)]
res_6 = differential_evolution(objective_6param, bounds=bounds_6, seed=42, popsize=40, maxiter=1000)

def evaluate(params, is_6param=True):
    if is_6param:
        eta_low, C0_s, C0_d, k, p, alpha = params
    else:
        eta_low, C0_s, C0_d, k, p = params
        alpha = 1.0
        
    errors_m = []
    errors_pct = []
    dev_names = []
    
    for d in devices:
        T_pred = predict_time(d, eta_low, C0_s, C0_d, k, p, alpha)
        err_m = T_pred - d["T_A"]
        err_pct = (err_m / d["T_A"]) * 100.0
        errors_m.append(err_m)
        errors_pct.append(err_pct)
        dev_names.append(d["name"])
        
    arr_m = np.array(errors_m)
    arr_pct = np.array(errors_pct)
    
    mean_dt = np.mean(arr_m)
    mae = np.mean(np.abs(arr_m))
    rmse = np.sqrt(np.mean(arr_m ** 2))
    
    abs_m = np.abs(arr_m)
    idx_m = np.argmax(abs_m)
    max_m = abs_m[idx_m]
    dev_max_m = dev_names[idx_m]
    
    abs_pct = np.abs(arr_pct)
    idx_pct = np.argmax(abs_pct)
    max_pct = abs_pct[idx_pct]
    dev_max_pct = dev_names[idx_pct]
    
    return {
        "eta": eta_low, "C0_s": C0_s, "C0_d": C0_d, "k": k, "p": p, "alpha": alpha,
        "mean_dt": mean_dt, "mae": mae, "rmse": rmse,
        "max_m": max_m, "dev_max_m": dev_max_m,
        "max_pct": max_pct, "dev_max_pct": dev_max_pct
    }

eval_5 = evaluate(res_5.x, is_6param=False)
eval_6 = evaluate(res_6.x, is_6param=True)

print("\n=== RESULTS FOR DELTA = 100.0 (MSE / L2 LOSS REGIME) ===")
print("Metric                    | 5-Parameter (alpha=1.0) | 6-Parameter (alpha free)")
print("-" * 75)
print(f"Calibrated alpha         | 1.0000 (fixed)          | {eval_6['alpha']:.4f}")
print(f"eta_low                   | {eval_5['eta']:.4f}                  | {eval_6['eta']:.4f}")
print(f"C0_single (h^-1)          | {eval_5['C0_s']:.4f}                  | {eval_6['C0_s']:.4f}")
print(f"C0_dual (h^-1)            | {eval_5['C0_d']:.4f}                  | {eval_6['C0_d']:.4f}")
print(f"k                         | {eval_5['k']:.4f}                  | {eval_6['k']:.4f}")
print(f"p                         | {eval_5['p']:.4f}                  | {eval_6['p']:.4f}")
print(f"Mean_dT (mins)            | {eval_5['mean_dt']:<+7.2f}                 | {eval_6['mean_dt']:<+7.2f}")
print(f"MAE_T (mins)              | {eval_5['mae']:<6.2f}                 | {eval_6['mae']:<6.2f}")
print(f"RMSE_T (mins)             | {eval_5['rmse']:<6.2f}                 | {eval_6['rmse']:<6.2f}")
print(f"Max Error (mins)          | {eval_5['max_m']:<6.2f} ({eval_5['dev_max_m']}) | {eval_6['max_m']:<6.2f} ({eval_6['dev_max_m']})")
print(f"Max Error (%)             | +{eval_5['max_pct']:<5.1f}% ({eval_5['dev_max_pct']}) | +{eval_6['max_pct']:<5.1f}% ({eval_6['dev_max_pct']})")
