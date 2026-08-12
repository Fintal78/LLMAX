import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

devices = [
    # --- DUAL-CELL 2S SERIES ULTRA FAST-CHARGERS ---
    {"name": "Realme GT3", "arch": "Dual", "P_peak": 240.0, "E_supply": 17.71, "T_A": 9.6},
    {"name": "Redmi Note 12 Explorer", "arch": "Dual", "P_peak": 210.0, "E_supply": 16.56, "T_A": 9.0},
    {"name": "iQOO 11 Pro", "arch": "Dual", "P_peak": 200.0, "E_supply": 18.10, "T_A": 12.0},
    {"name": "Motorola Edge 50 Pro", "arch": "Dual", "P_peak": 125.0, "E_supply": 17.33, "T_A": 18.0},
    {"name": "Xiaomi 13 Pro", "arch": "Dual", "P_peak": 120.0, "E_supply": 18.56, "T_A": 19.0},
    {"name": "Xiaomi 12T Pro", "arch": "Dual", "P_peak": 120.0, "E_supply": 19.25, "T_A": 19.0},
    {"name": "Poco F4 GT", "arch": "Dual", "P_peak": 120.0, "E_supply": 18.10, "T_A": 17.0},
    {"name": "Vivo X100 Pro", "arch": "Dual", "P_peak": 100.0, "E_supply": 20.79, "T_A": 31.0},
    {"name": "OnePlus 12", "arch": "Dual", "P_peak": 100.0, "E_supply": 20.79, "T_A": 26.0},
    {"name": "OnePlus 11", "arch": "Dual", "P_peak": 100.0, "E_supply": 19.25, "T_A": 25.0},
    {"name": "OnePlus 12R", "arch": "Dual", "P_peak": 80.0, "E_supply": 21.17, "T_A": 32.0},
    {"name": "Asus ROG Phone 7", "arch": "Dual", "P_peak": 65.0, "E_supply": 23.10, "T_A": 42.0},

    # --- SINGLE-CELL 1S HIGH-END & MID-RANGE ANDROID ---
    {"name": "Xiaomi 14", "arch": "Single", "P_peak": 90.0, "E_supply": 17.71, "T_A": 35.0},
    {"name": "Honor Magic 6 Pro", "arch": "Single", "P_peak": 80.0, "E_supply": 21.56, "T_A": 36.0},
    {"name": "Motorola Edge 40", "arch": "Single", "P_peak": 68.0, "E_supply": 17.33, "T_A": 44.0},
    {"name": "Xiaomi 13", "arch": "Single", "P_peak": 67.0, "E_supply": 17.33, "T_A": 42.0},
    {"name": "Honor Magic 5 Pro", "arch": "Single", "P_peak": 66.0, "E_supply": 19.64, "T_A": 48.0},
    {"name": "Samsung Galaxy S24 Ultra", "arch": "Single", "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0},
    {"name": "Samsung Galaxy S23 Ultra", "arch": "Single", "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0},
    {"name": "Samsung Galaxy S22 Ultra", "arch": "Single", "P_peak": 45.0, "E_supply": 19.25, "T_A": 59.0},
    {"name": "Nothing Phone (2)", "arch": "Single", "P_peak": 45.0, "E_supply": 18.10, "T_A": 55.0},
    {"name": "Google Pixel 9 Pro XL", "arch": "Single", "P_peak": 37.0, "E_supply": 19.48, "T_A": 79.0},
    {"name": "Google Pixel 8 Pro", "arch": "Single", "P_peak": 30.0, "E_supply": 19.44, "T_A": 81.0},
    {"name": "Samsung Galaxy S24", "arch": "Single", "P_peak": 25.0, "E_supply": 15.40, "T_A": 75.0},
    {"name": "Samsung Galaxy S23", "arch": "Single", "P_peak": 25.0, "E_supply": 15.02, "T_A": 80.0},
    {"name": "Samsung Galaxy A55", "arch": "Single", "P_peak": 25.0, "E_supply": 19.25, "T_A": 85.0},
    {"name": "Samsung Galaxy A54", "arch": "Single", "P_peak": 25.0, "E_supply": 19.25, "T_A": 82.0},
    {"name": "Samsung Galaxy A34", "arch": "Single", "P_peak": 25.0, "E_supply": 19.25, "T_A": 84.0},
    {"name": "Google Pixel 7 Pro", "arch": "Single", "P_peak": 23.0, "E_supply": 19.25, "T_A": 109.0},
    {"name": "Samsung Galaxy S10", "arch": "Single", "P_peak": 15.0, "E_supply": 13.09, "T_A": 108.0},
    {"name": "Samsung Galaxy S9", "arch": "Single", "P_peak": 15.0, "E_supply": 11.55, "T_A": 107.0},
    {"name": "Samsung Galaxy S8", "arch": "Single", "P_peak": 15.0, "E_supply": 11.55, "T_A": 100.0},
    {"name": "Nokia 2.4", "arch": "Single", "P_peak": 5.0, "E_supply": 17.33, "T_A": 215.0},
    {"name": "Samsung Galaxy A03 Core", "arch": "Single", "P_peak": 7.8, "E_supply": 19.25, "T_A": 205.0},

    # --- APPLE IPHONES & LG ---
    {"name": "Apple iPhone 16 Pro Max", "arch": "Single", "P_peak": 30.0, "E_supply": 18.04, "T_A": 117.0},
    {"name": "Apple iPhone 14 Pro Max", "arch": "Single", "P_peak": 29.0, "E_supply": 16.64, "T_A": 112.0},
    {"name": "Apple iPhone 15 Pro Max", "arch": "Single", "P_peak": 27.0, "E_supply": 17.02, "T_A": 109.0},
    {"name": "Apple iPhone 13 Pro Max", "arch": "Single", "P_peak": 27.0, "E_supply": 16.75, "T_A": 106.0},
    {"name": "Apple iPhone 11 Pro Max", "arch": "Single", "P_peak": 18.0, "E_supply": 15.04, "T_A": 120.0},
    {"name": "LG G7 ThinQ", "arch": "Single", "P_peak": 18.0, "E_supply": 11.55, "T_A": 108.0},
    {"name": "Apple iPhone XS Max", "arch": "Single", "P_peak": 15.0, "E_supply": 12.08, "T_A": 131.0},
    {"name": "Apple iPhone X", "arch": "Single", "P_peak": 15.0, "E_supply": 10.43, "T_A": 125.0},
    {"name": "Apple iPhone 8", "arch": "Single", "P_peak": 5.0, "E_supply": 7.01, "T_A": 148.0},
    {"name": "Apple iPhone 7 Plus", "arch": "Single", "P_peak": 5.0, "E_supply": 11.17, "T_A": 241.0}
]

# Calibrated parameters for delta = 0.0 (Pure MAE) under f_thermal = 1.0000
eta_low = 0.9670
C0_single_base = 0.4051
C0_dual_base = 2.6087
k = 1.1191
p = 0.1341

lines = []
lines.append("Below is the complete device-by-device prediction table under the primary calibrated configuration (`delta = 0.0 mins (Pure MAE Primary)`, `eta_low = 0.9670`, `C0_single_base = 0.4051 h^-1`, `C0_dual_base = 2.6087 h^-1`, `k = 1.1191`, `p = 0.1341`):")
lines.append("")
lines.append("| Smartphone Device Model      | Arch   | P_peak (W) | E_supply (Wh) | C_rate (h^-1) | P_eff (W) | F_system | `C0_effective` | `C0_base` | Benchmark `T_A` | Predicted `T_C` | Residual Error (`Delta`) | Error % |")
lines.append("| :--------------------------- | :----: | :--------: | :-----------: | :-----------: | :-------: | :------: | :------------: | :-------: | :-------------: | :-------------: | :----------------------: | :-----: |")

for d in devices:
    C_rate = d["P_peak"] / d["E_supply"]
    f_th = 1.0000
    C0_base = C0_dual_base if d["arch"] == "Dual" else C0_single_base
    C0_eff = C0_base * f_th
    
    if C_rate <= C0_eff:
        F_sys = eta_low
    else:
        denom = 1.0 + k * ((C_rate - C0_eff) ** p)
        F_sys = min(1.0, eta_low / denom)
        
    P_eff = d["P_peak"] * F_sys
    T_pred = (d["E_supply"] / P_eff) * 60.0
    err_m = T_pred - d["T_A"]
    err_pct = (err_m / d["T_A"]) * 100.0
    
    sign_d = "+" if err_m > 0 else ""
    sign_p = "+" if err_pct > 0 else ""
    
    lines.append(f"| **{d['name']}** | {d['arch']} | {d['P_peak']:.1f} W | {d['E_supply']:.2f} Wh | {C_rate:.2f} | {P_eff:.1f} W | {F_sys:.4f} | {C0_eff:.4f} | {C0_base:.4f} | {d['T_A']:.1f} m | {T_pred:.1f} m | {sign_d}{err_m:.1f} m | {sign_p}{err_pct:.1f}% |")

md_out = "\n".join(lines)
print(md_out)

with open("c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/modeling/section_8_2_method_c_huber_optimization_study/working_files/sec5_table_delta0_primary.md", "w", encoding="utf-8") as f:
    f.write(md_out)
