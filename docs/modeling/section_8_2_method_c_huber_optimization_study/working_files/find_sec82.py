import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_rules.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if "8.2" in line or "Method C" in line or "Wired Charging" in line or "Section 8" in line:
        print(f"Line {idx:<5}: {line.strip()[:100]}")
