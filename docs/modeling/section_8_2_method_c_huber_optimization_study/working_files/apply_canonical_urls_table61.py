import urllib.request
import re
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = {
    "Realme GT3": "https://www.gsmarena.com/realme_gt3-12102.php",
    "Redmi Note 12 Explorer": "https://www.gsmarena.com/xiaomi_redmi_note_12_discovery-11954.php",
    "iQOO 11 Pro": "https://www.gsmarena.com/vivo_iqoo_11_pro-11993.php",
    "Motorola Edge 50 Pro": "https://www.gsmarena.com/motorola_edge_50_pro-12907.php",
    "Xiaomi 13 Pro": "https://www.gsmarena.com/xiaomi_13_pro-11949.php",
    "Xiaomi 12T Pro": "https://www.gsmarena.com/xiaomi_12t_pro-11887.php",
    "Poco F4 GT": "https://www.gsmarena.com/xiaomi_poco_f4_gt-11489.php",
    "Vivo X100 Pro": "https://www.gsmarena.com/vivo_x100_pro-12642.php",
    "OnePlus 12": "https://www.gsmarena.com/oneplus_12-12725.php",
    "OnePlus 11": "https://www.gsmarena.com/oneplus_11-11893.php",
    "OnePlus 12R": "https://www.gsmarena.com/oneplus_12r-12727.php",
    "Asus ROG Phone 7": "https://www.gsmarena.com/asus_rog_phone_7-12217.php",
    "Xiaomi 14": "https://www.gsmarena.com/xiaomi_14-12626.php",
    "Honor Magic 6 Pro": "https://www.gsmarena.com/honor_magic6_pro-12783.php",
    "Motorola Edge 40": "https://www.gsmarena.com/motorola_edge_40-12204.php",
    "Xiaomi 13": "https://www.gsmarena.com/xiaomi_13-11985.php",
    "Honor Magic 5 Pro": "https://www.gsmarena.com/honor_magic5_pro-12147.php",
    "Samsung Galaxy S24 Ultra": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
    "Samsung Galaxy S23 Ultra": "https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php",
    "Samsung Galaxy S22 Ultra": "https://www.gsmarena.com/samsung_galaxy_s22_ultra_5g-11241.php",
    "Nothing Phone (2)": "https://www.gsmarena.com/nothing_phone_(2)-12331.php",
    "Google Pixel 9 Pro XL": "https://www.gsmarena.com/google_pixel_9_pro_xl-13265.php",
    "Google Pixel 8 Pro": "https://www.gsmarena.com/google_pixel_8_pro-12546.php",
    "Samsung Galaxy S24": "https://www.gsmarena.com/samsung_galaxy_s24-12773.php",
    "Samsung Galaxy S23": "https://www.gsmarena.com/samsung_galaxy_s23-12082.php",
    "Samsung Galaxy A55": "https://www.gsmarena.com/samsung_galaxy_a55-12824.php",
    "Samsung Galaxy A54": "https://www.gsmarena.com/samsung_galaxy_a54-12070.php",
    "Samsung Galaxy A34": "https://www.gsmarena.com/samsung_galaxy_a34-12074.php",
    "Google Pixel 7 Pro": "https://www.gsmarena.com/google_pixel_7_pro-11908.php",
    "Samsung Galaxy S10": "https://www.gsmarena.com/samsung_galaxy_s10-9536.php",
    "Samsung Galaxy S9": "https://www.gsmarena.com/samsung_galaxy_s9-8966.php",
    "Samsung Galaxy S8": "https://www.gsmarena.com/samsung_galaxy_s8-8161.php",
    "Nokia 2.4": "https://www.gsmarena.com/nokia_2_4-10426.php",
    "Samsung Galaxy A03 Core": "https://www.gsmarena.com/samsung_galaxy_a03_core-11226.php",
    "Apple iPhone 16 Pro Max": "https://www.gsmarena.com/apple_iphone_16_pro_max-13315.php",
    "Apple iPhone 14 Pro Max": "https://www.gsmarena.com/apple_iphone_14_pro_max-11773.php",
    "Apple iPhone 15 Pro Max": "https://www.gsmarena.com/apple_iphone_15_pro_max-12548.php",
    "Apple iPhone 13 Pro Max": "https://www.gsmarena.com/apple_iphone_13_pro_max-11089.php",
    "Apple iPhone 11 Pro Max": "https://www.gsmarena.com/apple_iphone_11_pro_max-9846.php",
    "LG G7 ThinQ": "https://www.gsmarena.com/lg_g7_thinq-9115.php",
    "Apple iPhone XS Max": "https://www.gsmarena.com/apple_iphone_xs_max-9319.php",
    "Apple iPhone X": "https://www.gsmarena.com/apple_iphone_x-8858.php",
    "Apple iPhone 8": "https://www.gsmarena.com/apple_iphone_8-8573.php",
    "Apple iPhone 7 Plus": "https://www.gsmarena.com/apple_iphone_7_plus-8065.php"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Verifying 44 URLs...")
passed = 0

for name, url in urls.items():
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            html = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
            title = title_m.group(1) if title_m else ""
            if status == 200 and "Page not found" not in html:
                print(f"[VERIFIED 200] {name:<25} -> {title[:50]}")
                passed += 1
            else:
                print(f"[FAIL {status}]     {name:<25} -> {title[:50]}")
    except Exception as e:
        print(f"[ERR]          {name:<25} -> {e}")
    time.sleep(2.0)

print(f"\nFinal Result: {passed} / 44 Verified!")
