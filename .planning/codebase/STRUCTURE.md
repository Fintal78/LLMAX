# Codebase Structure

**Analysis Date:** 2026-06-04

## Directory Layout

```
[project-root]/
├── data/               # Local database files
│   ├── phones_db.json  # Main database for scraped data
│   └── schema.json     # Database schema guidelines
├── docs/               # Technical specs and scoring documentation
│   ├── proposed_data_structure.md  # Detailed schema definitions & mock S24 Ultra
│   ├── scoring_rules.md            # Complete scoring equations & methodology
│   └── ...
├── src/                # Python source files
│   ├── scraper.py      # GSMArena specs scraper
│   ├── normalizer.py   # Raw to structured normalizer
│   ├── database_manager.py         # File-based DB repository manager
│   ├── scoring_utils.py            # Shared math/constants loader
│   ├── verify_pipeline.py          # Basic assertion-based verification
│   └── battery_score_*.py          # Battery scoring scripts
├── test_data/          # Temporary test output database
├── tests/              # Test assets
│   └── mock_scoring_rules.md       # JSON-structured test fixtures
└── requirements.txt    # Project dependencies
```

## Directory Purposes

**data/**
- Purpose: Stores active database files.
- Contains: JSON database files.
- Key files: `phones_db.json` (phone specifications database), `schema.json` (target schema structure).

**docs/**
- Purpose: Technical specs, math formulas, reference guidelines, and mock examples.
- Contains: Markdown technical documentation.
- Key files: `proposed_data_structure.md` (active target schema details), `scoring_rules.md` (formulas for CPU, GPU, display, thermal, software, and battery scoring).

**src/**
- Purpose: Core Python codebase scripts.
- Contains: `.py` Python scripts.
- Key files:
  - `scraper.py` - crawler and DOM extraction.
  - `normalizer.py` - parses string specifications to structured numbers and tokens.
  - `database_manager.py` - interfaces reading/writing JSON files.
  - `battery_score_single_test.py` - scores example S24 Ultra phone.
  - `verify_pipeline.py` - checks parsing/DB behavior with assertions.

**tests/**
- Purpose: Mock fixtures for verification checks.
- Contains: Markdown-formatted JSON test inputs.
- Key files: `mock_scoring_rules.md` (assert inputs).

## Key File Locations

**Entry Points:**
- `src/scraper.py`: Scrapes Samsung/Apple phones.
- `src/verify_pipeline.py`: Validates normalizer & database manager.
- `src/battery_score_single_test.py`: Calculates scores for a single phone.
- `src/battery_score_full_database.py`: Scores the entire database.

**Configuration:**
- `requirements.txt`: Python package requirements.
- `docs/scoring_constants.md` / `src/scoring_utils.py`: Constants utilized during scoring computations.

**Core Logic:**
- `src/normalizer.py`: Normalization processor.
- `src/database_manager.py`: Database reader/writer.
- `src/battery_score_single_test.py`: Calculations for battery scores.

**Testing:**
- `src/verify_pipeline.py`: Main validation file.

**Documentation:**
- `docs/proposed_data_structure.md`: Schema guidelines.
- `docs/scoring_rules.md`: CPU/GPU/Thermal mathematical models.

## Naming Conventions

**Files:**
- snake_case.py: Python source code (e.g., `database_manager.py`).
- kebab-case.md or UPPERCASE.md: Documentation files (e.g., `scoring_rules.md` or `README.md`).

**Directories:**
- snake_case: All directories (e.g., `test_data`).

**Special Patterns:**
- `battery_score_*.py` - Scripts performing various battery calculation operations.

## Where to Add New Code

**New Scraper Feature:**
- Implementation: `src/scraper.py`
- Tests: `src/verify_pipeline.py` or new script in `src/`

**New Scoring Model/Formula:**
- Constants: `docs/scoring_rules.md` and load constants.
- Implementation: `src/battery_score_single_test.py` and `src/battery_score_full_database.py`

**New Test Mock:**
- Add entry to `tests/mock_scoring_rules.md`

---

*Structure analysis: 2026-06-04*
*Update when directory structure changes*
