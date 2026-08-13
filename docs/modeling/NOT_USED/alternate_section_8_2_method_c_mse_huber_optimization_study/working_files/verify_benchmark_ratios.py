import math
import json

from optimize_method_c import BENCHMARK_DEVICES

# Test both proposed baseline parameters and calibrated loss-based parameters on benchmark devices
from test_loss_based_model import BASELINE_PARAMS_LOSS, p_rat_hub, p_exp_hub, predict_duration_loss

test_devices = [
    ("Apple iPhone 8", 5.0, 148.0),
    ("Samsung Galaxy S10", 15.0, 108.0),
    ("Google Pixel 8 Pro", 30.0, 81.0),
    ("Samsung Galaxy S24 Ultra", 45.0, 59.0),
    ("Xiaomi 13 Pro", 120.0, 19.0),
    ("Realme GT3", 240.0, 9.6),
]

print("=== BENCHMARK RATIO SANITY CHECK ON REPRESENTATIVE PHONES ===")
print(f"{'Phone':<26} {'Peak(W)':>7} {'T_Bench':>8} {'T_Base(Rat)':>11} {'T_Opt(Rat)':>11} {'T_Opt(Exp)':>11}")
print("-" * 80)

for d in BENCHMARK_DEVICES:
    if d[6] in [x[0] for x in test_devices]:
        wh, p_peak_w, arch_type, protocol_type, T_A, S_A, name, url = d
        t_base_rat = predict_duration_loss(wh, p_peak_w, arch_type, protocol_type, BASELINE_PARAMS_LOSS, "rational")
        t_opt_rat  = predict_duration_loss(wh, p_peak_w, arch_type, protocol_type, p_rat_hub, "rational")
        t_opt_exp  = predict_duration_loss(wh, p_peak_w, arch_type, protocol_type, p_exp_hub, "exponential")
        print(f"{name:<26} {p_peak_w:>7.1f} {T_A:>8.1f} {t_base_rat:>11.1f} {t_opt_rat:>11.1f} {t_opt_exp:>11.1f}")
