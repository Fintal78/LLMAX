import requests
from bs4 import BeautifulSoup
import json
import time
import re
import random
import os

class PhoneScraper:
    def __init__(self, db_path):
        self.base_url = "https://www.gsmarena.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.google.com/'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.db_path = db_path
        self.existing_data = self.load_db()
        self.existing_urls = {phone['url'] for phone in self.existing_data.get('phones', [])}

    def load_db(self):
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        return {"summary": {}, "phones": data}
                    return data
            except json.JSONDecodeError:
                return {"summary": {}, "phones": []}
        return {"summary": {}, "phones": []}

    def save_db(self, new_phones):
        # Merge new phones with existing
        all_phones = self.existing_data.get('phones', []) + new_phones
        
        # Deduplicate by URL just in case
        unique_phones = {p['url']: p for p in all_phones}.values()
        all_phones_list = list(unique_phones)
        
        # Calculate summary
        brand_counts = {}
        for p in all_phones_list:
            b = p.get('brand', 'Unknown')
            brand_counts[b] = brand_counts.get(b, 0) + 1
            
        summary = {
            "total_phones": len(all_phones_list),
            "brands": brand_counts
        }
        
        data = {
            "summary": summary,
            "phones": all_phones_list
        }
        
        # Atomic write (sort of) to prevent corruption
        temp_path = self.db_path + ".tmp"
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        os.replace(temp_path, self.db_path)
        
        # Update internal state
        self.existing_data = data
        self.existing_urls = {phone['url'] for phone in all_phones_list}
        print(f"Saved {len(all_phones_list)} phones to {self.db_path}")

    def get_soup(self, url):
        try:
            time.sleep(random.uniform(1, 2)) # Be polite
            print(f"Fetching {url}...")
            response = self.session.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def clean_text(self, text):
        if not text:
            return None
        # Remove multiple spaces, newlines, non-breaking spaces
        text = re.sub(r'[\r\n\t]+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def parse_memory(self, memory_str):
        if not memory_str:
            return None
        return self.clean_text(memory_str)

    def parse_display(self, display_obj):
        if not display_obj:
            return {}
        
        cleaned = {}
        for k, v in display_obj.items():
            cleaned[k] = self.clean_text(v)
            
        if 'Size' in cleaned:
            match = re.search(r'(\d+(\.\d+)?)\s*inches', cleaned['Size'])
            if match:
                cleaned['size_inches'] = float(match.group(1))
        
        return cleaned

    def parse_network(self, network_obj):
        cleaned = {}
        for k, v in network_obj.items():
            v_clean = self.clean_text(v)
            # User requested compact form (single line string)
            # If it was previously split, we join it back or just keep it as string
            # We ensure it's a clean string
            cleaned[k] = v_clean
        return cleaned

    def parse_specs(self, soup):
        specs = {}
        specs_list = soup.find('div', id='specs-list')
        if not specs_list:
            return specs

        for table in specs_list.find_all('table'):
            rows = table.find_all('tr')
            if not rows:
                continue
            
            main_category = None
            first_th = rows[0].find('th')
            if first_th:
                main_category = self.clean_text(first_th.get_text())
            
            if not main_category:
                continue

            specs[main_category] = {}
            
            for row in rows:
                ttl = row.find('td', class_='ttl')
                nfo = row.find('td', class_='nfo')
                
                if ttl and nfo:
                    key = self.clean_text(ttl.get_text())
                    value = self.clean_text(nfo.get_text())
                    
                    if not key:
                        key = "Other"
                        
                    if key in specs[main_category]:
                        if isinstance(specs[main_category][key], list):
                            specs[main_category][key].append(value)
                        else:
                            specs[main_category][key] = [specs[main_category][key], value]
                    else:
                        specs[main_category][key] = value
        
        # Post-processing
        if 'Display' in specs:
            specs['Display'] = self.parse_display(specs['Display'])
        if 'Network' in specs:
            specs['Network'] = self.parse_network(specs['Network'])
            
        return specs

    def scrape_brand(self, brand_name, brand_url, max_pages=5):
        current_url = brand_url
        pages_scraped = 0
        new_phones_batch = []
        
        while current_url and pages_scraped < max_pages:
            print(f"Scraping {brand_name} page {pages_scraped + 1}...")
            soup = self.get_soup(current_url)
            if not soup:
                break
                
            makers_div = soup.find('div', class_='makers')
            if not makers_div:
                break

            phones_on_page = []
            for li in makers_div.find_all('li'):
                link = li.find('a')
                if link:
                    phone_url = f"{self.base_url}/{link['href']}"
                    
                    if phone_url in self.existing_urls:
                        print(f"  Skipping {phone_url} (already exists)")
                        continue
                        
                    img_tag = link.find('img')
                    phone_name = img_tag['title'] if img_tag and 'title' in img_tag.attrs else link.get_text()
                    phone_name = phone_name.split(' Android smartphone')[0]
                    
                    phones_on_page.append({
                        'name': phone_name,
                        'url': phone_url
                    })
            
            for phone in phones_on_page:
                safe_name = phone['name'].encode('ascii', 'ignore').decode('ascii')
                print(f"  Scraping {safe_name}...")
                
                soup_phone = self.get_soup(phone['url'])
                if soup_phone:
                    specs = self.parse_specs(soup_phone)
                    phone_data = {
                        "brand": brand_name,
                        "model_name": phone['name'],
                        "url": phone['url'],
                        "specs": specs
                    }
                    new_phones_batch.append(phone_data)
            
            if new_phones_batch:
                self.save_db(new_phones_batch)
                new_phones_batch = []
            
            nav_pages = soup.find('div', class_='nav-pages')
            if nav_pages:
                next_link = nav_pages.find('a', title="Next page")
                if next_link:
                    current_url = f"{self.base_url}/{next_link['href']}"
                    pages_scraped += 1
                else:
                    current_url = None
            else:
                current_url = None

if __name__ == "__main__":
    db_path = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\data\phones_db.json"
    scraper = PhoneScraper(db_path)
    brands = {
        "Samsung": "https://www.gsmarena.com/samsung-phones-9.php",
        "Apple": "https://www.gsmarena.com/apple-phones-48.php"
    }
    for brand, url in brands.items():
        scraper.scrape_brand(brand, url, max_pages=2)
