import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Extract rules headers
with open('docs/scoring_rules.md', 'r', encoding='utf-8') as f:
    rules_lines = f.readlines()

# Map Number -> Title
num_to_title = {}
# Map simplified title -> Number
title_to_num = {}

for line in rules_lines:
    line = line.strip()
    # Match strings exactly like '### 🔹 2.5 Resolution Density'
    # Also '#### 6.1.0 CPU Core'
    m = re.match(r'#{1,4}\s*(?:🔹\s*)?(\d+\.\d+(?:\.\d+)?)\s+(.*)', line)
    if m:
        num = m.group(1)
        raw_title = m.group(2)
        # remove bolding, parenthetical abbreviations e.g. (HFS)
        title = raw_title.replace('*', '').split(' (')[0].split(' - ')[0].split(' — ')[0].strip()
        num_to_title[num] = title
        
        # Also map title keywords to number (simplified)
        simplified_title = re.sub(r'[^a-z0-9]', '', title.lower())
        title_to_num[simplified_title] = num

# Extract constants headers
with open('docs/scoring_constants.md', 'r', encoding='utf-8') as f:
    const_lines = f.readlines()

print('Checking scoring_constants.md...')
errors = []
for i, line in enumerate(const_lines, 1):
    line = line.strip()
    m = re.match(r'#{1,4}\s*(?:🔹\s*)?(\d+\.\d+(?:\.\d+)?)\s+(.*)', line)
    if m:
        c_num = m.group(1)
        c_title = m.group(2).replace('*', '').split(' (')[0].split(' - ')[0].split(' — ')[0].strip()
        
        simpl_c_title = re.sub(r'[^a-z0-9]', '', c_title.lower())
        
        expected_title = num_to_title.get(c_num)
        expected_num = title_to_num.get(simpl_c_title)
        
        if expected_title:
            simpl_expected_title = re.sub(r'[^a-z0-9]', '', expected_title.lower())
            # If titles are very different, it's a mismatch
            if simpl_c_title != simpl_expected_title and simpl_c_title not in simpl_expected_title and simpl_expected_title not in simpl_c_title:
                 print(f'L{i:4d}: Mismatch on {c_num}!')
                 print(f'       Constants => "{c_title}"')
                 print(f'       Rules     => "{expected_title}"')
                 if expected_num and c_num != expected_num:
                     print(f'       SUGGESTION: Constants="{c_title}" should likely be section {expected_num}')
        else:
             print(f'L{i:4d}: Unknown section {c_num} in rules! (Constants says "{c_title}")')
             if expected_num and c_num != expected_num:
                 print(f'       SUGGESTION: Constants="{c_title}" should likely be section {expected_num}')
