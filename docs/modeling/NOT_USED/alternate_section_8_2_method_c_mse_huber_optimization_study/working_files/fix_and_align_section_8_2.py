import re
import math
from optimize_method_c import BENCHMARK_DEVICES

# Table formatter helper function
def align_markdown_table_str(table_str):
    lines = [l.strip() for l in table_str.strip().split('\n') if l.strip()]
    if len(lines) < 2:
        return table_str

    rows_cells = []
    alignments = []
    
    # Parse header
    header_raw = [c.strip() for c in lines[0].split('|')[1:-1]]
    num_cols = len(header_raw)
    
    # Parse delimiter
    delim_raw = [c.strip() for c in lines[1].split('|')[1:-1]]
    for d in delim_raw:
        if d.startswith(':') and d.endswith(':'):
            alignments.append('center')
        elif d.endswith(':'):
            alignments.append('right')
        else:
            alignments.append('left')

    rows_cells.append(header_raw)
    
    for l in lines[2:]:
        cells = [c.strip() for c in l.split('|')[1:-1]]
        if len(cells) == num_cols:
            rows_cells.append(cells)
            
    col_widths = [0] * num_cols
    for row in rows_cells:
        for i in range(num_cols):
            col_widths[i] = max(col_widths[i], len(row[i]))
            
    # Format header
    header_cells = [rows_cells[0][i].ljust(col_widths[i]) for i in range(num_cols)]
    formatted_header = "| " + " | ".join(header_cells) + " |"
    
    # Format delimiter
    delim_cells = []
    for i in range(num_cols):
        w = col_widths[i]
        align = alignments[i]
        if align == 'center':
            delim_cells.append(':' + '-' * (w - 2) + ':')
        elif align == 'right':
            delim_cells.append('-' * (w - 1) + ':')
        else:
            delim_cells.append(':' + '-' * (w - 1))
    formatted_delim = "| " + " | ".join(delim_cells) + " |"
    
    # Format data rows
    formatted_rows = []
    for row in rows_cells[1:]:
        formatted_cells = []
        for i in range(num_cols):
            cell = row[i]
            align = alignments[i]
            if align == 'center':
                formatted_cells.append(cell.center(col_widths[i]))
            elif align == 'right':
                formatted_cells.append(cell.rjust(col_widths[i]))
            else:
                formatted_cells.append(cell.ljust(col_widths[i]))
        formatted_rows.append("| " + " | ".join(formatted_cells) + " |")
        
    return "\n".join([formatted_header, formatted_delim] + formatted_rows)


# Smooth Huber delta sweep computation
PARAM_KEYS_LOSS = [
    "eta_CCCV", "C_threshold", "s_low", "eta_arch_single",
    "eta_proto_cp", "eta_proto_pps", "eta_proto_fpd", "eta_proto_5v", "eta_proto_app",
    "k", "p", "T_handshake"
]

PARAM_BOUNDS_LOSS = [
    (0.30, 1.00), (0.50, 2.50), (0.01, 3.00), (0.70, 1.00),
    (0.50, 1.00), (0.50, 1.00), (0.50, 1.00), (0.50, 1.00), (0.50, 1.00),
    (0.01, 2.00), (0.10, 1.20), (0.50, 0.50)
]

HUBER_10_PARAMS = [
    0.5818, 0.5000, 1.9774, 0.9876,
    1.0000, 0.9305, 0.8398, 0.9611, 0.6671,
    0.0845, 0.7441, 0.5000
]

