import re

FILES = [
    r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\scoring_rules.md",
    r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\proposed_data_structure.md",
    r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\data_structure_guidelines.md"
]

REPLACEMENTS = {
    "Section 2.4": "Section 2.3",
    "Section 3.11": "Section 6.4",
    "Section 4.18": "Section 4.18", # Same
    "Section 3.1 Method C": "Section 6.1 Method C",
    "Section 3.2 Method C": "Section 6.2 Method C",
    "Section 5.1": "Section 8.1",
    "Section 3.1.0": "Section 6.1.0",
    "Section 3.0 CPU Core Architecture Reference": "Section 6.1.0 CPU Core Architecture Reference",
    "Section 3.0": "Section 6.1.0",
    "Section 3.1 ": "Section 6.1 ",
    "Section 3.2 ": "Section 6.2 ",
    "Section 3.3 ": "Section 6.3 ",
    "Section 3.3.0": "Section 6.3.0",
    "Section 3.4": "Section 6.10",
    "Section 6.2 (AI Feature Suite)": "Section 5.3 (AI Feature Suite)",
    "Section 3.5": "Section 6.5",
    "Section 3.6": "Section 6.6",
    "Section 7.1": "Section 7.1", # Same
    "Section 7.3": "Section 7.3", # Same
    "Section 6.3": "Section 5.2",
    "Subsection 4.5 ": "Subsection 4.6 ",
    "Subsection 4.4 ": "Subsection 4.4 ", # Same
    "Section 4.3 ": "Section 4.3 ", # Same
    "Section 4.16 ": "Section 4.16 ", # Same
    "Section 4.17 ": "Section 4.17 ", # Same
}

for file_path in FILES:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    # Order keys by length descending so "Section 3.11" matches before "Section 3.1"
    sorted_keys = sorted(REPLACEMENTS.keys(), key=len, reverse=True)
    
    for old_k in sorted_keys:
        new_k = REPLACEMENTS[old_k]
        if old_k != new_k:
            content = content.replace(old_k, new_k)
            
    # Also explicitly fix scoring_constants.md references since they use a specific format
    content = content.replace("scoring_constants.md) Section 2", "scoring_constants.md) Section 2")
    content = content.replace("scoring_constants.md) Section 6", "scoring_constants.md) Section 5")
    content = content.replace("scoring_constants.md) Section 3", "scoring_constants.md) Section 6")
    content = content.replace("scoring_constants.md) Section 5.1", "scoring_constants.md) Section 8.1")
    content = content.replace("scoring_constants.md) Section 5", "scoring_constants.md) Section 8")
    content = content.replace("scoring_constants.md) Section 9", "scoring_constants.md) Section 9")
            
    if content != orig:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated references in {file_path}")
        
print("Reference refactoring complete.")
