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

    # --- APPLE IPHONES & LG (STRICT THERMAL SKIN CAP T_limit = 35°C) ---
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

def calc_tdsi_and_power_ratio(stability_pct):
    tdsi = 10.0 * (np.log10(stability_pct) - np.log10(40.0)) / (np.log10(100.0) - np.log10(40.0))
    power_ratio = (stability_pct / 100.0) ** 3
    return tdsi, power_ratio

for d in devices:
    tdsi, pr = calc_tdsi_and_power_ratio(d["stability_pct"])
    d["tdsi"] = tdsi
    d["power_ratio"] = pr

def predict_charging_time(d, eta_low, C0_single_base, C0_dual_base, k, p):
    E_supply = d["E_supply"]
    P_peak = d["P_peak"]
    C_rate = P_peak / E_supply
    
    f_thermal = d["power_ratio"]
    f_skin_headroom = ((d["vendor_T_limit"] - 25.0) / 15.0) ** 0.5
    
    C0_base = C0_dual_base if d["arch"] == "Dual" else C0_single_base
    C0_effective = C0_base * f_thermal * f_skin_headroom
    
    if C_rate <= C0_effective:
        F_system = eta_low
    else:
        denom = 1.0 + k * ((C_rate - C0_effective) ** p)
        F_system = min(1.0, eta_low / denom)
        
    P_effective = P_peak * F_system
    T_handshake = 0.5
    T_predicted = (E_supply / P_effective) * 60.0 + T_handshake
    
    return T_predicted

bounds = [
    (0.85, 0.99),    # eta_low
    (0.10, 2.00),    # C0_single_base
    (1.00, 8.00),    # C0_dual_base
    (0.10, 5.00),    # k
    (0.05, 1.50)     # p
]

deltas = [0.0, 0.5, 1.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0, 30.0, 50.0, 100.0]

print("=== HUBER LOSS THRESHOLD (delta) FINE SENSITIVITY SWEEP ===")
print("| Huber Threshold (`delta`) | eta_low  | C0_single (h^-1) | C0_dual (h^-1) | `k`      | `p`      | `MAE_T` (mins) | `RMSE_T` (mins) | Max Error (mins) | Boundary Status |")
print("| :-----------------------: | :------: | :--------------: | :------------: | :------: | :------: | :------------: | :-------------: | :--------------: | :-------------: |")

for delta in deltas:
    def loss_func(params):
        eta_low, C0_single_base, C0_dual_base, k, p = params
        errors = []
        for d in devices:
            T_pred = predict_charging_time(d, eta_low, C0_single_base, C0_dual_base, k, p)
            err = d["T_A"] - T_pred
            errors.append(err)
        errors = np.array(errors)
        abs_err = np.abs(errors)
        
        if delta == 0.0:
            loss = abs_err
        else:
            loss = np.where(abs_err <= delta, 0.5 * (errors ** 2), delta * abs_err - 0.5 * (delta ** 2))
        return np.mean(loss)

    res = differential_evolution(loss_func, bounds, seed=42, popsize=20, maxiter=800)
    eta_low_opt, C0_single_opt, C0_dual_opt, k_opt, p_opt = res.x
    
    # Eval errors
    maes = []
    sq_errs = []
    for d in devices:
        tp = predict_charging_time(d, eta_low_opt, C0_single_opt, C0_dual_opt, k_opt, p_opt)
        e = abs(tp - d["T_A"])
        maes.append(e)
        sq_errs.append(e ** 2)
    
    mae_val = np.mean(maes)
    rmse_val = np.sqrt(np.mean(sq_errs))
    max_err_val = np.max(maes)
    
    # Boundary check
    is_interior = (
        0.8501 < eta_low_opt < 0.9899 and
        0.1001 < C0_single_opt < 1.999 and
        1.0001 < C0_dual_opt < 7.999 and
        0.1001 < k_opt < 4.999 and
        0.0501 < p_opt < 1.499
    )
    status = "OK (Interior)" if is_interior else "Boundary"
    
    label = f"**`{delta:.1f}`**" if delta > 0 else "**`0.0` (Pure MAE)**"
    if delta == 100.0: label = "**`100.0` (MSE-like)**"
    
    print(f"| {label:25s} | `{eta_low_opt:.4f}` | `{C0_single_opt:.4f}`         | `{C0_dual_opt:.4f}`       | `{k_opt:.4f}` | `{p_opt:.4f}` | **`{mae_val:.2f}`**     | `{rmse_val:.2f}`         | `{max_err_val:.2f}`          | {status:15s} |")

