import math
import json

from optimize_method_c import BENCHMARK_DEVICES, PARAM_KEYS, PARAM_BOUNDS

# Read optimization results JSON to get exact Huber Loss (Option 3) parameters
with open("scratch/optimization_results.json", "r") as f:
    res = json.load(f)

huber_params = res["params"]["huber_10"]
(C_thresh, k, p, eta_base, s_low, T_handshake,
 F_cp, F_pps, F_fpd, F_5v, F_app, F_arch_param) = huber_params

print(f"Huber 10 Calibrated Parameters:")
for name, val in zip(PARAM_KEYS, huber_params):
    print(f"  {name:<18} = {val:.4f}")

print("\nEvaluating 44-device detailed parameter breakdown:")
print(f"{'Device':<28} {'Wh':>5} {'P_peak':>6} {'C_rate':>6} {'Arch':>6} {'Protocol':>12} {'F_arch':>6} {'F_proto':>7} {'F_Crate':>7} {'eff_eta':>7} {'P_eff':>6} {'T_C':>6}")
print("-" * 115)

device_params_table = []
for d in BENCHMARK_DEVICES:
    wh, p_peak_w, arch_type, protocol_type, T_A, S_A, name, url = d
    C_rate = p_peak_w / max(0.01, wh)

    F_a = F_arch_param if arch_type == 'dual' else 1.0

    proto_map = {
        'charge_pump': F_cp,
        'pps': F_pps,
        'fixed_pd': F_fpd,
        'legacy_5v': F_5v,
        'apple_legacy': F_app,
    }
    F_proto = proto_map.get(protocol_type, 1.0)

    if C_rate > C_thresh:
        F_Crate = 1.0 / (1.0 + k * math.pow(max(1e-9, C_rate - C_thresh), p))
        eff_eta = eta_base
    else:
        F_Crate = 1.0
        eff_eta = eta_base + s_low * (C_thresh - C_rate)

    eff_eta_clamped = max(0.15, min(0.95, eff_eta))
    P_effective = p_peak_w * eff_eta_clamped * F_a * F_proto * F_Crate
    P_effective_clamped = max(0.1, P_effective)

    T_predicted = (wh / P_effective_clamped) * 60.0 + T_handshake

    row = {
        "name": name,
        "wh": wh,
        "p_peak_w": p_peak_w,
        "c_rate": round(C_rate, 2),
        "arch_type": arch_type,
        "protocol_type": protocol_type,
        "F_arch": round(F_a, 4),
        "F_proto": round(F_proto, 4),
        "F_Crate": round(F_Crate, 4),
        "eff_eta": round(eff_eta_clamped, 4),
        "P_eff": round(P_effective_clamped, 2),
        "T_C": round(T_predicted, 1)
    }
    device_params_table.append(row)
    print(f"{name:<28} {wh:>5.2f} {p_peak_w:>6.1f} {C_rate:>6.2f} {arch_type:>6} {protocol_type:>12} {F_a:>6.4f} {F_proto:>7.4f} {F_Crate:>7.4f} {eff_eta_clamped:>7.4f} {P_effective_clamped:>6.2f} {T_predicted:>6.1f}")
