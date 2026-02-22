# Data Structure Guidelines

## Purpose
This document establishes **strict, methodic rules** for the JSON structure in `proposed_data_structure.md`.  
**Goal:** Zero duplication, full traceability, and complete alignment with `scoring_rules.md`.

---

## 0. Meta & Identity (File Header)

**Purpose:** These fields are placed at the beginning of every JSON file to ensure **traceability**, **uniqueness**, and **version control**.

**Justification:**
- **Traceability:** The `meta` object tracks when the data was last updated and which schema version it follows, enabling change tracking and data integrity verification.
- **Uniqueness:** The `identity` object provides unambiguous device identification, preventing confusion between similar models (e.g., regional variants, carrier-specific versions).
- **Temporal Context:** The `release_date` disambiguates devices that share the same commercial name across generations (e.g., Galaxy S21 2021 vs. a potential future reuse) and provides context for interpreting specs relative to the technology available at launch.

### Meta Object (`meta`)
Metadata describing the file version and integrity.

**Schema:**
```json
"meta": {
  "schema_version": "5.1",
  "last_updated": "YYYY-MM-DD"
}
```

### Identity Object (`identity`)
Strict identification of the device to prevent ambiguity.

**Schema:**
```json
"identity": {
  "id": { 
    "value": "normalized_id", 
    "source": "...", 
    "exact_extract": "..." 
  },
  "brand": { 
    "value": "Brand Name", 
    "source": "...", 
    "exact_extract": "..." 
  },
  "model_name": { 
    "value": "Commercial Name", 
    "source": "...", 
    "exact_extract": "..." 
  },
  "model_aliases": { 
    "value": ["Alias 1", "Alias 2"], 
    "source": "...", 
    "exact_extract": "..." 
  },
  "release_date": { 
    "value": "YYYY-MM-DD", 
    "source": "...", 
    "exact_extract": "..." 
  }
}
```

---

## 1. Overview & Core Principles

### 1.1 Core Principles

1.  **Single Source of Truth:** Every raw data point exists in exactly one place.
2.  **Traceability:** Every value must have a clear origin (External Source or Internal Reference).
3.  **Neutrality:** All external data must include a verbatim extract as proof.
4.  **Strict Field Compliance:** All fields listed for each Type are **mandatory**. No fields may be omitted or added.
5.  **No Formulas in JSON:** All calculation logic resides strictly in scoring documentation.
6.  **Valid and Accessible URLs:** All `source` links must be verified to work before committing data.
7.  **Searchable Exact Extracts:** The `exact_extract` must be found verbatim (Ctrl+F) on the source page.

---

### 1.2 The Two-Layer Architecture

This database is built on a two-layer architecture:
1.  **Part A:** The Standard Scoring Sections (1–10)
2.  **Part B:** The Adjustment Layer (Section 11 - Boosters)

### Part A: The Standard Scoring Sections (1–10)
This hierarchy defines how the device is scored on its technical merits before any expert review adjustments.

#### 1. Sections (Root Level)
**Sections 1 to 10** → Represent major functional categories (e.g., `2_display`, `5_battery_and_charging`).
- Align with `scoring_rules.md` chapters.
- Contain either **non-scoring raw data** (placed at section root per Rule 1) or **Subsections** (scoring units).

#### 2. Reference Tables (X.Y.0)
**Definition:** Tables used solely to identify hardware components (e.g., `3_1_0_soc_reference`) so they can be referenced by multiple scoring subsections.
**Naming Convention:** Must be numbered as `X_Y_0` (where `X_Y` is the subsection that uses it) and placed immediately before `X_Y` in the structure.
**Core Rule:** These tables must contain **ONLY identifiers** (the "What"). All technical data (frequencies, scores) must reside in the relevant scoring subsection (the "How").

**Fields:**
-   **`<identifier_key>`**: Unique ID for the hardware component (e.g., `snapdragon_8_gen_3`) used for referencing in other subsections.
-   **`count`**: Number of instances of this component (e.g., number of cores).
-   **`source`**: URL proof of existence from a trusted source.
-   **`exact_extract`**: Verbatim text verifying the component's identity.

