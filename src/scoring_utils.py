
import os
import re

def load_constants(docs_dir=None):
    """
    Parses scoring_constants.md and returns a dictionary of constants.
    
    Expected format in markdown:
    * `Constant_Name` = Value ...
    
    Example:
    * `Weight_g_Min` = 140 (Score 10), `Weight_g_Max` = 250 (Score 0)
    """
    if docs_dir is None:
        # Assume standard structure: src/../docs
        script_dir = os.path.dirname(os.path.abspath(__file__))
        docs_dir = os.path.join(script_dir, '..', 'docs')
    
    file_path = os.path.join(docs_dir, 'scoring_constants.md')
    file_path = os.path.normpath(file_path)
    
    constants = {}
    
    if not os.path.exists(file_path):
        print(f"[scoring_utils] Warning: Constants file not found at {file_path}")
        return constants
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Regex to find `Name` = Value pairs
                # Captures: `Name` = 123 or `Name` = 123.45
                matches = re.findall(r'`([A-Za-z0-9_]+)`\s*=\s*([0-9\.]+)', line)
                
                for name, value_str in matches:
                    try:
                        if '.' in value_str:
                            value = float(value_str)
                        else:
                            value = int(value_str)
                        constants[name] = value
                    except ValueError:
                        continue
                        
        print(f"[scoring_utils] Loaded {len(constants)} constants from {os.path.basename(file_path)}")
        return constants
        
    except Exception as e:
        print(f"[scoring_utils] Error reading constants: {e}")
        return constants

if __name__ == "__main__":
    # Test execution
    consts = load_constants()
    print("Sample constants:")
    count = 0
    for k, v in consts.items():
        print(f"  {k}: {v}")
        count += 1
        if count >= 5: break
