import re
import os

OLD_FILE = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_rules_original.md"
NEW_FILE = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_rules.md"

# Define the exact mapping of Old Subsection Numbers to New Subsection Numbers
SUB_MAP = {
    "1.1": "1.1", "1.2": "1.2", "1.3": "1.3", "1.4": "1.4", "1.5": "1.5", "1.6": "1.6",
    
    "2.1": "2.1", "2.3": "2.2", "2.4": "2.3", "2.5": "2.4", "2.2": "2.5", 
    "2.6": "2.6", "2.7": "2.7", "2.10": "2.8", "2.9": "2.9", "2.8": "2.10", "2.11": "2.11",
    
    "8.1": "3.1", "8.2": "3.2", "8.3": "3.3", "8.4": "3.4",
    
    "4.1": "4.1", "4.2": "4.2", "4.3": "4.3", "4.4": "4.4", "4.6": "4.5", "4.5": "4.6", 
    "4.7": "4.7", "4.13": "4.8", "4.14": "4.9", "4.8": "4.10", "4.9": "4.11", "4.10": "4.12", 
    "4.11": "4.13", "4.12": "4.14", "4.15": "4.15", "4.16": "4.16", "4.17": "4.17", "4.18": "4.18",
    
    "6.1": "5.1", "6.3": "5.2", "6.2": "5.3",
    
    "3.1": "6.1", "3.2": "6.2", "3.3": "6.3", "3.10": "6.4", "3.5": "6.5", "3.6": "6.6", 
    "3.7": "6.7", "3.8": "6.8", "3.9": "6.9", "3.4": "6.10",
    
    "7.1": "7.1", "7.2": "7.2", "7.3": "7.3", "7.4": "7.4", "7.5": "7.7", "7.7": "7.6", 
    "7.6": "7.5", "7.9": "7.8", "7.8": "7.9",
    
    "5.1": "8.1", "5.2": "8.2", "5.3": "8.3", "5.5": "8.4", "5.4": "8.5", "5.6": "8.6",
    
    "9.1": "9.1", "9.3": "9.2", "9.2": "9.3",
}

NEW_STRUCTURE = {
    1: ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6"],
    2: ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "2.10", "2.11"],
    3: ["3.1", "3.2", "3.3", "3.4"],
    4: ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9", "4.10", "4.11", "4.12", "4.13", "4.14", "4.15", "4.16", "4.17", "4.18"],
    5: ["5.1", "5.2", "5.3"],
    6: ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7", "6.8", "6.9", "6.10"],
    7: ["7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9"],
    8: ["8.1", "8.2", "8.3", "8.4", "8.5", "8.6"],
    9: ["9.1", "9.2", "9.3"],
}

SEC_MAP = {1: 1, 2: 2, 3: 6, 4: 4, 5: 8, 6: 5, 7: 7, 8: 3, 9: 9}

try:
    with open(OLD_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
except UnicodeDecodeError:
    with open(OLD_FILE, "r", encoding="utf-16") as f:
        lines = f.readlines()

preamble = []
tail_end = []
idx = 0

# 1. Preamble
while idx < len(lines):
    if lines[idx].startswith("## 🟣 1."):
        break
    preamble.append(lines[idx])
    idx += 1

sections = {}
current_sec_id = None
current_sec_lines = []

# 2. Parse sections 1 to 9
while idx < len(lines):
    line = lines[idx]
    if line.startswith("## 🟣 10."):
        if current_sec_id is not None:
            sections[current_sec_id] = current_sec_lines
        break
    
    m = re.match(r'^## 🟣 (\d+)\.', line)
    if m:
        if current_sec_id is not None:
            sections[current_sec_id] = current_sec_lines
        current_sec_id = int(m.group(1))
        current_sec_lines = [line]
    else:
        current_sec_lines.append(line)
    idx += 1

# 3. Everything from 10 onwards is dumped into tail_end verbatim
while idx < len(lines):
    tail_end.append(lines[idx])
    idx += 1


new_sections_data = {}

for old_sec_id, sec_lines in sections.items():
    new_sec_id = SEC_MAP[old_sec_id]
    
    # Update the section header title number
    hdr = sec_lines[0]
    hdr = re.sub(r'## 🟣 \d+\.', f'## 🟣 {new_sec_id}.', hdr)
    sec_lines[0] = hdr
    
    # Parse subsections
    sec_preamble = []
    subsections = {}
    
    s_idx = 1
    while s_idx < len(sec_lines):
        line = sec_lines[s_idx]
        if line.startswith("### A.") or line.startswith("### B.") or line.startswith("### C.") or line.startswith("### D.") or line.startswith("### 🔹 "):
            break
        sec_preamble.append(line)
        s_idx += 1
    
    current_sub_id = None
    current_sub_lines = []
    pending_letter_headers = []
    
    while s_idx < len(sec_lines):
        line = sec_lines[s_idx]
        if line.startswith("### A.") or line.startswith("### B.") or line.startswith("### C.") or line.startswith("### D."):
            pending_letter_headers.append(line)
            s_idx += 1
            continue
            
        m = re.match(r'^### 🔹 (\d+\.\d+)', line)
        if m:
            if current_sub_id is not None:
                subsections[current_sub_id] = current_sub_lines
            current_sub_id = m.group(1)
            current_sub_lines = pending_letter_headers + [line]
            pending_letter_headers = []
        else:
            if current_sub_id is not None:
                current_sub_lines.append(line)
            else:
                sec_preamble.append(line)
        s_idx += 1
        
    if current_sub_id is not None:
        subsections[current_sub_id] = current_sub_lines

    reordered_lines = []
    reordered_lines.extend(sec_preamble)
    
    if new_sec_id in NEW_STRUCTURE:
        for new_sub_num in NEW_STRUCTURE[new_sec_id]:
            # Find which old sub num maps to this new sub num
            target_old_num = None
            for old_n, new_n in SUB_MAP.items():
                if new_n == new_sub_num:
                    target_old_num = old_n
                    break
            
            if target_old_num and target_old_num in subsections:
                lines_to_add = subsections[target_old_num]
                # Update the header in the lines
                for i in range(len(lines_to_add)):
                    if lines_to_add[i].startswith("### 🔹 "):
                        lines_to_add[i] = re.sub(r'### 🔹 \d+\.\d+', f'### 🔹 {new_sub_num}', lines_to_add[i])
                        break
                reordered_lines.extend(lines_to_add)
    
    new_sections_data[new_sec_id] = [sec_lines[0]] + reordered_lines


with open(NEW_FILE, "w", encoding="utf-8") as out:
    for line in preamble:
        out.write(line)
    for i in range(1, 10):
        if i in new_sections_data:
            for line in new_sections_data[i]:
                out.write(line)
    for line in tail_end:
        out.write(line)

print("Markdown extraction and reordering complete (safely mapping Section 1).")
