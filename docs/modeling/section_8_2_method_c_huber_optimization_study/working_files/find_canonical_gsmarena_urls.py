import urllib.request
import urllib.parse
import re
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

devices = [
    "Realme GT3",
    "Redmi Note 12 Explorer",
    "iQOO 11 Pro",
    "Motorola Edge 50 Pro",
    "Xiaomi 13 Pro",
    "Xiaomi 12T Pro",
    "Poco F4 GT",
    "Vivo X100 Pro",
    "OnePlus 12",
    "OnePlus 11",
    "OnePlus 12R",
    "Asus ROG Phone 7",
    "Xiaomi 14",
    "Honor Magic 6 Pro",
    "Motorola Edge 40",
    "Xiaomi 13",
    "Honor Magic 5 Pro",
    "Samsung Galaxy S24 Ultra",
    "Samsung Galaxy S23 Ultra",
    "Samsung Galaxy S22 Ultra",
    "Nothing Phone (2)",
    "Google Pixel 9 Pro XL",
    "Google Pixel 8 Pro",
    "Samsung Galaxy S24",
    "Samsung Galaxy S23",
    "Samsung Galaxy A55",
    "Samsung Galaxy A54",
    "Samsung Galaxy A34",
    "Google Pixel 7 Pro",
    "Samsung Galaxy S10",
    "Samsung Galaxy S9",
    "Samsung Galaxy S8",
    "Nokia 2.4",
    "Samsung Galaxy A03 Core",
    "Apple iPhone 16 Pro Max",
    "Apple iPhone 14 Pro Max",
    "Apple iPhone 15 Pro Max",
    "Apple iPhone 13 Pro Max",
    "Apple iPhone 11 Pro Max",
    "LG G7 ThinQ",
    "Apple iPhone XS Max",
    "Apple iPhone X",
    "Apple iPhone 8",
    "Apple iPhone 7 Plus"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# We perform a direct search on GSMArena.com search endpoint: https://www.gsmarena.com/results.php3?sQuickSearch=no&sName=...
# Or search gsmarena via search engine with exact HTML parsing
results = {}

for dev in devices:
    search_term = dev.replace("Discovery", "Explorer")
    url = f"https://www.gsmarena.com/res.php3?sSearch={urllib.parse.quote(search_term)}"
    req = urllib.request.Request(url, headers=headers)
    found_url = None
    title = ""
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for device links in search results: <a href="device_slug-id.php"><img ...><span>Phone Name</span></a>
            matches = re.findall(r'href="([a-zA-Z0-9_]+-\d+\.php)"[^>]*>.*?<span>(.*?)</span>', html, re.DOTALL | re.IGNORECASE)
            if matches:
                # Get the best match
                for href, name in matches:
                    clean_name = re.sub(r'<[^>]+>', '', name).strip()
                    found_url = "https://www.gsmarena.com/" + href
                    title = clean_name
                    break
    except Exception as e:
        print(f"[ERR] {dev}: {e}")
        
    print(f"{dev:<25} -> {found_url} (Found: {title})")
    results[dev] = (found_url, title)
    time.sleep(1.2)

print("\n--- Summary ---")
for k, v in results.items():
    print(f"'{k}': '{v[0]}',")