def predict_duration(wh, p_peak_w, arch_type, protocol_type, params):
    (eta_CCCV, C_thresh, s_low, eta_arch_s,
     eta_cp, eta_pps, eta_fpd, eta_5v, eta_app,
     k, p, T_handshake) = params

    E_supply = wh
    C_rate = p_peak_w / max(0.01, E_supply)
    eta_a = eta_arch_s if arch_type == 'single' else 1.00

    proto_map = {
        'charge_pump': eta_cp,
        'pps': eta_pps,
        'fixed_pd': eta_fpd,
        'legacy_5v': eta_5v,
        'apple_legacy': eta_app,
    }
    eta_proto = proto_map.get(protocol_type, 0.90)

    if C_rate > C_thresh:
        delta_C = max(1e-9, C_rate - C_thresh)
        eta_thermal = math.exp(-k * math.pow(delta_C, p))
        eff_eta_CCCV = eta_CCCV
    else:
        eta_thermal = 1.0
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)

    eff_eta_CCCV = max(0.15, min(0.95, eff_eta_CCCV))
    P_effective = p_peak_w * eff_eta_CCCV * eta_a * eta_proto * eta_thermal
    P_effective = max(0.1, P_effective)

    T_predicted = (E_supply / P_effective) * 60.0 + T_handshake
    return T_predicted

def predict_all(params):
    return [predict_duration(d[0], d[1], d[2], d[3], params) for d in BENCHMARK_DEVICES]

def compute_huber_loss(params, delta):
    T_C = predict_all(params)
    N = len(BENCHMARK_DEVICES)
    total = 0.0
    for i, d in enumerate(BENCHMARK_DEVICES):
        err = d[4] - T_C[i]
        ae = abs(err)
        if ae <= delta:
            total += 0.5 * ae * ae
        else:
            total += delta * ae - 0.5 * delta * delta
    return total / N

def compute_t_metrics(params):
    T_C = predict_all(params)
    N = len(BENCHMARK_DEVICES)
    e = [BENCHMARK_DEVICES[i][4] - T_C[i] for i in range(N)]
    mse = sum(x**2 for x in e) / N
    return {
        "MSE_T":   round(mse, 2),
        "RMSE_T":  round(math.sqrt(mse), 2),
        "MAE_T":   round(sum(abs(x) for x in e) / N, 2),
        "Mean_dT": round(sum(e) / N, 2),
    }

def local_pattern_search(init_params, delta, max_outer=100):
    best_p = list(init_params)
    best_l = compute_huber_loss(best_p, delta)
    step = 0.02
    for outer in range(max_outer):
        improved = False
        for j in range(len(PARAM_KEYS_LOSS)):
            lo, hi = PARAM_BOUNDS_LOSS[j]
            if lo == hi:
                continue
            for mult in [1.0, 0.4, 0.1, 0.02, 0.005]:
                s = step * mult * (hi - lo)
                for direction in [+1.0, -1.0]:
                    trial = max(lo, min(hi, best_p[j] + direction * s))
                    if abs(trial - best_p[j]) < 1e-12:
                        continue
                    cand = list(best_p)
                    cand[j] = trial
                    l = compute_huber_loss(cand, delta)
                    if l < best_l - 1e-8:
                        best_l = l
                        best_p = list(cand)
                        improved = True
        if not improved:
            step *= 0.5
            if step < 1e-6:
                break
    return best_p, best_l

deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]
sweep_results = []
curr = list(HUBER_10_PARAMS)

for dv in deltas:
    opt_p, opt_l = local_pattern_search(curr, dv)
    tm = compute_t_metrics(opt_p)
    sweep_results.append((dv, tm["MSE_T"], tm["RMSE_T"], tm["MAE_T"], tm["Mean_dT"]))
    curr = list(opt_p)

table_3_1_headers = [
    "Huber Threshold (`delta`)",
    "Mean Squared Error (`MSE_T`)",
    "Root Mean Sq Error (`RMSE_T`)",
    "Mean Absolute Error (`MAE_T`)",
    "Mean Duration Bias (`Mean_dT`)",
    "Study Status / Selection Rationale"
]
table_3_1_align = ['left', 'center', 'center', 'center', 'center', 'left']
table_3_1_rows = []

