# Algorithmic Rulebook for Smartphone Database (AI Strict Mode)

## 0. GLOBAL CONSTRAINTS

**SCOPE:** Entire JSON File

**CONSTRAINT 1 (Single Source):**
A raw data value **MUST** appear in exactly **ONE** place.

**CONSTRAINT 2 (Type Compliance):**
Every leaf node **MUST** be clearly identified as Type A (Raw), Type B (Reference), or Type C (Derivation).

**CONSTRAINT 3 (No Formulas):**
The JSON **MUST NOT** contain formula logic, only results.

**CONSTRAINT 4 (Validation):**
-   `source` **MUST** match Regex `^https?://` (HTTP/HTTPS URL).
-   `exact_extract` **MUST** be a non-empty string found verbatim on the `source` page.
-   `meta.schema_version` **MUST** match current version.

---

## 1. FILE STRUCTURE ALGORITHM

### TRIGGER: Initial File Creation

**ACTION:** GENERATE strict root object:

```json
{
  "meta": {
    "schema_version": "5.1",
    "last_updated": "<TODAY>"
  },
  "identity": { <IDENTITY_OBJECT_SCHEMA> },
  "1_cellular": { ... },
  ...
  "11_reviews_and_performance_boosters": { ... }
}
```

---

## 2. SCENARIO A: IDENTITY OBJECT

### TRIGGER: `identity` Key

**ACTION:** GENERATE strict object with normalized IDs.

**SCHEMA:**

```json
"identity": {
  "id": {
    "value": "<NORMALIZED_STRING>",
    "source": "<URL>",
    "exact_extract": "<TEXT>"
  },
  "brand": {
    "value": "<STRING>",
    "source": "<URL>",
    "exact_extract": "<TEXT>"
  },
  "model_name": {
    "value": "<STRING>",
    "source": "<URL>",
    "exact_extract": "<TEXT>"
  },
  "model_aliases": {
    "value": [<STRINGS>],
    "source": "<URL>",
    "exact_extract": "<TEXT>"
  },
  "release_date": {
    "value": "<YYYY-MM-DD>",
    "source": "<URL>",
    "exact_extract": "<TEXT>"
  }
}
```

---

## 3. SCENARIO B: NON-SCORING DATA (TYPE A)

### TRIGGER: Data Point NOT used in Scoring Formula

**LOCATION:** Root of Parent Section (e.g., `2_display`).

**ACTION:** GENERATE Type A Object.

**SCHEMA:**

```json
"<key_name>": {
  "value": <DATA_VALUE>,
  "source": "<URL>",
  "exact_extract": "<VERBATIM_TEXT>"
}
```

---

## 4. SCENARIO C: STANDARD SCORING SUBSECTION

### TRIGGER: Data Point USED in Scoring Formula

**LOCATION:** Nested Subsection (e.g., `2_1_resolution`).

**ACTION:** GENERATE Object with `components` and `scores`.

### SUB-ALGORITHM: COMPONENTS

**INPUT:** List of parameters required by formula.

**LOGIC:** For each parameter:
-   **IF** Raw Data -> GENERATE Type A (Scenario B).
-   **IF** Referenced Data -> GENERATE Type B (Scenario D).
-   **IF** Hardware Derived -> GENERATE Type C (Scenario E).

### SUB-ALGORITHM: SCORES

**INPUT:** Formula Result (`predicted`), Benchmark Data (`final`).

**LOGIC:**
-   `predicted`: = RESULT(Formula).
-   `final.value`:
    -   **IF** Reference Exists -> = Reference Value.
    -   **ELSE IF** Neighbor Exists -> = Neighbor Value.
    -   **ELSE** -> = `predicted` * `booster.multiplier`.

**SCHEMA:**

```json
"scores": {
  "predicted": <FLOAT>,
  "final": {
    "value": <FLOAT>,
    "method_used": <ENUM["Predictor", "Benchmark (Source)", "Neighbor Interpolation"]>,
    "booster": <STRING_OR_ENUM["No"]>,
    "confidence": <ENUM["High", "Medium", "Low", "N/A"]>
  }
}
```

**CONSTRAINTS:**
-   **IF** `method_used` != "Predictor" **THEN** `booster` **MUST BE** "No".
-   **IF** `booster` != "No" **THEN** `final.value` **MUST** == `predicted` * `booster_multiplier`.

---

## 5. SCENARIO D: SHARED DATA (REFERENCING)

### TRIGGER: Parameter exists in another section

**ACTION:** GENERATE Type B Object.

**SCHEMA:**

```json
"<key_name>": {
  "value": "<ABSOLUTE_PATH_TO_SOURCE>" // e.g. "2_1_panel.diagonal"
}
```

---

## 6. SCENARIO E: HARDWARE REFERENCE (X.Y.0)

### TRIGGER: Identification of Shared Component (SoC, Sensor)

**ACTION 1:** GENERATE Reference Table `X_Y_0_<name>_reference` BEFORE subsection.

**ACTION 2:** GENERATE Type C Object INSIDE subsection.

### SCHEMA (Table):

```json
"<id_key>": {
  "count": <INT>,
  "source": "<URL>",
  "exact_extract": "<TEXT>"
}
```

### SCHEMA (Type C Usage):

```json
"<parameter_name>": {
  "value": <DERIVED_SCORE>,
  "reference": "<TABLE_NAME>.<ID_KEY>",
  "description": "<EXPLANATION>"
}
```

---

## 7. SCENARIO F: BOOSTERS (SECTION 11)

### TRIGGER: Real-world anomaly requiring score adjustment

**ACTION 1:** GENERATE Entry in `11_reviews_and_performance_boosters`.

**ACTION 2:** REFERENCE in Subsection `scores.final.booster`.

### SCHEMA (Booster Def):

```json
"11_<X>_<name>": {
  "source_link": "<URL>",
  "impacted_subsection": "<X_Y_SUBSECTION>",
  "booster": <FLOAT != 1.0>,
  "justification": {
    "unaccounted_feature": "<VERBATIM_TEXT>",
    "unaccounted_reason": "<TEXT>",
    "observed_justification": "<VERBATIM_TEXT>"
  }
}
```
