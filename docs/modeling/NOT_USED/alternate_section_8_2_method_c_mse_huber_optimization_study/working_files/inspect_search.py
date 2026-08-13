import urllib.request

req = urllib.request.Request(
    'https://www.gsmarena.com/res.php3?sSearch=Realme+GT3',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Status: {resp.status}, Length: {len(html)}")
        print(html[:1000])
except Exception as e:
    print('Error:', e)