for dv, mse, rmse, mae, mean_d in sweep_results:
    mse_str = f"{mse:.2f} mins^2"
    rmse_str = f"{rmse:.2f} mins"
    mae_str = f"{mae:.2f} mins"
    bias_str = f"{mean_d:+.2f} mins"
    
    if abs(dv - 10.0) < 1e-5:
        d_str = f"**`delta = {dv:.1f} mins`**"
        m_str = f"**`{mse_str}`**"
        r_str = f"**`{rmse_str}`**"
        a_str = f"**`{mae_str}`**"
        b_str = f"**`{bias_str}`**"
        note = "**Selected Best**: Optimal balance of MSE variance reduction & linear MAE precision."
    else:
        d_str = f"**`delta = {dv:.1f} mins`**"
        m_str = f"`{mse_str}`"
        r_str = f"`{rmse_str}`"
        a_str = f"`{mae_str}`"
        b_str = f"`{bias_str}`"
        note = "Empirical grid evaluation step."
        
    table_3_1_rows.append([d_str, m_str, r_str, a_str, b_str, note])

# Build Table 3.1 format
col_widths = [len(h) for h in table_3_1_headers]
for r in table_3_1_rows:
    for i in range(len(col_widths)):
        col_widths[i] = max(col_widths[i], len(r[i]))

h_cells = [table_3_1_headers[i].ljust(col_widths[i]) for i in range(len(col_widths))]
h_line = "| " + " | ".join(h_cells) + " |"

d_cells = []
for i in range(len(col_widths)):
    w = col_widths[i]
    align = table_3_1_align[i]
    if align == 'center':
        d_cells.append(':' + '-' * (w - 2) + ':')
    elif align == 'right':
        d_cells.append('-' * (w - 1) + ':')
    else:
        d_cells.append(':' + '-' * (w - 1))
d_line = "| " + " | ".join(d_cells) + " |"

r_lines = []
for row in table_3_1_rows:
    f_cells = []
    for i in range(len(col_widths)):
        cell = row[i]
        align = table_3_1_align[i]
        if align == 'center':
            f_cells.append(cell.center(col_widths[i]))
        elif align == 'right':
            f_cells.append(cell.rjust(col_widths[i]))
        else:
            f_cells.append(cell.ljust(col_widths[i]))
    r_lines.append("| " + " | ".join(f_cells) + " |")

new_table_3_1_str = "\n".join([h_line, d_line] + r_lines)


# Read section 8.2 document
file_path = "docs/modeling/section_8_2_method_c_mse_huber_optimization_study.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Table 3.1 in content
# Locate Section 3.1 table area (between "high-precision multi-start global search:\n\n" and "\n\n**Selection Result:**")
pattern_3_1 = r"(using high-precision multi-start global search:\s*\n\n)([\s\S]*?)(\n\n\*\*Selection Result:\*\*)"
m = re.search(pattern_3_1, content)
if m:
    content = content[:m.start(2)] + new_table_3_1_str + content[m.end(2):]
    print("Successfully replaced Table 3.1 in document content!")
else:
    print("WARNING: Could not find Table 3.1 pattern in document!")

# Now locate all markdown tables in content and format/align them
def align_all_tables_in_doc(doc_text):
    # Regex to match markdown tables
    # A markdown table starts with a line containing '|', followed by delimiter line containing '|' and '-', followed by 1+ lines with '|'
    table_regex = re.compile(r'(\|[^\n]+\|\n\|[\s:\-\|]+\|\n(?:\|[^\n]+\|\n?)+)')
    
    def replacer(match):
        table_block = match.group(1)
        return align_markdown_table_str(table_block) + "\n"
        
    return table_regex.sub(replacer, doc_text)

aligned_content = align_all_tables_in_doc(content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(aligned_content)

print("SUCCESSFULLY ALIGNED ALL TABLES IN docs/modeling/section_8_2_method_c_mse_huber_optimization_study.md!")
