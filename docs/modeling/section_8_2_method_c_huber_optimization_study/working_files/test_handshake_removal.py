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
    {"name": "OnePlus 12", "arch": "Dual", "P_peak": 100.0, "E_supply": 20.79, "T_A": 26.0, "vendor_T_limit": 40.0, "stability_pct": 3.55}, # TDSI mapped
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

# Ensure OnePlus 12 stability_pct is correct 55.4
devices[8]["stability_pct"] = 55.4

for d in devices:
    d["power_ratio"] = (d["stability_pct"] / 100.0) ** 3

bounds = [
    (0.85, 0.99),    # eta_low
    (0.10, 2.00),    # C0_single_base
    (1.00, 8.00),    # C0_dual_base
    (0.10, 5.00),    # k
    (0.05, 1.50)     # p
]

def run_experiment(t_handshake, delta=5.0):
    def predict(d, eta_low, C0_single_base, C0_dual_base, k, p):
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
        T_predicted = (E_supply / P_effective) * 60.0 + t_handshake
        return T_predicted

    def loss_func(params):
        eta_low, C0_single_base, C0_dual_base, k, p = params
        errors = []
        for d in devices:
            T_pred = predict(d, eta_low, C0_single_base, C0_dual_base, k, p)
            err = d["T_A"] - T_pred
            errors.append(err)
        errors = np.array(errors)
        abs_err = np.abs(errors)
        loss = np.where(abs_err <= delta, 0.5 * (errors ** 2), delta * abs_err - 0.5 * (delta ** 2))
        return np.mean(loss)

    res = differential_evolution(loss_func, bounds, seed=42, popsize=20, maxiter=800)
    eta_low_opt, C0_single_opt, C0_dual_opt, k_opt, p_opt = res.x

    maes = []
    sq_errs = []
    diffs = []
    for d in devices:
        tp = predict(d, eta_low_opt, C0_single_opt, C0_dual_opt, k_opt, p_opt)
        e = abs(tp - d["T_A"])
        maes.append(e)
        sq_errs.append(e ** 2)
        diffs.append(d["T_A"] - tp)

    return {
        "t_handshake": t_handshake,
        "eta_low": eta_low_opt,
        "C0_single": C0_single_opt,
        "C0_dual": C0_dual_opt,
        "k": k_opt,
        "p": p_opt,
        "MAE_T": np.mean(maes),
        "RMSE_T": np.sqrt(np.mean(sq_errs)),
        "Max_err": np.max(maes),
        "Mean_dT": np.mean(diffs)
    }

res_05 = run_experiment(0.5, delta=5.0)
res_00 = run_experiment(0.0, delta=5.0)

print("=== COMPARISON WITH vs WITHOUT T_handshake (delta = 5.0 mins) ===")
print(f"WITH T_handshake = 0.5m:  MAE_T = {res_05['MAE_T']:.4f} mins, RMSE_T = {res_05['RMSE_T']:.4f} mins, Max_err = {res_05['Max_err']:.4f} mins, Mean_dT = {res_05['Mean_dT']:.4f} mins")
print(f"WITHOUT T_handshake = 0.0m: MAE_T = {res_00['MAE_T']:.4f} mins, RMSE_T = {res_00['RMSE_T']:.4f} mins, Max_err = {res_00['Max_err']:.4f} mins, Mean_dT = {res_00['Mean_dT']:.4f} mins")

print("\nParameter shift:")
print(f"WITH   T_handshake=0.5m: eta_low={res_05['eta_low']:.4f}, C0_single={res_05['C0_single']:.4f}, C0_dual={res_05['C0_dual']:.4f}, k={res_05['k']:.4f}, p={res_05['p']:.4f}")
print(f"WITHOUT T_handshake=0.0m: eta_low={res_00['eta_low']:.4f}, C0_single={res_00['C0_single']:.4f}, C0_dual={res_00['C0_dual']:.4f}, k={res_00['k']:.4f}, p={res_00['p']:.4f}")
