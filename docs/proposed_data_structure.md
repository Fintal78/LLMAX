# Ultimate Smartphone Data Structure Proposal (v5.1)

This schema is strictly aligned with the `scoring_rules.md` v8.0.

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
    "last_updated": "2026-03-11"
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
        "value_details": ["Grade 5 Titanium"],
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Look up the frame material in the Section 1.1.A table. Use the following terms exclusively for "value" with related scores as subscore:
        //   • Titanium Alloy       → 10.00
        //   • Stainless Steel      → 8.50
        //   • Aluminum Alloy       → 7.00
        //   • Polymer Composite    → 4.00
        //   • Not Disclosed        → 0.00
        // VALUE_DETAILS GUIDELINE: Record the exact Original Equipment Manufacturer (OEM) marketing name for the frame material (e.g., ["Grade 5 Titanium"], ["Armor Aluminum"], ["Stainless Steel 316L"]).
      },
      "back_material": {
        "value": "Strengthened Glass",
        "value_details": ["Gorilla Glass Victus 2"],
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.00
        // SCORING GUIDELINE: Look up the back panel material in the Section 1.1.B table. Use the following terms exclusively for "value" with related scores as subscore:
        //   • Ceramic              → 10.00
        //   • Strengthened Glass   → 8.00
        //   • Standard Glass       → 6.00
        //   • Polymer              → 4.00
        //   • Not Disclosed        → 0.00
        // VALUE_DETAILS GUIDELINE: Record the exact OEM marketing name for the back material (e.g., ["Gorilla Glass Victus 2"], ["Ceramic Shield"], ["Glastic"]).
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
        // SCORING GUIDELINE: Look up the first digit of the Ingress Protection (IP) rating in the Section 1.2.A table. Use the following terms exclusively for "value" with related scores as subscore:
        //   • Digit 6    → 10.00
        //   • Digit 5    → 8.00
        //   • Digit 4    → 6.00
        //   • Digit 3    → 4.00
        //   • Digit 2    → 2.00
        //   • Digit 0–1  → 0.00
      },
      "water_protection_digit": {
        "value_path": "1_2_durability.ingress_protection_rating.value",
        "value": "Digit 8",
        "subscore": 9.00
        // SCORING GUIDELINE: Look up the second digit of the Ingress Protection (IP) rating in the Section 1.2.B table. Use the following terms exclusively for "value" with related scores as subscore:
        //   • Digit 9    → 10.00
        //   • Digit 8    → 9.00
        //   • Digit 7    → 8.00
        //   • Digit 6    → 6.00
        //   • Digit 5    → 4.00
        //   • Digit 4    → 2.00
        //   • Digit 0–3  → 0.00
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
        "value": "Gorilla Glass Armor",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Identify the declared glass type. Use the following exact terms for "value" with related scores as subscore:
        //   • "Gorilla Glass Armor"                                       → 10.00
        //   • "Ceramic Shield (current gen)"                              → 9.50
        //   • "Gorilla Glass Victus 2"                                    → 9.00
        //   • "Gorilla Glass Victus or Victus+"                           → 8.00
        //   • "Dragontrail Star or Dragontrail Pro"                       → 8.00
        //   • "Gorilla Glass 5 or 6"                                      → 7.00
        //   • "Dragontrail X"                                             → 7.00
        //   • "Gorilla Glass 3 / Panda Glass / Dragontrail (standard)"    → 5.00
        //   • "Tempered Glass"                                            → 3.00 (Strengthened / Reinforced glass)
        //   • "Glass (Unspecified)"                                       → 2.00 (Generic 'Glass front')
        //   • "Plastic or No Glass"                                       → 0.00 (Polymer)
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
        "value_details": ["Dynamic AMOLED 2X"],
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 9.00
        // SCORING GUIDELINE: Identify the panel type. Use the following exact terms for "value" with related scores as subscore (Note: terms indicated AFTER the scores are alternative marketing names, i.e. "Dual-Layer OLED" can be found in spec sheets as an equivalent to "Tandem OLED"):
        //   • "Tandem OLED"      → 10.00 (Dual-Layer OLED)
        //   • "LTPO OLED"        → 9.00  (LTPO backplane, OLED ProMotion, Super Retina XDR ProMotion, Dynamic AMOLED 2X, ProXDR, LTPO4)
        //   • "AMOLED or OLED"   → 8.00  (Super AMOLED, Dynamic AMOLED" (without "2X"), P-OLED, Super Retina XDR/HD (without ProMotion))
        //   • "IPS LCD"          → 6.00  (Liquid Retina, Retina LCD/HD, IPS LCD/NEO)
        //   • "TFT or PLS LCD"   → 2.00  
        //   • "TN LCD or Legacy" → 0.00  (Twisted Nematic)
        // AMBIGUITY RULE: Plain "OLED" or "AMOLED" with NO "LTPO" qualifier must default to "AMOLED or OLED" (8.00).
        // In case of doubt consult #### Marketing Name → Canonical Tier Lookup
        // VALUE_DETAILS GUIDELINE: Record the exact OEM marketing name found in specs (e.g., ["Dynamic AMOLED 2X"], ["Super Retina XDR ProMotion"], ["LTPO4 AMOLED"]).
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
        "subscore": 8.00
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
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.00
          // SCORING GUIDELINE: Identify the physical speaker setup using spec sheets or teardowns. Use the following exact terms for "value" with related scores as subscore:
          //   • "Balanced / Symmetrical Stereo" → 10.00 (Must explicitly state "Symmetrical speakers" or "Balanced stereo")
          //   • "Standard Hybrid Stereo"        → 7.00  (Typically listed as 'Stereo Speakers' without symmetry claims)
          //   • "Mono Speaker"                  → 3.00  (Single active loudspeaker)
          //   • "No Usable Speaker"             → 0.00
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
          "value_details": ["360 Audio"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.00
          // SCORING GUIDELINE: Identify the highest-tier spatial capability. Use the following terms exclusively for "value" with related scores as subscore:
          //   • "Spatial audio with Dynamic Head Tracking"      → 10.00
          //   • "Static spatial audio (no head tracking)"       → 7.00
          //   • "No spatial rendering"                          → 0.00
          // VALUE_DETAILS GUIDELINE: Record the exact OEM marketing name for the spatial audio feature (e.g. ["360 Audio"], ["Dolby Atmos spatial"]).
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
          // SCORING GUIDELINE: Identify the highest supported wired audio tier. Use the following exact terms for "value" with related scores as subscore:
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
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the highest-tier recording capability. Use the following terms exclusively for "value" with related scores as subscore:
          //   • Multi-channel / spatial audio   → 10.00
          //   • Stereo                          → 8.00
          //   • Mono                            → 5.00
          //   • Voice-only / unclear            → 0.00
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
          "value_details": ["OIS"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the stabilization mechanism. Use the following exact terms for "value" with related scores as subscore:
          //   • "Multi-Axis Mechanical Stabilization (Gimbal)"          → 10.00 (Must contain Multi-axis mechanical and/or Gimbal)
          //   • "Sensor-Shift Optical Image Stabilization"              → 9.00  (Must explicitly state the sensor moves, e.g. IBIS)
          //   • "Lens-Based Optical Image Stabilization"                → 8.00  (Default for generic "OIS")
          //   • "Software-Only Stabilization (Electronic, no hardware)" → 5.00  (EIS/AIS only. No physical/hardware stabilization is mentioned.)
          //   • "None"                                                  → 0.00
          // AMBIGUITY RULE: If the spec sheet lists generic "Optical Image Stabilization (OIS)" without further qualification, default to 8.00.
          // VALUE_DETAILS GUIDELINE: Record the exact OEM stabilization term (e.g., ["OIS"], ["Sensor-Shift OIS"], ["SteadyShot with Active Mode"], ["Super Steady OIS + EIS"]).
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
          // SCORING GUIDELINE: Apply the Section 4.5.3 logarithmic formula: Score = 10 × (log(ultrawide_sensor_size) − log(Camera_Ultrawide_Sensor_Inch_Min)) / (log(Camera_Ultrawide_Sensor_Inch_Max) − log(Camera_Ultrawide_Sensor_Inch_Min)), clamped 0–10. Convert format string to decimal (e.g., "1/2.0" → 0.5). Only evaluated if presence = true. If presence = false, then all fields of this block must be "N/A".
        },
        "predicted_score": 8.67,
        // SCORING GUIDELINE: predicted_score = (0.60 × field_of_view_degrees.subscore) + (0.40 × ultrawide_sensor_size.subscore) if presence = true, source: UCC Formula of Section 4.5; otherwise predicted_score = 0.00.
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
          // SCORING GUIDELINE: Identify the maximum rear video resolution. Use the following exact terms for "value" with related scores as subscore:
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
          "value_details": ["ProRes"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the highest supported professional recording codec tier. Use the following exact terms for "value" with related scores as subscore:
          //   • "True RAW"    → 10.00 (Codecs: CinemaDNG, ProRes RAW, Blackmagic RAW (BRAW))
          //   • "Mezzanine"   → 8.00  (Codecs: ProRes, Advanced Professional Video (APV), DNxHR/HD)
          //   • "None"        → 0.00  (Standard H.264/H.265 only)
          // VALUE_DETAILS GUIDELINE: List all specific supported professional codecs found in specs (e.g., ["ProRes"], ["ProRes", "APV"], ["CinemaDNG", "ProRes RAW"]).
        },
        "log_color_profile_support": {
          "value": "True Log",
          "value_details": ["Apple Log"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the highest supported color profile tier based on Section 4.11.2. Use the following exact terms for "value" with related scores as subscore:
          //   • "True Log"      → 10.00 (Profiles: Apple Log, Samsung / Galaxy Log, S-Log / S-Log2 / S-Log3, V-Log, D-Log / D-Log M, F-Log, OPPO Log, Vivo Log, Xiaomi Log)
          //   • "Flat Profile"  → 5.00  (Profiles: S-Cinetone for mobile (Sony Flat), Cinelike-D / Cinelike-V, D-Cinelike)
          //   • "Standard"      → 0.00  (None / Standard contrast only)
          // VALUE_DETAILS GUIDELINE: List all specific supported log/flat profiles found in specs (e.g., ["Apple Log"], ["S-Log3", "S-Cinetone"], ["D-Log M"]).
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
          "exact_extract": "Proof pending",    
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
          "value_details": ["Phase Detection Auto Focus (PDAF)"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the front camera's focus type using the following exact terms for "value" with related scores as subscore:
          //   • "Autofocus"                        → 10.00 (Common types: Phase Detection Auto Focus (PDAF), Dual Pixel, Laser AF.)
          //   • "Fixed Focus (Modern Wide-DOF)"    → 6.00  (Identified by aperture_f_number ≥ 2.0 OR sensor_size ≤ 1/3".)
          //   • "Fixed Focus (Legacy Narrow-DOF)"  → 3.00  (Identified by aperture_f_number < 2.0 AND sensor_size > 1/3".)
          //   • "No Front Camera"                  → 0.00
          // MISSING DATA FALLBACK: If sensor size is missing from specs but aperture (f-number) is known, classify based solely on the aperture.
          // VALUE_DETAILS GUIDELINE: Record the exact technology (e.g., ["Phase Detection Auto Focus (PDAF)"], ["Dual Pixel PDAF"], ["Laser AF"]).
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
            // SCORING GUIDELINE: Mirroring Section 4.8 (Rear Video Resolution). Identify the maximum front video resolution. Use the following exact terms for "value" with related scores as subscore:
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
            "value_details": ["ProRes"],
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 8.00
            // SCORING GUIDELINE: Mirroring Section 4.11.1 (PCS). Identify the highest supported professional recording codec tier. Use the following exact terms for "value" with related scores as subscore:
            //   • "True RAW"    → 10.00 (Codecs: CinemaDNG, ProRes RAW, Blackmagic RAW (BRAW))
            //   • "Mezzanine"   → 8.00  (Codecs: ProRes, Advanced Professional Video (APV), DNxHR/HD)
            //   • "None"        → 0.00  (Standard H.264/H.265 only)
            // VALUE_DETAILS GUIDELINE: List all specific supported professional codecs found in specs (e.g., ["ProRes"], ["ProRes", "APV"], ["CinemaDNG", "ProRes RAW"]).
          }
        },
        "4_15_4_2_log_color_profile_support": {
          "supported_profiles": {
            "value": "True Log",
            "value_details": ["Apple Log"],
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.11.2 (LCPS). Identify the highest supported color profile tier. Use the following exact terms for "value" with related scores as subscore:
            //   • "True Log"      → 10.00 (Profiles: Apple Log, Samsung / Galaxy Log, S-Log / S-Log2 / S-Log3, V-Log, D-Log / D-Log M, F-Log, OPPO Log, Vivo Log, Xiaomi Log)
            //   • "Flat Profile"  → 5.00  (Profiles: S-Cinetone for mobile (Sony Flat), Cinelike-D / Cinelike-V, D-Cinelike)
            //   • "Standard"      → 0.00  (None / Standard contrast only)
            // VALUE_DETAILS GUIDELINE: List all specific supported log/flat profiles found in specs (e.g., ["Apple Log"], ["S-Log3", "S-Cinetone"], ["D-Log M"]).
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
          "value_details": ["Deep Fusion", "Smart HDR 5"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Use the following exact terms for "value" with related scores as subscore (Reference Section 4.16 for full details):
          //   • "Advanced Semantic & Neural Stacking" → 10.00
          //     Look for: Apple (Photonic Engine, Deep Fusion, Smart HDR 4/5), Google (HDR+ with Bracketing (Tensor-based), Super Res Zoom), Samsung (Enhanced Processing [S23+], Expert RAW Stacking), Vivo (V3/V4 Imaging Chip, BlueImage, Neural HDR), Oppo (MariSilicon X/Y, Ultra HDR), Common (Neural/AI Stacking, Semantic Segmentation, Zero Shutter Lag (ZSL)).
          //   • "Standard Always-on Multi-Frame HDR"  → 7.50
          //     Look for: Apple (Smart HDR 2/3), Google (Standard HDR+ [Pixel 1-5]), Samsung (Scene Optimizer [Multi-frame mode]), Common (Always-on HDR, Automatic Multi-frame Fusion).
          //   • "Conditional / Manual Multi-Frame"    → 5.00
          //     Look for: Generic "Auto-HDR", Manual HDR Mode, Night Mode Stacking (if only in dedicated mode).
          //   • "Basic / Single Frame (Legacy)"       → 0.00
          //     Look for: No multi-frame stacking, standard single exposure.
          // VALUE_DETAILS GUIDELINE: List the exact OEM feature names that justify the tier (e.g., ["Deep Fusion", "Smart HDR 5"], ["Neural HDR", "BlueImage"], ["HDR+ with Bracketing"]).
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
      "4_17_semantic_ai": {
        // SCORING GOAL: Scores the ability of the camera software to understand and segment scenes and subjects.
        "capability_tier": {
          "value": "Full semantic segmentation (faces, sky, objects)",
          "value_details": ["Scene Optimizer"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Use the following exact terms for "value" with related scores as subscore:
          //   • "Full semantic segmentation (faces, sky, objects)" → 10.00
          //   • "Basic portrait / scene detection" → 6.00
          //   • "None" → 0.00
          // VALUE_DETAILS GUIDELINE: Record the exact OEM feature names (e.g., ["Scene Optimizer"], ["Visual Intelligence", "Photographic Styles"], ["Google Lens integration"]).
        },
        "predicted_score": 10.00,
        // SCORING GUIDELINE: predicted_score directly inherits capability_tier.subscore.
        "final_score": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "Yes: 11_3_dxomark_portrait_skin_tone_rendering (+5%)",
          "confidence": "N/A"
        }
      },
      "4_18_generative_ai_tools": {
        // SCORING GOAL: Scores the ability to modify images after capture using AI.
        "feature_tier": {
          "value": "Generative erase / expand / relight",
          "value_details": ["Magic Eraser", "Best Take"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Use the following exact terms for "value" with related scores as subscore:
          //   • "Generative erase / expand / relight" → 10.00
          //   • "Non-generative AI edits" → 6.00
          //   • "None" → 0.00
          // VALUE_DETAILS GUIDELINE: List the exact OEM AI tool names (e.g., ["Magic Eraser", "Best Take"], ["Clean Up", "Image Playground"], ["AI Expand", "Generative Fill"]).
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
          "value": 6.00,
          "source": "N/A",
          "exact_extract": "N/A",
          "subscore": 6.00
          // SCORING GUIDELINE: Direct lookup from the `skin` field above via the Section 5.2 Platform Cleanliness table. Do not derive this value from any formula. Known platforms: iOS -> 10.0, Pixel UI / Stock Android -> 9.0, Samsung One UI -> 6.0, HyperOS -> 4.0, etc. If unlisted, score = N/A.
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
        },
        "live_speech_translation": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If value = true, subscore = 2.00. If value = false, subscore = 0.00.
        },
        "content_summarization": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.50
          // SCORING GUIDELINE: If value = true, subscore = 1.50. If value = false, subscore = 0.00.
        },
        "writing_tools": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.00
          // SCORING GUIDELINE: If value = true, subscore = 1.00. If value = false, subscore = 0.00.
        },
        "on_device_processing": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 3.00
          // SCORING GUIDELINE: If value = true, subscore = 3.00. If value = false, subscore = 0.00.
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
          // SCORING GUIDELINE: Look up the value in Section 6.5 memory technology table. E.g., LPDDR5X -> 10.0, LPDDR5 -> 8.0, LPDDR4X -> 5.0, LPDDR4 -> 3.0, older -> 0.0.
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
          // SCORING GUIDELINE: Apply Section 6.6 logarithmic formula based on RAM Capacity. Score = 10 * (log(GB) - log(RAM_GB_Min)) / (log(RAM_GB_Max) - log(RAM_GB_Min))
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
          // SCORING GUIDELINE: Look up the value in Section 6.7 storage technology table. NVMe / UFS 4.0 -> 10.0, UFS 3.1 -> 8.0, UFS 3.0 -> 6.0, UFS 2.2 -> 4.0, UFS 2.1 -> 3.0, eMMC 5.1 -> 0.0.
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
          // SCORING GUIDELINE: Apply Section 6.8 logarithmic formula based on Storage Capacity. Score = 10 * (log(GB) - log(Storage_GB_Min)) / (log(Storage_GB_Max) - log(Storage_GB_Min))
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
          // SCORING GUIDELINE: Look up the value in Section 6.9 storage expandability table. Dedicated MicroSD Slot -> 10.0, Shared SIM slot -> 7.0, NM Card -> 5.0, None -> 0.0.
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
          "value_details": ["Vapor Chamber cooling system"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Look up the value in Section 6.10 Part B table. Active Cooling (Fan) -> 10.0, Large VC -> 8.0, Vapor Chamber -> 7.0, Multi-layer Graphite -> 5.0, Single Heat Spreader -> 3.0, None -> 0.0.
          // VALUE_DETAILS GUIDELINE: Record the exact OEM cooling marketing term (e.g., ["IceLoop Thermal System"], ["Cryo-Velocity Vapor Chamber"], ["LiquidCool Technology"]).
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
          // SCORING GUIDELINE: Look up the value in Section 7.1 table.
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
          // SCORING GUIDELINE: Look up the value in Section 7.2 table.
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
          // SCORING GUIDELINE: Look up the value in Section 7.3 table.
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
          // SCORING GUIDELINE: Look up Bluetooth version score in Section 7.4 Part 1 table.
        },
        "highest_codec_supported": {
          "value": "aptX HD / LDAC",
          "value_details": ["LDAC", "aptX HD", "AAC", "SBC"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 4.00
          // SCORING GUIDELINE: Look up highest codec tier in Section 7.4 Part 2 table. Lossless -> 5.0, High-Res -> 4.0, Standard -> 1.5.
          // VALUE_DETAILS GUIDELINE: List all specific Bluetooth audio codecs supported by the device (e.g., ["LDAC", "aptX HD", "AAC", "SBC"], ["aptX Lossless", "LDAC", "aptX Adaptive"]).
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
          "value_details": ["Qualcomm 3D Sonic Gen 2"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Look up best available biometric method in Section 7.5 table.
          // VALUE_DETAILS GUIDELINE: Record the exact OEM biometric sensor model or marketing name (e.g., ["Qualcomm 3D Sonic Gen 2"], ["Face ID"], ["Optical in-display fingerprint"]).
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
          // SCORING GUIDELINE: Look up value in Section 7.7 table.
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
        },
        "cross_device_clipboard": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
        },
        "task_handoff": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
        },
        "communication_integration": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
        },
        "camera_virtualization": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If true, 2.00; false, 0.00.
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
          "subscore": 10.00
          // SCORING GUIDELINE: Look up value in Section 7.9 table.
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
          // SCORING GUIDELINE: Apply Section 8.2 logarithmic formula. Score = 10 * (log(W) - log(Charge_W_Min)) / (log(Charge_W_Max) - log(Charge_W_Min))
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
          // SCORING GUIDELINE: Section 8.6 scoring based on included charger wattage: >= 60W -> 10.0, 30W-59W -> 7.0, 15W-29W -> 4.0, <15W -> 2.0, None -> 0.0.
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
          // SCORING GUIDELINE: Section 9.2 table: 36+ Months -> 10.0, 24 Months -> 7.0, 12 Months -> 3.0.
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
          "value_details": ["S Pen"],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Section 10.1 table: Integrated Active -> 10.0, Active (No Silo) -> 7.0, Passive/Basic -> 3.0, None -> 0.0.
          // VALUE_DETAILS GUIDELINE: Record the exact OEM stylus product name (e.g., ["S Pen"], ["Apple Pencil Pro"], ["Xiaomi Smart Pen"]).
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
