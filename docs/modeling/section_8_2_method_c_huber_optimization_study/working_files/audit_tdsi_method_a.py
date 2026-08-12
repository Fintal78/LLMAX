import json
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

db_path = r'c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\data\phones_db.json'
with open(db_path, 'r', encoding='utf-8') as f:
    db = json.load(f)

phones = db.get('phones', [])

print(f"Total phones in database: {len(phones)}")

for i, p in enumerate(phones):
    brand = p.get('brand', '')
    model = p.get('model_name', '')
    full_name = f"{brand} {model}".strip()
    
    p_str = json.dumps(p)
    has_3dmark = '3dmark' in p_str.lower() or 'wild life' in p_str.lower() or 'wle' in p_str.lower()
    has_method_a = 'method_a' in p_str.lower()
    has_tdsi = 'tdsi' in p_str.lower() or 'stability' in p_str.lower()
    
    # Check battery scores
    battery = p.get('battery_scores', {})
    benchmarks = battery.get('benchmarks', {})
    
    print(f"{i+1:2d}. Phone: {full_name:40s} | 3DMark: {has_3dmark} | Method A: {has_method_a} | Benchmarks: {list(benchmarks.keys())}")
