import numpy as np
from recalibrate_with_corrected_data import parse_and_correct_dataset

dataset = parse_and_correct_dataset()

# Optimal parameters from recalibration: delta=1.0 / delta=5.0
eta_low   = 0.9695
c0_single = 0.4051
c0_dual   = 2.6594
k         = 1.1128
p         = 0.1298
t_handshake = 0.5

print("--- 44-DEVICE DETAILED RESIDUAL & BRAND BREAKDOWN ---")
print(f"{'Device Name':<28} | {'Brand':<10} | {'P_peak':<6} | {'C_rate':<6} | {'Arch':<6} | {'T_A':<6} | {'T_C':<6} | {'Error':<7} | {'AbsErr':<6}")
print("-" * 105)

brand_errors = {}
errors_list = []

for d in dataset:
    name = d['name']
    brand = name.split()[0]
    e_supply = d['battery_wh']
    p_peak = d['p_peak']
    c_rate = p_peak / e_supply
    arch = d['arch']
    t_a = d['t_a']
    
    c0 = c0_dual if arch == 'dual' else c0_single
    diff = max(0.0, c_rate - c0)
    f_sys = min(1.0, max(0.01, eta_low / (1.0 + k * (diff**p))))
    p_eff = p_peak * f_sys
    t_c = (e_supply / p_eff) * 60.0 + t_handshake
    
    err = t_c - t_a
    abs_err = abs(err)
    
    errors_list.append((name, brand, p_peak, c_rate, arch, t_a, t_c, err, abs_err))
    
    if brand not in brand_errors:
        brand_errors[brand] = []
    brand_errors[brand].append(abs_err)

errors_list.sort(key=lambda x: x[8], reverse=True)

for item in errors_list:
    print(f"{item[0]:<28} | {item[1]:<10} | {item[2]:<6.1f} | {item[3]:<6.2f} | {item[4]:<6} | {item[5]:<6.1f} | {item[6]:<6.1f} | {item[7]:+7.1f} | {item[8]:<6.1f}")

print("\n--- MEAN ABSOLUTE ERROR (MAE_T) BY BRAND ---")
print(f"{'Brand':<15} | {'Count':<6} | {'MAE_T (mins)':<12}")
print("-" * 40)
for brand, errs in sorted(brand_errors.items(), key=lambda x: np.mean(x[1]), reverse=True):
    print(f"{brand:<15} | {len(errs):<6} | {np.mean(errs):<12.2f}")
