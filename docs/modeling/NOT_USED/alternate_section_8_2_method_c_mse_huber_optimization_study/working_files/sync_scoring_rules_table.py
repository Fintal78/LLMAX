import json

with open("scratch/optimization_results.json", "r") as f:
    data = json.load(f)

h10 = [h for h in data["huber_sweep"] if h["delta"] == 10.0][0]
preds = h10["device_predictions"]

# Generate new table
lines = []
lines.append("##### Empirical Verification Table: Method A vs. Method C Across 44 Authentic Devices")
lines.append("Below is the empirical alignment verification table evaluating 44 real-world smartphones across all charging tiers from 5W to 240W, comparing verified GSMArena laboratory benchmarks (Method A) against the analytical physics predictor (Method C) calibrated under Huber Loss (`delta = 10.0 mins`) with Strategy 2 (Benchmark Aligned Bounds).\n")

lines.append("| Smartphone Device Model | P_peak (W) | T_A (mins) | T_C (mins) | S_A (pts) | S_C (pts) | dS (pts) | dT (mins) | GSMArena Benchmark Link |")
lines.append("| :---------------------- | :--------: | :--------: | :--------: | :-------: | :-------: | :------: | :-------: | :---------------------- |")

for d in preds:
    link_text = f"[{d['name']} Benchmark]({d['gsmarena_url']})"
    lines.append(f"| **{d['name']:<26}** | `{d['peak_power_w']:>5.1f} W` | `{d['t_actual']:>5.1f} m` | `{d['t_pred']:>5.1f} m` | `{d['s_actual']:>5.2f}` | `{d['s_pred_s2']:>5.2f}` | `{d['dS_s2']:>+5.2f}` | `{d['dT']:>+5.1f} m` | {link_text} |")

lines.append("\n> [!IMPORTANT]")
lines.append("> **Overall Systematic Bias & Accuracy Summary:**")
lines.append("> ")
lines.append("> ##### 1. Summary Metrics Comparison")
lines.append("> | Metric | Full Dataset (44 Smartphones) | Excluding Nokia 2.4 (43 Smartphones) | Excluding Nokia 2.4 & A03 Core (42 Smartphones) |")
lines.append("> | :----- | :---------------------------: | :----------------------------------: | :----------------------------------------------: |")
lines.append("> | **Mean Duration Difference (`T_C - T_A`)** | **`-0.34` minutes** | **`-1.83` minutes** | **`-1.92` minutes** |")
lines.append("> | **Mean Absolute Duration Error (`|T_C - T_A|`)** | **`6.81` minutes** | **`5.49` minutes** | **`5.58` minutes** |")
lines.append("> | **Mean Score Difference (`S_C - S_A`)** | **`-0.012` points** | **`+0.006` points** | **`+0.006` points** |")
lines.append("> | **Mean Absolute Score Difference (`|S_C - S_A|`)** | **`0.256` points** | **`0.243` points** | **`0.249` points** |")
lines.append("> ")
lines.append("> ##### 2. Outlier Justification & Technical Explanation")
lines.append("> *   **Nokia 2.4 Physical Duration Skew:** Nokia 2.4 combines a large 4,500 mAh battery with a minimal 5W (5V/1A) charger, producing a physical predicted duration `T_C = 278.6` minutes (`4.64` hours) vs. GSMArena benchmark `T_A = 215.0` minutes (a single-device duration delta of **`+63.6` minutes**).")
lines.append("> *   **Samsung Galaxy A03 Core Calibrated Accuracy:** Under the low-power efficiency scaling, Samsung Galaxy A03 Core (5,000 mAh battery with 7.8W charging) produces `T_C = 206.9` minutes vs. GSMArena benchmark `T_A = 205.0` minutes (a single-device duration delta of only **`+1.9` minutes**).")
lines.append("> *   **Score Floor Protection:** In Method C scoring, any predicted duration `T_C >= 241.0` minutes is clamped to the score floor of `241.0` minutes (receiving Score `0.00`). Because Nokia 2.4 receives Method C Score `0.00` (Method A Score `0.35`), these extreme physical duration tails are trimmed by the `T_max = 241.0` minute score floor and do **not** distort the score framework.\n")

new_block = "\n".join(lines)

with open("docs/scoring_rules.md", "r", encoding="utf-8") as f:
    content = f.read()

# Locate target block in scoring_rules.md
start_marker = "##### Empirical Verification Table: Method A vs. Method C Across 44 Authentic Devices"
end_marker = "#### 8.2.2 Ecosystem Interoperability & Advanced Hardware Features"

idx_start = content.find(start_marker)
idx_end = content.find(end_marker)

if idx_start != -1 and idx_end != -1:
    updated_content = content[:idx_start] + new_block + "\n" + content[idx_end:]
    with open("docs/scoring_rules.md", "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("SUCCESS: Updated scoring_rules.md empirical table!")
else:
    print(f"ERROR: Could not locate markers. start: {idx_start}, end: {idx_end}")
