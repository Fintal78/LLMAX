import re

with open("docs/scoring_rules.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

for i, line in enumerate(lines):
    if re.search(r"###.*6\.10|###.*8\.2", line):
        print(f"Line {i+1}: {line}")
