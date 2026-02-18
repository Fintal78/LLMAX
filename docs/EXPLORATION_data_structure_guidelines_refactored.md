# Data Structure Guidelines (Scenario-Based)

## Purpose / Core Principles
This document defines the strict rules for the JSON structure, organized by **Data Scenario**. Follow the scenario that matches your data type to ensure compliance.

### The 7 Core Principles
1.  **Single Source of Truth:** Every raw data point exists in exactly one place.
2.  **Traceability:** Every value must have a clear origin (External Source or Internal Reference).
3.  **Neutrality:** All external data must include a verbatim extract as proof.
4.  **Strict Field Compliance:** All fields listed for a Type are **mandatory**.
5.  **No Formulas in JSON:** Calculation logic resides in scoring documentation only.
6.  **Valid and Accessible URLs:** All `source` links must be verified.
7.  **Searchable Exact Extracts:** extracts must be verbatim (Ctrl+F).

---

## Scenario A: File Header (Meta & Identity)
**Use Case:** Setting up a new device file.
**Rule:** Every file MUST start with these two objects to ensure traceability and uniqueness.

### 1. Meta Object
Tracks schema version and update date.
```json
"meta": {
  "schema_version": "5.1",
  "last_updated": "YYYY-MM-DD"
}
```

### 2. Identity Object
Strictly identifies the device.
```json
"identity": {
  "id": { "value": "normalized_id", "source": "...", "exact_extract": "..." },
  "brand": { "value": "Brand", "source": "...", "exact_extract": "..." },
  "model_name": { "value": "Name", "source": "...", "exact_extract": "..." },
  "model_aliases": { "value": ["Alias1"], "source": "...", "exact_extract": "..." },
  "release_date": { "value": "YYYY-MM-DD", "source": "...", "exact_extract": "..." }
}
```

---

## Scenario B: Simple Descriptive Data (Non-Scoring)
**Use Case:** Raw data that is **NOT** used in any scoring formula (e.g., `aspect_ratio`, `sim_slot_type`).
**Placement:** Root of the parent Section.
**Format:** **Type A (Raw External Data)**.

### Type A Definition
| Field | Description |
| :--- | :--- |
| `value` | The actual data (number, string, array, boolean). |
| `source` | Valid URL to the specific page. |
| `exact_extract` | Verbatim text from the page. |

### Example
```json
"2_display": {
  "aspect_ratio": {
    "value": "19.5:9",
    "source": "https://www.gsmarena.com/...",
    "exact_extract": "19.5:9 ratio"
  }
}
```

---

## Scenario C: Standard Scoring Data (The Subsection)
**Use Case:** Data that **IS** used to calculate a score (e.g., `resolution`, `battery_capacity`).
**Placement:** Inside a **Subsection** (e.g., `2_1_resolution`).
**Structure:** Must follow the **Components + Scores** pattern.

### 1. Components (Input)
Break down the data into **Types A** (Raw) or **Type B** (Reference). **Visibility is Key:** Never use opaque objects; every formula input must be visible.

### 2. Scores (Output)
The calculated result.
-   **predicted**: Result of the formula.
-   **final**: Definitive score for ranking (Method: Predictor, Benchmark, or Neighbor).
-   **booster**: "No" (unless Scenario F applies).

### Example
```json
"2_2_resolution_density": {
  // 1. COMPONENTS
  "resolution_width": {
    "value": 1440,
    "source": "...",
    "exact_extract": "..."
  },
  "resolution_height": {
    "value": 3120,
    "source": "...",
    "exact_extract": "..."
  },
  
  // 2. SCORES
  "scores": {
    "predicted": 8.5,              // Score from formula
    "final": {
      "value": 8.925,              // Definitive score for ranking
      "method_used": "Predictor",  // Method used
      "booster": "11.1",           // Section reference or "No"
      "confidence": "N/A"          // Confidence level
    }
  }
}
```

### 3. The Scoring Mechanism
These rules define how the `scores` object is calculated.

#### A. Predicted vs Final
- **predicted**: The result of the formula defined in `scoring_rules.md`.
- **final**: The definitive score used for ranking.

