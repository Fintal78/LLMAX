import math

T_min_A = 9.0
T_max_A = 241.0

def calc_S(T):
    return 10.0 * (math.log(T_max_A / T) / math.log(T_max_A / T_min_A))

test_cases = [
    ("Redmi Note 12 Explorer", 9.0),
    ("Realme GT3", 9.6),
    ("Motorola Edge 50 Pro", 18.0),
    ("Samsung Galaxy S24 Ultra", 59.0),
    ("Apple iPhone 16 Pro Max", 107.0),
    ("Apple iPhone 7 Plus", 241.0),
    ("Nokia 2.4", 215.0),
]

print(f"{'Device':<30} | {'T_A':<6} | {'Calc S_A':<10}")
print("-" * 52)
for name, t in test_cases:
    s = calc_S(t)
    print(f"{name:<30} | {t:<6.1f} | {s:<10.4f}")
