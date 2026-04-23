"""
R_cond Negligibility Analysis for Smartphone Thermal Model
===========================================================
Compares full model (R_cond + R_conv) vs simplified model (R_conv only)
across diverse phone configurations.
"""
import math

def calc_thermal(config, include_rcond=True):
    """Calculate thermal model for a phone configuration."""
    name = config["name"]
    H, W, Z = config["H_mm"], config["W_mm"], config["Z_mm"]
    mass_kg = config["mass_g"] / 1000.0
    P_peak = config["P_peak_W"]
    
    k_front = config["k_front"]
    t_front = config["t_front"]
    seff_front = config["seff_front"]
    eratio_front = config["eratio_front"]
    
    k_frame = config["k_frame"]
    t_frame = config["t_frame"]
    seff_frame = config["seff_frame"]
    eratio_frame = config["eratio_frame"]
    
    k_back = config["k_back"]
    t_back = config["t_back"]
    seff_back = config["seff_back"]
    eratio_back = config["eratio_back"]
    
    diag_inch = config["diag_inch"]
    aspect_r = config["aspect_r"]
    
    Area_face = (H / 1000.0) * (W / 1000.0)
    Perimeter = 2 * (H + W) / 1000.0
    Area_frame = Perimeter * (Z / 1000.0) * 0.85
    Area_display_cm2 = (diag_inch * 2.54)**2 * (aspect_r / (aspect_r**2 + 1))
    
    A_front = Area_face * seff_front * eratio_front
    A_frame = Area_frame * seff_frame * eratio_frame
    A_back = Area_face * seff_back * eratio_back
    
    R_cond_front = t_front / (k_front * A_front) if include_rcond else 0.0
    R_cond_frame = t_frame / (k_frame * A_frame) if include_rcond else 0.0
    R_cond_back = t_back / (k_back * A_back) if include_rcond else 0.0
    
    h = config.get("h_conv", 10.0)
    R_conv_front = 1.0 / (h * A_front)
    R_conv_frame = 1.0 / (h * A_frame)
    R_conv_back = 1.0 / (h * A_back)
    
    R_front = R_cond_front + R_conv_front
    R_frame = R_cond_frame + R_conv_frame
    R_back = R_cond_back + R_conv_back
    
    G_total = (1.0/R_front) + (1.0/R_frame) + (1.0/R_back)
    R_total = 1.0 / G_total
    
    C = mass_kg * 850.0
    Tau = R_total * C
    
    exp_term = 1.0 - math.exp(-1200.0 / Tau)
    Z_th = R_total * exp_term
    P_adm = 20.0 / Z_th
    
    P_base = 0.40 + (0.0075 * Area_display_cm2)
    P_adm_soc = P_adm - P_base
    
    if P_adm_soc <= 0:
        ratio = 0.0
        stability = 0.0
    else:
        ratio = min(P_adm_soc / P_peak, 1.0)
        stability = 100.0 * (ratio ** 0.33)
    
    return {
        "name": name,
        "R_cond_front": R_cond_front, "R_conv_front": R_conv_front, "R_front": R_front,
        "R_cond_frame": R_cond_frame, "R_conv_frame": R_conv_frame, "R_frame": R_frame,
        "R_cond_back": R_cond_back, "R_conv_back": R_conv_back, "R_back": R_back,
        "R_total": R_total,
        "C": C, "Tau": Tau,
        "P_adm": P_adm, "P_base": P_base, "P_adm_soc": P_adm_soc,
        "ratio": ratio, "stability": stability,
        "A_front": A_front, "A_frame": A_frame, "A_back": A_back,
    }

