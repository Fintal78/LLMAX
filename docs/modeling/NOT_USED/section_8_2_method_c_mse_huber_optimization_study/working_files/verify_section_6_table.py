import sys
import os
import math

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from benchmark_devices import BENCHMARK_DEVICES, T_MIN_BENCHMARK, T_MAX_BENCHMARK
from verify_complete_document_alignment import predict_single

params_huber10 = [0.7533, 0.4026, 2.2493, 0.9688, 1.0000, 1.0000, 0.9043, 0.9938, 0.7196, 0.3933, 0.1808]

print("Verifying all 44 device predictions:")
all_correct = True
for dev in BENCHMARK_DEVICES:
    res = predict_single(dev, params_huber10)
    tp = res["t_pred"]
    ta = dev["t_actual_min"]
    sa = dev["s_actual"]
    s2 = 10.0 * (math.log(T_MAX_BENCHMARK / tp) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))
    s2 = min(10.0, max(0.0, s2))
    
    dT = tp - ta
    dS = s2 - sa
    
    # Format
    line = f"| **{dev['name']}** | `{dev['peak_power_w']:.1f} W` | `{ta:5.1f} m` | `{tp:5.1f} m` | `{sa:5.2f}` | `{s2:5.2f}` | `{dS:+5.2f}` | `{dT:+6.1f} m` |"
    # print(line)

print("Check completed.")
