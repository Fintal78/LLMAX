# Data Structure Guidelines

## Purpose
This document establishes **strict, methodic rules** for the JSON structure in `proposed_data_structure.md`.  
**Goal:** Full traceability and complete alignment with `scoring_rules.md`.

---

## 0. Meta & Identity (File Header)

**Purpose:** These fields are placed at the beginning of every JSON file to ensure **traceability**, **uniqueness**, and **version control**.

**Justification:**
- **Traceability:** The `meta` object tracks when the data was last updated and which schema version it follows, enabling change tracking and data integrity verification.
- **Uniqueness:** The `identity` object provides unambiguous device identification. Importantly, the `hardware_configuration` object explicitly defines which RAM, Storage, and Chipset combination is being scored. This isolates the specific hardware variant under review, preventing data cross-contamination (e.g., mistakenly pairing a Snapdragon chip's benchmarks with an Exynos variant's battery life, or confusing a base model's RAM with its Pro counterpart).
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
  "hardware_configuration": {
    "storage_gb": {
      "value": 256, // Storage in Gigabytes (GB)
      "source": "...",
      "exact_extract": "..."
    },
    "ram_gb": {
      "value": 12, // Random Access Memory (RAM) in Gigabytes (GB)
      "source": "...",
      "exact_extract": "..."
    },
    "chipset": {
      "value": "Snapdragon 8 Gen 3", // System-on-Chip (SoC) name
      "source": "...",
      "exact_extract": "..."
    }
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

1.  **Traceability:** Every value must have a clear origin (External Source or Internal Reference).
2.  **Neutrality:** All external data must include a verbatim extract as proof.
3.  **Strict Field Compliance:** All fields listed for each Type are **mandatory**. No fields may be omitted or added unless explicitly allowed otherwise.
4.  **Valid and Accessible URLs:** All `source` links must be verified to work before committing data. **🚨 ZERO TOLERANCE: Providing broken, dead, or hallucinated URLs is strictly forbidden and breaks the entire architectural chain. ALWAYS VERIFY!**
5.  **Searchable Exact Extracts:** The `exact_extract` must be found verbatim (Ctrl+F) on the source page.

---

### 1.2 Data Verification & URL Integrity Pipeline
To eliminate URL hallucinations or broken validation chains downstream, the following procedural loop is **mandatory** before any data is committed:

> [!CAUTION]
> ### 🚨 MANDATORY SCRIPT VERIFICATION (THE PYTHON BARRIER) 🚨
> AI models cannot self-police URL validity; they predict strings. 
> **You MUST physically run `python src/verify_urls.py <target_file>` over your Markdown or JSON file before committing it or declaring a task complete.** 
> The script acts as a strict compliance crawler. For primary source pairs, it downloads the HTML and guarantees the exact extract substring physically exists on the page. For inline context URLs, it verifies the link is not a 404 dead link or a silent redirect. 
> If the script triggers a `[X] REJECTED` failure on any URL or extract, the data is instantly invalid. Do not skip this step under any circumstances.

1.  **De-Obfuscation:** If a search API returns an obfuscated or redirected link, you MUST resolve it to its final physical destination URL before use. The verification script will strictly reject "soft 404" silent redirects.
2.  **Scrapability Check:** If a target server aggressively blocks automated scraping, that URL **CANNOT** be used as a primary "exact extract" data source. However, inline context links that return an anti-bot `403 Forbidden` or `429 Too Many Requests` are permitted as long as they do not return a dead `404 Not Found`.
3.  **Temporary Link Storage & Final Review:** During data gathering, all prospective links must be compiled into a temporary list. Before final task completion, this entire list must be batch-rechecked to ensure no hallucinated or dead URLs slipped into the final JSON output.

---

### 1.3 The Two-Layer Architecture

This database is built on a two-layer architecture:
1.  **Part A:** The Standard Scoring Sections (1–10)
2.  **Part B:** The Adjustment Layer (Section 11 - Boosters)

### Part A: The Standard Scoring Sections (1–10)
This hierarchy defines how the device is scored on its technical merits before any expert review adjustments.

#### 1. Sections (Root Level)
**Sections 1 to 10** → Represent major functional categories (e.g., `2_display`, `8_battery_and_charging`).
- Align with `scoring_rules.md` chapters.
- Contain either **non-scoring raw data** (placed at section root per Rule 1 of Chapter 2. Placement Rules) or **Subsections** (scoring units, more details below).

#### 2. Reference Tables (X.Y.0)
**Definition:** Tables used solely to identify hardware components (e.g., `6_1_0_soc_reference`) so they can be referenced by multiple scoring subsections.
**Naming Convention:** Must be numbered as `X_Y_0` (where `X_Y` is the subsection that uses it) and placed immediately before `X_Y` in the structure.
**Core Rule:** These tables must contain **ONLY identifiers** (the "What"). All technical data (frequencies, scores) must reside in the relevant scoring subsection (the "How").

**Fields:**
-   **`<identifier_key>`**: Unique ID for the hardware component (e.g., `snapdragon_8_gen_3`) used for referencing in other subsections.
-   **`count`**: Number of instances of this component (e.g., number of cores).
-   **`source`**: URL proof of existence from a trusted source.
-   **`exact_extract`**: Verbatim text verifying the component's identity.

**Schema:**
```json
"6_1_0_soc_reference": {
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
All scoring parameters must be broken down into specific identifier components (e.g., `core_sensor_suite`) which can be broken down further into sub-components until a **Type A** (Raw External) or **Type B** (Internal Reference) leaf node is reached (e.g., `accelerometer`, `gyroscope`, ...). 
-   **No Generic Names:** Never use abstract names like `component_1`. Always use the concrete, descriptive identifier of the spec.
-   **No Abbreviations:** All parameters to be stored must be explicit, never use abbreviations. For example do not use `pcs` but `professional_codec_support`.
-   **Visibility:** **NEVER** use opaque aggregate objects; every input to the formula must be visible.
-   **Typing:** Leaf nodes must strictly adhere to the defined Types (Value + Source + Extract).

**B. Scores (Output)**
**Important Note on Formulas:**
There is no need to repeat the source name "`scoring_rules.md`" in every inline comment. The entire data structure operates under the assumption that all formulas, tables, and rules referenced as "Section X.X" or "§X.X" are found in `scoring_rules.md`.

The calculated result of the subsection's formula.
The following rules define how the `scores` object is calculated, **bridging the technical inputs to the final ranking.**

- **predicted**: The mathematical result of the specific formula defined in `scoring_rules.md` for this subsection. This is typically the sum, weighted average, or lookup value derived from the individual `subscore` properties of the components defined below.
- **final**: The definitive score used for ranking. It is derived via one of four paths:
    1.  **Direct Benchmark:** Value from a trusted third-party test (e.g., DXOMARK). **Note:** If a direct benchmark is available, it completely overrides the `predicted` score's formula, as it represents real-world measured performance rather than theoretical specs.
    2.  **Neighbor Interpolation:** Calculated from similar devices (see `scoring_rules.md` Section 8.1).
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
- **Clamping Rule:** The final result of any booster-calculated score MUST be clamped at its boundaries: **minimum 0.0 and maximum 10.0**. A booster can never push a score beyond the normalized range for ranking.

**Confidence Levels (`confidence`):**
-   **High:** Verified by 2 consistent benchmarks with low variance.
-   **Medium:** Verified by 2 benchmarks with moderate variance.
-   **Low:** Verified by 2 benchmarks with high variance.
-   **N/A:** Predictor, Neighbor Interpolation, or Single Benchmark source.

**Schema:**
```json
"7_6_sensors": {
  "core_sensor_suite": {
    "accelerometer": {
      "value": true,
      "source": "https://www.phonearena.com/phones/Samsung-Galaxy-S24-Ultra_id12115",
      "exact_extract": "Sensors [...] Accelerometer",
      "subscore": 1.0
    },
    "gyroscope": {
      "value": true,
      "source": "https://www.phonearena.com/phones/Samsung-Galaxy-S24-Ultra_id12115",
      "exact_extract": "Sensors [...] Gyroscope",
      "subscore": 1.5
    },
    "magnetometer": {
      "value": true,
      "source": "https://www.phonearena.com/phones/Samsung-Galaxy-S24-Ultra_id12115",
      "exact_extract": "Sensors [...] Compass",
      "subscore": 1.0
    },
    "proximity_sensor": {
      "value": true,
      "source": "https://www.phonearena.com/phones/Samsung-Galaxy-S24-Ultra_id12115",
      "exact_extract": "Sensors [...] Proximity sensor",
      "subscore": 0.75
    },
    "ambient_light_sensor": {
      "value": true,
      "source": "https://www.phonearena.com/phones/Samsung-Galaxy-S24-Ultra_id12115",
      "exact_extract": "Sensors [...] Ambient light sensor",
      "subscore": 0.75
    }
  },
  "advanced_sensor_capabilities": {
    "barometer": {
      "value": true,
      "source": "https://www.phonearena.com/phones/Samsung-Galaxy-S24-Ultra_id12115",
      "exact_extract": "Sensors [...] Barometer",
      "subscore": 1.5
    },
    "lidar_tof_3d_depth_sensor": {
      "value": false,
      "source": "N/A",
      "exact_extract": "N/A",
      "subscore": 0.0
    },
    "color_spectrum_flicker_sensor": {
      "value": false,
      "source": "N/A",
      "exact_extract": "N/A",
      "subscore": 0.0
    }
  },
  "scores": {
    "predicted": 6.5,              // sum of all subscores
    "final": {
      "value": 6.83,               // Definitive score (Predicted x Booster multiplier of 1.05)
      "method_used": "Predictor",  // Method used to derive final value: Predictor | Benchmark (Source) | Neighbor Interpolation
      "booster": "11.5",           // Section reference to the booster, or "No"
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

Each booster is a standalone entry in the `11_reviews_and_performance_boosters` section. It provides the full evidence trail for the multiplier referenced in the subsection's `scores.final.booster` field. Section "11. Reviews & Performance Boosters" of `scoring_rules.md` describes precisely the logic and requirements regarding Booster sections.

**Schema Example:**

```json
"11_1_dxomark_24mp_texture_rendering": {
  "source_link": "https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/",
  "impacted_subsection": "4.16",
  "booster": 1.05,
  "justification": {
    "unaccounted_feature": "Other important updates compared to the previous generation iPhones include the jump from 12MP to 24MP images by default in most light conditions. In our tests, this made for significantly improved texture quality, especially in close-up portraits.",
    "unaccounted_reason": "Section 4.3 scores sensor resolution (48MP hardware), and Section 4.16 scores multi-frame processing presence (Always-on HDR + Night stacking). However, neither captures the quality impact of Apple's decision to bypass the industry standard and output 24MP images by default, which the review explicitly credits for improved texture preservation. Context: Modern smartphones group 4 small pixels together into 1 large pixel to capture more light (pixel binning), meaning even a 48MP camera normally outputs a 12MP image. Apple created unique software to simultaneously capture both a 12MP and 48MP image and merge them into a 24MP final image, yielding significantly higher detail without hardware changes (Source: https://www.apple.com/newsroom/2023/09/apple-unveils-iphone-15-pro-and-iphone-15-pro-max/).",
    "observed_justification": "The camera in Apple's new flagship device comes with an entirely new texture rendering management, and in our tests the results were outstanding. With most lighting conditions resulting in 24MP images, finest details were preserved much better than on most competitors. [...] The Apple iPhone 15 Pro Max provided very natural skin rendering with subtle local contrast and pleasant rendering of the finest details like hair, lips, wrinkles, etc."
  }
}
```

### 1.4 Component Input Directives (Transition)
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
*   **Justification:** Keeps the data contiguous with the formula that uses it for maximum readability.
*   **Example:** `2_2_resolution_density.ppi`

### Rule 3: Multi-Use Scoring Data → Primary Component + References
*   **Condition:** Raw data used in **multiple** subsections.
*   **Action:**
    1.  **Primary:** Store raw data in the subsection where it is most directly measured.
    2.  **Secondary:** Reference it in other subsections using **Type B**.
*   **Justification:** While raw values are duplicated across blocks for convenience, the **"Single Source of Truth"** is enforced via the mandatory path field in Type B references. This ensures full traceability to the primary data point and prevents administrative discrepancies by providing a clear map for systematic updates across all dependent subsections.
*   **Example:** Semiconductor node size is primarily extracted in `6_10_thermal_dissipation`, and referenced via Type B dependencies inside `8_1_battery_endurance` to calculate hardware efficiency.

### Rule 4: Architectural Identifiers → X.Y.0 Tables (Exception)
*   **Condition:** Hardware identifiers shared by multiple devices (e.g., SoC Model, GPU Model).
*   **Action:**
    1.  **X.Y.0 Table:** Store **only** the identifier.
    2.  **Scoring Subsection:** Store derived scores using **Type C** (Architectural Mapping).

---

## 3. Field Structure Definitions (The "What")

Every field must fall into one of these strict categories.

### Type A: Raw External Data
**Definition:** Hard facts scraped or extracted from an external source, paired with their evaluated mathematical constraint. The `value` field MUST be one of 5 strict data shapes: Continuous Numeric, Discrete Integer, Categorical String, String Array, or Pure Boolean. Artificial "logic" keys (e.g., `is_supported`) are strictly forbidden; the component key must be the name of the specification itself.

| Field           | Description                                                                                                         |
| :-------------- | :------------------------------------------------------------------------------------------------------------------ |
| `value`         | The raw hardware specification (must match one of the 5 allowed Data Shapes).                                       |
| `source`        | **MUST be a valid, accessible URL** to the exact page containing the data.                                          |
| `exact_extract` | **MUST be verbatim text** found exactly as-is on the source page.                                                   |
| `subscore`      | **[OPTIONAL]** The individual score mapped/calculated for this value. Omit if the parameter is not scored directly. |

**Example (Scored Value):**
```json
"bluetooth_version": {
  "value": 5.3,
  "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
  "exact_extract": "Comms [...] Bluetooth 5.3, A2DP, LE",
  "subscore": 4.5
}
```

**Example (Unscored Intermediate Input):**
```json
"resolution_width_px": {
  "value": 1440,
  "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
  "exact_extract": "DISPLAY [...] Resolution [...] 1440 x 3120 pixels, 19.5:9 ratio"
}
```
#### Data Extraction & Fallback Directives

**1. Syntax & Colocation Rules:**
*   **Full Context Path:** You must provide both the value AND the full hierarchical context/path (e.g., `"Memory [...] Internal [...] 8GB RAM"`, not just `"Internal 8GB"`) to completely distinguish its origin and placement.
*   **Single Value Targeting:** The extract should point ONLY towards the specific value it is referencing and nothing else. If there are other values in the same sentence or property (like a storage size next to a RAM size), they must be skipped or omitted using `[...]`.
*   **Disjointed Extracts:** Extracts may combine non-contiguous text from the same source to connect the key and the value using `[...]`.
*   **Colocation:** The elements joined by `[...]` must be logically coherent, clearly associated, and colocated within the same contextual block.
*   **Fluidity:** For optimal fluidity, parts separated by *less than 3 sentences* should NOT be separated by `[...]`.
*   **Complete Extraction Checklist:** When mapping a hardware component that contains multiple listed capabilities (like a comma-separated list of sensors or supported codecs), the extraction must be exhaustive across all items explicitly mentioned in the source that correspond to the scoring rules, regardless of the resulting size of the JSON object. Do not selectively omit items for brevity.

**2. The Omni-Scan Rule (Handling External Database Omissions):**
You cannot assume a primary source (like GSMArena) is perfectly exhaustive. Some sources silently drop universally standard components (like Ambient Light Sensors). To prevent penalizing phones due to a single database's omissions:
*   You MUST proactively scan at least **three distinct sources** (e.g., GSMArena, Official Specs, Wikipedia) to cross-reference the `scoring_rules.md` checklist.
*   If a feature is missing from the primary source but found on *any* verified secondary source, you MUST extract it and document it using that secondary source's URL and exact extract.


**3. The Explicit Default Rule (Schema Checklist):**
To prevent human or parser omission, every discrete scorable feature evaluated in `scoring_rules.md` for a given subsection MUST be present as a key in the JSON, even if the device does not possess it. 

*   **For Additive Components (e.g., Sensors, Additional Lenses):** 
    If the device lacks the component, you must explicitly declare it missing using `"value": false` and `"subscore": 0.0` to mathematically guarantee it was investigated:
    ```json
    "lidar_tof_3d_depth_sensor": {
      "value": false,
      "source": "N/A",
      "exact_extract": "N/A",
      "subscore": 0.0
    }
    ```
*   **For Hierarchical Categories (e.g., Wi-Fi, Audio Codecs, OS Version):**
    You do NOT list all the lower tiers as `false`. As per `scoring_rules.md`, these categories only score the *highest* supported tier. You extract and evaluate ONLY that single maximum tier:
    ```json
    "bluetooth_version": {
      "value": 5.3,
      "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
      "exact_extract": "Comms [...] Bluetooth 5.3, A2DP, LE",
      "subscore": 4.5
    }
    ```

### Type B: Internal Reference
**Definition:** A pointer to a value stored elsewhere (Rule 3).
**Usage:** When a formula needs a parameter defined in another subsection.

In this particular case the fields are optional to enable flexibility. Use only the fields that are needed. 
**Traceability Constraints:**
- When a value is re-used from an internal reference, `value_path` MUST be present for traceability reasons.
- Similarly, if a subscore is re-used from an internal source, `subscore_path` MUST be present for traceability reasons. 
- If the subscore from an internal source is not re-used and the subscore is directly calculated in the block, then obviously no path field (`subscore_path`) is needed.

| Field           | Description                                                                                    |
| :-------------- | :--------------------------------------------------------------------------------------------- |
| `value_path`    | Path to the source value: `"Section_Subsection.parameter.value"`.                              |
| `value`         | The literal parameter value extracted from `value_path`.                                       |
| `subscore_path` | Path to the subscore value: `"Section_Subsection.parameter.subscore"`.                         |
| `subscore`      | The literal parameter subscore extracted from `subscore_path`, if there is one, or calculated. |

**Example where the path `subscore_path` is not used:**
```json
"1_2_durability": {
      // GUIDELINE: `ingress_protection_rating` stores the full human-readable IP (Ingress Protection) composite string (e.g. "IP68") as declared by the manufacturer. It is not scored directly but the two individual digits extracted for scoring are `dust_protection_digit` and `water_protection_digit`, see below — always parse those from this `ingress_protection_rating.value` string.
      "ingress_protection_rating": {
        "value": "IP68",
        "source": "www.source.com",
        "exact_extract": "Proof_extract",
      },
      // SCORING GOAL: Scores dust and water resistance separately using the two digits of the IP (Ingress Protection) rating defined by IEC standard 60529.
      "dust_protection_digit": {
        "value_path": "1_2_durability.ingress_protection_rating.value",
        "value": "Digit 6",
        "subscore": 10.00
        // SCORING GUIDELINE: Look up the first digit of the IP rating in the Section 1.2.A table. Use the following terms exclusively for "value" with related scores:
        //   • Digit 6    → 10.00
        //   • Digit 5    → 8.00
        //   • Digit 4    → 6.00
        //   • Digit 3    → 4.00
        //   • Digit 2    → 2.00
        //   • Digit 0–1  → 0.00
      },
    },
```

### Type C: Architectural Mapping
**Definition:** A derived constant or score determined by a hardware identifier.
**Usage:** GPU Scores, Reference Frequencies.

| Field         | Description                                                                                     |
| :------------ | :---------------------------------------------------------------------------------------------- |
| `identifier`  | The identifier string matching the table record.                                                |
| `reference`   | Path to the Identifier in the X.Y.0 table.                                                      |
| `description` | **MUST** identify the specific column/parameter in the table (e.g., "Standard Graphics Score"). |
| `subscore`    | The score extracted from the reference table.                                                   |

**Example:**
```json
"graphics_architecture_score": {
  "identifier": "Adreno 750",
  "reference": "6_3_0_gpu_architecture_reference.gpu_model",
  "description": "Standard Graphics Score (SGS)",
  "subscore": 10.00
}
```

### Type D: Lookup Tables (Helper Blocks)
**Definition:** Static reference tables embedded in the JSON strictly to assist the scoring process. They are NOT scored themselves.
**Usage:** When a data point requires matching a marketing name or technical specification against a predefined list of tiers to determine the correct canonical name and score.

> [!WARNING]
> ### 🚨 STRICT LIMITATION ON LOOKUP TABLES 🚨
> Do **NOT** use lookup tables (Type D) unless absolutely necessary. 
> 
> **Rationale:** JSON lookup tables were designed for rigid regex parsing. For AI agents (LLMs), reading massive JSON arrays of keywords is highly inefficient and creates significant bloat. LLMs possess semantic understanding and can interpret direct inline guidelines much more effectively. Creating a 100-line lookup table wastes thousands of tokens per device evaluation and increases the risk of "pointer logic" errors.
> 
> **Best Practice:** Instead of a `_lookup` block, write a concise inline `SCORING GUIDELINE` comment directly within the relevant subscore node. Simply state the tier name, the required keyword context, and the score. Only use a lookup table if the mapping logic is so vast or non-semantic that an inline comment becomes unreadable.

**Standardized Format (Only if strictly required):**
All lookup tables MUST be suffixed with `_lookup` (e.g., `gpu_model_lookup`) and follow this structure:
```json
"example_lookup": { // this is a lookup table, do not score here
  "tier_key": {
    "tier_name": "String to be copied to the target 'value' field.",
    "score": 10.00, // Or "N/A" / descriptive string if not directly scored
    "verification_rule": "Detailed, exhaustive explanation of what the scorer should look for in specs or reviews to select this tier. Abbreviations MUST be written in full words the FIRST time they are used in a data block (e.g., 'Liquid-Crystal Display' alongside 'LCD').",
    "recognized_keywords": ["keyword 1", "keyword 2"] // [OPTIONAL] Specific terms to match against
  }
}
```

### Type E: Benchmarks
Data structures for benchmark-derived scores follow specialized formats different from standard Predictor properties.

**Example Structure:** See `"2_11_display_benchmark_final_scoring"` in `proposed_data_structure.md` for the canonical benchmark format.

---

## 4. Inline JSON Documentation Rules (The Recipe)

To ensure the JSON data structure is entirely self-contained, every scoring subsection within `proposed_data_structure.md` **MUST** include explicit explanatory comments (`//`) directly injected into the JSON. A user or script must be able to fill out the subsection perfectly using only these comments, without ever needing to open `scoring_rules.md`.

Every subsection must contain the following "recipe":
1.  **Subsection Goal:** An explanation at the very top of the subsection block detailing what the scoring goal is.
2.  **Subscore Extraction:** For every `subscore` field included in the structure (noting it is optional for raw data), provide an explicit explanation of how it is derived, including the formula and its specific references from `scoring_rules.md` (or the exact conditions under which it evaluates to `"N/A"`).
3.  **Predicted Score Logic:** For each `predicted_score` field, provide a clear explanation (including the mathematical formula) of how it is derived from the subscores above it.
4.  **Final Score Compliance:** The `final_score` object MUST strictly adhere to the `FINAL_SCORE_PREDICTOR_TEMPLATE` defined in the `proposed_data_structure.md` header. To ensure cleanliness and avoid duplication, do NOT add internal comments or per-field scoring guidelines within these blocks; the global template governs their logic (Booster application, clamping, etc.).
    *   **Exception (Hybrid Methods):** Subsections that use multiple scoring methods (e.g., Section 2.11 with Methods A/B/C) MUST include internal comments in the `final_score` object to document which method was selected and why.
5.  **LLM Semantic Matching & Robust Aliasing:** When parsing spec sheets, the AI agent will use natural language semantic matching to identify the appropriate tier.
    *   **Keyword Definition Standard:** Strings inside `recognized_keywords` arrays should be properly capitalized and human-readable (e.g., use `"Gorilla Glass Victus 2"`, `"Ceramic Shield"`). Do not overly strip symbols or lowercase everything.
    *   **Precise Aliasing:** Provide several intuitive aliases per tier to help the LLM recognize valid notations (e.g., including `"Victus 2"` alongside `"Corning Gorilla Glass Victus 2"`).
    *   **No Generic Overlaps:** Broad keywords that could trigger false positive matches across multiple tiers (e.g., `"Gorilla Glass"` alone) are strictly forbidden.
6.  **Ambiguity Resolution:** Any other explanation necessary to completely fill in the subsection without ambiguity, specifically handling fallback logic or edge cases.
7.  **NO UNEXPLAINED ABBREVIATIONS:** This is a zero-tolerance rule. If an abbreviation is used in the explanation, it must be explicitly defined (e.g., "Direct Current (DC)") or it will be rejected.
8.  **Meta Block Update (Mandatory at Every Run):** Every time `proposed_data_structure.md` is modified, the `meta` block at the top of the file **MUST** be updated before the task is declared complete:
    ```json
    "meta": {
      "schema_version": "5.1",
      "last_updated": "YYYY-MM-DD"  // Set to the actual current date of the run (not a placeholder).
    }
    ```
    Leaving `last_updated` stale is a data integrity violation — it breaks the file's change-tracking guarantee.
9.  **Numerical Precision:** Apply consistent decimal precision depending on the role of the number:
    - **Intermediate calculation values** (e.g. correction ratios, normalisation factors, raw benchmark inputs): **4 decimal places** (e.g. `9.5478`, `1.0312`). This preserves enough precision so downstream calculations do not accumulate rounding errors.
    - **Scores** (`subscore`, `predicted_score`, `final_score.value`): **2 decimal places** (e.g. `6.73`, `8.50`). Scores are human-facing outputs — excess precision is noise.
    - **Integers** (e.g. raw Megapixel (MP) counts, Hertz (Hz) values, pixel counts): store as plain integers with no decimal point (e.g. `200`, `120`).
10. **Handling Missing Data, Unlisted Features & Scoring Blockers**: 
    If a required parameter's value cannot be found after an exhaustive cross-reference search (strictly satisfying the **Omni-Scan Rule** in Section 3.1), OR if a feature is found but is not scorable using the provided options (e.g., a newly released codec not yet listed):
    - **Value Entry**: Set the `value` field strictly to `"Not found"` (if missing data) or the raw unlisted feature name (if unlisted feature). Do NOT use `null`, `0`, or empty strings. For missing data, set `source` and `exact_extract` fields to `"N/A"`.
    - **Scoring Resilience (Fallbacks & Benchmarks)**: A `"Not found"` or unlisted value does NOT automatically mean the subsection is unscorable:
        - **Fallback Path**: If `scoring_rules.md` provides an alternate calculation path (e.g., estimating HBM from Peak brightness), use it.
        - **Benchmark Override**: If a direct benchmark (Method A) is available, the subsection is scored normally using that method, regardless of the missing raw spec.
    - **Neighbor Interpolation (Method B) Blocked**: Unlike direct benchmarks, Method B **cannot** be used as a fallback for missing specs. Because Method B requires the Predictor (Method C) to identify similar neighbors, if a raw spec is missing and has no fallback, the Predictor cannot be calculated, which in turn blocks the possibility of using Neighbor Interpolation.
    - **Scoring Blocker & Unlisted Feature Procedure**: If the missing data is mandatory for the formula and NO fallback or benchmark override is possible, OR if an unlisted feature is encountered that likely should be scored:
        1. Set `subscore`, `predicted_score`, `final_score.value`, `final_score.method_used`, `final_score.booster`, and `final_score.confidence` to `"N/A"`.
        2. **Top-Level Alert**: You MUST place a GitHub Flavored Markdown (GFM) alert at the very top of `proposed_data_structure.md` (above the JSON block) following one of these exact templates to flag the record for review:
           > [!CAUTION]
           > ### 🚨 SCORING BLOCKER: UNRESOLVED DATA GAP
           > **Subsection [X.Y] ([Name])**: Score calculation is blocked due to missing required data: `[Parameter Name]`. No valid fallback exists.
           
           *OR*
           
           > [!CAUTION]
           > ### 🚨 SCORING BLOCKER: UNLISTED FEATURE DETECTED
           > **Subsection [X.Y] ([Name])**: A feature was found (`[Feature Name]`) but is not scorable using the provided options in the guidelines. This feature needs to be evaluated and added to the scoring guidelines.
    - **Research Guideline**: Before resorting to "Not found", attempt to derive the value from other confirmed specs (e.g., calculating PPI from resolution and diagonal size).
