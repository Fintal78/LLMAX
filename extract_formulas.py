import json
import re

formulas = []
current_section = ""

with open("docs/scoring_rules.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith("## ") or line.startswith("### "):
        current_section = line.strip()
    
    if "Formula" in line or "score =" in line.lower() or "score=" in line.lower():
        # Get context (2 lines before and 5 lines after)
        start = max(0, i - 2)
        end = min(len(lines), i + 8)
        context = "".join(lines[start:end])
        formulas.append({"section": current_section, "line": line.strip(), "context": context})

with open("formula_extract.json", "w", encoding="utf-8") as f:
    json.dump(formulas, f, indent=2)
print(f"Extracted {len(formulas)} formulas.")
