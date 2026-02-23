import re

FILES = [
    r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_rules.md",
    r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\proposed_data_structure.md",
    r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\data_structure_guidelines.md"
]

REPLACEMENTS = {
    # Fix the chained replacements
    "Section 5.2 GPU": "Section 6.3 GPU",
    "Section 5.2 (GPU": "Section 6.3 (GPU",
    "Section 5.2.0": "Section 6.3.0",
    "Final Section 5.2 Score": "Final Section 6.3 Score",
    
    # Fix the stragglers missed due to punctuation or specific phrasing
    "high 3.11 score": "high 6.4 score",
    "**Section 3.3**.": "**Section 6.3**.",
    "Model (Section 3.10).": "Model (Section 6.4)."
}

for file_path in FILES:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    for old_k, new_k in REPLACEMENTS.items():
        content = content.replace(old_k, new_k)
            
    if content != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Hotfixed references in {file_path}")
        
print("Hotfix complete.")
