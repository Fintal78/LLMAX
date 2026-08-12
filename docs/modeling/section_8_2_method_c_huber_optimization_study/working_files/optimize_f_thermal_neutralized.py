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

def huber_loss(residual, delta):
    abs_res = np.abs(residual)
    if delta == 0.0:
        return abs_res
    elif abs_res <= delta:
        return 0.5 * (abs_res ** 2)
    else:
        return delta * abs_res - 0.5 * (delta ** 2)

def predict_time(d, eta_low, C0_single, C0_dual, k, p):
    C_rate = d["P_peak"] / d["E_supply"]
    f_th = 1.0000  # Neutralized
    f_skin = 1.0000
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

def objective(params, delta):
    eta_low, C0_single, C0_dual, k, p = params
    total_loss = 0.0
    for d in devices:
        T_pred = predict_time(d, eta_low, C0_single, C0_dual, k, p)
        res = T_pred - d["T_A"]
        total_loss += huber_loss(res, delta)
    return total_loss / len(devices)

bounds = [
    (0.50, 1.00),   # eta_low
    (0.00, 15.00),  # C0_single
    (0.00, 15.00),  # C0_dual
    (0.00, 10.00),  # k
    (0.01, 5.00)    # p
]

deltas = [0.0, 0.5, 1.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0, 30.0, 50.0, 100.0]

print("Running 5-Parameter Optimization Sweep (f_thermal = 1.0000 neutralized)...")
print(f"{'Delta':<18} | {'eta_low':<7} | {'C0_s':<6} | {'C0_d':<6} | {'k':<6} | {'p':<6} | {'Mean_dT':<7} | {'MAE_T':<6} | {'RMSE_T':<6} | {'MaxErr(m)':<9} | {'MaxErr(%)':<9}")
print("-" * 125)

sec3_rows = []
for delta in deltas:
    res = differential_evolution(objective, bounds=bounds, args=(delta,), seed=42, popsize=40, maxiter=1000)
    eta_low, C0_single, C0_dual, k, p = res.x
    
    errors_m = []
    errors_pct = []
    for d in devices:
        T_pred = predict_time(d, eta_low, C0_single, C0_dual, k, p)
        err_m = T_pred - d["T_A"]
        err_pct = (err_m / d["T_A"]) * 100.0
        errors_m.append(err_m)
        errors_pct.append(err_pct)
        
    arr_m = np.array(errors_m)
    arr_pct = np.array(errors_pct)
    
    mean_dt = np.mean(arr_m)
    mae_t = np.mean(np.abs(arr_m))
    rmse_t = np.sqrt(np.mean(arr_m ** 2))
    max_err_m = np.max(np.abs(arr_m))
    max_err_pct = np.max(np.abs(arr_pct))
    
    sec3_rows.append({
        "delta": delta, "eta": eta_low, "C0_s": C0_single, "C0_d": C0_dual,
        "k": k, "p": p, "mean_dt": mean_dt, "mae": mae_t, "rmse": rmse_t,
        "max_m": max_err_m, "max_pct": max_err_pct
    })
    
    delta_label = f"{delta:.1f}"
    if delta == 0.0: delta_label = "0.0 (Pure MAE)"
    elif delta == 20.0: delta_label = "20.0 (Primary)"
    elif delta == 100.0: delta_label = "100.0 (MSE-like)"
    
    print(f"{delta_label:<18} | {eta_low:<7.4f} | {C0_single:<6.4f} | {C0_dual:<6.4f} | {k:<6.4f} | {p:<6.4f} | {mean_dt:<+7.2f} | {mae_t:<6.2f} | {rmse_t:<6.2f} | {max_err_m:<9.2f} | {max_err_pct:<+8.1f}%")

# Save Section 5 per-device predictions under primary delta = 20.0
res_20 = [r for r in sec3_rows if r["delta"] == 20.0][0]
p20_eta, p20_c0s, p20_c0d, p20_k, p20_p = res_20["eta"], res_20["C0_s"], res_20["C0_d"], res_20["k"], res_20["p"]

sec5_lines = []
sec5_lines.append("| Smartphone Device Model      | Arch   | P_peak (W) | E_supply (Wh) | C_rate (h^-1) | P_eff (W) | F_system | `C0_effective` | `C0_base` | Benchmark `T_A` | Predicted `T_C` | Residual Error (`Delta`) | Error % |")
sec5_lines.append("| :--------------------------- | :----: | :--------: | :-----------: | :-----------: | :-------: | :------: | :------------: | :-------: | :-------------: | :-------------: | :----------------------: | :-----: |")

for d in devices:
    C_rate = d["P_peak"] / d["E_supply"]
    f_th = 1.0000
    C0_base = p20_c0d if d["arch"] == "Dual" else p20_c0s
    C0_eff = C0_base * f_th
    
    if C_rate <= C0_eff:
        F_sys = p20_eta
    else:
        denom = 1.0 + p20_k * ((C_rate - C0_eff) ** p20_p)
        F_sys = min(1.0, p20_eta / denom)
        
    P_eff = d["P_peak"] * F_sys
    T_pred = (d["E_supply"] / P_eff) * 60.0
    err_m = T_pred - d["T_A"]
    err_pct = (err_m / d["T_A"]) * 100.0
    
    sign_d = "+" if err_m > 0 else ""
    sign_p = "+" if err_pct > 0 else ""
    
    sec5_lines.append(f"| **{d['name']}** | {d['arch']} | {d['P_peak']:.1f} W | {d['E_supply']:.2f} Wh | {C_rate:.2f} | {P_eff:.1f} W | {F_sys:.4f} | {C0_eff:.4f} | {C0_base:.4f} | {d['T_A']:.1f} m | {T_pred:.1f} m | {sign_d}{err_m:.1f} m | {sign_p}{err_pct:.1f}% |")

sec5_table_md = "\n".join(sec5_lines)
with open("c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/modeling/section_8_2_method_c_huber_optimization_study/working_files/sec5_neutralized_table.md", "w", encoding="utf-8") as f:
    f.write(sec5_table_md)
