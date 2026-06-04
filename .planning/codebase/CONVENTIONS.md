# Coding Conventions

**Analysis Date:** 2026-06-04

## Naming Patterns

**Files:**
- snake_case.py for all Python source code files (e.g., `database_manager.py`).
- kebab-case.md or snake_case.md for technical documentation (e.g., `scoring_rules.md`).

**Classes:**
- PascalCase for all class names (e.g., `DatabaseManager`, `PhoneScraper`, `Normalizer`).

**Functions:**
- snake_case for all class methods and functions (e.g., `normalize_phone_data`, `_extract_inches`, `calc_layer_b`).
- Leading underscore `_` prefix for private helper methods inside classes (e.g., `_generate_id`, `_parse_date`).

**Variables:**
- snake_case for all local variable names (e.g., `phone_data`, `wh_raw`, `battery_root`).

**Constants:**
- UPPER_SNAKE_CASE for script-level configuration lookup objects and bounds constants (e.g., `PROCESS_NODE_MIN`, `CPU_SCORES`, `OS_SKIN_SCORES`).

## Code Style

**Formatting:**
- Standard PEP 8 coding style for Python.
- 4-space indentation.
- Double quotes (`"..."`) generally preferred for string literals, though single quotes (`'...'`) are also used.

**Linting:**
- No automated linting tool (e.g. Flake8, Ruff) config file is committed.
- Clean standard syntax must be manually maintained.

## Import Organization

**Order:**
1. Standard libraries (e.g. `import re`, `import json`, `import os`).
2. Third-party packages (e.g. `import requests`, `from bs4 import BeautifulSoup`).
3. Local application imports (e.g. `from normalizer import Normalizer`, `from database_manager import DatabaseManager`).

**Grouping:**
- Blank lines between imports and code definitions.

## Error Handling

**Patterns:**
- Use `try/except` blocks to wrap risky network or file operations.
- Catch general exceptions or specific ones, printing errors directly to standard output: `print(f"Error fetching {url}: {e}")`.
- Return safe default values (e.g., `None`, `[]`, `{}`) instead of bubbling crashes up to user.
- Guard clauses at function entry:
  ```python
  if not phone_data or 'id' not in phone_data:
      print("Invalid phone data, cannot save.")
      return
  ```

## Logging

**Framework:**
- Standard Python `print` function for terminal stdout logging.
- Console feedback is descriptive, indicating starting and completed operations (e.g., `print(f"Saved {phone_data['id']}")`).

## Comments

**When to Comment:**
- Business logic or mathematical scoring rationale should be documented above function/constant definitions.
- Explanatory comment notes indicating where in `scoring_rules.md` a specific section or formula originates.
- Obvious code (e.g., standard variables) should not be commented.

**Docstrings:**
- Module-level triple-quoted string docstrings explaining script usage, limits, inputs, and outputs.
- Function-level docstrings explaining purpose, params, and return types.

**TODO Comments:**
- Format: `# TODO: description` or `# Placeholder for ...`.

## Function Design

**Size:**
- Single functions or calculations generally kept focused, though scoring routines (like `calc_layer_b`) handle multiple computations and dictionary lookups.

**Parameters:**
- Keep parameter lists minimal (mostly single `data` dictionary object containing normalized specs).

**Early Return:**
- Implement early returns or guard clauses to handle missing data or error conditions efficiently.

---

*Convention analysis: 2026-06-04*
*Update when patterns change*
