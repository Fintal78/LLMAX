---
description: Standardized workflow for adding a new phone to the database (Scraping -> Scoring -> Boosters -> Commit)
---

# Standardized Phone Addition Workflow

This workflow is the **SINGLE SOURCE OF TRUTH** for adding a new phone to the database. It orchestrates the entire process and strictly enforces the rules defined in `docs/scoring_rules.md`.

## Phase 1: Data Acquisition & Ancestry (The "Source of Truth")

**CRITICAL PROTOCOL:** Every single data point scraped or entered into the database must be traceable back to its origin. We do not accept "trust me" values.

### 1.1 The "Data Ancestry" Triple
For every input parameter (e.g., `frame_material`, `peak_nits`, `battery_mah`), you **MUST** replace the simple value with a **Data Object** containing 3 fields:

1.  **`value`**: The actual data (string, number, boolean, or array).
2.  **`source`**: The **ACTIVE, DIRECT URL** where this specific value was found.
    *   *Preference:* Official Manufacturer Page > Detailed Review (NotebookCheck, DXOMARK) > Spec Aggregator (GSMArena).
3.  **`exact_extract`**: A **VERBATIM** copy-paste substring from the webpage that contains the value.
    *   *Requirement:* A text search (Ctrl+F) for this string on the `source` URL **must** return a match.
    *   *Purpose:* automated verification and auditability.

#### 1.2 Schema Example
**Old (Forbidden):**
```json
"1_1_materials": {
  "frame_material": "Titanium Alloy"
}
```

**New (Required):**
```json
"1_1_materials": {
  "frame_material": {
    "value": "Titanium Alloy",
    "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
    "exact_extract": "Titanium Frame"
  }
}
```

### 1.3 Scope of Application
*   **APPLY TO:** All "Input" parameters scraped from the web (Sections 1-10 inputs, Identity, etc.).
*   **DO NOT APPLY TO:**
    *   Calculated fields (`predicted_score`, `final_score`, `total_hei_score`).
    *   Internal schema structures (`meta`, `scoring_components`).
    *   `score_adjustment` blocks (these follow the Booster schema).

1.  **Scrape Specs**: Run `src/scraper.py` to populate these 3 fields automatically where possible.
2.  **Verify Data**: Manually verify that `exact_extract` is indeed present on `source` for key differentiators.

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

2.  **Schema Implementation (Data Structure Update)**:
    
    **CRITICAL RULE:** The `score_adjustment` block must ONLY exist in a subsection if there is at least one active booster defined in Section 11 that targets that subsection.
    
    **Step-by-Step Integration Process:**
    
    **Step 1: Identify the Target Subsection**
    - Locate the subsection number from the booster definition in Section 11.
    - Example: If `"impacted_subsection": "4.16"`, navigate to the `4_16_multiframe_photo` object in the JSON.
    
    **Step 2: Add the `score_adjustment` Block**
    - Insert the `score_adjustment` object immediately after `predicted_score` and before `final_score`.
    - The structure must follow this exact format:
    
    ```json
    "predicted_score": 0.0,
    "score_adjustment": {
      "booster_1": {
        "value": 1.05,
        "booster_title": "11_1_dxomark_24mp_texture_rendering"
      }
    },
    "final_score": 0.0
    ```
    
    **Step 3: Booster Field Structure**
    - Each booster is named `booster_N` where N is a sequential integer starting from 1.
    - If a subsection has multiple boosters, use `booster_1`, `booster_2`, `booster_3`, etc.
    - Each `booster_N` object contains exactly **2 required fields**:
        1. **`value`** (number): The numeric multiplier (e.g., `1.05` for +5%, `0.95` for -5%).
        2. **`booster_title`** (string): The exact key name from Section 11 (e.g., `"11_2_toms_guide_display_factory_calibration"`).
    
    **Step 4: Multiple Boosters Example**
    - If a subsection has 2 boosters:
    
    ```json
    "score_adjustment": {
      "booster_1": {
        "value": 1.05,
        "booster_title": "11_1_dxomark_24mp_texture_rendering"
      },
      "booster_2": {
        "value": 1.03,
        "booster_title": "11_4_another_review_source"
      }
    }
    ```
    
    **Step 5: Cleanup Rule**
    - If a subsection has NO boosters, the entire `score_adjustment` block must be **completely removed**.
    - Do NOT leave empty `score_adjustment` objects or default values like `"booster": 1.0`.
    
    **Step 6: Verification Checklist**
    - [ ] `booster_title` exactly matches the key in Section 11 (case-sensitive, including underscores).
    - [ ] `value` is a valid decimal number (typically between 0.90 and 1.10).
    - [ ] Sequential numbering: `booster_1`, `booster_2`, `booster_3` (no gaps).
    - [ ] No legacy fields: `source` field has been removed.
    - [ ] Placement: `score_adjustment` appears between `predicted_score` and `final_score`.

## Phase 4: Final Commit
1.  **Update Database**: Commit the new JSON entry to the database.
2.  **Regenerate Rankings**: Run `src/normalizer.py` (or equivalent) to update global rankings.
