import re

with open('scoring_rules.md', 'r', encoding='utf-8') as f:
    text = f.read()

subsections = re.findall(r'### 🔹 (\d+\.\d+) (.*?)\n(.*?)(?=\n### 🔹 |\Z)', text, re.DOTALL)

print(f"Total Subsections: {len(subsections)}")

categories = {
    'single_value': [],    # Subsections that just parse 1 value -> 1 score
    'multi_subscore': [],  # Subsections with A, B, C sub-items that need aggregation
    'table_lookup': []     # Subsections relying on a table matching a categorical string
}

for num, title, content in subsections:
    # Identify if it contains sub-components like "1.1.A" or "4.13" with nested headers
    sub_components = re.findall(rf'#### {num}\.[A-Z] (.*?)\n', content)
    
    # Or if it describes multiple discrete scores in a table
    table_scores = re.search(r'\|\s*Score\s*\|', content)
    
    if len(sub_components) > 1:
        categories['multi_subscore'].append((num, title, len(sub_components)))
    elif table_scores:
        categories['table_lookup'].append((num, title))
    else:
        categories['single_value'].append((num, title))

print(f"\nMulti-Subscore Subsections ({len(categories['multi_subscore'])}):")
for item in categories['multi_subscore']:
    print(f"  {item[0]} {item[1]} ({item[2]} sub-components)")

print(f"\nTable Lookup Subsections ({len(categories['table_lookup'])}):")
for item in categories['table_lookup'][:5]:
    print(f"  {item[0]} {item[1]}")
print("  ...")

print(f"\nSingle Value Formula Subsections ({len(categories['single_value'])}):")
for item in categories['single_value'][:5]:
    print(f"  {item[0]} {item[1]}")
print("  ...")
