import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
import urllib.request
import re
import ssl

def verify_json_urls(filepath):
    """
    A strict deterministic script designed to scan JSON/Markdown files 
    for the "source" key and physically ping every URL it finds. 
    It combats LLM generative hallucinations by enforcing a hard 200 OK status.
    """
    print(f"\n[+] Scanning {filepath} for URLs...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[-] Error reading {filepath}: {e}")
        return False

    # Extract all strings following "source": "
    urls = re.findall(r'"source":\s*"(https?://.*?)"', content)
    
    if not urls:
        print("[-] No JSON 'source' URLs found.")
        return True

    # Bypass SSL verification for aggressive scraping
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    success = True
    print(f"[*] Found {len(urls)} URLs. Initiating connection pings...")

    for url in set(urls): # Use set to avoid pinging identical URLs multiple times
        # 1. Explicitly ban placeholder structures
        if 'verified-source' in url or 'example.com' in url or 'dummy' in url:
             print(f"[X] REJECTED (Placeholder/Hallucination): {url}")
             success = False
             continue
             
        # 2. Physically Ping the URL
        try:
            # We spoof the User-Agent to bypass basic scraping blocks (like Cloudflare 403s on specs sites)
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
            )
            res = urllib.request.urlopen(req, timeout=10, context=ctx)
            
            if res.status == 200:
                print(f"[V] OK: {url}")
            else:
                 print(f"[X] REJECTED (Status {res.status}): {url}")
                 success = False
                 
        except Exception as e:
            print(f"[X] REJECTED (Error {e}): {url}")
            success = False
            
    return success

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python verify_urls.py <markdown_or_json_file>")
        sys.exit(1)
        
    all_passed = True
    for file in sys.argv[1:]:
        if not verify_json_urls(file):
            all_passed = False
            
    if not all_passed:
        print("\n\n🚨 CRITICAL FAILURE: Broken or hallucinated URLs detected. Data rejected.")
        sys.exit(1)
    else:
        print("\n\n✅ ALL URLs VERIFIED. Data is clean.")
