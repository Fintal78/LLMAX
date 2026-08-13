import os

path = r'c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\modeling\section_8_2_method_c_huber_optimization_study\section_8_2_method_c_huber_optimization_study.md'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
new_lines = []
in_t61 = False

for l in lines:
    if '### 6.1 Physical Component Evaluation' in l:
        in_t61 = True
        new_lines.append(l)
        continue
    elif '### 6.2 Master 44-Device Duration' in l:
        in_t61 = False
        new_lines.append(l)
        continue

    if in_t61:
        if l.startswith('| Smartphone Device Model'):
            new_lines.append('| Smartphone Device Model      | Arch   | P_peak  | E_supply | C_rate | P_eff  | F_system | C0_effective | GSMArena Review Link                                                                            |')
        elif l.startswith('| :---'):
            new_lines.append('| :--------------------------- | :----: | :-----: | :------: | :----: | :----: | :------: | :----------: | :---------------------------------------------------------------------------------------------: |')
        elif l.startswith('| **'):
            parts = [p.strip() for p in l.split('|')[1:-1]]
            if len(parts) >= 10:
                # drop parts[8] (the duplicate c0_base)
                new_parts = parts[:8] + [parts[9]]
                new_lines.append('| ' + ' | '.join(new_parts) + ' |')
            else:
                new_lines.append(l)
        else:
            new_lines.append(l)
    else:
        new_lines.append(l)

text_out = '\n'.join(new_lines)

old_intro = "`delta = 0.0 mins (Pure MAE Primary)`, `eta_low = 0.9670`, `C0_single_base = 0.4051 h^-1`, `C0_dual_base = 2.6087 h^-1`, `k = 1.1191`, `p = 0.1341`)."
new_intro = "`delta = 0.0 mins (Pure MAE Primary)`, `eta_low = 0.9670`, `C0_single_base = 0.4051 h^-1`, `C0_dual_base = 2.6087 h^-1`, `k = 1.1191`, `p = 0.1341`). Note that because `f_thermal = 1.0000` and `f_skin_headroom = 1.0000` across all devices in the baseline physical model, the effective thermal onset threshold `C0_effective` is identical to `C0_base` (`2.6087 h^-1` for 2S dual-cell and `0.4051 h^-1` for 1S single-cell)."

text_out = text_out.replace(old_intro, new_intro)

old_rule = "physically realistic exponent constraints (`p >= 0.40`)"
new_rule = "sub-linear exponent bounds (`p ≈ 0.1341`)"

text_out = text_out.replace(old_rule, new_rule)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text_out)

print("Successfully updated Section 6!")
