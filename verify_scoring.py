import json
import re

def verify_scoring_fields(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract JSON block
    match = re.search(r'```json\s*(\{.*?\})\s*```', content, re.DOTALL)
    if not match:
        print("No JSON block found")
        return

    json_str = match.group(1)
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")
        return

    missing_scores = []
    
    # Iterate through top-level sections (e.g., "1_design_and_build_quality")
    for section_key, section_data in data.items():
        if not isinstance(section_data, dict):
            continue
            
        # Iterate through subsections (e.g., "1_1_materials")
        for sub_key, sub_data in section_data.items():
            # Check if likely a numbered subsection (X_Y_...)
            if re.match(r'^\d+_\d+_[a-z0-9_]+$', sub_key):
                scores_present = True
                if "predicted_score" not in sub_data:
                    missing_scores.append(f"{sub_key} (missing predicted_score)")
                    scores_present = False
                if "final_score" not in sub_data:
                    missing_scores.append(f"{sub_key} (missing final_score)")
                    scores_present = False
                
                if scores_present:
                    # Optional: Print present? No, just errors.
                    pass

    if missing_scores:
        print("MISSING SCORES FOUND:")
        for m in missing_scores:
            print(f"- {m}")
    else:
        print("SUCCESS: All subsections have scoring fields.")

if __name__ == "__main__":
    verify_scoring_fields(r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\proposed_data_structure.md")
