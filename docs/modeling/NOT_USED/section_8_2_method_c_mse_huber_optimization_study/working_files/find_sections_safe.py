import re

with open("docs/scoring_rules.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()

with open("scratch/sections_found.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if re.search(r"###.*6\.10|###.*8\.2", line):
            out.write(f"Line {i+1}: {line}\n")

print("Wrote sections_found.txt")