**Schema:**
```json
"3_1_0_soc_reference": {
  "snapdragon_8_gen_3": {
    "count": 1,              // Number of instances
    "source": "URL",         // Proof of existence
    "exact_extract": "Text"  // Verification extract
  },
  "cortex_x4": {
    "count": 1,
    "source": "URL",
    "exact_extract": "Text"
  },
  "cortex_a720": {
    "count": 5,
    "source": "URL",
    "exact_extract": "Text"
  },
  "cortex_a520": {
    "count": 2,
    "source": "URL",
    "exact_extract": "Text"
  }
}
```

#### 3. Subsections (X.Y)
The atomic units of evaluation (e.g., `2_1_panel_architecture`).

**Structure Rule:** Every scoring subsection **MUST** follow this exact schema:

**A. Components (Recursive Input Data)**
All scoring parameters must be broken down into components (`component_1` ... `component_n`) which can be broken down further into sub-components until a **Type A** (Raw External) or **Type B** (Internal Reference) leaf node is reached. 
-   **Visibility:** **NEVER** use opaque aggregate objects; every input to the formula must be visible.
-   **Typing:** Leaf nodes must strictly adhere to the defined Types (Value + Source + Extract).

**B. Scores (Output)**
The calculated result of the subsection's formula.
The following rules define how the `scores` object is calculated.

- **predicted**: The result of the formula defined in `scoring_rules.md`.
- **final**: The definitive score used for ranking. It is derived via one of four paths:
    1.  **Direct Benchmark:** Value from a trusted source (e.g., DXOMARK).
    2.  **Neighbor Interpolation:** Calculated from similar devices (see `scoring_rules.md` Section 5.1).
    3.  **Predictor + Booster:** The `predicted` score adjusted by one or more Section 11 Boosters.
    4.  **Predictor (Default):** The `predicted` score used as-is when no benchmark, neighbor, or booster applies.

**Allowable Methods (`method_used`):**
1.  `"Predictor"`: Theoretical score based on rules. Can be boosted.
2.  `"Benchmark (Source)"`: Direct real-world test (e.g. "Benchmark (DXOMARK)"). **NO BOOSTERS**.
3.  `"Neighbor Interpolation"`: Derived from similar devices. **NO BOOSTERS**.

**Booster Field (`booster`):**
Defines which Section 11 adjustment(s) are applied to the `predicted` score.
-   `"No"`: No booster applied.
-   `"Section #"`: Single booster (e.g., `"11.1"`).
-   `"Section # + Section #"`: Multiple boosters (e.g., `"11.1 + 11.2"`).

**Consistency Rule:** When a subsection references multiple boosters, all their multipliers are applied in sequence: `scores.final.value = predicted × booster_11.1 × booster_11.2 × ...`

**Confidence Levels (`confidence`):**
-   **High:** Verified by 2 consistent benchmarks with low variance.
-   **Medium:** Verified by 2 benchmarks with moderate variance.
-   **Low:** Verified by 2 benchmarks with high variance.
-   **N/A:** Predictor, Neighbor Interpolation, or Single Benchmark source.

**Schema:**
```json
"subsection_name": {
  "component_1": { ... }, // Input data decomposed recursively
  ...
  "component_n": { ... },
  "scores": {
      "predicted": 8.5,              // Score from formula in scoring_rules.md
    "final": {
      "value": 8.925,              // Definitive score for ranking
      "method_used": "Predictor",  // Method used to derive final value: Predictor | Benchmark (Source) | Neighbor Interpolation
      "booster": "11.1",           // Section reference or "No"
      "confidence": "N/A"          // Confidence level, N/A for Predictor; High/Medium/Low for 2 Benchmarks
    }
  }
}
```

---

### Part B: The Adjustment Layer (Section 11)
**Section 11 (Boosters)** captures **real-world performance anomalies** not reflected in specs — validated by an expert review. This layer sits *on top* of Part A to adjust the "Predictor" scores.

**Constraint:** Boosters are applied **ONLY** to Predictor scores and are **FORBIDDEN** for Benchmark or Neighbor Interpolation methods, as those already reflect real-world performance.

#### Booster Definition Schema

Each booster is a standalone entry in the `11_reviews_and_performance_boosters` section. It provides the full evidence trail for the multiplier referenced in the subsection's `scores.final.booster` field.

