import os
import re

DOCS_DIR = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs"

MD_FILES = [
    "scoring_rules.md",
    "scoring_constants.md",
    "proposed_data_structure.md",
    "data_sources.md",
    "data_structure_guidelines.md",
    "battery_scoring_model.md"
]

pattern = re.compile(r'(Section\s+\d+|\[.*?\]\(#.*?\))', re.IGNORECASE)

with open("reference_audit.txt", "w", encoding="utf-8") as out:
    for filename in MD_FILES:
        filepath = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(filepath):
            continue
            
        out.write(f"\n====================================\n")
        out.write(f"FILE: {filename}\n")
        out.write(f"====================================\n")
        
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                matches = pattern.findall(line)
                if matches:
                    out.write(f"L{i+1}: {line.strip()}\n")
                    
print("Audit complete.")
