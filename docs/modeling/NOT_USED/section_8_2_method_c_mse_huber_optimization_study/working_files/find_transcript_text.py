import json

log_path = r"C:\Users\Ion\.gemini\antigravity-ide\brain\820aacbf-b3ce-4e2d-adfa-5c58204758e4\.system_generated\logs\transcript.jsonl"

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        if "Statistical Assumption:" in line or "Gauss-Markov Theorem" in line:
            obj = json.loads(line)
            content = str(obj.get("content", ""))
            idx = content.find("Option 1: Pure Mean Squared Error")
            if idx != -1:
                print(content[idx:idx+2500])
                print("="*60)
