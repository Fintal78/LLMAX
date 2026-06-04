# Architecture

**Analysis Date:** 2026-06-04

## Pattern Overview

**Overall:** Script-based Data Processing Pipeline.

**Key Characteristics:**
- CLI (Command Line Interface) executions via individual entry scripts.
- Multi-step pipelined data flow: Scraping -> Normalization -> Scoring -> Database Storage.
- File-based JSON data management.

## Layers

**Scraping Layer:**
- Purpose: Retrieve raw hardware specs and launch details from remote sources.
- Contains: `src/scraper.py`, `src/scraper_client.py`
- Depends on: `requests` and `beautifulsoup4`
- Used by: CLI user / automated scripts

**Normalization Layer:**
- Purpose: Parse, clean, and structure messy raw specifications text into formatted fields.
- Contains: `src/normalizer.py`
- Depends on: Python standard libraries
- Used by: Scoring and verification logic

**Database Layer:**
- Purpose: Read and write phone records to the local JSON file database.
- Contains: `src/database_manager.py`
- Depends on: Standard JSON file I/O
- Used by: Scraping pipeline, scoring scripts

**Scoring & Modeling Layer:**
- Purpose: Implement multi-layered mathematical models to score battery endurance and performance capabilities.
- Contains: `src/battery_score_single_test.py`, `src/battery_score_full_database.py`, `src/battery_score_new_phone.py`, `src/thermal_sim.py`, `src/scoring_utils.py`
- Depends on: Normalization and Database layers, `docs/scoring_rules.md`
- Used by: CLI user / DB manager

## Data Flow

**Scraping & Normalization Flow:**
1. User executes scraper via `python src/scraper.py`.
2. Scraper fetches brand lists and phone specification pages from GSMArena.
3. BS4 (BeautifulSoup 4) extracts table-based specifications into a dictionary.
4. Raw data is normalized via `Normalizer` to clean up text, extract values (e.g. screen sizes, RAM, battery mAh).
5. DatabaseManager saves the structured JSON data locally to `data/phones_db.json`.

**Scoring Flow:**
1. Scoring script (e.g. `src/battery_score_single_test.py`) reads normalized specifications.
2. Layer A calculations: Computes battery energy in Wh (Watt-hours).
3. Layer B calculations: Computes hardware efficiency based on SoC (System on Chip) architecture, display technology, connectivity, and thermals (TDSI - Thermal Dissipation Stability Index).
4. Layer C calculations: Computes software optimization scores (OS version, cleanliness/bloatware).
5. Predicted score is calculated from A, B, and C weights.
6. Benchmarks are loaded and normalized.
7. Final score is computed (using benchmarks or fallback to predicted score with interpolation) and written back to the target file.

## Key Abstractions

**PhoneScraper:**
- Location: `src/scraper.py`
- Purpose: Handles HTTP requests, rate-limiting delays, and DOM parsing.
- Pattern: Object-oriented worker class.

**Normalizer:**
- Location: `src/normalizer.py`
- Purpose: Regex-based field extraction (inches, resolution, RAM, etc.).
- Pattern: Stateless processor class.

**DatabaseManager:**
- Location: `src/database_manager.py`
- Purpose: Simplifies file-system read/write operations for phone records.
- Pattern: File-based Repository.

## Entry Points

**Scraper Entry:**
- Location: `src/scraper.py`
- Triggers: CLI execution (`python src/scraper.py`)
- Responsibilities: Crawl and save Samsung/Apple phone specifications.

**Verification Entry:**
- Location: `src/verify_pipeline.py`
- Triggers: CLI execution (`python src/verify_pipeline.py`)
- Responsibilities: Run pipeline unit assertions on normalizer and database manager.

**Scoring Entry:**
- Location: `src/battery_score_single_test.py`
- Triggers: CLI execution (`python src/battery_score_single_test.py`)
- Responsibilities: Parse and calculate scores for the example phone in `docs/proposed_data_structure.md`.

## Error Handling

**Strategy:** Fail fast during pipeline validations, print descriptive logs, and exit.
- HTTP requests: Catch general network and status exceptions, log URL, skip on failure.
- JSON parsing: Handle JSONDecodeError with fallbacks to empty collections to prevent crashes.
- Calculations: Validate values (e.g. non-zero denominators) and clamp ranges to protect against division by zero and extreme values.

---

*Architecture analysis: 2026-06-04*
*Update when major patterns change*
