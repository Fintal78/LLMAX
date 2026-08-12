import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

docs_dir = r'c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs'

devices_found = []

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith('.md'):
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if any(k in line.lower() for k in ['tdsi', 'stability', '3dmark', 'wild life']):
                        # Check if device name or stability percentage is in line
                        if '%' in line or '10.' in line or '0.' in line or 'Score' in line or 'Method A' in line:
                            print(f"{file} L{i+1}: {line.strip()[:120]}")
