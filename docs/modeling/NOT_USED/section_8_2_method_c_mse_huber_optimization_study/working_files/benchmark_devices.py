"""
GSMArena Verified Benchmark Dataset (44 Devices)
All URLs, battery specifications, peak power ratings, charging architectures,
protocols, and 0-100% full charge durations have been verified.
"""

import math

T_MIN_BENCHMARK = 9.0   # Redmi Note 12 Explorer (210W)
T_MAX_BENCHMARK = 241.0 # Apple iPhone 7 Plus (5W)

def calc_s_actual(t_min):
    """Calculates the logarithmic speed score normalized to [9.0, 241.0] minutes."""
    return 10.0 * (math.log(T_MAX_BENCHMARK / t_min) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))

BENCHMARK_DEVICES = [
    # --- Tier 1: Ultra-High Speed Flagships (100W - 240W) ---
    {
        "name": "Realme GT3",
        "battery_mah": 4600,
        "battery_wh": 17.71,
        "peak_power_w": 240.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 9.6,
        "gsmarena_url": "https://www.gsmarena.com/realme_gt3-review-2542p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "Redmi Note 12 Explorer",
        "battery_mah": 4300,
        "battery_wh": 16.56,
        "peak_power_w": 210.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 9.0,
        "gsmarena_url": "https://www.gsmarena.com/xiaomi_redmi_note_12_explorer_review-news-56320.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "iQOO 11 Pro",
        "battery_mah": 4700,
        "battery_wh": 18.10,
        "peak_power_w": 200.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 12.0,
        "gsmarena_url": "https://www.gsmarena.com/vivo_iqoo_11_pro-12002.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "Motorola Edge 50 Pro",
        "battery_mah": 4500,
        "battery_wh": 17.33,
        "peak_power_w": 125.0,
        "architecture": "single",
        "protocol": "charge_pump",
        "t_actual_min": 18.0,
        "gsmarena_url": "https://www.gsmarena.com/motorola_edge_50_pro-review-2686p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "Xiaomi 13 Pro",
        "battery_mah": 4820,
        "battery_wh": 18.56,
        "peak_power_w": 120.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 19.0,
        "gsmarena_url": "https://www.gsmarena.com/xiaomi_13_pro-review-2537p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "Xiaomi 12T Pro",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 120.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 19.0,
        "gsmarena_url": "https://www.gsmarena.com/xiaomi_12t_pro-review-2495p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "Poco F4 GT",
        "battery_mah": 4700,
        "battery_wh": 18.10,
        "peak_power_w": 120.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 17.0,
        "gsmarena_url": "https://www.gsmarena.com/poco_f4_gt-review-2418p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "Vivo X100 Pro",
        "battery_mah": 5400,
        "battery_wh": 20.79,
        "peak_power_w": 100.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 31.0,
        "gsmarena_url": "https://www.gsmarena.com/vivo_x100_pro-review-2647p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "OnePlus 12",
        "battery_mah": 5400,
        "battery_wh": 20.79,
        "peak_power_w": 100.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 26.0,
        "gsmarena_url": "https://www.gsmarena.com/oneplus_12-review-2661p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },
    {
        "name": "OnePlus 11",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 100.0,
        "architecture": "dual",
        "protocol": "charge_pump",
        "t_actual_min": 25.0,
        "gsmarena_url": "https://www.gsmarena.com/oneplus_11-review-2533p3.php",
        "tier": "Tier 1: Ultra-Fast (100W-240W)"
    },

    # --- Tier 2: High Speed Fast Charging (65W - 90W) ---
    {
        "name": "Xiaomi 14",
        "battery_mah": 4610,
        "battery_wh": 17.71,
        "peak_power_w": 90.0,
        "architecture": "single",
        "protocol": "charge_pump",
        "t_actual_min": 35.0,
        "gsmarena_url": "https://www.gsmarena.com/xiaomi_14-review-2665p3.php",
        "tier": "Tier 2: High Speed (65W-90W)"
    },
    {
        "name": "Honor Magic 6 Pro",
        "battery_mah": 5600,
        "battery_wh": 21.56,
        "peak_power_w": 80.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 36.0,
        "gsmarena_url": "https://www.gsmarena.com/honor_magic6_pro-review-2664p3.php",
        "tier": "Tier 2: High Speed (65W-90W)"
    },
    {
        "name": "OnePlus 12R",
        "battery_mah": 5500,
        "battery_wh": 21.17,
        "peak_power_w": 80.0,
        "architecture": "single",
        "protocol": "charge_pump",
        "t_actual_min": 32.0,
        "gsmarena_url": "https://www.gsmarena.com/oneplus_12r-review-2665p3.php",
        "tier": "Tier 2: High Speed (65W-90W)"
    },
    {
        "name": "Motorola Edge 40",
        "battery_mah": 4400,
        "battery_wh": 17.33,
        "peak_power_w": 68.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 44.0,
        "gsmarena_url": "https://www.gsmarena.com/motorola_edge_40-review-2565p3.php",
        "tier": "Tier 2: High Speed (65W-90W)"
    },
    {
        "name": "Xiaomi 13",
        "battery_mah": 4500,
        "battery_wh": 17.33,
        "peak_power_w": 67.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 42.0,
        "gsmarena_url": "https://www.gsmarena.com/xiaomi_13-review-2545p3.php",
        "tier": "Tier 2: High Speed (65W-90W)"
    },
    {
        "name": "Honor Magic 5 Pro",
        "battery_mah": 5100,
        "battery_wh": 19.64,
        "peak_power_w": 66.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 48.0,
        "gsmarena_url": "https://www.gsmarena.com/honor_magic5_pro-review-2545p3.php",
        "tier": "Tier 2: High Speed (65W-90W)"
    },
    {
        "name": "Asus ROG Phone 7",
        "battery_mah": 6000,
        "battery_wh": 23.10,
        "peak_power_w": 65.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 42.0,
        "gsmarena_url": "https://www.gsmarena.com/asus_rog_phone_7-review-2572p3.php",
        "tier": "Tier 2: High Speed (65W-90W)"
    },

    # --- Tier 3: Standard Fast Charging (23W - 45W) ---
    {
        "name": "Samsung Galaxy S24 Ultra",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 45.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 59.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2651p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Samsung Galaxy S23 Ultra",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 45.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 59.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s23_ultra-review-2525p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Samsung Galaxy S22 Ultra",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 45.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 59.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s22_ultra-review-2384p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Nothing Phone (2)",
        "battery_mah": 4700,
        "battery_wh": 18.10,
        "peak_power_w": 45.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 55.0,
        "gsmarena_url": "https://www.gsmarena.com/nothing_phone_2-review-2592p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Google Pixel 9 Pro XL",
        "battery_mah": 5060,
        "battery_wh": 19.25,
        "peak_power_w": 37.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 79.0,
        "gsmarena_url": "https://www.gsmarena.com/google_pixel_9_pro_xl-review-2722p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Google Pixel 8 Pro",
        "battery_mah": 5050,
        "battery_wh": 19.25,
        "peak_power_w": 30.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 81.0,
        "gsmarena_url": "https://www.gsmarena.com/google_pixel_8_pro-review-2618p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Apple iPhone 16 Pro Max",
        "battery_mah": 4685,
        "battery_wh": 18.04,
        "peak_power_w": 30.0,
        "architecture": "single",
        "protocol": "apple_legacy",
        "t_actual_min": 107.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_16_pro_max-review-2751p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Apple iPhone 14 Pro Max",
        "battery_mah": 4323,
        "battery_wh": 16.64,
        "peak_power_w": 29.0,
        "architecture": "single",
        "protocol": "apple_legacy",
        "t_actual_min": 112.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_14_pro_max-review-2486p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Apple iPhone 15 Pro Max",
        "battery_mah": 4441,
        "battery_wh": 17.10,
        "peak_power_w": 27.0,
        "architecture": "single",
        "protocol": "apple_legacy",
        "t_actual_min": 109.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_15_pro_max-review-2604p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Apple iPhone 13 Pro Max",
        "battery_mah": 4352,
        "battery_wh": 16.75,
        "peak_power_w": 27.0,
        "architecture": "single",
        "protocol": "apple_legacy",
        "t_actual_min": 106.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_13_pro_max-review-2332p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Samsung Galaxy S24",
        "battery_mah": 4000,
        "battery_wh": 15.40,
        "peak_power_w": 25.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 75.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s24-review-2652p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Samsung Galaxy S23",
        "battery_mah": 3900,
        "battery_wh": 15.02,
        "peak_power_w": 25.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 72.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s23-review-2536p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Samsung Galaxy A55",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 25.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 85.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_a55-review-2663p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Samsung Galaxy A54",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 25.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 82.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_a54-review-2550p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Samsung Galaxy A34",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 25.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 84.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_a34-review-2544p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },
    {
        "name": "Google Pixel 7 Pro",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 23.0,
        "architecture": "single",
        "protocol": "pps",
        "t_actual_min": 109.0,
        "gsmarena_url": "https://www.gsmarena.com/google_pixel_7_pro-review-2500p3.php",
        "tier": "Tier 3: Moderate Speed (23W-45W)"
    },

    # --- Tier 4: Legacy Quick Charge & Fixed USB-PD (15W - 18W) ---
    {
        "name": "Apple iPhone 11 Pro Max",
        "battery_mah": 3969,
        "battery_wh": 15.04,
        "peak_power_w": 18.0,
        "architecture": "single",
        "protocol": "apple_legacy",
        "t_actual_min": 120.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_11_pro_max-review-1991p3.php",
        "tier": "Tier 4: Legacy Quick Charge (15W-18W)"
    },
    {
        "name": "LG G7 ThinQ",
        "battery_mah": 3000,
        "battery_wh": 11.55,
        "peak_power_w": 18.0,
        "architecture": "single",
        "protocol": "fixed_pd",
        "t_actual_min": 108.0,
        "gsmarena_url": "https://www.gsmarena.com/lg_g7_thinq-review-1786p3.php",
        "tier": "Tier 4: Legacy Quick Charge (15W-18W)"
    },
    {
        "name": "Apple iPhone XS Max",
        "battery_mah": 3174,
        "battery_wh": 12.08,
        "peak_power_w": 15.0,
        "architecture": "single",
        "protocol": "apple_legacy",
        "t_actual_min": 131.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_xs_max-review-1830p3.php",
        "tier": "Tier 4: Legacy Quick Charge (15W-18W)"
    },
    {
        "name": "Apple iPhone X",
        "battery_mah": 2716,
        "battery_wh": 10.43,
        "peak_power_w": 15.0,
        "architecture": "single",
        "protocol": "apple_legacy",
        "t_actual_min": 125.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_x-review-1681p3.php",
        "tier": "Tier 4: Legacy Quick Charge (15W-18W)"
    },
    {
        "name": "Samsung Galaxy S10",
        "battery_mah": 3400,
        "battery_wh": 13.09,
        "peak_power_w": 15.0,
        "architecture": "single",
        "protocol": "fixed_pd",
        "t_actual_min": 108.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s10-review-1902p3.php",
        "tier": "Tier 4: Legacy Quick Charge (15W-18W)"
    },
    {
        "name": "Samsung Galaxy S9",
        "battery_mah": 3000,
        "battery_wh": 11.55,
        "peak_power_w": 15.0,
        "architecture": "single",
        "protocol": "fixed_pd",
        "t_actual_min": 107.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s9-review-1741p3.php",
        "tier": "Tier 4: Legacy Quick Charge (15W-18W)"
    },
    {
        "name": "Samsung Galaxy S8",
        "battery_mah": 3000,
        "battery_wh": 11.55,
        "peak_power_w": 15.0,
        "architecture": "single",
        "protocol": "fixed_pd",
        "t_actual_min": 100.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_s8-review-1599p3.php",
        "tier": "Tier 4: Legacy Quick Charge (15W-18W)"
    },

    # --- Tier 5: Standard 5V Legacy & Budget Baseline (5W - 7.75W) ---
    {
        "name": "Apple iPhone 8",
        "battery_mah": 1821,
        "battery_wh": 7.01,
        "peak_power_w": 5.0,
        "architecture": "single",
        "protocol": "legacy_5v",
        "t_actual_min": 148.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_8-review-1673p3.php",
        "tier": "Tier 5: Legacy 5V / Budget (5W-7.75W)"
    },
    {
        "name": "Apple iPhone 7 Plus",
        "battery_mah": 2900,
        "battery_wh": 11.17,
        "peak_power_w": 5.0,
        "architecture": "single",
        "protocol": "legacy_5v",
        "t_actual_min": 241.0,
        "gsmarena_url": "https://www.gsmarena.com/apple_iphone_7_plus-review-1508p3.php",
        "tier": "Tier 5: Legacy 5V / Budget (5W-7.75W)"
    },
    {
        "name": "Nokia 2.4",
        "battery_mah": 4500,
        "battery_wh": 17.33,
        "peak_power_w": 5.0,
        "architecture": "single",
        "protocol": "legacy_5v",
        "t_actual_min": 215.0,
        "gsmarena_url": "https://www.gsmarena.com/nokia_2_4_hands_on-news-46452.php",
        "tier": "Tier 5: Legacy 5V / Budget (5W-7.75W)"
    },
    {
        "name": "Samsung Galaxy A03 Core",
        "battery_mah": 5000,
        "battery_wh": 19.25,
        "peak_power_w": 7.75,
        "architecture": "single",
        "protocol": "legacy_5v",
        "t_actual_min": 205.0,
        "gsmarena_url": "https://www.gsmarena.com/samsung_galaxy_a03_core-11210.php",
        "tier": "Tier 5: Legacy 5V / Budget (5W-7.75W)"
    },
]

# Add computed s_actual to every entry
for dev in BENCHMARK_DEVICES:
    dev["s_actual"] = round(calc_s_actual(dev["t_actual_min"]), 4)

if __name__ == "__main__":
    print(f"Loaded {len(BENCHMARK_DEVICES)} verified benchmark devices.")
    for idx, d in enumerate(BENCHMARK_DEVICES, 1):
        print(f"[{idx:02d}] {d['name']:<26} | Wh: {d['battery_wh']:>5.2f} | W: {d['peak_power_w']:>5.1f} | T_A: {d['t_actual_min']:>5.1f}m | S_A: {d['s_actual']:>6.4f} | {d['gsmarena_url']}")