configs = [
    {
        "name": "S24 Ultra (Glass+XL_VC+Ti)",
        "H_mm": 162.3, "W_mm": 79.0, "Z_mm": 8.6, "mass_g": 232,
        "P_peak_W": 14.0, "diag_inch": 6.8, "aspect_r": 9.0/19.5,
        "k_front": 1.1, "t_front": 0.0007, "seff_front": 0.25, "eratio_front": 1.0,
        "k_frame": 7.0, "t_frame": 0.003, "seff_frame": 0.40, "eratio_frame": 1.0,
        "k_back": 1.1, "t_back": 0.0006, "seff_back": 0.95, "eratio_back": 0.40,
    },
    {
        "name": "iPhone 16 PM (Glass+StdVC+Ti)",
        "H_mm": 163.0, "W_mm": 77.6, "Z_mm": 8.25, "mass_g": 227,
        "P_peak_W": 14.5, "diag_inch": 6.9, "aspect_r": 9.0/19.5,
        "k_front": 1.1, "t_front": 0.0007, "seff_front": 0.25, "eratio_front": 1.0,
        "k_frame": 7.0, "t_frame": 0.003, "seff_frame": 0.40, "eratio_frame": 1.0,
        "k_back": 1.1, "t_back": 0.0006, "seff_back": 0.60, "eratio_back": 0.40,
    },
    {
        "name": "Aluminum Unibody (Metal+NoVC+Al)",
        "H_mm": 147.6, "W_mm": 71.6, "Z_mm": 7.8, "mass_g": 187,
        "P_peak_W": 9.0, "diag_inch": 6.1, "aspect_r": 9.0/19.5,
        "k_front": 1.1, "t_front": 0.0007, "seff_front": 0.25, "eratio_front": 1.0,
        "k_frame": 190.0, "t_frame": 0.003, "seff_frame": 1.00, "eratio_frame": 1.0,
        "k_back": 190.0, "t_back": 0.0006, "seff_back": 0.60, "eratio_back": 0.40,
    },
    {
        "name": "Budget Polymer (Plastic+NoVC+Plastic)",
        "H_mm": 164.0, "W_mm": 75.8, "Z_mm": 8.9, "mass_g": 193,
        "P_peak_W": 3.2, "diag_inch": 6.6, "aspect_r": 9.0/20.0,
        "k_front": 1.1, "t_front": 0.0007, "seff_front": 0.25, "eratio_front": 1.0,
        "k_frame": 0.3, "t_frame": 0.003, "seff_frame": 0.05, "eratio_frame": 1.0,
        "k_back": 0.3, "t_back": 0.0006, "seff_back": 0.05, "eratio_back": 0.40,
    },
    {
        "name": "Gaming Fan (Glass+Fan+Al)",
        "H_mm": 163.6, "W_mm": 76.4, "Z_mm": 8.9, "mass_g": 225,
        "P_peak_W": 19.5, "diag_inch": 6.8, "aspect_r": 9.0/20.0,
        "k_front": 1.1, "t_front": 0.0007, "seff_front": 0.25, "eratio_front": 1.0,
        "k_frame": 190.0, "t_frame": 0.003, "seff_frame": 1.00, "eratio_frame": 1.0,
        "k_back": 1.1, "t_back": 0.0006, "seff_back": 0.95, "eratio_back": 0.40,
        "h_conv": 30.0,
    },
    {
        "name": "SS Frame (Glass+Graphene+SS)",
        "H_mm": 160.8, "W_mm": 78.1, "Z_mm": 8.3, "mass_g": 240,
        "P_peak_W": 14.5, "diag_inch": 6.7, "aspect_r": 9.0/19.5,
        "k_front": 1.1, "t_front": 0.0007, "seff_front": 0.25, "eratio_front": 1.0,
        "k_frame": 16.0, "t_frame": 0.003, "seff_frame": 0.40, "eratio_frame": 1.0,
        "k_back": 1.1, "t_back": 0.0006, "seff_back": 0.45, "eratio_back": 0.40,
    },
]

print("=" * 120)
print("R_cond NEGLIGIBILITY ANALYSIS - Smartphone Thermal Model")
print("=" * 120)

print("\n>>> DETAILED PATH BREAKDOWN: Galaxy S24 Ultra <<<")
full = calc_thermal(configs[0], include_rcond=True)
simp = calc_thermal(configs[0], include_rcond=False)

print(f"\n{'Path':<12} {'R_cond (K/W)':>14} {'R_conv (K/W)':>14} {'R_path (K/W)':>14} {'R_cond/R_conv':>14} {'R_cond/R_path':>14}")
print("-" * 84)
for path_name, rc, rv, rp in [
    ("Front",  full["R_cond_front"], full["R_conv_front"], full["R_front"]),
    ("Frame",  full["R_cond_frame"], full["R_conv_frame"], full["R_frame"]),
    ("Back",   full["R_cond_back"],  full["R_conv_back"],  full["R_back"]),
]:
    pct_of_conv = (rc / rv) * 100
    pct_of_path = (rc / rp) * 100
    print(f"{path_name:<12} {rc:>14.4f} {rv:>14.2f} {rp:>14.2f} {pct_of_conv:>13.3f}% {pct_of_path:>13.3f}%")

