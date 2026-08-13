import re

with open("docs/scoring_rules.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if re.search(r"6\.10|8\.2|thermal|battery", line, re.IGNORECASE):
        print(f"Line {i+1}: {line.strip()[:100]}")
