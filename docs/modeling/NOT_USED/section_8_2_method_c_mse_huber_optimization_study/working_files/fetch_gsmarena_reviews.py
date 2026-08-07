import urllib.request
import urllib.parse
import re
import time
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_html(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def search_device(name):
    query = urllib.parse.quote_plus(name)
    search_url = f"https://www.gsmarena.com/res.php3?sSearch={query}"
    html = get_html(search_url)
    if not html:
        return []
    # Pattern for search results: <a href="device_url"><img ...><strong><span>Device Name</span></strong></a>
    # Or in maker items: <div class="makers"><ul><li><a href="..."><img ...><strong><span>...</span></strong></a>
    matches = re.findall(r'<a href="([^"]+\.php)">.*?<strong><span>([^<]+)</span></strong>', html, re.DOTALL)
    results = []
    for link, title in matches:
        results.append({"title": title.strip(), "specs_url": f"https://www.gsmarena.com/{link}"})
    return results

def get_review_from_specs(specs_url):
    html = get_html(specs_url)
    if not html:
        return None
    # Check for review link in specs page: e.g. <li class="article-info-meta-link"><a href="realme_gt3-review-2544.php">Review</a></li>
    # or <a class="specs-review-link" href="...">...</a>
    # or in meta links
    matches = re.findall(r'<a[^>]+href="([^"]+-review-[^"]+\.php)"[^>]*>.*?Review', html, re.IGNORECASE | re.DOTALL)
    if matches:
        base_review = matches[0]
        if not base_review.startswith("http"):
            base_review = f"https://www.gsmarena.com/{base_review}"
        return base_review
    
    # Also check if there's any -review- link
    matches = re.findall(r'href="([^"]+-review-\d+\.php)"', html)
    if matches:
        base_review = matches[0]
        if not base_review.startswith("http"):
            base_review = f"https://www.gsmarena.com/{base_review}"
        return base_review
    return None

if __name__ == "__main__":
    test_names = ["Realme GT3", "Redmi Note 12 Explorer", "Samsung Galaxy S24 Ultra", "Apple iPhone 16 Pro Max", "Nokia 2.4"]
    for name in test_names:
        print(f"\nSearching for: {name}")
        res = search_device(name)
        print(f"Found {len(res)} results:")
        for r in res[:3]:
            print(f"  Specs: {r['title']} -> {r['specs_url']}")
            rev = get_review_from_specs(r['specs_url'])
            print(f"  Review URL: {rev}")
        time.sleep(1)
