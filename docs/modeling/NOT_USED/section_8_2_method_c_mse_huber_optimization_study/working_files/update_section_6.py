import json

with open("scratch/optimization_results.json", "r") as f:
    data = json.load(f)

matrix = data["device_matrix"]

lines = []
lines.append("## 6. Step 4: Master 55-Device Prediction Matrix & Final Evaluation (Huber Loss + Strategy 2)\n")
lines.append("The master evaluation table below details predicted physical charging durations (`T_C`) and mapped speed scores (`S_C`) across all 55 benchmark devices in the GSMArena laboratory dataset under the optimal setup (**Option 3: Huber Loss Model with Strategy 2 Benchmark Aligned Bounds**). All values are computed directly by [optimize_method_c.py](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/scratch/optimize_method_c.py):\n")
lines.append("| Device Model                 |  Power  | T_A (Bench) | T_C (Huber) |  Score A  | Score C (Optimal) | dScore (A-C) |   dT (A-C)  | Source                                                                                 |")
lines.append("| :--------------------------- | :-----: | :---------: | :---------: | :-------: | :---------------: | :----------: | :---------: | :------------------------------------------------------------------------------------- |")

for r in matrix:
    ds_val = r["dS"]
    dt_val = r["dT"]
    ds_str = f"+{ds_val:.2f}" if ds_val >= 0 else f"{ds_val:.2f}"
    dt_str = f"+{dt_val:.1f} m" if dt_val >= 0 else f"{dt_val:.1f} m"
    name_str = f"**{r['name']}**"
    power_str = f"{r['power_w']:.1f} W"
    ta_str = f"**{r['T_A']:.1f} m**"
    tc_str = f"**{r['T_C']:.1f} m**"
    sa_str = f"**{r['S_A']:.2f}**"
    sc_str = f"**{r['S_C']:.2f}**"
    ds_formatted = f"**{ds_str}**"
    dt_formatted = f"**{dt_str:^9}**"
    source_str = f"[GSMArena Review]({r['url']})"
    
    line = f"| {name_str:<28} | {power_str:>7} | {ta_str:>11} | {tc_str:>11} | {sa_str:>9} | {sc_str:>17} | {ds_formatted:>12} | {dt_formatted:>11} | {source_str:<86} |"
    lines.append(line)

new_section_6 = "\n".join(lines)

with open("scratch/section_6_table.md", "w") as f:
    f.write(new_section_6)

print("Created scratch/section_6_table.md successfully.")
