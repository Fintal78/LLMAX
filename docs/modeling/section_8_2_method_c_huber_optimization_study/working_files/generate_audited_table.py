import re
from recalibrate_with_corrected_data import parse_and_correct_dataset

dataset = parse_and_correct_dataset()

# Configuration 1: Full 44-device Unconstrained Huber (delta=1.0) Calibration
params_cfg1 = {
    'name': 'Full 44-Device Unconstrained Huber (delta=1.0)',
    'eta_low': 0.9695,
    'c0_single': 0.4051,
    'c0_dual': 2.6594,
    'k': 1.1128,
    'p': 0.1298,
    't_handshake': 0.5
}

# Configuration 2: Physically Sound (p >= 0.40) Calibration on Standard/Android Dataset (34 devices)
params_cfg2 = {
    'name': 'Physically Sound (p >= 0.40) Standard/Android Calibration',
    'eta_low': 0.9659,
    'c0_single': 0.3133,
    'c0_dual': 2.3236,
    'k': 0.8810,
    'p': 0.4000,
    't_handshake': 0.5
}

def generate_table(cfg):
    eta_low = cfg['eta_low']
    c0_single = cfg['c0_single']
    c0_dual = cfg['c0_dual']
    k = cfg['k']
    p = cfg['p']
    t_handshake = cfg['t_handshake']
    
    lines = []
    lines.append(f"### {cfg['name']}\n")
    lines.append(f"**Parameter Values Used:**")
    lines.append(f"- `eta_low` = **{eta_low:.4f}**")
    lines.append(f"- `C0_single` = **{c0_single:.4f} h^-1**")
    lines.append(f"- `C0_dual` = **{c0_dual:.4f} h^-1**")
    lines.append(f"- `k` = **{k:.4f}**")
    lines.append(f"- `p` = **{p:.4f}**")
    lines.append(f"- `T_handshake` = **{t_handshake:.1f} mins**\n")
    
    lines.append("| Device Model | Arch | P_peak (W) | C_rate (h^-1) | F_system | P_eff (W) | T_A (Actual) | T_C (Pred) | Delta (mins) | Error % |")
    lines.append("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    
    mae = 0
    rmse = 0
    
    for d in dataset:
        e_supply = d['battery_wh']
        p_peak = d['p_peak']
        c_rate = p_peak / e_supply
        arch = d['arch']
        t_a = d['t_a']
        
        c0 = c0_dual if arch == 'dual' else c0_single
        diff = max(0.0, c_rate - c0)
        f_system = eta_low / (1.0 + k * (diff ** p))
        f_system = min(1.0, max(0.01, f_system))
        
        p_effective = p_peak * f_system
        t_c = (e_supply / p_effective) * 60.0 + t_handshake
        
        delta = t_c - t_a
        error_pct = (delta / t_a) * 100.0
        
        mae += abs(delta)
        rmse += delta**2
        
        lines.append(f"| **{d['name']}** | {arch.capitalize()} | {p_peak:.1f} W | {c_rate:.2f} | {f_system:.4f} | {p_effective:.1f} W | {t_a:.1f} m | {t_c:.1f} m | {delta:+.1f} m | {error_pct:+.1f}% |")
        
    mae /= len(dataset)
    rmse = (rmse / len(dataset)) ** 0.5
    
    lines.append(f"\n*   **Population MAE_T:** `{mae:.2f} mins` | **RMSE_T:** `{rmse:.2f} mins`\n")
    return "\n".join(lines)

if __name__ == "__main__":
    table_content = "# Method C Detailed Audited 44-Device Results & Parameter Calibration\n\n"
    table_content += generate_table(params_cfg1)
    table_content += "\n---\n\n"
    table_content += generate_table(params_cfg2)
    print(table_content[:500])