print(f"\nR_total (Full Model):       {full['R_total']:.4f} K/W")
print(f"R_total (Without R_cond):   {simp['R_total']:.4f} K/W")
print(f"Absolute Difference:        {abs(full['R_total'] - simp['R_total']):.4f} K/W")
print(f"Relative Difference:        {abs(full['R_total'] - simp['R_total'])/full['R_total']*100:.3f}%")

print(f"\nP_adm  (Full): {full['P_adm']:.3f} W    vs    (Simplified): {simp['P_adm']:.3f} W    (Delta: {abs(full['P_adm']-simp['P_adm']):.3f} W)")
print(f"P_adm_soc (Full): {full['P_adm_soc']:.3f} W    vs    (Simplified): {simp['P_adm_soc']:.3f} W")
print(f"Ratio     (Full): {full['ratio']:.4f}        vs    (Simplified): {simp['ratio']:.4f}")
print(f"Stability (Full): {full['stability']:.1f}%         vs    (Simplified): {simp['stability']:.1f}%")

print("\n\n" + "=" * 120)
print("COMPARATIVE SUMMARY: All Configurations (Full Model vs. Simplified / No R_cond)")
print("=" * 120)

header = f"{'Configuration':<40} {'R_tot Full':>10} {'R_tot Simp':>10} {'Delta%':>8} {'Stab Full':>10} {'Stab Simp':>10} {'Delta':>8}"
print(header)
print("-" * len(header))

for cfg in configs:
    f = calc_thermal(cfg, include_rcond=True)
    s = calc_thermal(cfg, include_rcond=False)
    delta_r = abs(f["R_total"] - s["R_total"]) / f["R_total"] * 100
    delta_s = abs(f["stability"] - s["stability"])
    print(f"{cfg['name']:<40} {f['R_total']:>10.2f} {s['R_total']:>10.2f} {delta_r:>7.3f}% {f['stability']:>9.1f}% {s['stability']:>9.1f}% {delta_s:>7.2f}pp")

print("\n\n" + "=" * 120)
print("PER-PATH R_cond / R_conv RATIO (% of convective resistance)")
print("=" * 120)

header2 = f"{'Configuration':<40} {'Front':>10} {'Frame':>10} {'Back':>10} {'Max':>10}"
print(header2)
print("-" * len(header2))

for cfg in configs:
    f = calc_thermal(cfg, include_rcond=True)
    pct_f = (f["R_cond_front"] / f["R_conv_front"]) * 100
    pct_m = (f["R_cond_frame"] / f["R_conv_frame"]) * 100
    pct_b = (f["R_cond_back"] / f["R_conv_back"]) * 100
    mx = max(pct_f, pct_m, pct_b)
    print(f"{cfg['name']:<40} {pct_f:>9.3f}% {pct_m:>9.3f}% {pct_b:>9.3f}% {mx:>9.3f}%")

print("\n\nCONCLUSION:")
print("-" * 80)
max_delta_r = 0
max_delta_s = 0
max_rcond_ratio = 0
for cfg in configs:
    f = calc_thermal(cfg, include_rcond=True)
    s = calc_thermal(cfg, include_rcond=False)
    dr = abs(f["R_total"] - s["R_total"]) / f["R_total"] * 100
    ds = abs(f["stability"] - s["stability"])
    max_delta_r = max(max_delta_r, dr)
    max_delta_s = max(max_delta_s, ds)
    pct_f = (f["R_cond_front"] / f["R_conv_front"]) * 100
    pct_m = (f["R_cond_frame"] / f["R_conv_frame"]) * 100
    pct_b = (f["R_cond_back"] / f["R_conv_back"]) * 100
    max_rcond_ratio = max(max_rcond_ratio, pct_f, pct_m, pct_b)

print(f"Maximum R_total deviation across all configs:   {max_delta_r:.3f}%")
print(f"Maximum Stability deviation across all configs: {max_delta_s:.2f} percentage points")
print(f"Maximum R_cond/R_conv ratio on any single path: {max_rcond_ratio:.3f}%")
