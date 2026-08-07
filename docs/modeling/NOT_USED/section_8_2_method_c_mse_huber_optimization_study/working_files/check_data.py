"""
Validate the BENCHMARK_DEVICES dataset against scoring_rules.md baseline predictions.

The scoring_rules.md table provides verified baseline T_C predictions using:
  eta_base=0.45, s_low=0.32, C_threshold=1.5, k=0.12, p=0.30,
  T_handshake=0.5, F_charge_pump=1.10, F_pps=1.05, F_fixed_pd=0.95,
  F_legacy_5v=0.85, F_apple=0.88, F_arch=1.25

For each device, we compare our baseline T_C with the scoring_rules.md T_C.
If they match closely, the device data (Wh, power, arch, protocol) is correct.
"""
import math

# The scoring_rules.md table data (44 devices):
# (name, power_W, T_A_mins, T_C_baseline_mins, Score_A, Score_C_baseline)
SCORING_RULES_TABLE = [
    ("Realme GT3",               240.0,   9.6,   9.5, 10.00, 10.00),
    ("Redmi Note 12 Explorer",   210.0,   9.0,  10.0, 10.00,  9.82),
    ("iQOO 11 Pro",              200.0,  12.0,  11.3,  9.12,  9.44),
    ("Motorola Edge 50 Pro",     125.0,  18.0,  20.7,  7.89,  7.58),
    ("Xiaomi 13 Pro",            120.0,  19.0,  18.4,  7.73,  7.94),
    ("Xiaomi 12T Pro",           120.0,  19.0,  19.0,  7.73,  7.84),
    ("Poco F4 GT",               120.0,  17.0,  18.0,  8.07,  8.02),
    ("Vivo X100 Pro",            100.0,  31.0,  24.1,  6.24,  7.11),
    ("OnePlus 12",               100.0,  26.0,  24.1,  6.77,  7.11),
    ("OnePlus 11",               100.0,  25.0,  22.5,  6.89,  7.33),
    ("Xiaomi 14",                 90.0,  35.0,  28.6,  5.87,  6.58),
    ("Honor Magic 6 Pro",         80.0,  36.0,  39.9,  5.78,  5.55),
    ("OnePlus 12R",               80.0,  32.0,  37.5,  6.14,  5.75),
    ("Motorola Edge 40",          68.0,  44.0,  37.1,  5.17,  5.78),
    ("Xiaomi 13",                 67.0,  42.0,  38.4,  5.31,  5.67),
    ("Honor Magic 5 Pro",         66.0,  48.0,  43.7,  4.91,  5.27),
    ("Asus ROG Phone 7",          65.0,  42.0,  51.5,  5.31,  4.77),
    ("Samsung Galaxy S24 Ultra",  45.0,  59.0,  61.0,  4.28,  4.24),
    ("Samsung Galaxy S23 Ultra",  45.0,  59.0,  61.0,  4.28,  4.24),
    ("Samsung Galaxy S22 Ultra",  45.0,  59.0,  61.0,  4.28,  4.24),
    ("Nothing Phone (2)",         45.0,  55.0,  57.7,  4.49,  4.42),
    ("Google Pixel 9 Pro XL",     37.0,  79.0,  73.5,  3.39,  3.67),
    ("Google Pixel 8 Pro",        30.0,  81.0,  86.6,  3.32,  3.16),
    ("Apple iPhone 16 Pro Max",   30.0, 107.0,  97.9,  2.47,  2.78),
    ("Apple iPhone 14 Pro Max",   29.0, 112.0,  94.3,  2.33,  2.90),
    ("Apple iPhone 15 Pro Max",   27.0, 109.0, 101.5,  2.41,  2.67),
    ("Apple iPhone 13 Pro Max",   27.0, 106.0, 100.4,  2.50,  2.71),
    ("Samsung Galaxy S24",        25.0,  75.0,  83.7,  3.55,  3.27),
    ("Samsung Galaxy S23",        25.0,  72.0,  82.1,  3.67,  3.33),
    ("Samsung Galaxy A55",        25.0,  85.0,  86.0,  3.17,  3.18),
    ("Samsung Galaxy A54",        25.0,  82.0,  86.0,  3.28,  3.18),
    ("Samsung Galaxy A34",        25.0,  84.0,  86.0,  3.21,  3.18),
    ("Google Pixel 7 Pro",        23.0, 109.0,  87.8,  2.41,  3.12),
    ("Apple iPhone 11 Pro Max",   18.0, 120.0, 105.2,  2.12,  2.56),
    ("LG G7 ThinQ",              18.0, 108.0,  95.2,  2.44,  2.87),
    ("Apple iPhone XS Max",       15.0, 131.0, 103.9,  1.85,  2.60),
    ("Apple iPhone X",            15.0, 125.0, 101.4,  2.00,  2.67),
    ("Samsung Galaxy S10",        15.0, 108.0,  98.3,  2.44,  2.77),
    ("Samsung Galaxy S9",         15.0, 107.0,  95.0,  2.47,  2.87),
    ("Samsung Galaxy S8",         15.0, 100.0,  95.0,  2.68,  2.87),
    ("Apple iPhone 8",             5.0, 148.0, 141.5,  1.48,  1.64),
    ("Apple iPhone 7 Plus",        5.0, 241.0, 200.9,  0.00,  0.56),
    ("Nokia 2.4",                  5.0, 215.0, 292.5,  0.35,  0.00),
    ("Samsung Galaxy A03 Core",    7.7, 205.0, 220.5,  0.49,  0.27),
]