#### B. Allowable Methods (`method_used`)
1.  `"Predictor"`: Theoretical score based on rules. Can be boosted.
2.  `"Benchmark (Source)"`: Direct real-world test (e.g. "Benchmark (DXOMARK)"). **NO BOOSTERS**.
3.  `"Neighbor Interpolation"`: Derived from similar devices. **NO BOOSTERS**.

#### C. Booster Application (`booster`)
-   `"No"`: No booster applied.
-   `"Section #"`: Single booster (e.g., `"11.1"`).
-   `"Section # + Section #"`: Multiple boosters.
-   **Consistency Rule:** `final.value = predicted × booster_11.1 × ...`

#### D. Confidence Levels (`confidence`)
-   **High:** 2 consistent benchmarks, low variance.
-   **Medium:** 2 benchmarks, moderate variance.
-   **Low:** 2 benchmarks, high variance.
-   **N/A:** Predictor, Neighbor, or Single Benchmark.

---

## Scenario D: Shared Data (Referencing)
**Use Case:** A data point is measured in Section X but also needed for a formula in Section Y (e.g., `screen_size` needed for PPI).
**Rule:** Define it once (where it belongs), reference it elsewhere.

### 1. Primary Definition (Source)
Define as **Type A** in its logical home (e.g., `2_1_panel.diagonal_inches`).

### 2. Secondary Reference (Destination)
Use **Type B (Internal Reference)** in the other section.

### Type B Definition
| Field | Description |
| :--- | :--- |
| `value` | Absolute path: `"Section_Subsection.parameter"` |

### Example
```json
"2_2_resolution_density": {
  "screen_size_ref": {
    "value": "2_1_panel_architecture.diagonal_inches"
  }
}
```

---

## Scenario E: Hardware/Architecture (The Reference Table)
**Use Case:** Hardware components shared by many devices (SoC, GPU, Sensors) where scoring depends on the *identity* of the part.
**Structure:** Two steps.

### Step 1: The Reference Table (X.Y.0)
Place a table **immediately before** the subsection. It maps the **Identifier** to its proof.
-   **Key**: Unique ID (e.g., `snapdragon_8_gen_3`).
-   **Fields**: `<identifier_key>`, `count`, `source`, `exact_extract`.

### Step 2: The Architectural Mapping (Type C)
Inside the scoring subsection, reference the ID to derive a score/constant.

### Type C Definition
| Field | Description |
| :--- | :--- |
| `value` | The derived score/constant. |
| `reference` | Path to the X.Y.0 table key. |
| `description` | Explanation of the derived value. |

### Example
```json
// STEP 1: REFERENCE TABLE
"3_1_0_soc_reference": {
  "snapdragon_8_gen_3": {
    "count": 1,
    "source": "URL",
    "exact_extract": "Text"
  }
},

// STEP 2: SCORING SUBSECTION
"3_1_performance": {
  "soc_score": {
    "value": 156,
    "reference": "3_1_0_soc_reference.snapdragon_8_gen_3",
    "description": "Standard Benchmark Score for SD8 Gen 3"
  }
}
```

---

## Scenario F: Expert Review Adjustment (Boosters)
**Use Case:** An expert review reveals performance that contradicts the specs (e.g., bad software optimization despite good hardware).
**Rule:** Apply a **Booster** from Section 11 to the **Standard Scoring Subsection (Scenario C)**.

### Step 1: Define Booster (Section 11)
Create an entry in `11_reviews_and_performance_boosters`.
-   **source_link**: Link to review.
-   **booster**: Multiplier (e.g., 0.9 or 1.1).
-   **justification**: Verbatim "Unaccounted Feature" + "Observed Evidence".

### Step 2: Apply in Subsection
Update the `scores.final` object in the target subsection.
-   **booster**: Reference the Section 11 ID (e.g., `"11.1"`).
-   **value**: `predicted * booster`.

### Example
**Section 11:**
```json
"11_1_camera_lag": {
  "booster": 0.9,
  "impacted_subsection": "4_1_camera",
  "justification": { ... }
}
```

**Section 4.1:**
```json
"scores": {
  "predicted": 8.0,
  "final": {
    "value": 7.2,  // 8.0 * 0.9
    "method_used": "Predictor",
    "booster": "11.1"
  }
}
```
