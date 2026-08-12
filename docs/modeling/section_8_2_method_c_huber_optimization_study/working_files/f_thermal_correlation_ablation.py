import numpy as np
import scipy.stats as stats
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

y_time = np.array([d["T_A"] for d in devices])
f_th = np.array([(d["stability_pct"] / 100.0) ** 3 for d in devices])
c_rate = np.array([d["P_peak"] / d["E_supply"] for d in devices])
inv_c_rate = 1.0 / c_rate
stability = np.array([d["stability_pct"] for d in devices])
arch_dual = np.array([1 if d["arch"] == "Dual" else 0 for d in devices])

print("=========================================================================")
print("1. DIRECT BIVARIATE & PARTIAL CORRELATIONS WITH CHARGING DURATION (T_A)")
print("=========================================================================")

r_fth, p_fth = stats.pearsonr(f_th, y_time)
rho_fth, p_rho_fth = stats.spearmanr(f_th, y_time)

r_stab, p_stab = stats.pearsonr(stability, y_time)
rho_stab, p_rho_stab = stats.spearmanr(stability, y_time)

print(f"f_thermal vs T_A   -> Pearson r = {r_fth:<+7.4f} (p = {p_fth:.4e}) | Spearman rho = {rho_fth:<+7.4f} (p = {p_rho_fth:.4e})")
print(f"stability vs T_A   -> Pearson r = {r_stab:<+7.4f} (p = {p_stab:.4e}) | Spearman rho = {rho_stab:<+7.4f} (p = {p_rho_stab:.4e})")

# Partial correlation: Correlation between f_thermal and T_A, controlling for inv_C_rate
# Residuals of T_A on inv_C_rate
res_y = y_time - np.polyval(np.polyfit(inv_c_rate, y_time, 1), inv_c_rate)
# Residuals of f_thermal on inv_C_rate
res_f = f_th - np.polyval(np.polyfit(inv_c_rate, f_th, 1), inv_c_rate)

r_partial, p_partial = stats.pearsonr(res_f, res_y)
print(f"\nPARTIAL CORRELATION (f_thermal vs T_A, controlling for inv_C_rate):")
print(f"  Partial Pearson r = {r_partial:<+7.4f} (p-value = {p_partial:.4f})")

print("\n=========================================================================")
print("2. ABLATION STUDY: WITH f_thermal VS. NEUTRALIZED f_thermal = 1.0000")
print("=========================================================================")

# Re-calibrate Model with f_thermal active vs f_thermal = 1.0000
def huber_loss(res, delta=20.0):
    abs_res = np.abs(res)
    return np.where(abs_res <= delta, 0.5 * (abs_res ** 2), delta * abs_res - 0.5 * (delta ** 2))

def predict_model(params, use_f_thermal=True):
    eta_low, C0_single, C0_dual, k, p = params
    preds = []
    for d in devices:
        C_rate = d["P_peak"] / d["E_supply"]
        f_t = ((d["stability_pct"] / 100.0) ** 3) if use_f_thermal else 1.0
        C0_base = C0_dual if d["arch"] == "Dual" else C0_single
        C0_eff = C0_base * f_t
        
        if C_rate <= C0_eff:
            F_sys = eta_low
        else:
            denom = 1.0 + k * ((C_rate - C0_eff) ** p)
            F_sys = min(1.0, eta_low / denom)
            
        P_eff = d["P_peak"] * F_sys
        T_pred = (d["E_supply"] / P_eff) * 60.0
        preds.append(T_pred)
    return np.array(preds)

def obj_active(params):
    preds = predict_model(params, use_f_thermal=True)
    return np.mean(huber_loss(preds - y_time))

def obj_neutralized(params):
    preds = predict_model(params, use_f_thermal=False)
    return np.mean(huber_loss(preds - y_time))

bounds = [(0.50, 1.00), (0.00, 15.00), (0.00, 15.00), (0.00, 10.00), (0.01, 5.00)]

res_act = differential_evolution(obj_active, bounds=bounds, seed=42, popsize=40, maxiter=1000)
res_neu = differential_evolution(obj_neutralized, bounds=bounds, seed=42, popsize=40, maxiter=1000)

preds_act = predict_model(res_act.x, use_f_thermal=True)
preds_neu = predict_model(res_neu.x, use_f_thermal=False)

err_act = preds_act - y_time
err_neu = preds_neu - y_time

print(f"{'Configuration':<35} | {'eta_low':<7} | {'C0_s':<6} | {'C0_d':<6} | {'k':<6} | {'p':<6} | {'MAE (m)':<7} | {'RMSE (m)':<8} | {'MaxErr(m)':<9} | {'MaxErr(%)':<9}")
print("-" * 125)

p_a = res_act.x
p_n = res_neu.x

mae_a, rmse_a = np.mean(np.abs(err_act)), np.sqrt(np.mean(err_act**2))
max_m_a, max_pct_a = np.max(np.abs(err_act)), np.max(np.abs((err_act/y_time)*100.0))

mae_n, rmse_n = np.mean(np.abs(err_neu)), np.sqrt(np.mean(err_neu**2))
max_m_n, max_pct_n = np.max(np.abs(err_neu)), np.max(np.abs((err_neu/y_time)*100.0))

print(f"{'With f_thermal = power_ratio':<35} | {p_a[0]:<7.4f} | {p_a[1]:<6.4f} | {p_a[2]:<6.4f} | {p_a[3]:<6.4f} | {p_a[4]:<6.4f} | {mae_a:<7.2f} | {rmse_a:<8.2f} | {max_m_a:<9.2f} | +{max_pct_a:<7.1f}%")
print(f"{'Neutralized f_thermal = 1.0000':<35} | {p_n[0]:<7.4f} | {p_n[1]:<6.4f} | {p_n[2]:<6.4f} | {p_n[3]:<6.4f} | {p_n[4]:<6.4f} | {mae_n:<7.2f} | {rmse_n:<8.2f} | {max_m_n:<9.2f} | +{max_pct_n:<7.1f}%")
