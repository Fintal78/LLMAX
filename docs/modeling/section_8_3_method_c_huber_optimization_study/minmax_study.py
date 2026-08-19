k = 1.1232
p = 0.2194
c0 = 0.7778

scenarios = [
    {"name": "Ultra-Fast Concept (4000mAh, 100W, Fan)", "cap": 4000, "p_max": 100, "f_trans": 0.83},
    {"name": "Fastest Reality (Xiaomi 14U: 5000mAh, 80W, Fan)", "cap": 5000, "p_max": 80, "f_trans": 0.83},
    {"name": "Slowest Reality (Big Batt legacy: 6000mAh, 5W, No Fan)", "cap": 6000, "p_max": 5, "f_trans": 0.72},
    {"name": "Absolute Worst (Rugged legacy: 10000mAh, 5W, No Fan)", "cap": 10000, "p_max": 5, "f_trans": 0.72},
    {"name": "iPhone 15 Pro Max (4422mAh, 15W, MagSafe)", "cap": 4422, "p_max": 15, "f_trans": 0.82},
]

for s in scenarios:
    e_wh = s['cap'] * 3.85 / 1000.0
    c_rate = s['p_max'] / e_wh
    base = max(0.0, c_rate - c0)
    f_therm = 1.0 / (1.0 + k * (base ** p))
    p_eff = s['p_max'] * s['f_trans'] * f_therm
    t_pred = 60.0 * (e_wh / p_eff)
    print(f"{s['name']}: {t_pred:.1f} mins (P_eff: {p_eff:.1f}W)")
