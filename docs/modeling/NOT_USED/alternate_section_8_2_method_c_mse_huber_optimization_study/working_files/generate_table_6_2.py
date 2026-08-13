import math
from benchmark_devices import BENCHMARK_DEVICES

p = {
    "eta_CCCV": 0.7533, "C_threshold": 0.4026, "s_low": 2.2493,
    "eta_arch_single": 0.9688, "eta_proto_cp": 1.0000, "eta_proto_pps": 1.0000,
    "eta_proto_fpd": 0.9043, "eta_proto_5v": 0.9938, "eta_proto_app": 0.7196,
    "k": 0.3933, "p": 0.1808, "T_handshake": 0.5000
}

T_MIN_BENCHMARK = 9.0
T_MAX_BENCHMARK = 241.0

# Table order 1: T_A, T_C, dT (mins), dT (%), S_A, S_C, dS (pts), dS (%), Link
rows = []
for d in BENCHMARK_DEVICES:
    Wh = d["battery_wh"]
    P_peak = d["peak_power_w"]
    arch = d["architecture"]
    proto = d["protocol"]
    T_A = d["t_actual_min"]
    S_A = d["s_actual"]
    
    C_rate = P_peak / Wh
    if C_rate > p["C_threshold"]:
        eff_eta_CCCV = p["eta_CCCV"]
    else:
        eff_eta_CCCV = min(1.0, p["eta_CCCV"] + p["s_low"] * (p["C_threshold"] - C_rate))
    
    eta_arch = 1.0 if arch == "dual" else p["eta_arch_single"]
    
    proto_map = {
        "charge_pump": p["eta_proto_cp"],
        "pps": p["eta_proto_pps"],
        "fixed_pd": p["eta_proto_fpd"],
        "legacy_5v": p["eta_proto_5v"],
        "apple_legacy": p["eta_proto_app"]
    }
    eta_proto = proto_map[proto]
    
    if C_rate > p["C_threshold"]:
        eta_thermal = math.exp(-p["k"] * ((C_rate - p["C_threshold"]) ** p["p"]))
    else:
        eta_thermal = 1.0
        
    P_eff = P_peak * eff_eta_CCCV * eta_arch * eta_proto * eta_thermal
    T_C = (Wh / P_eff) * 60.0 + p["T_handshake"]
    
    raw_s = 10.0 * (math.log(T_MAX_BENCHMARK / T_C) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))
    S_C = min(10.0, max(0.0, raw_s))
    
    # Exact table strings
    s_a_disp = f"{S_A:5.2f}"
    s_c_disp = f"{S_C:5.2f}"
    t_a_disp = f"{T_A:5.1f} m"
    t_c_disp = f"{T_C:5.1f} m"
    p_peak_disp = f"{P_peak:5.1f} W"
    
    dS = round(S_C, 2) - round(S_A, 2)
    dT = round(T_C, 1) - round(T_A, 1)
    
    if abs(dS) < 0.005:
        dS_disp = "+0.00" if dS >= 0 else "-0.00"
    else:
        dS_disp = f"{dS:+5.2f}"
        
    if abs(dT) < 0.05:
        dT_disp = "  0.0 m"
    else:
        dT_disp = f"{dT:+6.1f} m"
        
    dT_pct = (T_C - T_A) / T_A * 100.0
    dT_pct_disp = f"{dT_pct:+5.1f}%"
    
    if S_A > 0:
        dS_pct = (S_C - S_A) / S_A * 100.0
        dS_pct_disp = f"{dS_pct:+5.1f}%"
    else:
        dS_pct_disp = "  N/A  "
        
    link = d.get("gsmarena_url", "")
    link_md = f"[GSMArena Review]({link})"
    
    rows.append({
        "name": f"**{d['name']}**",
        "P_peak": f"`{p_peak_disp}`",
        "T_A": f"`{t_a_disp}`",
        "T_C": f"`{t_c_disp}`",
        "dT": f"`{dT_disp}`",
        "dT_pct": f"`{dT_pct_disp}`",
        "S_A": f"`{s_a_disp}`",
        "S_C": f"`{s_c_disp}`",
        "dS": f"`{dS_disp}`",
        "dS_pct": f"`{dS_pct_disp}`",
        "link": link_md
    })

headers = [
    "Smartphone Device Model", "P_peak (W)", "T_A (mins)", "T_C (mins)",
    "dT (mins)", "dT (%)", "S_A (pts)", "S_C (pts)", "dS (pts)", "dS (%)", "GSMArena Benchmark Link"
]

keys = ["name", "P_peak", "T_A", "T_C", "dT", "dT_pct", "S_A", "S_C", "dS", "dS_pct", "link"]

col_widths = {k: len(h) for k, h in zip(keys, headers)}
for r in rows:
    for k in keys:
        col_widths[k] = max(col_widths[k], len(r[k]))

header_line = "| " + " | ".join(f"{h:<{col_widths[k]}}" if k in ["name", "link"] else f"{h:^{col_widths[k]}}" for k, h in zip(keys, headers)) + " |"
sep_line = "| " + " | ".join(f":{'-'*(col_widths[k]-2)} " if k == "name" else f":{'-'*(col_widths[k]-2)}:" for k in keys) + " |"

out_lines = [header_line, sep_line]
for r in rows:
    row_str = "| " + " | ".join(f"{r[k]:<{col_widths[k]}}" if k in ["name", "link"] else f"{r[k]:^{col_widths[k]}}" for k in keys) + " |"
    out_lines.append(row_str)

table_str = "\n".join(out_lines)
with open("scratch/formatted_table_6_2.md", "w") as f:
    f.write(table_str)

print("Saved formatted table to scratch/formatted_table_6_2.md")
