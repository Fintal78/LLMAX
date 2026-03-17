# Ultimate Smartphone Data Structure Proposal (v5.1)

This schema is the primary, self-contained "Recipe" for AI-automated classification and scoring. It is strictly aligned with the file `scoring_rules.md`.

> [!IMPORTANT]
> ### 🚨 Handling Missing Data, Unlisted Features & Scoring Blockers
> If a required parameter's value cannot be found after an exhaustive search, OR if a feature is found but is not scorable using the provided options (e.g., a newly released codec not yet listed):
> - **Value Entry**: Set the `value` field strictly to `"Not found"` (if missing data) or the raw unlisted feature name (if unlisted feature). Do NOT use `null`, `0`, or empty strings. For missing data, set `source` and `exact_extract` fields to `"N/A"`.
> - **Scoring Procedure**: If the missing data or unlisted feature blocks the formula and NO fallback or benchmark override is possible:
>     1. Set `subscore`, `predicted_score`, `final_score.value`, `final_score.method_used`, `final_score.booster`, and `final_score.confidence` to `"N/A"`.
>     2. **Top-Level Alert**: You MUST place a GFM alert at the very top of the generated file (above the JSON block) following one of these exact templates:
>        <br>`> [!CAUTION]`
>        <br>`> ### 🚨 SCORING BLOCKER: UNRESOLVED DATA GAP`
>        <br>`> **Subsection [X.Y] ([Name])**: Score calculation is blocked due to missing required data: [Parameter Name]. No valid fallback exists.`
>        <br>*OR*
>        <br>`> [!CAUTION]`
>        <br>`> ### 🚨 SCORING BLOCKER: UNLISTED FEATURE DETECTED`
>        <br>`> **Subsection [X.Y] ([Name])**: A feature was found ([Feature Name]) but is not scorable using the provided options in the guidelines. This feature needs to be evaluated.`

