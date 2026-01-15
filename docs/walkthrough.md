# Smartphone Database Walkthrough

I have successfully created a tool to generate a database of Apple and Samsung smartphones.

## How to Run

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Scraper**:
    ```bash
    python scraper.py
    ```
    This will fetch phones from Samsung and Apple. It saves progress incrementally to `phones_db.json`. You can stop and restart it at any time; it will skip phones that are already in the database.

    > **Note**: The scraper may hit rate limits (Error 429) if run for too long. Just wait a while and run it again to continue.

## Output

The output is a JSON file `phones_db.json` in the project folder.

### Structure

```json
{
  "summary": {
    "total_phones": 61,
    "brands": {
      "Samsung": 56,
      "Apple": 5
    }
  },
  "phones": [
    {
      "brand": "Samsung",
      "model_name": "Samsung Galaxy S25 Ultra",
      "specs": {
        "Network": {
          "Technology": "GSM / CDMA / HSPA / EVDO / LTE / 5G",
          "5G bands": ["1", "3", "5", "7", "8", "20", "28", "38", "40", "41", "66", "77", "78 SA/NSA/Sub6"]
        },
        "Display": {
          "Type": "Dynamic LTPO AMOLED 2X, 120Hz...",
          "Size": "6.9 inches...",
          "size_inches": 6.9
        }
      }
    },
    ...
  ]
}
```

## Verification Results

-   **Iterative Scraping**: Validated that the scraper skips existing URLs and appends new ones.
-   **Data Quality**:
    -   Network bands are now parsed into lists (e.g., `["1", "3", "5"]`) instead of long strings.
    -   Display size is parsed into a number (`size_inches`).
    -   Text is cleaned of excessive whitespace.
-   **Summary**: The file now starts with a summary of the total count and breakdown by brand.
