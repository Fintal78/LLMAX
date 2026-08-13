import re
from align_tables import format_table

def clean_cell_contents(cell):
    c = cell.strip()
    # If cell is like **Name    **, change to **Name**
    bold_match = re.match(r'^\*\*(.*?)\*\*$', c)
    if bold_match:
        inner = bold_match.group(1).strip()
        return f"**{inner}**"
    
    # If link text is like [Device Name Benchmark](url), change to [GSMArena Review](url) for compactness
    link_match = re.match(r'^\[(.*?)\]\((.*?)\)$', c)
    if link_match:
        text, url = link_match.group(1).strip(), link_match.group(2).strip()
        if "Benchmark" in text or "Review" in text:
            return f"[GSMArena Review]({url})"
    return c

def process_file_compact(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
        
    new_lines = []
    curr_table = []
    
    for line in lines:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            # clean inner cell contents before formatting
            raw_cells = [c.strip() for c in line.strip()[1:-1].split('|')]
            cleaned_cells = [clean_cell_contents(c) for c in raw_cells]
            curr_table.append('| ' + ' | '.join(cleaned_cells) + ' |')
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
    result = process_file_compact(target)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(result)
    print("All tables compacted and aligned successfully.")
