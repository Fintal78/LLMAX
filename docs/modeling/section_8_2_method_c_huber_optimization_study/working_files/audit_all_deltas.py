import numpy as np

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
    d["power_ratio"] = (d["stability_pct"] / 100.0) ** 3

# Sweep results from recalibration with delta sweep:
sweep_params = [
    {"delta": 0.0,  "name": "0.0 (Pure MAE)", "eta": 0.9673, "C0_s": 0.4029, "C0_d": 4.7127, "k": 1.0371, "p": 0.2261},
    {"delta": 0.5,  "name": "0.5",            "eta": 0.9673, "C0_s": 0.4034, "C0_d": 4.6212, "k": 1.0333, "p": 0.2221},
    {"delta": 1.0,  "name": "1.0",            "eta": 0.9674, "C0_s": 0.4032, "C0_d": 4.6944, "k": 1.0387, "p": 0.2245},
    {"delta": 2.5,  "name": "2.5",            "eta": 0.9676, "C0_s": 0.4026, "C0_d": 4.8238, "k": 1.0482, "p": 0.2299},
    {"delta": 5.0,  "name": "5.0",            "eta": 0.9679, "C0_s": 0.4021, "C0_d": 4.9126, "k": 1.0576, "p": 0.2347},
    {"delta": 7.5,  "name": "7.5",            "eta": 0.9681, "C0_s": 0.4012, "C0_d": 4.9815, "k": 1.0686, "p": 0.2429},
    {"delta": 10.0, "name": "10.0",           "eta": 0.9682, "C0_s": 0.3997, "C0_d": 4.9985, "k": 1.0778, "p": 0.2531},
    {"delta": 15.0, "name": "15.0",           "eta": 0.9683, "C0_s": 0.3965, "C0_d": 5.0235, "k": 1.0943, "p": 0.2735},
    {"delta": 20.0, "name": "20.0 (Primary)", "eta": 0.9687, "C0_s": 0.3943, "C0_d": 5.0649, "k": 1.1188, "p": 0.2893},
    {"delta": 30.0, "name": "30.0",           "eta": 0.9692, "C0_s": 0.3933, "C0_d": 5.1037, "k": 1.1437, "p": 0.2993},
    {"delta": 50.0, "name": "50.0",           "eta": 0.9692, "C0_s": 0.3933, "C0_d": 5.1049, "k": 1.1444, "p": 0.2996},
    {"delta": 100.0,"name": "100.0 (MSE-like)","eta": 0.9692, "C0_s": 0.3933, "C0_d": 5.1048, "k": 1.1444, "p": 0.2996}
]

print(f"{'Delta':<18} | {'eta_low':<7} | {'C0_s':<6} | {'C0_d':<6} | {'k':<6} | {'p':<6} | {'Mean_dT':<7} | {'MAE_T':<6} | {'RMSE_T':<6} | {'MaxErr(m)':<9} | {'MaxErr(m) Dev':<22} | {'MaxErr(%)':<9} | {'MaxErr(%) Dev':<22}")
print("-" * 155)

for sp in sweep_params:
    eta = sp["eta"]
    C0_s = sp["C0_s"]
    C0_d = sp["C0_d"]
    k = sp["k"]
    p = sp["p"]
    
    errors_m = []
    errors_pct = []
    dev_names = []
    
    for d in devices:
        C_rate = d["P_peak"] / d["E_supply"]
        f_th = d["power_ratio"]
        f_skin = 1.0
        C0_base = C0_d if d["arch"] == "Dual" else C0_s
        C0_eff = C0_base * f_th * f_skin
        
        if C_rate <= C0_eff:
            F_sys = eta
        else:
            denom = 1.0 + k * ((C_rate - C0_eff) ** p)
            F_sys = min(1.0, eta / denom)
            
        P_eff = d["P_peak"] * F_sys
        T_pred = (d["E_supply"] / P_eff) * 60.0
        
        err_m = T_pred - d["T_A"]
        err_pct = (err_m / d["T_A"]) * 100.0
        
        errors_m.append(err_m)
        errors_pct.append(err_pct)
        dev_names.append(d["name"])
        
    arr_m = np.array(errors_m)
    arr_pct = np.array(errors_pct)
    
    mean_dt = np.mean(arr_m)
    mae_t = np.mean(np.abs(arr_m))
    rmse_t = np.sqrt(np.mean(arr_m ** 2))
    
    # Max absolute error in minutes
    abs_m = np.abs(arr_m)
    idx_max_m = np.argmax(abs_m)
    max_err_m = abs_m[idx_max_m]
    max_dev_m = dev_names[idx_max_m]
    
    # Max absolute error in percent
    abs_pct = np.abs(arr_pct)
    idx_max_pct = np.argmax(abs_pct)
    max_err_pct = abs_pct[idx_max_pct]
    max_dev_pct = dev_names[idx_max_pct]
    
    print(f"{sp['name']:<18} | {eta:<7.4f} | {C0_s:<6.4f} | {C0_d:<6.4f} | {k:<6.4f} | {p:<6.4f} | {mean_dt:<+7.2f} | {mae_t:<6.2f} | {rmse_t:<6.2f} | {max_err_m:<9.2f} | {max_dev_m:<22} | {max_err_pct:<+8.1f}% | {max_dev_pct:<22}")
