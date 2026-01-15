import requests
import json
import time
import os

class ScraperClient:
    def __init__(self, base_url="http://localhost:3000"):
        # Using a placeholder URL for the local instance of the scraper API
        # In a real scenario, this would point to the hosted instance or local service
        self.base_url = base_url
        self.session = requests.Session()

    def get_brands(self):
        """Fetch list of all brands."""
        try:
            response = self.session.get(f"{self.base_url}/brands")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching brands: {e}")
            return []

    def get_phones_by_brand(self, brand_slug):
        """Fetch all phones for a specific brand."""
        phones = []
        page = 1
        while True:
            try:
                # Assuming the API supports pagination or returns all in one go
                # Adjusting logic based on common API patterns for this specific scraper
                url = f"{self.base_url}/brands/{brand_slug}?page={page}"
                print(f"Fetching {url}...")
                response = self.session.get(url)
                response.raise_for_status()
                data = response.json()
                
                if 'data' in data:
                    current_phones = data['data']
                else:
                    current_phones = data

                if not current_phones:
                    break
                
                phones.extend(current_phones)
                
                # Simple pagination check - if we got fewer than expected, might be last page
                # Or check specific pagination fields if available
                if 'last_page' in data and page >= data['last_page']:
                    break
                
                page += 1
                time.sleep(1) # Be polite
            except requests.RequestException as e:
                print(f"Error fetching phones for {brand_slug} page {page}: {e}")
                break
        return phones

    def get_phone_details(self, phone_slug):
        """Fetch detailed specs for a specific phone."""
        try:
            url = f"{self.base_url}/phones/{phone_slug}"
            print(f"Fetching details for {phone_slug}...")
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching details for {phone_slug}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    client = ScraperClient()
    # Test with Samsung (usually 'samsung-phones-9') or similar slug depending on API
    # This requires the actual API to be running.
    pass
