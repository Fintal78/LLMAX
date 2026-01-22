---
description: Standardized workflow for adding a new phone to the database (Scraping -> Scoring -> Boosters -> Commit)
---

# Standardized Phone Addition Workflow

This workflow is the **SINGLE SOURCE OF TRUTH** for adding a new phone to the database. It orchestrates the entire process and strictly enforces the rules defined in `docs/scoring_rules.md`.

## Phase 1: Data Acquisition
1.  **Scrape Specs**: Run `src/scraper.py` (or equivalent) to fetch raw data for the new device.
2.  **Verify Data**: Manually verify the scraped data against official manufacturer specifications, referencing `docs/proposed_data_structure.md` for schema compliance.

## Phase 2: Automated Scoring
1.  **Run Base Scoring**: Execute `src/battery_score_new_phone.py` (and any other relevant scoring scripts).
2.  **Review Output**: Check the generated scores against the baselines defined in `docs/scoring_rules.md`.

## Phase 3: Performance Boosters (The "Human Element")
**CRITICAL:** This phase strictly enforces `docs/scoring_rules.md` Section 11. **DO NOT** deviate from the rules defined there.

1.  **Execute Section 11 Process**:
    *   **Eligibility Check**: Follow **Section 11.A** (Eligibility Criteria) to determine if a booster is warranted. *Note the Exclusion List.*
    *   **Justification Logic**: Follow **Section 11.B** (Justification Logic) to construct a valid argument.
    *   **Evidence Collection**: Follow **Section 11.C** (Output & Evidence Requirements).
        *   **MANDATORY ACTION**: You **MUST** perform the **Source Verification** step defined in Rule 11.C (e.g., using `read_url_content` to verify the link and extract).
        *   **LITMUS TEST**: Apply the "Blind Test" and "Connector Test" to your chosen extract. If it fails, find a better one.
    *   **Verification**: Follow **Section 11.D** (Process) to verify the booster before finalizing.

## Phase 4: Final Commit
1.  **Update Database**: Commit the new JSON entry to the database.
2.  **Regenerate Rankings**: Run `src/normalizer.py` (or equivalent) to update global rankings.
