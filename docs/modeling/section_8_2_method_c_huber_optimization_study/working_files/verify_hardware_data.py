import os

# Deep Hardware Audit of the 44 Devices
# Verifying single-cell vs dual-cell configurations from official teardowns / manufacturer spec sheets:

hardware_audits = [
    {"name": "Realme GT3", "P_peak": 240.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2300mAh series cells (2S)"},
    {"name": "Redmi Note 12 Explorer", "P_peak": 210.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2150mAh series cells (2S)"},
    {"name": "iQOO 11 Pro", "P_peak": 200.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2350mAh series cells (2S)"},
    {"name": "Motorola Edge 50 Pro", "P_peak": 125.0, "arch_current": "single", "arch_actual": "dual", "notes": "4500mAh 125W TurboPower uses dual-cell 2S structure"},
    {"name": "Xiaomi 13 Pro", "P_peak": 120.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2410mAh series cells (2S)"},
    {"name": "Xiaomi 12T Pro", "P_peak": 120.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2500mAh series cells (2S)"},
    {"name": "Poco F4 GT", "P_peak": 120.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2350mAh series cells (2S)"},
    {"name": "Vivo X100 Pro", "P_peak": 100.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2700mAh series cells (2S)"},
    {"name": "OnePlus 12", "P_peak": 100.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2700mAh series cells (2S)"},
    {"name": "OnePlus 11", "P_peak": 100.0, "arch_current": "dual", "arch_actual": "dual", "notes": "2x 2500mAh series cells (2S)"},
    {"name": "Xiaomi 14", "P_peak": 90.0, "arch_current": "single", "arch_actual": "single", "notes": "4610mAh single-cell high-energy density battery"},
    {"name": "Honor Magic 6 Pro", "P_peak": 80.0, "arch_current": "single", "arch_actual": "single", "notes": "5600mAh silicon-carbon single-cell battery"},
    {"name": "OnePlus 12R", "P_peak": 80.0, "arch_current": "single", "arch_actual": "dual", "notes": "5500mAh SuperVOOC uses dual-cell 2S design"},
    {"name": "Motorola Edge 40", "P_peak": 68.0, "arch_current": "single", "arch_actual": "single", "notes": "4400mAh single-cell battery"},
    {"name": "Xiaomi 13", "P_peak": 67.0, "arch_current": "single", "arch_actual": "single", "notes": "4500mAh single-cell battery"},
    {"name": "Honor Magic 5 Pro", "P_peak": 66.0, "arch_current": "single", "arch_actual": "single", "notes": "5100mAh single-cell battery"},
    {"name": "Asus ROG Phone 7", "P_peak": 65.0, "arch_current": "single", "arch_actual": "dual", "notes": "6000mAh split dual-cell (2x 3000mAh) battery"},
    {"name": "Samsung Galaxy S24 Ultra", "P_peak": 45.0, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"},
    {"name": "Samsung Galaxy S23 Ultra", "P_peak": 45.0, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"},
    {"name": "Samsung Galaxy S22 Ultra", "P_peak": 45.0, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"},
    {"name": "Nothing Phone (2)", "P_peak": 45.0, "arch_current": "single", "arch_actual": "single", "notes": "4700mAh single-cell battery"},
    {"name": "Google Pixel 9 Pro XL", "P_peak": 37.0, "arch_current": "single", "arch_actual": "single", "notes": "5060mAh single-cell battery"},
    {"name": "Google Pixel 8 Pro", "P_peak": 30.0, "arch_current": "single", "arch_actual": "single", "notes": "5050mAh single-cell battery"},
    {"name": "Apple iPhone 16 Pro Max", "P_peak": 30.0, "arch_current": "single", "arch_actual": "single", "notes": "4685mAh single-cell L-shaped battery"},
    {"name": "Apple iPhone 14 Pro Max", "P_peak": 29.0, "arch_current": "single", "arch_actual": "single", "notes": "4323mAh single-cell battery"},
    {"name": "Apple iPhone 15 Pro Max", "P_peak": 27.0, "arch_current": "single", "arch_actual": "single", "notes": "4422mAh single-cell battery"},
    {"name": "Apple iPhone 13 Pro Max", "P_peak": 27.0, "arch_current": "single", "arch_actual": "single", "notes": "4352mAh single-cell battery"},
    {"name": "Samsung Galaxy S24", "P_peak": 25.0, "arch_current": "single", "arch_actual": "single", "notes": "4000mAh single-cell battery"},
    {"name": "Samsung Galaxy S23", "P_peak": 25.0, "arch_current": "single", "arch_actual": "single", "notes": "3900mAh single-cell battery"},
    {"name": "Samsung Galaxy A55", "P_peak": 25.0, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"},
    {"name": "Samsung Galaxy A54", "P_peak": 25.0, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"},
    {"name": "Samsung Galaxy A34", "P_peak": 25.0, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"},
    {"name": "Google Pixel 7 Pro", "P_peak": 23.0, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"},
    {"name": "Apple iPhone 11 Pro Max", "P_peak": 18.0, "arch_current": "single", "arch_actual": "single", "notes": "3969mAh single-cell battery"},
    {"name": "LG G7 ThinQ", "P_peak": 18.0, "arch_current": "single", "arch_actual": "single", "notes": "3000mAh single-cell battery"},
    {"name": "Apple iPhone XS Max", "P_peak": 15.0, "arch_current": "single", "arch_actual": "single", "notes": "3174mAh single-cell L-shaped battery"},
    {"name": "Apple iPhone X", "P_peak": 15.0, "arch_current": "single", "arch_actual": "single", "notes": "2716mAh 2-cell L-pack (connected in parallel = 1S2P, acts electrically as single cell)"},
    {"name": "Samsung Galaxy S10", "P_peak": 15.0, "arch_current": "single", "arch_actual": "single", "notes": "3400mAh single-cell battery"},
    {"name": "Samsung Galaxy S9", "P_peak": 15.0, "arch_current": "single", "arch_actual": "single", "notes": "3000mAh single-cell battery"},
    {"name": "Samsung Galaxy S8", "P_peak": 15.0, "arch_current": "single", "arch_actual": "single", "notes": "3000mAh single-cell battery"},
    {"name": "Apple iPhone 8", "P_peak": 5.0, "arch_current": "single", "arch_actual": "single", "notes": "1821mAh single-cell battery"},
    {"name": "Apple iPhone 7 Plus", "P_peak": 5.0, "arch_current": "single", "arch_actual": "single", "notes": "2900mAh single-cell battery"},
    {"name": "Nokia 2.4", "P_peak": 5.0, "arch_current": "single", "arch_actual": "single", "notes": "4500mAh single-cell battery"},
    {"name": "Samsung Galaxy A03 Core", "P_peak": 7.8, "arch_current": "single", "arch_actual": "single", "notes": "5000mAh single-cell battery"}
]

mismatches = [item for item in hardware_audits if item['arch_current'] != item['arch_actual']]

print(f"Found {len(mismatches)} hardware architecture mismatches in current dataset:")
for m in mismatches:
    print(f"- {m['name']}: current={m['arch_current']} vs actual={m['arch_actual']} ({m['notes']})")
