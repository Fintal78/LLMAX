import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search for any device with Method A benchmark stability score (3DMark Wild Life / Steel Nomad Stress Test)

docs_path = r'c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs'

device_stability_map = {}

# Check CPU_tdsi_calibration_details.md and performance_scoring_weights_rationale.md
for fname in ['CPU_tdsi_calibration_details.md', 'performance_scoring_weights_rationale.md', 'proposed_data_structure.md']:
    fpath = os.path.join(docs_path, 'modeling', fname) if fname != 'proposed_data_structure.md' else os.path.join(docs_path, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
            # find matches like stability = XX.X% or TDSI = X.XX
            matches = re.findall(r'([A-Za-z0-9\s\+\-]{3,30}).*?(?:stability|TDSI).*?(\d{1,3}\.\d{1,4})', text, re.IGNORECASE)
            for m in matches:
                dev = m[0].strip()
                val = m[1]
                print(f"Found in {fname}: {dev} -> {val}")

