
file_path = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_rules.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_line = 114 # 0-indexed, so line 115
end_line = 124

print(f"Checking lines {start_line+1} to {end_line+1}")
for i in range(start_line, end_line):
    line = lines[i].strip()
    print(f"Line {i+1}: '{line}' Length: {len(line)}")
    if '\t' in line:
        print(f"TAB FOUND in line {i+1}")
    
    # Check pipe positions
    pipes = [pos for pos, char in enumerate(line) if char == '|']
    print(f"Pipes at: {pipes}")
