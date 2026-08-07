import re

def parse_row(row_str):
    # Strip leading and trailing '|'
    s = row_str.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    # Split by '|'
    cells = [c.strip() for c in s.split('|')]
    return cells

def format_table(table_lines):
    rows = [parse_row(line) for line in table_lines]
    if len(rows) < 2:
        return table_lines
    
    num_cols = max(len(r) for r in rows)
    # Pad rows that have fewer cells
    for r in rows:
        while len(r) < num_cols:
            r.append('')
            
    # Determine alignments from separator row (row 1)
    sep_row = rows[1]
    alignments = []
    for cell in sep_row:
        c = cell.strip()
        if c.startswith(':') and c.endswith(':'):
            alignments.append('center')
        elif c.endswith(':'):
            alignments.append('right')
        elif c.startswith(':'):
            alignments.append('left')
        else:
            alignments.append('left')
            
    # Calculate max width for each column (ignoring sep row for width)
    widths = [0] * num_cols
    for r_idx, r in enumerate(rows):
        if r_idx == 1:
            continue
        for c_idx, cell in enumerate(r):
            widths[c_idx] = max(widths[c_idx], len(cell))
            
    # Ensure minimum width of 3 for ':---:' or ':---'
    for c_idx in range(num_cols):
        widths[c_idx] = max(widths[c_idx], 3)
        
    formatted_lines = []
    for r_idx, r in enumerate(rows):
        if r_idx == 1:
            # Separator line
            sep_cells = []
            for c_idx in range(num_cols):
                w = widths[c_idx]
                align = alignments[c_idx]
                if align == 'center':
                    sep_cells.append(':' + '-' * (w - 2) + ':')
                elif align == 'right':
                    sep_cells.append('-' * (w - 1) + ':')
                else:
                    sep_cells.append(':' + '-' * (w - 1))
            formatted_lines.append('| ' + ' | '.join(sep_cells) + ' |')
        else:
            line_cells = []
            for c_idx, cell in enumerate(r):
                w = widths[c_idx]
                align = alignments[c_idx]
                if align == 'center':
                    line_cells.append(cell.center(w))
                elif align == 'right':
                    line_cells.append(cell.rjust(w))
                else:
                    line_cells.append(cell.ljust(w))
            formatted_lines.append('| ' + ' | '.join(line_cells) + ' |')
            
    return formatted_lines

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        
    new_lines = []
    curr_table = []
    
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            curr_table.append(line)
        else:
            if curr_table:
                new_lines.extend(format_table(curr_table))
                curr_table = []
            new_lines.append(line)
            
    if curr_table:
        new_lines.extend(format_table(curr_table))
        
    output_text = '\n'.join(new_lines) + '\n'
    return output_text

if __name__ == '__main__':
    target = 'docs/modeling/section_8_2_method_c_mse_huber_optimization_study.md'
    result = process_file(target)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(result)
    print("All tables formatted and aligned successfully.")
