import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

VALID = {
    '1.1','1.2','1.3','1.4','1.5','1.6',
    '2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','2.10','2.11',
    '3.1','3.2','3.2.1','3.2.2','3.3','3.4','3.4.1','3.4.2','3.4.3',
    '4.1','4.2','4.3','4.4','4.5','4.6','4.7','4.8','4.9',
    '4.10','4.11','4.12','4.13','4.13.1','4.13.2','4.13.3',
    '4.14','4.15','4.16','4.17','4.18',
    '5.1','5.2','5.3',
    '6.1','6.1.0','6.2','6.3','6.3.0','6.4','6.4.0','6.5','6.6','6.7','6.8','6.9','6.10',
    '7.1','7.2','7.3','7.4','7.5','7.5.1','7.6','7.6.1','7.6.2','7.7','7.8','7.9',
    '8.1','8.2','8.3','8.4','8.5','8.6',
    '9.1','9.2','9.3',
    '10.1','10.2',
    '11.1','11.2','11.3',
}

with open('docs/scoring_rules.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Also capture inline refs like "(2.10)" or "Section 2.10" or "Sec 2.10", "subsection 2.10"
# Exclude obvious non-section patterns: version numbers v8.0, formula values, scores, dimensions
CONTEXT_REF = re.compile(
    r'(?:[Ss]ection|[Ss]ubsection|Sec)\s+(\d+\.\d+(?:\.\d+)?)'
    r'|(?<!\d)\((\d+\.\d+(?:\.\d+)?)\)(?!\d)'          # bare (X.Y)
    r'|\b(\d{1,2}\.\d{1,2})\s+(?:Score|Method|Table|Part|Performance|Scoring|Category|Capacity|Size|Ratio|Resolution|Speed|Rate|Benchmark|Weight|Scale)'
)

section_name_pattern = re.compile(
    r'\*\*([\w &/]+)\s+\((\d+\.\d+(?:\.\d+)?)\)\*\*'  # bold name (X.Y)
    r'|\*\*Section (\d+\.\d+(?:\.\d+)?)\s+\(.*?\)\*\*'
)

errors = []
for i, line in enumerate(lines, 1):
    for m in re.finditer(r'[Ss]ection\s+(\d+\.\d+(?:\.\d+)?)', line):
        num = m.group(1)
        if num not in VALID:
            errors.append((i, m.group(0), line.strip()[:110]))
    # Also check parenthetical "(X.Y)" which describes a section name like "(TDSI)"
    for m in re.finditer(r'\((\d+\.\d+(?:\.\d+)?)\)', line):
        num = m.group(1)
        if num not in VALID:
            # exclude if looks like a formula or score context
            context = line[max(0, m.start()-30):m.end()+30]
            if not re.search(r'[=\d\*\/\+\-]', line[max(0, m.start()-5):m.start()]):
                errors.append((i, f'({num})', line.strip()[:110]))

if errors:
    # Deduplicate
    seen = set()
    unique = []
    for e in errors:
        key = (e[0], e[1])
        if key not in seen:
            seen.add(key)
            unique.append(e)
    print(f'INVALID SECTION REFERENCES ({len(unique)} found):')
    for lineno, ref, ctx in unique:
        print(f'  L{lineno:4d}  {ref}  ==> {ctx}')
else:
    print('All section references are valid.')
