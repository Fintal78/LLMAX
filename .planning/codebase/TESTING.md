# Testing Patterns

**Analysis Date:** 2026-06-04

## Test Framework

**Runner:**
- Custom Assertion Runner - Custom python execution script performing assertion-based tests.
- Config: None.

**Assertion Library:**
- Python standard library built-in `assert` statement.
- Examples: `assert normalized_data['id'] == "samsung_galaxy_s24_ultra"`

**Run Commands:**
```bash
python src/verify_pipeline.py          # Runs normalizer and database manager verification checks
python src/battery_score_single_test.py # Executes scoring logic check on example phone data
```

## Test File Organization

**Location:**
- Verification scripts are situated in the `src/` folder alongside application source files.
- Mock fixtures and templates are stored in `tests/`.

**Structure:**
```
src/
  normalizer.py
  database_manager.py
  verify_pipeline.py       # Verification script executing normalizer & DB tests
tests/
  mock_scoring_rules.md    # JSON data file used as a mock test input
```

## Test Structure

**Suite Organization:**
- Tests are organized into top-level functions (e.g., `run_verification()`) inside verification scripts:
```python
def run_verification():
    print("Starting verification...")
    
    # 1. Test Normalizer
    normalizer = Normalizer()
    normalized_data = normalizer.normalize_phone_data(mock_samsung_data)
    
    # Check critical fields
    assert normalized_data['id'] == "samsung_galaxy_s24_ultra"
    ...
```

## Mocking

**Framework:**
- Static dictionaries inside test files representing raw scraper outputs (e.g., `mock_samsung_data` in `src/verify_pipeline.py`).
- No dynamic mocking libraries (such as `unittest.mock`) are used.

**What to Mock:**
- Scraper outputs are mocked using raw nested dictionaries matching actual GSMArena page parsed structures.

## Fixtures and Factories

**Test Data:**
- Dictionaries nested inside the test file (e.g. `mock_samsung_data` in `src/verify_pipeline.py`).
- JSON-style test cases inside `tests/mock_scoring_rules.md`.

## Coverage

**Requirements:**
- No automated code coverage tracking (such as Coverage.py) is implemented.
- Focus is on validating critical paths (normalizer regexes, basic data structures saving and loading).

## Test Types

**Unit & Integration Tests:**
- Validates the `Normalizer` class behavior under controlled inputs.
- Validates the `DatabaseManager` saving and reading operations under `test_data/` directory.

**Manual Verification:**
- CLI run scripts to view terminal calculation summaries and check math correctness manually.

---

*Testing analysis: 2026-06-04*
*Update when test patterns change*
