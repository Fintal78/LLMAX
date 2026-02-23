import json
import re

FILE = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\proposed_data_structure.md"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
data = json.loads(json_match.group(1))

with open("json_keys.txt", "w", encoding="utf-8") as out:
    for k, v in data.items():
        out.write(k + "\n")
        if isinstance(v, dict):
            for sub_k in v.keys():
                out.write("  " + sub_k + "\n")
