import re

DOCS_DIR = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs"
FILES = [
    rf"{DOCS_DIR}\scoring_rules.md",
    rf"{DOCS_DIR}\scoring_constants.md",
    rf"{DOCS_DIR}\proposed_data_structure.md",
    rf"{DOCS_DIR}\data_sources.md",
    rf"{DOCS_DIR}\data_structure_guidelines.md"
]

# We are looking for any pattern that looks like a sub-subsection (e.g. 8.4.1)
# That isn't part of a Golden Ring reference table (like 3.1.0 or 6.1.0 or 5.2.0)
# We exclude IP addresses or common version strings by ensuring it has spaces/brackets around it.

pattern = re.compile(r'(?<!\d\.)\b(\d{1,2}\.\d{1,2}\.\d{1,2})\b(?!\.\d)')

with open("deep_scan_audit.txt", "w", encoding="utf-8") as out:
    for filepath in FILES:
        out.write(f"\n====================================\n")
        out.write(f"FILE: {filepath.split('\\')[-1]}\n")
        out.write(f"====================================\n")
        
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                matches = pattern.findall(line)
                if matches:
                    # Filter out the known valid reference tables to reduce noise
                    filtered_matches = [m for m in matches if m not in ['6.1.0', '6.3.0', '3.1.0', '3.3.0', '5.2.0']]
                    if filtered_matches:
                        out.write(f"L{i+1}: {line.strip()}\n")
                        
print("Deep scan complete.")
