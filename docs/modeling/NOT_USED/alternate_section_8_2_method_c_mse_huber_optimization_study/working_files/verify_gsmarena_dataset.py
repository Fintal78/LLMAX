import urllib.request
import urllib.parse
import json
import re
import time

# List of all 44 benchmark devices with current dataset parameters
DEVICES_TO_VERIFY = [
    # Tier 1
    {"name": "Realme GT3", "wh": 17.71, "p_peak": 240.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 9.6},
    {"name": "Redmi Note 12 Explorer", "wh": 16.56, "p_peak": 210.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 9.0},
    {"name": "iQOO 11 Pro", "wh": 18.10, "p_peak": 200.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 12.0},
    {"name": "Motorola Edge 50 Pro", "wh": 17.33, "p_peak": 125.0, "arch": "single", "proto": "charge_pump", "t_claimed": 18.0},
    {"name": "Xiaomi 13 Pro", "wh": 18.56, "p_peak": 120.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 19.0},
    {"name": "Xiaomi 12T Pro", "wh": 19.25, "p_peak": 120.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 19.0},
    {"name": "Poco F4 GT", "wh": 18.10, "p_peak": 120.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 17.0},
    {"name": "Vivo X100 Pro", "wh": 20.79, "p_peak": 100.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 31.0},
    {"name": "OnePlus 12", "wh": 20.79, "p_peak": 100.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 26.0},
    {"name": "OnePlus 11", "wh": 19.25, "p_peak": 100.0, "arch": "dual", "proto": "charge_pump", "t_claimed": 25.0},

    # Tier 2
    {"name": "Xiaomi 14", "wh": 17.71, "p_peak": 90.0, "arch": "single", "proto": "charge_pump", "t_claimed": 35.0},
    {"name": "Honor Magic 6 Pro", "wh": 21.56, "p_peak": 80.0, "arch": "single", "proto": "pps", "t_claimed": 36.0},
    {"name": "OnePlus 12R", "wh": 21.17, "p_peak": 80.0, "arch": "single", "proto": "charge_pump", "t_claimed": 32.0},
    {"name": "Motorola Edge 40", "wh": 17.33, "p_peak": 68.0, "arch": "single", "proto": "pps", "t_claimed": 44.0},
    {"name": "Xiaomi 13", "wh": 17.33, "p_peak": 67.0, "arch": "single", "proto": "pps", "t_claimed": 42.0},
    {"name": "Honor Magic 5 Pro", "wh": 19.64, "p_peak": 66.0, "arch": "single", "proto": "pps", "t_claimed": 48.0},
    {"name": "Asus ROG Phone 7", "wh": 23.10, "p_peak": 65.0, "arch": "single", "proto": "pps", "t_claimed": 42.0},

    # Tier 3
    {"name": "Samsung Galaxy S24 Ultra", "wh": 19.25, "p_peak": 45.0, "arch": "single", "proto": "pps", "t_claimed": 59.0},
    {"name": "Samsung Galaxy S23 Ultra", "wh": 19.25, "p_peak": 45.0, "arch": "single", "proto": "pps", "t_claimed": 59.0},
    {"name": "Samsung Galaxy S22 Ultra", "wh": 19.25, "p_peak": 45.0, "arch": "single", "proto": "pps", "t_claimed": 59.0},
    {"name": "Nothing Phone (2)", "wh": 18.10, "p_peak": 45.0, "arch": "single", "proto": "pps", "t_claimed": 55.0},
    {"name": "Google Pixel 9 Pro XL", "wh": 19.25, "p_peak": 37.0, "arch": "single", "proto": "pps", "t_claimed": 79.0},
    {"name": "Google Pixel 8 Pro", "wh": 19.25, "p_peak": 30.0, "arch": "single", "proto": "pps", "t_claimed": 81.0},
    {"name": "Apple iPhone 16 Pro Max", "wh": 18.04, "p_peak": 30.0, "arch": "single", "proto": "apple_legacy", "t_claimed": 107.0},
    {"name": "Apple iPhone 14 Pro Max", "wh": 16.64, "p_peak": 29.0, "arch": "single", "proto": "apple_legacy", "t_claimed": 112.0},
    {"name": "Apple iPhone 15 Pro Max", "wh": 17.10, "p_peak": 27.0, "arch": "single", "proto": "apple_legacy", "t_claimed": 109.0},
    {"name": "Apple iPhone 13 Pro Max", "wh": 16.75, "p_peak": 27.0, "arch": "single", "proto": "apple_legacy", "t_claimed": 106.0},
    {"name": "Samsung Galaxy S24", "wh": 15.40, "p_peak": 25.0, "arch": "single", "proto": "pps", "t_claimed": 75.0},
    {"name": "Samsung Galaxy S23", "wh": 15.02, "p_peak": 25.0, "arch": "single", "proto": "pps", "t_claimed": 72.0},
    {"name": "Samsung Galaxy A55", "wh": 19.25, "p_peak": 25.0, "arch": "single", "proto": "pps", "t_claimed": 85.0},
    {"name": "Samsung Galaxy A54", "wh": 19.25, "p_peak": 25.0, "arch": "single", "proto": "pps", "t_claimed": 82.0},
    {"name": "Samsung Galaxy A34", "wh": 19.25, "p_peak": 25.0, "arch": "single", "proto": "pps", "t_claimed": 84.0},
    {"name": "Google Pixel 7 Pro", "wh": 19.25, "p_peak": 23.0, "arch": "single", "proto": "pps", "t_claimed": 109.0},

    # Tier 4
    {"name": "Apple iPhone 11 Pro Max", "wh": 15.04, "p_peak": 18.0, "arch": "single", "proto": "apple_legacy", "t_claimed": 120.0},
    {"name": "LG G7 ThinQ", "wh": 11.55, "p_peak": 18.0, "arch": "single", "proto": "fixed_pd", "t_claimed": 108.0},
    {"name": "Apple iPhone XS Max", "wh": 12.08, "p_peak": 15.0, "arch": "single", "proto": "apple_legacy", "t_claimed": 131.0},
    {"name": "Apple iPhone X", "wh": 10.43, "p_peak": 15.0, "arch": "single", "proto": "apple_legacy", "t_claimed": 125.0},
    {"name": "Samsung Galaxy S10", "wh": 13.09, "p_peak": 15.0, "arch": "single", "proto": "fixed_pd", "t_claimed": 108.0},
    {"name": "Samsung Galaxy S9", "wh": 11.55, "p_peak": 15.0, "arch": "single", "proto": "fixed_pd", "t_claimed": 107.0},
    {"name": "Samsung Galaxy S8", "wh": 11.55, "p_peak": 15.0, "arch": "single", "proto": "fixed_pd", "t_claimed": 100.0},

    # Tier 5
    {"name": "Apple iPhone 8", "wh": 7.01, "p_peak": 5.0, "arch": "single", "proto": "legacy_5v", "t_claimed": 148.0},
    {"name": "Apple iPhone 7 Plus", "wh": 11.17, "p_peak": 5.0, "arch": "single", "proto": "legacy_5v", "t_claimed": 241.0},
    {"name": "Nokia 2.4", "wh": 17.33, "p_peak": 5.0, "arch": "single", "proto": "legacy_5v", "t_claimed": 215.0},
    {"name": "Samsung Galaxy A03 Core", "wh": 19.25, "p_peak": 7.7, "arch": "single", "proto": "legacy_5v", "t_claimed": 205.0},
]

print(f"Total devices to verify: {len(DEVICES_TO_VERIFY)}")
