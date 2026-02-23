import re

with open(r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_constants.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("headers_const.txt", "w", encoding="utf-8") as out:
    for line in lines:
        if line.startswith("**") or line.startswith("### "):
            out.write(line)
