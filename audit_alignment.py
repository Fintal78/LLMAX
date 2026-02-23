import re
import json

DOCS_DIR = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs"
RULES = rf"{DOCS_DIR}\scoring_rules.md"
CONSTANTS = rf"{DOCS_DIR}\scoring_constants.md"
PDS = rf"{DOCS_DIR}\proposed_data_structure.md"

def extract_rules_subsections():
    subs = []
    with open(RULES, "r", encoding="utf-8") as f:
        for line in f:
            m = re.search(r'^### 🔹 (\d+\.\d+)', line)
            if m:
                subs.append(m.group(1))
    return set(subs), subs

def extract_constants_subsections():
    subs = []
    with open(CONSTANTS, "r", encoding="utf-8") as f:
        for line in f:
            m = re.search(r'^### (\d+\.\d+)', line)
            if m:
                subs.append(m.group(1))
    return set(subs), subs

def extract_json_subsections():
    with open(PDS, "r", encoding="utf-8") as f:
        content = f.read()
    
    json_match = re.search(r'```json\n(.*)\n```', content, re.DOTALL)
    if not json_match:
        return set(), []
        
    data = json.loads(json_match.group(1))
    subs = set()
    sub_list = []
    
    for top_k, val in data.items():
        if isinstance(val, dict):
            for k in val.keys():
                m = re.match(r'^(\d+)_(\d+)_', k)
                if m:
                    ext = f"{m.group(1)}.{m.group(2)}"
                    subs.add(ext)
                    sub_list.append(ext)
                else:
                    m2 = re.match(r'^(\d+)_(\d+)$', k)
                    if m2:
                        ext = f"{m2.group(1)}.{m2.group(2)}"
                        subs.add(ext)
                        sub_list.append(ext)
                        
    return set(subs), sub_list

def check_sequential_gaps(ordered_list):
    groups = {}
    for item in ordered_list:
        parts = item.split('.')
        if len(parts) == 2:
            sec, sub = int(parts[0]), int(parts[1])
            if sec not in groups:
                groups[sec] = []
            groups[sec].append(sub)
            
    warnings = []
    for sec in sorted(groups.keys()):
        subs = groups[sec] # ordered as they appeared in the document
        expected = 1
        for s in subs:
            if s != expected:
                warnings.append(f"GAP in Section {sec}: Expected {sec}.{expected} but found {sec}.{s}")
                expected = s + 1
            else:
                expected += 1
    return warnings

rules_set, rules_list = extract_rules_subsections()
const_set, const_list = extract_constants_subsections()
json_set, json_list = extract_json_subsections()

print("="*40)
print("1. SEQUENTIAL GAP CHECK (`scoring_rules.md`)")
print("="*40)
gaps = check_sequential_gaps(rules_list)
if not gaps:
    print("ALL CLEAR: No sequential subsection gaps found (e.g. jumping from 2.1 to 2.3).")
else:
    for g in gaps:
        print(f"WARNING: {g}")

print("\n" + "="*40)
print("2. CONSTANTS ORPHAN CHECK")
print("="*40)
# Everything in scoring_constants.md should exist in scoring_rules.md
orphans = const_set - rules_set
if not orphans:
    print("ALL CLEAR: Every subsection in scoring_constants.md exists in scoring_rules.md.")
else:
    print(f"WARNING: Found constants for non-existent subsections: {sorted(list(orphans))}")

print("\n" + "="*40)
print("3. JSON MAPPING CHECK")
print("="*40)
# Everything in scoring_rules.md should ideally be in the JSON
missing_in_json = rules_set - json_set - {'3.1.0', '6.1.0', '6.3.0', '3.3.0'} # Ignore reference tables
if not missing_in_json:
    print("ALL CLEAR: Every subsection in scoring_rules.md has a corresponding key in proposed_data_structure.md")
else:
    print(f"WARNING: Found rules missing from JSON structure: {sorted(list(missing_in_json))}")

missing_in_rules = json_set - rules_set - {'3.1.0', '6.1.0', '6.3.0', '3.3.0'}
if not missing_in_rules:
    print("ALL CLEAR: Every key in proposed_data_structure.md maps back to a valid scoring_rules.md subsection")
else:
    print(f"WARNING: Found JSON keys missing from rules: {sorted(list(missing_in_rules))}")

print("\n" + "="*40)
print("4. TOTAL SUBSECTION COUNT")
print("="*40)
print(f"scoring_rules.md subsections: {len(rules_set)}")
print(f"scoring_constants.md groups: {len(const_set)}")
print(f"JSON data structures mapped: {len(json_set)}")