# My device specs (Wh, arch, protocol) for the 44 devices
# Format: (Wh, arch_type, protocol_type)
# Wh = capacity_mAh * 3.85 / 1000 (or 7.70 for dual-cell per-cell stated capacity)
DEVICE_SPECS = {
    "Realme GT3":               (17.71, 'dual',   'charge_pump'),  # 4600 mAh, dual-cell 2S
    "Redmi Note 12 Explorer":   (16.56, 'single', 'charge_pump'),  # 4300 mAh, single
    "iQOO 11 Pro":              (18.10, 'dual',   'charge_pump'),  # 4700 mAh, dual-cell 2S
    "Motorola Edge 50 Pro":     (17.33, 'single', 'charge_pump'),  # 4500 mAh, single (125W TurboPower)
    "Xiaomi 13 Pro":            (18.56, 'single', 'charge_pump'),  # 4820 mAh, single (120W HyperCharge)
    "Xiaomi 12T Pro":           (19.25, 'single', 'charge_pump'),  # 5000 mAh, single
    "Poco F4 GT":               (18.10, 'dual',   'charge_pump'),  # 4700 mAh, dual-cell 2S
    "Vivo X100 Pro":            (20.79, 'single', 'charge_pump'),  # 5400 mAh, single (100W FlashCharge)
    "OnePlus 12":               (20.79, 'single', 'charge_pump'),  # 5400 mAh, single (100W SUPERVOOC)
    "OnePlus 11":               (19.25, 'dual',   'charge_pump'),  # 5000 mAh, dual-cell 2S (100W SUPERVOOC)
    "Xiaomi 14":                (17.71, 'single', 'charge_pump'),  # 4610 mAh, single (90W HyperCharge)
    "Honor Magic 6 Pro":        (21.56, 'single', 'pps'),          # 5600 mAh, single (80W PPS)
    "OnePlus 12R":              (21.17, 'dual',   'charge_pump'),  # 5500 mAh, dual-cell 2S (80W SUPERVOOC)
    "Motorola Edge 40":         (17.33, 'single', 'pps'),          # 4500 mAh, single (68W PPS)
    "Xiaomi 13":                (17.33, 'single', 'pps'),          # 4500 mAh, single (67W)
    "Honor Magic 5 Pro":        (19.64, 'single', 'pps'),          # 5100 mAh, single (66W)
    "Asus ROG Phone 7":         (23.10, 'dual',   'pps'),          # 6000 mAh, dual-cell 2S (65W)
    "Samsung Galaxy S24 Ultra": (19.25, 'single', 'pps'),          # 5000 mAh, single (45W PPS)
    "Samsung Galaxy S23 Ultra": (19.25, 'single', 'pps'),          # 5000 mAh, single (45W PPS)
    "Samsung Galaxy S22 Ultra": (19.25, 'single', 'pps'),          # 5000 mAh, single (45W PPS)
    "Nothing Phone (2)":        (18.10, 'single', 'pps'),          # 4700 mAh, single (45W PPS)
    "Google Pixel 9 Pro XL":    (19.25, 'single', 'pps'),          # 5000 mAh (actual 5060), single (37W PPS)
    "Google Pixel 8 Pro":       (19.25, 'single', 'pps'),          # 5000 mAh (actual 5050), single (30W PPS)
    "Apple iPhone 16 Pro Max":  (18.59, 'single', 'apple_legacy'), # 4685 mAh (4.38V -> let me use 3.85V: 18.04? Actually 4685*3.97=18.60)
    "Apple iPhone 14 Pro Max":  (16.79, 'single', 'apple_legacy'), # 4323 mAh (4685 was 16 PM, this is 14 PM: 4323 mAh)
    "Apple iPhone 15 Pro Max":  (17.10, 'single', 'apple_legacy'), # 4441 mAh
    "Apple iPhone 13 Pro Max":  (16.75, 'single', 'apple_legacy'), # 4352 mAh
    "Samsung Galaxy S24":       (15.40, 'single', 'pps'),          # 4000 mAh, single (25W)
    "Samsung Galaxy S23":       (15.02, 'single', 'pps'),          # 3900 mAh, single (25W)
    "Samsung Galaxy A55":       (19.25, 'single', 'fixed_pd'),     # 5000 mAh, single (25W adaptive)
    "Samsung Galaxy A54":       (19.25, 'single', 'fixed_pd'),     # 5000 mAh, single (25W)
    "Samsung Galaxy A34":       (19.25, 'single', 'fixed_pd'),     # 5000 mAh, single (25W)
    "Google Pixel 7 Pro":       (19.25, 'single', 'pps'),          # 5000 mAh, single (23W)
    "Apple iPhone 11 Pro Max":  (15.04, 'single', 'apple_legacy'), # 3969 mAh
    "LG G7 ThinQ":             (11.55, 'single', 'fixed_pd'),     # 3000 mAh, fixed QC 3.0
    "Apple iPhone XS Max":      (12.08, 'single', 'apple_legacy'), # 3174 mAh
    "Apple iPhone X":           (10.43, 'single', 'apple_legacy'), # 2716 mAh
    "Samsung Galaxy S10":       (13.09, 'single', 'fixed_pd'),     # 3400 mAh, AFC 15W
    "Samsung Galaxy S9":        (11.55, 'single', 'fixed_pd'),     # 3000 mAh, AFC 15W
    "Samsung Galaxy S8":        (11.55, 'single', 'fixed_pd'),     # 3000 mAh, AFC 15W
    "Apple iPhone 8":           ( 6.96, 'single', 'apple_legacy'), # 1821 mAh
    "Apple iPhone 7 Plus":      (11.10, 'single', 'apple_legacy'), # 2900 mAh
    "Nokia 2.4":                (17.33, 'single', 'legacy_5v'),    # 4500 mAh, 5V/1A
    "Samsung Galaxy A03 Core":  (19.25, 'single', 'legacy_5v'),    # 5000 mAh, 7.7W
}

