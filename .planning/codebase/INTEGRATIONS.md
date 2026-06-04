# External Integrations

**Analysis Date:** 2026-06-04

## APIs & External Services

**Scraping Target:**
- GSMArena - Used to retrieve specifications, release dates, and general information for mobile phones.
  - SDK/Client: None (Vanilla HTTP requests via Python `requests` library).
  - Auth: None (Uses standard user-agent and referer headers to bypass simple bot protection).
  - Endpoints used: `https://www.gsmarena.com` and its brand lists/phone spec pages.
  - Rate limiting / Politeness: Uses `time.sleep(random.uniform(1, 2))` between requests to prevent IP blocks.

## Data Storage

**Databases:**
- Flat-File JSON Database - Local directory-based data storage.
  - Location: `data/`
  - Critical files:
    - `data/phones_db.json` - Main storage for scraped raw specs and normalized details.
    - `data/schema.json` - JSON schema defining expected data shapes.
  - Client: Python `json` module, encapsulated in `src/database_manager.py` (`DatabaseManager`).
  - Migrations: Handled programmatically via python normalization or validation scripts.

## Authentication & Identity

- None.

## Monitoring & Observability

- Standard Output (Stdout/Stderr) - Logs execution, failures, and results directly to the terminal using Python `print`.

## CI/CD & Deployment

- None.

## Environment Configuration

**Development:**
- Main DB Path: `data/phones_db.json`
- Test DB Path: `test_data/`
- All paths are relative or defined directly in script entry points. No environment variables are used.

## Webhooks & Callbacks

- None.

---

*Integration audit: 2026-06-04*
*Update when adding/removing external services*
