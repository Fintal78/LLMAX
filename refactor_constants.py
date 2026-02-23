import re

OLD_FILE = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_constants.md"
NEW_FILE = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_constants_new.md"

SUB_MAP = {
    # 2. Display
    "2.2": "2.4", "2.3": "2.2", "2.4": "2.3", "2.6": "2.6", "2.7": "2.7", "2.8": "2.10", "2.9": "2.9", "2.10": "2.8", "2.11": "2.11",
    # 3. Processing -> 6
    "3.1": "6.1", "3.2": "6.2", "3.3": "6.3", "3.4": "6.10", "3.6": "6.6", "3.8": "6.8", "3.10": "6.4",
    # 4. Camera -> 4
    "4.1": "4.1", "4.2": "4.2", "4.3": "4.3", "4.5": "4.6", "4.6": "4.5", "4.7": "4.7", "4.9": "4.11", "4.12": "4.14", "4.13": "4.8", "4.15": "4.15",
    # 5. Battery -> 8
    "5.1": "8.1", "5.2": "8.2", "5.3": "8.3", "5.4": "8.5", "5.5": "8.4",
    # 6. Software -> 5
    "6.1": "5.1",
    # 7. Connectivity & Audio
    "7.4": "7.4", # Bluetooth
    # 9. Financial -> 9
    "9.1": "9.1",
}

# The remaining ones mapping straight over (e.g. 1.4, 1.5, 1.6)
for i in [1]:
    for j in range(1, 10):
        key = f"{i}.{j}"
        if key not in SUB_MAP:
            SUB_MAP[key] = key

NEW_SECTIONS = {
    1: "**1. Design & Build**",
    2: "**2. Display**",
    3: "**3. Audio**",
    4: "**4. Camera Systems**",
    5: "**5. Software & Longevity**",
    6: "**6. Processing Power**",
    7: "**7. Connectivity & Sensors**",
    8: "**8. Battery & Charging**",
    9: "**9. Financial & Value**",
}

with open(OLD_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

preamble = []
idx = 0
while idx < len(lines):
    if lines[idx].startswith("**1."):
        break
    preamble.append(lines[idx])
    idx += 1

subsections = {}
current_sub = None
current_lines = []

while idx < len(lines):
    line = lines[idx]
    if line.startswith("**"):
        idx += 1
        continue
    
    m = re.match(r'^### (\d+\.\d+)', line)
    if m:
        if current_sub:
            subsections[current_sub] = current_lines
        current_sub = m.group(1)
        current_lines = [line]
    else:
        if current_sub:
            current_lines.append(line)
    idx += 1

if current_sub:
    subsections[current_sub] = current_lines

# Reorder
mapped_subsections = {}
for old_id, content in subsections.items():
    if old_id in SUB_MAP:
        new_id = SUB_MAP[old_id]
        
        # update title
        new_title = re.sub(r'^### \d+\.\d+', f'### {new_id}', content[0])
        content[0] = new_title
        mapped_subsections[new_id] = content

# Sort by new id
def sort_key(k):
    parts = k.split('.')
    return (int(parts[0]), int(parts[1]))

ordered_keys = sorted(mapped_subsections.keys(), key=sort_key)

with open(NEW_FILE, "w", encoding="utf-8") as out:
    for p in preamble:
        out.write(p)
    
    current_sec = None
    for k in ordered_keys:
        sec = int(k.split('.')[0])
        if sec != current_sec:
            out.write(f"\n{NEW_SECTIONS[sec]}\n\n")
            current_sec = sec
        for line in mapped_subsections[k]:
            out.write(line)