# Baseline parameters from scoring_rules.md
BASELINE = {
    'C_threshold': 1.50, 'k': 0.12, 'p': 0.30,
    'eta_base': 0.45, 's_low': 0.32, 'T_handshake': 0.50,
    'F_charge_pump': 1.10, 'F_pps': 1.05, 'F_fixed_pd': 0.95,
    'F_legacy_5v': 0.85, 'F_apple': 0.88, 'F_arch': 1.25,
}


def predict_baseline(wh, p_peak, arch, proto):
    E = wh
    C_rate = p_peak / max(0.01, E)
    
    F_a = BASELINE['F_arch'] if arch == 'dual' else 1.0
    F_p = BASELINE[f'F_{proto}'] if proto != 'apple_legacy' else BASELINE['F_apple']
    
    if C_rate > BASELINE['C_threshold']:
        F_Crate = 1.0 / (1.0 + BASELINE['k'] * math.pow(C_rate - BASELINE['C_threshold'], BASELINE['p']))
        eff = BASELINE['eta_base']
    else:
        F_Crate = 1.0
        eff = BASELINE['eta_base'] + BASELINE['s_low'] * (BASELINE['C_threshold'] - C_rate)
    
    eff = max(0.15, min(0.95, eff))
    P_eff = p_peak * eff * F_a * F_p * F_Crate
    P_eff = max(0.1, P_eff)
    T = (E / P_eff) * 60.0 + BASELINE['T_handshake']
    return T


print(f"{'Device':<30} {'P(W)':>5} {'Wh':>6} {'arch':<7} {'proto':<13} {'T_C_ref':>7} {'T_C_calc':>8} {'diff':>6} {'OK?':>4}")
print("-" * 105)

total_err = 0
max_err = 0
issues = []

for dev in SCORING_RULES_TABLE:
    name, power, T_A, T_C_ref, S_A, S_C = dev
    specs = DEVICE_SPECS.get(name)
    if not specs:
        print(f"  MISSING: {name}")
        continue
    
    wh, arch, proto = specs
    T_C_calc = predict_baseline(wh, power, arch, proto)
    diff = T_C_calc - T_C_ref
    ok = "OK" if abs(diff) < 1.0 else "FAIL"
    
    total_err += abs(diff)
    max_err = max(max_err, abs(diff))
    if abs(diff) >= 1.0:
        issues.append((name, diff))
    
    print(f"{name:<30} {power:>5.0f} {wh:>6.2f} {arch:<7} {proto:<13} {T_C_ref:>7.1f} {T_C_calc:>8.1f} {diff:>+6.1f} {ok:>4}")

print(f"\nMean |error|: {total_err/len(SCORING_RULES_TABLE):.2f} mins")
print(f"Max |error|: {max_err:.2f} mins")
print(f"\nFailed devices ({len(issues)}):")
for name, diff in issues:
    print(f"  {name}: {diff:+.1f} mins off")
