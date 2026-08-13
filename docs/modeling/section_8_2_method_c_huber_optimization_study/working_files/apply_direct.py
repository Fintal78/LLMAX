import os

path = r'c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\modeling\section_8_2_method_c_huber_optimization_study\section_8_2_method_c_huber_optimization_study.md'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for l in lines:
    if 'Below is the complete 44-device prediction dataset' in l:
        new_lines.append("Below is the complete 44-device prediction dataset under the primary calibrated configuration (`delta = 0.0 mins (Pure MAE Primary)`, `eta_low = 0.9670`, `C0_single_base = 0.4051 h^-1`, `C0_dual_base = 2.6087 h^-1`, `k = 1.1191`, `p = 0.1341`). Note that because `f_thermal = 1.0000` and `f_skin_headroom = 1.0000` across all devices in the baseline physical model, the effective thermal onset threshold `C0_effective` is identical to `C0_base` (`2.6087 h^-1` for 2S dual-cell and `0.4051 h^-1` for 1S single-cell).\n")
    elif '| Smartphone Device Model      | Arch   | P_peak  | E_supply | C_rate | P_eff  | F_system | C0_effective | C0_base |' in l:
        new_lines.append("| Smartphone Device Model      | Arch   | P_peak  | E_supply | C_rate | P_eff  | F_system | C0_effective | GSMArena Review Link |\n")
    elif '| :--------------------------- | :----: | :-----: | :------: | :----: | :----: | :------: | :----------: | :-----: |' in l:
        new_lines.append("| :--------------------------- | :----: | :-----: | :------: | :----: | :----: | :------: | :----------: | :-------------------: |\n")
    elif l.startswith('| **') and '2.6087' in l:
        new_l = l.replace('|    2.6087    |  2.6087 |', '|    2.6087    |')
        new_lines.append(new_l)
    elif l.startswith('| **') and '0.4051' in l:
        new_l = l.replace('|    0.4051    |  0.4051 |', '|    0.4051    |')
        new_lines.append(new_l)
    else:
        new_lines.append(l)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Direct replacement completed successfully.")
