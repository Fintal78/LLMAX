import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract links from DDG HTML results
            # links are in <a class="result__url" href="..."> or <a class="result__snippet" href="...">
            matches = re.findall(r'href="([^"]*gsmarena\.com[^"]*)"', html)
            # clean ddg redirect urls
            cleaned = []
            for m in matches:
                if "uddg=" in m:
                    actual = urllib.parse.unquote(m.split("uddg=")[1].split("&")[0])
                    cleaned.append(actual)
                elif "gsmarena.com" in m:
                    cleaned.append(m)
            return list(dict.fromkeys(cleaned))
    except Exception as e:
        print(f"Error: {e}")
        return []

print("Realme GT3 review search:")
urls = search_ddg("site:gsmarena.com Realme GT3 review")
for u in urls[:5]:
    print(" ", u)
