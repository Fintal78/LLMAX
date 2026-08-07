import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

def search_bing(query):
    url = f"https://www.bing.com/search?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract links from Bing
            matches = re.findall(r'href="(https://www\.gsmarena\.com/[^"]+)"', html)
            return list(dict.fromkeys(matches))
    except Exception as e:
        print(f"Error: {e}")
        return []

test_phones = ["Redmi Note 12 Explorer", "iQOO 11 Pro", "Xiaomi 13 Pro", "Xiaomi 12T Pro", "Poco F4 GT", "Vivo X100 Pro", "OnePlus 12", "OnePlus 11"]
for p in test_phones:
    urls = search_bing(f"site:gsmarena.com {p} review")
    print(f"\n{p}:")
    for u in urls[:4]:
        print("  ", u)
