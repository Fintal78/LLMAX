# Technology Stack

**Analysis Date:** 2026-06-04

## Languages

**Primary:**
- Python 3.x - Used for all application logic, scraping, database management, scoring calculation, and validation scripts.

## Runtime

**Environment:**
- Python 3 Runtime - Script execution environment.
- No browser or server runtime (CLI tool and local processing only).

**Package Manager:**
- pip - Package installer for Python.
- Lockfile: None (simple `requirements.txt` present).

## Frameworks

**Core:**
- None - Vanilla Python script-based utility tools.

**Testing:**
- Custom assertions - Basic inline Python assertions in verification scripts (e.g., `src/verify_pipeline.py`).

**Build/Dev:**
- None - Raw Python scripts executed directly.

## Key Dependencies

**Critical:**
- `requests` - Used in `src/scraper.py` and `src/scraper_client.py` for fetching HTML pages from GSMArena and raw data sources.
- `beautifulsoup4` (bs4) - Used in `src/scraper.py` for parsing HTML/DOM trees.

**Infrastructure:**
- Python Standard Library built-ins - `json`, `os`, `sys`, `re`, `time`, `random`, `math` for processing, logic, parsing, and math equations.

## Configuration

**Environment:**
- File-based paths - Configuration for DB paths and source files is done directly within the Python script's `__main__` entry blocks or via inline function arguments (e.g., `db_path`).

**Build:**
- None.

## Platform Requirements

**Development:**
- Any OS (Windows/macOS/Linux) with Python 3.x and dependencies installed via `requirements.txt`.

**Production:**
- Local execution via Python command line.

---

*Stack analysis: 2026-06-04*
*Update after major dependency changes*
