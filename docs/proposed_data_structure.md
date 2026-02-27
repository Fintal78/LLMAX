# Ultimate Smartphone Data Structure Proposal (v5.1)

This schema is strictly aligned with the `scoring_rules.md` v8.0.

```json
{
  // GUIDELINE: All scoring formulas and lookup tables referenced as "Section X.X" or "§X.X" throughout this document are defined in scoring_rules.md. All numeric constants (e.g. _Min / _Max thresholds) are from scoring_constants.md. There is no need to repeat these file names in individual Source comments below.
  
  // GUIDELINE (meta): Tracks the state of this document itself. Update both fields every time you modify this file.
  "meta": {
    "schema_version": "5.1",
    // GUIDELINE: Version of the data structure schema. Increment only when a structural change is made (new fields added, renamed, or removed). Use semantic versioning (Major.Minor).
    "last_updated": "2026-02-27"
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
        // SCORING GUIDELINE: Look up the frame material in the Section 1.1.A table. Use the following terms exclusively with related scores:
        //   • Titanium Alloy       → 10.0
        //   • Stainless Steel      → 8.5
        //   • Aluminum Alloy       → 7.0
        //   • Polymer Composite    → 4.0
        //   • Not Disclosed        → 0.0
      },
      "back_material": {
        "value": "Strengthened Glass",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.00
        // SCORING GUIDELINE: Look up the back panel material in the Section 1.1.B table. Use the following terms exclusively with related scores:
        //   • Ceramic              → 10.0
        //   • Strengthened Glass   → 8.0
        //   • Standard Glass       → 6.0
        //   • Polymer              → 4.0
        //   • Not Disclosed        → 0.0
      },
      // SCORING GUIDELINE: predicted_score = (0.6 × frame_material.subscore) + (0.4 × back_material.subscore). Source: §1.1 Materials formula for Materials Score.
      "predicted_score": 9.20,
      "final_score": {
        "value": 9.20,
        // SCORING GUIDELINE: Definitive materials score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "1_2_durability": {
      // GUIDELINE: `ip_rating` stores the full human-readable IP (Ingress Protection) composite string (e.g. "IP68") as declared by the manufacturer. It is not scored directly but the two individual digits extracted for scoring are `dust_protection_digit` and `water_protection_digit`, see below — always parse those from this `ip_rating.value` string.
      "ip_rating": {
        "value": "IP68",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A" // no score here, it will be calculated below from dust_protection_digit and water_protection_digit
      },
      // SCORING GOAL: Scores dust and water resistance separately using the two digits of the IP (Ingress Protection) rating defined by IEC standard 60529. The full composite string is available at `1_2_durability.ip_rating.value` for reference.
      "dust_protection_digit": {
        "value": 6,
        "source": "1_2_durability.ip_rating.value",
        "exact_extract": "6",
        "subscore": 10.00
        // SCORING GUIDELINE: Look up the first digit of the IP rating in the Section 1.2.A table. Use the following terms exclusively with related scores:
        //   • Digit 6    → 10.0
        //   • Digit 5    → 8.0
        //   • Digit 4    → 6.0
        //   • Digit 3    → 4.0
        //   • Digit 2    → 2.0
        //   • Digit 0–1  → 0.0
      },
      "water_protection_digit": {
        "value": 8,
        "source": "1_2_durability.ip_rating.value",
        "exact_extract": "8",
        "subscore": 9.00
        // SCORING GUIDELINE: Look up the second digit of the IP rating in the Section 1.2.B table. Use the following terms exclusively with related scores:
        //   • Digit 9    → 10.0
        //   • Digit 8    → 9.0
        //   • Digit 7    → 8.0
        //   • Digit 6    → 6.0
        //   • Digit 5    → 4.0
        //   • Digit 4    → 2.0
        //   • Digit 0–3  → 0.0
      },
      // SCORING GUIDELINE: predicted_score = (0.5 × dust_protection_digit.subscore) + (0.5 × water_protection_digit.subscore). Source: §1.2 IP Score formula.
      "predicted_score": 9.50,
      "final_score": {
        "value": 9.50,
        // SCORING GUIDELINE: Definitive durability score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "1_3_glass_protection": {
      // SCORING GOAL: Scores the protective glass type on the display, known as Display Glass Protection (DGP), based on the manufacturer-declared glass generation's certified drop and scratch resistance class.
      "glass_generation": {
        "value": "Gorilla Glass Armor",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.0
        // SCORING GUIDELINE: Look up the declared glass type in the Section 1.3 table. Use the following terms exclusively with related scores:
        //   • Gorilla Glass Armor                  → 10.0
        //   • Ceramic Shield (current gen)         → 9.5
        //   • Gorilla Glass Victus 2               → 9.0
        //   • Gorilla Glass Victus or Victus+      → 8.0
        //   • Dragontrail Star or Dragontrail Pro  → 8.0
        //   • Gorilla Glass 5 or 6                 → 7.0
        //   • Dragontrail X                        → 7.0
        //   • Gorilla Glass 3                      → 5.0
        //   • Panda Glass                          → 5.0
        //   • Dragontrail (standard)               → 5.0
        //   • Tempered Glass                       → 3.0
        //   • Glass (Unspecified)                  → 2.0
        //   • Plastic or No Glass                  → 0.0
      },
      // SCORING GUIDELINE: predicted_score directly inherits glass_generation.subscore.
      "predicted_score": 10.00,
      "final_score": {
        "value": 10.00,
        // SCORING GUIDELINE: Definitive glass protection score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
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
      // SCORING GUIDELINE: predicted_score directly inherits thickness_mm.subscore.
      "predicted_score": 3.50,
      "final_score": {
        "value": 3.50,
        // SCORING GUIDELINE: Definitive thickness score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
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
      // SCORING GUIDELINE: predicted_score directly inherits weight_g.subscore.
      "predicted_score": 1.64,
      "final_score": {
        "value": 1.64,
        // SCORING GUIDELINE: Definitive weight score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
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
      // SCORING GUIDELINE: predicted_score directly inherits width_mm.subscore.
      "predicted_score": 0.00,
      "final_score": {
        "value": 0.00,
        // SCORING GUIDELINE: Definitive ergonomics score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
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
      //   Assign "LTPO OLED" (9.0) ONLY when LTPO backplane OR a Tier-9 name below is confirmed.
      // ─────────────────────────────────────────────────────────────────────────────
      "panel_type_lookup": {
        "tier_10_tandem_oled": {
          "canonical": "Tandem OLED",
          "score": 10.0,
          "marketing_names": [
            "Tandem OLED",
            "Dual-Layer OLED"
          ]
        },
        "tier_9_ltpo_oled": {
          "canonical": "LTPO OLED",
          "score": 9.0,
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
          "score": 8.0,
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
          "score": 6.0,
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
          "score": 2.0,
          "marketing_names": [
            "PLS TFT",
            "PLS",
            "TFT LCD",
            "TFT (no IPS qualifier)"
          ]
        },
        "tier_0_tn_lcd_or_legacy": {
          "canonical": "TN LCD or Legacy",
          "score": 0.0,
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
        // SCORING GUIDELINE: Find the spec-sheet label in panel_type_lookup above → copy the canonical string here and its score into subscore. Use the following terms exclusively with related scores:
        //   • Tandem OLED        → 10.0
        //   • LTPO OLED          → 9.0
        //   • AMOLED or OLED     → 8.0
        //   • IPS LCD            → 6.0
        //   • TFT or PLS LCD     → 2.0
        //   • TN LCD or Legacy   → 0.0
      },
      // SCORING GUIDELINE: predicted_score directly inherits panel_type.subscore.
      "predicted_score": 9.00,
      "final_score": {
        "value": 9.00,
        // SCORING GUIDELINE: Definitive panel architecture score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
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
        // SCORING GUIDELINE: Apply the Section 2.2 logarithmic formula: HBM_Score = 10 × (log(hbm_nits) − log(Display_HBM_Nits_Min)) / (log(Display_HBM_Nits_Max) − log(Display_HBM_Nits_Min)), clamped 0–10. Fallback: if hbm_nits is unavailable, estimate hbm_nits = peak_nits / 1.5.
      },
      // SCORING GUIDELINE: predicted_score = (0.7 × hbm_nits.subscore) + (0.3 × peak_nits.subscore). HBM is weighted at 70% because it reflects true daily outdoor usability; Peak at 30% for HDR media capability.
      "predicted_score": 7.37,
      "final_score": {
        "value": 7.37,
        // SCORING GUIDELINE: Definitive brightness score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_3_color_gamut_coverage": {
      // SCORING GOAL: Scores how much of the DCI-P3 (Digital Cinema Initiatives P3) professional color space the display can reproduce. A wider gamut means richer, more saturated colors in photos, videos, and HDR content.
      "dci_p3_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Apply the Section 2.3 linear formula: Score = 10 × (dci_p3_percent − Display_P3_Coverage_Percent_Min) / (Display_P3_Coverage_Percent_Max − Display_P3_Coverage_Percent_Min), clamped 0–10.
      },
      "srgb_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A"
        // SCORING GUIDELINE: sRGB coverage is a fallback data source only. Its subscore is always "N/A". Use it to estimate DCI-P3 ONLY when dci_p3_percent is not available from any source: DCI-P3_estimate = min(srgb_percent × 0.75, 100). Once converted, score the estimate via the dci_p3_percent formula above.
      },
      // SCORING GUIDELINE: predicted_score directly inherits dci_p3_percent.subscore.
      "predicted_score": 10.00,
      "final_score": {
        "value": 10.00,
        // SCORING GUIDELINE: Definitive color gamut score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster (e.g., when an expert review validates exceptional factory calibration accuracy).
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.2"), or "No" if unadjusted. Example: booster "11_2_toms_guide_display_factory_calibration" would be referenced here.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_4_hdr_format_support": {
      // SCORING GOAL: Scores which High Dynamic Range (HDR) video formats the display officially supports. Dynamic HDR formats optimize brightness and colour frame-by-frame, unlocking the full quality of premium streaming content.
      "formats": {
        "value": [
          "HDR10+",
          "HDR10",
          "HLG"
        ],
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.0
        // SCORING GUIDELINE: Identify the highest-tier format combination supported and look it up in the Section 2.4 table.
        //   • Universal Dynamic HDR (Dolby Vision + HDR10+ + HDR10)  → 10.0
        //   • Primary Dynamic HDR (Dolby Vision + HDR10 only)        → 9.0
        //   • Alternative Dynamic HDR (HDR10+ + HDR10 only)         → 8.0
        //   • Basic Static HDR (HDR10 only)                         → 6.0
        //   • No HDR                                                → 0.0
        //   Note: HLG is supplementary and does not change the tier.
      },
      // SCORING GUIDELINE: predicted_score directly inherits formats.subscore.
      "predicted_score": 8.00,
      "final_score": {
        "value": 8.00,
        // SCORING GUIDELINE: Definitive HDR format score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_5_resolution_density": {
      // SCORING GOAL: Scores pixel density (Pixels Per Inch, PPI) as a measure of display sharpness. Higher PPI means text and images look crisp with no visible pixels.
      "resolution_width_px": {
        // GUIDELINE: Horizontal pixel count of the display (e.g. 1440 for QHD+). Used to derive PPI via PPI = √(width² + height²) / diagonal_inches. Source from manufacturer spec sheet or GSMArena.
        "value": 1440,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "resolution_height_px": {
        // GUIDELINE: Vertical pixel count of the display (e.g. 3120 for QHD+). Used together with resolution_width_px to derive PPI. Source from manufacturer spec sheet or GSMArena.
        "value": 3120,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "ppi": {
        "value": 505,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.43
        // SCORING GUIDELINE: Apply the Section 2.5 logarithmic formula: Score = 10 × (log(ppi) − log(Display_PPI_Min)) / (log(Display_PPI_Max) − log(Display_PPI_Min)), clamped 0–10. Logarithmic because human visual acuity has diminishing returns at high PPI. Derive ppi if not published: PPI = √(resolution_width_px² + resolution_height_px²) / diagonal_inches.
      },
      // SCORING GUIDELINE: predicted_score directly inherits ppi.subscore.
      "predicted_score": 8.43,
      "final_score": {
        "value": 8.43,
        // SCORING GUIDELINE: Definitive resolution density score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_6_refresh_rate_max_hz": {
      // SCORING GOAL: Scores Motion Smoothness via maximum refresh rate. Higher Hertz (Hz) means scrolling and animations look smoother. 120 Hz and above are perceptibly superior to standard 60 Hz.
      "max_hz": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.55
        // SCORING GUIDELINE: Apply the Section 2.6 logarithmic formula: Score = 10 × (log(max_hz) − log(Display_Refresh_Rate_Hz_Min)) / (log(Display_Refresh_Rate_Hz_Max) − log(Display_Refresh_Rate_Hz_Min)), clamped 0–10. Logarithmic because the perceptual smoothness gain of each additional Hz diminishes at high frequencies.
      },
      // SCORING GUIDELINE: predicted_score directly inherits max_hz.subscore.
      "predicted_score": 7.55,
      "final_score": {
        "value": 7.55,
        // SCORING GUIDELINE: Definitive motion smoothness score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_7_touch_responsiveness": {
      // SCORING GOAL: Scores touch sampling rate as a measure of how instantly the screen responds to finger input. Higher rates produce a "glued to your finger" feel, critical for gaming and UI fluidity.
      "sampling_rate_hz": {
        "value": 240,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 5.00
        // SCORING GUIDELINE: Apply the Section 2.7 logarithmic formula: Score = 10 × (log(sampling_rate_hz) − log(Display_Touch_Sampling_Hz_Min)) / (log(Display_Touch_Sampling_Hz_Max) − log(Display_Touch_Sampling_Hz_Min)), clamped 0–10. Logarithmic because the perceptual benefit of a faster sampling rate diminishes at high frequencies.
      },
      // SCORING GUIDELINE: predicted_score directly inherits sampling_rate_hz.subscore.
      "predicted_score": 5.00,
      "final_score": {
        "value": 5.00,
        // SCORING GUIDELINE: Definitive touch responsiveness score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_8_screen_to_body_ratio": {
      // SCORING GOAL: Scores the Screen-to-Body Ratio (SBR) — how much of the front face is active display versus border (bezel). Higher percentage means a more immersive, modern design.
      "percent": {
        "value": 88.5,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.64
        // SCORING GUIDELINE: Apply the Section 2.8 linear formula: Score = 10 × ((percent − Display_SBR_Percent_Min) / (Display_SBR_Percent_Max − Display_SBR_Percent_Min)), clamped 0–10. Linear because each percentage point represents a proportional increase in visible display area.
      },
      // SCORING GUIDELINE: predicted_score directly inherits percent.subscore.
      "predicted_score": 8.64,
      "final_score": {
        "value": 8.64,
        // SCORING GUIDELINE: Definitive screen-to-body ratio score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_9_screen_size": {
      // SCORING GOAL: Scores the physical display diagonal as a measure of immersion and media consumption experience. Larger screens offer more real estate for video, gaming, and productivity.
      "diagonal_inches": {
        "value": 6.8,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.93
        // SCORING GUIDELINE: Apply the Section 2.9 quadratic formula: Score = 10 × ((diagonal_inches² − Display_Size_Inch_Min²) / (Display_Size_Inch_Max² − Display_Size_Inch_Min²)), clamped 0–10. Quadratic because usable screen real estate scales as area (proportional to the square of the diagonal), heavily rewarding larger screens.
      },
      // SCORING GUIDELINE: predicted_score directly inherits diagonal_inches.subscore.
      "predicted_score": 6.93,
      "final_score": {
        "value": 6.93,
        // SCORING GUIDELINE: Definitive screen size score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_10_eye_comfort": {
      // SCORING GOAL: Evaluates how the screen dims at low brightness levels to prevent eye strain and headaches. It scores either the perfect continuous light of Direct Current (DC) Dimming, or scales the Pulse-Width Modulation (PWM) frequency if flickering is present.
      "dimming_hardware": {
        "pwm_dimming_active": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": "N/A"
          // SCORING GUIDELINE: If value = true then PWM Dimming is active, this subscore remains "N/A" as the score will be defined by the frequency 'pwm_dimming_hz'. If value = false then DC Dimming is active, this specific subscore is evaluated as 10.0 without any impact of 'pwm_dimming_hz'.
        },
        "pwm_dimming_hz": {
          "value": 492,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 4.07
          // SCORING GUIDELINE: If `pwm_dimming_active` = true, evaluate this specific subscore using the Section 2.10.2 logarithmic formula with the provided value of 'pwm_dimming_hz'. If `pwm_dimming_active` = false, this specific subscore MUST be "N/A".
        }
      },
      // SCORING GUIDELINE: The predicted score directly inherits whichever subscore is NOT "N/A" from the `dimming_hardware` block above.
      "predicted_score": 4.07,
      "final_score": {
        "value": 4.07,
        // SCORING GUIDELINE: The definitive eye comfort score. It inherits the `predicted_score` unless mathematically modified by a Section 11 expert review Booster. (This section has no Benchmark or Neighbor equivalents).
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 rule applied (e.g., "11.5"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "2_11_display_benchmark_final_scoring": {
      // SCORING GOAL: Produces the overall Display Final Score using a three-method hierarchy (A→B→C). Method A uses the DXOMARK Display benchmark when available. Method B uses Nearest Neighbor Interpolation when only similar devices have benchmarks. Method C (Predictor) is the fallback when no benchmarks exist for any similar device.
      "dxomark_display_score": {
        "value": 150,
        "source": "https://www.dxomark.com/smartphones/#display",
        "exact_extract": "Proof pending",
        "subscore": 9.34
        // SCORING GUIDELINE: Apply the Section 2.11 Method A logarithmic normalization: Score = 10 × (log(dxomark_display_score) − log(Display_DXO_Score_Min)) / (log(Display_DXO_Score_Max) − log(Display_DXO_Score_Min)), clamped 0–10. DXOMARK scores cover readability, colour, video, motion, touch. If no DXOMARK score is available set value to null and subscore to "N/A".
      },
      // SCORING GUIDELINE: predicted_score = weighted sum of sub-section predicted scores per Method C formula (Section 2.11): (0.15 × 2.1) + (0.20 × 2.2) + (0.10 × 2.3) + (0.10 × 2.4) + (0.10 × 2.5) + (0.15 × 2.6) + (0.10 × 2.7) + (0.10 × 2.10). Sections 2.8 and 2.9 are excluded because DXOMARK does not evaluate physical dimensions.
      "predicted_score": 7.51,
      "final_score": {
        "value": 9.34,
        // SCORING GUIDELINE: Use Method A if dxomark_display_score is available (dxomark_display_score.subscore becomes the final value). Otherwise use Method B (Nearest Neighbor Interpolation per Section 2.11 Euclidean distance search). Otherwise fall back to Method C (predicted_score). No Booster applies to Benchmark or Neighbor Interpolation results.
        "method_used": "Benchmark (DXOMARK)",
        // SCORING GUIDELINE: Set to "Benchmark (DXOMARK)" for Method A, "Neighbor Interpolation" for Method B, or "Predictor" for Method C.
        "booster": "No",
        // SCORING GUIDELINE: Must always be "No" for Benchmark and Neighbor Interpolation methods. Boosters are only allowed on Predictor results.
        "confidence": "N/A"
        // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor. "High", "Medium", or "Low" only when 2 independent benchmarks are cross-referenced.
      }
    }
  },
  "3_audio": {
    "3_1_speaker_quality": {
      // SCORING GOAL: Scores the physical speaker hardware configuration (Speaker System Capability, SSC) for audio output without headphones. Evaluates speaker count, placement, and channel symmetry.
      "speaker_configuration": {
        "value": "Balanced Stereo (Hybrid)",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.0
        // SCORING GUIDELINE: Look up the configuration in the Section 3.1 table.
        //   • Balanced / Symmetrical Stereo (two identical drivers)  → 10.0
        //   • Standard Hybrid Stereo (earpiece + bottom driver)      → 7.0
        //   • Mono Speaker                                           → 3.0
        //   • No Usable Speaker                                      → 0.0
        //   Note: Verify via spec sheet or a review that explicitly states symmetry for 10.0.
      },
      // SCORING GUIDELINE: predicted_score directly inherits speaker_configuration.subscore.
      "predicted_score": 7.00,
      "final_score": {
        "value": 7.00,
        // SCORING GUIDELINE: Definitive speaker quality score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "3_2_playback_audio_processing_immersion": {
      // SCORING GOAL: Scores Playback Audio Processing & Immersion (PAPI) as a composite of two sub-criteria: audio format decoding capability (3.2.1, weight 50%) and spatial audio rendering capability (3.2.2, weight 50%).
      "audio_format_decode": {
        // SCORING GUIDELINE: 3.2.1 Audio Format Decode Support. Per the hierarchical category rule, only the highest-tier supported format is stored. Identify the best combination from the Section 3.2.1 table.
        "best_supported_format": {
          "value": "Dolby Atmos ONLY",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.0
          // SCORING GUIDELINE: Look up the highest-tier combination in the Section 3.2.1 table.
          //   • Dolby Atmos AND DTS:X                           → 10.0
          //   • Dolby Atmos ONLY                                → 8.0
          //   • Multichannel Surround (Dolby Digital/DTS) only  → 5.0
          //   • Stereo only                                     → 0.0
        }
      },
      "spatial_audio_rendering": {
        // SCORING GUIDELINE: 3.2.2 Spatial Audio Rendering. Per the hierarchical category rule, only the highest-tier capability is stored.
        "best_spatial_capability": {
          "value": "Spatial audio (Static, no head tracking)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.0
          // SCORING GUIDELINE: Look up in the Section 3.2.2 table.
          //   • Spatial audio WITH Dynamic Head Tracking (gyroscope-anchored soundstage)  → 10.0
          //   • Static spatial audio (no head tracking)                                   → 7.0
          //   • No spatial rendering                                                      → 0.0
        }
      },
      // SCORING GUIDELINE: predicted_score = (0.5 × audio_format_decode.best_supported_format.subscore) + (0.5 × spatial_audio_rendering.best_spatial_capability.subscore). Both sub-criteria are equally weighted per the PAPI formula in Section 3.2.
      "predicted_score": 7.5,
      "final_score": {
        "value": 7.5,
        // SCORING GUIDELINE: Definitive PAPI score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "3_3_wired_audio_capability": {
      // SCORING GOAL: Scores native wired audio output capability. Evaluates the best natively supported wired audio tier without requiring powered external accessories. Per the hierarchical category rule, only the highest supported tier is stored.
      "wired_audio_tier": {
        "value": "USB-C digital audio only (dongle required)",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 3.0
        // SCORING GUIDELINE: Look up the highest-tier natively supported option in the Section 3.3 table.
        //   • 3.5mm headphone jack (native analog)               → 10.0
        //   • USB-C with documented analog audio output          → 6.0
        //   • USB-C digital audio only (dongle required)         → 3.0
        //   • No wired audio support                             → 0.0
      },
      // SCORING GUIDELINE: predicted_score directly inherits wired_audio_tier.subscore.
      "predicted_score": 3.0,
      "final_score": {
        "value": 3.0,
        // SCORING GUIDELINE: Definitive wired audio score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "3_4_microphone_audio_recording": {
      // SCORING GOAL: Scores Microphone & Audio Recording (MAR) as a composite of hardware count (3.4.1, 30%), recording channels (3.4.2, 30%), and advanced capture features (3.4.3, 40%).
      "mhc": {
        // SCORING GUIDELINE: 3.4.1 Microphone Hardware Count (MHC). The subscore is placed on the data field itself, not in a separate score object.
        "microphone_count": {
          "value": 3,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.0
          // SCORING GUIDELINE: Look up count in the Section 3.4.1 table.
          //   • ≥4 microphones   → 10.0
          //   • 3                 → 8.0
          //   • 2                 → 5.0
          //   • 1                 → 2.0
          //   • Unknown           → 0.0
        }
      },
      "rcm": {
        // SCORING GUIDELINE: 3.4.2 Recording Channels & Modes (RCM). Per the hierarchical category rule, store only the highest-tier recording capability.
        "recording_channels": {
          "value": "Stereo",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.0
          // SCORING GUIDELINE: Look up in the Section 3.4.2 table.
          //   • Multi-channel / Spatial audio   → 10.0
          //   • Stereo                          → 8.0
          //   • Mono                            → 5.0
          //   • Voice-only / Unclear            → 0.0
        }
      },
      "acf": {
        // SCORING GUIDELINE: 3.4.3 Advanced Capture Features (ACF). The list is additive: each documented feature from the Section 3.4.3 checklist (Directional Zoom, Wind Noise Reduction, Voice Focus, Pro Mic Support) adds +2.5 points, capped at 10.0.
        "features": {
          "value": [
            "Directional/Audio Zoom",
            "Wind noise reduction"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 5.0
          // SCORING GUIDELINE: Count the number of features in the list and apply: subscore = 2.5 × count (clamped 0–10). Example: 2 features × 2.5 = 5.0. Always populate the full list from the Omni-Scan Rule — do not selectively omit.
        }
      },
      // SCORING GUIDELINE: predicted_score = (0.30 × mhc.microphone_count.subscore) + (0.30 × rcm.recording_channels.subscore) + (0.40 × acf.features.subscore). Weights from the MAR formula in Section 3.4.
      "predicted_score": 6.80,
      "final_score": {
        "value": 6.80,
        // SCORING GUIDELINE: Definitive MAR score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    }
  },
  "4_camera_systems": {
    "camera_hardware_specs": {
      "rear": [
        {
          "role": {
            "value": "Main",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "sensor": {
            "value": "ISOCELL HP2",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "mp": {
            "value": 200,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "aperture": {
            "value": "f/1.7",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "ois": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        {
          "role": {
            "value": "Tele 5x",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "sensor": {
            "value": "IMX854",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "mp": {
            "value": 50,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "aperture": {
            "value": "f/3.4",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "ois": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        {
          "role": {
            "value": "Tele 3x",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "sensor": {
            "value": "IMX754",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "mp": {
            "value": 10,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "aperture": {
            "value": "f/2.4",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "ois": {
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        {
          "role": {
            "value": "Ultrawide",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "sensor": {
            "value": "IMX564",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "mp": {
            "value": 12,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "aperture": {
            "value": "f/2.2",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "fov": {
            "value": 120,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        }
      ]
    },
    "4_1_main_sensor_size": {
      // SCORING GOAL: Scores the main camera sensor size as the primary determinant of image quality. Larger sensors capture more light, yielding better low-light performance, more dynamic range, and natural background blur (bokeh).
      "optical_format": {
        "value": "1/1.3 inches",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.11
        // SCORING GUIDELINE: Apply the Section 4.1 logarithmic formula: Score = 10 × (log(Size_Inch) − log(Camera_Main_Sensor_Inch_Min)) / (log(Camera_Main_Sensor_Inch_Max) − log(Camera_Main_Sensor_Inch_Min)), clamped 0–10. Convert the optical format string to a decimal (e.g., "1/1.3 inches" → 0.769). Logarithmic because the real-world photographic benefit of a larger sensor follows a diminishing return curve.
      },
      // SCORING GUIDELINE: predicted_score directly inherits optical_format.subscore.
      "predicted_score": 8.11,
      "final_score": {
        "value": 8.11,
        // SCORING GUIDELINE: Definitive sensor size score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "4_2_main_camera_aperture": {
      // SCORING GOAL: Scores the main camera lens aperture (f-number). Wider apertures (lower f-number) admit more light into the sensor, improving low-light performance and enabling natural background blur.
      "aperture_f_stop": {
        "value": "f/1.7",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.40
        // SCORING GUIDELINE: Apply the Section 4.2 inverted logarithmic formula: Score = 10 × (log(Camera_Main_Aperture_f_Max) − log(f_stop)) / (log(Camera_Main_Aperture_f_Max) − log(Camera_Main_Aperture_f_Min)), clamped 0–10. Parse the f-stop string to a decimal (e.g., "f/1.7" → 1.7). The formula is inverted because lower f-numbers are better.
      },
      // SCORING GUIDELINE: predicted_score directly inherits aperture_f_stop.subscore.
      "predicted_score": 6.40,
      "final_score": {
        "value": 6.40,
        // SCORING GUIDELINE: Definitive aperture score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "4_3_main_camera_resolution": {
      // SCORING GOAL: Scores the main sensor's maximum pixel count in Megapixels (MP). Higher resolution allows finer detail capture and more flexible cropping, especially in good lighting conditions.
      "mp": {
        "value": 200,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Apply the Section 4.3 logarithmic formula: Score = 10 × (log(mp) − log(Camera_Main_Resolution_MP_Min)) / (log(Camera_Main_Resolution_MP_Max) − log(Camera_Main_Resolution_MP_Min)), clamped 0–10. Logarithmic because beyond ~50 MP, real-world detail gains hit a diffraction ceiling.
      },
      // SCORING GUIDELINE: predicted_score directly inherits mp.subscore.
      "predicted_score": 10.00,
      "final_score": {
        "value": 10.00,
        // SCORING GUIDELINE: Definitive resolution score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "4_4_image_stabilization": {
      // SCORING GOAL: Scores the Optical Image Stabilization (OIS) or equivalent mechanism used to compensate for hand shake. Better stabilization produces sharper low-light photos and smoother video.
      "stabilization_type": {
        "value": "Lens-Based OIS",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.0
        // SCORING GUIDELINE: Look up the mechanism in the Section 4.4 table.
        //   • Multi-Axis Gimbal / Multi-Sensor Shift     → 10.0
        //   • Sensor-Shift OIS                           → 9.0
        //   • Lens-Based OIS                             → 8.0
        //   • EIS (Electronic Image Stabilization) only  → 5.0
        //   • None                                       → 0.0
        //   Note: "Standard OIS" maps to Lens-Based OIS (8.0).
      },
      // SCORING GUIDELINE: predicted_score directly inherits stabilization_type.subscore.
      "predicted_score": 8.00,
      "final_score": {
        "value": 8.00,
        // SCORING GUIDELINE: Definitive stabilization score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "4_5_ultrawide_capability": {
      // SCORING GOAL: Scores Ultrawide Camera Capability (UCC) as a composite of Field of View (FOV, 55%) and sensor size (45%), gated by the presence of an ultrawide lens. A wider FOV and larger sensor both directly improve the quality of wide-perspective photography.
      "presence": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A"
        // SCORING GUIDELINE: Binary gate — this field has no numeric subscore. If value = false, the entire UCC score is 0.0 and all other subscores in this subsection MUST be "N/A". If value = true, proceed to score fov_degrees and sensor_size_format.
      },
      "fov_degrees": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.67
        // SCORING GUIDELINE: Apply the Section 4.5.2 linear formula: Score = 10 × (fov_degrees − Camera_Ultrawide_FOV_Deg_Min) / (Camera_Ultrawide_FOV_Deg_Max − Camera_Ultrawide_FOV_Deg_Min), clamped 0–10. Only evaluated if presence = true.
      },
      "sensor_size_format": {
        "value": "1/2.0",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Apply the Section 4.5.3 logarithmic formula: Score = 10 × (log(Size_Inch) − log(Camera_Ultrawide_Sensor_Inch_Min)) / (log(Camera_Ultrawide_Sensor_Inch_Max) − log(Camera_Ultrawide_Sensor_Inch_Min)), clamped 0–10. Convert format string to decimal (e.g., "1/2.0" → 0.5). Only evaluated if presence = true.
      },
      // SCORING GUIDELINE: predicted_score = (0.55 × fov_degrees.subscore) + (0.45 × sensor_size_format.subscore) if presence = true; otherwise predicted_score = 0.0. FOV is weighted 55% because it is the primary purpose of an ultrawide lens, while sensor size (45%) governs low-light quality.
      "predicted_score": 8.17,
      "final_score": {
        "value": 8.17,
        // SCORING GUIDELINE: Definitive UCC score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "4_6_zoom_capability": {
      // SCORING GOAL: Scores optical zoom power. Optical zoom allows sharp photos of distant subjects (e.g., concert, wildlife) without digital quality loss. Only true optical magnification is counted; digital/crop zoom is excluded.
      "optical_zoom_x": {
        "value": 5,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.99
        // SCORING GUIDELINE: Apply the Section 4.6 logarithmic formula: Score = 10 × (log(optical_zoom_x) − log(Camera_Zoom_Optical_x_Min)) / (log(Camera_Zoom_Optical_x_Max) − log(Camera_Zoom_Optical_x_Min)), clamped 0–10. Logarithmic because the reach improvement from 1x to 3x is transformational, while the difference between 10x and 12x is marginal.
      },
      // SCORING GUIDELINE: predicted_score directly inherits optical_zoom_x.subscore.
      "predicted_score": 6.99,
      "final_score": {
        "value": 6.99,
        // SCORING GUIDELINE: Definitive zoom score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "4_7_macro_capability": {
      // SCORING GOAL: Scores Macro Capability & Close-Focus Performance (MCFP). Evaluates three hardware paths (Ultrawide, Telemacro, Dedicated Macro Lens). The final score is the maximum across all three paths, ensuring the best hardware implementation wins regardless of type.
      "4_7_1_ultrawide_path": {
        // SCORING GOAL (4.7.1): Groups the ultrawide lens macro capability via Autofocus (AF) and Minimum Focus Distance. Only evaluated if an ultrawide lens is present (see 4_5_ultrawide_capability.presence).
        "ultrawide_af": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.0
          // SCORING GUIDELINE (4.7.1.1): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. If true: value = true (Autofocus) → subscore = 10.0; value = false (Fixed focus) → subscore = 6.0. If presence = false, this subscore MUST be "N/A" and Score_4.7.1 = 0.0.
        },
        "min_focus_distance_cm": {
          "value": 2.5,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 7.31
          // SCORING GUIDELINE (4.7.1.2): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. Apply the Section 4.7.1.2 logarithmic formula: Score = 10 × (log(Camera_Macro_Dist_cm_Max) − log(distance)) / (log(Camera_Macro_Dist_cm_Max) − log(Camera_Macro_Dist_cm_Min)), clamped 0–10. Lower focus distance = higher score.
        },
        // SCORING GUIDELINE: predicted_score (Score_4.7.1) = (0.4 × ultrawide_af.subscore) + (0.6 × min_focus_distance_cm.subscore) if presence = true; otherwise 0.0. Minimum focus distance is weighted higher (60%) because it directly determines how close the lens can physically get to a subject.
        "predicted_score": 8.39,
        "final_score": {
          "value": 8.39,
          // SCORING GUIDELINE: Intermediate path score feeding into the parent 4_7 final formula. Inherits predicted_score. (No Booster applies at this child level.)
          "method_used": "Predictor",
          // SCORING GUIDELINE: Must be "Predictor" natively.
          "booster": "No",
          // SCORING GUIDELINE: Always "No" at child path level. Boosters are only applied at the parent 4_7 level.
          "confidence": "N/A"
          // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
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
        // SCORING GUIDELINE: predicted_score (Score_4.7.2) = 0.0 if telemacro_presence = false; otherwise derived from the telemacro formula above.
        "predicted_score": 0.00,
        "final_score": {
          "value": 0.00,
          // SCORING GUIDELINE: Intermediate path score. Inherits predicted_score. (No Booster applies at child level.)
          "method_used": "Predictor",
          // SCORING GUIDELINE: Must be "Predictor" natively.
          "booster": "No",
          // SCORING GUIDELINE: Always "No" at child path level.
          "confidence": "N/A"
          // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
        }
      },
      "4_7_3_dedicated_path": {
        // SCORING GOAL (4.7.3): Scores a dedicated macro lens (a small fixed lens separate from the main/ultrawide/tele). Scores are capped at 6.0 to ensure dedicated lenses never outperform a high-quality Autofocus Ultrawide (max 10.0) or Telemacro (max 10.0).
        "dedicated_macro_mp": {
          "value": 0,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.0
          // SCORING GUIDELINE: Apply the Section 4.7.3 linear formula: Score_4.7.3 = clamp(dedicated_macro_mp, 0, 6). The score equals the Megapixel (MP) count, capped at 6.0. A value of 0 MP means no dedicated macro lens is present (score = 0.0). Values above 6 MP all score 6.0 maximum.
        },
        // SCORING GUIDELINE: predicted_score (Score_4.7.3) directly inherits dedicated_macro_mp.subscore.
        "predicted_score": 0.00,
        "final_score": {
          "value": 0.00,
          // SCORING GUIDELINE: Intermediate path score. Inherits predicted_score. (No Booster applies at child level.)
          "method_used": "Predictor",
          // SCORING GUIDELINE: Must be "Predictor" natively.
          "booster": "No",
          // SCORING GUIDELINE: Always "No" at child path level.
          "confidence": "N/A"
          // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
        }
      },
      // SCORING GUIDELINE: predicted_score (MCFP Score) = Max(Score_4.7.1, Score_4.7.2, Score_4.7.3). The system evaluates all three paths independently and awards the score of the best-performing hardware implementation.
      "predicted_score": 8.39,
      "final_score": {
        "value": 8.39,
        // SCORING GUIDELINE: Definitive MCFP score. Inherits predicted_score unless adjusted by a Section 11 expert review Booster. (No Benchmark or Neighbor Interpolation applies here.)
        "method_used": "Predictor",
        // SCORING GUIDELINE: Must be "Predictor" natively.
        "booster": "No",
        // SCORING GUIDELINE: Lists the Section 11 booster rule applied (e.g., "11.1"), or "No" if unadjusted.
        "confidence": "N/A"
        // SCORING GUIDELINE: Must be "N/A" for Predictor methods.
      }
    },
    "4_8_rear_video_resolution": {
      "max_resolution": {
        "value": "8K",
        "source": "TBD",
        "exact_extract": "Proof pending"
        // SCORING GUIDELINE: Look up the max resolution in the Section 4.8 table.
        //   • ≥ 4K Ultra HD (incl. 8K)   → 10.0
        //   • 1440p / QHD (2.5K)         → 8.0
        //   • 1080p Full HD              → 6.0
        //   • 720p HD                    → 3.0
        //   • ≤ 480p                     → 0.0
        //   Note: 8K and 4K both score 10 — see §4.8 for rationale.
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_9_rear_video_fps": {
      "max_fps_1080p_plus": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_10_video_hdr": {
      "capability": {
        "value": "Dolby Vision",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_11_video_encoding": {
      "professional_codec_support": {
        "value": "ProRes 4K60",
        "source": "https://www.tomsguide.com/reviews/iphone-15-pro-max",
        "exact_extract": "export ProRes footage via USB-C at up to 4K and 60 frames per second",
        "subscore": 10.0
      },
      "log_color_profile_support": {
        "value": "Apple Log",
        "source": "https://www.tomsguide.com/reviews/iphone-15-pro-max",
        "exact_extract": "export ProRes footage",
        "subscore": 10.0
      },
      "color_bit_depth": {
        "value": 10,
        "source": "https://www.gsmarena.com/apple_iphone_15_pro-12557.php",
        "exact_extract": "Display [...] 10-bit HDR",
        "subscore": 10.0
      },
      "predicted_score": 10.0,
      "final_score": 10.0
    },
    "4_12_slow_motion": {
      "max_fps": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "resolution_mp": {
        "value": 8.3,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_13_front_camera_resolution": {
      "mp": {
        "value": 12,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_14_front_camera_focus": {
      "type": {
        "value": "Autofocus",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_15_front_camera_video": {
      "max_resolution": {
        "value": "4K",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "max_fps": {
        "value": 60,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "hdr_capability": {
        "value": "SDR",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
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
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster_1": {
          "value": 1.05,
          "booster_title": "11_1_dxomark_24mp_texture_rendering"
        }
      },
      "final_score": 0.0
    },
    "4_17_semantic_ai": {
      "features": {
        "value": [
          "Semantic Segmentation"
        ],
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster_1": {
          "value": 1.05,
          "booster_title": "11_3_dxomark_portrait_skin_tone_rendering"
        }
      },
      "final_score": 0.0
    },
    "4_18_generative_ai_tools": {
      "features": {
        "value": [
          "Magic Eraser"
        ],
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    }
  },
  "5_software_and_longevity": {
    "os_version": {
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
      //   • iOS                                    → 10.0
      //   • Pixel UI / Stock Android               → 9.0
      //   • AOSP / Generic Stock Android           → 9.0
      //   • Fairphone OS                           → 9.0
      //   • Nothing OS                             → 9.0
      //   • Motorola MyUX / Hello UI               → 8.0
      //   • Sony Xperia UI                         → 8.0
      //   • Nokia (Stock Android)                  → 8.0
      //   • Sharp AQUOS UI                         → 8.0
      //   • ASUS ZenUI / ROG UI                    → 7.0
      //   • Samsung One UI                         → 6.0
      //   • OxygenOS (OnePlus)                     → 6.0
      //   • Redmagic OS                            → 6.0
      //   • Honor MagicOS                          → 5.0
      //   • Vivo FunTouch OS / OriginOS            → 5.0
      //   • ColorOS (Oppo)                         → 5.0
      //   • Realme UI                              → 5.0
      //   • LG UX (Legacy)                         → 5.0
      //   • HTC Sense (Legacy)                     → 5.0
      //   • ZTE MiFavor UI / MyOS                  → 4.0
      //   • HyperOS (Xiaomi)                       → 4.0
      //   • Huawei EMUI / HarmonyOS                → 3.0
      //   • MIUI (Legacy Xiaomi)                   → 3.0
      //   • Tecno HiOS / Infinix XOS / Itel OS     → 2.0
      //   If unlisted, score = N/A (update Section 5.2 first).
    },
    "5_1_support_longevity": {
      "years_os": {
        "value": 7,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "years_security": {
        "value": 7,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "5_2_system_cleanliness_control": {
      // SCORING GUIDELINE: platform_score is a direct lookup from the `skin` field above via the Section 5.2 Platform Cleanliness table. Do not derive this value from any formula — just look up the skin string and copy the table score here.
      "platform_score": 6.0,
      "predicted_score": 6.0,
      "final_score": 6.0
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
      "predicted_score": 10.0,
      "final_score": 0.0
    }
  },
  "6_processing_power_and_performance": {
    "soc_name": {
      "value": "Snapdragon 8 Gen 3",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "6_1_0_soc_reference": {
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
            "value": 10.0,
            "description": "Frequency-Adjusted Core Score"
          },
          {
            "name": "Cortex-A720",
            "value": 39.9,
            "description": "Frequency-Adjusted Core Score"
          },
          {
            "name": "Cortex-A520",
            "value": 4.6,
            "description": "Frequency-Adjusted Core Score"
          }
        ]
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "6_2_cpu_architecture_single_core": {
      "geekbench_6_single_score": {
        "value": 2200,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "scoring_components": {
        "core_architecture_score": {
          "value": 10,
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
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "6_3_0_gpu_architecture_reference": {
      "gpu_model": {
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
        "value": 10,
        "description": "Section 6.3.0 Standard Graphics Score"
      },
      "ray_tracing_score": {
        "value": 10,
        "description": "Section 6.3.0 Ray Tracing Score"
      },
      "efficiency_score": {
        "value": 9,
        "description": "Section 6.3.0 Efficiency Score (for battery calculations)"
      }
    },
    "6_3_gpu_performance": {
      "benchmark_steel_nomad_light": {
        "value": 1800,
        "source": "UL Benchmarks Leaderboard",
        "exact_extract": "Proof pending",
        "description": "3DMark Steel Nomad Light Score (Vulkan 1.1 Rasterization)"
      },
      "scoring_components": {
        "graphics_architecture_score": {
          "value": "6_3_0_gpu_architecture_reference.standard_graphics_score",
          "description": "GPU Architecture Score (Standard Graphics) from Section 6.3.0"
        },
        "frequency_scaling_factor": {
          "value": 1.0,
          "description": "Frequency Scaling Factor",
          "actual_frequency_mhz": {
            "value": 903,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "reference_frequency_mhz": {
            "value": "6_3_0_gpu_architecture_reference.reference_frequency_mhz",
            "description": "Reference frequency from Section 6.3.0 for FSF calculation"
          }
        },
        "api_modifier": {
          "value": 1.0,
          "description": "API Efficiency Modifier (0.75-1.0)",
          "formula": "0.75 + (0.25 * API_Score / 10)",
          "components": {
            "vulkan_version": {
              "value": "1.3",
              "source": "TBD",
              "exact_extract": "Proof pending"
            },
            "opengl_es_version": {
              "value": "3.2",
              "source": "TBD",
              "exact_extract": "Proof pending"
            },
            "api_score": {
              "value": 10.0,
              "description": "Highest API score (Vulkan 1.3 = 10.0)"
            }
          }
        },
        "ray_tracing_score": {
          "reference": "6_3_0_gpu_architecture_reference.ray_tracing_score",
          "description": "Ray Tracing Score from Section 6.3.0 (0-10)"
        }
      },
      "standard_graphics_score": {
        "value": 10.0,
        "description": "Standard Graphics Score (from Method A/B/C)",
        "method_used": "A"
      },
      "final_score": {
        "value": 10.0,
        "formula": "(SGS * 0.9) + (RTS * 0.1)",
        "description": "Final GPU Performance Score"
      },
      "confidence": "High"
    },
    "6_4_npu_hardware_performance": {
      "geekbench_ai_score_quantized": {
        "value": 4500,
        "source": "https://browser.geekbench.com/ai-benchmarks",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 9.75,
      "final_score": 9.75,
      // SCORING GUIDELINE: SoC AI scores for Method C (predicted_score) — look up the SoC in the Section 6.4 table.
      //   • Snapdragon 8 Gen 3                    → 10
      //   • Dimensity 9300                        → 10
      //   • Exynos 2400                           → 9
      //   • Apple A18 Pro                         → 9
      //   • Tensor G4                             → 8
      //   • Snapdragon 8 Gen 2                    → 8
      //   • Apple A17 Pro                         → 8
      //   • Apple A16 Bionic                      → 7
      //   • Tensor G3                             → 7
      //   • Dimensity 9200                        → 7
      //   • Apple A15 Bionic                      → 6
      //   • Snapdragon 8 Gen 1                    → 6
      //   • Dimensity 9000                        → 6
      //   • Tensor G2                             → 5
      //   • Apple A14 Bionic                      → 5
      //   • Snapdragon 888                        → 4
      //   • Snapdragon 7 Gen 3                    → 4
      //   • Dimensity 8200                        → 4
      //   • Snapdragon 7 Gen 1 / 7 Gen 2          → 3
      //   • Dimensity 8100                        → 3
      //   • Budget (Helio G / Snapdragon 4xx)     → 1
      //   If the SoC is NOT listed: add it to Section 6.4 first (use its Geekbench AI score
      //   via the Method A formula) — do not guess.
      //   final_score uses Method A (Geekbench AI) if available, else Method B (Neighbor), else Method C (predicted).
    },
    "6_5_ram_technology": {
      "technology": {
        "value": "LPDDR5X",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "6_6_ram_capacity": {
      "max_gb": {
        "value": 12,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "6_7_storage_technology": {
      "technology": {
        "value": "UFS 4.0",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "6_8_storage_capacity": {
      "capacity_gb": {
        "value": 1024,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "6_9_storage_expandability": {
      "slot_type": {
        "value": "No Expansion Slot",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "6_10_thermal_dissipation_stability": {
      "process_nm": {
        "value": 4,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "foundry": {
        "value": "TSMC",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "frame_material": {
        "value": "Titanium Alloy Frame",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "weight_g": {
        "value": 232,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "height_mm": {
        "value": 162.3,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "width_mm": {
        "value": 79.0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "thickness_mm": {
        "value": 8.6,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "cooling_system": {
        "value": "Vapor Chamber (Standard)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 8.16
    }
  },
  "7_connectivity_and_sensors": {
    "7_1_cellular_capabilities": {
      "features": {
        "value": [
          "5G mmWave",
          "5G Sub-6"
        ],
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_2_sim_capabilities": {
      "value": {
        "value": "Dual SIM (Nano + eSIM)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_3_wifi_standard": {
      "value": {
        "value": "Wi-Fi 7",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_4_bluetooth_codecs": {
      "value": {
        "value": "BT 5.3 + LDAC/aptX HD",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_5_biometrics": {
      "value": {
        "value": "Ultrasonic Fingerprint",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_6_sensors": {
      "value": {
        "value": "Full (Gyro, Compass, Baro)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_7_nfc_uwb": {
      "value": {
        "value": "NFC + UWB (Precision)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_8_ecosystem_continuity": {
      "value": {
        "value": [
          "AirDrop",
          "Handoff",
          "Universal Clipboard"
        ],
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_9_usb_port_speed": {
      "version": {
        "value": "USB 3.2 Gen 2 (10Gbps)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "video_out": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    }
  },
  "8_battery_and_charging": {
    "mah": {
      "value": 5000,
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "battery_voltage_v": {
      "value": "Not available",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "battery_cell_configuration": {
      "value": "dual-cell",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "8_1_battery_endurance": {
      "layer_a_energy": {
        "wh": {
          "value": 19.25,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": 6.62
      },
      "layer_b_hardware_efficiency": {
        "b_1_soc_efficiency": {
          "dependencies": [
            "6_processing_power_and_performance.6_9_efficiency_node",
            "6_processing_power_and_performance.6_1_0_soc_reference",
            "6_processing_power_and_performance.6_3_0_gpu_architecture_reference"
          ],
          "breakdown": {
            "process_node_score": 8.64,
            "gpu_efficiency_score": 9,
            "gpu_performance_score": 9,
            "cpu_architecture_score_aes": 7.5
          },
          "score": 8.37
        },
        "b_2_display_efficiency": {
          // NOTE: megapixels_mp, refresh_rate_min_hz and refresh_rate_adaptive are raw input fields stored here because they are only used in this battery sub-formula — they are not scored in any Section 2 subsection.
          "megapixels_mp": {
            // GUIDELINE: Total display pixel count in Megapixels (MP), computed as (resolution_width_px × resolution_height_px) / 1 000 000 and rounded to 1 decimal. Example: 1440 × 3120 → 4.5 MP. Used directly in the B.2.3 Resolution Efficiency formula. Derive from 2_display.2_5_resolution_density.resolution_width_px and resolution_height_px.
            "value": 4.5,
            "source": "derived",
            "exact_extract": "N/A"
          },
          "refresh_rate_min_hz": {
            // GUIDELINE: Minimum refresh rate the display can drop to, in Hertz (Hz). On LTPO (Low Temperature Polycrystalline Oxide) panels this can be as low as 1 Hz. Used in the B.2.2 formula: effective_hz = adaptive ? (min_hz + max_hz) / 2 : max_hz.
            "value": 1,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "refresh_rate_adaptive": {
            // GUIDELINE: Whether the display adjusts its refresh rate dynamically between min_hz and max_hz. true = LTPO/adaptive panel; false = fixed-rate panel (always at max_hz). Controls the B.2.2 formula: effective_hz = adaptive ? (min_hz + max_hz) / 2 : max_hz.
            "value": true,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "dependencies": [
            "2_display.2_1_panel_architecture",
            "2_display.2_6_refresh_rate_max_hz.max_hz"
          ],
          "breakdown": {
            "panel_technology_score": 9,
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
            "cellular_score": 0,
            "wifi_score": 0
          },
          "score": 0.0
        },
        "b_4_thermal_efficiency": {
          "dependencies": [
            "6_processing_power_and_performance.6_10_thermal_dissipation_stability"
          ],
          "score": 8.2
        },
        "total_hei_score": 7.14
      },
      "layer_c_software_optimization": {
        "dependencies": [
          "6_software.os_version",
          "6_software.6_3_system_cleanliness_control"
        ],
        "breakdown": {
          "c_1_os_generation": 10,
          "c_2_bloatware": 6.0
        },
        "total_soi_score": 8.4
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
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "8_3_wireless_charging_speed": {
      "watts": {
        "value": 15,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "8_4_reverse_wired": {
      "watts": {
        "value": 0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "8_5_reverse_wireless": {
      "watts": {
        "value": 4.5,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "8_6_charger_in_box": {
      "included_watts": {
        "value": 0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    }
  },
  "9_financial_and_economic_value": {
    "9_1_price": {
      "usd": {
        "value": 1299,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.8,
      "final_score": 0.8
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
      "predicted_score": 3.0,
      "final_score": 3.0
    },
    "9_3_repairability": {
      "ifixit_score": 8,
      "eu_repairability_index": {
        "value": 4.0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "eu_converted_score": 8.0,
      "predicted_score": 8.0,
      "confidence": {
        "value": "High",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "final_score": 8.0
    }
  },
  "10_miscellaneous": {
    "10_1_stylus_hardware_system_support": {
      "value": "Integrated active stylus + dedicated digitizer + BT features",
      "source": "TBD",
      "exact_extract": "Proof pending",
      "predicted_score": 10.0,
      "final_score": 10.0
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
