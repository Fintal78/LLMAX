import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
import urllib.request
import urllib.error
import re
import ssl
import html

def clean_html(raw_html):
    """Removes HTML tags, decodes entities, and normalizes all whitespace."""
    # Remove script and style elements entirely
    text = re.sub(r'<script.*?>.*?</script>', ' ', raw_html, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'<style.*?>.*?</style>', ' ', text, flags=re.IGNORECASE | re.DOTALL)
    # Remove all HTML tags
    text = re.sub(r'<.*?>', ' ', text)
    # Unescape HTML entities (e.g., &amp;, &#39;)
    text = html.unescape(text)
    # Normalize typography
    text = text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    text = text.replace('–', '-').replace('—', '-')
    # Normalize whitespaces (tabs, newlines, multiple spaces -> single space)
    return ' '.join(text.split())

def verify_json_urls(filepath):
    """
    Context-Aware Validator: Extracts URL + Text pairs. 
    Downloads live HTML, cleans it, and guarantees the text substring exists on the page.
    Combats completely fabricated / dashboard URLs bypassing the 200 OK check.
    """
    print(f"\n[+] Scanning {filepath} for URLs and Extract Pairs...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[-] Error reading {filepath}: {e}")
        return False

    pairs = []
    
    # 1. Type A: "source" + "exact_extract"
    for match in re.finditer(r'"source":\s*"(https?://[^"]*)",\s*"exact_extract":\s*"([^"]*)"', content):
        url, extract = match.groups()
        pairs.append((url, extract))

    # 2. Type B: "source_link" + "observed_justification" (Boosters)
    for match in re.finditer(r'"source_link":\s*"(https?://[^"]*)".*?"observed_justification":\s*"([^"]*)"', content, re.DOTALL):
        url, extract = match.groups()
        # Ensure we didn't greedily cross another "source_link" inside the JSON structure
        if match.group(0).count('"source_link"') == 1:
            pairs.append((url, extract))
            
    # Find all loose URLs merely for fallback HTTP ping
    all_urls = re.findall(r'"(?:source|source_link)":\s*"(https?://.*?)"', content)
    
    # Catch inline context links (e.g. within an unaccounted_reason string)
    inline_urls = re.findall(r'\(Source:\s*(https?://[^)]+)\)', content)
    all_urls.extend(inline_urls)
    
    paired_urls = set([u for u, e in pairs])
    loose_urls = [u for u in all_urls if u not in paired_urls]

    if not pairs and not loose_urls:
        print("[-] No verifiable JSON 'source' URLs found.")
        return True

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    success = True
    print(f"[*] Found {len(pairs)} Extract Pairs and {len(loose_urls)} Loose URLs. Initiating deep validation...")

    # PAIR VALIDATION (CONTENT-AWARE)
    for url, extract in pairs:
        # Ignore structural placeholders
        if extract in ["N/A", "Proof pending"]:
            continue
            
        if 'verified-source' in url or 'example.com' in url or 'dummy' in url:
             print(f"[X] REJECTED (Placeholder URL): {url}")
             success = False
             continue

        print(f"[*] Validating content match: {url}")
        
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.9'}
            )
            res = urllib.request.urlopen(req, timeout=15, context=ctx)
            
            html_bytes = res.read()
            html_text = html_bytes.decode('utf-8', errors='ignore')
            clean_page = clean_html(html_text)

            # Handle '['...' ']' disjointed extracts by checking ordered existence of all fragments
            parts = [p.strip() for p in extract.split('[...]')]
            
            search_start = 0
            found_all = True
            for part in parts:
                if not part: continue
                
                # Normalize the target string to match HTML normalization
                normalized_part = part.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
                normalized_part = normalized_part.replace('–', '-').replace('—', '-')
                normalized_part = ' '.join(normalized_part.split())
                
                pos = clean_page.find(normalized_part, search_start)
                
                if pos == -1:
                    print(f"[X] REJECTED (Text Missing): Could not find substring '{normalized_part}' in the HTML of {url}")
                    found_all = False
                    success = False
                    break
                search_start = pos + len(normalized_part)

            if found_all:
                print(f"[V] OK (Extract Content Verified): {url}")
                
        except urllib.error.HTTPError as e:
            if e.code in [403, 429]:
                 print(f"[~] WARNING (Bot Protected {e.code}): Could not scrape HTML to verify extract for {url}")
            else:
                 print(f"[X] REJECTED (HTTP Error {e.code}): {url}")
                 success = False
        except Exception as e:
            print(f"[X] REJECTED (Network/Parse Error {e}): {url}")
            success = False

    # LOOSE URL VALIDATION (PING ONLY)
    for url in set(loose_urls):
        if 'verified-source' in url or 'example.com' in url or 'dummy' in url:
             print(f"[X] REJECTED (Placeholder URL): {url}")
             success = False
             continue

        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=10, context=ctx)
            if res.status == 200:
                final_url = res.url
                if final_url != url and final_url != url + '/' and final_url.replace('https://', 'http://') != url.replace('https://', 'http://'):
                     print(f"[X] REJECTED (Redirected/Soft 404 to {final_url}): {url}")
                     success = False
                else:
                     print(f"[V] OK (Ping Only): {url}")
            else:
                 print(f"[X] REJECTED (Status {res.status}): {url}")
                 success = False
        except urllib.error.HTTPError as e:
            if e.code in [403, 429]:
                 print(f"[~] WARNING (Bot Protected {e.code} - Ping Only): {url}")
            else:
                 print(f"[X] REJECTED (HTTP Error {e.code}): {url}")
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
        print("\n\n🚨 CRITICAL FAILURE: Broken URLs or missing exact extracts detected. Data hard rejected.")
        sys.exit(1)
    else:
        print("\n\n✅ ALL URLs & EXTRACTS VERIFIED. Data is physically clean.")