```json
{
  // GUIDELINE: All scoring logic, tiers, and technical definitions are provided inline within this document to ensure self-containment for AI agents. `scoring_rules.md` and `scoring_constants.md` serve as baseline references and external constant repositories, respectively.
  // GUIDELINE: All scoring formulas and lookup tables referenced as "Section X.X" or "§X.X" throughout this document are defined in scoring_rules.md. All numeric constants (e.g. _Min / _Max thresholds) are from scoring_constants.md. There is no need to repeat these file names in individual Source comments below.

  // ─────────────────────────────────────────────────────────────────────────────
  // FINAL_SCORE_PREDICTOR_TEMPLATE — applies to ALL subsections that use the "Predictor" method.
  // This template defines the structure and rules for every "final_score" object in Predictor-only subsections.
  // Each "final_score" block that references this template MUST follow it exactly.
  // Do NOT add per-field scoring guidelines inside those final_score blocks.
  //
  //   "final_score": {
  //     "value": <number>,         → The definitive score for this subsection.
  //                                  Calculation: 
  //                                  If no booster is applied, value = predicted_score (i.e., multiplier is 1.0).
  //                                  If there is one booster:
  //                                  value = predicted_score × booster_multiplier
  //                                  If there are several boosters:
  //                                  value = predicted_score × booster_multiplier_1 × booster_multiplier_2 × ... 
  //                                  Each booster multiplier comes from the corresponding Section 11 entry.
  //                                  CLAMPING: The result of this calculation is ALWAYS clamped to [0.00, 10.00].
  //     "method_used": "Predictor" → Always "Predictor" for spec-calculated scores (no Benchmark or Neighbor Interpolation).
  //     "booster": "No"            → Which Section 11 adjustment(s) are applied to the predicted score:
  //                                  • "No"                    = No booster applied (value = predicted_score).
  //                                  • "Section #"             = Single booster (e.g., "11.1").
  //                                  • "Section # + Section #" = Multiple boosters applied in sequence (e.g., "11.1 + 11.2").
  //     "confidence": "N/A"        → Always "N/A" for Predictor methods.
  //   }
  // ─────────────────────────────────────────────────────────────────────────────
  
  // GUIDELINE (meta): Tracks the state of this document itself. Update both fields every time you modify this file.
  "meta": {
    "schema_version": "5.1",
    // GUIDELINE: Version of the data structure schema. Increment only when a structural change is made (new fields added, renamed, or removed). Use semantic versioning (Major.Minor).
    "last_updated": "2026-03-16"
    // GUIDELINE: Date this file was last modified, in ISO 8601 format (YYYY-MM-DD). MUST be updated on every run — leaving this stale is a data integrity violation.
  },
  // GUIDELINE (identity): Uniquely identifies the device and the specific hardware variant being scored. None of these fields feed into scoring — they are used for display, search, and database linking.
  "identity": {
    "id": "samsung_galaxy_s24_ultra",
    // GUIDELINE: Unique machine-readable key for this record. Format: {brand}_{model_name_snakecase}. Must be lowercase, words separated by underscores, no special characters. Example: "samsung_galaxy_s24_ultra".
    "brand": "Samsung",
    // GUIDELINE: Manufacturer brand name exactly as marketed (e.g. "Samsung", "Apple", "Google"). Use the brand's own capitalisation.
    "model_name": "Galaxy S24 Ultra",
    // GUIDELINE: Full commercial model name as printed on the box, including any series suffix (e.g. "Galaxy S24 Ultra", "iPhone 16 Pro Max"). Do not abbreviate.
    "website": "TBD",
    // GUIDELINE: URL of the manufacturer's official product page for this model. Used as the primary source for identity fields. Set to "TBD" until sourced.
    "model_aliases": [
      "SM-S928B",
      "SM-S928U"
    ],
    // GUIDELINE: List of official model numbers (SKUs) corresponding to this variant (e.g. regional or carrier codes). Source from the manufacturer's spec sheet or regulatory filings. Include all known variants that share the same hardware configuration scored in this record.
    "hardware_configuration": {
      // GUIDELINE: Specifies the exact hardware tier being scored. A single device model can ship in multiple RAM/storage configurations — always document the specific variant below.
      "storage_gb": {
        "value": 512,
        "source": "TBD",
        "exact_extract": "Proof pending"
        // GUIDELINE: Internal storage capacity in gigabytes (GB) of this specific variant. Use the marketed integer value (e.g. 256, 512, 1024).
      },
      "ram_gb": {
        "value": 12,
        "source": "TBD",
        "exact_extract": "Proof pending"
        // GUIDELINE: RAM (Random Access Memory) capacity in gigabytes (GB). Use the marketed integer value (e.g. 8, 12, 16).
      },
      "chipset": {
        "value": "Snapdragon 8 Gen 3",
        "source": "TBD",
        "exact_extract": "Proof pending"
        // GUIDELINE: System-on-Chip (SoC) name as marketed (e.g. "Snapdragon 8 Gen 3", "Apple A18 Pro", "Exynos 2400"). Include the brand prefix. Use the variant that matches the region/carrier of this record.
      }
    },
    "release_date": {
      "value": "2024-01-24",
      "source": "TBD",
      "exact_extract": "Proof pending"
      // GUIDELINE: Global launch date in ISO 8601 format (YYYY-MM-DD). Use the first official commercial availability date worldwide. If regional launch dates differ, use the earliest one.
    }
  },
  "1_design_and_build_quality": {
    "form_factor": {
      // The physical shape and deployment style of the device. Allowed values: "Bar" (standard slab, the default for modern smartphones), "Flip" (clamshell foldable that folds horizontally), "Fold" (book-style foldable that opens to a tablet-sized screen), "Slider" (keyboard or screen slides out), "Rugged" (reinforced thick body for extreme conditions). Used for filtering and display only — not scored.
      "value": "Bar",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    // GUIDELINE: List all official colour variants released for this model. Each entry has two fields: `name` (the manufacturer's official marketing name, e.g. "Titanium Black") and `hex` (the closest solid RGB hex code approximating that colour — derive it from official press images or the manufacturer's product page, not from the colour name alone). Used for display and filtering only — not scored.
    "colors": [
      // GUIDELINE: Add as many blocks as there are official colors.
      {
        "name": {
          "value": "Titanium Black",
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "hex": {
          "value": "#1C1C1C",
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      {
        "name": {
          "value": "Titanium Blue",
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "hex": {
          "value": "#4B5D7E",
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      }
    ],
    "1_1_materials": {
      // SCORING GOAL: Scores the structural frame and back panel materials to evaluate build premium and durability class.
      "frame_material": {
        "value": "Titanium Alloy",
        "value_details": {
          "Titanium Alloy": ["Grade 5 Titanium"],
          "Stainless Steel": [],
          "Aluminum Alloy": [],
          "Polymer Composite": [],
          "Not Disclosed": []
        },
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
          // SCORING GUIDELINE: Identify the frame material. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Titanium Alloy"     → 10.00
          //     Definition: High-strength, aerospace-grade alloy (e.g., Grade 5 Titanium).
          //   • "Stainless Steel"    → 8.50
          //     Definition: Corrosion-resistant surgical-grade steel (e.g., SS 316L).
          //   • "Aluminum Alloy"     → 7.00
          //     Definition: Standard lightweight structural alloy (e.g., 6000/7000 series).
          //   • "Polymer Composite"  → 4.00
          //     Definition: Reinforced plastic or resin-based materials (e.g., Polycarbonate).
          //   • "Not Disclosed"      → 0.00
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
      },
      "back_material": {
        "value": "Strengthened Glass",
        "value_details": {
          "Ceramic": [],
          "Strengthened Glass": ["Gorilla Glass Victus 2"],
          "Standard Glass": [],
          "Polymer": [],
          "Not Disclosed": []
        },
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.00
          // SCORING GUIDELINE: Identify the back panel material. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Ceramic"            → 10.00
          //     Definition: Inorganic, non-metallic solid offering superior scratch resistance and heat dissipation.
          //   • "Strengthened Glass" → 8.00
          //     Definition: Chemically tempered or ion-exchange glass (e.g., Victus 2, Ceramic Shield).
          //   • "Standard Glass"     → 6.00
          //     Definition: Basic tempered glass without advanced reinforcement.
          //   • "Polymer"            → 4.00
          //     Definition: Plastic-based resin or composite materials.
          //   • "Not Disclosed"      → 0.00
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
      },
      "predicted_score": 9.20,
      // SCORING GUIDELINE: predicted_score = (0.6 × frame_material.subscore) + (0.4 × back_material.subscore). Source: §1.1 Materials formula for Materials Score.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 9.20,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "1_2_durability": {
      // GUIDELINE: `ingress_protection_rating` stores the full human-readable Ingress Protection (IP) composite string (e.g. "IP68") as declared by the manufacturer. It is not scored directly but the two individual digits extracted for scoring are `dust_protection_digit` and `water_protection_digit`, see below — always parse those from this `ingress_protection_rating.value` string.
      "ingress_protection_rating": {
        "value": "IP68",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      // SCORING GOAL: Scores dust and water resistance separately using the two digits of the Ingress Protection (IP) rating defined by International Electrotechnical Commission (IEC) standard 60529. The full composite string is available at `1_2_durability.ingress_protection_rating.value` for reference.
      "dust_protection_digit": {
        "value_path": "1_2_durability.ingress_protection_rating.value",
        "value": "Digit 6",
        "subscore": 10.00
          // SCORING GUIDELINE: Identify the first digit of the IP rating via "ingress_protection_rating". Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Digit 6"    → 10.00
          //   • "Digit 5"    → 8.00
          //   • "Digit 4"    → 6.00
          //   • "Digit 3"    → 4.00
          //   • "Digit 2"    → 2.00
          //   • "Digit 0–1"  → 0.00
      },
      "water_protection_digit": {
        "value_path": "1_2_durability.ingress_protection_rating.value",
        "value": "Digit 8",
        "subscore": 9.00
          // SCORING GUIDELINE: Identify the second digit of the IP rating via "ingress_protection_rating". Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Digit 9"    → 10.00
          //   • "Digit 8"    → 9.00
          //   • "Digit 7"    → 8.00
          //   • "Digit 6"    → 6.00
          //   • "Digit 5"    → 4.00
          //   • "Digit 4"    → 2.00
          //   • "Digit 0–3"  → 0.00
      },
      "predicted_score": 9.50,
      // SCORING GUIDELINE: predicted_score = (0.5 × dust_protection_digit.subscore) + (0.5 × water_protection_digit.subscore). Source: §1.2 IP Score formula.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 9.50,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "1_3_glass_protection": {
      // SCORING GOAL: Scores the protective glass type on the display, known as Display Glass Protection (DGP), based on the manufacturer-declared glass generation's certified drop and scratch resistance class. Source: Section 1.3 Display Glass Protection table.
      "glass_generation": {
        "value": "Armor-Class",
        "value_details": {
          "Armor-Class": ["Gorilla Glass Armor"],
          "Shield-Class": [],
          "Ultra-Reinforced": [],
          "Premium Reinforced": [],
          "Standard Reinforced": [],
          "Entry-Level Reinforced": [],
          "Tempered Glass": [],
          "Glass (Unspecified)": [],
          "Plastic or No Glass": []
        },
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Identify the highest glass tier based on manufacturer drop/scratch claims. Use the following exact Tier Names for "value" with related scores as subscore:
        //   • "Armor-Class"           → 10.00
        //     Definition: Anti-reflective (AR) coating + ≥2.0m rough-surface drop certification (e.g., Gorilla Glass Armor).
        //   • "Shield-Class"          → 9.50
        //     Definition: Ceramic-infused matrix + ≥2.0m drop certification (e.g., Ceramic Shield, Kunlun Glass).
        //   • "Ultra-Reinforced"      → 9.00
        //     Definition: Advanced alumina-silicate glass optimized for rough-surface drops (≥2.0m class) (e.g., Gorilla Glass Victus 2).
        //   • "Premium Reinforced"    → 8.00
        //     Definition: High-end chemical tempering with ≥2.0m standard drop certification (e.g., Victus, Victus+, Star 2).
        //   • "Standard Reinforced"   → 7.00
        //     Definition: Regular flagship-grade chemical tempering with ≥1.6m drop certification (e.g., Gorilla Glass 5/6, Dragontrail Pro / Star).
        //   • "Entry-Level Reinforced" → 5.00
        //     Definition: Basic chemical tempering with ~1.2m drop certification (e.g., Gorilla Glass 3, Panda Glass, Dragontrail).
        //   • "Tempered Glass"        → 3.00
        //     Definition: Basic chemically strengthened glass with no certified drop class.
        //   • "Glass (Unspecified)"   → 2.00
        //   • "Plastic or No Glass"   → 0.00
        // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
      },
      "predicted_score": 10.00,
      // SCORING GUIDELINE: predicted_score directly inherits glass_generation.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 10.00,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "1_4_thickness": {
      // SCORING GOAL: Scores device thickness (excluding camera bump) as a measure of pocketability and hand comfort. Thinner is always better.
      "thickness_mm": {
        "value": 8.6,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 3.50
        // SCORING GUIDELINE: Apply the Section 1.4 linear formula: Score = 10 − 10 × ((thickness_mm − Thickness_mm_Min) / (Thickness_mm_Max − Thickness_mm_Min)), clamped 0–10.
      },
      "predicted_score": 3.50,
      // SCORING GUIDELINE: predicted_score directly inherits thickness_mm.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 3.50,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "1_5_weight": {
      // SCORING GOAL: Scores total device weight as a measure of long-term holding comfort. Lighter phones cause less wrist and arm fatigue during extended use.
      "weight_g": {
        "value": 232,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 1.64
        // SCORING GUIDELINE: Apply the Section 1.5 linear formula: Score = 10 − 10 × ((weight_g − Weight_g_Min) / (Weight_g_Max − Weight_g_Min)), clamped 0–10.
      },
      "predicted_score": 1.64,
      // SCORING GUIDELINE: predicted_score directly inherits weight_g.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 1.64,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "1_6_ergonomics": {
      // SCORING GOAL: Scores device width as a measure of one-handed ergonomics. Beyond a critical threshold, phones become difficult to grip and operate single-handedly. Note: the positive benefit of a wider screen is already captured in Sections 2.8 (Screen-to-Body Ratio) and 2.9 (Screen Size).
      "width_mm": {
        "value": 79.0,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.00
        // SCORING GUIDELINE: Apply the Section 1.6 quadratic formula: Score = 10 × (1 − ((width_mm − Width_mm_Min) / (Width_mm_Max − Width_mm_Min))²), clamped 0–10.
      },
      "predicted_score": 0.00,
      // SCORING GUIDELINE: predicted_score directly inherits width_mm.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 0.00,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    }
  },
  "2_display": {
    "aspect_ratio": {
      // GUIDELINE: Width-to-height display ratio expressed as W:H (e.g. "19.5:9"). Used for display and filtering only — not scored. Determines the shape of the canvas (e.g. whether content letterboxes, how wide the keyboard appears, cinematic vs. tall format).
      "value": "19.5:9",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "2_1_panel_architecture": {
      // SCORING GOAL: Scores the physical display technology (Display Panel Architecture, DPA) used to generate light and images. Focuses on panel construction only — not brightness, color, or refresh behaviour. Source: Section 2.1 Display Panel Architecture.
      "panel_type": {
        "value": "LTPO OLED",
        "value_details": {
          "Tandem OLED": [],
          "LTPO OLED": ["Dynamic AMOLED 2X"],
          "Standard OLED/AMOLED (LTPS)": [],
          "IPS LCD": [],
          "TFT or PLS LCD": [],
          "TN LCD or Legacy": []
        },
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 9.00
        // SCORING GUIDELINE: Identify the panel type. Use the following exact Tier Names for "value" with related scores as subscore:
        //   • "Tandem OLED"                   → 10.00
        //     Definition: Dual-stack Organic Light-Emitting Diode (OLED) with two vertical light-emitting layers.
        //   • "LTPO OLED"                     → 9.00
        //     Definition: Organic Light-Emitting Diode (OLED) with Low-Temperature Polycrystalline Oxide (LTPO) backplane. Supports variable refresh rate down to 1 Hz.
        //   • "Standard OLED/AMOLED (LTPS)"   → 8.00
        //     Definition: Organic Light-Emitting Diode (OLED) with Low-Temperature Polycrystalline Silicon (LTPS) backplane. Self-emissive pixels; lacks variable refresh rate down to 1 Hz.
        //   • "IPS LCD"                       → 6.00
        //     Definition: In-Plane Switching Liquid-Crystal Display (IPS LCD). Utilizes a backlight with in-plane liquid crystal alignment.
        //   • "TFT or PLS LCD"                → 2.00
        //     Definition: Standard active-matrix Liquid-Crystal Display (LCD) including Plane-to-Line Switching (PLS) and non-IPS Thin-Film Transistor (TFT) variants. 
        //   • "TN LCD or Legacy"              → 0.00
        //     Definition: Twisted Nematic Liquid-Crystal Display (TN LCD) or legacy technologies. Liquid crystals twist to control light; characterized by color inversion or contrast shift at off-axis viewing angles.
        // AMBIGUITY RULE: Plain "OLED" or "AMOLED" with NO "LTPO" qualifier must default to "Standard OLED/AMOLED (LTPS)" (8.00).
        // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
      },
      "predicted_score": 9.00,
      // SCORING GUIDELINE: predicted_score directly inherits panel_type.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 9.00,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_2_brightness": {
      // SCORING GOAL: Scores peak and High Brightness Mode (HBM) brightness together, as HBM governs outdoor readability while peak brightness governs High Dynamic Range (HDR) media quality.
      "peak_nits": {
        "value": 2600,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.73
        // SCORING GUIDELINE: Apply the Section 2.2 logarithmic formula: Peak_Score = 10 × (log(peak_nits) − log(Display_Brightness_Nits_Min)) / (log(Display_Brightness_Nits_Max) − log(Display_Brightness_Nits_Min)), clamped 0–10.
      },
      "hbm_nits": {
        "value": 1500,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.21
        // SCORING GUIDELINE: Apply the Section 2.2 logarithmic formula: HBM_Score = 10 × (log(hbm_nits) − log(Display_HBM_Nits_Min)) / (log(Display_HBM_Nits_Max) − log(Display_HBM_Nits_Min)), clamped 0–10. Fallback: if hbm_nits is unavailable, then set "value" to "Not found" and use the formula with the fallback value hbm_nits = peak_nits / 1.5.
      },
      "predicted_score": 7.37,
      // SCORING GUIDELINE: predicted_score = (0.7 × hbm_nits.subscore) + (0.3 × peak_nits.subscore)
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 7.37,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_3_color_gamut_coverage": {
      // SCORING GOAL: Scores how much of the Digital Cinema Initiatives (DCI-P3) professional color space the display can reproduce. A wider gamut means richer, more saturated colors in photos, videos, and High Dynamic Range (HDR) content.
      "dci_p3_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Apply the Section 2.3 linear formula: Score = 10 × (dci_p3_percent − Display_P3_Coverage_Percent_Min) / (Display_P3_Coverage_Percent_Max − Display_P3_Coverage_Percent_Min), clamped 0–10. If dci_p3_percent is not available from any source then set "value" to "Not found" and subscore to "N/A". Then use the "srgb_percent" block below as fallback scoring. 
      },
      "srgb_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A"
        // SCORING GUIDELINE: sRGB coverage is a fallback data source only. ONLY when dci_p3_percent is not available from any source use the formula above with DCI-P3_estimate = min(srgb_percent × 0.75, 100) to calculate the subscore of this block. When dci_p3_percent is available and the subscore was calculated in the previous block then set the subscore of this block to "N/A".
      },
      "predicted_score": 10.00,
      // SCORING GUIDELINE: predicted_score directly inherits dci_p3_percent.subscore or srgb_percent.subscore, whichever is not "N/A".
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 10.00,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_4_hdr_format_support": {
      // SCORING GOAL: Scores which High Dynamic Range (HDR) video formats the display officially supports. Dynamic HDR formats optimize brightness and colour frame-by-frame, unlocking the full quality of premium streaming content.
      "supported_formats": {
        "value": [
          "HDR10+",
          "HDR10"
        ],
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.00
        // SCORING GUIDELINE: Identify the presence of officially supported HDR formats. For each supported format, use the exact term below for the "value" array:
        //   • "Dolby Vision"  → adds +3.00 to the subscore
        //   • "HDR10+"        → adds +2.00 to the subscore
        //   • "HDR10"         → adds +5.00 to the subscore
        // The subscore is the sum of these points (Clamped 0–10). Example: ["HDR10+", "HDR10"] = 5.00 + 2.00 = 7.00.
        // If the device does not list support for any HDR formats (or explicitly only supports Standard Dynamic Range / SDR), leave the array empty [] and set subscore to 0.00.
      },
      "predicted_score": 7.00,
      // SCORING GUIDELINE: predicted_score directly inherits supported_formats.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 7.00,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_5_resolution_density": {
      // SCORING GOAL: Scores pixel density (Pixels Per Inch, PPI) as a measure of display sharpness. Higher PPI means text and images look crisp with no visible pixels.
      "resolution_width_px": {
        // GUIDELINE: Horizontal pixel count of the display. Used for scoring ONLY when Pixels Per Inch (PPI) is not available from any source.
        "value": 1440,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "resolution_height_px": {
        // GUIDELINE: Vertical pixel count of the display. Used for scoring ONLY when Pixels Per Inch (PPI) is not available from any source.
        "value": 3120,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "pixels_per_inch": {
        "value": 505,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.43
        // SCORING GUIDELINE: Apply the Section 2.5 logarithmic formula: Score = 10 × (log(pixels_per_inch) − log(Display_PPI_Min)) / (log(Display_PPI_Max) − log(Display_PPI_Min)), clamped 0–10. Use directly pixels_per_inch.value if available from any source. 
        // ONLY if pixels_per_inch is NOT available derive PPI: pixels_per_inch = √(resolution_width_px² + resolution_height_px²) / diagonal_inches 
        // with diagonal_inches = 2_9_screen_size.diagonal_inches.value and in that case set "source" to "Derived from resolution_width_px, resolution_height_px, and diagonal_inches" and set "exact_extract" to "N/A".
      },
      "predicted_score": 8.43,
      // SCORING GUIDELINE: predicted_score directly inherits pixels_per_inch.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 8.43,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_6_motion_smoothness": {
      // SCORING GOAL: Scores Motion Smoothness via maximum refresh rate. Higher Hertz (Hz) means scrolling and animations look smoother. 120 Hz and above are perceptibly superior to standard 60 Hz.
      "maximum_refresh_rate_hz": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.55
        // SCORING GUIDELINE: Apply the Section 2.6 logarithmic formula: Score = 10 × (log(maximum_refresh_rate_hz) − log(Display_Refresh_Rate_Hz_Min)) / (log(Display_Refresh_Rate_Hz_Max) − log(Display_Refresh_Rate_Hz_Min)), clamped 0–10.
      },
      "predicted_score": 7.55,
      // SCORING GUIDELINE: predicted_score directly inherits maximum_refresh_rate_hz.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 7.55,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_7_touch_responsiveness": {
      // SCORING GOAL: Scores touch sampling rate as a measure of how instantly the screen responds to finger input. Higher rates produce a "glued to your finger" feel, critical for gaming and User Interface (UI) fluidity.
      "touch_sampling_rate_hz": {
        "value": 240,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 5.00,
        // SCORING GUIDELINE: Apply the Section 2.7 logarithmic formula: Score = 10 × (log(touch_sampling_rate_hz) − log(Display_Touch_Sampling_Hz_Min)) / (log(Display_Touch_Sampling_Hz_Max) − log(Display_Touch_Sampling_Hz_Min)), clamped 0–10.
      },
      "predicted_score": 5.00,
      // SCORING GUIDELINE: predicted_score directly inherits touch_sampling_rate_hz.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 5.00,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_8_screen_to_body_ratio": {
      // SCORING GOAL: Scores the Screen-to-Body Ratio (SBR) — how much of the front face is active display versus border (bezel). Higher percentage means a more immersive, modern design.
      "screen_to_body_ratio_percent": {
        "value": 88.5,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.64
        // SCORING GUIDELINE: Apply the Section 2.8 linear formula: Score = 10 × ((screen_to_body_ratio_percent − Display_SBR_Percent_Min) / (Display_SBR_Percent_Max − Display_SBR_Percent_Min)), clamped 0–10.
        // FALLBACK: If "screen_to_body_ratio_percent" is NOT available from primary sources, derive it using: (Active Display Area / Total Frontal Area) * 100. That should be well documented and justified via "source" and "exact_extract", if needed by providing multiple sources and extracts (stored in "source" and "exact_extract" and separated via commas). 
      },
      "predicted_score": 8.64,
      // SCORING GUIDELINE: predicted_score directly inherits screen_to_body_ratio_percent.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 8.64,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_9_screen_size": {
      // SCORING GOAL: Scores the physical display diagonal as a measure of immersion and media consumption experience. Larger screens offer more real estate for video, gaming, and productivity.
      "diagonal_inches": {
        "value": 6.8,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.93
        // SCORING GUIDELINE: Apply the Section 2.9 quadratic formula: Score = 10 × ((diagonal_inches² − Display_Size_Inch_Min²) / (Display_Size_Inch_Max² − Display_Size_Inch_Min²)), clamped 0–10.
      },
      "predicted_score": 6.93,
      // SCORING GUIDELINE: predicted_score directly inherits diagonal_inches.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 6.93,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_10_eye_comfort": {
      // SCORING GOAL: Evaluates display flicker at low brightness levels to prevent eye strain and fatigue. Scores either the constant light of Direct Current (DC) Dimming (10.00) or a tiered penalty based on the Pulse-Width Modulation (PWM) frequency.
      "flicker_presence": {
        "value": "Yes",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A"
        // SCORING GUIDELINE: Record if PWM flicker is present (Yes/No).
        //   • "No" (DC Dimming): Applies to Liquid-Crystal Display (LCD) or In-Plane Switching (IPS) panels utilizing standard DC dimming with zero measurable flicker. Subscore is 10.00.
        //   • "Yes" (PWM Dimming): Applies to Organic Light-Emitting Diode (OLED) or Active Matrix Organic Light-Emitting Diode (AMOLED) panels using PWM for dimming, or any LCD confirmed to have measurable PWM flicker. Subscore is "N/A" (score will be derived from frequency, see below).
      },
      "pulse_width_modulation_dimming_hertz": {
        "value": 492,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 4.07
        // SCORING GUIDELINE: Only evaluated if flicker_presence.value = "Yes". Apply the Section 2.10.2 logarithmic formula: Score = 10 × (log(pulse_width_modulation_dimming_hertz) − log(Display_PWM_Hz_Min)) / (log(Display_PWM_Hz_Max) − log(Display_PWM_Hz_Min)), clamped 0–10. If flicker_presence.value = "No", all fields MUST be "N/A".
      },
      "predicted_score": 4.07,
      // SCORING GUIDELINE: The predicted score directly inherits whichever subscore is NOT "N/A" between flicker_presence and pulse_width_modulation_dimming_hertz.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 4.07,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_11_display_benchmark_final_scoring": {
      // SCORING GOAL: Produces the overall Display Final Score using a three-method hierarchy (A→B→C). Method A uses the DXOMARK Display benchmark when available. Method B uses Nearest Neighbor Interpolation when only similar devices have benchmarks. Method C (Predictor) is the fallback weighted sum of sub-section predicted scores.

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD A — Direct Benchmark (Primary)
      // ═══════════════════════════════════════════════════════════════════════════
      "dxomark_display_score": {
        "value": 150,
        "source": "https://www.dxomark.com/smartphones/#display", // if the score is available for the device you MUST put the exact url here
        "exact_extract": "Proof pending",
        "subscore": 9.34
        // SCORING GUIDELINE: Apply the Section 2.11 Method A logarithmic normalization: Score = 10 × (log(dxomark_display_score) − log(Display_DXO_Score_Min)) / (log(Display_DXO_Score_Max) − log(Display_DXO_Score_Min)), clamped 0–10. DXOMARK scores cover readability, colour, video, motion, touch. If no DXOMARK score is available set value to "Not found" and exact_extract and subscore to "N/A".
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD C — Predicted Calculation (Tertiary / baseline for Method B)
      // ═══════════════════════════════════════════════════════════════════════════
      
      "method_c_predicted_score": {
        // SCORING GUIDELINE (Section 2.11 Method C), these are the 8 perceptual sub-section predicted scores and their weights:
        "subscore_2_1":  { "subscore_path": "2_1_panel_architecture.predicted_score",   "weight_2_1": 0.15 },
        "subscore_2_2":  { "subscore_path": "2_2_brightness.predicted_score",            "weight_2_2": 0.20 },
        "subscore_2_3":  { "subscore_path": "2_3_color_gamut_coverage.predicted_score",  "weight_2_3": 0.10 },
        "subscore_2_4":  { "subscore_path": "2_4_hdr_format_support.predicted_score",    "weight_2_4": 0.10 },
        "subscore_2_5":  { "subscore_path": "2_5_resolution_density.predicted_score",    "weight_2_5": 0.10 },
        "subscore_2_6":  { "subscore_path": "2_6_motion_smoothness.predicted_score",     "weight_2_6": 0.15 },
        "subscore_2_7":  { "subscore_path": "2_7_touch_responsiveness.predicted_score",  "weight_2_7": 0.10 },
        "subscore_2_10": { "subscore_path": "2_10_eye_comfort.predicted_score",          "weight_2_10": 0.10 },

        // These inputs are used to calculate the overall predicted_score (Method C):
        "predicted_score": 7.51,
        // SCORING GUIDELINE: predicted_score = Sum(subscore_X × weight_X) for all 8 entries above. 

        // Sections 2.8 (Screen-to-Body Ratio) and 2.9 (Screen Size) are excluded because DXOMARK does not evaluate physical dimensions.
        // IMPORTANT: Always use Predicted Scores (before any Boosters), not Final Scores, to ensure hardware-only comparison.
      },
    
      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD B — Nearest Neighbor Interpolation (Secondary)
      // ═══════════════════════════════════════════════════════════════════════════
      
      "method_b_neighbor_interpolation": {
        // SCORING GUIDELINE (Section 2.11 Method B): Only populated when Method A is NOT available but at least 3 devices with DXOMARK Display scores exist in the database. If Method A is available for the device then Method B can be skipped completely, all fields must be set to "N/A".
        // Step 1 (Section 2.11 Method B.1): Find the 3 devices with the smallest weighted Euclidean distance using the method_c_predicted_score weights and sub-section predicted scores.
        //         Distance = √( Sum( weight_i × (SubScore_Target_i − SubScore_Neighbor_i)² ) )
        //         Where 'i' iterates over each of the 8 method_c_predicted_score entries (subscore_2_1 through subscore_2_10, except subscore_2_8 and subscore_2_9), weight_i is the entry's weight, SubScore_Target_i is this device's sub-section_i predicted score, and SubScore_Neighbor_i is the candidate neighbor's sub-section_i predicted score.
        //         Search space: all phones that have a known DXOMARK Display score (Method A).
        // Step 2 (Section 2.11 Method B.2–B.3): Calculate the correction ratio and apply it to the average neighbor benchmark.
        "neighbors": [
          {
            // Neighbor1
            "device_id_1": "N/A",
            // GUIDELINE: The identity.id of the neighbor device (e.g., "google_pixel_9_pro").
            "euclidean_distance_1": "N/A",
            // GUIDELINE: Weighted Euclidean distance from Step 1.
            "predicted_score_1": "N/A",
            // GUIDELINE: The neighbor's own Method C predicted_score (overall display).
            "benchmark_score_1": "N/A"
            // GUIDELINE: The neighbor's Method A dxomark_display_score.subscore.
          },
          {
            // Neighbor2
            "device_id_2": "N/A",
            "euclidean_distance_2": "N/A",
            "predicted_score_2": "N/A",
            "benchmark_score_2": "N/A"
          },
          {
            // Neighbor3
            "device_id_3": "N/A",
            "euclidean_distance_3": "N/A",
            "predicted_score_3": "N/A",
            "benchmark_score_3": "N/A"
          }
        ],
        "avg_predicted_neighbors": "N/A",
        // SCORING GUIDELINE (Section 2.11 Method B Step 2): (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
        "avg_benchmark_neighbors": "N/A",
        // SCORING GUIDELINE (Section 2.11 Method B Step 3): (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
        "correction_ratio": "N/A",
        // SCORING GUIDELINE (Section 2.11 Method B Step 2): method_c_predicted_score.predicted_score / avg_predicted_neighbors.
        "interpolated_score": "N/A"
        // SCORING GUIDELINE (Section 2.11 Method B Step 3): correction_ratio × avg_benchmark_neighbors. This is the final Method B score, used only if Method A is unavailable.
      },

      "final_score": {
        "value": 9.34,
        // SCORING GUIDELINE (Section 2.11): Use Method A if dxomark_display_score is available (dxomark_display_score.subscore becomes the final value). Otherwise use Method B (interpolated_score from method_b_neighbor_interpolation). Otherwise fall back to Method C (method_c_predicted_score.predicted_score). 
        "method_used": "Benchmark (DXOMARK)",
        // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
        //   • Benchmark (DXOMARK)    → Method A (documented DXOMARK score)
        //   • Neighbor Interpolation → Method B (similar device benchmarks)
        //   • Predictor              → Method C (weighted spec calculation)
        "booster": "No",
        // SCORING GUIDELINE: Must always be set to "No".
        "confidence": "N/A"
        // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor. "High", "Medium", or "Low" only when 2 independent benchmarks are cross-referenced.
      }
    },
    "3_audio": {
      "3_1_speaker_system_capability": {
        // SCORING GOAL: Scores the physical speaker hardware configuration (Speaker System Capability, SSC) for audio output without headphones. Evaluates speaker count, placement, and channel symmetry. Source: Section 3.1 Speaker System Capability.
        "speaker_configuration": {
          "value": "Standard Hybrid Stereo",
          "value_details": {
            "Balanced / Symmetrical Stereo": [],
            "Standard Hybrid Stereo": ["Stereo Speakers"],
            "Mono Speaker": [],
            "No Usable Speaker": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.00
          // SCORING GUIDELINE: Identify the physical speaker setup. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Balanced / Symmetrical Stereo" → 10.00
          //     Definition: Two identical or near-identical dedicated speaker units (top/bottom or left/right) offering matched frequency response and volume. Must explicitly state "Symmetrical speakers" or "Balanced stereo".
          //   • "Standard Hybrid Stereo"        → 7.00
          //     Definition: Typically uses the earpiece as a second channel, lacking the bass response and volume of the primary speaker. Typically listed as 'Stereo Speakers' without symmetry claims.
          //   • "Mono Speaker"                  → 3.00
          //     Definition: Single active loudspeaker for media playback.
          //   • "No Usable Speaker"             → 0.00
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 7.00,
        // SCORING GUIDELINE: predicted_score directly inherits speaker_configuration.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "3_2_playback_audio_processing_immersion": {
        // SCORING GOAL: Scores Playback Audio Processing & Immersion (PAPI) as a composite of two sub-criteria: audio format decoding capability (3.2.1, weight 50%) and spatial audio rendering capability (3.2.2, weight 50%). Source: Section 3.2 Playback Audio Processing & Immersion (PAPI).
        "audio_format_decode": {
          "value": [
            "Dolby Atmos",
            "Dolby Digital / Dolby Audio"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the presence of officially supported audio formats. For each supported format, use the exact term below for the "value" array:
          //   • "Dolby Atmos"                 → adds +5.00 to the subscore
          //   • "Dolby Digital / Dolby Audio" → adds +3.00 to the subscore
          //   • "DTS:X"                       → adds +1.00 to the subscore
          //   • "DTS / DTS-HD"                → adds +1.00 to the subscore
          // The subscore is the sum of these points (Clamped 0–10). Example: ["Dolby Atmos", "Dolby Digital / Dolby Audio"] = 5.00 + 3.00 = 8.00.
          // If the device does not list support for any multichannel/object formats (or explicitly only supports stereo), leave the array empty [] and set subscore to 0.00.
        },
        "spatial_audio_rendering": {
          "value": "Static spatial audio (no head tracking)",
          "value_details": {
            "Spatial audio with Dynamic Head Tracking": [],
            "Static spatial audio (no head tracking)": ["360 Audio"],
            "No spatial rendering": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.00
          // SCORING GUIDELINE: Identify the highest-tier spatial capability. Use the following terms exclusively for "value" with related scores as subscore:
          //   • "Spatial audio with Dynamic Head Tracking"      → 10.00
          //   • "Static spatial audio (no head tracking)"       → 7.00
          //   • "No spatial rendering"                          → 0.00
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 7.50,
        // SCORING GUIDELINE: predicted_score = (0.5 × audio_format_decode.subscore) + (0.5 × spatial_audio_rendering.subscore).
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.50,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "3_3_wired_audio_capability": {
        // SCORING GOAL: Scores native wired audio output capability. Evaluates the best natively supported wired audio tier without requiring powered external accessories. Per the hierarchical category rule, only the highest supported tier is stored. Source: §3.3 Wired Audio Capability.
        "wired_audio_tier": {
          "value": "USB-C digital audio only (dongle required)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 3.00
          // SCORING GUIDELINE: Identify the highest supported wired audio tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "3.5mm headphone jack (native analog output)"  → 10.00
          //   • "USB-C with documented analog audio output"    → 6.00
          //   • "USB-C digital audio only (dongle required)"   → 3.00
          //   • "No wired audio support"                       → 0.00
        },
        "predicted_score": 3.00,
        // SCORING GUIDELINE: predicted_score (Wired Audio Score) directly inherits wired_audio_tier.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 3.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "3_4_microphone_audio_recording": {
        // SCORING GOAL: Scores Microphone & Audio Recording (MAR) as a composite of hardware count (3.4.1, 30%), recording channels (3.4.2, 30%), and advanced capture features (3.4.3, 40%). Source: Section 3.4 Microphone & Audio Recording (MAR).
        "microphone_hardware_count": {
          "value": "3",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Record the physical microphone count. Use the following terms exclusively for "value" with related scores as subscore:
          //   • ≥4 microphones   → 10.00
          //   • 3                → 8.00
          //   • 2                → 5.00
          //   • 1                → 2.00
          //   • None             → 0.00
        },
        "recording_channels_modes": {
          "value": "Stereo",
          "value_details": {
            "Multi-channel / spatial audio": [],
            "Stereo": ["Stereo recording"],
            "Mono": [],
            "Voice-only / unclear": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the highest-tier recording capability. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Multi-channel / spatial audio" → 10.00
          //     Definition: Captures audio with directional data (e.g., 5.1, 7.1, or OZO Audio).
          //   • "Stereo"                        → 8.00
          //     Definition: Standard two-channel (Left/Right) audio recording.
          //   • "Mono"                          → 5.00
          //     Definition: Single-channel audio recording.
          //   • "Voice-only / unclear"          → 0.00
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "advanced_capture_features": {
          "value": [
            "Directional / Audio Zoom",
            "Wind Noise Reduction"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 5.00
          // SCORING GUIDELINE: Identify the presence of documented features from the list below. For each detected feature, use the exact term before the ": " symbol (e.g., "Directional / Audio Zoom" or "Wind Noise Reduction") for the "value" array. Each feature adds +2.50 points to the subscore (Clamped 0–10). Example: 2 features × 2.50 = 5.00.
          //   • Directional / Audio Zoom: Focuses audio on the zoomed subject (e.g., "Audio Zoom", "Zoom-in Mic")
          //   • Wind Noise Reduction: Dedicated toggle or feature to filter wind rumble
          //   • Voice Focus / Isolation: Feature to enhance speech over background noise (e.g., "Speech Enhancement", "Audio Eraser")
          //   • Pro Mic Support: Accepts an external mic for video recording — wired (USB-C or 3.5mm) or wireless (Bluetooth). Verify via spec sheet listing for example "external mic input", a documented gain/level control in the camera app, or reviewer confirmation of external mic recording
          // Always populate the full list of detected features in "value". Do not selectively omit. Source: §3.4.3 Advanced Capture Features.
        },
        "predicted_score": 6.80,
        // SCORING GUIDELINE: predicted_score = (0.30 × microphone_hardware_count.subscore) + (0.30 × recording_channels_modes.subscore) + (0.40 × advanced_capture_features.subscore). Weights from the MAR formula in Section 3.4.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 6.80,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "4_camera_systems": {
      // GUIDELINE: Hardware inventory of all physical camera modules. Contains ONLY unscored reference data, as non-scoring data must be placed at section root. All scored parameters are stored in their respective scoring subsections and are NOT duplicated here.
      // Each key under "rear_camera" / "front_camera" is the lens role (e.g., "main", "tele_5x"). All fields inside are unscored reference data.
      // MISSING DATA RULE: If a required specification cannot be verified (either because the feature is absent 
      // or the data is unavailable after an exhaustive research), set the "value" field strictly to "Not found or non existing" 
      // and set "source" and "exact_extract" to "N/A".
      "rear_camera": {
        "main": {
          // GUIDELINE: Main rear camera module. Only the sensor model name is stored here as unscored reference.
          "sensor_model_name": {
            // GUIDELINE: Sensor model name (e.g., "ISOCELL HP2").
            "value": "ISOCELL HP2",
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        "telephoto_1": {
          // GUIDELINE: First telephoto rear camera module (highest optical zoom). Use "telephoto_1" for the primary
          // telephoto lens, "telephoto_2" for a second one if present. 
          "optical_zoom": {
            // GUIDELINE: Optical zoom factor of this telephoto lens (e.g., "5x", "3x", "10x").
            "value": "5x",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "sensor_model_name": {
            // GUIDELINE: Sensor model name.
            "value": "IMX854",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "megapixels": {
            // GUIDELINE: Resolution of this non-main lens in Megapixels (MP).
            "value": 50,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "aperture": {
            // GUIDELINE: Aperture of this non-main lens.
            "value": "f/3.4",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "optical_image_stabilization": {
            // GUIDELINE: Whether this non-main lens has Optical Image Stabilization (OIS).
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        "telephoto_2": {
          // GUIDELINE: Second telephoto rear camera module (if present).
          "optical_zoom": {
            // GUIDELINE: Optical zoom factor of this telephoto lens (e.g., "3x", "2x").
            "value": "3x",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "sensor_model_name": {
            // GUIDELINE: Sensor model name.
            "value": "IMX754",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "megapixels": {
            // GUIDELINE: Resolution of this non-main lens in Megapixels (MP).
            "value": 10,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "aperture": {
            // GUIDELINE: Aperture of this non-main lens.
            "value": "f/2.4",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "optical_image_stabilization": {
            // GUIDELINE: Whether this non-main lens has Optical Image Stabilization (OIS).
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        "ultrawide": {
          // GUIDELINE: Ultrawide rear camera module.
          "sensor_model_name": {
            // GUIDELINE: Sensor model name.
            "value": "IMX564",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "megapixels": {
            // GUIDELINE: Resolution of this non-main lens in Megapixels (MP).
            "value": 12,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "aperture": {
            // GUIDELINE: Aperture of this non-main lens.
            "value": "f/2.2",
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        }
      },
      "front_camera": {
        "main": {
          // GUIDELINE: Main front-facing camera module. Only the sensor model name is stored here as unscored reference.
          "sensor_model_name": {
            // GUIDELINE: Front sensor model name.
            "value": "Not found or non existing",
            "source": "N/A",
            "exact_extract": "N/A"
          }
        }
      },
      "4_1_main_sensor_size": {
        // SCORING GOAL: Scores the main camera sensor size as the primary determinant of image quality.
        "optical_format": {
          "value": "1/1.3 inches",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.11
          // SCORING GUIDELINE: Apply the Section 4.1 logarithmic formula: Score = 10 × (log(4_1_main_sensor_size.optical_format.value) − log(Camera_Main_Sensor_Inch_Min)) / (log(Camera_Main_Sensor_Inch_Max) − log(Camera_Main_Sensor_Inch_Min)), clamped 0–10. Convert the optical format string to a decimal (e.g., "1/1.3 inches" → 0.7692).
        },
        "predicted_score": 8.11,
        // SCORING GUIDELINE: predicted_score directly inherits optical_format.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.11,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_2_main_camera_aperture": {
        // SCORING GOAL: Scores the main camera lens aperture (f-number).
        "aperture_f_stop": {
          "value": "f/1.7",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 6.40
          // SCORING GUIDELINE: Apply the Section 4.2 inverted logarithmic formula: Score = 10 × (log(Camera_Main_Aperture_f_Max) − log(aperture_f_stop)) / (log(Camera_Main_Aperture_f_Max) − log(Camera_Main_Aperture_f_Min)), clamped 0–10. Parse the f-stop string to a decimal (e.g., "f/1.7" → 1.7). The formula is inverted because lower f-numbers are better.
        },
        "predicted_score": 6.40,
        // SCORING GUIDELINE: predicted_score directly inherits aperture_f_stop.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 6.40,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_3_main_camera_resolution": {
        // SCORING GOAL: Scores the main sensor's maximum pixel count in Megapixels (MP).
        "megapixels": {
          "value": 200,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 4.3 logarithmic formula: Score = 10 × (log(megapixels) − log(Camera_Main_Resolution_MP_Min)) / (log(Camera_Main_Resolution_MP_Max) − log(Camera_Main_Resolution_MP_Min)), clamped 0–10.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits megapixels.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_4_image_stabilization": {
        // SCORING GOAL: Scores the image stabilization mechanism used to compensate for hand shake during photo and video capture. Source: Section 4.4 Image Stabilization.
        "stabilization_type": {
          "value": "Lens-Based Optical Image Stabilization",
          "value_details": {
            "Multi-Axis Mechanical Stabilization (Gimbal)": [],
            "Sensor-Shift Optical Image Stabilization": [],
            "Lens-Based Optical Image Stabilization": ["OIS"],
            "Software-Only Stabilization (Electronic, no hardware)": [],
            "None": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the stabilization mechanism. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Multi-Axis Mechanical Stabilization (Gimbal)"          → 10.00
          //     Definition: The entire camera module floats on a multi-axis mechanical suspension or gimbal (e.g., vivo, ASUS ROG/Zenfone).
          //   • "Sensor-Shift Optical Image Stabilization"              → 9.00
          //     Definition: The image sensor itself physically moves (IBIS) instead of the lens (primarily found on Apple iPhones 12 Pro Max and newer).
          //   • "Lens-Based Optical Image Stabilization"                → 8.00
          //     Definition: Individual optical lens elements move to counteract shake. This is the default tier for generic "OIS" listings.
          //   • "Software-Only Stabilization (Electronic, no hardware)" → 5.00
          //     Definition: Purely algorithmic stabilization (EIS/AIS) via digital cropping; requires no moving physical parts.
          //   • "None"                                                  → 0.00
          //     Definition: No hardware or software stabilization is detected or documented.
          // AMBIGUITY RULE: If the spec sheet lists only "Optical Image Stabilization (OIS)" without further qualification (no mention of "sensor-shift" or "gimbal"), default to 8.00.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 8.00,
        // SCORING GUIDELINE: predicted_score directly inherits stabilization_type.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_5_ultrawide_capability": {
        // SCORING GOAL: Scores Ultrawide Camera Capability (UCC) as a composite of Field of View and sensor size, gated by the presence of an ultrawide lens.
        "presence": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": "N/A"
          // SCORING GUIDELINE: Binary gate. If value = false, the subscore is 0.00, the fields "source" and "exact_extract" must be "N/A" unless you find a source that explicitly states the device has no ultrawide lens, in that case "source" and "exact_extract" should reflect that finding. If value = true, then the subscore must be "N/A" and the scores will be calculated in the sections below.
        },
        "field_of_view_degrees": {
          "value": 120,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.78
          // SCORING GUIDELINE: Apply the Section 4.5.2 linear formula: Score = 10 × (field_of_view_degrees − Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max) / (Camera_Ultrawide_FOV_Deg_Max − Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max), clamped 0–10. Only evaluated if presence = true. If presence = false, then all fields of this block must be "N/A".
        },
        "ultrawide_sensor_size": {
          "value": "1/2.0",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 4.5.3 logarithmic formula: Score = 10 × (log(ultrawide_sensor_size) − log(Camera_Ultrawide_Sensor_Inch_Min)) / (log(Camera_Ultrawide_Sensor_Inch_Max) − log(Camera_Ultrawide_Sensor_Inch_Min)), clamped 0–10. Convert format string to decimal for the scoring formula (e.g., "1/2.0" → 0.5). Only evaluated if presence = true. If presence = false, then all fields of this block must be "N/A".
        },
        "predicted_score": 8.67,
        // SCORING GUIDELINE: predicted_score = (0.60 × field_of_view_degrees.subscore) + (0.40 × ultrawide_sensor_size.subscore) if presence = true; otherwise predicted_score = 0.00. Source: UCC Formula of Section 4.5.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.67,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_6_zoom_capability": {
        // SCORING GOAL: Scores optical zoom power. Only true optical magnification is counted; digital/crop zoom is excluded.
        "optical_zoom_x": {
          "value": 5,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 6.99
          // SCORING GUIDELINE: Apply the Section 4.6 logarithmic formula: Score = 10 × (log(optical_zoom_x) − log(Camera_Zoom_Optical_x_Min)) / (log(Camera_Zoom_Optical_x_Max) − log(Camera_Zoom_Optical_x_Min)), clamped 0–10.
        },
        "predicted_score": 6.99,
        // SCORING GUIDELINE: predicted_score directly inherits optical_zoom_x.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 6.99,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_7_macro_capability": {
        // SCORING GOAL: Scores Macro Capability & Close-Focus Performance (MCFP). Evaluates three hardware paths (Ultrawide, Telemacro, Dedicated Macro Lens). The final score is the maximum across all three paths.
        "4_7_1_ultrawide_path": {
          // SCORING GOAL (4.7.1): Groups the ultrawide lens macro capability via Autofocus (AF) and Minimum Focus Distance. Only evaluated if an ultrawide lens is present (see 4_5_ultrawide_capability.presence).
          "ultrawide_autofocus": {
            "value": "Autofocus",
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE (4.7.1.1): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. Use the following terms exclusively for "value" with related scores as subscore:
            //   • Autofocus    → 10.00
            //   • Fixed Focus  → 3.00
            //   If presence = false, "value" MUST be "Not present or not found", "source" and "exact_extract" must be set to "N/A", and "subscore" MUST be 0.00.
          },
          "min_focus_distance_cm": {
            "value": 2.5,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 7.31
            // SCORING GUIDELINE (4.7.1.2): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. Apply the Section 4.7.1.2 logarithmic formula: Score = 10 × (log(Camera_Macro_Dist_cm_Max) − log(distance)) / (log(Camera_Macro_Dist_cm_Max) − log(Camera_Macro_Dist_cm_Min)), clamped 0–10. If `4_5_ultrawide_capability.presence.value` = false, then all fields of this block must be "N/A".
          },
          "predicted_score": 8.39,
          // SCORING GUIDELINE: predicted_score (Source: *Formula for 4.7.1 Ultrawide Path:* Score_4.7.1) = (0.40 × ultrawide_autofocus.subscore) + (0.60 × min_focus_distance_cm.subscore) if `4_5_ultrawide_capability.presence.value` = true; otherwise 0.00.
          "final_score": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.39,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        },
        "4_7_2_telemacro_path": {
          // SCORING GOAL (4.7.2): Scores Telemacro (Telephoto Macro) capability. A telephoto macro lens enables close-up shots from a greater working distance (10–15 centimeters away), preventing the phone from casting a shadow and delivering natural background blur.
          "telemacro_presence": {
            "value": false,
            "source": "N/A",
            "exact_extract": "N/A",
            "subscore": 0.00
            // SCORING GUIDELINE: Binary gate. If value = false, the subscore is 0.00, the fields "source" and "exact_extract" must be "N/A" unless you find a source that explicitly states the device has no telemacro, in that case "source" and "exact_extract" should reflect that finding. If value = true, then the subscore must be "N/A" and the scores will be calculated in the sections below.
            // VERIFICATION RULE: Set to true only if specifications explicitly confirm "Macro telephoto", "floating elements", or list a focus distance between 5 centimeters and 30 centimeters for a specific telephoto lens.
          },
          "telemacro_optical_x": {
            "value": "N/A",
            "source": "N/A",
            "exact_extract": "N/A",
            "subscore": "N/A"
            // SCORING GUIDELINE: Only evaluated if telemacro_presence = true.
            // WHERE TO FIND IT: Look for the optical zoom of the specific telephoto lens with macro capability (e.g., "3× optical zoom", "5× periscope", "70 mm telephoto", etc.). If only millimeters focal length is provided, divide by main lens focal length (usually ~24 mm) to get the magnification. Example: a 70 mm telephoto on a phone with a 24 mm main = roughly 3×.
            // IMPORTANT: Only use the optical magnification of the lens with confirmed telemacro capability. If a phone has a 3× and a 5× telephoto but only the 3× supports macro focus, use 3×.
            // CALCULATION: Zoom_Score = 10 × (log(telemacro_optical_x) − log(Camera_Telemacro_x_Min)) / (log(Camera_Telemacro_x_Max) − log(Camera_Telemacro_x_Min)), clamped 0–10.
            // If telemacro_presence = false, then all fields of this block must be "N/A".
          },
          "telemacro_min_focus_distance_cm": {
            "value": "N/A",
            "source": "N/A",
            "exact_extract": "N/A",
            "subscore": "N/A"
            // SCORING GUIDELINE: Only evaluated if telemacro_presence = true.
            // WHERE TO FIND IT: Look for "minimum focus distance", "closest focus distance" or "macro focus from X cm" specifically for the telephoto lens.
            // CALCULATION: MFD_Score = 10 × (log(Camera_Telemacro_MFD_cm_Max) − log(telemacro_min_focus_distance_cm)) / (log(Camera_Telemacro_MFD_cm_Max) − log(Camera_Telemacro_MFD_cm_Min)), clamped 0–10.
            // If telemacro_presence = false, then all fields of this block must be "N/A".
          },
          "predicted_score": 0.00,
          // SCORING GUIDELINE: predicted_score (Score_4.7.2) = 0.00 if telemacro_presence = false; otherwise Score = 7.0 + 0.3 × (0.70 × telemacro_optical_x.subscore + 0.30 × telemacro_min_focus_distance_cm.subscore).
          "final_score": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 0.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        },
        "4_7_3_dedicated_path": {
          // SCORING GOAL (4.7.3): Scores a dedicated macro lens (a small fixed lens separate from the main/ultrawide/telephoto). Scores are capped at 3.00 to appropriately rank them below higher-quality macro implementations that use more capable primary or ultrawide sensors.
          "dedicated_macro_megapixels": {
            "value": 0,
            "source": "N/A",
            "exact_extract": "N/A",
            "subscore": 0.00
            // SCORING GUIDELINE: Apply the Section 4.7.3 linear formula: Score_4.7.3 = clamp(3.0 × dedicated_macro_megapixels / Camera_Dedicated_Macro_MP_Max, 0.00, 3.00). The score maps the Megapixels (MP) count linearly onto 0–3.00, where Camera_Dedicated_Macro_MP_Max scores 3.00. Values above Camera_Dedicated_Macro_MP_Max are capped at 3.00. A value of 0 MP means no dedicated macro lens (score = 0.00), in that case "source" and "exact_extract" must be "N/A" unless you find a source that explicitly states the device has no dedicated macro, in that case "source" and "exact_extract" should reflect that finding.
          },
          "predicted_score": 0.00,
          // SCORING GUIDELINE: predicted_score (Score_4.7.3) directly inherits dedicated_macro_megapixels.subscore.
          "final_score": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 0.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        },
        "predicted_score": 8.39,
        // SCORING GUIDELINE: predicted_score (MCFP Score) = Max(Score_4.7.1, Score_4.7.2, Score_4.7.3). The system evaluates all three paths independently and awards the score of the best-performing hardware implementation.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.39,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_8_rear_video_resolution": {
        // SCORING GOAL: Scores the maximum spatial resolution supported for rear-camera video recording.
        "maximum_resolution": {
          "value": "4K (Ultra HD)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the maximum rear video resolution. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "8K"                    → 10.00
          //   • "4K (Ultra HD)"         → 10.00
          //   • "1440p / QHD (2.5K)"    → 8.00
          //   • "1080p (Full HD)"       → 6.00
          //   • "720p (HD)"             → 3.00
          //   • "≤ 480p"                → 0.00
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits maximum_resolution.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_9_rear_video_frame_rate": {
        // SCORING GOAL: Scores the maximum standard frame rate achieved specifically at the device's highest supported resolution (as scored in Section 4.8), capped at 4K.
        "maximum_frames_per_second": {
          "value": 120,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the exact maximum Frames Per Second (FPS) supported at the resolution evaluated in Section "4_8_rear_video_resolution" capped at 4K. For example, if the device scored 8K in "4_8_rear_video_resolution", evaluate its 4K FPS instead. If the device scored 1080p in "4_8_rear_video_resolution", evaluate its 1080p FPS. Apply the Section 4.9 logarithmic formula: Score = 10 × (log(maximum_frames_per_second) − log(Camera_Video_FPS_Min)) / (log(Camera_Video_FPS_Max) − log(Camera_Video_FPS_Min)), clamped 0–10. Explicitly exclude any frame rates designated for "Slow Motion" or "High-Speed Burst" (e.g., 240fps+).
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits maximum_frames_per_second.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_10_video_hdr": {
        // SCORING GOAL: Scores which High Dynamic Range (HDR) video formats the camera system can record in. Dynamic HDR formats (Dolby Vision, HDR10+) optimize brightness and colour frame-by-frame for superior realism and grading headroom.
        "supported_formats": {
          "value": [
            "Dolby Vision",
            "HDR10"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the presence of officially supported High Dynamic Range (HDR) video recording formats. For each supported format, use its exact term below for the "value" array:
          //   • "HDR10" or "HLG"           → adds +5.00 to the subscore
          //   • "Dolby Vision"             → adds +3.00 to the subscore
          //   • "HDR10+"                   → adds +2.00 to the subscore
          // The subscore is the sum of these points (Clamped 0–10). If no HDR recording is supported (standard Standard Dynamic Range / SDR), leave the array empty [] and set subscore to 0.00.
        },
        "predicted_score": 8.00,
        // SCORING GUIDELINE: predicted_score directly inherits supported_formats.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_11_video_encoding": {
        // SCORING GOAL: Scores support for professional codecs and recording profiles as a composite index.
        "professional_codec_support": {
          "value": "Mezzanine",
          "value_details": {
            "True RAW": [],
            "Mezzanine": ["ProRes"],
            "Standard": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the highest supported professional recording codec tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "True RAW"    → 10.00
          //     Definition: Uncompressed or losslessly compressed raw video data with full sensor bit depth. Qualifying terms: CinemaDNG, Blackmagic RAW, ProRes RAW, Internal RAW.
          //   • "Mezzanine"   → 8.00
          //     Definition: High-bitrate intermediate production codecs with intra-frame compression. Qualifying terms: Apple ProRes 422 (HQ/Standard/LT/Proxy), Samsung Professional Video (ProRes), Xiaomi ProRes.
          //   • "Standard"    → 0.00
          //     Definition: Industry-standard distribution codecs (H.264/AVC, H.265/HEVC) without dedicated professional containers.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "log_color_profile_support": {
          "value": "True Log",
          "value_details": {
            "True Log": ["Apple Log"],
            "Flat / Cine": [],
            "Standard only": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the supported log profiles. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "True Log"       → 10.00
          //     Definition: Logarithmic gamma curve for professional grading (e.g., Apple Log, S-Log3, D-Log).
          //   • "Flat / Cine"    → 5.00
          //     Definition: Desaturated profiles that are not mathematically logarithmic (e.g., S-Cinetone, D-Cinelike).
          //   • "Standard only"  → 0.00
          //     Definition: No professional gamma profiles; only standard rec.709 or rec.2020 curves.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "color_bit_depth": {
          "value": "10-bit color",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 5.00
          // SCORING GUIDELINE: Use the following exact same terms for "value" with related scores for "subscore": "12-bit color" (score 10.00), "10-bit color" (score 5.00), or "8-bit color" (score 0.00).
        },
        "predicted_score": 7.95,
        // SCORING GUIDELINE: predicted_score = (0.40 × professional_codec_support.subscore) + (0.35 × log_color_profile_support.subscore) + (0.25 × color_bit_depth.subscore).
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.95,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_12_slow_motion": {
        // SCORING GOAL: Scores the ability to capture video at very high frame rates in a dedicated "Slow Motion" mode based on maximum data throughput, expressed in Megapixels per second (MP/s).
        "supported_modes": {
          "value": [
            {
              "resolution_megapixels": 2.07,
              "frames_per_second": 960
            },
            {
              "resolution_megapixels": 8.29,
              "frames_per_second": 120
            }
          ],
          "source": "TBD",
          "exact_extract": "Proof pending"
          // SCORING GUIDELINE: Enter all Resolution/Frames per Second(FPS) pairs explicitly listed in the device's secondary video specifications under marketing terms like "Slow Motion" or "High Speed Video" (Do NOT use standard video resolutions). Calculate MP/s (Resolution × FPS) for each pair and place the combination yielding the absolute highest MP/s in the VERY FIRST position of this array. If no dedicated slow-motion mode exists, leave the array empty [].
        },
        "predicted_score": 8.55,
        // SCORING GUIDELINE: Use the first item in `supported_modes.value` (the highest MP/s pair) to calculate MP_s = resolution_megapixels × frames_per_second. Apply the Section 4.12 logarithmic formula: predicted_score = 10 × (log(MP_s) − log(Camera_SlowMo_MPs_Min)) / (log(Camera_SlowMo_MPs_Max) − log(Camera_SlowMo_MPs_Min)), clamped 0–10. If the array is empty, set predicted_score to 0.00.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.55,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_13_front_camera_resolution": {
        // SCORING GOAL: Scores the spatial resolution of the front-facing camera.
        "megapixels": {
          "value": 12,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 4.72,
        // SCORING GUIDELINE: Mirroring Section 4.3 (Main Camera Resolution). Apply the Section 4.13 logarithmic formula: Score = 10 × (log(megapixels) − log(Camera_Front_Resolution_MP_Min)) / (log(Camera_Front_Resolution_MP_Max) − log(Camera_Front_Resolution_MP_Min)), clamped 0–10.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 4.72,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_14_front_camera_focus": {
        // SCORING GOAL: Scores the ability of the front-facing camera to maintain sharp focus.
        "aperture_f_number": {
          "value": 2.2,
          "source": "TBD",
          "exact_extract": "Proof pending"
          // DATA GUIDELINE: Identify the Aperture f-number of the front camera. This is the numerical part of the fraction (e.g., 2.2 for f/2.2).
        },
        "sensor_size": {
          "value": "1/3",
          "source": "TBD",
          "exact_extract": "Proof pending"
          // DATA GUIDELINE: Identify the sensor size fraction (e.g., "1/3", "1/3.1", "1/4").
        },
        "focus_system_tier": {
          "value": "Autofocus",
          "value_details": {
            "Autofocus": ["Phase Detection Auto Focus (PDAF)"],
            "Fixed Focus (Modern Wide-DOF)": [],
            "Fixed Focus (Legacy Narrow-DOF)": [],
            "No Front Camera": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the front camera's focus type. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Autofocus"                        → 10.00
          //     Definition: An active mechanical system where the lens moves to find focus (e.g., Phase Detection Auto Focus (PDAF), Dual Pixel, or Laser Auto Focus).
          //   • "Fixed Focus (Modern Wide-DOF)"    → 6.00
          //     Definition: A lens with no moving hardware parts configured for a wide Depth of Field (DOF) focus zone. Identified by (aperture_f_number ≥ 2.0) OR (sensor_size ≤ 1/3").
          //   • "Fixed Focus (Legacy Narrow-DOF)"  → 3.00
          //     Definition: A lens with no moving hardware parts featuring a narrow Depth of Field (DOF) focus zone. Identified by (aperture_f_number < 2.0) AND (sensor_size > 1/3").
          //   • "No Front Camera"                  → 0.00
          //     Definition: Device lacks a front-facing selfie camera module.
          // AMBIGUITY RESOLUTION: Focus Zone width is determined by Depth of Field (DOF). If sensor size data is missing, classify based solely on the aperture (f-number) if it is known.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits focus_system_tier.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_15_front_camera_video": {
        // SCORING GOAL: Scores maximum video capture capability (resolution, frame rate, High Dynamic Range (HDR), and Professional Recording) of the front camera as a composite score.
        "4_15_1_video_resolution": {
          "maximum_resolution": {
            "value": "4K (Ultra HD)",
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.8 (Rear Video Resolution). Identify the maximum front video resolution. Use the following exact Tier Names for "value" with related scores as subscore:
            //     "8K"                      10.00
            //     "4K (Ultra HD)"           10.00
            //     "1440p / QHD (2.5K)"      8.00
            //     "1080p (Full HD)"         6.00
            //     "720p (HD)"               3.00
            //     "≤480p"                   0.00
          }
        },
        "4_15_2_video_frame_rate": {
          "maximum_frames_per_second": {
            "value": 60,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.9 (Rear Video Frame Rate). Identify the maximum Frames per second (FPS) specifically at the resolution listed in "4_15_1_video_resolution.maximum_resolution", capped at 4K. For example, if the device scored 8K in "4_15_1_video_resolution", evaluate its 4K FPS instead. If the device scored 1080p in "4_15_1_video_resolution", evaluate its 1080p FPS. Apply the Section 4.15.2 logarithmic formula: FPSScore = 10 × (log(maximum_frames_per_second) − log(Camera_Front_Video_FPS_Min)) / (log(Camera_Front_Video_FPS_Max) − log(Camera_Front_Video_FPS_Min)), clamped 0–10.
          }
        },
        "4_15_3_video_hdr": {
          "supported_formats": {
            "value": [
              "HDR10",
              "Dolby Vision",
              "HDR10+"
            ],
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.10 (Rear Video HDR). Identify the presence of officially supported High Dynamic Range (HDR) video recording formats. For each supported format, use its exact term below for the "value" array:
            //   • "HDR10" or "HLG"           → adds +5.00 to the subscore
            //   • "Dolby Vision"             → adds +3.00 to the subscore
            //   • "HDR10+"                   → adds +2.00 to the subscore
            // The subscore is the sum of these points (Clamped 0–10). If no HDR recording is supported (standard Standard Dynamic Range / SDR), leave the array empty [] and set subscore to 0.00.
          }
        },
        "4_15_4_1_professional_codec_support": {
          "supported_codecs": {
            "value": "Mezzanine",
            "value_details": {
              "True RAW": [],
              "Mezzanine": ["ProRes"],
              "Standard": []
            },
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 8.00
          // SCORING GUIDELINE: Mirroring Section 4.11.1 (PCS). Identify the highest supported professional recording codec tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "True RAW"    → 10.00
          //     Definition: Uncompressed or losslessly compressed raw video data with full sensor bit depth. Qualifying terms: CinemaDNG, Blackmagic RAW, ProRes RAW, Internal RAW.
          //   • "Mezzanine"   → 8.00
          //     Definition: High-bitrate intermediate production codecs with intra-frame compression. Qualifying terms: Apple ProRes 422 (HQ/Standard/LT/Proxy), Samsung Professional Video (ProRes), Xiaomi ProRes.
          //   • "Standard"    → 0.00
          //     Definition: Industry-standard distribution codecs (H.264/AVC, H.265/HEVC) without dedicated professional containers.
          // VALUE_DETAILS GUIDELINE: List all specific supported professional codecs found in specs. Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
          }
        },
        "4_15_4_2_log_color_profile_support": {
          "supported_profiles": {
            "value": "True Log",
            "value_details": {
              "True Log": ["Apple Log"],
              "Flat / Cine": [],
              "Standard only": []
            },
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.11.2 (LCP). Identify the supported log profiles. Use the following exact Tier Names for "value" with related scores as subscore:
            //   • "True Log"       → 10.00
            //     Definition: Logarithmic gamma curve for professional grading (e.g., Apple Log, S-Log3, D-Log).
            //   • "Flat / Cine"    → 5.00
            //     Definition: Desaturated profiles that are not mathematically logarithmic (e.g., S-Cinetone, Cinelike-D).
            //   • "Standard only"  → 0.00
            //     Definition: No professional gamma profiles. only standard rec.709 or rec.2020 curves.
            // VALUE_DETAILS GUIDELINE: List all specific supported log/flat profiles found in specs. Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
          }
        },
        "predicted_score": 9.80,
        // SCORING GUIDELINE: calculated_professional_score = (0.50 * 4_15_4_1_professional_codec_support.supported_codecs.subscore) + (0.50 * 4_15_4_2_log_color_profile_support.supported_profiles.subscore).
        // final_composite_predicted_score = (0.35 × 4_15_1_video_resolution.maximum_resolution.subscore) + (0.25 × 4_15_2_video_frame_rate.maximum_frames_per_second.subscore) + (0.20 × 4_15_3_video_hdr.supported_formats.subscore) + (0.20 × calculated_professional_score).
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 9.80,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_16_multiframe_photo": {
        // SCORING GOAL: Scores camera system's automatic multi-frame capture and stacking capabilities. 
        "processing_tier": {
          "value": "Advanced Semantic & Neural Stacking",
          "value_details": {
            "Advanced Semantic & Neural Stacking": ["Deep Fusion", "Photonic Engine"],
            "Standard Always-on Multi-Frame HDR": ["Smart HDR 5"],
            "Conditional / Manual Multi-Frame": [],
            "Basic / Single Frame (Legacy)": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the Multi-Frame Computational Photography (MFCP) tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Advanced Semantic & Neural Stacking" → 10.0
          //     Definition: Advanced pipeline that uses semantic segmentation (understanding sky, faces, skin) within a Zero Shutter Lag (ZSL) multi-frame buffer.
          //   • "Standard Always-on Multi-Frame HDR"  → 7.5
          //     Definition: Always-on multi-frame HDR capture (e.g., Smart HDR) without advanced per-pixel semantic segmentation.
          //   • "Conditional / Manual Multi-Frame"    → 5.0
          //     Definition: Multi-frame processing only activates in specific modes (e.g., Night Mode) or requires manual activation (HDR toggle).
          //   • "Basic / Single Frame (Legacy)"       → 0.0
          //     Definition: No multi-frame stacking; reliance on single-frame exposure.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Advanced Semantic & Neural Stacking": ["Photonic Engine", "Deep Fusion"], "Standard Always-on Multi-Frame HDR": ["Smart HDR 5"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits processing_tier.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_17_pipeline_semantic_ai": {
        // SCORING GOAL: Automatic Capture-Time AI. Scores the ability of the software to segment scenes and subjects using Artificial Intelligence (AI).
        "capability_tier": {
          "value": "Neural Semantic Segmentation",
          "value_details": {
            "Neural Semantic Segmentation": ["AI ProVisual Engine", "Object-aware engine"],
            "Object-Based Optimization": [],
            "Basic Metadata AI": [],
            "None": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the Pipeline AI tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Neural Semantic Segmentation" → 10.0
          //     Definition: Real-time, pixel-level differentiation between multiple semantic categories (skin, sky, hair, eyes, teeth) during captured multi-frame pipeline.
          //   • "Object-Based Optimization"   → 7.5
          //     Definition: Recognizes high-level subjects (dog, flower, sunset) to apply preset global/local enhancements ("Scene Optimizer").
          //   • "Basic Metadata AI"           → 4.0
          //     Definition: Basic subject prioritization for focus and exposure (Face/Eye detection). No content-aware color science.
          //   • "None"                        → 0.0
          //     Definition: No scene or subject interpretation in the processing pipeline.    
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier Name": ["Marketing Name 1", "Marketing Name 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits capability_tier.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "4_18_post_capture_generative_ai": {
        // SCORING GOAL: User-Initiated Gallery-Time Artificial Intelligence (AI). Scores the ability to modify images after capture using AI tools.
        "feature_tier": {
          "value": "Generative Content Transformation",
          "value_details": {
            "Generative Content Transformation": ["Magic Editor", "Best Take"],
            "Advanced Semantic Edits": [],
            "Basic Algorithmic Fixes": [],
            "None": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the Generative AI tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Generative Content Transformation" → 10.0
          //     Definition: Advanced on-device or cloud-based generative AI that can add, remove, move, or transform objects within an image with pixel-accurate context awareness.
          //   • "Advanced Semantic Edits"           → 7.50
          //     Definition: Rule-based or shallow-learning tools for localized adjustments (shadow/reflection removal, face unblur, object erasure without generative fill).
          //   • "Basic Algorithmic Fixes"           → 4.00
          //     Definition: Standard beauty filters, color-aware auto-fixing, or basic object prioritization for cropping.
          //   • "None"                              → 0.0
          //     Definition: No AI-enhanced editing tools beyond standard gallery filters.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Generative Content Transformation": ["Generative Edit", "Magic Editor"], "Advanced Semantic Edits": ["Clean Up", "AI Eraser 2.0"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits feature_tier.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "5_software_and_longevity": {
      "operating_system_version": {
        // GUIDELINE: The operating system and version shipped with the device.
        "value": "Android 14",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "skin": {
        // SCORING GUIDELINE: Record the exact OEM skin / platform name as declared by the manufacturer. Section 5.2 uses this for scoring. Known platforms include iOS, Pixel UI / Stock Android, Samsung One UI, HyperOS (Xiaomi), etc.
        "value": "One UI 6.1",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "5_1_support_longevity": {
        // SCORING GOAL: Scores the manufacturer's update policy commitment length.
        "years_operating_system": {
          "value": 7,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "years_security": {
          "value": 7,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 5.1 logarithmic formula: Score = 10 × (log(years) − log(Support_Years_Min)) / (log(Support_Years_Max) − log(Support_Years_Min)), clamped 0–10. Use the maximum committed years (OS or security) as the "years" variable.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits years_security.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "5_2_system_cleanliness_control": {
        // SCORING GOAL: Evaluates the out-of-box software experience (bloatware, user control, ads) derived from the platform/skin.
        "platform_score": {
          "value": "Tier 3: Moderate",
          "value_details": {
            "Tier 1: Clean / Premium": [],
            "Tier 2: Controlled": [],
            "Tier 3: Moderate": ["One UI"],
            "Tier 4: Heavy / Bloated": [],
            "Tier 5: Restrictive": []
          },
          "source": "N/A",
          "exact_extract": "N/A",
          "subscore": 6.00
          // SCORING GUIDELINE: Identify the software platform tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Tier 1: Clean / Premium" → 10.0
          //     Definition: Minimalist experience with no third-party bloatware or ads (e.g., iOS, Pixel UI, Nothing OS).
          //   • "Tier 2: Controlled"       → 8.0
          //     Definition: Light skin with minimal, removable bloatware (e.g., Motorola, OxygenOS).
          //   • "Tier 3: Moderate"         → 6.0
          //     Definition: Notable bloatware and removable third-party apps (e.g., One UI).
          //   • "Tier 4: Heavy / Bloated"  → 4.0
          //     Definition: Significant bloatware and system-level advertisements (e.g., HyperOS, ColorOS).
          //   • "Tier 5: Restrictive"      → 0.0
          //     Definition: Extreme bloatware and non-optional system ads (e.g., HiOS, XOS).
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Tier 1: Clean / Premium": ["iOS"], "Tier 3: Moderate": ["One UI"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 6.00,
        // SCORING GUIDELINE: predicted_score directly inherits platform_score.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 6.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "5_3_ai_feature_suite": {
        // SCORING GOAL: Evaluates the specific AI software features available. Score is calculated using weighted binary features. Max score is 10.00.
        "visual_screen_search": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.50
          // SCORING GUIDELINE: If value = true, subscore = 2.50. If value = false, subscore = 0.00.
          // Definition: A system-level visual search tool activated by circling, highlighting, or long-pressing any on-screen content (text, image, product). The phone identifies the item and returns relevant search results, shopping links, or translations without leaving the current app.
        },
        "live_speech_translation": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If value = true, subscore = 2.00. If value = false, subscore = 0.00.
          // Definition: Real-time voice or text translation during phone calls, video calls, or in-person conversations. Must operate as a native system service (not a standalone third-party app download).
        },
        "content_summarization": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.50
          // SCORING GUIDELINE: If value = true, subscore = 1.50. If value = false, subscore = 0.00.
          // Definition: A system-integrated Artificial Intelligence (AI) feature that condenses long-form content (web pages, articles, recorded voice memos, notification threads) into a short summary. Must be built into the operating system or first-party apps, not a third-party add-on.
        },
        "writing_tools": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.00
          // SCORING GUIDELINE: If value = true, subscore = 1.00. If value = false, subscore = 0.00.
          // Definition: System-wide AI text rewriting, tone adjustment, grammar correction, or proofreading available in any text input field. Must be an operating-system-level feature accessible across all apps.
        },
        "on_device_processing": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 3.00
          // SCORING GUIDELINE: If value = true, subscore = 3.00. If value = false, subscore = 0.00.
          // Definition: The device can run its core AI features (at least summarisation and writing tools) locally on the Neural Processing Unit (NPU) without requiring a cloud/internet connection. Provides privacy, lower latency, and offline reliability.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score is the sum of all subscores in this block (visual_screen_search + live_speech_translation + content_summarization + writing_tools + on_device_processing).
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "6_processing_power_and_performance": {
      "system_on_chip_name": {
        "value": "Snapdragon 8 Gen 3",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "6_1_0_system_on_chip_reference": {
        "cortex_x4": {
          "count": 1,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "cortex_a720": {
          "count": 5,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "cortex_a520": {
          "count": 2,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "6_1_cpu_multi_core_performance": {
        "geekbench_6_multi_score": {
          "value": 7200,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "scoring_components": {
          "frequency_adjusted_core_score": [
            {
              "name": "Cortex-X4",
              "value": 10.00,
              "description": "Frequency-Adjusted Core Score"
            },
            {
              "name": "Cortex-A720",
              "value": 39.90,
              "description": "Frequency-Adjusted Core Score"
            },
            {
              "name": "Cortex-A520",
              "value": 4.60,
              "description": "Frequency-Adjusted Core Score"
            }
          ]
        },
        "predicted_score": 0.00,
        "final_score": 0.00
      },
      "6_2_cpu_architecture_single_core": {
        "geekbench_6_single_score": {
          "value": 2200,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "scoring_components": {
          "core_architecture_score": {
            "value": 10.00,
            "description": "Core Architecture Score - strongest core"
          },
          "frequency_scaling_factor": {
            "value": 1.03,
            "description": "Frequency Scaling Factor",
            "actual_frequency_ghz": {
              "value": 3.4,
              "source": "TBD",
              "exact_extract": "Proof pending"
              // SCORING GUIDELINE: Identify the core performance tier based on the strongest core. Use the following exact Tier Names for "value" with related scores as subscore:
              //   • "Ultra Performance" → 10.00
              //     Definition: Cutting-edge microarchitecture with peak instruction-per-clock (IPC) performance (e.g., Apple A18 Pro, Cortex-X925).
              //   • "High Performance"  → 8.50
              //     Definition: Flagship-class performance cores from recent generations (e.g., Cortex-X4, Apple A17).
              //   • "Mid-tier"          → 6.00
              //     Definition: Balanced efficiency/performance cores (e.g., Cortex-A720, Apple A15).
              //   • "Basic"             → 3.00
              //     Definition: Efficiency-focused cores for standard tasks (e.g., Cortex-A520).
              //   • "Legacy / Ultra Low"→ 1.00
              //     Definition: Outdated or ultra-low power cores (e.g., Cortex-A55).
            }
          }
        },
        "predicted_score": 0.00,
        "final_score": 0.00
      },
      "6_3_0_graphics_processing_unit_architecture_reference": {
        "graphics_processing_unit_model": {
          "value": "Adreno 750",
          "source": "TBD",
          "exact_extract": "Proof pending"
          // SCORING GUIDELINE: Record the exact GPU model name as listed on GSMArena under "Chipset".
          //   Then look up the Standard Graphics, Ray Tracing, Ref Freq, and Efficiency scores
          //   in the Section 6.3.0 table. Known GPU models (add to Section 6.3.0 if unlisted):
          //   Immortalis-G720 MC12 · Adreno 750 · Xclipse 940 · Adreno 740 · Immortalis-G715 MC11
          //   Apple GPU (A18 Pro) · Apple GPU (A17 Pro) · Apple GPU (A16 Bionic) · Adreno 730
          //   Mali-G715 MC9 · Xclipse 920 · Mali-G710 MC10 · Adreno 660 · Mali-G715 (Tensor G3)
          //   Mali-G715 MC7 · Apple GPU (A15 Bionic) · Adreno 650 · Adreno 642L · Mali-G610 MC6
          //   Mali-G77 MC9 · Apple GPU (A14 Bionic) · Adreno 640 · Mali-G610 MC4 · Adreno 620
          //   Adreno 619 · Mali-G68 MC4 · Adreno 618 · Mali-G57 MC3 · Adreno 610 · Mali-G57 MC2
          //   Mali-G52 MP2 · PowerVR GE8320
        },
        "standard_graphics_score": {
          "value": 10.00,
          "description": "Section 6.3.0 Standard Graphics Score"
        },
        "ray_tracing_score": {
          "value": 10.00,
          "description": "Section 6.3.0 Ray Tracing Score"
        },
        "efficiency_score": {
          "value": 10.00,
          "description": "Section 6.3.0 Efficiency Score"
        }
      },
      "6_3_graphics_processing_unit_performance": {
        // SCORING GOAL: Scores raw GPU compute capability using standard graphics tasks and hardware ray tracing.
        "3d_mark_steel_nomad_light_score": {
          "value": 1850,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 6.3 Part 1 formula: SGS_Bench = 10 × (log(Score) − log(GPU_SteelNomad_Score_Min)) / (log(GPU_SteelNomad_Score_Max) − log(GPU_SteelNomad_Score_Min))
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score = (SGS × 0.9) + (RTS × 0.1). SGS is derived either from Benchmark (Method A) or 6.3.0 table (Method C). RTS is unconditionally derived from 6.3.0 table.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "6_4_ai_hardware_performance": {
        // SCORING GOAL: Evaluates the Neural Processing Unit (NPU) speed.
        "geekbench_ai_quantized_score": {
          "value": 6000,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 6.4 logarithmic formula based on Geekbench AI Quantized score.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits geekbench_ai_quantized_score.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "6_5_ram_technology": {
        // SCORING GOAL: Evaluates RAM type efficiency and bandwidth.
        "technology_generation": {
          "value": "LPDDR5X",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the RAM technology. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "LPDDR5X"      → 10.00
          //     Definition: Highest speed tier (e.g., LPDDR5X).
          //   • "LPDDR5 / 4X"  → 7.00
          //     Definition: Standard modern memory (e.g., LPDDR5, LPDDR4X).
          //   • "Legacy"       → 0.00
          //     Definition: LPDDR3 or older technology.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits technology_generation.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "6_6_ram_capacity": {
        // SCORING GOAL: Evaluates total system RAM capacity.
        "capacity_gb": {
          "value_path": "identity.hardware_configuration.ram_gb.value",
          "value": 12,
          "subscore": 8.00
          // SCORING GUIDELINE: Apply Section 6.6 logarithmic formula. Score = 10 * (log(GB) - log(RAM_GB_Min)) / (log(RAM_GB_Max) - log(RAM_GB_Min)).
        },
        "predicted_score": 8.00,
        // SCORING GUIDELINE: predicted_score directly inherits capacity_gb.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "6_7_storage_technology": {
        // SCORING GOAL: Evaluates internal storage format efficiency and read/write speeds.
        "storage_format": {
          "value": "UFS 4.0",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the internal storage technology. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "UFS 4.0 / NVMe" → 10.00
          //     Definition: Highest speed tier (e.g., UFS 4.0, Apple NVMe).
          //   • "UFS 3.1"        → 8.00
          //     Definition: High-speed standard (e.g., UFS 3.1).
          //   • "UFS 2.2 / eMMC" → 0.00
          //     Definition: Legacy or budget storage (e.g., UFS 2.2, eMMC 5.1).
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits storage_format.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "6_8_storage_capacity": {
        // SCORING GOAL: Evaluates maximum internal storage capacity.
        "capacity_gb": {
          "value_path": "identity.hardware_configuration.storage_gb.value",
          "value": 512,
          "subscore": 8.00
          // SCORING GUIDELINE: Apply Section 6.8 logarithmic formula. Score = 10 * (log(GB) - log(Storage_GB_Min)) / (log(Storage_GB_Max) - log(Storage_GB_Min)).
        },
        "predicted_score": 8.00,
        // SCORING GUIDELINE: predicted_score directly inherits capacity_gb.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "6_9_storage_expandability": {
        // SCORING GOAL: Evaluates if SD Card expansion is supported.
        "expandability_support": {
          "value": "No SD Card slot",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.00
          // SCORING GUIDELINE: Identify the expandability support. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Dedicated Slot" → 10.00
          //     Definition: Separate tray or contact specifically for a removable memory card (MicroSD) that does not interfere with SIM card usage.
          //   • "Hybrid Slot"    → 7.00
          //     Definition: Shared slot where the user must choose between a second SIM card or a memory card (e.g., MicroSD, Nano Memory).
          //   • "Proprietary"    → 5.00
          //     Definition: Support for branded/exclusive removable storage formats (e.g., Huawei NM Card).
          //   • "None"           → 0.00
          //     Definition: No physical slot for internal storage expansion.
        },
        "predicted_score": 0.00,
        // SCORING GUIDELINE: predicted_score directly inherits expandability_support.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 0.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "6_10_thermal_dissipation_stability": {
        // SCORING GOAL: Evaluates thermal cooling capability based on frame architecture, weight, surface area, and active/passive cooling system.
        "part_b_cooling_system_class": {
          "value": "Large Vapor Chamber (≥4000 mm²)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the cooling mechanism class. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Active Cooling (Fan)"              → 10.00
          //     Definition: Internal motorized fan pushing air through the chassis for heat dissipation.
          //   • "Extreme Passive (VC ≥4000 mm²)"    → 8.00
          //     Definition: Vapor Chamber cooling with a verified surface area of 4000 square millimeters or more.
          //   • "Standard Passive (VC <4000 mm²)"   → 7.00
          //     Definition: Presence of a Vapor Chamber (VC) cooling system that is smaller or of unspecified area.
          //   • "Basic Passive (Multi-layer Graphite)" → 5.00
          //     Definition: Use of graphite sheets or copper foil for heat spreading without a phase-change vapor chamber.
          //   • "Legacy (Metal Shielding only)"     → 3.00
          //     Definition: Reliance on standard chassis metal and shielding for heat.
          //   • "None / Air-only"                   → 0.00
          //     Definition: No dedicated internal thermal dissipation materials or structures mentioned.
        },
        "part_c_process_node_size_nm": {
          "value": 4,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Process Node Score calculated via Section 6.10 Part C Node Score formula.
        },
        "part_c_foundry": {
          "value": "TSMC",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Foundry Score via Section 6.10 Part C Foundry efficiency table (TSMC=10, Samsung=5, Others=0).
        },
        "predicted_score": 9.50,
        // SCORING GUIDELINE: predicted_score calculated using Physical Score and Peak Thermal Demand Compensation from Section 6.10.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 9.50,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "7_connectivity_and_sensors": {
      "7_1_cellular_capabilities": {
        // SCORING GOAL: Evaluates max cellular network standards.
        "network_technology": {
          "value": "5G mmWave + Sub-6 (Global band coverage)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the highest cellular technology supported. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "5G mmWave + Sub-6 (Global band coverage)" → 10.00
          //     Definition: Supports both mmWave (high frequency, short range) and Sub-6 (lower frequency, long range) 5G spectrums, covering all major global frequency bands.
          //   • "5G Sub-6 (Global band coverage)"          → 8.50
          //     Definition: Supports 5G on Sub-6GHz frequencies with extensive band coverage for global roaming.
          //   • "5G Sub-6 (Regional band coverage)"        → 7.50
          //     Definition: Supports 5G on Sub-6GHz but with band coverage limited to specific markets.
          //   • "4G LTE-A (Cat 24+)"                       → 5.00
          //     Definition: 4G LTE Advanced with support for high-order carrier aggregation and 4x4 MIMO.
          //   • "4G LTE"                                   → 2.50
          //     Definition: Standard 4G Long-Term Evolution without advanced carrier aggregation.
          //   • "3G / Legacy"                              → 0.00
          //     Definition: Limited to 3G (UMTS/HSPA) or older technologies.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits network_technology.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_2_sim_capabilities": {
        // SCORING GOAL: Evaluates subscriber identity module format support.
        "sim_configuration": {
          "value": "Dual eSIM / iSIM + Physical Nano-SIM Slot",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the SIM configuration. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Tier 1: Dual eSIM / iSIM + Physical Slot" → 10.00
          //     Definition: Supports two or more active eSIM profiles/integrated SIM alongside a physical Nano-SIM slot.
          //   • "Tier 2: eSIM + Physical Slot"              → 8.00
          //     Definition: Supports one active eSIM profile alongside a physical Nano-SIM slot.
          //   • "Tier 3: Dual Physical Nano-SIM Only"       → 6.00
          //     Definition: Two physical Nano-SIM slots; no electronic/programmable SIM support.
          //   • "Tier 4: Single Physical Nano-SIM Only"     → 4.00
          //     Definition: Only one physical Nano-SIM slot; no dual-SIM or eSIM support.
          //   • "None"                                      → 0.00
          //     Definition: No cellular SIM capability (e.g., tablet/media player without modem).
          // VALUE_DETAILS GUIDELINE: Record the exact OEM marketing name for SIM support (e.g., ["Dual eSIM"], ["Dual SIM (Nano-SIM, dual stand-by)"]).
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits sim_configuration.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_3_wifi_standard": {
        // SCORING GOAL: Evaluates Wi-Fi network standards.
        "standard": {
          "value": "Wi-Fi 7",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the highest supported Wi-Fi standard. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Wi-Fi 7"   → 10.00
          //     Definition: 802.11be standard (Extremely High Throughput). Supports 320 MHz channels, 4K QAM, and Multi-Link Operation (MLO).
          //   • "Wi-Fi 6E"  → 8.00
          //     Definition: 802.11ax standard adding support for the 6GHz spectrum, reducing congestion.
          //   • "Wi-Fi 6"   → 6.00
          //     Definition: 802.11ax standard on 2.4/5GHz. Improved efficiency and performance in dense environments.
          //   • "Wi-Fi 5"   → 3.00
          //     Definition: 802.11ac standard.
          //   • "Legacy"    → 0.00
          //     Definition: 802.11n (Wi-Fi 4) or older technology.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits standard.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_4_bluetooth_and_audio_codecs": {
        // SCORING GOAL: Evaluates Bluetooth version and high-fidelity audio codec support.
        "bluetooth_version": {
          "value": 5.3,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 4.50
          // SCORING GUIDELINE: Identify the Bluetooth version. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • 5.4      → 5.00
          //     Definition: Latest standard with Periodic Advertising with Responses (PAwR) and Encrypted Advertising Data.
          //   • 5.3      → 4.50
          //     Definition: Improved encryption, connection reliability, and efficiency.
          //   • 5.2      → 3.50
          //     Definition: Introduces LE Audio and Enhanced Attribute Protocol (EATT).
          //   • 5.1 / 5.0 → 2.50
          //     Definition: Basic Bluetooth 5 standards.
          //   • 4.2      → 1.00
          //     Definition: Legacy Bluetooth 4 standards.
          //   • < 4.2    → 0.00
          //     Definition: Obsolete Bluetooth standards.
        },
        "highest_codec_supported": {
          "value": "High-Res",
          "value_details": {
            "Lossless": [],
            "High-Res": ["LDAC", "aptX HD"],
            "Standard": ["AAC", "SBC"]
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 4.00
          // SCORING GUIDELINE: Identify the highest supported Bluetooth audio codec tier. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Lossless"   → 5.00
          //     Definition: CD-quality audio without data loss over Bluetooth. Qualifying terms: aptX Lossless.
          //   • "High-Res"   → 4.00
          //     Definition: Near-lossless or high-bitrate codecs (up to 990kbps). Qualifying terms: LDAC, aptX Adaptive, aptX HD, LHDC.
          //   • "Standard"   → 1.50
          //     Definition: Basic distribution codecs with significant compression. Qualifying terms: AAC, SBC.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"Lossless": ["aptX Lossless"], "High-Res": ["LDAC", "aptX HD"], "Standard": ["AAC", "SBC"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 8.50,
        // SCORING GUIDELINE: predicted_score = bluetooth_version.subscore + highest_codec_supported.subscore (Max 10.0).
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.50,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_5_biometrics": {
        // SCORING GOAL: Evaluates secure unlock mechanisms.
        "best_technology": {
          "value": "Ultrasonic FP",
          "value_details": {
            "3D Face / Sonic Gen 2": [],
            "Ultrasonic FP": ["Qualcomm 3D Sonic Gen 2"],
            "Optical FP / 2D Face": [],
            "Capacitive FP": [],
            "None / Pin Only": []
          },
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the most secure/advanced available biometric unlock method. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "3D Face / Sonic Gen 2"  → 10.00
          //     Definition: Secure 3D facial recognition (e.g., Face ID) or 2nd-gen Ultrasonic fingerprint sensors (large area, fast).
          //   • "Ultrasonic FP"          → 8.00
          //     Definition: Standard ultrasonic fingerprint sensors (3D mapping of the finger via sound waves).
          //   • "Optical FP / 2D Face"  → 6.00
          //     Definition: Standard optical fingerprint sensors (2D photograph of the finger) or basic 2D webcam-style face unlock (non-secure for payments).
          //   • "Capacitive FP"          → 4.00
          //     Definition: Physical button-integrated fingerprint sensors (side-mounted or rear-mounted).
          //   • "None / Pin Only"        → 0.00
          //     Definition: No biometric sensors; reliance on PIN, pattern, or password.
          // VALUE_DETAILS GUIDELINE: Dictionary where keys are Tier Names and values are arrays of strings (e.g., {"3D Face / Sonic Gen 2": ["Face ID"], "Ultrasonic FP": ["Qualcomm 3D Sonic Gen 2"]}). IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "predicted_score": 8.00,
        // SCORING GUIDELINE: predicted_score directly inherits best_technology.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_6_sensors": {
        // SCORING GOAL: Evaluates navigation and accessory sensors.
        "core_sensor_suite": {
          "accelerometer": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 1.00
            // SCORING GUIDELINE: If true, 1.00; false, 0.00.
          },
          "gyroscope": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 1.50
            // SCORING GUIDELINE: If true, 1.50; false, 0.00.
          },
          "magnetometer": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 1.00
            // SCORING GUIDELINE: If true, 1.00; false, 0.00.
          },
          "proximity_sensor": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 0.75
            // SCORING GUIDELINE: If true, 0.75; false, 0.00.
          },
          "ambient_light_sensor": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 0.75
            // SCORING GUIDELINE: If true, 0.75; false, 0.00.
          }
        },
        "advanced_sensor_capabilities": {
          "barometer": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 1.50
            // SCORING GUIDELINE: If true, 1.50; false, 0.00.
          },
          "lidar_tof_3d_depth_sensor": {
            "value": false,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 0.00
            // SCORING GUIDELINE: If true, 2.00; false, 0.00.
          },
          "color_spectrum_flicker_sensor": {
            "value": false,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 0.00
            // SCORING GUIDELINE: If true, 1.50; false, 0.00.
          }
        },
        "predicted_score": 6.50,
        // SCORING GUIDELINE: predicted_score is sum of core_sensor_suite + advanced_sensor_capabilities subscores (Max 10.0).
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 6.50,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_7_nfc_and_uwb": {
        // SCORING GOAL: Evaluates short-range wireless connectivity technologies.
        "configuration": {
          "value": "NFC + UWB",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the short-range wireless configuration. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "NFC + UWB" → 10.00
          //     Definition: Near Field Communication (NFC) for payments AND Ultra-Wideband (UWB) for precise directional tracking and digital keys.
          //   • "NFC Only"   → 5.00
          //     Definition: Near Field Communication support only; no directional UWB tracking.
          //   • "None"       → 0.00
          //     Definition: No short-range wireless connectivity.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits configuration.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_8_connectivity_and_cdc_index": {
        // SCORING GOAL: Evaluates seamless ecosystem connectivity features.
        "fast_file_transfer": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
          // Definition: High-speed peer-to-peer file sharing protocol over Wi-Fi/Bluetooth (e.g., Quick Share, AirDrop).
        },
        "cross_device_clipboard": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
          // Definition: Unified clipboard allowing copy-paste across different devices logged into the same account.
        },
        "task_handoff": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
          // Definition: Seamlessly resuming an active task (e.g., email draft, webpage) on a different device.
        },
        "communication_integration": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
          // Definition: Ability to pick up phone calls or reply to SMS from other connected devices (tablet/laptop).
        },
        "camera_virtualization": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
          // Definition: Using the smartphone's camera as a high-quality webcam for a connected tablet or laptop.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score is sum of all subscores above (Max 10.0).
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "7_9_usb_port_speed": {
        // SCORING GOAL: Evaluates wired transfer speed.
        "version_speed": {
          "value": "USB 3.2 Gen 2 (10Gbps)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 9.00
          // SCORING GUIDELINE: Identify the USB version and speed. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "USB 3.2 Gen 2x2 (20Gbps)" → 10.00
          //     Definition: SuperSpeed USB 20Gbps.
          //   • "USB 3.2 Gen 2 (10Gbps)"   → 9.00
          //     Definition: SuperSpeed USB 10Gbps.
          //   • "USB 3.2 Gen 1 (5Gbps)"    → 7.50
          //     Definition: SuperSpeed USB 5Gbps (formerly USB 3.0/3.1 Gen 1).
          //   • "USB 2.0 (480Mbps)"        → 2.00
          //     Definition: High Speed USB 2.0.
          //   • "Proprietary / Legacy"     → 0.00
          //     Definition: Non-standard or obsolete physical/logical interface.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits version_speed.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "8_battery_and_charging": {
      "8_1_battery_endurance_score": {
        // SCORING GOAL: Evaluates real-world battery life.
        "predicted_score": 7.90,
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.33,
          "method_used": "Benchmark (GSMArena + PhoneArena)",
          "booster": "No",
          "confidence": "High"
        }
      },
      "8_2_wired_charging_speed": {
        // SCORING GOAL: Evaluates maximum wired charging input.
        "watts": {
          "value": 45,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Apply Section 8.2 logarithmic formula. Score = 10 * (log(W) - log(Charge_W_Min)) / (log(Charge_W_Max) - log(Charge_W_Min)).
        },
        "predicted_score": 8.00,
        // SCORING GUIDELINE: predicted_score directly inherits watts.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "8_3_wireless_charging_speed": {
        // SCORING GOAL: Evaluates maximum wireless charging input.
        "watts": {
          "value": 15,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 5.00
          // SCORING GUIDELINE: Apply Section 8.3 logarithmic formula. Score = 10 * (log(W) - log(Wireless_W_Min)) / (log(Wireless_W_Max) - log(Wireless_W_Min)). Set to 0 if unsupported.
        },
        "predicted_score": 5.00,
        // SCORING GUIDELINE: predicted_score directly inherits watts.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 5.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "8_4_reverse_wired": {
        // SCORING GOAL: Evaluates reverse wired charging output capability.
        "watts": {
          "value": 0,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.00
          // SCORING GUIDELINE: Section 8.4 scoring: 10.0 if >= 10W, 5.0 if < 10W (but supported), 0.0 if unsupported. Value in Watts.
        },
        "predicted_score": 0.00,
        // SCORING GUIDELINE: predicted_score directly inherits watts.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 0.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "8_5_reverse_wireless": {
        // SCORING GOAL: Evaluates reverse wireless charging output capability.
        "watts": {
          "value": 4.5,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 5.00
          // SCORING GUIDELINE: Section 8.5 scoring: 10.0 if >= 10W, 5.0 if < 10W (but supported), 0.0 if unsupported. Value in Watts.
        },
        "predicted_score": 5.00,
        // SCORING GUIDELINE: predicted_score directly inherits watts.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 5.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "8_6_charger_in_box": {
        // SCORING GOAL: Rewards devices that include a high-speed charger in the box.
        "included_watts": {
          "value": 0,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.00
          // SCORING GUIDELINE: Identify the included charger wattage. Use the following thresholds for "value" with related scores as subscore:
          //   • >= 60W    → 10.00
          //     Definition: Ultra-high speed charger included in the box.
          //   • 30W - 59W → 7.00
          //     Definition: High speed charger included.
          //   • 15W - 29W → 4.00
          //     Definition: Standard speed charger included.
          //   • < 15W     → 2.00
          //     Definition: Low speed / basic charger included.
          //   • None      → 0.00
          //     Definition: No charger included in the retail box.
        },
        "predicted_score": 0.00,
        // SCORING GUIDELINE: predicted_score directly inherits included_watts.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 0.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "9_financial_and_economic_value": {
      "9_1_price": {
        // SCORING GOAL: Evaluates device price relative to standard flagships. Lower is better.
        "usd": {
          "value": 1299,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.80
          // SCORING GUIDELINE: Calculate the Base Inverted Cost Score (Section 9.1 Base Inverted Formula). Score = 10 × (X_max - Price) / (X_max - X_min). Clamped between 0 and 10. X_max = Max_Price_Threshold, X_min = Min_Price_Threshold.
        },
        "predicted_score": 0.80,
        // SCORING GUIDELINE: predicted_score directly inherits usd.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 0.80,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "9_2_manufacturer_warranty_commitment": {
        // SCORING GOAL: Evaluates standard included warranty length.
        "months": {
          "value": 12,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 3.00
          // SCORING GUIDELINE: Map months to scores using the following thresholds:
          //   • ">= 36 Months" → 10.00
          //   • "24 Months"    → 7.00
          //   • "12 Months"    → 3.00
          //   • "< 12 Months"  → 0.00
        },
        "predicted_score": 3.00,
        // SCORING GUIDELINE: predicted_score directly inherits months.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 3.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      },
      "9_3_repairability": {
        // SCORING GOAL: Evaluates official repairability scores.
        "european_union_repairability_index": {
          "value": 7.50,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.50
          // SCORING GUIDELINE: Direct inheritance. Max 10.00.
        },
        "predicted_score": 7.50,
        // SCORING GUIDELINE: predicted_score directly inherits european_union_repairability_index.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.50,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "10_miscellaneous": {
      "10_1_stylus_hardware_system_support": {
        // SCORING GOAL: Evaluates native stylus presence and hardware digitizer support.
        "support_tier": {
          "value": "Integrated active stylus + dedicated digitizer + Bluetooth features",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the stylus support level. Use the following exact Tier Names for "value" with related scores as subscore:
          //   • "Integrated active stylus + dedicated digitizer + Bluetooth features" → 10.00
          //     Definition: Stylus is stored inside the device (silo), uses an active digitizer layer for pressure/tilt, and has a battery for remote Bluetooth gestures.
          //   • "Active stylus support (dedicated digitizer, no silo)"              → 7.00
          //     Definition: Device has a dedicated digitizer layer for high-precision active pens (e.g., Apple Pencil, S Pen) but no internal storage for the pen.
          //   • "Passive stylus or basic touch pen"                                  → 3.00
          //     Definition: No dedicated digitizer; works with generic capacitive pens that mimic finger touch.
          //   • "None"                                                               → 0.00
          //     Definition: No official stylus support or secondary digitizer layer.
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits support_tier.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
  "11_reviews_and_performance_boosters": {
    "11_1_dxomark_24mp_texture_rendering": {
      "source_link": "https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/",
      "impacted_subsection": "4.16",
      "booster": 1.05,
      "justification": {
        "unaccounted_feature": "Other important updates compared to the previous generation iPhones include the jump from 12MP to 24MP images by default in most light conditions. In our tests, this made for significantly improved texture quality, especially in close-up portraits.",
        "unaccounted_reason": "Section 4.3 scores sensor resolution (48MP hardware), and Section 4.16 scores multi-frame processing presence (Always-on HDR + Night stacking). However, neither captures the quality impact of Apple's decision to bypass the industry standard and output 24MP images by default, which the review explicitly credits for improved texture preservation. Context: Modern smartphones group 4 small pixels together into 1 large pixel to capture more light (pixel binning), meaning even a 48MP camera normally outputs a 12MP image. Apple created unique software to simultaneously capture both a 12MP and 48MP image and merge them into a 24MP final image, yielding significantly higher detail without hardware changes (Source: https://www.apple.com/newsroom/2023/09/apple-unveils-iphone-15-pro-and-iphone-15-pro-max/).",
        "observed_justification": "The camera in Apple's new flagship device comes with an entirely new texture rendering management, and in our tests the results were outstanding. With most lighting conditions resulting in 24MP images, finest details were preserved much better than on most competitors. [...] The Apple iPhone 15 Pro Max provided very natural skin rendering with subtle local contrast and pleasant rendering of the finest details like hair, lips, wrinkles, etc."
      }
    },
    "11_2_toms_guide_display_factory_calibration": {
      "source_link": "https://www.tomsguide.com/reviews/iphone-15-pro-max",
      "impacted_subsection": "2.4",
      "booster": 1.05,
      "justification": {
        "unaccounted_feature": "it earned a Delta-E score of 0.14 (where zero is perfect)",
        "unaccounted_reason": "Section 2.3 scores DCI-P3 coverage percentage, which measures what colors the display *can* show. It does not measure factory calibration accuracy (Delta-E), which determines how *correctly* those colors are rendered. A display with 100% DCI-P3 coverage but poor calibration will show inaccurate colors.",
        "observed_justification": "The iPhone 15 Pro Max's display offers more accurate colors, as it earned a Delta-E score of 0.14 (where zero is perfect)"
      }
    },
    "11_3_dxomark_portrait_skin_tone_rendering": {
      "source_link": "https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/",
      "impacted_subsection": "4.17",
      "booster": 1.05,
      "justification": {
        "unaccounted_feature": "The smart HDR feature helped produce very natural and pleasant colors, even in very challenging light conditions.",
        "unaccounted_reason": "Section 4.17 scores the binary presence of semantic segmentation features (face detection, scene recognition). It does not score the specific quality of the tuning, such as the effectiveness of the Smart HDR algorithm in delivering strictly accurate and natural skin tones across diverse demographics, which requires qualitative validation beyond a checklist feature.",
        "observed_justification": "Skin tones were improved compared to the already very good Apple iPhone 14 Pro, across all skin tone types."
      }
    }
  }
}
```