**Schema:**
```json
"11_X_booster_name": {
  "source_link": "URL",              // Full URL to the expert review
  "impacted_subsection": "X.Y",      // Subsection whose predicted_score is multiplied
  "booster": 1.05,                   // Multiplier applied to predicted_score (see Consistency Rule below)
  "justification": {
    "unaccounted_feature": "...",    // Verbatim quote: the real-world quality the spec misses
    "unaccounted_reason": "...",     // Why the scoring formula cannot capture it
    "observed_justification": "..."  // Verbatim quote: real-world evidence from the review
  }
}

```

### 1.3 Component Structure Guidelines (Transition)
The following sections (2 and 3) detail how to structure the components within each section or subsection. They define **WHERE** to place data (Section 2) and **WHAT** strict format that data must follow (Section 3) to ensure the scoring mechanism described above functions correctly.

---

## 2. Placement Rules (The "Where")

### Rule 1: Non-Scoring Data → Section Root
*   **Condition:** Raw data NOT used for any scoring formula.
*   **Action:** Place at the root of the parent section.
*   **Example:** `2_display.aspect_ratio`

### Rule 2: Single-Use Scoring Data → Subsection Components
*   **Condition:** Raw data used for scoring in **only one** subsection.
*   **Action:** Place inside the subsection as a component.
*   **Example:** `2_2_resolution_density.ppi`

### Rule 3: Multi-Use Scoring Data → Primary Component + References
*   **Condition:** Raw data used in **multiple** subsections.
*   **Action:**
    1.  **Primary:** Store raw data in the subsection where it is most directly measured.
    2.  **Secondary:** Reference it in other subsections using **Type B**.
*   **Example:** `screen_size` in `2_1`, referenced in `2_2`.

### Rule 4: Architectural Identifiers → X.X.0 Tables (Exception)
*   **Condition:** Hardware identifiers shared by multiple devices (e.g., SoC Model, GPU Model).
*   **Action:**
    1.  **X.X.0 Table:** Store **only** the identifier.
    2.  **Scoring Subsection:** Store derived scores using **Type C** (Architectural Mapping).

---

## 3. Field Structure Definitions (The "What")

Every field must fall into one of these strict categories. **Formulas are forbidden.**

### Type A: Raw External Data
**Definition:** Hard facts scraped or extracted from an external source.

| Field           | Description                                                                                |
| :-------------- | :----------------------------------------------------------------------------------------- |
| `value`         | The actual number, string, boolean, or **array** of these.                                 |
| `source`        | **MUST be a valid, accessible URL** to the exact page containing the data.                 |
| `exact_extract` | **MUST be verbatim text** found exactly as-is on the source page (searchable with Ctrl+F). |

**Example:**
```json
"screen_size_inches": {
  "value": 6.8,
  "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
  "exact_extract": "6.8 inches"
}
```

### Type B: Internal Reference
**Definition:** A pointer to a value stored elsewhere (Rule 3).
**Usage:** When a formula needs a parameter defined in another subsection.

| Field   | Description                                                                                        |
| :------ | :------------------------------------------------------------------------------------------------- |
| `value` | The absolute path to the data: `"Section_Subsection.parameter"`. |

**Example:**
```json
"screen_size_ref": {
  "value": "2_1_panel_architecture.diagonal_inches"
}
```

### Type C: Architectural Mapping
**Definition:** A derived constant or score determined by a hardware identifier (Rule 4).
**Usage:** GPU Scores, Reference Frequencies.

| Field         | Description                                                                                     |
| :------------ | :---------------------------------------------------------------------------------------------- |
| `value`       | The score or constant associated with the hardware.                                             |
| `reference`   | Path to the Identifier in the X.X.0 table.                                                      |
| `description` | **MUST** identify the specific column/parameter in the table (e.g., "Standard Graphics Score"). |

**Example:**
```json
"gas": {
  "value": 10,
  "reference": "3_3_0_gpu_architecture_reference.gpu_model",
  "description": "Standard Graphics Score (SGS) column for Adreno 750"
}
```

---

## 4. Validation Checklist

1.  [ ] **Structure Check:** Does every subsection operate on the strict `scores` nested object?
2.  [ ] **Decomposition Check:** Are all parameters broken down to **Type A** or **Type B** leaves?
3.  [ ] **Booster Check:** Are boosters applied **ONLY** to usage of the "Predictor" method?
4.  [ ] **Confidence Check:** Is "High/Medium/Low" used **ONLY** when 2 benchmark sources exist?
5.  [ ] **Raw Data Check:** Is every external data point **Type A** (Source + Extract)?


