import numpy as np
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

# Calibrated parameters under delta = 20.0 mins
eta_low_opt = 0.9687
C0_single_opt = 0.3943
C0_dual_opt = 5.0649
k_opt = 1.1188
p_opt = 0.2893

def calc_tdsi_and_power_ratio(stability_pct):
    tdsi = 10.0 * (np.log10(stability_pct) - np.log10(40.0)) / (np.log10(100.0) - np.log10(40.0))
    power_ratio = (stability_pct / 100.0) ** 3
    return tdsi, power_ratio

for d in devices:
    tdsi, pr = calc_tdsi_and_power_ratio(d["stability_pct"])
    d["tdsi"] = tdsi
    d["power_ratio"] = pr

def predict_charging_time(d):
    E_supply = d["E_supply"]
    P_peak = d["P_peak"]
    C_rate = P_peak / E_supply
    
    f_thermal = d["power_ratio"]
    f_skin_headroom = 1.0  # Always 1.0
    
    C0_base = C0_dual_opt if d["arch"] == "Dual" else C0_single_opt
    C0_effective = C0_base * f_thermal * f_skin_headroom
    
    if C_rate <= C0_effective:
        F_system = eta_low_opt
    else:
        denom = 1.0 + k_opt * ((C_rate - C0_effective) ** p_opt)
        F_system = min(1.0, eta_low_opt / denom)
        
    P_effective = P_peak * F_system
    T_predicted = (E_supply / P_effective) * 60.0
    
    return T_predicted, f_thermal, F_system, P_effective, C_rate, C0_effective, C0_base

table_rows = []
for d in devices:
    T_pred, f_th, F_sys, P_eff, C_rate, C0_eff, C0_base = predict_charging_time(d)
    err = T_pred - d["T_A"]
    err_pct = (err / d["T_A"]) * 100.0
    
    table_rows.append([
        f"**{d['name']}**",
        d["arch"],
        f"{d['P_peak']:.1f} W",
        f"{d['E_supply']:.2f} Wh",
        f"{C_rate:.2f}",
        f"{P_eff:.1f} W",
        f"{F_sys:.4f}",
        f"{C0_eff:.4f}",
        f"{C0_base:.4f}",
        f"{f_th:.4f}",
        f"{d['tdsi']:.2f}",
        f"{d['T_A']:.1f} m",
        f"{T_pred:.1f} m",
        f"{'+' if err>=0 else ''}{err:.1f} m",
        f"{'+' if err_pct>=0 else ''}{err_pct:.1f}%"
    ])

headers = [
    "Smartphone Device Model", "Arch", "P_peak (W)", "E_supply (Wh)", "C_rate (h^-1)",
    "P_eff (W)", "F_system", "`C0_effective`", "`C0_base`", "`f_thermal`",
    "TDSI Score", "Benchmark `T_A`", "Predicted `T_C`", "Residual Error (`Delta`)", "Error %"
]
alignments = [":---", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:", ":---:"]

col_widths = [len(h) for h in headers]
for row in table_rows:
    for i, val in enumerate(row):
        col_widths[i] = max(col_widths[i], len(val))

header_str = "| " + " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers))) + " |"

align_cells = []
for i, a in enumerate(alignments):
    w = col_widths[i]
    if a == ":---:":
        s = ":" + "-" * (w - 2) + ":"
    elif a == ":---":
        s = ":" + "-" * (w - 1)
    align_cells.append(s)
align_str = "| " + " | ".join(align_cells) + " |"

lines_out = [header_str, align_str]
for row in table_rows:
    r_str = "| " + " | ".join(row[i].ljust(col_widths[i]) for i in range(len(row))) + " |"
    lines_out.append(r_str)

formatted_md = "\n".join(lines_out)
with open(r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\modeling\section_8_2_method_c_huber_optimization_study\working_files\generated_table_no_fskin.md", "w", encoding="utf-8") as f:
    f.write(formatted_md)

print("Generated table without f_skin_headroom successfully.")
