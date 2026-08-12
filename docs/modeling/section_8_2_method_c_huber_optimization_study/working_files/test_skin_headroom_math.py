import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

# iPhone 16 Pro Max specs:
# P_peak = 30.0 W, E_supply = 18.04 Wh
# C_rate = 30.0 / 18.04 = 1.663 h^-1
# stability_pct = 68.0% => power_ratio = (0.68)^3 = 0.3144 (f_thermal)
# C0_single_base = 0.4021 h^-1
# k = 1.0576, p = 0.2347, eta_low = 0.9679

P_peak = 30.0
E_supply = 18.04
C_rate = P_peak / E_supply # 1.663
f_thermal = (0.68) ** 3 # 0.3144
C0_single_base = 0.4021
k = 1.0576
p = 0.2347
eta_low = 0.9679

# CASE A: f_skin_headroom = 1.0000 (No skin cap reduction)
f_skin_A = 1.0000
C0_eff_A = C0_single_base * f_thermal * f_skin_A # 0.4021 * 0.3144 * 1.0 = 0.1264 h^-1
excess_C_A = C_rate - C0_eff_A # 1.663 - 0.1264 = 1.5366 h^-1
F_sys_A = eta_low / (1.0 + k * (excess_C_A ** p)) # 0.9679 / (1 + 1.0576 * (1.5366)^0.2347)
P_eff_A = P_peak * F_sys_A
T_pred_A = (E_supply / P_eff_A) * 60.0

# CASE B: f_skin_headroom = 0.8165 (18.35% decrease)
f_skin_B = 0.8165
C0_eff_B = C0_single_base * f_thermal * f_skin_B # 0.4021 * 0.3144 * 0.8165 = 0.1032 h^-1
excess_C_B = C_rate - C0_eff_B # 1.663 - 0.1032 = 1.5598 h^-1
F_sys_B = eta_low / (1.0 + k * (excess_C_B ** p)) # 0.9679 / (1 + 1.0576 * (1.5598)^0.2347)
P_eff_B = P_peak * F_sys_B
T_pred_B = (E_supply / P_eff_B) * 60.0

print("=== EXACT SENSITIVITY MATH FOR IPHONE 16 PRO MAX ===")
print(f"C_rate = {C_rate:.4f} h^-1")
print(f"CASE A (f_skin_headroom = 1.0000): C0_eff = {C0_eff_A:.4f} | excess_C = {excess_C_A:.4f} | F_sys = {F_sys_A:.4f} | P_eff = {P_eff_A:.2f} W | T_pred = {T_pred_A:.2f} mins")
print(f"CASE B (f_skin_headroom = 0.8165): C0_eff = {C0_eff_B:.4f} | excess_C = {excess_C_B:.4f} | F_sys = {F_sys_B:.4f} | P_eff = {P_eff_B:.2f} W | T_pred = {T_pred_B:.2f} mins")
print(f"Difference in C0_eff: {C0_eff_A - C0_eff_B:.4f} h^-1 (only {C0_eff_A - C0_eff_B:.4f} h^-1 change in excess C_rate!)")
print(f"Difference in F_system: {F_sys_A - F_sys_B:.4f} (from {F_sys_A:.4f} to {F_sys_B:.4f}, a tiny {((F_sys_A - F_sys_B)/F_sys_A)*100:.2f}% drop)")
print(f"Difference in Predicted Time: {T_pred_B - T_pred_A:.2f} minutes! (moves from {T_pred_A:.1f}m to {T_pred_B:.1f}m)")
