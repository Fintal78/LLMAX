import numpy as np
import scipy.stats as stats
import sys

sys.stdout.reconfigure(encoding='utf-8')

devices = [
    # --- DUAL-CELL 2S SERIES ULTRA FAST-CHARGERS ---
    {"name": "Realme GT3", "arch": 2, "P_peak": 240.0, "E_supply": 17.71, "T_A": 9.6, "vendor_T_limit": 40.0, "stability_pct": 63.5},
    {"name": "Redmi Note 12 Explorer", "arch": 2, "P_peak": 210.0, "E_supply": 16.56, "T_A": 9.0, "vendor_T_limit": 40.0, "stability_pct": 59.8},
    {"name": "iQOO 11 Pro", "arch": 2, "P_peak": 200.0, "E_supply": 18.10, "T_A": 12.0, "vendor_T_limit": 40.0, "stability_pct": 58.0},
    {"name": "Motorola Edge 50 Pro", "arch": 2, "P_peak": 125.0, "E_supply": 17.33, "T_A": 18.0, "vendor_T_limit": 40.0, "stability_pct": 99.1},
    {"name": "Xiaomi 13 Pro", "arch": 2, "P_peak": 120.0, "E_supply": 18.56, "T_A": 19.0, "vendor_T_limit": 40.0, "stability_pct": 68.2},
    {"name": "Xiaomi 12T Pro", "arch": 2, "P_peak": 120.0, "E_supply": 19.25, "T_A": 19.0, "vendor_T_limit": 40.0, "stability_pct": 62.4},
    {"name": "Poco F4 GT", "arch": 2, "P_peak": 120.0, "E_supply": 18.10, "T_A": 17.0, "vendor_T_limit": 40.0, "stability_pct": 53.0},
    {"name": "Vivo X100 Pro", "arch": 2, "P_peak": 100.0, "E_supply": 20.79, "T_A": 31.0, "vendor_T_limit": 40.0, "stability_pct": 52.6},
    {"name": "OnePlus 12", "arch": 2, "P_peak": 100.0, "E_supply": 20.79, "T_A": 26.0, "vendor_T_limit": 40.0, "stability_pct": 55.4},
    {"name": "OnePlus 11", "arch": 2, "P_peak": 100.0, "E_supply": 19.25, "T_A": 25.0, "vendor_T_limit": 40.0, "stability_pct": 54.1},
    {"name": "OnePlus 12R", "arch": 2, "P_peak": 80.0, "E_supply": 21.17, "T_A": 32.0, "vendor_T_limit": 40.0, "stability_pct": 65.5},
    {"name": "Asus ROG Phone 7", "arch": 2, "P_peak": 65.0, "E_supply": 23.10, "T_A": 42.0, "vendor_T_limit": 40.0, "stability_pct": 79.2},

    # --- SINGLE-CELL 1S HIGH-END & MID-RANGE ANDROID ---
    {"name": "Xiaomi 14", "arch": 1, "P_peak": 90.0, "E_supply": 17.71, "T_A": 35.0, "vendor_T_limit": 40.0, "stability_pct": 58.5},
    {"name": "Honor Magic 6 Pro", "arch": 1, "P_peak": 80.0, "E_supply": 21.56, "T_A": 36.0, "vendor_T_limit": 40.0, "stability_pct": 64.0},
    {"name": "Motorola Edge 40", "arch": 1, "P_peak": 68.0, "E_supply": 17.33, "T_A": 44.0, "vendor_T_limit": 40.0, "stability_pct": 78.5},
    {"name": "Xiaomi 13", "arch": 1, "P_peak": 67.0, "E_supply": 17.33, "T_A": 42.0, "vendor_T_limit": 40.0, "stability_pct": 72.0},
    {"name": "Honor Magic 5 Pro", "arch": 1, "P_peak": 66.0, "E_supply": 19.64, "T_A": 48.0, "vendor_T_limit": 40.0, "stability_pct": 68.0},
    {"name": "Samsung Galaxy S24 Ultra", "arch": 1, "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0, "vendor_T_limit": 40.0, "stability_pct": 59.0},
    {"name": "Samsung Galaxy S23 Ultra", "arch": 1, "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0, "vendor_T_limit": 40.0, "stability_pct": 58.2},
    {"name": "Samsung Galaxy S22 Ultra", "arch": 1, "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0, "vendor_T_limit": 40.0, "stability_pct": 54.8},
    {"name": "Nothing Phone (2)", "arch": 1, "P_peak": 45.0, "E_supply": 18.10, "T_A": 55.0, "vendor_T_limit": 40.0, "stability_pct": 72.1},
    {"name": "Google Pixel 9 Pro XL", "arch": 1, "P_peak": 37.0, "E_supply": 19.48, "T_A": 79.0, "vendor_T_limit": 40.0, "stability_pct": 58.0},
    {"name": "Google Pixel 8 Pro", "arch": 1, "P_peak": 30.0, "E_supply": 19.44, "T_A": 81.0, "vendor_T_limit": 40.0, "stability_pct": 53.5},
    {"name": "Samsung Galaxy S24", "arch": 1, "P_peak": 25.0, "E_supply": 15.40, "T_A": 75.0, "vendor_T_limit": 40.0, "stability_pct": 58.4},
    {"name": "Samsung Galaxy S23", "arch": 1, "P_peak": 25.0, "E_supply": 15.02, "T_A": 80.0, "vendor_T_limit": 40.0, "stability_pct": 62.1},
    {"name": "Samsung Galaxy A55", "arch": 1, "P_peak": 25.0, "E_supply": 19.25, "T_A": 85.0, "vendor_T_limit": 40.0, "stability_pct": 99.4},
    {"name": "Samsung Galaxy A54", "arch": 1, "P_peak": 25.0, "E_supply": 19.25, "T_A": 82.0, "vendor_T_limit": 40.0, "stability_pct": 99.2},
    {"name": "Samsung Galaxy A34", "arch": 1, "P_peak": 25.0, "E_supply": 19.25, "T_A": 84.0, "vendor_T_limit": 40.0, "stability_pct": 99.3},
    {"name": "Google Pixel 7 Pro", "arch": 1, "P_peak": 23.0, "E_supply": 19.25, "T_A": 109.0, "vendor_T_limit": 40.0, "stability_pct": 64.2},
    {"name": "Samsung Galaxy S10", "arch": 1, "P_peak": 15.0, "E_supply": 13.09, "T_A": 108.0, "vendor_T_limit": 40.0, "stability_pct": 74.5},
    {"name": "Samsung Galaxy S9", "arch": 1, "P_peak": 15.0, "E_supply": 11.55, "T_A": 107.0, "vendor_T_limit": 40.0, "stability_pct": 78.0},
    {"name": "Samsung Galaxy S8", "arch": 1, "P_peak": 15.0, "E_supply": 11.55, "T_A": 100.0, "vendor_T_limit": 40.0, "stability_pct": 82.0},
    {"name": "Nokia 2.4", "arch": 1, "P_peak": 5.0, "E_supply": 17.33, "T_A": 215.0, "vendor_T_limit": 40.0, "stability_pct": 99.8},
    {"name": "Samsung Galaxy A03 Core", "arch": 1, "P_peak": 7.8, "E_supply": 19.25, "T_A": 205.0, "vendor_T_limit": 40.0, "stability_pct": 99.6},

    # --- APPLE IPHONES & LG ---
    {"name": "Apple iPhone 16 Pro Max", "arch": 1, "P_peak": 30.0, "E_supply": 18.04, "T_A": 117.0, "vendor_T_limit": 35.0, "stability_pct": 68.0},
    {"name": "Apple iPhone 14 Pro Max", "arch": 1, "P_peak": 29.0, "E_supply": 16.64, "T_A": 112.0, "vendor_T_limit": 35.0, "stability_pct": 68.4},
    {"name": "Apple iPhone 15 Pro Max", "arch": 1, "P_peak": 27.0, "E_supply": 17.02, "T_A": 109.0, "vendor_T_limit": 35.0, "stability_pct": 65.8},
    {"name": "Apple iPhone 13 Pro Max", "arch": 1, "P_peak": 27.0, "E_supply": 16.75, "T_A": 106.0, "vendor_T_limit": 35.0, "stability_pct": 73.5},
    {"name": "Apple iPhone 11 Pro Max", "arch": 1, "P_peak": 18.0, "E_supply": 15.04, "T_A": 120.0, "vendor_T_limit": 35.0, "stability_pct": 75.0},
    {"name": "LG G7 ThinQ", "arch": 1, "P_peak": 18.0, "E_supply": 11.55, "T_A": 108.0, "vendor_T_limit": 35.0, "stability_pct": 61.2},
    {"name": "Apple iPhone XS Max", "arch": 1, "P_peak": 15.0, "E_supply": 12.08, "T_A": 131.0, "vendor_T_limit": 35.0, "stability_pct": 72.0},
    {"name": "Apple iPhone X", "arch": 1, "P_peak": 15.0, "E_supply": 10.43, "T_A": 125.0, "vendor_T_limit": 35.0, "stability_pct": 70.0},
    {"name": "Apple iPhone 8", "arch": 1, "P_peak": 5.0, "E_supply": 7.01, "T_A": 148.0, "vendor_T_limit": 35.0, "stability_pct": 85.0},
    {"name": "Apple iPhone 7 Plus", "arch": 1, "P_peak": 5.0, "E_supply": 11.17, "T_A": 241.0, "vendor_T_limit": 35.0, "stability_pct": 88.0}
]

eta_low = 0.9687
C0_s = 0.3943
C0_d = 5.0649
k = 1.1188
p = 0.2893

data = {}
data["P_peak"] = np.array([d["P_peak"] for d in devices])
data["E_supply"] = np.array([d["E_supply"] for d in devices])
data["C_rate"] = data["P_peak"] / data["E_supply"]
data["inv_C_rate"] = 1.0 / data["C_rate"]
data["arch"] = np.array([d["arch"] for d in devices])
data["f_thermal"] = np.array([(d["stability_pct"] / 100.0) ** 3 for d in devices])
data["C0_base"] = np.array([C0_d if d["arch"] == 2 else C0_s for d in devices])
data["C0_effective"] = data["C0_base"] * data["f_thermal"]

y = np.array([d["T_A"] for d in devices])

print("=========================================================================")
print("1. BIVARIATE CORRELATION ANALYSIS WITH EMPIRICAL METHOD A CHARGING TIME (T_A)")
print("=========================================================================")

feature_names = ["inv_C_rate", "P_peak", "C_rate", "E_supply", "arch", "f_thermal", "C0_base", "C0_effective"]

print(f"{'Feature':<16} | {'Pearson r':<10} | {'Pearson p':<10} | {'Spearman rho':<12} | {'Spearman p':<10}")
print("-" * 75)
for feat in feature_names:
    x = data[feat]
    r_val, r_p = stats.pearsonr(x, y)
    rho_val, rho_p = stats.spearmanr(x, y)
    print(f"{feat:<16} | {r_val:<+10.4f} | {r_p:<10.4e} | {rho_val:<+12.4f} | {rho_p:<10.4e}")

print("\n=========================================================================")
print("2. MULTIPLE OLS REGRESSION MODELS & FEATURE IMPORTANCE")
print("=========================================================================")

def fit_ols(X_matrix, y_vector):
    N = len(y_vector)
    K = X_matrix.shape[1]
    X_design = np.column_stack([np.ones(N), X_matrix])
    beta = np.linalg.lstsq(X_design, y_vector, rcond=None)[0]
    y_pred = X_design @ beta
    residuals = y_vector - y_pred
    ss_tot = np.sum((y_vector - np.mean(y_vector)) ** 2)
    ss_res = np.sum(residuals ** 2)
    r2 = 1.0 - (ss_res / ss_tot)
    r2_adj = 1.0 - (1.0 - r2) * (N - 1) / (N - K - 1)
    rmse = np.sqrt(np.mean(residuals ** 2))
    mae = np.mean(np.abs(residuals))
    return r2, r2_adj, mae, rmse, beta

# Model 1: inv_C_rate alone
r2_1, r2_adj_1, mae_1, rmse_1, b1 = fit_ols(data["inv_C_rate"][:, None], y)
print(f"Model 1 (inv_C_rate alone):               R^2 = {r2_1:.4f} | Adj R^2 = {r2_adj_1:.4f} | MAE = {mae_1:.2f} m | RMSE = {rmse_1:.2f} m")

# Model 2: inv_C_rate + Arch
r2_2, r2_adj_2, mae_2, rmse_2, b2 = fit_ols(np.column_stack([data["inv_C_rate"], data["arch"]]), y)
print(f"Model 2 (inv_C_rate + Arch):             R^2 = {r2_2:.4f} | Adj R^2 = {r2_adj_2:.4f} | MAE = {mae_2:.2f} m | RMSE = {rmse_2:.2f} m")

# Model 3: inv_C_rate + Arch + C0_effective
r2_3, r2_adj_3, mae_3, rmse_3, b3 = fit_ols(np.column_stack([data["inv_C_rate"], data["arch"], data["C0_effective"]]), y)
print(f"Model 3 (inv_C_rate + Arch + C0_eff):    R^2 = {r2_3:.4f} | Adj R^2 = {r2_adj_3:.4f} | MAE = {mae_3:.2f} m | RMSE = {rmse_3:.2f} m")

# Model 4: inv_C_rate + Arch + f_thermal + C0_effective
r2_4, r2_adj_4, mae_4, rmse_4, b4 = fit_ols(np.column_stack([data["inv_C_rate"], data["arch"], data["f_thermal"], data["C0_effective"]]), y)
print(f"Model 4 (inv_C_rate + Arch + f_th + C0):  R^2 = {r2_4:.4f} | Adj R^2 = {r2_adj_4:.4f} | MAE = {mae_4:.2f} m | RMSE = {rmse_4:.2f} m")

print("\n=========================================================================")
print("3. METHOD C ABLATION STUDY: PHYSICAL IMPACT OF C0_effective")
print("=========================================================================")

def predict_method_c(d, use_C0=True):
    C_rate = d["P_peak"] / d["E_supply"]
    f_th = (d["stability_pct"] / 100.0) ** 3
    C0_base = C0_d if d["arch"] == 2 else C0_s
    C0_eff = C0_base * f_th if use_C0 else 0.0
    
    if C_rate <= C0_eff:
        F_sys = eta_low
    else:
        denom = 1.0 + k * ((C_rate - C0_eff) ** p)
        F_sys = min(1.0, eta_low / denom)
        
    P_eff = d["P_peak"] * F_sys
    return (d["E_supply"] / P_eff) * 60.0

T_pred_full = np.array([predict_method_c(d, use_C0=True) for d in devices])
T_pred_no_C0 = np.array([predict_method_c(d, use_C0=False) for d in devices])

err_full = T_pred_full - y
err_no_C0 = T_pred_no_C0 - y

print(f"Overall 44-Device Suite:")
print(f"  Full Method C (with C0_effective) -> MAE: {np.mean(np.abs(err_full)):.2f} mins | RMSE: {np.sqrt(np.mean(err_full**2)):.2f} mins")
print(f"  Ablated Method C (C0_effective=0) -> MAE: {np.mean(np.abs(err_no_C0)):.2f} mins | RMSE: {np.sqrt(np.mean(err_no_C0**2)):.2f} mins")

# Sub-dataset Breakdown
mask_dual = (data["arch"] == 2)
mask_low = (data["P_peak"] <= 10.0)
mask_single_fast = (data["arch"] == 1) & (data["P_peak"] > 10.0)

print(f"\nSub-Group 1: Dual-Cell Series Hardware (12 devices)")
err_f_d = err_full[mask_dual]
err_n_d = err_no_C0[mask_dual]
print(f"  Full Method C  -> MAE: {np.mean(np.abs(err_f_d)):.2f} mins | RMSE: {np.sqrt(np.mean(err_f_d**2)):.2f} mins")
print(f"  No C0_effective -> MAE: {np.mean(np.abs(err_n_d)):.2f} mins | RMSE: {np.sqrt(np.mean(err_n_d**2)):.2f} mins")

print(f"\nSub-Group 2: Low-Power Legacy Hardware (4 devices: Nokia 2.4, Galaxy A03 Core, iPhone 8, 7 Plus)")
err_f_l = err_full[mask_low]
err_n_l = err_no_C0[mask_low]
print(f"  Full Method C  -> MAE: {np.mean(np.abs(err_f_l)):.2f} mins | RMSE: {np.sqrt(np.mean(err_f_l**2)):.2f} mins")
print(f"  No C0_effective -> MAE: {np.mean(np.abs(err_n_l)):.2f} mins | RMSE: {np.sqrt(np.mean(err_n_l**2)):.2f} mins")

print(f"\nSub-Group 3: High-Power Single-Cell Androids (28 devices)")
err_f_s = err_full[mask_single_fast]
err_n_s = err_no_C0[mask_single_fast]
print(f"  Full Method C  -> MAE: {np.mean(np.abs(err_f_s)):.2f} mins | RMSE: {np.sqrt(np.mean(err_f_s**2)):.2f} mins")
print(f"  No C0_effective -> MAE: {np.mean(np.abs(err_n_s)):.2f} mins | RMSE: {np.sqrt(np.mean(err_n_s**2)):.2f} mins")
