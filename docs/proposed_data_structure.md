# Ultimate Smartphone Data Structure Proposal (v5.1)

This schema is strictly aligned with the `scoring_rules.md` v8.0.

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
    "last_updated": "2026-03-03"
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
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Look up the frame material in the Section 1.1.A table. Use the following terms exclusively for "value" with related scores:
        //   • Titanium Alloy       → 10.00
        //   • Stainless Steel      → 8.50
        //   • Aluminum Alloy       → 7.00
        //   • Polymer Composite    → 4.00
        //   • Not Disclosed        → 0.00
      },
      "back_material": {
        "value": "Strengthened Glass",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.00
        // SCORING GUIDELINE: Look up the back panel material in the Section 1.1.B table. Use the following terms exclusively for "value" with related scores:
        //   • Ceramic              → 10.00
        //   • Strengthened Glass   → 8.00
        //   • Standard Glass       → 6.00
        //   • Polymer              → 4.00
        //   • Not Disclosed        → 0.00
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
      // GUIDELINE: `ingress_protection_rating` stores the full human-readable IP (Ingress Protection) composite string (e.g. "IP68") as declared by the manufacturer. It is not scored directly but the two individual digits extracted for scoring are `dust_protection_digit` and `water_protection_digit`, see below — always parse those from this `ingress_protection_rating.value` string.
      "ingress_protection_rating": {
        "value": "IP68",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A" // no score here, it will be calculated below from dust_protection_digit and water_protection_digit
      },
      // SCORING GOAL: Scores dust and water resistance separately using the two digits of the IP (Ingress Protection) rating defined by IEC standard 60529. The full composite string is available at `1_2_durability.ingress_protection_rating.value` for reference.
      "dust_protection_digit": {
        "value": "Digit 6",
        "source": "1_2_durability.ingress_protection_rating.value",
        "exact_extract": "6",
        "subscore": 10.00
        // SCORING GUIDELINE: Look up the first digit of the IP rating in the Section 1.2.A table. Use the following terms exclusively for "value" with related scores:
        //   • Digit 6    → 10.00
        //   • Digit 5    → 8.00
        //   • Digit 4    → 6.00
        //   • Digit 3    → 4.00
        //   • Digit 2    → 2.00
        //   • Digit 0–1  → 0.00
      },
      "water_protection_digit": {
        "value": "Digit 8",
        "source": "1_2_durability.ingress_protection_rating.value",
        "exact_extract": "8",
        "subscore": 9.00
        // SCORING GUIDELINE: Look up the second digit of the IP rating in the Section 1.2.B table. Use the following terms exclusively for "value" with related scores:
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
      // SCORING GOAL: Scores the protective glass type on the display, known as Display Glass Protection (DGP), based on the manufacturer-declared glass generation's certified drop and scratch resistance class.
      "glass_generation": {
        "value": "Gorilla Glass Armor",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Look up the declared glass type in the Section 1.3 table. Use the following terms exclusively for "value" with related scores:
        //   • Gorilla Glass Armor                  → 10.00
        //   • Ceramic Shield (current gen)         → 9.50
        //   • Gorilla Glass Victus 2               → 9.00
        //   • Gorilla Glass Victus or Victus+      → 8.00
        //   • Dragontrail Star or Dragontrail Pro  → 8.00
        //   • Gorilla Glass 5 or 6                 → 7.00
        //   • Dragontrail X                        → 7.00
        //   • Gorilla Glass 3                      → 5.00
        //   • Panda Glass                          → 5.00
        //   • Dragontrail (standard)               → 5.00
        //   • Tempered Glass                       → 3.00
        //   • Glass (Unspecified)                  → 2.00
        //   • Plastic or No Glass                  → 0.00
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
      // SCORING GOAL: Scores the physical display technology (Display Panel Architecture, DPA) used to generate light and images. Focuses on panel construction only — not brightness, color, or refresh behaviour.

      // ─────────────────────────────────────────────────────────────────────────────
      // MARKETING NAME → CANONICAL TIER LOOKUP  (static reference — do not score from here)
      // Source: Marketing Name → Canonical Tier Lookup from Section 2.1 Display Panel Architecture (DPA)
      //
      // Step 1: find the spec-sheet label of the phone under test in the lists below.
      // Step 2: use the matching "canonical" string as panel_type.value.
      // Step 3: copy the matching "score" into panel_type.subscore.
      //
      // DECISION RULE — ambiguous labels:
      //   Plain "OLED" or "AMOLED" with NO LTPO qualifier → default to "AMOLED or OLED" (8.0).
      //   Assign "LTPO OLED" (9.00) ONLY when LTPO backplane OR a Tier-9 name below is confirmed.
      // ─────────────────────────────────────────────────────────────────────────────
      "panel_type_lookup": {
        "tier_10_tandem_oled": {
          "canonical": "Tandem OLED",
          "score": 10.00,
          "marketing_names": [
            "Tandem OLED",
            "Dual-Layer OLED"
          ]
        },
        "tier_9_ltpo_oled": {
          "canonical": "LTPO OLED",
          "score": 9.00,
          "marketing_names": [
            "Dynamic AMOLED 2X",
            "OLED ProMotion",
            "Super Retina XDR with ProMotion",
            "Super Retina XDR ProMotion",
            "ProMotion (combined with any OLED label)",
            "ProXDR Display",
            "LTPO OLED",
            "LTPO4 / LTPO 4.0"
          ]
        },
        "tier_8_amoled_or_oled": {
          "canonical": "AMOLED or OLED",
          "score": 8.00,
          "marketing_names": [
            "Super AMOLED",
            "Dynamic AMOLED (without 2X suffix)",
            "AMOLED",
            "Super Retina XDR (without ProMotion)",
            "Super Retina HD",
            "P-OLED / pOLED",
            "Flexible OLED",
            "OLED (no LTPO qualifier — see decision rule above)"
          ]
        },
        "tier_6_ips_lcd": {
          "canonical": "IPS LCD",
          "score": 6.00,
          "marketing_names": [
            "Liquid Retina HD",
            "Liquid Retina",
            "Retina LCD",
            "Retina HD",
            "IPS LCD",
            "IPS NEO",
            "In-Cell Touch IPS"
          ]
        },
        "tier_2_tft_or_pls_lcd": {
          "canonical": "TFT or PLS LCD",
          "score": 2.00,
          "marketing_names": [
            "PLS TFT",
            "PLS",
            "TFT LCD",
            "TFT (no IPS qualifier)"
          ]
        },
        "tier_0_tn_lcd_or_legacy": {
          "canonical": "TN LCD or Legacy",
          "score": 0.00,
          "marketing_names": [
            "TFT (TN)",
            "Any explicitly TN-type label"
          ]
        }
      },

      "panel_type": {
        "value": "LTPO OLED",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 9.00
        // SCORING GUIDELINE: Find the spec-sheet label in panel_type_lookup above → copy the canonical string here and its score into subscore. Use the following terms exclusively for "value" with related scores:
        //   • Tandem OLED        → 10.00
        //   • LTPO OLED          → 9.00
        //   • AMOLED or OLED     → 8.00
        //   • IPS LCD            → 6.00
        //   • TFT or PLS LCD     → 2.00
        //   • TN LCD or Legacy   → 0.00
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
      // SCORING GOAL: Scores peak and High Brightness Mode (HBM) brightness together, as HBM governs outdoor readability while peak brightness governs HDR (High Dynamic Range) media quality.
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
      // SCORING GOAL: Scores how much of the DCI-P3 (Digital Cinema Initiatives P3) professional color space the display can reproduce. A wider gamut means richer, more saturated colors in photos, videos, and HDR content.
      "dci_p3_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Apply the Section 2.3 linear formula: Score = 10 × (dci_p3_percent − Display_P3_Coverage_Percent_Min) / (Display_P3_Coverage_Percent_Max − Display_P3_Coverage_Percent_Min), clamped 0–10. If dci_p3_percent is not available from any source then set "value" to "Not found" and subscore to "N/A". Then use the "srgb_percent" bloc below as fallback scoring. 
      },
      "srgb_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A"
        // SCORING GUIDELINE: sRGB coverage is a fallback data source only. ONLY when dci_p3_percent is not available from any source use the formula above with DCI-P3_estimate = min(srgb_percent × 0.75, 100) to calculate the subscore of this bloc. When dci_p3_percent is available and the subscore was calculated in the previous bloc then set the subscore of this bloc to "N/A".
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
      "formats": {
        "value": "Alternative Dynamic HDR (HDR10+ + HDR10 only)",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.00
        // SCORING GUIDELINE: Identify the highest-tier format combination supported and look it up in the Section 2.4 table. Use the following terms exclusively for "value" with related scores:
        //   • Universal Dynamic HDR (Dolby Vision + HDR10+ + HDR10)  → 10.00
        //   • Primary Dynamic HDR (Dolby Vision + HDR10 only)        → 9.00
        //   • Alternative Dynamic HDR (HDR10+ + HDR10 only)         → 8.00
        //   • Basic Static HDR (HDR10 only)                         → 6.00
        //   • No HDR                                                → 0.00
      },
      "predicted_score": 8.00,
      // SCORING GUIDELINE: predicted_score directly inherits formats.subscore.
      "final_score": {
        // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
        "value": 8.00,
        "method_used": "Predictor",
        "booster": "No",
        "confidence": "N/A"
      }
    },
    "2_5_resolution_density": {
      // SCORING GOAL: Scores pixel density (Pixels Per Inch, PPI) as a measure of display sharpness. Higher PPI means text and images look crisp with no visible pixels.
      "resolution_width_px": {
        // GUIDELINE: Horizontal pixel count of the display. Used for scoring ONLY when ppi is not available from any source.
        "value": 1440,
        "source": "TBD",
        "exact_extract": "Proof pending",
      },
      "resolution_height_px": {
        // GUIDELINE: Vertical pixel count of the display. Used for scoring ONLY when pixels_per_inch is not available from any source.
        "value": 3120,
        "source": "TBD",
        "exact_extract": "Proof pending",
      },
      "pixels_per_inch": {
        "value": 505,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.43
        // SCORING GUIDELINE: Apply the Section 2.5 logarithmic formula: Score = 10 × (log(pixels_per_inch) − log(Display_PPI_Min)) / (log(Display_PPI_Max) − log(Display_PPI_Min)), clamped 0–10. Use directly pixels_per_inch.value if available from any source. 
        // ONLY if pixels_per_inch is NOT available derive PPI: PPI = √(resolution_width_px² + resolution_height_px²) / diagonal_inches 
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
      // SCORING GOAL: Scores touch sampling rate as a measure of how instantly the screen responds to finger input. Higher rates produce a "glued to your finger" feel, critical for gaming and UI fluidity.
      "sampling_rate_hz": {
        "value": 240,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 5.00
        // SCORING GUIDELINE: Apply the Section 2.7 logarithmic formula: Score = 10 × (log(sampling_rate_hz) − log(Display_Touch_Sampling_Hz_Min)) / (log(Display_Touch_Sampling_Hz_Max) − log(Display_Touch_Sampling_Hz_Min)), clamped 0–10.
      },
      "predicted_score": 5.00,
      // SCORING GUIDELINE: predicted_score directly inherits sampling_rate_hz.subscore.
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
      // SCORING GOAL: Evaluates how the screen dims at low brightness levels to prevent eye strain and headaches. It scores either the perfect continuous light of Direct Current (DC) Dimming, or scales the Pulse-Width Modulation (PWM) frequency if flickering is present.

      // ─────────────────────────────────────────────────────────────────────────────
      // DIMMING TECHNOLOGY → VERIFICATION RULE LOOKUP (static reference — do not score from here)
      // Source: Section 2.10.1 PWM Dimming (Flicker) Presence table.
      //
      // Step 1: Identify if the panel uses Pulse-Width Modulation (PWM) or Direct Current (DC) dimming.
      // Step 2: Use the "presence" value (Yes/No) for flicker_presence.
      // Step 3: Match with the corresponding technical details below.
      // ─────────────────────────────────────────────────────────────────────────────
      "dimming_technology_lookup": { // this is a lookup table, do not score here
        "option_flicker_active": {
          "presence": "Yes",
          "technology": "PWM Dimming active",
          "verification_rule": "Any OLED/AMOLED panel (inherent), or an LCD specifically tested to have PWM flicker.",
          "score_impact": "Determined by frequency (Hz)"
        },
        "option_no_flicker": {
          "presence": "No",
          "technology": "DC (Direct Current)",
          "verification_rule": "Standard LCD/IPS panel with confirmed DC (Direct Current) dimming (no measurable PWM flicker).",
          "score_impact": 10.00
        }
      },
      
      "flicker_presence": {
        "value": "Yes",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A"
        // SCORING GUIDELINE: Record if PWM flicker is present (Yes/No) based on the verification rules in dimming_technology_lookup above.
        //   • If "No" (DC Dimming), subscore is 10.00.
        //   • If "Yes" (PWM Dimming), subscore is "N/A" as the score is derived from frequency below.
      },
      "pulse_width_modulation_dimming_hertz": {
        "value": 492,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 4.07
        // SCORING GUIDELINE: Only evaluated if flicker_presence.value = "Yes". Apply the Section 2.10.2 logarithmic formula: Score = 10 × (log(pulse_width_modulation_dimming_hertz) − log(Display_PWM_Hz_Min)) / (log(Display_PWM_Hz_Max) − log(Display_PWM_Hz_Min)), clamped 0–10. If flicker_presence.value = "No", this subscore MUST be "N/A".
      },
      "predicted_score": 4.07,
      // SCORING GUIDELINE: The predicted score directly inherits whichever subscore is NOT "N/A" between flicker_presence and pulse_width_modulation_dimming_hertz. 
      // (If No-Flicker, inherits 10.00 from flicker_presence; if Flicker-Active, inherits frequency score from pulse_width_modulation_dimming_hertz).
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
        // SCORING GOAL: Scores the physical speaker hardware configuration (Speaker System Capability, SSC) for audio output without headphones. Evaluates speaker count, placement, and channel symmetry.

        // ─────────────────────────────────────────────────────────────────────────────
        // SPEAKER CONFIGURATION → CANONICAL TIER LOOKUP (static reference — do not score from here)
        // Source: Section 3.1 Speaker System Capability (SSC) tiers and Explanation of Tiers.
        //
        // Step 1: Identify the device's physical speaker setup (count and placement) from spec sheets or teardowns.
        // Step 2: Match the setup to the matching "canonical" string as speaker_configuration.value.
        // Step 3: Copy the matching "score" into speaker_configuration.subscore.
        // ─────────────────────────────────────────────────────────────────────────────
        "speaker_system_lookup": { // this is a lookup table, do not score here
          "balanced_stereo": {
            "canonical": "Balanced / Symmetrical Stereo",
            "score": 10.00,
            "definition": "Two identical or near-identical dedicated speaker units (e.g., dual front-facing or matching top/bottom drivers) providing equal volume and tonal balance.",
            "justification": "A rare, hardware-intensive setup where both left/right drivers are physically identical, guaranteeing superior stereo imaging and center-channel stability. Review explicitly states 'Symmetrical speakers' or 'Balanced stereo'."
          },
          "standard_stereo": {
            "canonical": "Standard Hybrid Stereo",
            "score": 7.00,
            "definition": "Can use the earpiece as a second channel (tweeter) combined with a dedicated bottom main driver (woofer).",
            "justification": "The smaller earpiece focuses on highs while the bottom driver handles mids/lows, creating a slight tonal imbalance compared to perfect symmetry. Spec sheet lists 'Stereo Speakers' without specific 'Symmetrical' confirmation."
          },
          "mono_speaker": {
            "canonical": "Mono Speaker",
            "score": 3.00,
            "definition": "Single active loudspeaker, typically bottom-firing only.",
            "justification": "Provides no spatial separation; all sound originates from a single point. Spec sheet lists 'Loudspeaker' (singular) or reviews confirm lack of stereo effect."
          },
          "no_speaker": {
            "canonical": "No Usable Speaker",
            "score": 0.00,
            "definition": "No built-in loudspeaker; relies entirely on external audio.",
            "justification": "Zero capability for independent audio output."
          }
        },

        "speaker_configuration": {
          "value": "Standard Hybrid Stereo",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.00
          // SCORING GUIDELINE: Look up the configuration in the speaker_system_lookup above. Use the matching "canonical" string for "value" and its "score" for subscore.
          // Note: Verify via spec sheet or a review that explicitly states symmetry for 10.00.
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
        // SCORING GOAL: Scores Playback Audio Processing & Immersion (PAPI) as a composite of two sub-criteria: audio format decoding capability (3.2.1, weight 50%) and spatial audio rendering capability (3.2.2, weight 50%).
        "audio_format_decode": {
          "value": "Dolby Atmos ONLY",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the highest-tier supported format capability. Use the following terms exclusively for "value" with related scores:
          //   • Dolby Atmos AND DTS:X                          → 10.00
          //   • Dolby Atmos ONLY                               → 8.00
          //   • Multichannel Surround (Dolby Digital / DTS)    → 5.00
          //   • Stereo ONLY                                    → 0.00
        },
        "spatial_audio_rendering": {
          "value": "Static spatial audio (no head tracking)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.00
          // SCORING GUIDELINE: Identify the highest-tier spatial capability. Use the following terms exclusively for "value" with related scores:
          //   • Spatial audio with Dynamic Head Tracking      → 10.00
          //   • Static spatial audio (no head tracking)       → 7.00
          //   • No spatial rendering                          → 0.00
        },
        "predicted_score": 7.50,
        // SCORING GUIDELINE: predicted_score = (0.5 × audio_format_decode.subscore) + (0.5 × spatial_audio_rendering.subscore). Both sub-criteria are equally weighted per the PAPI formula in Section 3.2.
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
          // SCORING GUIDELINE: Identify the highest supported wired audio tier. Use the following terms exclusively for "value" with related scores:
          //   • 3.5mm headphone jack (native analog output)   → 10.00
          //   • USB-C with documented analog audio output     → 6.00
          //   • USB-C digital audio only (dongle required)    → 3.00
          //   • No wired audio support                        → 0.00
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
        // SCORING GOAL: Scores Microphone & Audio Recording (MAR) as a composite of hardware count (3.4.1, 30%), recording channels (3.4.2, 30%), and advanced capture features (3.4.3, 40%). Source: §3.4 Microphone & Audio Recording.
        "microphone_hardware_count": {
          "value": "3",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Record the physical microphone count. Use the following terms exclusively for "value" with related scores:
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
          // SCORING GUIDELINE: Identify the highest-tier recording capability. Use the following terms exclusively for "value" with related scores:
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
      // GUIDELINE: Hardware inventory of all physical camera modules. Contains ONLY unscored reference data
      // (Rule 1 — non-scoring data at section root). All scored parameters are stored in their respective
      // scoring subsections and are NOT duplicated here.
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
        // SCORING GOAL: Scores the image stabilization mechanism used to compensate for hand shake during photo and video capture.

        // ─────────────────────────────────────────────────────────────────────────────
        // STABILIZATION TYPE → TIER LOOKUP (static reference — do not score from here)
        // Source: Section 4.4 — Spec Sheet Keyword → Tier Lookup table.
        //
        // Step 1: Identify which stabilization keywords appear in the device's spec sheet.
        // Step 2: Match with the highest-applicable tier below.
        // Step 3: Use the corresponding "tier_name" value for stabilization_type.value.
        // ─────────────────────────────────────────────────────────────────────────────
        "stabilization_type_lookup": {  // this is a lookup table, do not score here
          "tier_10_multi_axis_mechanical": {
            "tier_name": "Multi-Axis Mechanical Stabilization (Gimbal)",
            "score": 10.00,
            "recognized_keywords": ["Gimbal stabilization", "Gimbal-grade OIS", "Micro-gimbal", "Multi-axis gimbal", "6-axis stabilization", "Super Steady OIS (hardware)", "Gimbal 2.0", "Gimbal 3.0"],
            "verification_rule": "Manufacturer explicitly names a multi-axis mechanical gimbal system. A simple 'OIS' label is NOT sufficient."
          },
          "tier_9_sensor_shift": {
            "tier_name": "Sensor-Shift Optical Image Stabilization",
            "score": 9.00,
            "recognized_keywords": ["Sensor-shift OIS", "Sensor-shift optical image stabilization", "IBIS (In-Body Image Stabilization)", "Sensor-based OIS"],
            "verification_rule": "Manufacturer explicitly states the sensor (not the lens) moves. Currently mostly used by Apple (iPhone 12 Pro Max+ / iPhone 13+)."
          },
          "tier_8_lens_based": {
            "tier_name": "Lens-Based Optical Image Stabilization",
            "score": 8.00,
            "recognized_keywords": ["OIS", "Optical Image Stabilization", "Lens-shift OIS", "Lens-based OIS", "Prism Tilt OIS"],
            "verification_rule": "Default tier for any unspecified 'OIS'. The majority of Android phones use lens-based mechanisms."
          },
          "tier_5_software_only": {
            "tier_name": "Software-Only Stabilization",
            "score": 5.00,
            "recognized_keywords": ["EIS (Electronic Image Stabilization)", "Digital stabilization", "AIS (Artificial Image Stabilization)", "Software stabilization", "Video stabilization (without OIS mention)"],
            "verification_rule": "No hardware Optical Image Stabilization is mentioned. Only software-based correction."
          },
          "tier_0_none": {
            "tier_name": "None",
            "score": 0.00,
            "recognized_keywords": [],
            "verification_rule": "No stabilization terms found in spec sheet or review."
          }
        },

        "stabilization_type": {
          "value": "Lens-Based Optical Image Stabilization",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the mechanism by matching spec sheet keywords against the stabilization_type_lookup above. 
          // Set "value" to the matching tier's exact tier_name and "subscore" to that tier's score.
          // AMBIGUITY RULE: If the spec sheet says only "OIS" without further qualification, default to the "Lens-Based Optical Image Stabilization" tier.
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
          // SCORING GUIDELINE: Binary gate. If value = false, the subscore is 0.00 and all other fields in the 2 sections below MUST be "N/A". If value = true, then the subscore must be "N/A" and the scores will be calculated in the sections below.
        },
        "field_of_view_degrees": {
          "value": 120,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.78
          // SCORING GUIDELINE: Apply the Section 4.5.2 linear formula: Score = 10 × (field_of_view_degrees − Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max) / (Camera_Ultrawide_FOV_Deg_Max − Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max), clamped 0–10. Only evaluated if presence = true. If presence = false, then all fields of this bloc must be "N/A".
        },
        "ultrawide_sensor_size": {
          "value": "1/2.0",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 4.5.3 logarithmic formula: Score = 10 × (log(ultrawide_sensor_size) − log(Camera_Ultrawide_Sensor_Inch_Min)) / (log(Camera_Ultrawide_Sensor_Inch_Max) − log(Camera_Ultrawide_Sensor_Inch_Min)), clamped 0–10. Convert format string to decimal (e.g., "1/2.0" → 0.5). Only evaluated if presence = true. If presence = false, then all fields of this bloc must be "N/A".
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
            // SCORING GUIDELINE (4.7.1.1): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. Use the following terms exclusively for "value" with related scores:
            //   • Autofocus    → 10.00
            //   • Fixed focus  → 6.00
            //   If presence = false, this subscore MUST be "N/A" and Score_4.7.1 = 0.00.
          },
          "min_focus_distance_cm": {
            "value": 2.5,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 7.31
            // SCORING GUIDELINE (4.7.1.2): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. Apply the Section 4.7.1.2 logarithmic formula: Score = 10 × (log(Camera_Macro_Dist_cm_Max) − log(distance)) / (log(Camera_Macro_Dist_cm_Max) − log(Camera_Macro_Dist_cm_Min)), clamped 0–10. Lower focus distance = higher score.
          },
          "predicted_score": 8.39,
          // SCORING GUIDELINE: predicted_score (Score_4.7.1) = (0.40 × ultrawide_autofocus.subscore) + (0.60 × min_focus_distance_cm.subscore) if presence = true; otherwise 0.00. Minimum focus distance is weighted higher (60%) because it directly determines how close the lens can physically get to a subject.
          "final_score": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.39,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        },
        "4_7_2_telemacro_path": {
          // SCORING GOAL (4.7.2): Scores Telemacro (Telephoto Macro) capability. A telephoto macro lens enables close-up shots from a greater working distance (10–15 cm away), preventing the phone from casting a shadow and delivering natural background blur.
          "telemacro_presence": {
            "value": false,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": "N/A"
            // SCORING GUIDELINE: Binary gate. If value = false, Score_4.7.2 = 0.0 and telemacro_optical_x.subscore MUST be "N/A". If value = true, proceed to score telemacro_optical_x using the Section 4.7.2 formula.
          },
          "telemacro_optical_x": {
            "value": 0,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": "N/A"
            // SCORING GUIDELINE: Only evaluated if telemacro_presence = true. Apply the Section 4.7.2 formula: Score_4.7.2 = 7.0 + (3.0 × Zoom_Score / 10), where Zoom_Score = 10 × (log(magnification) − log(Camera_Telemacro_x_Min)) / (log(Camera_Telemacro_x_Max) − log(Camera_Telemacro_x_Min)), clamped 0–10. This guarantees a minimum of 7.0 for the architectural advantage of telemacro.
          },
          "predicted_score": 0.00,
          // SCORING GUIDELINE: predicted_score (Score_4.7.2) = 0.0 if telemacro_presence = false; otherwise derived from the telemacro formula above.
          "final_score": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 0.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        },
        "4_7_3_dedicated_path": {
          // SCORING GOAL (4.7.3): Scores a dedicated macro lens (a small fixed lens separate from the main/ultrawide/tele). Scores are capped at 6.00 to ensure dedicated lenses never outperform a high-quality Autofocus Ultrawide (max 10.00) or Telemacro (max 10.00).
          "dedicated_macro_megapixels": {
            "value": 0,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 0.00
            // SCORING GUIDELINE: Apply the Section 4.7.3 linear formula: Score_4.7.3 = clamp(dedicated_macro_megapixels, 0.00, 6.00). The score equals the Megapixel (MP) count, capped at 6.00. A value of 0 MP means no dedicated macro lens is present (score = 0.00). Values above 6 MP all score 6.00 maximum.
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
        "value": "8K",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Look up the max resolution in the Section 4.8 table. Use the following terms exclusively for "value" with related scores:
        //   • ≥ 4K Ultra HD (incl. 8K)   → 10.00
        //   • 1440p / QHD (2.5K)         → 8.00
        //   • 1080p Full HD              → 6.00
        //   • 720p HD                    → 3.00
        //   • ≤ 480p                     → 0.00
      },
      "4_9_rear_video_frames_per_second": {
        "maximum_frames_per_second_1080p_plus": {
          "value": 120,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 0.00,
        "final_score": 0.00
      },
      "4_10_video_hdr": {
        "value": "Dolby Vision",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.00
      },
      "4_11_video_encoding": {
        "professional_codec_support": {
          "value": "ProRes 4K60",
          "source": "https://www.tomsguide.com/reviews/iphone-15-pro-max",
          "exact_extract": "export ProRes footage via USB-C at up to 4K and 60 frames per second",
          "subscore": 10.00
        },
        "log_color_profile_support": {
          "value": "Apple Log",
          "source": "https://www.tomsguide.com/reviews/iphone-15-pro-max",
          "exact_extract": "export ProRes footage",
          "subscore": 10.00
        },
        "color_bit_depth": {
          "value": 10,
          "source": "https://www.gsmarena.com/apple_iphone_15_pro-12557.php",
          "exact_extract": "Display [...] 10-bit HDR",
          "subscore": 10.00
        },
        "predicted_score": 10.00,
        "final_score": 10.00
      },
      "4_12_slow_motion": {
        "maximum_frames_per_second": {
          "value": 120,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "resolution_megapixels": {
          "value": 8.3,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 0.00,
        "final_score": 0.00
      },
      "4_13_front_camera_resolution": {
        "value": 12,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.00
      },
      "4_14_front_camera_focus": {
        "value": "Autofocus",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.00
      },
      "4_15_front_camera_video": {
        "maximum_resolution_pixels": {
          "value": "4K",
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "maximum_frames_per_second": {
          "value": 60,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "high_dynamic_range_capability": {
          "value": "SDR",
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 0.00,
        "final_score": 0.00
      },
      "4_16_multiframe_photo": {
        "features": {
          "value": [
            "Advanced HDR",
            "Night Mode"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 0.00,
        "score_adjustment": {
          "booster_1": {
            "value": 1.05,
            "booster_title": "11_1_dxomark_24mp_texture_rendering"
          }
        },
        "final_score": 0.00
      },
      "4_17_semantic_ai": {
        "features": {
          "value": [
            "Semantic Segmentation"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 0.00,
        "score_adjustment": {
          "booster_1": {
            "value": 1.05,
            "booster_title": "11_3_dxomark_portrait_skin_tone_rendering"
          }
        },
        "final_score": 0.00
      },
      "4_18_generative_ai_tools": {
        "features": {
          "value": [
            "Magic Eraser"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 0.00,
        "final_score": 0.00
      }
    },
    "5_software_and_longevity": {
      "operating_system_version": {
        "value": "Android 14",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "skin": {
        "value": "One UI 6.1",
        "source": "TBD",
        "exact_extract": "Proof pending"
        // SCORING GUIDELINE: Record the exact OEM skin / platform name as declared by the manufacturer.
        //   Section 5.2 maps this string to a score. Known platforms:
        //   • iOS                                    → 10.00
        //   • Pixel UI / Stock Android               → 9.00
        //   • AOSP / Generic Stock Android           → 9.00
        //   • Fairphone OS                           → 9.00
        //   • Nothing OS                             → 9.00
        //   • Motorola MyUX / Hello UI               → 8.00
        //   • Sony Xperia UI                         → 8.00
        //   • Nokia (Stock Android)                  → 8.00
        //   • Sharp AQUOS UI                         → 8.00
        //   • ASUS ZenUI / ROG UI                    → 7.00
        //   • Samsung One UI                         → 6.00
        //   • OxygenOS (OnePlus)                     → 6.00
        //   • Redmagic OS                            → 6.00
        //   • Honor MagicOS                          → 5.00
        //   • Vivo FunTouch OS / OriginOS            → 5.00
        //   • ColorOS (Oppo)                         → 5.00
        //   • Realme UI                              → 5.00
        //   • LG UX (Legacy)                         → 5.00
        //   • HTC Sense (Legacy)                     → 5.00
        //   • ZTE MiFavor UI / MyOS                  → 4.00
        //   • HyperOS (Xiaomi)                       → 4.00
        //   • Huawei EMUI / HarmonyOS                → 3.00
        //   • MIUI (Legacy Xiaomi)                   → 3.00
        //   • Tecno HiOS / Infinix XOS / Itel OS     → 2.00
        //   If unlisted, score = N/A (update Section 5.2 first).
      },
      "5_1_support_longevity": {
        "years_operating_system": {
          "value": 7,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "years_security": {
          "value": 7,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 0.00,
        "final_score": 0.00
      },
      "5_2_system_cleanliness_control": {
        "platform_score": 6.00,
        // SCORING GUIDELINE: platform_score is a direct lookup from the `skin` field above via the Section 5.2 Platform Cleanliness table. Do not derive this value from any formula — just look up the skin string and copy the table score here.
        "predicted_score": 6.00,
        "final_score": 6.00
      },
      "5_3_ai_feature_suite": {
        "visual_screen_search": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "live_speech_translation": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "content_summarization": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "writing_tools": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "on_device_processing": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "predicted_score": 10.00,
        "final_score": 0.00
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
            // GUIDELINE: Whether the display adjusts its refresh rate dynamically between min_hz and max_hz. true = LTPO/adaptive panel; false = fixed-rate panel (always at max_hz). Controls the B.2.2 formula: effective_hz = adaptive ? (min_hz + max_hz) / 2 : max_hz.
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "dependencies": [
            "2_display.2_1_panel_architecture",
            "2_display.2_6_motion_smoothness.maximum_refresh_rate_hz"
          ],
          "breakdown": {
            "panel_technology_score": 9.00,
            "refresh_efficiency_score": 7.74,
            "resolution_efficiency_score": 5.21
          },
          "score": 7.42
        },
        "b_3_connectivity_efficiency": {
          "dependencies": [
            "7_connectivity.7_1_cellular_capabilities",
            "7_connectivity.7_3_wifi_standard"
          ],
          "breakdown": {
            "cellular_score": 0.00,
            "wifi_score": 0.00
          },
          "score": 0.00
        },
        "b_4_thermal_efficiency": {
          "dependencies": [
            "6_processing_power_and_performance.6_10_thermal_dissipation_stability"
          ],
          "score": 8.20
        },
        "hardware_efficiency_index_total_score": 7.14
      },
      "layer_c_software_optimization": {
        "dependencies": [
          "5_software_and_longevity.operating_system_version",
          "5_software_and_longevity.5_2_system_cleanliness_control"
        ],
        "breakdown": {
          "c_1_operating_system_generation": 10.00,
          "c_2_bloatware": 6.00
        },
        "software_optimization_index_total_score": 8.40
      },
      "predicted_score": 7.16,
      "benchmarks": {
        "gsmarena_active_use": {
          "hours": 16.75,
          "normalized_score": 5.84
        },
        "phonearena_battery_life": {
          "hours": 10.5,
          "normalized_score": 8.82
        }
      },
      "final_score": 7.33,
      "score_adjustment": {
        "booster": 1.024,
        "source": "GSMArena Active Use + PhoneArena Battery Life"
      }
    },
    "8_2_wired_charging_speed": {
      "watts": {
        "value": 45,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.00,
      "final_score": 0.00
    },
    "8_3_wireless_charging_speed": {
      "watts": {
        "value": 15,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.00,
      "final_score": 0.00
    },
    "8_4_reverse_wired": {
      "watts": {
        "value": 0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.00,
      "final_score": 0.00
    },
    "8_5_reverse_wireless": {
      "watts": {
        "value": 4.5,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.00,
      "final_score": 0.00
    },
    "8_6_charger_in_box": {
      "included_watts": {
        "value": 0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.00,
      "final_score": 0.00
    }
  },
  "9_financial_and_economic_value": {
    "9_1_price": {
      "usd": {
        "value": 1299,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.80,
      "final_score": 0.80
    },
    "9_2_manufacturer_warranty_commitment": {
      "months": {
        "value": 12,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "value": {
        "value": "1 Year Standard",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 3.00,
      "final_score": 3.00
    },
    "9_3_repairability": {
      "ifixit_score": 8.00,
      "european_union_repairability_index": {
        "value": 4.00,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "european_union_converted_score": 8.00,
      "predicted_score": 8.00,
      "confidence": {
        "value": "High",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "final_score": 8.00
    }
  },
  "10_miscellaneous": {
    "10_1_stylus_hardware_system_support": {
      "value": "Integrated active stylus + dedicated digitizer + Bluetooth features",
      "source": "TBD",
      "exact_extract": "Proof pending",
      "predicted_score": 10.00,
      "final_score": 10.00
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
