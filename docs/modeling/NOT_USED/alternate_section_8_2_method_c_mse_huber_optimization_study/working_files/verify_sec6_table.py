import math
import numpy as np
from benchmark_devices import BENCHMARK_DEVICES

p = {
    "eta_CCCV": 0.7533, "C_threshold": 0.4026, "s_low": 2.2493,
    "eta_arch_single": 0.9688, "eta_proto_cp": 1.0000, "eta_proto_pps": 1.0000,
    "eta_proto_fpd": 0.9043, "eta_proto_5v": 0.9938, "eta_proto_app": 0.7196,
    "k": 0.3933, "p": 0.1808, "T_handshake": 0.5000
}

T_MIN_BENCHMARK = 9.0
T_MAX_BENCHMARK = 241.0

print("Checking Section 6.1 & 6.2 rows:")
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
    
    dS = S_C - S_A
    dT = T_C - T_A
    
    print(f"{d['name']:<26} | P_eff={P_eff:5.2f}W | T_C={T_C:5.1f}m | T_A={T_A:5.1f}m | S_C={S_C:4.2f} | S_A={S_A:4.2f} | dS={dS:+5.2f} | dT={dT:+5.1f}m")
