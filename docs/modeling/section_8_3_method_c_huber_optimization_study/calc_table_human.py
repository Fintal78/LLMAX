devices = [
    {'name': 'Xiaomi 14 Ultra', 'cap': 5000, 'v_nom': 3.85, 'p_max': 80, 'f_trans': 0.83, 't_act': 46},
    {'name': 'OnePlus 12', 'cap': 5400, 'v_nom': 3.85, 'p_max': 50, 'f_trans': 0.83, 't_act': 55},
    {'name': 'Samsung Galaxy S24 Ultra', 'cap': 5000, 'v_nom': 3.85, 'p_max': 15, 'f_trans': 0.78, 't_act': 125},
    {'name': 'iPhone 15 Pro Max', 'cap': 4422, 'v_nom': 3.85, 'p_max': 15, 'f_trans': 0.82, 't_act': 135},
    {'name': 'Google Pixel 8 Pro', 'cap': 5050, 'v_nom': 3.85, 'p_max': 23, 'f_trans': 0.83, 't_act': 140}
]

k = 1.1232
p = 0.2194
c0 = 0.7778

print("| Device                   | Cap (mAh) | V_nom (V) | E_wh    | P_max (W) | C_rate | F_trans | F_therm | P_eff (W) | T_act (m) | T_pred (m) | Err (m) | Err (%) |")
print("| :----------------------- | :-------- | :-------- | :------ | :-------- | :----- | :------ | :------ | :-------- | :-------- | :--------- | :------ | :------ |")

for d in devices:
    e_wh = round(d['cap'] * d['v_nom'] / 1000.0, 4)
    c_rate = round(d['p_max'] / e_wh, 4)
    
    base = max(0.0, c_rate - c0)
    f_therm = round(1.0 / (1.0 + k * (base ** p)), 4)
    
    p_eff = round(d['p_max'] * d['f_trans'] * f_therm, 4)
    t_pred = round(60.0 * (e_wh / p_eff), 1)
    
    err_m = round(t_pred - d['t_act'], 1)
    err_pct = round((err_m / d['t_act']) * 100.0, 1)
    
    # Ensure + signs for positive errors
    err_m_str = f"{err_m:+.1f}" if err_m != 0.0 else "+0.0"
    err_pct_str = f"{err_pct:+.1f}%" if err_pct != 0.0 else "+0.0%"
    
    print(f"| {d['name']:<24} | {d['cap']:<9} | {d['v_nom']:<9.2f} | {e_wh:<7.4f} | {d['p_max']:<9} | {c_rate:<6.4f} | {d['f_trans']:<7.2f} | {f_therm:<7.4f} | {p_eff:<9.4f} | {d['t_act']:<9} | {t_pred:<10.1f} | {err_m_str:<7} | {err_pct_str:<7} |")
