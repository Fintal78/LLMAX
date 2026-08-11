import os

def align_table_block(table_lines):
    rows = []
    for line in table_lines:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 3 and parts[0] == '' and parts[-1] == '':
            rows.append(parts[1:-1])
        elif len(parts) >= 2:
            if parts[0] == '':
                parts = parts[1:]
            if parts and parts[-1] == '':
                parts = parts[:-1]
            rows.append(parts)
            
    if not rows:
        return table_lines
        
    num_cols = max(len(r) for r in rows)
    
    for r in rows:
        while len(r) < num_cols:
            r.append("")
            
    col_widths = []
    for c in range(num_cols):
        w = max(len(r[c]) for r in rows)
        col_widths.append(max(w, 3))
        
    aligned_lines = []
    for r_idx, row in enumerate(rows):
        formatted_cells = []
        for c_idx in range(num_cols):
            cell = row[c_idx]
            w = col_widths[c_idx]
            if r_idx == 1:
                has_left = cell.startswith(':')
                has_right = cell.endswith(':')
                
                if has_left and has_right:
                    f_cell = ':' + '-' * (w - 2) + ':'
                elif has_left:
                    f_cell = ':' + '-' * (w - 1)
                elif has_right:
                    f_cell = '-' * (w - 1) + ':'
                else:
                    f_cell = '-' * w
            else:
                f_cell = cell.ljust(w)
            formatted_cells.append(f_cell)
            
        aligned_lines.append("| " + " | ".join(formatted_cells) + " |")
        
    return aligned_lines

def align_file_tables(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]
        
    new_lines = []
    current_table = []
    
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            current_table.append(line)
        else:
            if current_table:
                aligned = align_table_block(current_table)
                new_lines.extend(aligned)
                current_table = []
            new_lines.append(line)
            
    if current_table:
        aligned = align_table_block(current_table)
        new_lines.extend(aligned)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines) + "\n")
        
    print(f"Successfully aligned all tables in {filepath}")

if __name__ == "__main__":
    align_file_tables(r"../section_8_2_method_c_huber_optimization_study.md")
