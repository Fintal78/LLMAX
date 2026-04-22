# Ultimate Smartphone Data Structure Proposal (v5.1)

This schema is the primary, self-contained "Recipe" for AI-automated classification and scoring. It is strictly aligned with the file `scoring_rules.md`.

> [!IMPORTANT]
> ### 🚨 Handling Missing Data, Unlisted Features & Scoring Blockers
> If a required parameter's value cannot be found after an exhaustive search, OR if a feature is found but is not scorable using the provided options (e.g., a newly released codec not yet listed):
> - **Value Entry**: Set the `value` field strictly to `"Not found"` (if missing data) or the raw unlisted feature name (if unlisted feature). Do NOT use `null`, `0`, or empty strings. For missing data, set `source` and `exact_extract` fields to `"N/A"`.
> - **Scoring Procedure**: If the missing data or unlisted feature blocks the formula and NO fallback or benchmark override is possible:
>     1. Set `subscore`, `scores.predicted`, `scores.final.value`, `scores.final.method_used`, `scores.final.booster`, and `scores.final.confidence` to `"N/A"`.
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
  // This template defines the structure and rules for every final score object (scores.final) in Predictor-only subsections.
  // Each scores.final block that references this template MUST follow it exactly.
  // Do NOT add per-field scoring guidelines inside those blocks.
  //
  //   "final": {
  //     "value": <number>,         → The definitive score for this subsection.
  //                                  Calculation: 
  //                                  If no booster is applied, value = predicted score, i.e. scores.predicted (multiplier is 1.0).
  //                                  If there is one booster:
  //                                  value = scores.predicted * booster_multiplier
  //                                  If there are several boosters:
  //                                  value = scores.predicted * booster_multiplier_1 * booster_multiplier_2 * ... 
  //                                  Each booster multiplier comes from the corresponding Section 11 entry.
  //                                  CLAMPING: The result of this calculation is ALWAYS clamped to [0.00, 10.00].
  //     "method_used": "Predictor" → Always "Predictor" for spec-calculated scores (no Benchmark or Neighbor Interpolation).
  //     "booster": "No"            → Which Section 11 adjustment(s) are applied to the predicted score:
  //                                  • "No"                    = No booster applied (value = scores.predicted).
  //                                  • "Section #"             = Single booster (e.g., "11.1").
  //                                  • "Section # + Section #" = Multiple boosters applied in sequence (e.g., "11.1 + 11.2").
  //     "confidence": "N/A"        → Always "N/A" for Predictor methods.
  //   }
  // ─────────────────────────────────────────────────────────────────────────────
  
  // GUIDELINE (meta): Tracks the state of this document itself. Update both fields every time you modify this file.
  "meta": {
    "schema_version": "5.7",
    // GUIDELINE: Version of the data structure schema. Increment only when a structural change is made (new fields added, renamed, or removed). Use semantic versioning (Major.Minor).
    "last_updated": "2026-04-15"
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
      // SCORING GOAL: Scores the structural frame (chassis) and back panel (cladding) materials using two distinct methodologies. The frame is evaluated via the Structural Merit Index (Yield Strength/Rigidity) to ensure structural integrity, while the back uses the Surface Merit Index (Hardness/Toughness) to evaluate scratch and shatter resistance.
      "frame_material": {
        "value": "Titanium Alloy",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.80
          // SCORING GUIDELINE: Identify the frame material. Use the following exact strings for "value" with related scores as subscore (always apply the highest applicable category):
          //   • "Amorphous Alloy"                      → 10.00 (LiquidMetal, Vitreloy, Vit105; confirmed via BOM)
          //   • "Specialized Ceramic"                  → 9.46  (ZrO2 Zirconia, Sapphire composites)
          //   • "Titanium Alloy"                       → 8.80  (Grade 5 Titanium, Ti-6Al-4V)
          //   • "7000 Series Aluminum"                 → 7.40  (7xxx series alloys, "Armor Aluminum")
          //   • "Stainless Steel"                      → 7.17  (316L, 304, Surgical Grade Steel)
          //   • "6000 Series Aluminum"                 → 6.45  (6xxx series alloys, Verified extrusion)
          //   • "Zinc Alloy (Zamak 3)"                 → 5.80  (High-density cast alloy, rugged side-rails)
          //   • "Die-Cast Aluminum (ADC12)"            → 5.05  (Standard cast "Metal Frame" [Default])
          //   • "Magnesium Alloy"                      → 4.97  (AZ91D, Thixomolded Magnesium)
          //   • "Reinforced Polymer"                   → 3.68  (Glass-Fiber/Carbon-Fiber Polyamide)
          //   • "High-Performance Polymer"             → 1.16  (Branded resins, SORPLAS, Bio-PC, "Glasstic")
          //   • "Standard Polymer"                     → 0.00  (Plastic, Polycarbonate (PC), Thermoplastic Polyurethane (TPU), ABS)
          //   • "Not Disclosed"                        → 0.00  (Defaulted to worst-case structural category)
          //
          // AMBIGUITY RESOLUTION RULES (MANDATORY):
          //   1. METAL DEFAULT: "Metal Frame", "Aluminum", "Aluminum Panel", or any "Metal" with no alloy specified MUST default to "Die-Cast Aluminum (ADC12)".
          //   2. STRENGTH CLAIMS: "High-strength Aluminum" or "Armor Aluminum" defaults to "7000 Series Aluminum".
          //   3. PLASTIC DEFAULT: "Plastic Frame" or generic "Polymer" with no reinforcement or grade mentioned MUST default to "Standard Polymer".
          //   4. MARKETING FINISHES: "Titanium-look", "Metal-like", or "Metallic finish" defaults to "High-Performance Polymer" unless metal core is verified.
          //   5. TEARDOWN OVERRIDE: If a teardown confirms a material different from marketing (e.g. "Titanium" being only a thin coating over Aluminum), the structural core material (Aluminum) MUST be used for scoring.
          //   6. EXOTIC EXCLUSIVITY: "Amorphous Alloy" is strictly for non-crystalline metals. Do NOT use for standard aerospace aluminum or common steel. It must not be used as a catch-all.
      },
      "back_material": {
        "value": "Armor-Class Glass",
        "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
        "exact_extract": "Corning® Gorilla® Armor",
        "subscore": 6.41
          // SCORING GUIDELINE: Identify the back panel material. Use the following exact strings for "value" with related scores as subscore (always apply the highest applicable category): 
          //   • "Specialized Ceramic"                  → 10.00 (Zirconia, Alumina, Glass-Ceramic, Sapphire)
          //   • "7000 Series Aluminum"                 → 8.55  (Full metal back, 7xxx series alloys)
          //   • "6000 Series Aluminum"                 → 8.33  (Full metal back, 6xxx series alloys)
          //   • "Zinc Alloy (Zamak 3)"                 → 8.25  (Precision-cast rugged cladding)
          //   • "Die-Cast Aluminum (ADC12)"            → 8.20  (Standard unbranded metal back/unibody [Default])
          //   • "Armor-Class Glass"                    → 6.41  (Corning Gorilla Glass Armor)
          //   • "Shield-Class Glass"                   → 6.25  (Apple Ceramic Shield [all versions], Corning Gorilla Glass Victus 2, Huawei Kunlun Glass 2, AGC Dragontrail Star 2, Vivo Crystal Armor)
          //   • "Reinforced Glass"                     → 6.00  (Corning Gorilla Glass Victus, Gorilla Glass Victus+, Gorilla Glass 3 to Gorilla Glass 6, Schott Xensation Up/Alpha/3D, AGC Dragontrail Pro/Star 1/Standard, Huawei Kunlun Glass 1, Xiaomi Shield Glass, Meizu Titan Glass)
          //   • "Reinforced Polymer"                   → 5.03  (Carbon/Glass-fiber reinforced technical resins: Carbon/Glass-fiber PA, G-10)
          //   • "Flexible Membrane"                    → 4.02  (Vegan/Genuine Leather, Silicone, Alcantara, Bio-leather)
          //   • "Standard Glass"                       → 3.08  (Generic "Glass", Soda-Lime [Default])
          //   • "Composite Sheet"                      → 2.85  (Thin Multi-layer PC/Acrylic, Carbon/Aramid sheet)
          //   • "High-Performance Polymer"             → 2.74  (Branded technical plastics: SORPLAS, Bio-PC, Glasstic, Glastic)
          //   • "Standard Polymer"                     → 0.00  (Unreinforced Polycarbonate, ABS, TPU, Rubber, standard density plastics)
          //   • "Not Disclosed"                        → 0.00
          //
          // AMBIGUITY RESOLUTION RULES (MANDATORY):
          //   1. LEATHER IDENTIFICATION: Any material marketed as "Leather" (Vegan, Eco, Bio, Faux) MUST be scored as "Flexible Membrane" based on its high-quality surface finish and tactile engineering.
          //   2. MIMETIC RULE: Any material marketed with a specific mimetic branding (e.g., "Glasstic", "Glastic", "Glass-touch", "Ceramic-feel") MUST be categorized as "High-Performance Polymer" to recognize its premium finish.
          //   3. GLASS RESOLUTION (GENERIC): Any material listed simply as "Glass" with no verified generation MUST default to "Standard Glass". This rewards the manufacturer for the specific use of mineral glass over a polymer mimic while maintaining the durability penalty floor.
          //   4. MARKETING FINISHES: Surface treatments like "Frosted", "Satin", or "Titanium-finish" MUST be mapped to the core material class (e.g., Frosted Glass -> mapped to specific Glass generation).
          //   5. PREMIUM POLYMER RESOLUTION (MANDATORY): To qualify for the "High-Performance Polymer" class, the material must meet either of the following:
          //       - Recognized Engineering/Sustainable Brand (e.g., SORPLAS, Bio-PC, Glasstic, Glastic).
          //       - Technical proof of high-density reinforcement or Yield Strength ≥45 MPa.
          //       Failure to meet these thresholds defaults the material to the "Standard Polymer" class.
          //   6. METAL UNIBODY: Marketing terms like "Metal Unibody", "Aluminum Panel", or "Metal Panel" MUST default to "Die-Cast Aluminum (ADC12)" for the back.
      },
      "scores": {
        "predicted": 7.84,
        // SCORING GUIDELINE: scores.predicted = (0.6 * frame_material.subscore) + (0.4 * back_material.subscore).
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.84,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
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
        "value": "Tier 1: Digit 6",
        "value_path": "1_2_durability.ingress_protection_rating.value",
        "subscore": 10.00
          // SCORING GUIDELINE: Identify the first digit of the IP rating via "ingress_protection_rating". Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Digit 6"    → 10.00
          //   • "Tier 2: Digit 5"    → 8.00
          //   • "Tier 3: Digit 4"    → 6.00
          //   • "Tier 4: Digit 3"    → 4.00
          //   • "Tier 5: Digit 2"    → 2.00
          //   • "Tier 6: Digit 0–1"  → 0.00
      },
      "water_protection_digit": {
        "value": "Tier 2: Digit 8",
        "value_path": "1_2_durability.ingress_protection_rating.value",
        "subscore": 9.00
          // SCORING GUIDELINE: Identify the second digit of the IP rating via "ingress_protection_rating". Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Digit 9"    → 10.00
          //   • "Tier 2: Digit 8"    → 9.00
          //   • "Tier 3: Digit 7"    → 8.00
          //   • "Tier 4: Digit 6"    → 6.00
          //   • "Tier 5: Digit 5"    → 4.00
          //   • "Tier 6: Digit 4"    → 2.00
          //   • "Tier 7: Digit 0–3"  → 0.00
      },
      "scores": {
        "predicted": 9.50,
        // SCORING GUIDELINE: scores.predicted = (0.5 * dust_protection_digit.subscore) + (0.5 * water_protection_digit.subscore).
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 9.50,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "1_3_glass_protection": {
      // SCORING GOAL: Scores the protective glass type on the display, known as Display Glass Protection (DGP), based on the manufacturer-declared glass generation's certified drop and scratch resistance class. 
      "glass_generation": {
        "value": "Tier 1: Armor-Class",
        "value_details": {
          "Tier 1: Armor-Class": [
            { "name": "Gorilla Glass Armor", "source": "TBD", "exact_extract": "Proof pending" }
          ],
          "Tier 2: Shield-Class": [],
          "Tier 3: Ultra-Reinforced": [],
          "Tier 4: Premium Reinforced": [],
          "Tier 5: Standard Reinforced": [],
          "Tier 6: Entry-Level Reinforced": [],
          "Tier 7: Tempered Glass": [],
          "Tier 8: Glass (Unspecified)": [],
          "Tier 9: Plastic or No Glass": []
        },
        "subscore": 10.00
        // SCORING GUIDELINE: Identify the highest glass tier based on manufacturer drop/scratch claims. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
        //   • "Tier 1: Armor-Class"            → 10.00
        //     Definition: Anti-reflective (AR) coating + ≥2.0m rough-surface drop certification (e.g., Gorilla Glass Armor).
        //   • "Tier 2: Shield-Class"           → 9.50
        //     Definition: Ceramic-infused matrix + ≥2.0m drop certification (e.g., Ceramic Shield, Kunlun Glass).
        //   • "Tier 3: Ultra-Reinforced"       → 9.00
        //     Definition: Advanced alumina-silicate glass optimized for rough-surface drops (≥2.0m class) (e.g., Gorilla Glass Victus 2).
        //   • "Tier 4: Premium Reinforced"     → 8.00
        //     Definition: High-end chemical tempering with ≥2.0m standard drop certification (e.g., Victus, Victus+, Star 2).
        //   • "Tier 5: Standard Reinforced"    → 7.00
        //     Definition: Regular flagship-grade chemical tempering with ≥1.6m drop certification (e.g., Gorilla Glass 5/6, Dragontrail Pro / Star).
        //   • "Tier 6: Entry-Level Reinforced" → 5.00
        //     Definition: Basic chemical tempering with ~1.2m drop certification (e.g., Gorilla Glass 3, Panda Glass, Dragontrail).
        //   • "Tier 7: Tempered Glass"         → 3.00
        //     Definition: Basic chemically strengthened glass with no certified drop class.
        //   • "Tier 8: Glass (Unspecified)"    → 2.00
        //   • "Tier 9: Plastic or No Glass"    → 0.00
        // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are **arrays of objects**. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
      },
      "scores": {
        "predicted": 10.00,
        // SCORING GUIDELINE: scores.predicted directly inherits glass_generation.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "1_4_thickness": {
      // SCORING GOAL: Scores device thickness (excluding camera bump) as a measure of pocketability and hand comfort. Thinner is always better.
      "thickness_mm": {
        "value": 8.6,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 4.36
        // SCORING GUIDELINE: Apply the Section 1.4 linear formula: Score = 10 − 10 * ((thickness_mm − Thickness_mm_Min) / (Thickness_mm_Max − Thickness_mm_Min)), clamped 0–10.
      },
      "scores": {
        "predicted": 4.36,
        // SCORING GUIDELINE: scores.predicted directly inherits thickness_mm.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 4.36,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "1_5_weight": {
      // SCORING GOAL: Scores total device weight as a measure of long-term holding comfort. Lighter phones cause less wrist and arm fatigue during extended use.
      "weight_g": {
        "value": 232,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 2.33
        // SCORING GUIDELINE: Apply the Section 1.5 linear formula: Score = 10 − 10 * ((weight_g − Weight_g_Min) / (Weight_g_Max − Weight_g_Min)), clamped 0–10.
      },
      "scores": {
        "predicted": 2.33,
        // SCORING GUIDELINE: scores.predicted directly inherits weight_g.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 2.33,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "1_6_ergonomics": {
      // SCORING GOAL: Scores device width as a measure of one-handed ergonomics. Beyond a critical threshold, phones become difficult to grip and operate single-handedly. Note: the positive benefit of a wider screen is already captured in Sections 2.8 (Screen-to-Body Ratio) and 2.9 (Screen Size).
      "width_mm": {
        "value": 79.0,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.00
        // SCORING GUIDELINE: Apply the Section 1.6 quadratic formula: Score = 10 * (1 − ((width_mm − Width_mm_Min) / (Width_mm_Max − Width_mm_Min))²), clamped 0–10.
      },
      "scores": {
        "predicted": 0.00,
        // SCORING GUIDELINE: scores.predicted directly inherits width_mm.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 0.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
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
      "panel_type": {
        "value": "Tier 2: LTPO OLED",
        "value_details": {
          "Tier 1: Tandem OLED": [],
          "Tier 2: LTPO OLED": [
            { "name": "Dynamic AMOLED 2X", "source": "TBD", "exact_extract": "Proof pending" }
          ],
          "Tier 3: Standard OLED/AMOLED (LTPS)": [],
          "Tier 4: IPS LCD": [],
          "Tier 5: TFT or PLS LCD": [],
          "Tier 6: TN LCD or Legacy": []
        },
        "subscore": 9.00
        // SCORING GUIDELINE: Identify the panel type. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
        //   • "Tier 1: Tandem OLED"                   → 10.00
        //     Definition: Dual-stack Organic Light-Emitting Diode (OLED) with two vertical light-emitting layers.
        //   • "Tier 2: LTPO OLED"                     → 9.00
        //     Definition: Organic Light-Emitting Diode (OLED) with Low-Temperature Polycrystalline Oxide (LTPO) backplane. Supports variable refresh rate down to 1 Hz.
        //   • "Tier 3: Standard OLED/AMOLED (LTPS)"   → 8.00
        //     Definition: Organic Light-Emitting Diode (OLED) with Low-Temperature Polycrystalline Silicon (LTPS) backplane. Self-emissive pixels; lacks variable refresh rate down to 1 Hz.
        //   • "Tier 4: IPS LCD"                       → 6.00
        //     Definition: In-Plane Switching Liquid-Crystal Display (IPS LCD). Utilizes a backlight with in-plane liquid crystal alignment.
        //   • "Tier 5: TFT or PLS LCD"                → 2.00
        //     Definition: Standard active-matrix Liquid-Crystal Display (LCD) including Plane-to-Line Switching (PLS) and non-IPS Thin-Film Transistor (TFT) variants. 
        //   • "Tier 6: TN LCD or Legacy"              → 0.00
        //     Definition: Twisted Nematic Liquid-Crystal Display (TN LCD) or legacy technologies. Liquid crystals twist to control light; characterized by color inversion or contrast shift at off-axis viewing angles.
        // AMBIGUITY RULE: Plain "OLED" or "AMOLED" with NO "LTPO" qualifier must default to "Tier 3: Standard OLED/AMOLED (LTPS)" (8.00).
        // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are **arrays of objects**. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
      },
      "scores": {
        "predicted": 9.00,
        // SCORING GUIDELINE: scores.predicted directly inherits panel_type.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 9.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_2_brightness": {
      // SCORING GOAL: Scores peak and High Brightness Mode (HBM) brightness together, as HBM governs outdoor readability while peak brightness governs High Dynamic Range (HDR) media quality.
      "peak_nits": {
        "value": 2600,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.73
        // SCORING GUIDELINE: Apply the Section 2.2 logarithmic formula: Peak_Score = 10 * (log(peak_nits) − log(Display_Brightness_Nits_Min)) / (log(Display_Brightness_Nits_Max) − log(Display_Brightness_Nits_Min)), clamped 0–10.
      },
      "hbm_nits": {
        "value": 1500,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.21
        // SCORING GUIDELINE: Apply the Section 2.2 logarithmic formula: HBM_Score = 10 * (log(hbm_nits) − log(Display_HBM_Nits_Min)) / (log(Display_HBM_Nits_Max) − log(Display_HBM_Nits_Min)), clamped 0–10. Fallback: if hbm_nits is unavailable, then set "value" to "Not found" and use the formula with the fallback value hbm_nits = peak_nits / 1.5.
      },
      "scores": {
        "predicted": 7.37,
        // SCORING GUIDELINE: scores.predicted = (0.7 * hbm_nits.subscore) + (0.3 * peak_nits.subscore)
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.37,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_3_color_gamut_coverage": {
      // SCORING GOAL: Scores how much of the Digital Cinema Initiatives (DCI-P3) professional color space the display can reproduce. A wider gamut means richer, more saturated colors in photos, videos, and High Dynamic Range (HDR) content.
      "dci_p3_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 10.00
        // SCORING GUIDELINE: Apply the Section 2.3 linear formula: Score = 10 * (dci_p3_percent − Display_P3_Coverage_Percent_Min) / (Display_P3_Coverage_Percent_Max − Display_P3_Coverage_Percent_Min), clamped 0–10. If dci_p3_percent is not available from any source then set "value" to "Not found" and subscore to "N/A". Then use the "srgb_percent" block below as fallback scoring. 
      },
      "srgb_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": "N/A"
        // SCORING GUIDELINE: sRGB coverage is a fallback data source only. ONLY when dci_p3_percent is not available from any source use the formula above with DCI-P3_estimate = min(srgb_percent * 0.75, 100) to calculate the subscore of this block. When dci_p3_percent is available and the subscore was calculated in the previous block then set the subscore of this block to "N/A".
      },
      "scores": {
        "predicted": 10.00,
        // SCORING GUIDELINE: scores.predicted directly inherits dci_p3_percent.subscore or srgb_percent.subscore, whichever is not "N/A".
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_4_hdr_format_support": {
      // SCORING GOAL: Scores which High Dynamic Range (HDR) video formats the display officially supports. Dynamic HDR formats optimize brightness and colour frame-by-frame, unlocking the full quality of premium streaming content.
      "supported_formats": {
        "value": [
          "HDR10+",
          "HDR10"
        ],
        "value_details": {
          "Dolby Vision": [],
          "HDR10+": [
            { "name": "HDR10+", "source": "TBD", "exact_extract": "Proof pending" }
          ],
          "HDR10": [
            { "name": "HDR10", "source": "TBD", "exact_extract": "Proof pending" }
          ],
          "HLG": []
        },
        "subscore": 7.00,
        // SCORING GUIDELINE: Identify the presence of officially supported HDR formats. Be exhaustive and add all that apply. For each supported format, use the exact term below for the "value" array:
        //   • "Dolby Vision"             → adds +3.00 to the subscore
        //   • "HDR10+"                   → adds +2.00 to the subscore
        //   • "HDR10" or "HLG"           → adds +5.00 to the subscore (Base HDR tier, points do not stack)
        // The subscore is the sum of these points (Clamped 0–10). Example: ["HDR10+", "HDR10"] = 5.00 + 2.00 = 7.00.
        // If the device does not list support for any HDR formats (or explicitly only supports Standard Dynamic Range / SDR), leave the array empty [] and set subscore to 0.00.
        // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are arrays of objects. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
      },
      "scores": {
        "predicted": 7.00,
        // SCORING GUIDELINE: scores.predicted directly inherits supported_formats.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
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
        // SCORING GUIDELINE: Apply the Section 2.5 logarithmic formula: Score = 10 * (log(pixels_per_inch) − log(Display_PPI_Min)) / (log(Display_PPI_Max) − log(Display_PPI_Min)), clamped 0–10. Use directly pixels_per_inch.value if available from any source. 
        // ONLY if pixels_per_inch is NOT available derive PPI: pixels_per_inch = √(resolution_width_px² + resolution_height_px²) / diagonal_inches 
        // with diagonal_inches = 2_9_screen_size.diagonal_inches.value and in that case set "source" to "Derived from resolution_width_px, resolution_height_px, and diagonal_inches" and set "exact_extract" to "N/A".
      },
      "scores": {
        "predicted": 8.43,
        // SCORING GUIDELINE: scores.predicted directly inherits pixels_per_inch.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.43,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_6_motion_smoothness": {
      // SCORING GOAL: Scores Motion Smoothness via maximum refresh rate. Higher Hertz (Hz) means scrolling and animations look smoother. 120 Hz and above are perceptibly superior to standard 60 Hz.
      "maximum_refresh_rate_hz": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.55
        // SCORING GUIDELINE: Apply the Section 2.6 logarithmic formula: Score = 10 * (log(maximum_refresh_rate_hz) − log(Display_Refresh_Rate_Hz_Min)) / (log(Display_Refresh_Rate_Hz_Max) − log(Display_Refresh_Rate_Hz_Min)), clamped 0–10.
      },
      "scores": {
        "predicted": 7.55,
        // SCORING GUIDELINE: scores.predicted directly inherits maximum_refresh_rate_hz.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 7.55,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_7_touch_responsiveness": {
      // SCORING GOAL: Scores touch sampling rate as a measure of how instantly the screen responds to finger input. Higher rates produce a "glued to your finger" feel, critical for gaming and User Interface (UI) fluidity.
      "touch_sampling_rate_hz": {
        "value": 240,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 5.00,
        // SCORING GUIDELINE: Apply the Section 2.7 logarithmic formula: Score = 10 * (log(touch_sampling_rate_hz) − log(Display_Touch_Sampling_Hz_Min)) / (log(Display_Touch_Sampling_Hz_Max) − log(Display_Touch_Sampling_Hz_Min)), clamped 0–10.
      },
      "scores": {
        "predicted": 5.00,
        // SCORING GUIDELINE: scores.predicted directly inherits touch_sampling_rate_hz.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 5.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_8_screen_to_body_ratio": {
      // SCORING GOAL: Scores the Screen-to-Body Ratio (SBR) — how much of the front face is active display versus border (bezel). Higher percentage means a more immersive, modern design.
      "screen_to_body_ratio_percent": {
        "value": 88.5,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.64
        // SCORING GUIDELINE: Apply the Section 2.8 linear formula: Score = 10 * ((screen_to_body_ratio_percent − Display_SBR_Percent_Min) / (Display_SBR_Percent_Max − Display_SBR_Percent_Min)), clamped 0–10.
        // FALLBACK: If "screen_to_body_ratio_percent" is NOT available from primary sources, derive it using: (Active Display Area / Total Frontal Area) * 100. That should be well documented and justified via "source" and "exact_extract", if needed by providing multiple sources and extracts (stored in "source" and "exact_extract" and separated via commas). 
      },
      "scores": {
        "predicted": 8.64,
        // SCORING GUIDELINE: scores.predicted directly inherits screen_to_body_ratio_percent.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.64,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_9_screen_size": {
      // SCORING GOAL: Scores the physical display diagonal as a measure of immersion and media consumption experience. Larger screens offer more real estate for video, gaming, and productivity.
      "diagonal_inches": {
        "value": 6.8,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.93
        // SCORING GUIDELINE: Apply the Section 2.9 quadratic formula: Score = 10 * ((diagonal_inches² − Display_Size_Inch_Min²) / (Display_Size_Inch_Max² − Display_Size_Inch_Min²)), clamped 0–10.
      },
      "scores": {
        "predicted": 6.93,
        // SCORING GUIDELINE: scores.predicted directly inherits diagonal_inches.subscore.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 6.93,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
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
        // SCORING GUIDELINE: Only evaluated if flicker_presence.value = "Yes". Apply the Section 2.10.2 logarithmic formula: Score = 10 * (log(pulse_width_modulation_dimming_hertz) − log(Display_PWM_Hz_Min)) / (log(Display_PWM_Hz_Max) − log(Display_PWM_Hz_Min)), clamped 0–10. If flicker_presence.value = "No", all fields MUST be "N/A".
      },
      "scores": {
        "predicted": 4.07,
        // SCORING GUIDELINE: scores.predicted directly inherits whichever subscore is NOT "N/A" between flicker_presence and pulse_width_modulation_dimming_hertz.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 4.07,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "2_11_display_benchmark_final_scoring": {
      // SCORING GOAL: Produces the overall Display Final Score using a three-method hierarchy (A→B→C). Method A uses the DXOMARK Display benchmark when available. Method B uses Nearest Neighbor Interpolation when only similar devices have benchmarks. Method C (Predictor) is the fallback weighted sum of sub-section predicted scores.

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD A — Direct Benchmark (Primary)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_a_benchmark_Display": {
        "value": 150,
        "source": "https://www.dxomark.com/smartphones/#display", // if the score is available for the device you MUST put the exact url here
        "exact_extract": "Proof pending",
        "subscore": 9.34
        //     - WHERE TO FIND IT: Search for "[Device Name] DXOMARK display score" on dxomark.com.
        //     - EXTRACTION RULE: Use the "Overall Display Score". Ensure category is "Display" (not Camera/Selfie/Audio).
        // SCORING GUIDELINE: Score = 10 * (log(method_a_benchmark_Display.value) − log(Display_DXO_Score_Min)) / (log(Display_DXO_Score_Max) − log(Display_DXO_Score_Min)), clamped 0–10. If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD C — Weighted Prediction Model (Tertiary / baseline for Method B)
      // ═══════════════════════════════════════════════════════════════════════════
      
      "method_c_prediction_model_Display": {
        // SCORING GUIDELINE: these are the 8 perceptual sub-section predicted scores and their weights:
        "subscore_2_1":  { "subscore_path": "2_1_panel_architecture.scores.predicted",   "weight_2_1": 0.15 },
        "subscore_2_2":  { "subscore_path": "2_2_brightness.scores.predicted",            "weight_2_2": 0.20 },
        "subscore_2_3":  { "subscore_path": "2_3_color_gamut_coverage.scores.predicted",  "weight_2_3": 0.10 },
        "subscore_2_4":  { "subscore_path": "2_4_hdr_format_support.scores.predicted",    "weight_2_4": 0.10 },
        "subscore_2_5":  { "subscore_path": "2_5_resolution_density.scores.predicted",    "weight_2_5": 0.10 },
        "subscore_2_6":  { "subscore_path": "2_6_motion_smoothness.scores.predicted",     "weight_2_6": 0.15 },
        "subscore_2_7":  { "subscore_path": "2_7_touch_responsiveness.scores.predicted",  "weight_2_7": 0.10 },
        "subscore_2_10": { "subscore_path": "2_10_eye_comfort.scores.predicted",          "weight_2_10": 0.10 },

        // These inputs are used to calculate the overall predicted_score (Method C):
        "predicted_score": 7.51,
        // SCORING GUIDELINE: predicted_score = Sum(subscore_X * weight_X) for all 8 entries above. This is the score used for Method B neighbors. 

        // Sections 2.8 (Screen-to-Body Ratio) and 2.9 (Screen Size) are excluded because DXOMARK does not evaluate physical dimensions.
        // IMPORTANT: Always use Predicted Scores (before any Boosters), not Final Scores, to ensure hardware-only comparison.
      },
    
      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD B — Nearest Neighbor Interpolation (Secondary)
      // ═══════════════════════════════════════════════════════════════════════════
      
      "method_b_neighbor_interpolation_Display": {
        // SCORING GUIDELINE: Method B is populated for ALL phones (even if Method A is available) to evaluate the precision of the interpolation model. The interpolation MUST be performed using exactly 3 distinct neighbor devices, explicitly excluding the target device itself.
        // Step 1: Find the 3 distinct devices with the smallest weighted Euclidean distance using the method_c_prediction_model_Display weights and sub-section predicted scores, excluding the target device itself.
        //         Distance = √( Sum( weight_i * (SubScore_Target_i − SubScore_Neighbor_i)² ) )
        //         Where 'i' iterates over each of the 8 method_c_prediction_model_Display entries (subscore_2_1 through subscore_2_10, except subscore_2_8 and subscore_2_9), weight_i is the entry's weight, SubScore_Target_i is this device's sub-section_i predicted score, and SubScore_Neighbor_i is the candidate neighbor's sub-section_i predicted score.
        //         Search space: all phones that have a known DXOMARK Display score (Method A), excluding the target device itself.
        // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
        "neighbors": [
          {
            // Neighbor1
            "device_id_1": "google_pixel_9_pro",
            // GUIDELINE: The identity.id of the neighbor device (e.g., "google_pixel_9_pro").
            "euclidean_distance_1": 0.0500,
            // GUIDELINE: Weighted Euclidean distance from Step 1.
            "predicted_score_1": 7.50,
            // GUIDELINE: The neighbor's own Method C predicted score.
            "benchmark_score_1": 9.30
            // GUIDELINE: The neighbor's Method A subscore.
          },
          {
            // Neighbor2
            "device_id_2": "samsung_galaxy_s23_ultra",
            "euclidean_distance_2": 0.0800,
            "predicted_score_2": 7.45,
            "benchmark_score_2": 9.20
          },
          {
            // Neighbor3
            "device_id_3": "apple_iphone_15_pro_max",
            "euclidean_distance_3": 0.1200,
            "predicted_score_3": 7.60,
            "benchmark_score_3": 9.40
          }
        ],
        "avg_predicted_neighbors": 7.5167,
        // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
        "avg_benchmark_neighbors": 9.3000,
        // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
        "correction_ratio": 0.9991,
        // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_Display.predicted_score / avg_predicted_neighbors.
        "interpolated_score": 9.29
        // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
      },

      "scores": {
        "predicted": 7.51,
        // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_Display.predicted_score.
        "final": {
          "value": 9.34,
          // SCORING GUIDELINE: Use Method A if method_a_benchmark_Display is available (method_a_benchmark_Display.subscore becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_Display.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_Display.predicted_score). 
          "method_used": "Benchmark (DXOMARK)",
          // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
          //   • Benchmark (DXOMARK)    → Method A (documented DXOMARK score)
          //   • Neighbor Interpolation → Method B (similar device benchmarks)
          //   • Predictor              → Method C (weighted spec calculation)
          "booster": "No",
          // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
          "confidence": "N/A"
          // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
        }
      }
    },
    "3_audio": {
      "3_1_speaker_system_capability": {
        // SCORING GOAL: Scores the physical speaker hardware configuration (Speaker System Capability, SSC) for audio output without headphones. Evaluates speaker count, placement, and channel symmetry.
        "speaker_configuration": {
          "value": "Tier 2: Standard Hybrid Stereo",
          "value_details": {
            "Tier 1: Balanced / Symmetrical Stereo": [],
            "Tier 2: Standard Hybrid Stereo": [
              { "name": "Stereo Speakers", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: Mono Speaker": [],
            "Tier 4: No Usable Speaker": []
          },
          "subscore": 7.00
          // SCORING GUIDELINE: Identify the physical speaker setup. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Balanced / Symmetrical Stereo" → 10.00
          //     Definition: Two identical or near-identical dedicated speaker units (top/bottom or left/right) offering matched frequency response and volume. Must explicitly state "Symmetrical speakers" or "Balanced stereo".
          //   • "Tier 2: Standard Hybrid Stereo"        → 7.00
          //     Definition: Typically uses the earpiece as a second channel, lacking the bass response and volume of the primary speaker. Typically listed as 'Stereo Speakers' without symmetry claims.
          //   • "Tier 3: Mono Speaker"                  → 3.00
          //     Definition: Single active loudspeaker for media playback.
          //   • "Tier 4: No Usable Speaker"             → 0.00
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are **arrays of objects**. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 7.00,
          // SCORING GUIDELINE: scores.predicted directly inherits speaker_configuration.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 7.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "3_2_playback_audio_processing_immersion": {
        // SCORING GOAL: Scores Playback Audio Processing & Immersion (PAPI) as a composite of two sub-criteria: audio format decoding capability (3.2.1, weight 50%) and spatial audio rendering capability (3.2.2, weight 50%).
        "audio_format_decode": {
          "value": [
            "Dolby Atmos",
            "Dolby Digital / Dolby Audio"
          ],
          "value_details": {
            "Dolby Atmos": [
              { "name": "Dolby Atmos", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "DTS:X": [],
            "Dolby Digital / Dolby Audio": [
              { "name": "Dolby Digital", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "DTS / DTS-HD": []
          },
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the presence of officially supported audio formats. For each supported format, use the exact term below for the "value" array:
          //   • "Dolby Atmos"                 → adds +5.00 to the subscore
          //   • "DTS:X"                       → adds +1.00 to the subscore
          //   • "Dolby Digital / Dolby Audio" → adds +3.00 to the subscore
          //   • "DTS / DTS-HD"                → adds +1.00 to the subscore
          // The subscore is the sum of these points (Clamped 0–10). Example: ["Dolby Atmos", "Dolby Digital / Dolby Audio"] = 5.00 + 3.00 = 8.00.
          // If the device does not list support for any multichannel/object formats (or explicitly only supports stereo), leave the array empty [] and set subscore to 0.00.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported audio formats/codecs found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply.
        },
        "spatial_audio_rendering": {
          "value": "Tier 2: Static spatial audio (no head tracking)",
          "value_details": {
            "Tier 1: Spatial audio with Dynamic Head Tracking": [],
            "Tier 2: Static spatial audio (no head tracking)": [
              { "name": "360 Audio", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: No spatial rendering": []
          },
          "subscore": 7.00
          // SCORING GUIDELINE: Identify the highest-tier spatial capability. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Spatial audio with Dynamic Head Tracking"      → 10.00
          //   • "Tier 2: Static spatial audio (no head tracking)"       → 7.00
          //   • "Tier 3: No spatial rendering"                          → 0.00
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported spatial rendering technologies found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 7.50,
          // SCORING GUIDELINE: scores.predicted = (0.5 * audio_format_decode.subscore) + (0.5 * spatial_audio_rendering.subscore).
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 7.50,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "3_3_wired_audio_capability": {
        // SCORING GOAL: Scores native wired audio output capability. Evaluates the best natively supported wired audio tier without requiring powered external accessories. Per the hierarchical category rule, only the highest supported tier is stored.
        "wired_audio_tier": {
          "value": "Tier 3: USB-C digital audio only (dongle required)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 3.00
          // SCORING GUIDELINE: Identify the highest supported wired audio tier. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: 3.5mm headphone jack (native analog output)"  → 10.00
          //   • "Tier 2: USB-C with documented analog audio output"    → 6.00
          //   • "Tier 3: USB-C digital audio only (dongle required)"   → 3.00
          //   • "Tier 4: No wired audio support"                       → 0.00
        },
        "scores": {
          "predicted": 3.00,
          // SCORING GUIDELINE: scores.predicted directly inherits wired_audio_tier.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 3.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "3_4_microphone_audio_recording": {
        // SCORING GOAL: Scores Microphone & Audio Recording (MAR) as a composite of hardware count (3.4.1, 30%), recording channels (3.4.2, 30%), and advanced capture features (3.4.3, 40%).
        "microphone_hardware_count": {
          "value": "Tier 2: 3",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Record the physical microphone count. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: ≥4 microphones" → 10.00
          //   • "Tier 2: 3"              → 8.00
          //   • "Tier 3: 2"              → 5.00
          //   • "Tier 4: 1"              → 2.00
          //   • "Tier 5: None"           → 0.00
        },
        "recording_channels_modes": {
          "value": "Tier 2: Stereo",
          "value_details": {
            "Tier 1: Multi-channel / spatial audio": [],
            "Tier 2: Stereo": [
              { "name": "Stereo recording", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: Mono": [],
            "Tier 4: Voice-only / unclear": []
          },
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the highest-tier recording capability. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Multi-channel / spatial audio" → 10.00
          //     Definition: Captures audio with directional data (e.g., 5.1, 7.1, or OZO Audio).
          //   • "Tier 2: Stereo"                        → 8.00
          //     Definition: Standard two-channel (Left/Right) audio recording.
          //   • "Tier 3: Mono"                          → 5.00
          //     Definition: Single-channel audio recording.
          //   • "Tier 4: Voice-only / unclear"          → 0.00
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific recording technologies found in specs (e.g., OZO Audio, Audio Zoom). To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "advanced_capture_features": {
          "value": [
            "Directional / Audio Zoom",
            "Wind Noise Reduction"
          ],
          "value_details": {
            "Directional / Audio Zoom": [
              { "name": "Audio Zoom", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Wind Noise Reduction": [
              { "name": "Wind Noise Reduction", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Voice Focus / Isolation": [],
            "Pro Mic Support": []
          },
          "subscore": 5.00
          // SCORING GUIDELINE: Identify the presence of documented features from the list below. For each detected feature, use the exact term before the ": " symbol (e.g., "Directional / Audio Zoom" or "Wind Noise Reduction") for the "value" array. Each feature adds +2.50 points to the subscore (Clamped 0–10). Example: 2 features * 2.50 = 5.00.
          //   • Directional / Audio Zoom: Focuses audio on the zoomed subject (e.g., "Audio Zoom", "Zoom-in Mic")
          //   • Wind Noise Reduction: Dedicated toggle or feature to filter wind rumble
          //   • Voice Focus / Isolation: Feature to enhance speech over background noise (e.g., "Speech Enhancement", "Audio Eraser")
          //   • Pro Mic Support: Accepts an external mic for video recording — wired (USB-C or 3.5mm) or wireless (Bluetooth). Verify via spec sheet listing for example "external mic input", a documented gain/level control in the camera app, or reviewer confirmation of external mic recording
          // Always populate the full list of detected features in "value". Do not selectively omit.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported features found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply.
        },
        "scores": {
          "predicted": 6.80,
          // SCORING GUIDELINE: scores.predicted = (0.30 * microphone_hardware_count.subscore) + (0.30 * recording_channels_modes.subscore) + (0.40 * advanced_capture_features.subscore). Weights from the MAR formula in Section 3.4.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 6.80,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
          // SCORING GUIDELINE: Apply the Section 4.1 logarithmic formula: Score = 10 * (log(4_1_main_sensor_size.optical_format.value) − log(Camera_Main_Sensor_Inch_Min)) / (log(Camera_Main_Sensor_Inch_Max) − log(Camera_Main_Sensor_Inch_Min)), clamped 0–10. Convert the optical format string to a decimal (e.g., "1/1.3 inches" → 0.7692).
        },
        "scores": {
          "predicted": 8.11,
          // SCORING GUIDELINE: scores.predicted directly inherits optical_format.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.11,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_2_main_camera_aperture": {
        // SCORING GOAL: Scores the main camera lens aperture (f-number).
        "aperture_f_stop": {
          "value": "f/1.7",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 6.40
          // SCORING GUIDELINE: Apply the Section 4.2 inverted logarithmic formula: Score = 10 * (log(Camera_Main_Aperture_f_Max) − log(aperture_f_stop)) / (log(Camera_Main_Aperture_f_Max) − log(Camera_Main_Aperture_f_Min)), clamped 0–10. Parse the f-stop string to a decimal (e.g., "f/1.7" → 1.7). The formula is inverted because lower f-numbers are better.
        },
        "scores": {
          "predicted": 6.40,
          // SCORING GUIDELINE: scores.predicted directly inherits aperture_f_stop.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 6.40,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_3_main_camera_resolution": {
        // SCORING GOAL: Scores the main sensor's maximum pixel count in Megapixels (MP).
        "megapixels": {
          "value": 200,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 4.3 logarithmic formula: Score = 10 * (log(megapixels) − log(Camera_Main_Resolution_MP_Min)) / (log(Camera_Main_Resolution_MP_Max) − log(Camera_Main_Resolution_MP_Min)), clamped 0–10.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits megapixels.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_4_image_stabilization": {
        // SCORING GOAL: Scores the image stabilization mechanism used to compensate for hand shake during photo and video capture.
        "stabilization_type": {
          "value": "Tier 3: Lens-Based Optical Image Stabilization",
          "value_details": {
            "Tier 1: Multi-Axis Mechanical Stabilization (Gimbal)": [],
            "Tier 2: Sensor-Shift Optical Image Stabilization": [],
            "Tier 3: Lens-Based Optical Image Stabilization": [
              { "name": "OIS", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 4: Software-Only Stabilization (Electronic, no hardware)": [],
            "Tier 5: None": []
          },
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the stabilization mechanism. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Multi-Axis Mechanical Stabilization (Gimbal)"          → 10.00
          //     Definition: The entire camera module floats on a multi-axis mechanical suspension or gimbal (e.g., vivo, ASUS ROG/Zenfone).
          //   • "Tier 2: Sensor-Shift Optical Image Stabilization"              → 9.00
          //     Definition: The image sensor itself physically moves (IBIS) instead of the lens (primarily found on Apple iPhones 12 Pro Max and newer).
          //   • "Tier 3: Lens-Based Optical Image Stabilization"                → 8.00
          //     Definition: Individual optical lens elements move to counteract shake. This is the default tier for generic "OIS" listings.
          //   • "Tier 4: Software-Only Stabilization (Electronic, no hardware)" → 5.00
          //     Definition: Purely algorithmic stabilization (EIS/AIS) via digital cropping; requires no moving physical parts.
          //   • "Tier 5: None"                                                  → 0.00
          //     Definition: No hardware or software stabilization is detected or documented.
          // AMBIGUITY RULE: If the spec sheet lists only "Optical Image Stabilization (OIS)" without further qualification (no mention of "sensor-shift" or "gimbal"), default to "Tier 3: Lens-Based Optical Image Stabilization" (8.00).
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are **arrays of objects**. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 8.00,
          // SCORING GUIDELINE: scores.predicted directly inherits stabilization_type.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
          // SCORING GUIDELINE: Apply the Section 4.5.2 linear formula: Score = 10 * (field_of_view_degrees − Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max) / (Camera_Ultrawide_FOV_Deg_Max − Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max), clamped 0–10. Only evaluated if presence = true. If presence = false, then all fields of this block must be "N/A".
        },
        "ultrawide_sensor_size": {
          "value": "1/2.0",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Apply the Section 4.5.3 logarithmic formula: Score = 10 * (log(ultrawide_sensor_size) − log(Camera_Ultrawide_Sensor_Inch_Min)) / (log(Camera_Ultrawide_Sensor_Inch_Max) − log(Camera_Ultrawide_Sensor_Inch_Min)), clamped 0–10. Convert format string to decimal for the scoring formula (e.g., "1/2.0" → 0.5). Only evaluated if presence = true. If presence = false, then all fields of this block must be "N/A".
        },
        "scores": {
          "predicted": 8.67,
          // SCORING GUIDELINE: scores.predicted = (0.60 * field_of_view_degrees.subscore) + (0.40 * ultrawide_sensor_size.subscore) if presence = true; otherwise scores.predicted = 0.00.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.67,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_6_zoom_capability": {
        // SCORING GOAL: Scores optical zoom power. Only true optical magnification is counted; digital/crop zoom is excluded.
        "optical_zoom_x": {
          "value": 5,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 6.99
          // SCORING GUIDELINE: Apply the Section 4.6 logarithmic formula: Score = 10 * (log(optical_zoom_x) − log(Camera_Zoom_Optical_x_Min)) / (log(Camera_Zoom_Optical_x_Max) − log(Camera_Zoom_Optical_x_Min)), clamped 0–10.
        },
        "scores": {
          "predicted": 6.99,
          // SCORING GUIDELINE: scores.predicted directly inherits optical_zoom_x.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 6.99,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_7_macro_capability": {
        // SCORING GOAL: Scores Macro Capability & Close-Focus Performance (MCFP). Evaluates three hardware paths (Ultrawide, Telemacro, Dedicated Macro Lens). The final score is the maximum across all three paths.
        "4_7_1_ultrawide_path": {
          // SCORING GOAL (4.7.1): Groups the ultrawide lens macro capability via Autofocus (AF) and Minimum Focus Distance. Only evaluated if an ultrawide lens is present (see 4_5_ultrawide_capability.presence).
          "ultrawide_autofocus": {
            "value": "Tier 1: Autofocus",
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE (4.7.1.1): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
            //   • "Tier 1: Autofocus"   → 10.00
            //   • "Tier 2: Fixed Focus" → 3.00
            //   If presence = false, "value" MUST be "Not present or not found", "source" and "exact_extract" must be "N/A", and "subscore" MUST be 0.00.
          },
          "min_focus_distance_cm": {
            "value": 2.5,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 7.31
            // SCORING GUIDELINE (4.7.1.2): Only evaluated if `4_5_ultrawide_capability.presence.value` = true. Apply the Section 4.7.1.2 logarithmic formula: Score = 10 * (log(Camera_Macro_Dist_cm_Max) − log(distance)) / (log(Camera_Macro_Dist_cm_Max) − log(Camera_Macro_Dist_cm_Min)), clamped 0–10. If `4_5_ultrawide_capability.presence.value` = false, then all fields of this block must be "N/A".
          },
          "scores": {
            "predicted": 8.39,
            // SCORING GUIDELINE: scores.predicted (Source: *Formula for 4.7.1 Ultrawide Path:* Score_4.7.1) = (0.40 * ultrawide_autofocus.subscore) + (0.60 * min_focus_distance_cm.subscore) if `4_5_ultrawide_capability.presence.value` = true; otherwise 0.00.
            "final": {
              // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
              "value": 8.39,
              "method_used": "Predictor",
              "booster": "No",
              "confidence": "N/A"
            }
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
            // CALCULATION: Zoom_Score = 10 * (log(telemacro_optical_x) − log(Camera_Telemacro_x_Min)) / (log(Camera_Telemacro_x_Max) − log(Camera_Telemacro_x_Min)), clamped 0–10.
            // If telemacro_presence = false, then all fields of this block must be "N/A".
          },
          "telemacro_min_focus_distance_cm": {
            "value": "N/A",
            "source": "N/A",
            "exact_extract": "N/A",
            "subscore": "N/A"
            // SCORING GUIDELINE: Only evaluated if telemacro_presence = true.
            // WHERE TO FIND IT: Look for "minimum focus distance", "closest focus distance" or "macro focus from X cm" specifically for the telephoto lens.
            // CALCULATION: MFD_Score = 10 * (log(Camera_Telemacro_MFD_cm_Max) − log(telemacro_min_focus_distance_cm)) / (log(Camera_Telemacro_MFD_cm_Max) − log(Camera_Telemacro_MFD_cm_Min)), clamped 0–10.
            // If telemacro_presence = false, then all fields of this block must be "N/A".
          },
          "scores": {
            "predicted": 0.00,
            // SCORING GUIDELINE: scores.predicted (Score_4.7.2) = 0.00 if telemacro_presence = false; otherwise Score = 7.0 + 0.3 * (0.70 * telemacro_optical_x.subscore + 0.30 * telemacro_min_focus_distance_cm.subscore).
            "final": {
              // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
              "value": 0.00,
              "method_used": "Predictor",
              "booster": "No",
              "confidence": "N/A"
            }
          }
        },
        "4_7_3_dedicated_path": {
          // SCORING GOAL (4.7.3): Scores a dedicated macro lens (a small fixed lens separate from the main/ultrawide/telephoto). Scores are capped at 3.00 to appropriately rank them below higher-quality macro implementations that use more capable primary or ultrawide sensors.
          "dedicated_macro_megapixels": {
            "value": 0,
            "source": "N/A",
            "exact_extract": "N/A",
            "subscore": 0.00
            // SCORING GUIDELINE: Apply the Section 4.7.3 linear formula: Score_4.7.3 = clamp(3.0 * dedicated_macro_megapixels / Camera_Dedicated_Macro_MP_Max, 0.00, 3.00). The score maps the Megapixels (MP) count linearly onto 0–3.00, where Camera_Dedicated_Macro_MP_Max scores 3.00. Values above Camera_Dedicated_Macro_MP_Max are capped at 3.00. A value of 0 MP means no dedicated macro lens (score = 0.00), in that case "source" and "exact_extract" must be "N/A" unless you find a source that explicitly states the device has no dedicated macro, in that case "source" and "exact_extract" should reflect that finding.
          },
          "scores": {
            "predicted": 0.00,
            // SCORING GUIDELINE: scores.predicted directly inherits dedicated_macro_megapixels.subscore.
            "final": {
              // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
              "value": 0.00,
              "method_used": "Predictor",
              "booster": "No",
              "confidence": "N/A"
            }
          }
        },
        "scores": {
          "predicted": 8.39,
          // SCORING GUIDELINE: scores.predicted (MCFP Score) = Max(Score_4.7.1, Score_4.7.2, Score_4.7.3). The system evaluates all three paths independently and awards the score of the best-performing hardware implementation.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.39,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_8_rear_video_resolution": {
        // SCORING GOAL: Scores the maximum spatial resolution supported for rear-camera video recording.
        "maximum_resolution": {
          "value": "Tier 2: 4K (Ultra HD)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the maximum rear video resolution. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: 8K"                    → 10.00
          //   • "Tier 2: 4K (Ultra HD)"         → 10.00
          //   • "Tier 3: 1440p / QHD (2.5K)"    → 8.00
          //   • "Tier 4: 1080p (Full HD)"       → 6.00
          //   • "Tier 5: 720p (HD)"             → 3.00
          //   • "Tier 6: ≤ 480p"                → 0.00
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits maximum_resolution.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_9_rear_video_frame_rate": {
        // SCORING GOAL: Scores the maximum standard frame rate achieved specifically at the device's highest supported resolution (as scored in Section 4.8), capped at 4K.
        "maximum_frames_per_second": {
          "value": 120,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the exact maximum Frames Per Second (FPS) supported at the resolution evaluated in Section "4_8_rear_video_resolution" capped at 4K. For example, if the device scored 8K in "4_8_rear_video_resolution", evaluate its 4K FPS instead. If the device scored 1080p in "4_8_rear_video_resolution", evaluate its 1080p FPS. Apply the Section 4.9 logarithmic formula: Score = 10 * (log(maximum_frames_per_second) − log(Camera_Video_FPS_Min)) / (log(Camera_Video_FPS_Max) − log(Camera_Video_FPS_Min)), clamped 0–10. Explicitly exclude any frame rates designated for "Slow Motion" or "High-Speed Burst" (e.g., 240fps+).
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits maximum_frames_per_second.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_10_video_hdr": {
        // SCORING GOAL: Scores which High Dynamic Range (HDR) video formats the camera system can record in. Dynamic HDR formats (Dolby Vision, HDR10+) optimize brightness and colour frame-by-frame for superior realism and grading headroom.
        "supported_formats": {
          "value": [
            "Dolby Vision",
            "HDR10"
          ],
          "value_details": {
            "Dolby Vision": [
              { "name": "Dolby Vision", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "HDR10+": [],
            "HDR10": [
              { "name": "HDR10", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "HLG": []
          },
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the presence of officially supported High Dynamic Range (HDR) video recording formats. For each supported format, use its exact term below for the "value" array:
          //   • "Dolby Vision"             → adds +3.00 to the subscore
          //   • "HDR10+"                   → adds +2.00 to the subscore
          //   • "HDR10" or "HLG"           → adds +5.00 to the subscore (Base HDR tier, points do not stack)
          // The subscore is the sum of these points (Clamped 0–10). If no HDR recording is supported (standard Standard Dynamic Range / SDR), leave the array empty [] and set subscore to 0.00.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported HDR formats found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply. 
        },
        "scores": {
          "predicted": 8.00,
          // SCORING GUIDELINE: scores.predicted directly inherits supported_formats.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_11_video_encoding": {
        // SCORING GOAL: Scores support for professional codecs and recording profiles as a composite index.
        "professional_codec_support": {
          "value": "Tier 2: Mezzanine",
          "value_details": {
            "Tier 1: True RAW": [],
            "Tier 2: Mezzanine": [
              { "name": "ProRes", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: Standard": []
          },
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the highest supported professional recording codec tier. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: True RAW"    → 10.00
          //     Definition: Uncompressed or losslessly compressed raw video data with full sensor bit depth. Qualifying terms: CinemaDNG, Blackmagic RAW, ProRes RAW, Internal RAW.
          //   • "Tier 2: Mezzanine"   → 8.00
          //     Definition: High-bitrate intermediate production codecs with intra-frame compression. Qualifying terms: Apple ProRes 422 (HQ/Standard/LT/Proxy), Samsung Professional Video (ProRes), Xiaomi ProRes.
          //   • "Tier 3: Standard"    → 0.00
          //     Definition: Industry-standard distribution codecs (H.264/AVC, H.265/HEVC) without dedicated professional containers.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported professional codecs found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "log_color_profile_support": {
          "value": "Tier 1: True Log",
          "value_details": {
            "Tier 1: True Log": [
              { "name": "Apple Log", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 2: Flat / Cine": [],
            "Tier 3: Standard only": []
          },
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the supported log profiles. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: True Log"       → 10.00
          //     Definition: Logarithmic gamma curve for professional grading (e.g., Apple Log, S-Log3, D-Log).
          //   • "Tier 2: Flat / Cine"    → 5.00
          //     Definition: Desaturated profiles that are not mathematically logarithmic (e.g., S-Cinetone, D-Cinelike).
          //   • "Tier 3: Standard only"  → 0.00
          //     Definition: No professional gamma profiles; only standard rec.709 or rec.2020 curves.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported log/flat profiles found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "color_bit_depth": {
          "value": "Tier 2: 10-bit color",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 5.00
          // SCORING GUIDELINE: Use the following exact same Tier Names for "value" with related scores as subscore: 
          //   • "Tier 1: 12-bit color" → 10.00
          //   • "Tier 2: 10-bit color" → 5.00
          //   • "Tier 3: 8-bit color"  → 0.00
        },
        "scores": {
          "predicted": 7.95,
          // SCORING GUIDELINE: scores.predicted = (0.40 * professional_codec_support.subscore) + (0.35 * log_color_profile_support.subscore) + (0.25 * color_bit_depth.subscore).
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 7.95,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
          // SCORING GUIDELINE: Enter all Resolution/Frames per Second(FPS) pairs explicitly listed in the device's secondary video specifications under marketing terms like "Slow Motion" or "High Speed Video" (Do NOT use standard video resolutions). Calculate MP/s (Resolution * FPS) for each pair and place the combination yielding the absolute highest MP/s in the VERY FIRST position of this array. If no dedicated slow-motion mode exists, leave the array empty [].
        },
        "scores": {
          "predicted": 8.55,
          // SCORING GUIDELINE: Use the first item in `supported_modes.value` (the highest MP/s pair) to calculate MP_s = resolution_megapixels * frames_per_second. Apply the Section 4.12 logarithmic formula: scores.predicted = 10 * (log(MP_s) − log(Camera_SlowMo_MPs_Min)) / (log(Camera_SlowMo_MPs_Max) − log(Camera_SlowMo_MPs_Min)), clamped 0–10. If the array is empty, set scores.predicted to 0.00.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.55,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_13_front_camera_resolution": {
        // SCORING GOAL: Scores the spatial resolution of the front-facing camera.
        "megapixels": {
          "value": 12,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "scores": {
          "predicted": 4.72,
          // SCORING GUIDELINE: Mirroring Section 4.3 (Main Camera Resolution). Apply the Section 4.13 logarithmic formula: Score = 10 * (log(megapixels) − log(Camera_Front_Resolution_MP_Min)) / (log(Camera_Front_Resolution_MP_Max) − log(Camera_Front_Resolution_MP_Min)), clamped 0–10.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 4.72,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
          "value": "Tier 1: Autofocus",
          "value_details": {
            "Tier 1: Autofocus": [
              { "name": "Phase Detection Auto Focus (PDAF)", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 2: Fixed Focus (Modern Wide-DOF)": [],
            "Tier 3: Fixed Focus (Legacy Narrow-DOF)": [],
            "Tier 4: No Front Camera": []
          },
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the front camera's focus type. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Autofocus"                        → 10.00
          //     Definition: An active mechanical system where the lens moves to find focus (e.g., Phase Detection Auto Focus (PDAF), Dual Pixel, or Laser Auto Focus).
          //   • "Tier 2: Fixed Focus (Modern Wide-DOF)"    → 6.00
          //     Definition: A lens with no moving hardware parts configured for a wide Depth of Field (DOF) focus zone. Identified by (aperture_f_number ≥ 2.0) OR (sensor_size ≤ 1/3").
          //   • "Tier 3: Fixed Focus (Legacy Narrow-DOF)"  → 3.00
          //     Definition: A lens with no moving hardware parts featuring a narrow Depth of Field (DOF) focus zone. Identified by (aperture_f_number < 2.0) AND (sensor_size > 1/3").
          //   • "Tier 4: No Front Camera"                  → 0.00
          //     Definition: Device lacks a front-facing selfie camera module.
          // AMBIGUITY RESOLUTION: Focus Zone width is determined by Depth of Field (DOF). If sensor size data is missing, classify based solely on the aperture (f-number) if it is known.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are **arrays of objects**. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits focus_system_tier.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_15_front_camera_video": {
        // SCORING GOAL: Scores maximum video capture capability (resolution, frame rate, High Dynamic Range (HDR), and Professional Recording) of the front camera as a composite score.
        "4_15_1_video_resolution": {
          "maximum_resolution": {
            "value": "Tier 2: 4K (Ultra HD)",
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.8 (Rear Video Resolution). Identify the maximum front video resolution. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
            //   • "Tier 1: 8K"                    → 10.00
            //   • "Tier 2: 4K (Ultra HD)"         → 10.00
            //   • "Tier 3: 1440p / QHD (2.5K)"    → 8.00
            //   • "Tier 4: 1080p (Full HD)"       → 6.00
            //   • "Tier 5: 720p (HD)"             → 3.00
            //   • "Tier 6: ≤480p"                 → 0.00
          }
        },
        "4_15_2_video_frame_rate": {
          "maximum_frames_per_second": {
            "value": 60,
            "source": "TBD",
            "exact_extract": "Proof pending",
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.9 (Rear Video Frame Rate). Identify the maximum Frames per second (FPS) specifically at the resolution listed in "4_15_1_video_resolution.maximum_resolution", capped at 4K. For example, if the device scored 8K in "4_15_1_video_resolution", evaluate its 4K FPS instead. If the device scored 1080p in "4_15_1_video_resolution", evaluate its 1080p FPS. Apply the Section 4.15.2 logarithmic formula: FPSScore = 10 * (log(maximum_frames_per_second) − log(Camera_Front_Video_FPS_Min)) / (log(Camera_Front_Video_FPS_Max) − log(Camera_Front_Video_FPS_Min)), clamped 0–10.
          }
        },
        "4_15_3_video_hdr": {
          "supported_formats": {
            "value": [
              "Dolby Vision",
              "HDR10+",
              "HDR10"
            ],
            "value_details": {
              "Dolby Vision": [
                { "name": "Dolby Vision", "source": "TBD", "exact_extract": "Proof pending" }
              ],
              "HDR10+": [
                { "name": "HDR10+", "source": "TBD", "exact_extract": "Proof pending" }
              ],
              "HDR10": [
                { "name": "HDR10", "source": "TBD", "exact_extract": "Proof pending" }
              ],
              "HLG": []
            },
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.10 (Rear Video HDR). Identify the presence of officially supported High Dynamic Range (HDR) video recording formats. For each supported format, use its exact term below for the "value" array:
            //   • "Dolby Vision"             → adds +3.00 to the subscore
            //   • "HDR10+"                   → adds +2.00 to the subscore
            //   • "HDR10" or "HLG"           → adds +5.00 to the subscore (Base HDR tier, points do not stack)
            // The subscore is the sum of these points (Clamped 0–10). If no HDR recording is supported (standard Standard Dynamic Range / SDR), leave the array empty [] and set subscore to 0.00.
            // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported HDR formats found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply.
          }
        },
        "4_15_4_1_professional_codec_support": {
          "supported_codecs": {
            "value": "Tier 2: Mezzanine",
            "value_details": {
              "Tier 1: True RAW": [],
              "Tier 2: Mezzanine": [
                { "name": "ProRes", "source": "TBD", "exact_extract": "Proof pending" }
              ],
              "Tier 3: Standard": []
            },
            "subscore": 8.00
          // SCORING GUIDELINE: Mirroring Section 4.11.1 (PCS). Identify the highest supported professional recording codec tier. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: True RAW"    → 10.00
          //     Definition: Uncompressed or losslessly compressed raw video data with full sensor bit depth. Qualifying terms: CinemaDNG, Blackmagic RAW, ProRes RAW, Internal RAW.
          //   • "Tier 2: Mezzanine"   → 8.00
          //     Definition: High-bitrate intermediate production codecs with intra-frame compression. Qualifying terms: Apple ProRes 422 (HQ/Standard/LT/Proxy), Samsung Professional Video (ProRes), Xiaomi ProRes.
          //   • "Tier 3: Standard"    → 0.00
          //     Definition: Industry-standard distribution codecs (H.264/AVC, H.265/HEVC) without dedicated professional containers.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported professional codecs found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
          }
        },
        "4_15_4_2_log_color_profile_support": {
          "supported_profiles": {
            "value": "Tier 1: True Log",
            "value_details": {
              "Tier 1: True Log": [
                { "name": "Apple Log", "source": "TBD", "exact_extract": "Proof pending" }
              ],
              "Tier 2: Flat / Cine": [],
              "Tier 3: Standard only": []
            },
            "subscore": 10.00
            // SCORING GUIDELINE: Mirroring Section 4.11.2 (LCP). Identify the supported log profiles. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
            //   • "Tier 1: True Log"       → 10.00
            //     Definition: Logarithmic gamma curve for professional grading (e.g., Apple Log, S-Log3, D-Log).
            //   • "Tier 2: Flat / Cine"    → 5.00
            //     Definition: Desaturated profiles that are not mathematically logarithmic (e.g., S-Cinetone, Cinelike-D).
            //   • "Tier 3: Standard only"  → 0.00
            //     Definition: No professional gamma profiles. only standard rec.709 or rec.2020 curves.
            // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported log/flat profiles found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
          }
        },
        "scores": {
          "predicted": 9.80,
          // SCORING GUIDELINE: scores.predicted = (0.35 * 4_15_1_video_resolution.maximum_resolution.subscore) + (0.25 * 4_15_2_video_frame_rate.maximum_frames_per_second.subscore) + (0.20 * 4_15_3_video_hdr.supported_formats.subscore) + (0.10 * 4_15_4_1_professional_codec_support.supported_codecs.subscore) + (0.10 * 4_15_4_2_log_color_profile_support.supported_profiles.subscore).
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 9.80,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_16_multiframe_photo": {
        // SCORING GOAL: Scores camera system's automatic multi-frame capture and stacking capabilities. 
        "processing_tier": {
          "value": "Tier 1: Advanced Semantic & Neural Stacking",
          "value_details": {
            "Tier 1: Advanced Semantic & Neural Stacking": [
              { "name": "Deep Fusion", "source": "TBD", "exact_extract": "Proof pending" },
              { "name": "Photonic Engine", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 2: Standard Always-on Multi-Frame HDR": [
              { "name": "Smart HDR 5", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: Conditional / Manual Multi-Frame": [],
            "Tier 4: Basic / Single Frame (Legacy)": []
          },
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the Multi-Frame Computational Photography (MFCP) tier. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Advanced Semantic & Neural Stacking" → 10.0
          //     Definition: Advanced pipeline that uses semantic segmentation (understanding sky, faces, skin) within a Zero Shutter Lag (ZSL) multi-frame buffer.
          //   • "Tier 2: Standard Always-on Multi-Frame HDR"  → 7.5
          //     Definition: Always-on multi-frame HDR capture (e.g., Smart HDR) without advanced per-pixel semantic segmentation.
          //   • "Tier 3: Conditional / Manual Multi-Frame"    → 5.0
          //     Definition: Multi-frame processing only activates in specific modes (e.g., Night Mode) or requires manual activation (HDR toggle).
          //   • "Tier 4: Basic / Single Frame (Legacy)"       → 0.0
          //     Definition: No multi-frame stacking; reliance on single-frame exposure.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported multi-frame features found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits processing_tier.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_17_pipeline_semantic_ai": {
        // SCORING GOAL: Automatic Capture-Time AI. Scores the ability of the software to segment scenes and subjects using Artificial Intelligence (AI).
        "capability_tier": {
          "value": "Tier 1: Neural Semantic Segmentation",
          "value_details": {
            "Tier 1: Neural Semantic Segmentation": [
              { "name": "AI ProVisual Engine", "source": "TBD", "exact_extract": "Proof pending" },
              { "name": "Object-aware engine", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 2: Object-Based Optimization": [],
            "Tier 3: Basic Metadata AI": [],
            "Tier 4: None": []
          },
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the Pipeline AI tier. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Neural Semantic Segmentation" → 10.0
          //     Definition: Real-time, pixel-level differentiation between multiple semantic categories (skin, sky, hair, eyes, teeth) during captured multi-frame pipeline.
          //   • "Tier 2: Object-Based Optimization"    → 7.5
          //     Definition: Recognizes high-level subjects (dog, flower, sunset) to apply preset global/local enhancements ("Scene Optimizer").
          //   • "Tier 3: Basic Metadata AI"            → 4.0
          //     Definition: Simple EXIF-level scene recognition (e.g., "Food", "Text") without intelligent segmentation or pixel-level relighting.
          //   • "Tier 4: None"                         → 0.0
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported AI pipeline features found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits capability_tier.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "4_18_post_capture_ai_tools": {
        // SCORING GOAL: User-Initiated Gallery-Time Artificial Intelligence (AI). Scores the ability to modify images after capture using AI tools.
        "feature_tier": {
          "value": "Tier 1: Generative Content Transformation",
          "value_details": {
            "Tier 1: Generative Content Transformation": [
              { "name": "Magic Editor", "source": "TBD", "exact_extract": "Proof pending" },
              { "name": "Best Take", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 2: Advanced Semantic Edits": [],
            "Tier 3: Basic Algorithmic Fixes": [],
            "Tier 4: None": []
          },
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the Post-Capture AI tier. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Generative Content Transformation" → 10.0
          //     Definition: Advanced on-device or cloud-based generative AI that can add, remove, move, or transform objects within an image with pixel-accurate context awareness.
          //   • "Tier 2: Advanced Semantic Edits"           → 7.50
          //     Definition: Rule-based or shallow-learning tools for localized adjustments (shadow/reflection removal, face unblur, object erasure without generative fill).
          //   • "Tier 3: Basic Algorithmic Fixes"           → 4.00
          //     Definition: Standard beauty filters, color-aware auto-fixing, or basic object prioritization for cropping.
          //   • "Tier 4: None"                              → 0.0
          //     Definition: No AI-enhanced editing tools beyond standard gallery filters.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported AI features found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits feature_tier.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
      "5_1_support_longevity": {
        // SCORING GOAL: Scores the manufacturer's software update commitment. The score is dynamic and decays as the device ages relative to its end_of_support_date.
        //   • Goal: Measure "Safe Utility Lifespan" (Longevity).
        //   • Anchor: The latest (most future) date between Operating System (OS) and Security support.
        "launch_date_ref": {
          "value": "2024-01-24",
          "value_path": "identity.release_date.value"
          // Use the global launch date (identity.release_date) as the baseline for all calculations below.
        },
        "os_end_date": {
          "value": "2031-01-24",
          "source": "TBD",
          "exact_extract": "Proof pending"
          // GUIDELINE: Record the verbatim phrase for Operating System (OS) updates (e.g., "4 generations of OS updates"). Translate to a date:
          //   • os_end_date.value = launch_date_ref.value + X Years (Rule: 1 Generation = 1 Year).
          //   • Result must be an ISO 8601 date (YYYY-MM-DD).
        },
        "security_end_date": {
          "base_security_end_date": {
            "value": "2030-01-24",
            "source": "TBD",
            "exact_extract": "Proof pending"
            // GUIDELINE: Record the verbatim phrase for standard Security updates (e.g., "Security updates until Jan 2029" or "5 years of security updates"). Translate to a date:
            //   • If "Until [Date]": base_security_end_date.value = [Date].
            //   • If "X Years": base_security_end_date.value = launch_date_ref.value + X Years.
          },
          "enterprise_extension_years": {
            "value": 1,
            "source": "TBD",
            "exact_extract": "Proof pending"
            // GUIDELINE: Record the additional years of security support for Enterprise/Business editions (e.g., "+1" or "+2 years"). If not applicable, set value to 0.
          },
          "value": "2031-01-24"
          // GUIDELINE: security_end_date.value = (security_end_date.base_security_end_date.value extended by security_end_date.enterprise_extension_years.value).
        },
        "end_of_support_date": {
          "value": "2031-01-24",
          "subscore": "[DYNAMIC_CALCULATION: Formula_Section_5_1]"
          // GUIDELINE: end_of_support_date.value = Max(os_end_date.value, security_end_date.value).
          // SCORING RECIPE: 
          //   1. Determine Remaining_Years: (end_of_support_date.value - Current_Date).
          //   2. Calculate subscore: 10 * (log(Remaining_Years) - log(Support_Years_Min)) / (log(Support_Years_Max) - log(Support_Years_Min)).
          //   3. Clamping: Minimum 0, Maximum 10.
        },
        "scores": {
          "predicted": "[DYNAMIC_CALCULATION: Section_5_1.end_of_support_date.subscore]",
          // SCORING GUIDELINE: scores.predicted directly inherits end_of_support_date.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": "[DYNAMIC_CALCULATION: Section_5_1.end_of_support_date.subscore]",
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "5_2_system_cleanliness_control": {
        // SCORING GOAL: Evaluates the out-of-box software experience by analyzing Preinstalled App Load (PAL), User Control (UC), and System Ads (SA).
        "skin": {
          "value": "One UI 6.1",
          "source": "TBD",
          "exact_extract": "Proof pending"
          // DATA GUIDELINE: Record the exact Original Equipment Manufacturer (OEM) skin / platform name as declared by the manufacturer.
          // SCORING GUIDELINE: ALL subscores below (PAL, UC, SA) MUST be extracted directly from this Skin Lookup Table based on the `skin` value.
          //
          // █ SKIN_LOOKUP_TABLE:
          // | Platform / Skin                           | PAL Score (40%) | UC Score (30%) | SA Score (30%) | *Composite* |
          // | :---------------------------------------- | :-------------: | :------------: | :------------: | :---------: |
          // | **iOS**                                   | **10.0**        | **10.0**       | **10.0**       | *10.00*     |
          // | **Pixel UI / Stock Android**              | **10.0**        | **10.0**       | **10.0**       | *10.00*     |
          // | **AOSP / Fairphone OS / Nothing OS**      | **10.0**        | **10.0**       | **10.0**       | *10.00*     |
          // | **Motorola MyUX / Hello UI**              | **6.0**         | **10.0**       | **10.0**       | *8.40*      |
          // | **Sony Xperia UI / Sharp AQUOS / Nokia**  | **6.0**         | **10.0**       | **10.0**       | *8.40*      |
          // | **ASUS ZenUI / ROG UI**                   | **6.0**         | **10.0**       | **10.0**       | *8.40*      |
          // | **Redmagic OS**                           | **3.0**         | **10.0**       | **10.0**       | *7.20*      |
          // | **Funtouch OS (Vivo)**                    | **6.0**         | **5.0**        | **10.0**       | *6.90*      |
          // | **LG UX / HTC Sense (Legacy)**            | **6.0**         | **5.0**        | **5.0**        | *5.40*      |
          // | **OxygenOS (OnePlus)**                    | **3.0**         | **5.0**        | **5.0**        | *4.20*      |
          // | **Samsung One UI**                        | **3.0**         | **5.0**        | **5.0**        | *4.20*      |
          // | **ColorOS / Realme UI / OriginOS / Vivo** | **3.0**         | **5.0**        | **5.0**        | *4.20*      |
          // | **Honor MagicOS**                         | **3.0**         | **5.0**        | **5.0**        | *4.20*      |
          // | **ZTE MiFavor UI / MyOS**                 | **3.0**         | **5.0**        | **5.0**        | *4.20*      |
          // | **HyperOS (Xiaomi) / Huawei EMUI**        | **0.0**         | **5.0**        | **0.0**        | *1.50*      |
          // | **MIUI (Legacy Xiaomi)**                  | **0.0**         | **0.0**        | **0.0**        | *0.00*      |
          // | **Tecno HiOS / Infinix XOS / Itel OS**    | **0.0**         | **0.0**        | **0.0**        | *0.00*      |
        },
        "5_2_1_preinstalled_app_load_score": {
          "identifier": "Samsung One UI",
          // GUIDELINE: Standardized name from the SKIN_LOOKUP_TABLE corresponding to the device's `skin.value`.
          "reference_table": "SKIN_LOOKUP_TABLE",
          // GUIDELINE: Path to the authoritative lookup table for mapping.
          "lookup_parameter": "Preinstalled App Load (PAL) Score",
          // GUIDELINE: Description of the column being retrieved.
          "value": 3.00
          // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter` (e.g. PAL). 
          // For info only:
          //   • "Tier 1: Minimal / Core Only"        → 10.00
          //     Definition: No third-party applications or redundant first-party duplicates.
          //   • "Tier 2: Moderate Proprietary"       →  6.00
          //     Definition: First-party duplicates present (e.g., two browsers), rare third-party.
          //   • "Tier 3: Significant Bloat"          →  3.00
          //     Definition: Multiple pre-loaded social media apps, games, and partner software.
          //   • "Tier 4: Extreme Bloat"              →  0.00
          //     Definition: Dozens of third-party apps and promotional "Hot Apps" folders out-of-box.
        },
        "5_2_2_user_control_score": {
          "identifier": "Samsung One UI",
          // GUIDELINE: Standardized name from the SKIN_LOOKUP_TABLE corresponding to the device's `skin.value`.
          "reference_table": "SKIN_LOOKUP_TABLE",
          // GUIDELINE: Path to the authoritative lookup table for mapping.
          "lookup_parameter": "User Control (UC) Score",
          // GUIDELINE: Description of the column being retrieved.
          "value": 5.00
          // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter` (e.g. UC).
          // For info only:
          //   • "Tier 1: Fully Uninstallable"       → 10.00
          //     Definition: Almost all non-essential apps can be completely deleted.
          //   • "Tier 2: Disabling Only"            →  5.00
          //     Definition: Many apps cannot be deleted but can be natively hidden and "disabled".
          //   • "Tier 3: Highly Restrictive"        →  0.00
          //     Definition: Core bloatware runs in the background and cannot be turned off normally.
        },
        "5_2_3_system_ads_score": {
          "identifier": "Samsung One UI",
          // GUIDELINE: Standardized name from the SKIN_LOOKUP_TABLE corresponding to the device's `skin.value`.
          "reference_table": "SKIN_LOOKUP_TABLE",
          // GUIDELINE: Path to the authoritative lookup table for mapping.
          "lookup_parameter": "System Advertisements (SA) Score",
          // GUIDELINE: Description of the column being retrieved.
          "value": 5.00
          // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter` (e.g. SA).
          // For info only:
          //   • "Tier 1: Ad-Free"                   → 10.00
          //     Definition: Zero system-level advertisements or promotional pushes.
          //   • "Tier 2: Opt-Out / Occasional"      →  5.00
          //     Definition: Native app promotions exist but can be permanently deactivated.
          //   • "Tier 3: Intrusive / Persistent"    →  0.00
          //     Definition: Mandatory UI ads and lock screen promotions that cannot be disabled.
        },
        "scores": {
          "predicted": 4.20,
          // SCORING GUIDELINE: scores.predicted = (0.40 * 5_2_1_preinstalled_app_load_score.value) + (0.30 * 5_2_2_user_control_score.value) + (0.30 * 5_2_3_system_ads_score.value). Alternatively, use the *Composite* score from the SKIN_LOOKUP_TABLE directly.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 4.20,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "5_3_ai_feature_suite": {
        // SCORING GOAL: Evaluates the specific AI software features available. Score is calculated using weighted binary features. Max score is 10.00.
        // EXTRACTION GUIDELINE: Identify the specific Marketing Name found in official specs or reviewer evidence. If the phone has the capability under any name (Circle to Search, Magic Portal, etc.), set "value" to that name. If the feature is missing, set "value" to "None".
        "visual_screen_search": {
          "value": "Circle to Search",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If value = "None", subscore = 0.00. Otherwise, subscore = 2.00.
          // Definition: A system-level visual search tool. The phone identifies an item and returns search results without leaving the app.
          // Marketing Names: Circle to Search (Google, Samsung, Xiaomi, Oppo, OnePlus, Realme, Honor, Vivo, Motorola, Asus, Nothing), Visual Intelligence / Visual Look Up (Apple), Magic Portal (Honor), AI Screen Recognition (ZTE, Nubia, Redmagic, Tecno, Infinix), AI Search (Nothing, Itel).
        },
        "live_speech_translation": {
          "value": "Live Translate",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.50
          // SCORING GUIDELINE: If value = "None", subscore = 0.00. Otherwise, subscore = 1.50.
          // Definition: Real-time voice or text translation during calls or in-person conversations natively embedded in the system.
          // Marketing Names: Live Translate (Samsung, Google), Interpreter (Samsung, Google, Xiaomi, Oppo, OnePlus, Vivo, Realme, iQOO), Translate App: Auto-Translate (Apple), AI Call Translator / Assistant (Asus, ROG, Vivo), AI Call Translation (Honor, ZTE, Tecno, Infinix), AI Real-time Subtitles / Live Subtitles (Xiaomi, Oppo, Vivo), AI Real-time Translation (Nubia, Redmagic), Moto AI Translate (Motorola), Ella Translate (Tecno, Infinix).
        },
        "content_summarization": {
          "value": "Note Assist",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If value = "None", subscore = 0.00. Otherwise, subscore = 2.00.
          // Definition: Condenses long-form content (web pages, articles, notes) into a short summary.
          // Marketing Names: Note Assist / Browsing Assist (Samsung), Recorder Summarize (Google), Writing Tools: Summarize / Notification Summaries (Apple), AI Summary / AI Web Page Summary (Xiaomi, Oppo, OnePlus, Realme, Honor, Vivo, iQOO, ZTE, Nubia, Redmagic, Tecno, Infinix, Asus, ROG), Catch Me Up (Motorola).
        },
        "writing_tools": {
          "value": "Chat Assist",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.50
          // SCORING GUIDELINE: If value = "None", subscore = 0.00. Otherwise, subscore = 0.50.
          // Definition: System-wide AI text rewriting, tone adjustment, or proofreading available in any text field.
          // Marketing Names: Chat Assist / Keyboard AI (Samsung), Magic Compose / Help me write (Google, Gboard), Writing Tools: Rewrite / Proofread (Apple), AI Writing Assistant / AI Writer (Xiaomi, Oppo, OnePlus, Realme, Honor, Vivo, iQOO, ZTE, Tecno, Infinix, Asus, ROG), AI Creative Writing (Nubia, Redmagic), Magic Text (Honor), Style Sync (Motorola).
        },
        "meeting_call_transcription": {
          "value": "Transcribe Assist",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If value = "None", subscore = 0.00. Otherwise, subscore = 2.00.
          // Definition: Auto-generates text from recordings or live calls into meeting minutes or transcripts.
          // Marketing Names: Transcript Assist (Samsung), Recorder: AI Transcription (Google), Call Notes (Google), Call Transcription / Audio Transcription (Apple), AI Recorder / AI Recording Summary (Xiaomi, Oppo, OnePlus, Realme, Honor, Vivo, iQOO, ZTE, Nubia, Redmagic, Tecno, Infinix), AI Voice Scribe (Oppo, OnePlus), AI Transcript / AI Voice Recording (Asus, ROG, Vivo), Pay Attention (Motorola).
        },
        "on_device_reliability": {
          "value": "Gemini Nano",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: If value = "None", subscore = 0.00. Otherwise, subscore = 2.00.
          // Definition: The device can run its core generative AI features locally (via NPU/TPU) without requiring a persistent cloud/internet connection.
          // Marketing Names: "Process data only on device" (Samsung, Google, Xiaomi, Apple), Gemini Nano (Google, Samsung, Motorola, Realme), Private Cloud Compute / Secure Enclave (Apple), MagicLM On-Device (Honor), BlueLM (Vivo, iQOO), HyperMind / HyperAI (Xiaomi), Breeno / AndesBrain (Oppo), Nebula AI Model (ZTE, Nubia, Redmagic), Moto AI On-Device (Motorola), Ella AI (Tecno, Infinix).
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted is the sum of all subscores in this block (visual_screen_search + live_speech_translation + content_summarization + writing_tools + meeting_call_transcription + on_device_reliability).
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      }
    },
    "6_processing_power_and_performance": {
      
      // █ CPU_CORE_ARCHITECTURE_LOOKUP_TABLE
      // Defines CAS (Core Architecture Score) and Ref Freq (Reference Frequency).
      // 
      // | CPU Core Architecture        | Score | Ref Freq (GHz) |
      // |:-----------------------------|:-----:|:--------------:|
      // | Apple Everest (A18/Pro)      | 10.00 |      4.05      |
      // | Oryon Gen 2 (SD 8 Elite)     | 10.00 |      4.32      |
      // | Cortex-X925 / Lumex Ultra    |  9.00 |      3.60      |
      // | Apple A17 Pro Cores          |  9.00 |      3.78      |
      // | Apple A16 Bionic             |  8.00 |      3.46      |
      // | Cortex-X4                    |  8.00 |      3.30      |
      // | Apple A15 Bionic             |  7.00 |      3.22      |
      // | Cortex-X3                    |  7.00 |      3.20      |
      // | Apple A14 Bionic             |  6.00 |      3.10      |
      // | Cortex-X2                    |  6.00 |      3.00      |
      // | Cortex-X1                    |  5.00 |      2.84      |
      // | Cortex-A725 / A720           |  5.00 |      2.80      |
      // | Cortex-A715 / A710           |  4.00 |      2.50      |
      // | Cortex-A78 / A77             |  3.00 |      2.40      |
      // | Cortex-A76                   |  2.00 |      2.20      |
      // | Cortex-A75 / A73             |  1.00 |      2.00      |
      // | Cortex-A525 / A520 / A510    |  1.00 |      2.00      |
      // | Cortex-A55 / A53             |  0.00 |      1.80      |
      // | Legacy 32-bit (A7 / A9)      |  0.00 |      1.50      |
      // -------------------------------------------------------------------------

      "6_1_0_system_on_chip_reference": {
        // SCORING GOAL: Serves as the authoritative hardware reference for the SoC (System on Chip) architecture, including core counts and architectural types.
        "value": "Snapdragon 8 Gen 3",
        // GUIDELINE: Inherits the chipset model name from the device identity record.
        "value_path": "identity.hardware_configuration.chipset.value",
        // GUIDELINE: Absolute path to the chipset identifier in the device identity section.
        "clusters": [
          // GUIDELINE: The number of cluster objects and their roles (e.g., "Prime", "Performance", "Efficiency") must be dynamically adjusted (added or removed) to match the specific SoC architecture (e.g., 2 clusters for Apple, 3 for most Android).
          {
            "role": "Prime",
            // GUIDELINE: The functional role of the cluster (e.g., "Prime", "Performance", "Efficiency").
            "architecture": "Cortex-X4",
            // GUIDELINE: The specific CPU core architecture name matching the Table above (e.g., "Cortex-X4").
            "count": 1,
            // GUIDELINE: The number of cores contained in this specific cluster.
            "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
            // GUIDELINE: Direct source URL for architectural data (type and count).
            "exact_extract": "Cortex-X4"
            // GUIDELINE: The verbatim proof from the source confirming architecture type and core count.
          },
          {
            "role": "Performance",
            "architecture": "Cortex-A720",
            "count": 5,
            "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
            "exact_extract": "Cortex-A720"
          },
          {
            "role": "Efficiency",
            "architecture": "Cortex-A520",
            "count": 2,
            "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
            "exact_extract": "Cortex-A520"
          }
        ]
      },
      "6_1_cpu_multi_core_performance": {
        // SCORING GOAL: Measures the actual delivered CPU performance during intense, multi-threaded workloads to ensure the device can handle heavy multitasking, gaming physics, and background processing. A three-method hierarchy (A→B→C) is used. Method A uses the Geekbench 6 Multi-Core benchmark when available. Method B uses Nearest Neighbor Interpolation when only similar devices have benchmarks. Method C (Predictor) is the fallback predicted score.
        
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Direct Benchmark (Primary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_CPU_multi": {
          "value": 7200,
          "source": "https://browser.geekbench.com/android-benchmarks",
          "exact_extract": "Samsung Galaxy S24 Ultra [...] 7200",
          "subscore": 8.63
          // SCORING GUIDELINE: primary benchmark is Geekbench 6 Multi-Core.
          // • WHERE TO FIND IT: Query browser.geekbench.com for the host SoC or exact device model.
          // • EXTRACTION RULE: Use the "Multi-Core Score" from the "Android" or "iOS" category. Verify version is 6.x. Do NOT use v4/v5 or Single-Core scores.
          // SCORING GUIDELINE: subscore = 10 * (log(method_a_benchmark_CPU_multi.value) − log(CPU_GB6_Multi_Score_Min)) / (log(CPU_GB6_Multi_Score_Max) − log(CPU_GB6_Multi_Score_Min)), clamped 0–10. If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Throughput Prediction Model (Tertiary / baseline for Method B)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_CPU_multi": {
          // GUIDELINE: Instead of fixed cluster keys, use an array of objects for each core cluster defined in §6.1.0. The number of blocks in this array must exactly match the number of clusters found in the SoC (System on Chip) reference. Add or remove cluster blocks accordingly.
          "clusters": [
            {
              "core_architecture_score": {
                "identifier": "Cortex-X4",
                // GUIDELINE: Standardized core architecture name matching the record in 6_1_0_system_on_chip_reference.clusters[0].architecture
                "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "CPU Score",
                // GUIDELINE: Description of the column being retrieved.
                "value": 8.00
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              },
              "reference_frequency_ghz": {
                "identifier": "Cortex-X4",
                // GUIDELINE: Standardized core architecture name matching the record in 6_1_0_system_on_chip_reference.clusters[0].architecture
                "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "Ref Freq (GHz)",
                // GUIDELINE: Description of the column being retrieved.
                "value": 3.30
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              },
              "core_count": {
                "value": 1,
                // GUIDELINE: Inherits count from the referenced §6.1.0 cluster.
                "value_path": "6_1_0_system_on_chip_reference.clusters[0].count"
                // GUIDELINE: Absolute path to the core count in Section 6.1.0.
              },
              "actual_frequency_ghz": {
                "value": 3.3,
                "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
                "exact_extract": "1x 3.3 GHz"
                // GUIDELINE: The maximum advertised frequency for this specific core cluster in GHz.
              },
              "frequency_adjusted_core_score": 8.0000,
                // GUIDELINE: core_architecture_score.value * core_count.value * actual_frequency_ghz.value / reference_frequency_ghz.value Total throughput contribution of this cluster. Keep 4 decimal places (e.g. 9.5478) to preserve precision.
            },
            {
              "core_architecture_score": {
                "identifier": "Cortex-A720",
                // GUIDELINE: Standardized core architecture name matching the record in 6_1_0_system_on_chip_reference.clusters[1].architecture
                "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "CPU Score",
                // GUIDELINE: Description of the column being retrieved.
                "value": 5.00
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              },
              "reference_frequency_ghz": {
                "identifier": "Cortex-A720",
                // GUIDELINE: Standardized core architecture name matching the record in 6_1_0_system_on_chip_reference.clusters[1].architecture
                "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "Ref Freq (GHz)",
                // GUIDELINE: Description of the column being retrieved.
                "value": 2.80
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              },
              "core_count": {
                "value": 5,
                // GUIDELINE: Inherits count from the referenced §6.1.0 cluster.
                "value_path": "6_1_0_system_on_chip_reference.clusters[1].count"
                // GUIDELINE: Absolute path to the core count in Section 6.1.0.
              },
              "actual_frequency_ghz": {
                "value": 3.2,
                "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
                "exact_extract": "5x 3.2 GHz"
                // GUIDELINE: The maximum advertised frequency for this specific core cluster in GHz.
              },
              "frequency_adjusted_core_score": 28.5714, 
                // GUIDELINE: core_architecture_score.value * core_count.value * actual_frequency_ghz.value / reference_frequency_ghz.value Total throughput contribution of this cluster. Keep 4 decimal places (e.g. 9.5478) to preserve precision.
            },
            {
              "core_architecture_score": {
                "identifier": "Cortex-A520",
                // GUIDELINE: Standardized core architecture name matching the record in 6_1_0_system_on_chip_reference.clusters[2].architecture
                "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "CPU Score",
                // GUIDELINE: Description of the column being retrieved.
                "value": 1.00
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              },
              "reference_frequency_ghz": {
                "identifier": "Cortex-A520",
                // GUIDELINE: Standardized core architecture name matching the record in 6_1_0_system_on_chip_reference.clusters[2].architecture
                "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "Ref Freq (GHz)",
                // GUIDELINE: Description of the column being retrieved.
                "value": 2.00
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              },
              "core_count": {
                "value": 2,
                // GUIDELINE: Inherits count from the referenced §6.1.0 cluster.
                "value_path": "6_1_0_system_on_chip_reference.clusters[2].count"
                // GUIDELINE: Absolute path to the core count in Section 6.1.0.
              },
              "actual_frequency_ghz": {
                "value": 2.3,
                "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
                "exact_extract": "2x 2.3 GHz"
                // GUIDELINE: The maximum advertised frequency for this specific core cluster in GHz.
              },
              "frequency_adjusted_core_score": 2.3000,
                // GUIDELINE: core_architecture_score.value * core_count.value * actual_frequency_ghz.value / reference_frequency_ghz.value Total throughput contribution of this cluster. Keep 4 decimal places (e.g. 9.5478) to preserve precision.
            }
          ],
          "raw_performance_throughput_score": 38.8714,
          // GUIDELINE: raw_performance_throughput_score = Sum of all frequency_adjusted_core_score values in the clusters array above. Keep 4 decimal places (e.g. 9.5478) to preserve precision. 
          "predicted_score": 7.40
          // SCORING GUIDELINE: predicted_score = 10 * (log(raw_performance_throughput_score) − log(CPU_PTS_Score_Min)) / (log(CPU_PTS_Score_Max) − log(CPU_PTS_Score_Min)), clamped 0–10. This is the score used for Method B neighbors.
        },
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_CPU_multi": {
          // SCORING GUIDELINE: Method B is populated for ALL phones (even if Method A is available) for precision validation. Search space: all phones with a known Geekbench 6 Multi-Core score (Method A), excluding the target device itself. The interpolation MUST use exactly 3 distinct neighbor devices.
          // Step 1 (Neighbor Selection): Find the 3 distinct devices with the smallest absolute difference in Predicted Score from Method C (|Predicted_Target − Predicted_Neighbor|), excluding the target device itself.
          // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
          "neighbors": [
            {
              // Neighbor1
              "device_id_1": "xiaomi_14_ultra",
              // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
              "predicted_score_1": 7.40,
              // GUIDELINE: The neighbor's own Method C predicted score (overall Multi-Core).
              "benchmark_score_1": 8.60
              // GUIDELINE: The neighbor's Method A subscore.
            },
            {
              // Neighbor2
              "device_id_2": "oneplus_12",
              "predicted_score_2": 7.38,
              "benchmark_score_2": 8.55
            },
            {
              // Neighbor3
              "device_id_3": "asus_rog_phone_8_pro",
              "predicted_score_3": 7.42,
              "benchmark_score_3": 8.65
            }
          ],
          "avg_predicted_neighbors": 7.4000,
          // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
          "avg_benchmark_neighbors": 8.6000,
          // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
          "correction_ratio": 1.0000,
          // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_CPU_multi.predicted_score / avg_predicted_neighbors.
          "interpolated_score": 8.60
          // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
        },

        "scores": {
          "predicted": 7.40,
          // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_CPU_multi.predicted_score.
          "final": {
            "value": 8.63,
            // SCORING GUIDELINE: Use Method A if method_a_benchmark_CPU_multi is available (method_a_benchmark_CPU_multi.subscore becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_CPU_multi.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_CPU_multi.predicted_score).
            "method_used": "Benchmark (Geekbench 6)",
            // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
            //   • Benchmark (Geekbench 6) → Method A (documented Geekbench 6 score)
            //   • Neighbor Interpolation  → Method B (similar device benchmarks)
            //   • Predictor               → Method C (spec calculation)
            "booster": "No",
            // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
            "confidence": "N/A"
            // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
          }
        }
      },
      "6_2_cpu_architecture_single_core": {
        // SCORING GOAL: Evaluates individual core capability and IPC efficiency(Instructions Per Cycle—a measure of how many tasks a CPU can perform in every clock tick), representing the snappiness of the interface and single-threaded application speed.
        
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Direct Benchmark (Primary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_CPU_single": {
          "value": 2200,
          "source": "https://browser.geekbench.com/android-benchmarks",
          "exact_extract": "Samsung Galaxy S24 Ultra [...] 2200",
          "subscore": 8.53
          // SCORING GUIDELINE: primary benchmark is Geekbench 6 Single-Core.
          // • WHERE TO FIND IT: Query browser.geekbench.com for the host SoC or exact device model.
          // • EXTRACTION RULE: Use the "Single-Core Score" from the "Android" or "iOS" category. Verify version is 6.x. Do NOT use v4/v5 or Multi-Core scores.
          // SCORING GUIDELINE: subscore = 10 * (log(method_a_benchmark_CPU_single.value) − log(CPU_GB6_Single_Score_Min)) / (log(CPU_GB6_Single_Score_Max) − log(CPU_GB6_Single_Score_Min)), clamped 0–10. If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Single-Thread Efficiency Prediction Model (Tertiary / baseline for Method B)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_CPU_single": {
          // GUIDELINE: Evaluation focuses on the strongest core in the SoC (System on Chip) (typically the Prime core, i.e. clusters[0]).
          "strongest_core": {
            "core_architecture_score": {
              "identifier": "Cortex-X4",
              // GUIDELINE: Standardized core architecture name of the **STRONGEST** core which should be matching the record in 6_1_0_system_on_chip_reference.clusters[0].architecture
              "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "CPU Score",
              // GUIDELINE: Description of the column being retrieved.
              "value": 8.00
              // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
            },
            "reference_frequency_ghz": {
              "identifier": "Cortex-X4",
              // GUIDELINE: Standardized core architecture name of the **STRONGEST** core which should be matching the record in 6_1_0_system_on_chip_reference.clusters[0].architecture
              "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Ref Freq (GHz)",
              // GUIDELINE: Description of the column being retrieved.
              "value": 3.30
              // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
            },
            "actual_frequency_ghz": {
              "value": 3.3,
              // GUIDELINE: Inherits frequency from the strongest core cluster in §6.1.
              "value_path": "6_1_cpu_multi_core_performance.method_c_prediction_model_CPU_multi.clusters[0].actual_frequency_ghz.value"
              // GUIDELINE: Absolute path to the actual clock frequency of the strongest core.
            },
            "frequency_adjusted_core_score": 8.0000,
              // GUIDELINE: core_architecture_score.value * actual_frequency_ghz.value / reference_frequency_ghz.value. Adjusted performance baseline of this cluster. Keep 4 decimal places (e.g. 9.5478) to preserve precision.
          },
          "predicted_score": 9.31
          // SCORING GUIDELINE: predicted_score = 10 * (log(strongest_core.frequency_adjusted_core_score) − log(CPU_STRS_Score_Min)) / (log(CPU_STRS_Score_Max) − log(CPU_STRS_Score_Min)), clamped 0–10. This is the score used for Method B neighbors.
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_CPU_single": {
          // SCORING GUIDELINE: Method B is populated for ALL phones (even if Method A is available) for precision validation. Search space: all phones with a known Geekbench 6 Single-Core score (Method A), excluding the target device itself. The interpolation MUST use exactly 3 distinct neighbor devices.
          // Step 1: Find the 3 distinct devices with the smallest absolute difference in Predicted Score from Method C (|Predicted_Target − Predicted_Neighbor|), excluding the target device itself.
          // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
          "neighbors": [
            {
              // Neighbor1
              "device_id_1": "xiaomi_14_ultra",
              // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
              "predicted_score_1": 9.31,
              // GUIDELINE: The neighbor's own Method C predicted score (overall Single-Core).
              "benchmark_score_1": 8.49
              // GUIDELINE: The neighbor's Method A subscore.
            },
            {
              // Neighbor2
              "device_id_2": "oneplus_12",
              "predicted_score_2": 9.29,
              "benchmark_score_2": 8.45
            },
            {
              // Neighbor3
              "device_id_3": "asus_rog_phone_8_pro",
              "predicted_score_3": 9.33,
              "benchmark_score_3": 8.57
            }
          ],
          "avg_predicted_neighbors": 9.3100,
          // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
          "avg_benchmark_neighbors": 8.5033,
          // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
          "correction_ratio": 1.0000,
          // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_CPU_single.predicted_score / avg_predicted_neighbors.
          "interpolated_score": 8.50
          // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
        },
        "scores": {
          "predicted": 9.31,
          // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_CPU_single.predicted_score.
          "final": {
            "value": 8.53,
            // SCORING GUIDELINE: Use Method A if method_a_benchmark_CPU_single is available (method_a_benchmark_CPU_single.subscore becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_CPU_single.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_CPU_single.predicted_score).
            "method_used": "Benchmark (Geekbench 6)",
            // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
            //   • Benchmark (Geekbench 6) → Method A (documented Geekbench 6 score)
            //   • Neighbor Interpolation  → Method B (similar device benchmarks)
            //   • Predictor               → Method C (spec calculation)
            "booster": "No",
            // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
            "confidence": "N/A"
            // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
          }
        }
      },
      // █ GPU_ARCHITECTURE_LOOKUP_TABLE
      // Centralized hardware index used to ensure 100% autonomous scoring across performance (§6.3) and efficiency (§8.1) modules.
      // • Standard Graphics Score (SGS): The baseline architectural performance capacity for standard rasterization (non-RT) tasks.
      // • Ray Tracing Score (RTS): The specialized hardware performance index for accelerated ray tracing calculations.
      // • Ref Freq (MHz): The canonical maximum frequency used to calculate frequency-corrected performance multipliers in Method C.
      // • Efficiency: The silicon-level power/thermal management index used exclusively for Section 8.1 benchmarking to derive normalized efficiency scores.
      // 
      // | GPU Model                  | Standard Graphics | Ray Tracing | Ref Freq (MHz) | Efficiency |
      // | :------------------------- | :---------------: | :---------: | :------------: | :--------: |
      // | Adreno 830                 |      10.00        |    10.00    |      1100      |    10.00   |
      // | Immortalis-G925 MC12       |      10.00        |    10.00    |      1626      |    10.00   |
      // | Immortalis-G720 MC12       |      10.00        |    10.00    |      1300      |    10.00   |
      // | Adreno 750                 |      10.00        |    10.00    |       903      |     9.00   |
      // | Apple GPU (A18 Pro)        |       9.00        |     9.00    |      1398      |    10.00   |
      // | Apple GPU (A18)            |       9.00        |     8.00    |      1398      |    10.00   |
      // | Immortalis-G715 MC11       |       9.00        |     8.00    |       981      |     9.00   |
      // | Xclipse 940                |       9.00        |     8.00    |      1100      |     7.00   |
      // | Adreno 740                 |       9.00        |     8.00    |       680      |     9.00   |
      // | Apple GPU (A17 Pro)        |       8.00        |     7.00    |      1398      |     9.00   |
      // | Adreno 735                 |       8.00        |     6.00    |       950      |     8.00   |
      // | Adreno 732                 |       8.00        |     6.00    |       900      |     8.00   |
      // | Adreno 730                 |       8.00        |     6.00    |       900      |     7.00   |
      // | Adreno 725                 |       8.00        |     5.00    |       580      |     9.00   |
      // | Mali-G715 MC9              |       8.00        |     6.00    |       850      |     9.00   |
      // | Apple GPU (A16 Bionic)     |       7.00        |     4.00    |      1398      |     8.00   |
      // | Xclipse 920                |       7.00        |     5.00    |      1300      |     6.00   |
      // | Mali-G710 MC10             |       7.00        |     5.00    |       850      |     8.00   |
      // | Adreno 660                 |       7.00        |     0.00    |       840      |     5.00   |
      // | Mali-G715 MC7              |       7.00        |     5.00    |       850      |     9.00   |
      // | Mali-G715 (Tensor G3)      |       7.00        |     4.00    |       890      |     6.00   |
      // | Apple GPU (A15 Bionic)     |       6.00        |     0.00    |      1296      |     8.00   |
      // | Adreno 720                 |       6.00        |     0.00    |       800      |     8.00   |
      // | Adreno 710                 |       6.00        |     0.00    |       800      |     8.00   |
      // | Adreno 650                 |       6.00        |     0.00    |       587      |     6.00   |
      // | Adreno 642L                |       6.00        |     0.00    |       490      |     8.00   |
      // | Mali-G610 MC6              |       6.00        |     0.00    |       850      |     8.00   |
      // | Mali-G77 MC9               |       6.00        |     0.00    |       850      |     6.00   |
      // | Apple GPU (A14 Bionic)     |       5.00        |     0.00    |      1086      |     7.00   |
      // | Apple GPU (A13 Bionic)     |       5.00        |     0.00    |       979      |     6.00   |
      // | Adreno 640                 |       5.00        |     0.00    |       585      |     5.00   |
      // | Mali-G610 MC4              |       5.00        |     0.00    |       850      |     7.00   |
      // | Adreno 620                 |       4.00        |     0.00    |       625      |     6.00   |
      // | Adreno 619                 |       4.00        |     0.00    |       825      |     6.00   |
      // | Mali-G68 MC4               |       4.00        |     0.00    |       900      |     6.00   |
      // | Adreno 618                 |       3.00        |     0.00    |       610      |     5.00   |
      // | Mali-G57 MC3               |       3.00        |     0.00    |       950      |     5.00   |
      // | Adreno 613                 |       3.00        |     0.00    |       955      |     6.00   |
      // | Adreno 610                 |       2.00        |     0.00    |       600      |     8.00   |
      // | Mali-G57 MC2               |       2.00        |     0.00    |       950      |     5.00   |
      // | Mali-G52 MP2               |       1.00        |     0.00    |       850      |     4.00   |
      // | PowerVR GE8320             |       0.00        |     0.00    |       680      |     2.00   |
      // -------------------------------------------------------------------------
      // Understanding Mali/Immortalis "MC" Notation:
      // ARM Mali and Immortalis GPUs use Multi-Core (MC) configurations. The number after "MC" indicates the shader core count.
      // - Immortalis-G715 MC11 = 11 shader cores (flagship config)
      // - Mali-G715 MC9 = 9 shader cores (high-end config)
      // - Mali-G715 MC7 = 7 shader cores (mid-range config)
      // More cores = higher performance. Always match the exact MC count from device specifications.
      // -------------------------------------------------------------------------
      // AMBIGUOUS SPECIFICATION RESOLUTION (MANDATORY PROCEDURE)
      // 1. Identify the SoC: Retrieve the specific chipset model from identity.hardware_configuration.chipset.value
      // 2. External Verification (Web Search): The parsing engine is strictly prohibited from guessing the GPU tier based on incomplete generic strings. The engine MUST execute an active web search targeting the host SoC's official specifications (e.g., query: "Qualcomm Snapdragon 680 GPU specs" or "Dimensity 9000 exact GPU model").
      // 3. Canonical Component Extraction: Extract the exact GPU model number from the search results.
      // 4. Final Mapping: Map this newly verified, precise component directly to its corresponding row in the Scoring Table above.
      
      "6_3_0_graphics_processing_unit_architecture_reference": {
        "value": "Snapdragon 8 Gen 3",
        // GUIDELINE: Inherits the chipset model name from the device identity record to link with GPU architecture.
        "value_path": "identity.hardware_configuration.chipset.value",
        // GUIDELINE: Absolute path to the chipset identifier in the device identity section.
        "graphics_processing_unit_model": {
          "value": "Adreno 750",
          // GUIDELINE: Must match a specific model from the GPU_ARCHITECTURE_LOOKUP_TABLE above. If the spec sheet assigns a generic family name without identifiers (e.g., "Adreno GPU"), the engine MUST execute the "AMBIGUOUS SPECIFICATION RESOLUTION" procedure above to infer the canonical GPU architecture.
          "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
          // GUIDELINE: Direct source URL for GPU model data.
          "exact_extract": "Qualcomm® Adreno™ GPU"
          // GUIDELINE: The verbatim proof from the source confirming the GPU identifier.
        }
      },
      "6_3_graphics_processing_unit_performance": {
        // SCORING GOAL: Scores raw GPU compute capability using standard graphics tasks and hardware ray tracing.
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Direct Benchmark (Primary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_GPU": {
          "value": 1850,
          "source": "https://www.3dmark.com/search",
          "exact_extract": "Samsung Galaxy S24 Ultra [...] 1850",
          "subscore": 8.36
          // SCORING GUIDELINE: primary benchmark is 3DMark Steel Nomad Light.
          // • WHERE TO FIND IT: Search 3dmark.com search index or GSMArena/NotebookCheck reviews.
          // • EXTRACTION RULE: Use the "Steel Nomad Light" score. Ensure it is not the desktop "Steel Nomad" or older "Wild Life" benchmarks.
          // SCORING GUIDELINE: subscore = 10 * (log(method_a_benchmark_GPU.value) − log(GPU_SteelNomad_Score_Min)) / (log(GPU_SteelNomad_Score_Max) − log(GPU_SteelNomad_Score_Min)), clamped 0–10. If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Graphics Performance Prediction Model (Tertiary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_GPU": {
          "graphics_processing_unit": {
            "graphics_architecture_score": {
              "identifier": "Adreno 750",
              // GUIDELINE: Standardized GPU model name matching the record in 6_3_0_graphics_processing_unit_architecture_reference.graphics_processing_unit_model.value
              "reference_table": "GPU_ARCHITECTURE_LOOKUP_TABLE",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Standard Graphics",
              // GUIDELINE: Description of the column being retrieved.
              "value": 10.00
              // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
            },
            "reference_frequency_mhz": {
              "identifier": "Adreno 750",
              // GUIDELINE: Standardized GPU model name matching the record in 6_3_0_graphics_processing_unit_architecture_reference.graphics_processing_unit_model.value
              "reference_table": "GPU_ARCHITECTURE_LOOKUP_TABLE",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Ref Freq (MHz)",
              // GUIDELINE: Description of the column being retrieved.
              "value": 903.00
              // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
            },
            "actual_frequency_mhz": {
              "value": 1100,
              "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
              "exact_extract": "Qualcomm® Adreno™ GPU [...] 1.1 GHz"
              // GUIDELINE: The maximum advertised frequency of the GPU in MHz (e.g., 1100).
            },
          },
          "api_modifier": {
            "value": "Vulkan 1.3",
            // GUIDELINE: Standardized API version supported by the GPU as found in technical specifications.
            "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2667.php",
            "exact_extract": "Vulkan 1.3 support",          
            "api_support_score": {
              // █ GPU_API_SUPPORT_LOOKUP_TABLE
              // Defines the scoring for the highest supported graphics API (Vulkan/Metal/OpenGL ES/DirectX).
              //
              // | Vulkan (Android)  | Metal (iOS)    | OpenGL ES (Leg)    | DirectX (Win Mob)       | Score     |
              // | :---------------- | :------------- | :----------------- | :---------------------- | :-------: |
              // | Vulkan 1.4        | Metal 4.0      | —                  | D3D 12 (FL 12_2)        | 10.0      |
              // | —                 | Metal 3.3      | —                  | —                       | 9.8       |
              // | —                 | Metal 3.2      | —                  | D3D 12 (FL 12_1)        | 9.6       |
              // | —                 | Metal 3.1      | —                  | —                       | 9.4       |
              // | Vulkan 1.3        | Metal 3.0      | —                  | D3D 12 (FL 12_0)        | 9.2       |
              // | —                 | Metal 2.4      | —                  | D3D 11.2                | 8.5       |
              // | Vulkan 1.2        | Metal 2.3      | —                  | D3D 11.1                | 8.0       |
              // | —                 | Metal 2.2      | —                  | —                       | 7.5       |
              // | —                 | Metal 2.1      | —                  | —                       | 7.0       |
              // | Vulkan 1.1        | Metal 2.0      | —                  | D3D 11.0                | 6.5       |
              // | Vulkan 1.0        | —              | —                  | D3D 10.1                | 6.0       |
              // | —                 | —              | OpenGL ES 3.2      | D3D 10.0                | 5.0       |
              // | —                 | Metal 1.2      | —                  | —                       | 4.5       |
              // | —                 | Metal 1.1      | —                  | —                       | 4.2       |
              // | —                 | Metal 1.0      | —                  | D3D 9.3                 | 4.0       |
              // | —                 | —              | —                  | D3D 9.2                 | 3.5       |
              // | —                 | —              | OpenGL ES 3.1      | —                       | 3.0       |
              // | —                 | —              | —                  | D3D 9.1                 | 2.5       |
              // | —                 | —              | —                  | D3D 9.0c                | 2.0       |
              // | —                 | —              | —                  | —                       | 1.5       |
              // | —                 | —              | OpenGL ES 3.0      | —                       | 1.0       |
              // | —                 | —              | OpenGL ES 2.0      | —                       | 0.5       |
              // | —                 | —              | OpenGL ES 1.x      | —                       | 0.0       |
              //
              // AMBIGUOUS API RESOLUTION (MANDATORY FALLBACK CENSUS)
              // If the explicit API version is NOT disclosed on the primary spec sheet, the agent MUST resolve the score using the following exhaustive OS/Architecture fallback matrices.
              //
              // MATRIX 1: APPLE / iOS (Deep Coverage Mirror)
              // | Apple SoC Generation | Min iOS Version | Inferred API Version |
              // | :------------------- | :-------------- | :------------------- |
              // | A18, M4, M5          | iOS 18+         | Metal 4.0            | 
              // | A17 Pro, M3          | iOS 17.5+       | Metal 3.3            |
              // | A15, A16, M2         | iOS 17.0+       | Metal 3.2            | 
              // | A14, M1              | iOS 16.4+       | Metal 3.1            |
              // | A13 (Apple Family 6) | iOS 16.0+       | Metal 3.0            |
              // | A12 Bionic           | iOS 15.x        | Metal 2.4            |
              // | A11 Bionic           | iOS 14.x        | Metal 2.3            |
              // | A10 Fusion           | iOS 13.x        | Metal 2.2            |
              // | A9 / A9X             | iOS 12.x        | Metal 2.1            |
              // | A8 / A8X             | iOS 11.x        | Metal 2.0            | 
              // | A7 (64-bit Baseline) | iOS 10.x        | Metal 1.2            |
              // | A7 (64-bit Baseline) | iOS 9.x         | Metal 1.1            |
              // | A7 (64-bit Baseline) | iOS 8.x         | Metal 1.0            |
              // | A4, A5, A6           | iOS 6.x - 10.x  | OpenGL ES 2.0        |
              // | iPhone 1st Gen / 3G  | iPhone OS 1 - 3 | OpenGL ES 1.1        |
              //
              // MATRIX 2: ANDROID (Deep Coverage Mirror)
              // | Android Launch OS    | GPU Architecture Baseline      | Inferred API  |
              // | :------------------- | :----------------------------- | :------------ |
              // | Android 15+          | Adreno 8xx+, Immortalis G92x+  | Vulkan 1.4    |
              // | Android 13 - 14      | Adreno 7xx, Mali-G71x          | Vulkan 1.3    |
              // | Android 12           | Adreno 66x, Mali-G710          | Vulkan 1.2    |
              // | Android 10 - 11      | Adreno 6xx, Mali-G77/G78       | Vulkan 1.1    |
              // | Android 7.0 - 9.0    | Adreno 5xx, Mali-G71/G72       | Vulkan 1.0    |
              // | Android 6.0          | Adreno 4xx, Mali-T8xx          | OpenGL ES 3.2 |
              // | Android 5.0          | Adreno 3xx (Newer), Mali-T7xx  | OpenGL ES 3.1 |
              // | Android 4.3          | Adreno 3xx (Older), Mali-T6xx  | OpenGL ES 3.0 |
              // | Android 2.0 - 4.2    | Adreno 2xx, Mali-400           | OpenGL ES 2.0 |
              // | Android 1.x          | Adreno 1xx (Adreno 130)        | OpenGL ES 1.x | 
              //
              // MATRIX 3: WINDOWS MOBILE (Deep Coverage Mirror)
              // | Windows OS Version   | Era / Reference Hardware       | Inferred API  |
              // | :------------------- | :----------------------------- | :------------ |
              // | Windows 11 (24H2)    | Snapdragon X Elite (Adreno X1) | D3D 12 (12_2) |
              // | Windows 11 (22H2)    | Snapdragon 8cx Gen 3           | D3D 12 (12_1) |
              // | Windows 10/11 ARM    | Snapdragon 850 / 8cx Gen 1/2   | D3D 12 (12_0) |
              // | Windows 10 Mobile    | Lumia 950 / 950 XL             | D3D 11.2      |
              // | Windows Phone 8.1    | Lumia 930 / 1520               | D3D 11.1      |
              // | Windows Phone 8 GDR  | Snapdragon 800 / 400 (Late WP8)| D3D 11.0      |
              // | Windows Phone 8.0    | Lumia 520 / 620 (Entry Adreno) | D3D 10.1      |
              // | Windows Phone 8.0    | Early Surface RT / Tegra 3     | D3D 10.0      |
              // | Windows Phone 8.0    | Lumia 920 / 1020 (Baseline)    | D3D 9.3       |
              // | Windows Phone 8.0    | Early builds / Dev hardware    | D3D 9.2       |
              // | Windows Phone 7.x    | Lumia 800 / 900                | D3D 9.1       |
              // | Windows Phone 7.0    | Samsung Focus / LG Quantum     | D3D 9.0c      |
              // | Pre-WP7 Legacy       | Pre-2010 HTC / Samsung         | OpenGL ES 1.x |
              // ------------------------------------------------------------------------- 
              "identifier": "Vulkan 1.3",
              // GUIDELINE: Retrieved from "api_modifier.value".
              "reference_table": "GPU_API_SUPPORT_LOOKUP_TABLE",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Score",
              // GUIDELINE: Description of the column being retrieved.
              "value": 9.20
              // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`. If unspecified, execute AMBIGUOUS API RESOLUTION.
            }
          },
          "graphics_raw_score": 11.9380,
          // SCORING GUIDELINE: graphics_raw_score = graphics_processing_unit.graphics_architecture_score.value * graphics_processing_unit.actual_frequency_mhz.value / graphics_processing_unit.reference_frequency_mhz.value * (0.75 + 0.25 * api_modifier.api_support_score.value / 10.0).
          "predicted_score": 9.98
          // SCORING GUIDELINE: predicted_score = 10 * (log(graphics_raw_score) - log(GPU_RC_Score_Min)) / (log(GPU_RC_Score_Max) - log(GPU_RC_Score_Min)), clamped 0–10. This is the score used for Method B neighbors.
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_GPU": {
          // SCORING GUIDELINE: Method B is populated for ALL phones (even if Method A is available) for precision validation. Search space: all phones with a known 3DMark Steel Nomad Light score (Method A), excluding the target device itself. The interpolation MUST use exactly 3 distinct neighbor devices.
          // Step 1: Find the 3 distinct devices with the smallest absolute difference in Predicted Score from Method C (|Predicted_Target − Predicted_Neighbor|), excluding the target device itself.
          // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
          "neighbors": [
            {
              // Neighbor1
              "device_id_1": "xiaomi_14_ultra",
              // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
              "predicted_score_1": 9.40,
              // GUIDELINE: The neighbor's own Method C predicted score.
              "benchmark_score_1": 7.82
              // GUIDELINE: The neighbor's Method A subscore.
            },
            {
              // Neighbor2
              "device_id_2": "samsung_galaxy_s24_ultra",
              "predicted_score_2": 9.71,
              "benchmark_score_2": 8.05
            },
            {
              // Neighbor3
              "device_id_3": "oneplus_12",
              "predicted_score_3": 9.40,
              "benchmark_score_3": 7.88
            }
          ],
          "avg_predicted_neighbors": 9.5033,
          // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
          "avg_benchmark_neighbors": 7.9167,
          // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
          "correction_ratio": 1.0502,
          // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_GPU.predicted_score / avg_predicted_neighbors.
          "interpolated_score": 8.31
          // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // Ray Tracing 
        // ═══════════════════════════════════════════════════════════════════════════
        "ray_tracing_score": {
          // This measures dedicated hardware acceleration for lighting and reflections.
          "identifier": "Adreno 750",
          // GUIDELINE: Standardized GPU model name matching the record in 6_3_0_graphics_processing_unit_architecture_reference.graphics_processing_unit_model.value
          "reference_table": "GPU_ARCHITECTURE_LOOKUP_TABLE",
          // GUIDELINE: Path to the authoritative lookup table for mapping.
          "lookup_parameter": "Ray Tracing",
          // GUIDELINE: Description of the column being retrieved.
          "value": 10.00
          // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
        },
        
        "scores": {
          "predicted": 9.98,
          // SCORING GUIDELINE: Final weighted predicted score including ray tracing. Formula: (method_c_prediction_model_GPU.predicted_score * 0.90) + (ray_tracing_score.value * 0.10).
          "final": {
            "value": 8.52,
            // SCORING GUIDELINE: Final Score combines rasterization (via Standard Graphics Score) and ray tracing capability according to the A→B→C hierarchy. Formula: (Standard Graphics Score * 0.90) + (ray_tracing_score.value * 0.10). Standard Graphics Score is derived from Method A (method_a_benchmark_GPU.subscore) if available; if not, Method B (method_b_neighbor_interpolation_GPU.interpolated_score); if not, Method C (method_c_prediction_model_GPU.predicted_score).
            "method_used": "Benchmark (3DMark)",
            // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
            //   • Benchmark (3DMark)     → Method A (documented 3DMark score)
            //   • Neighbor Interpolation → Method B (similar device benchmarks)
            //   • Predictor              → Method C (weighted spec calculation)
            "booster": "No",
            // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
            "confidence": "N/A"
            // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
          }
        }
      },
      // █ SOC_NEURAL_PROCESSING_UNIT_(NPU)_/_AI_ACCELERATOR_LOOKUP_TABLE
      //
      // TOPS values prefixed with ~ are estimates from vendor relative claims and family cross-referencing.
      //
      // |  # | SoC Model                  | NPU / AI Engine               | TOPS(INT8) | TOPS Norm | Arch Gen         | Precision     | NPU Score |
      // |:--:|:---------------------------|:------------------------------|:----------:|:---------:|:-----------------|:-------------:|:---------:|
      // |  1 | Snapdragon 8 Elite         | Hexagon (Oryon NPU)           |      45    |   9.77    | Gen AI Native    | INT4+8+FP16   |   9.88    |
      // |  2 | Dimensity 9400             | APU 890                       |     ~40    |   9.52    | Gen AI Native    | INT4+8+FP16   |   9.76    |
      // |  3 | Apple A18                  | 16-Core Neural Engine         |      35    |   9.23    | Gen AI Native    | INT4+8+FP16   |   9.62    |
      // |  4 | Apple A18 Pro              | 16-Core Neural Engine         |      35    |   9.23    | Gen AI Native    | INT4+8+FP16   |   9.62    |
      // |  5 | Snapdragon 8 Gen 3         | Hexagon (2024)                |      45    |   9.77    | Gen AI Capable   | INT4+8+FP16   |   9.28    |
      // |  6 | Apple A17 Pro              | 16-Core Neural Engine         |      35    |   9.23    | Gen AI Capable   | INT4+8+FP16   |   9.01    |
      // |  7 | Exynos 2400                | NPU 5th-gen                   |    34.7    |   9.21    | Gen AI Capable   | INT4+8+FP16   |   9.00    |
      // |  8 | Dimensity 9300             | APU 790                       |     ~30    |   8.89    | Gen AI Capable   | INT4+8+FP16   |   8.84    |
      // |  9 | Snapdragon 8 Gen 2         | Hexagon (2023)                |      26    |   8.58    | Gen AI Capable   | INT4+8+FP16   |   8.69    |
      // | 10 | Snapdragon 8 Gen 1         | Hexagon (2022)                |      27    |   8.66    | ML Optimized     | INT8+FP16     |   7.53    |
      // | 11 | Snapdragon 888             | Hexagon 780                   |      26    |   8.58    | ML Accelerated   | INT8+FP16     |   6.89    |
      // | 12 | Snapdragon 888+            | Hexagon 780 (OC)              |      26    |   8.58    | ML Accelerated   | INT8+FP16     |   6.89    |
      // | 13 | Dimensity 9200             | APU 690                       |     ~18    |   7.78    | ML Optimized     | INT8+FP16     |   7.09    |
      // | 14 | Apple A16 Bionic           | 16-Core Neural Engine         |      17    |   7.66    | ML Optimized     | INT8+FP16     |   7.03    |
      // | 15 | Apple A15 Bionic           | 16-Core Neural Engine         |    15.8    |   7.50    | ML Optimized     | INT8+FP16     |   6.95    |
      // | 16 | Exynos 1480                | NPU (6K MAC)                  |     ~20    |   8.01    | ML Accelerated   | INT8+FP16     |   6.61    |
      // | 17 | Snapdragon 7+ Gen 2        | Hexagon (Mid 2023)            |     ~13    |   7.07    | ML Optimized     | INT8+FP16     |   6.74    |
      // | 18 | Kirin 9010                 | Da Vinci (Refined)            |     ~12    |   6.90    | ML Optimized     | INT8+FP16     |   6.65    |
      // | 19 | Tensor G4                  | Google TPU (2024)             |     ~12    |   6.90    | ML Optimized     | INT8+FP16     |   6.65    |
      // | 20 | Exynos 990                 | Dual-core NPU                 |     ~15    |   7.39    | ML Accelerated   | INT8+FP16     |   6.29    |
      // | 21 | Snapdragon 865             | Hexagon 698                   |      15    |   7.39    | ML Accelerated   | INT8+FP16     |   6.29    |
      // | 22 | Snapdragon 870             | Hexagon 698                   |      15    |   7.39    | ML Accelerated   | INT8+FP16     |   6.29    |
      // | 23 | Kirin 9000                 | Da Vinci 2.0 (2+1 core)       |     ~10    |   6.51    | ML Optimized     | INT8+FP16     |   6.46    |
      // | 24 | Tensor G3                  | Google TPU (2023)             |     ~10    |   6.51    | ML Optimized     | INT8+FP16     |   6.46    |
      // | 25 | Dimensity 9000             | APU 590                       |     ~12    |   6.90    | ML Accelerated   | INT8+FP16     |   6.05    |
      // | 26 | Snapdragon 778G / 778G+    | Hexagon 770                   |      12    |   6.90    | ML Accelerated   | INT8+FP16     |   6.05    |
      // | 27 | Snapdragon 780G            | Hexagon 770                   |      12    |   6.90    | ML Accelerated   | INT8+FP16     |   6.05    |
      // | 28 | Apple A14 Bionic           | 16-Core Neural Engine         |      11    |   6.71    | ML Accelerated   | INT8+FP16     |   5.96    |
      // | 29 | Exynos 2200                | Xclipse NPU                   |     ~10    |   6.51    | ML Accelerated   | INT8+FP16     |   5.86    |
      // | 30 | Snapdragon 7 Gen 3         | Hexagon (Mid 2024)            |     ~10    |   6.51    | ML Accelerated   | INT8+FP16     |   5.86    |
      // | 31 | Snapdragon 7 Gen 1         | Hexagon (Mid 2022)            |      ~9    |   6.28    | ML Accelerated   | INT8+FP16     |   5.74    |
      // | 32 | Kirin 990 5G               | Da Vinci 1.0 (2+1 core)       |      ~8    |   6.02    | ML Accelerated   | INT8+FP16     |   5.61    |
      // | 33 | Tensor G2                  | Google TPU (2022)             |      ~8    |   6.02    | ML Accelerated   | INT8+FP16     |   5.61    |
      // | 34 | Unisoc T820                | Dedicated NPU                 |       8    |   6.02    | ML Accelerated   | INT8+FP16     |   5.61    |
      // | 35 | Apple A13 Bionic           | 8-Core Neural Engine          |      ~6    |   5.40    | ML Accelerated   | INT8+FP16     |   5.30    |
      // | 36 | Dimensity 8200             | APU 580                       |      ~6    |   5.40    | ML Accelerated   | INT8+FP16     |   5.30    |
      // | 37 | Dimensity 8100             | APU 580                       |    ~5.5    |   5.21    | ML Accelerated   | INT8+FP16     |   5.21    |
      // | 38 | Dimensity 7300             | APU 650+                      |      ~5    |   5.00    | ML Accelerated   | INT8+FP16     |   5.10    |
      // | 39 | Dimensity 8000             | APU 580                       |      ~5    |   5.00    | ML Accelerated   | INT8+FP16     |   5.10    |
      // | 40 | Tensor G1                  | Google TPU (2021)             |      ~5    |   5.00    | ML Accelerated   | INT8+FP16     |   5.10    |
      // | 41 | Apple A12 Bionic           | 8-Core Neural Engine          |       5    |   5.00    | ML Accelerated   | INT8 only     |   4.50    |
      // | 42 | Exynos 1380                | NPU                           |     4.9    |   4.96    | ML Accelerated   | INT8 only     |   4.48    |
      // | 43 | Dimensity 1300             | APU 3.0 (6-core OC)           |    ~4.5    |   4.77    | ML Accelerated   | INT8 only     |   4.38    |
      // | 44 | Exynos 1280                | NPU                           |     4.3    |   4.67    | ML Accelerated   | INT8 only     |   4.33    |
      // | 45 | Dimensity 1200             | APU 3.0 (6-core)              |      ~4    |   4.52    | ML Accelerated   | INT8 only     |   4.26    |
      // | 46 | Dimensity 7200             | APU 650                       |      ~4    |   4.52    | ML Accelerated   | INT8 only     |   4.26    |
      // | 47 | Kirin 980                  | Cambricon (Dual-NPU)          |      ~4    |   4.52    | ML Accelerated   | INT8 only     |   4.26    |
      // | 48 | Snapdragon 6 Gen 3         | Hexagon (Mid-tier)            |      ~4    |   4.52    | ML Accelerated   | INT8 only     |   4.26    |
      // | 49 | Unisoc T770                | Imagination NNA               |      ~4    |   4.52    | ML Accelerated   | INT8 only     |   4.26    |
      // | 50 | Dimensity 7050             | APU 650                       |    ~3.5    |   4.23    | ML Accelerated   | INT8 only     |   4.12    |
      // | 51 | Snapdragon 680             | Hexagon 686                   |     3.3    |   4.10    | DSP/HVX          | INT8 only     |   3.45    |
      // | 52 | Snapdragon 695             | Hexagon 686                   |     3.3    |   4.10    | DSP/HVX          | INT8 only     |   3.45    |
      // | 53 | Unisoc T760                | Dedicated NPU                 |     3.2    |   4.03    | DSP/HVX          | INT8 only     |   3.42    |
      // | 54 | Snapdragon 480             | Hexagon 686                   |      ~3    |   3.89    | DSP/HVX          | INT8 only     |   3.34    |
      // | 55 | Snapdragon 6 Gen 1         | Hexagon (Mid-tier)            |      ~3    |   3.89    | DSP/HVX          | INT8 only     |   3.34    |
      // | 56 | Snapdragon 662             | Hexagon 686                   |      ~3    |   3.89    | DSP/HVX          | INT8 only     |   3.34    |
      // | 57 | Snapdragon 685             | Hexagon 686                   |      ~3    |   3.89    | DSP/HVX          | INT8 only     |   3.34    |
      // | 58 | Kirin 970                  | Cambricon (Single-NPU)        |      ~2    |   3.01    | ML Accelerated   | INT8 only     |   3.50    |
      // | 59 | Dimensity 6100+            | APU (Budget)                  |      ~2    |   3.01    | DSP/HVX          | INT8 only     |   2.91    |
      // | 60 | Snapdragon 4 Gen 2         | Hexagon (Budget)              |      ~2    |   3.01    | DSP/HVX          | INT8 only     |   2.91    |
      // | 61 | Snapdragon 4 Gen 1         | Hexagon (Budget)              |    ~1.5    |   2.39    | DSP/HVX          | INT8 only     |   2.59    |
      // | 62 | Snapdragon 4s Gen 2        | Hexagon (Budget)              |    ~1.5    |   2.39    | DSP/HVX          | INT8 only     |   2.59    |
      // | 63 | Exynos 850                 | Minimal NPU                   |      ~1    |   1.51    | DSP/HVX          | INT8 only     |   2.16    |
      // | 64 | Helio G99                  | APU 2.0                       |      ~1    |   1.51    | DSP/HVX          | INT8 only     |   2.16    |
      // | 65 | Helio G96                  | APU 2.0                       |    ~0.8    |   1.02    | DSP/HVX          | INT8 only     |   1.91    |
      // | 66 | Apple A11 Bionic           | 2-Core Neural Engine          |     0.6    |   0.40    | ML Accelerated   | INT8 only     |   2.20    |
      // | 67 | Helio G95                  | APU 2.0                       |    ~0.7    |   0.73    | DSP/HVX          | INT8 only     |   1.77    |
      // | 68 | Helio G85 / G88            | CPU-only emulation            |    <0.5    |   0.00    | CPU-Only         | None          |   0.00    |
      // | 69 | Unisoc T616 / T612 / T606  | CPU-only emulation            |    <0.5    |   0.00    | CPU-Only         | None          |   0.00    |
      // -------------------------------------------------------------------------
      
      "6_4_ai_hardware_performance": {
        // SCORING GOAL: Evaluates the AI hardware acceleration capability.
        // AI_System_Score: Method A → B → C hierarchy.
        
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Direct Benchmark (Primary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_AI": {
          "value": 35000,
          "source": "https://browser.geekbench.com/ai-benchmarks",
          "exact_extract": "Samsung Galaxy S24 Ultra [...] 35000",
          "subscore": 8.34
          // SCORING GUIDELINE: primary benchmark is Geekbench AI (v1.x).
          // • WHERE TO FIND IT: browser.geekbench.com/ai.
          // • EXTRACTION RULE: Use the "Quantized Score (INT8)". Do NOT use "Half-Precision" or "Single-Precision" scores. Confirm version 1.x.
          // SCORING GUIDELINE: subscore = 10 * (log(method_a_benchmark_AI.value) - log(AI_GB_Quant_Score_Min)) / (log(AI_GB_Quant_Score_Max) - log(AI_GB_Quant_Score_Min)), clamped 0-10. This subscore is the "AI System Score" for Method A. If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Static Component Prediction Model (Tertiary / baseline for Method B)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_AI": {
          "npu_score": {
            "identifier": "Snapdragon 8 Gen 3",
            // GUIDELINE: Standardized SoC identifier matching the record in identity.hardware_configuration.chipset.value
            "reference_table": "SOC_NEURAL_PROCESSING_UNIT_(NPU)_/_AI_ACCELERATOR_LOOKUP_TABLE",
            // GUIDELINE: Path to the authoritative lookup table for mapping.
            "lookup_parameter": "NPU Score",
            // GUIDELINE: Description of the column being retrieved.
            "value": 9.28
            // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`
          },
          "software_stack": {
            "value": "Tier 2: SDK Co-Optimized",
            "value_details": {
              "Tier 1: Native Synergistic": [],
              "Tier 2: SDK Co-Optimized": [
                {
                  "name": "Qualcomm Neural Network (QNN) SDK",
                  "source": "https://www.qualcomm.com/products/technology/processors/snapdragon-8-gen-3",
                  "exact_extract": "Qualcomm Neural Network (QNN) SDK [...] Optimized NPU delegation"
                }
              ],
              "Tier 3: Hardware Accelerated / Optimized Fallback": [],
              "Tier 4: CPU/GPU Fallback": [],
              "Tier 5: Minimal / None": []
            },
            "subscore": 8.00
            // SCORING GUIDELINE: **AI Software Stack Scoring Guideline:**
            //
            // Classify the device's AI software stack strictly via deterministic boolean architecture cutoffs. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
            //
            //  • "Tier 1: Native Synergistic"                        → 10.00
            //     *   *Definition:* The device manufacturer natively designs the OS framework strictly for their own silicon compiler. This guarantees exclusive high-speed pipelines bypassing generic API translation layers (e.g., **Apple Core ML**, **Google Android AICore + Edge TPU**, **Huawei MindSpore**).
            //     *   *Agent Validation Rule (Concrete boolean check):*
            //         *   `IF (SoC_Family == "Google Tensor")` → Score 10.0.
            //         *   `IF (Device_Brand == "Apple" AND SoC_Model >= "Apple A11")` → Score 10.0.
            //         *   `IF (OS == "HarmonyOS" AND SoC_Manufacturer == "HiSilicon" AND NPU == True)` → Score 10.0.
            //
            //  • "Tier 2: SDK Co-Optimized"                          → 8.00
            //     *   *Definition:* The device uses a modern 3rd-party SoC supported by a robust, vendor-specific optimization SDK that bridges the OS and hardware (e.g., **Qualcomm QNN**, **MediaTek NeuroPilot**, **Samsung ENN**).
            //     *   *Agent Validation Rule (Concrete boolean check):*
            //         *   `IF (SoC_Manufacturer IN ["Qualcomm", "MediaTek", "Samsung", "HiSilicon"]) AND (NPU == True)` → Score 8.0.
            //         *   `IF (Device Specs contain custom Co-processor ("MariSilicon", "Vivo V-series", "Xiaomi Surge"))` → Score 8.0.
            //
            //  • "Tier 3: Hardware Accelerated / Optimized Fallback" → 5.50
            //     *   *Definition:* The device lacks a modern dedicated NPU but features an OS-level API highly optimized for bare-metal GPU acceleration or standard fixed-function blocks (e.g., **Apple Metal Performance Shaders (MPS)**, **Qualcomm SNPE**).
            //     *   *Agent Validation Rule (Concrete boolean check):*
            //         *   `IF (NPU == True) AND NOT (Rule_Match == Tier 1 OR Rule_Match == Tier 2)` → Score 5.5 (e.g. Budget NPU Standard Fallback).
            //         *   `IF (Device_Brand == "Apple" AND SoC_Model IN ["Apple A8", "Apple A9", "Apple A10"])` → Score 5.5.
            //         *   `IF (SoC_Model IN ["Snapdragon 820", "Snapdragon 821", "Snapdragon 835", "Snapdragon 730", "Snapdragon 675", "Snapdragon 670"])` → Score 5.5.
            //
            //  • "Tier 4: CPU/GPU Fallback"                          → 3.00
            //     *   *Definition:* The device relies entirely on generic runtime translation (e.g., standard **Android NNAPI** or early OpenGL kernels). Operations are emulated slowly without pipeline-specific silicon.
            //     *   *Agent Validation Rule (Concrete boolean check):*
            //         *   `IF (OS IN ["Android", "HarmonyOS", "iOS", "Windows Mobile", "BlackBerry OS", "Tizen"])` AND NOT (Previous Tier Match) → Score 3.0.
            //         *   *Example Application:* Budget Unisoc/Helio A-series, iPhone 4S through iPhone 5s (A4-A7).
            //
            //  • "Tier 5: Minimal / None"                            → 0.00
            //     *   *Definition:* Device lacks any software framework capable of ML execution.
            //     *   *Agent Validation Rule (Concrete boolean check):*
            //         *   `IF (OS IN ["KaiOS", "Series 30+", "Symbian", "Proprietary"]) OR (Form_Factor == "Feature Phone")` → Score 0.0.
            //         *   `IF (SoC_Series == "Pre-A4 Apple" OR "ARMv6 and older")` → Score 0.0.
            //
            // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all applicable marketing names/technologies found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
          },
          "scores": {
            "subscore_NPU":      { "subscore_path": "6_4_ai_hardware_performance.method_c_prediction_model_AI.npu_score.value",               "weight_NPU": 0.40 },
            "subscore_RAM_tech": { "subscore_path": "6_5_ram_technology.scores.predicted",                                                    "weight_RAM_tech": 0.20 },
            "subscore_Software": { "subscore_path": "6_4_ai_hardware_performance.method_c_prediction_model_AI.software_stack.subscore",       "weight_Software": 0.15 },
            "subscore_GPU":      { "subscore_path": "6_3_graphics_processing_unit_performance.method_c_prediction_model_GPU.predicted_score", "weight_GPU": 0.15 },
            "subscore_CPU":      { "subscore_path": "6_2_cpu_architecture_single_core.scores.predicted",                                      "weight_CPU": 0.10 },
            // These inputs are used to calculate the predicted score (Method C):
            "predicted": 9.21,
            // SCORING GUIDELINE: Sum(subscore_X * weight_X) for all 5 entries above. This is the score used for Method B neighbors.
            // IMPORTANT: Always use Predicted Scores (before any Boosters), not Final Scores, to ensure hardware-only comparison. IMPORTANT: For the `GPU` component score, use the **Model C Predicted Score** (Standard Graphics only) and NOT the final composite score, as Ray Tracing does not contribute to AI performance.
          }
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_AI": {
          // SCORING GUIDELINE: Method B is populated for ALL phones (even if Method A is available) for precision validation. Search space: all phones with a known Geekbench AI score (Method A), excluding the target device itself. The interpolation MUST use exactly 3 distinct neighbor devices.
          // Step 1: Find the 3 distinct devices with the smallest weighted Euclidean distance, excluding the target device itself.
          //         Distance = √( 0.40 * (NPU_Diff)² + 0.20 * (RAM_Tech_Diff)² + 0.15 * (Software_Diff)² + 0.15 * (GPU_Diff)² + 0.10 * (CPU_Diff)² )
          //         - Where each "Diff" term represents the absolute score difference (|Target − Neighbor|) for the component scores retrieved via the `subscore_path` entries in `method_c_prediction_model_AI.scores`.
          // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
          "neighbors": [
            {
              // Neighbor1
              "device_id_1": "xiaomi_14_ultra",
              // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
              "euclidean_distance_1": 0.0500,
              // GUIDELINE: Weighted Euclidean distance from Step 1.
              "predicted_score_1": 8.60,
              // GUIDELINE: The neighbor's own Method C predicted score.
              "benchmark_score_1": 8.34
              // GUIDELINE: The neighbor's Method A subscore.
            },
            {
              // Neighbor2
              "device_id_2": "oneplus_12",
              "euclidean_distance_2": 0.0800,
              "predicted_score_2": 8.50,
              "benchmark_score_2": 8.30
            },
            {
              // Neighbor3
              "device_id_3": "asus_rog_phone_8_pro",
              "euclidean_distance_3": 0.1000,
              "predicted_score_3": 8.55,
              "benchmark_score_3": 8.32
            }
          ],
          "avg_predicted_neighbors": 8.5500,
          // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
          "avg_benchmark_neighbors": 8.3200,
          // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
          "correction_ratio": 1.0772,
          // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_AI.scores.predicted / avg_predicted_neighbors.
          "interpolated_score": 8.96
          // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
        },
        "scores": {
          "predicted": 8.90,
          // SCORING GUIDELINE: Final weighted predicted score. Formula: (method_c_prediction_model_AI.scores.predicted * 0.75) + (6_6_ram_capacity.scores.predicted * 0.10) + (6_10_thermal_dissipation_stability.scores.predicted * 0.075) + (6_8_storage_capacity.scores.predicted * 0.05) + (6_7_storage_technology.scores.predicted * 0.025).
          "final": {
            "value": 8.25,
            // SCORING GUIDELINE: Final Score combines the AI System Score with residency gates (RAM/Storage) and thermal stability (TDSI) according to the A→B→C hierarchy. Formula: (AI_System_Score * 0.75) + (6_6_ram_capacity.scores.predicted * 0.10) + (6_10_thermal_dissipation_stability.scores.predicted * 0.075) + (6_8_storage_capacity.scores.predicted * 0.05) + (6_7_storage_technology.scores.predicted * 0.025). 
            // AI_System_Score is derived from Method A (method_a_benchmark_AI.subscore) if available; if not, Method B (method_b_neighbor_interpolation_AI.interpolated_score); if not, Method C (method_c_prediction_model_AI.scores.predicted). 
            "method_used": "Benchmark (Geekbench AI)",
            // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
            //   • Benchmark (Geekbench AI) → Method A (documented Geekbench AI score)
            //   • Neighbor Interpolation   → Method B (similar device benchmarks)
            //   • Predictor                → Method C (weighted spec calculation)
            "booster": "No",
            // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
            "confidence": "N/A"
            // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
          }
        }
      },
      "6_5_ram_technology": {
        // SCORING GOAL: Evaluates RAM (Random Access Memory) throughput and efficiency using the Memory Technology Efficiency Index (MTEI).
        // RAM is the device's "short-term memory" where active data is stored for immediate access. 
        // Newer technologies like LPDDR5X or even LPDDR5T allow for significantly faster data transfer speeds—measured in MT/s (Megatransfers per second).
        //
        // ═══════════════════════════════════════════════════════════════════════════
        // MTEI SCORING & RESOLUTION MATRIX (AUTONOMOUS REFERENCE)
        // ═══════════════════════════════════════════════════════════════════════════
        // | Denomination | MT/s (Basis)  | Score | Marketing Terms & Keywords                                 |
        // | :----------- | :-----------: | :---- | :--------------------------------------------------------- |
        // | LPDDR5T      | 9600          | 10.00 | Turbo (SK Hynix/Vivo), 9.6 Gbps, Enhanced 5X Peak          |
        // | LPDDR5X-8533 | 8533          |  9.34 | Full-blooded (Xiaomi/Redmi), Peak, 8.5 Gbps                |
        // | LPDDR5X-7500 | 7500          |  8.62 | Power Optimized, 7.5 Gbps, Standard 5X, Optimized          |
        // | LPDDR5-6400  | 6400          |  7.74 | Unified Memory (Apple A16/A17 Pro), 6.4 Gbps, High-speed 5 |
        // | LPDDR5-5500  | 5500          |  6.89 | Standard LPDDR5, 5.5 Gbps, Mainstream 5                    |
        // | LPDDR4X-4266 | 4266          |  5.47 | Enhanced 4X, Peak 4X, 4.2 Gbps, High-speed 4X              |
        // | LPDDR4X-3733 | 3733          |  4.73 | Standard LPDDR4X, 3.7 Gbps, Mainstream 4X                  |
        // | LPDDR4-3200  | 3200          |  3.87 | High-speed LPDDR4, 3.2 Gbps, Standard 4                    |
        // | LPDDR4-2133  | 2133          |  1.60 | Budget LPDDR4, 2.1 Gbps, Entry LPDDR4                      |
        // | LPDDR3       | 1600          |  0.00 | Baseline, Legacy, Obsolete, 1.6 Gbps, LPDDR3/2/1           |
        //
        // DATA PRIORITY RULES (Authoritative Logic Hierarchy):
        // To ensure absolute scoring neutrality and prevent speculative "peak-speed" awarding for undisclosed hardware, the following hierarchy MUST be followed:
        //
        //   1. LEVEL 1: VERBATIM SPECIFICATION (PRIMARY)
        //      - Use only if the exact MT/s (e.g., "8533 MT/s") is found in the official technical specification or verified hardware teardown.
        //   2. LEVEL 2: DETERMINISTIC MARKETING BIN (SECONDARY)
        //      - If MT/s is missing but qualified marketing terms (e.g., "Turbo", "9.6 Gbps", "Full-blooded") are used, match them directly to the Resolution Matrix above.
        //   3. LEVEL 3: CONSERVATIVE GENERATIONAL FALLBACK
        //      - If only a generic generation is disclosed (e.g., "LPDDR5X", "LPDDR5"), the agent MUST resolve to the **Standard/Consensus JEDEC baseline** for that generation.
        //      - PEAK BIN SCORES (e.g., 8533 MT/s, 9600 MT/s) are strictly PROHIBITED for generic disclosures.
        //      - EXAMPLES: 
        //                       Generic "LPDDR5X" resolves to **7500 MT/s**
        //                       Generic "LPDDR5"  resolves to **5500 MT/s**
        //                       Generic "LPDDR4X" resolves to **3733 MT/s**

        "technology_generation": {
          "value": "Tier 2: LPDDR5X-8533",
          "value_details": {
            "Tier 1: LPDDR5T-9600": [],
            "Tier 2: LPDDR5X-8533": [
              { "name": "Full-blooded LPDDR5X", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: LPDDR5X-7500": [],
            "Tier 4: LPDDR5-6400": [],
            "Tier 5: LPDDR5-5500": [],
            "Tier 6: LPDDR4X-4266": [],
            "Tier 7: LPDDR4X-3733": [],
            "Tier 8: LPDDR4-3200": [],
            "Tier 9: LPDDR4-2133": [],
            "Tier 10: LPDDR3-1600 or older": []
          }
          // SCORING GUIDELINE: Identify the RAM technical denomination strictly via reported standard or data rate.
          // Match the device's highest verified specification to the corresponding Tier in the "MTEI SCORING & RESOLUTION MATRIX" above. 
          // Use the following exact Tier Names for "value" (always apply the highest applicable tier) and store the related score in "effective_speed_mts".
          //   • "Tier 1: LPDDR5T-9600"         → 10.00
          //   • "Tier 2: LPDDR5X-8533"         → 9.34
          //   • "Tier 3: LPDDR5X-7500"         → 8.62
          //   • "Tier 4: LPDDR5-6400"          → 7.74
          //   • "Tier 5: LPDDR5-5500"          → 6.89
          //   • "Tier 6: LPDDR4X-4266"         → 5.47
          //   • "Tier 7: LPDDR4X-3733"         → 4.73
          //   • "Tier 8: LPDDR4-3200"          → 3.87
          //   • "Tier 9: LPDDR4-2133"          → 1.60
          //   • "Tier 10: LPDDR3-1600 or older" → 0.00
          // VALUE_DETAILS GUIDELINE: To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name/Data Rate", "source": "URL", "exact_extract": "Verbatim proof"}.
        },
        "effective_speed_mts": {
          "value": 8533,
          // GUIDELINE: The effective transfer rate in MT/s.
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 9.34
          // SCORING GUIDELINE: Match the "effective_speed_mts.value" to the "MTEI SCORING & RESOLUTION MATRIX" above to retrieve the precise score.
        },
        "scores": {
          "predicted": 9.34,
          // SCORING GUIDELINE: scores.predicted directly inherits effective_speed_mts.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 9.34,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "6_6_ram_capacity": {
        // SCORING GOAL: Evaluates total physical system RAM capacity.
        "capacity_gb": {
          "value": 12,
          // GUIDELINE: Inherits the physical RAM capacity from the device identity Section.
          "value_path": "identity.hardware_configuration.ram_gb.value",
          "subscore": 7.21
          // SCORING GUIDELINE: Score = 10 * (log(GB) - log(RAM_GB_Min)) / (log(RAM_GB_Max) - log(RAM_GB_Min)), clamped 0-10. 
          // VIRTUAL RAM DISCRIMINATION:
          //    - The scoring engine MUST strictly distinguish between physical hardware and software-based "Virtual RAM" (e.g., RAM Plus, Dynamic RAM, Extended RAM).
          //    - VIRTUAL RAM IS PROHIBITED: If a spec says "12GB + 8GB Extended RAM", the scorable value is STRICTLY **12**.
          //    - DYNAMIC STRINGS: Ignore strings like "Up to 24GB RAM" if they refer to swap space.
        },
        "scores": {
          "predicted": 7.21,
          // SCORING GUIDELINE: scores.predicted directly inherits capacity_gb.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 7.21,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "6_7_storage_technology": {
        // SCORING GOAL: Evaluates internal storage protocol efficiency and sequential throughput using the Storage Technology Efficiency Index (STEI).
        // Faster storage directly impacts system boot times, app installation speed, and overall OS responsiveness.
        // Storage throughput is measured in MB/s (Megabytes per second), representing the data bottleneck between the flash memory and the SoC.
        //
        // ═══════════════════════════════════════════════════════════════════════════
        // STEI SCORING & RESOLUTION MATRIX (AUTONOMOUS REFERENCE)
        // ═══════════════════════════════════════════════════════════════════════════
        // | Tier    | Denomination (Logic Key)      | Score | MB/s  |
        // | :------ | :---------------------------- | :---- | :---- |
        // | Tier 1  | UFS 4.0 Peak / NVMe (A17/18)  | 10.00 | 4200  |
        // | Tier 2  | UFS 4.0 Base / NVMe (A16)     |  9.10 | 3000  |
        // | Tier 3  | UFS 3.1 (Enhanced - WB+HPB)   |  8.15 | 2100  |
        // | Tier 4  | UFS 3.1 Standard / NVMe (A15) |  7.66 | 1750  |
        // | Tier 5  | UFS 3.0 / NVMe (A14)          |  7.15 | 1450  |
        // | Tier 6  | UFS 2.2 / NVMe (A13)          |  6.16 | 1000  |
        // | Tier 7  | UFS 2.1 (Peak)                |  5.72 | 850   |
        // | Tier 8  | UFS 2.1 Standard / NVMe (A12) |  4.80 | 600   |
        // | Tier 9  | UFS 2.0 / NVMe (A11)          |  4.02 | 450   |
        // | Tier 10 | eMMC 5.1 Peak / NVMe (A10)    |  3.20 | 330   |
        // | Tier 11 | eMMC 5.1 Base / NVMe (A9)     |  2.11 | 220   |
        // | Tier 12 | eMMC 5.0                      |  1.09 | 150   |
        // | Tier 13 | eMMC ≤ 4.5 / NVMe (A8 & Older)|  0.00 | 100   |
        //
        // RESOLUTION LOGIC:
        // 1. PRIMARY: MB/s VERBATIM -> Match verbatim sequential read speed (e.g., "2100 MB/s") to the nearest Basis.
        // 2. SECONDARY: TECH + KEYWORDS (Exhaustive Mapping) ->
        //    - Tier 1 (Peak 4.0): Requires "UFS 4.0" AND ("Peak" OR "High-speed" OR "4.2 GB/s").
        //    - Tier 3 (Enhanced 3.1): Requires "UFS 3.1" AND ("Write Booster" OR "WB") AND ("HPB" OR "Host Performance Booster").
        //    - Tier 7 (Peak 2.1): Requires "UFS 2.1" AND ("Turbo Write" OR "Write Booster" OR "WB").
        //    - Tier 10 (Peak eMMC 5.1): Requires "eMMC 5.1" AND ("Peak" OR "High-speed").
        // 3. TERTIARY: BASELINE by default (Ambiguous Disclosure) ->
        //    - Generic "UFS 4.0" -> Tier 2 (Baseline).
        //    - Generic "UFS 3.1" -> Tier 4 (Baseline).
        //    - Generic "UFS 2.1" -> Tier 8 (Baseline).
        //    - Generic "eMMC 5.1" -> Tier 11 (Baseline).
        // 4. FALLBACK: SoC PARITY -> Map Apple devices exactly as defined in 'Denomination' column.
        //
        "storage_format": {
          "value": "Tier 1: UFS 4.0 Peak",
          "value_details": {
            "Tier 1: \"UFS 4.0 Peak\" OR \"NVMe (A17/18)\"": [
               { "name": "UFS 4.0 Peak", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 2: \"UFS 4.0 Base\" OR \"NVMe (A16)\"": [],
            "Tier 3: \"UFS 3.1 (Enhanced - WB + HPB)\"": [],
            "Tier 4: \"UFS 3.1 Standard\" OR \"NVMe (A15)\"": [],
            "Tier 5: \"UFS 3.0\" OR \"NVMe (A14)\"": [],
            "Tier 6: \"UFS 2.2\" OR \"NVMe (A13)\"": [],
            "Tier 7: \"UFS 2.1 (Peak)\"": [],
            "Tier 8: \"UFS 2.1 Standard\" OR \"NVMe (A12)\"": [],
            "Tier 9: \"UFS 2.0\" OR \"NVMe (A11)\"": [],
            "Tier 10: \"eMMC 5.1 Peak\" OR \"NVMe (A10)\"": [],
            "Tier 11: \"eMMC 5.1 Base\" OR \"NVMe (A9)\"": [],
            "Tier 12: \"eMMC 5.0\"": [],
            "Tier 13: \"eMMC ≤ 4.5\" OR \"NVMe (A8 & Older)\"": []
          }
          // SCORING GUIDELINE: Identify the storage technical denomination strictly via reported protocol or sequential throughput.
          // Match the device's highest verified specification to the corresponding Tier in the "STEI SCORING & RESOLUTION MATRIX" above.
          // TRACEABILITY RULE: In the final "value" field, keep ONLY the denomination part that applies to the device to ensure precise traceability.
          // Use the following exact Tier Names as the basis for "value" (always apply the highest applicable tier) and store the related score in "effective_sequential_read_mbps".
          //   • Tier 1:  "UFS 4.0 Peak" OR "NVMe (A17/18)"        → 10.00
          //   • Tier 2:  "UFS 4.0 Base" OR "NVMe (A16)"           → 9.10
          //   • Tier 3:  "UFS 3.1 (Enhanced - WB + HPB)"          → 8.15
          //   • Tier 4:  "UFS 3.1 Standard" OR "NVMe (A15)"       → 7.66
          //   • Tier 5:  "UFS 3.0" OR "NVMe (A14)"                → 7.15
          //   • Tier 6:  "UFS 2.2" OR "NVMe (A13)"                → 6.16
          //   • Tier 7:  "UFS 2.1 (Peak)"                         → 5.72
          //   • Tier 8:  "UFS 2.1 Standard" OR "NVMe (A12)"       → 4.80
          //   • Tier 9:  "UFS 2.0" OR "NVMe (A11)"                → 4.02
          //   • Tier 10: "eMMC 5.1 Peak" OR "NVMe (A10)"          → 3.20
          //   • Tier 11: "eMMC 5.1 Base" OR "NVMe (A9)"           → 2.11
          //   • Tier 12: "eMMC 5.0"                               → 1.09
          //   • Tier 13: "eMMC ≤ 4.5" OR "NVMe (A8 & Older)"      → 0.00
          // VALUE_DETAILS GUIDELINE: To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name/MBps Rate", "source": "URL", "exact_extract": "Verbatim proof"}.
        },
        "effective_sequential_read_mbps": {
          "value": 4200,
          // GUIDELINE: The effective sequential throughput in MB/s.
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Match the "effective_sequential_read_mbps.value" to the "STEI SCORING & RESOLUTION MATRIX" above to retrieve the precise score.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits effective_sequential_read_mbps.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "6_8_storage_capacity": {
        // SCORING GOAL: Evaluates total physical internal non-volatile memory capacity using the Storage Capacity Index (SCI).
        // Higher storage allows for expansive on-device AI models (§6.4) and high-resolution media without performance degradation due to capacity saturation.
        //
        // ═════════════════════════════════════
        // SCI SCORING & BENCHMARK REFERENCE
        // ═════════════════════════════════════
        // | Denomination | Basis (GB) | Score | 
        // | :----------- | :--------: | :---- |
        // | 2 TB         | 2048       | 10.00 |
        // | 1 TB         | 1024       |  8.75 |
        // | 512 GB       | 512        |  7.50 |
        // | 256 GB       | 256        |  6.25 |
        // | 128 GB       | 128        |  5.00 |
        // | 64 GB        | 64         |  3.75 |
        // | 32 GB        | 32         |  2.50 |
        // | 16 GB        | 16         |  1.25 |
        // | ≤8 GB        | 8          |  0.00 |
        //
        // CONSOLIDATION & NORMALIZATION RULES:
        // 1. VARIANT ISOLATION: The database scores the SPECIFIC variant listed in Section 0 (Identity). If a phone has 128/256/512 variants, ensure the scorable `value` matches the `identity` version.
        // 2. PHYSICAL EXCLUSIVITY: Strictly exclude "Cloud", "Virtual", or "MicroSD-combined" strings. Only the physical NAND flash integrated into the main logic board is eligible for scoring.
        //
        "capacity_gb": {
          "value": 512,
          // GUIDELINE: Inherits the physical storage capacity from the device identity Section.
          "value_path": "identity.hardware_configuration.storage_gb.value",
          "subscore": 7.50
          // SCORING GUIDELINE: Subscore is resolved via the SCI SCORING & BENCHMARK REFERENCE table (defined above). Score is clamped 0-10.
        },
        "scores": {
          "predicted": 7.50,
          // SCORING GUIDELINE: scores.predicted directly inherits capacity_gb.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 7.50,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "6_9_storage_expandability": {
        // SCORING GOAL: Evaluates the device's ability to expand its non-volatile memory via removable media (e.g. microSD, NM card). 
        // This is a critical usability differentiator for power users, media creators, and offline consumers who require large, inexpensive storage buffers without sacrificing SIM connectivity.
        // It is a deterministic index based strictly on physical slot configuration and trade-offs.
        //
        // ════════════════════════════════════════════════════════════════════════════════════════════════════════════════
        // MEMORY EXPANSION RESOLUTION MATRIX (AUTONOMOUS REFERENCE)
        // ════════════════════════════════════════════════════════════════════════════════════════════════════════════════
        // | Tier    | Architecture (Logic Key)      | Score | Marketing Terms & Keywords                                 |
        // | :------ | :---------------------------- | :---- | :--------------------------------------------------------- |
        // | Tier 1  | Dedicated Slot                | 10.00 | Triple slot, 3-card tray, 2 SIM + 1 SD, Dedicated microSD  |
        // | Tier 2  | Hybrid Slot                   |  7.00 | Shared SIM slot, SIM2 or MicroSD, 2-in-1 tray              |
        // | Tier 3  | Proprietary                   |  5.00 | Nano Memory, NM card support, Huawei Memory                |
        // | Tier 4  | None                          |  0.00 | No expansion, non-expandable, physical storage fixed       |
        //
        // DATA PRIORITY RULES (Authoritative Logic Hierarchy):
        // 1. PRIMARY: PHYSICAL TRAY INSPECTION / SCHEMATIC ->
        //    - Tier 1: Requires evidence of 3 distinct physical contact points (e.g. "Triple slot") or official mention of "Dedicated slot for MicroSD".
        //    - Tier 2: Confirmed by terms like "Shared slot" or "SIM2 or SD".
        // 2. SECONDARY: eSIM FLEXIBILITY CLARIFICATION ->
        //    - Devices utilizing a physical Hybrid tray (1x dedicated Nano-SIM slot + 1x shared slot for either SIM2 or a memory card) are strictly categorized as **Tier 2: Hybrid Slot**, regardless of eSIM support. While eSIM allows for dual-line usage without a second physical card, the physical architecture still forces a trade-off for users with two physical Nano-SIM cards.
        // 3. TERTIARY: Original Equipment Manufacturer (OEM) BRANDING ->
        //    - Huawei devices with NM cards score strictly as **Tier 3 (Proprietary)** due to limited third-party card availability and higher cost-per-GB.
        // 4. FALLBACK: ABSENCE OF EVIDENCE -> 
        //    - If no expansion mentioned in GSMarena or other sources (Memory -> Card slot: No), resolve to **Tier 4 (None)**.
        //
        "expandability_support": {
          "value": "Tier 4: None",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.00
          // SCORING GUIDELINE: Identify the expandability support strictly via the physical slot configuration. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Dedicated Slot" → 10.00
          //     Definition: Separate tray or contact specifically for a removable memory card (microSD) that does not interfere with simultaneous Dual SIM usage.
          //   • "Tier 2: Hybrid Slot"    → 7.00
          //     Definition: Shared slot where the user must choose between a second physical SIM card or a memory card (e.g., microSD, Nano Memory).
          //   • "Tier 3: Proprietary"    → 5.00
          //     Definition: Support for branded/exclusive removable storage formats (e.g., Huawei NM Card).
          //   • "Tier 4: None"           → 0.00
          //     Definition: No physical hardware interface for local storage expansion.
          // 
          // RESOLUTION OF AMBIGUITY:
          // In cases where marketing terms or technical descriptions are unclear, prioritize the PHYSICAL TRAY INSPECTION and DATA PRIORITY RULES documented in the RESOLUTION MATRIX above to ensure deterministic categorization.
        },
        "scores": {
          "predicted": 0.00,
          // SCORING GUIDELINE: scores.predicted directly inherits expandability_support.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 0.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "6_10_thermal_dissipation_stability": {
        // SCORING GOAL: Evaluates internal cooling capability and sustained performance using the Thermodynamic RC Model.
        // This section bridges physical heat dissipation capacity (Watts) to visual stability (FPS) using a 0.40 Gamma scaling factor.
        
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Direct Benchmark (Primary Standard: 3DMark Wild Life Extreme)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_TDSI": {
          "value": 92.4,
          // GUIDELINE: Stability percentage from a 20-minute 3DMark Wild Life Extreme Stress Test.
          "source": "https://www.gsmarena.com/oneplus_nord_4-review-2720p4.php",
          "exact_extract": "OnePlus Nord 4 [...] 3DMark Wild Life Extreme Stress Test stability: 92.4%",
          "subscore": 9.01
          // SCORING GUIDELINE: subscore = 10 * (log(value) - log(GPU_Stability_Min)) / (log(GPU_Stability_Max) - log(GPU_Stability_Min)), clamped 0-10. (Min=40, Max=100).
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_TDSI": {
          "neighbors": [
            {
              "device_id_1": "oneplus_nord_3",
              "predicted_score_1": 8.10,
              "benchmark_score_1": 7.85
            },
            {
              "device_id_2": "samsung_galaxy_s24_ultra",
              "predicted_score_2": 8.65,
              "benchmark_score_2": 3.65
            },
            {
              "device_id_3": "xiaomi_14_ultra",
              "predicted_score_3": 8.50,
              "benchmark_score_3": 5.20
            }
          ],
          "avg_predicted_neighbors": 8.41,
          "avg_benchmark_neighbors": 5.57,
          "correction_ratio": 1.0285,
          "interpolated_score": 5.73
          // SCORING GUIDELINE: standard correction ratio interpolation based on Method C predicted scores.
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Thermodynamic RC Prediction Model (Tertiary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_TDSI": {
          "supply_dissipation_capacity": {
            "effective_surface_area_mm2": {
              "value": 9500,
              "calculation": "Total_Area * Beta(0.80 for Metal + Graphite)",
              "subscore": 8.50
            },
            "thermal_mass_capacitance": {
              "value": 200,
              "description": "Chassis weight in grams acting as thermal sponge",
              "subscore": 7.50
            },
            "sustainable_watts_20min": 4.85
            // SCORING GUIDELINE: Result of the transient ODE solver at 1200s for a 20°C rise.
          },
          "demand_soc_generation": {
            // █ SOC_PEAK_POWER_MATRIX:
            // | SoC Model                                | Peak Power (W) | Node  | Foundry |
            // | :---------------------------------------- | :------------: | :---: | :-----: |
            // | **Snapdragon 8 Elite**                    | **19.5**       | 3nm   | TSMC    |
            // | **Snapdragon 8 Gen 5 (Est.)**             | **19.0**       | 2nm   | TSMC    |
            // | **Snapdragon 8 Gen 1**                    | **16.5**       | 4nm   | Samsung |
            // | **Dimensity 9400**                        | **15.5**       | 3nm   | TSMC    |
            // | **Apple A19 Pro (Est.)**                  | **15.0**       | 2nm   | TSMC    |
            // | **Apple A18 Pro**                         | **14.5**       | 3nm   | TSMC    |
            // | **Snapdragon 8 Gen 3**                    | **14.0**       | 4nm   | TSMC    |
            // | **Exynos 2400**                           | **12.5**       | 4nm   | Samsung |
            // | **Dimensity 9300**                        | **12.0**       | 4nm   | TSMC    |
            // | **Apple A17 Pro**                         | **11.5**       | 3nm   | TSMC    |
            // | **Kirin 9010**                            | **11.0**       | 7nm   | SMIC    |
            // | **Snapdragon 888**                        | **10.5**       | 5nm   | Samsung |
            // | **Kirin 9000S**                           | **10.5**       | 7nm   | SMIC    |
            // | **Exynos 2200**                           | **10.0**       | 4nm   | Samsung |
            // | **Google Tensor G3**                      | **9.5**        | 4nm   | Samsung |
            // | **Snapdragon 8 Gen 2**                    | **9.0**        | 4nm   | TSMC    |
            // | **Kirin 9000**                            | **9.0**        | 5nm   | TSMC    |
            // | **Apple A16 Bionic**                      | **8.5**        | 4nm   | TSMC    |
            // | **Snapdragon 8+ Gen 1**                   | **8.0**        | 4nm   | TSMC    |
            // | **Apple A15 Bionic**                      | **7.5**        | 5nm   | TSMC    |
            // | **Snapdragon 7+ Gen 2**                   | **7.0**        | 4nm   | TSMC    |
            // | **Dimensity 8100**                        | **6.5**        | 5nm   | TSMC    |
            // | **Snapdragon 865**                        | **6.2**        | 7nm   | TSMC    |
            // | **Apple A14 Bionic**                      | **5.8**        | 5nm   | TSMC    |
            // | **Exynos 990**                            | **5.5**        | 7nm   | Samsung |
            // | **Snapdragon 855**                        | **5.2**        | 7nm   | TSMC    |
            // | **Apple A13 Bionic**                      | **4.8**        | 7nm   | TSMC    |
            // | **Snapdragon 845**                        | **4.5**        | 10nm  | Samsung |
            // | **Apple A12 Bionic**                      | **4.2**        | 7nm   | TSMC    |
            // | **Snapdragon 835**                        | **4.0**        | 10nm  | Samsung |
            // | **Apple A11 Bionic**                      | **4.0**        | 10nm  | TSMC    |
            // | **Apple A10 Fusion**                      | **3.8**        | 16nm  | TSMC    |
            // | **Helio G99**                             | **3.2**        | 6nm   | TSMC    |
            // | **Snapdragon 820**                        | **3.0**        | 14nm  | Samsung |
            // | **Dimensity 6020**                        | **2.8**        | 7nm   | TSMC    |
            // | **Snapdragon 625**                        | **2.5**        | 14nm  | Samsung |
            // | **Unisoc T606**                           | **2.2**        | 12nm  | TSMC    |
            //
            "peak_soc_wattage_tier": {
              "identifier": "Snapdragon 7+ Gen 3",
              "reference_table": "SOC_PEAK_POWER_MATRIX",
              "lookup_parameter": "Peak Power (W)",
              "value": 11.5
            }
          },
          "base_system_heat": {
            "p_static_watts": 0.40,
            "display_area_cm2": 107.4,
            "k_display_heat": 0.007,
            "total_base_heat_watts": 1.15
            // SCORING GUIDELINE: 0.40 + (0.007 * Area_Front_cm2).
          },
          "admissible_soc_budget": 2.50,
          // SCORING GUIDELINE: System_P_adm (from capacity_dissipation) - total_base_heat_watts.
          "sustained_performance_ratio": 0.76,
          // SCORING GUIDELINE: (admissible_soc_budget / peak_soc_wattage) ^ 0.33. Max 1.0.
          "predicted_score": 7.00
          // SCORING GUIDELINE: 10 * (log(Ratio * 100) - log(40)) / (log(100) - log(40)).
        },

        "scores": {
          "predicted": 8.95,
          "final": {
            "value": 9.01,
            "method_used": "Benchmark (3DMark)",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      }
    },
    "7_connectivity_and_sensors": {
      "7_1_cellular_capabilities": {
        // SCORING GOAL: Evaluates max cellular network standards.
        "network_technology": {
          "value": "Tier 1: 5G mmWave + Sub-6 (Global band coverage)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the highest cellular technology supported. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: 5G mmWave + Sub-6 (Global band coverage)" → 10.00
          //     Definition: Supports both mmWave (high frequency, short range) and Sub-6 (lower frequency, long range) 5G spectrums, covering all major global frequency bands.
          //   • "Tier 2: 5G Sub-6 (Global band coverage)"          → 8.50
          //     Definition: Supports 5G on Sub-6GHz frequencies with extensive band coverage for global roaming.
          //   • "Tier 3: 5G Sub-6 (Regional band coverage)"        → 7.50
          //     Definition: Supports 5G on Sub-6GHz but with band coverage limited to specific markets.
          //   • "Tier 4: 4G LTE-A (Cat 24+)"                       → 5.00
          //     Definition: 4G LTE Advanced with support for high-order carrier aggregation and 4x4 MIMO.
          //   • "Tier 5: 4G LTE"                                   → 2.50
          //     Definition: Standard 4G Long-Term Evolution without advanced carrier aggregation.
          //   • "Tier 6: 3G / Legacy"                              → 0.00
          //     Definition: Limited to 3G (UMTS/HSPA) or older technologies.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits network_technology.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "7_2_sim_capabilities": {
        // SCORING GOAL: Evaluates subscriber identity module format support.
        "sim_configuration": {
          "value": "Tier 1: Dual eSIM / iSIM + Physical Slot",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the SIM configuration. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Dual eSIM / iSIM + Physical Slot" → 10.00
          //     Definition: Supports two or more active eSIM profiles/integrated SIM alongside a physical Nano-SIM slot.
          //   • "Tier 2: eSIM + Physical Slot"              → 8.00
          //     Definition: Supports one active eSIM profile alongside a physical Nano-SIM slot.
          //   • "Tier 3: Dual Physical Nano-SIM Only"       → 6.00
          //     Definition: Two physical Nano-SIM slots; no electronic/programmable SIM support.
          //   • "Tier 4: Single Physical Nano-SIM Only"     → 4.00
          //     Definition: Only one physical Nano-SIM slot; no dual-SIM or eSIM support.
          //   • "Tier 5: None"                              → 0.00
          //     Definition: No cellular SIM capability (e.g., tablet/media player without modem).
          // VALUE_DETAILS GUIDELINE: Record the exact Original Equipment Manufacturer (OEM) marketing name for SIM support (e.g., ["Dual eSIM"], ["Dual SIM (Nano-SIM, dual stand-by)"]).
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits sim_configuration.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "7_3_wifi_standard": {
        // SCORING GOAL: Evaluates Wi-Fi network standards.
        "standard": {
          "value": "Tier 1: Wi-Fi 7",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the highest supported Wi-Fi standard. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Wi-Fi 7"   → 10.00
          //     Definition: 802.11be standard (Extremely High Throughput). Supports 320 MHz channels, 4K QAM, and Multi-Link Operation (MLO).
          //   • "Tier 2: Wi-Fi 6E"  → 8.00
          //     Definition: 802.11ax standard adding support for the 6GHz spectrum, reducing congestion.
          //   • "Tier 3: Wi-Fi 6"   → 6.00
          //     Definition: 802.11ax standard on 2.4/5GHz. Improved efficiency and performance in dense environments.
          //   • "Tier 4: Wi-Fi 5"   → 3.00
          //     Definition: 802.11ac standard.
          //   • "Tier 5: Legacy"    → 0.00
          //     Definition: 802.11n (Wi-Fi 4) or older technology.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits standard.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "7_4_bluetooth_and_audio_codecs": {
        // SCORING GOAL: Evaluates Bluetooth version and high-fidelity audio codec support.
        "bluetooth_version": {
          "value": "Tier 2: 5.3",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 4.50
          // SCORING GUIDELINE: Identify the Bluetooth version. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: 5.4"      → 5.00
          //     Definition: Latest standard with Periodic Advertising with Responses (PAwR) and Encrypted Advertising Data.
          //   • "Tier 2: 5.3"      → 4.50
          //     Definition: Improved encryption, connection reliability, and efficiency.
          //   • "Tier 3: 5.2"      → 3.50
          //     Definition: Introduces LE Audio and Enhanced Attribute Protocol (EATT).
          //   • "Tier 4: 5.1 / 5.0" → 2.50
          //     Definition: Basic Bluetooth 5 standards.
          //   • "Tier 5: 4.2"      → 1.00
          //     Definition: Legacy Bluetooth 4 standards.
          //   • "Tier 6: < 4.2"    → 0.00
          //     Definition: Obsolete Bluetooth standards.
        },
        "highest_codec_supported": {
          "value": "Tier 2: High-Res",
          "value_details": {
            "Tier 1: Lossless": [],
            "Tier 2: High-Res": [
              { "name": "LDAC", "source": "TBD", "exact_extract": "Proof pending" },
              { "name": "aptX HD", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: Standard": [
              { "name": "AAC", "source": "TBD", "exact_extract": "Proof pending" },
              { "name": "SBC", "source": "TBD", "exact_extract": "Proof pending" }
            ]
          },
          "subscore": 4.00
          // SCORING GUIDELINE: Identify the highest supported Bluetooth audio codec tier. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Lossless"   → 5.00
          //     Definition: CD-quality audio without data loss over Bluetooth. Qualifying terms: aptX Lossless.
          //   • "Tier 2: High-Res"   → 4.00
          //     Definition: Near-lossless or high-bitrate codecs (up to 990kbps). Qualifying terms: LDAC, aptX Adaptive, aptX HD, LHDC.
          //   • "Tier 3: Standard"   → 1.50
          //     Definition: Basic distribution codecs with significant compression. Qualifying terms: AAC, SBC.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported Bluetooth codecs found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 8.50,
          // SCORING GUIDELINE: scores.predicted = bluetooth_version.subscore + highest_codec_supported.subscore (Max 10.0).
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.50,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "7_5_biometrics": {
        // SCORING GOAL: Evaluates secure unlock mechanisms.
        "best_technology": {
          "value": "Tier 2: Ultrasonic FP",
          "value_details": {
            "Tier 1: 3D Face / Sonic Gen 2": [],
            "Tier 2: Ultrasonic FP": [
              { "name": "Qualcomm 3D Sonic Gen 2", "source": "TBD", "exact_extract": "Proof pending" }
            ],
            "Tier 3: Optical FP / 2D Face": [],
            "Tier 4: Capacitive FP": [],
            "Tier 5: None / Pin Only": []
          },
          "subscore": 8.00
          // SCORING GUIDELINE: Identify the most secure/advanced available biometric unlock method. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: 3D Face / Sonic Gen 2"  → 10.00
          //     Definition: Secure 3D facial recognition (e.g., Face ID) or 2nd-gen Ultrasonic fingerprint sensors (large area, fast).
          //   • "Tier 2: Ultrasonic FP"          → 8.00
          //     Definition: Standard ultrasonic fingerprint sensors (3D mapping of the finger via sound waves).
          //   • "Tier 3: Optical FP / 2D Face"  → 6.00
          //     Definition: Standard optical fingerprint sensors (2D photograph of the finger) or basic 2D webcam-style face unlock (non-secure for payments).
          //   • "Tier 4: Capacitive FP"          → 4.00
          //     Definition: Physical button-integrated fingerprint sensors (side-mounted or rear-mounted).
          //   • "Tier 5: None / Pin Only"        → 0.00
          //     Definition: No biometric sensors; reliance on PIN, pattern, or password.
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific biometric technologies found in specs (e.g., FaceID, specific sensor models). To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "predicted": 8.00,
          // SCORING GUIDELINE: scores.predicted directly inherits best_technology.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
        "scores": {
          "predicted": 6.50,
          // SCORING GUIDELINE: scores.predicted is sum of core_sensor_suite + advanced_sensor_capabilities subscores (Max 10.0).
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 6.50,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "7_7_nfc_and_uwb": {
        // SCORING GOAL: Evaluates short-range wireless connectivity technologies.
        "configuration": {
          "value": "Tier 1: NFC + UWB",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the short-range wireless configuration. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: NFC + UWB" → 10.00
          //     Definition: Near Field Communication (NFC) for payments AND Ultra-Wideband (UWB) for precise directional tracking and digital keys.
          //   • "Tier 2: NFC Only"   → 5.00
          //     Definition: Near Field Communication support only; no directional UWB tracking.
          //   • "Tier 3: None"       → 0.00
          //     Definition: No short-range wireless connectivity.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits configuration.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted is sum of all subscores above (Max 10.0).
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "7_9_usb_port_speed": {
        // SCORING GOAL: Evaluates wired transfer speed.
        "version_speed": {
          "value": "Tier 2: USB 3.2 Gen 2 (10Gbps)",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 9.00
          // SCORING GUIDELINE: Identify the USB version and speed. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: USB 3.2 Gen 2x2 (20Gbps)" → 10.00
          //     Definition: SuperSpeed USB 20Gbps.
          //   • "Tier 2: USB 3.2 Gen 2 (10Gbps)"   → 9.00
          //     Definition: SuperSpeed USB 10Gbps.
          //   • "Tier 3: USB 3.2 Gen 1 (5Gbps)"    → 7.50
          //     Definition: SuperSpeed USB 5Gbps (formerly USB 3.0/3.1 Gen 1).
          //   • "Tier 4: USB 2.0 (480Mbps)"        → 2.00
          //     Definition: High Speed USB 2.0.
          //   • "Tier 5: Proprietary / Legacy"     → 0.00
          //     Definition: Non-standard or obsolete physical/logical interface.
        },
        "scores": {
          "predicted": 9.00,
          // SCORING GUIDELINE: scores.predicted directly inherits version_speed.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 9.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      }
    },
    "8_battery_and_charging": {
      "8_1_battery_endurance_score": {
        // SCORING GOAL: Evaluates smartphone battery life by prioritizing real-world performance data over theoretical specifications via a Benchmark-First Approach with Predictive Interpolation.
        
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Benchmark Validation (Primary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_Battery": {
          "gsmarena_active_use_score_v2": {
            "value": 16.75,
            "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2667p3.php",
            "exact_extract": "Active use score: 16:45h",
            "subscore": 9.45
            // SCORING GUIDELINE: source is GSMArena.
            // • WHERE TO FIND IT: GSMarena.com review (Battery page).
            // • EXTRACTION RULE: Use the "Active use score" (e.g., "16:45h"). 
            // • CALCULATION: Convert format HH:MM to decimal hours (e.g., 16:45 = 16.75) for the normalization formula.
            // SCORING GUIDELINE: subscore = 10 * (value - Battery_GSMArena_Hours_Min) / (Battery_GSMArena_Hours_Max - Battery_GSMArena_Hours_Min), clamped 0-10.
            // If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
          },
          "phonearena_battery_life_estimate": {
            "value": 15.50,
            "source": "https://www.phonearena.com/phones/Samsung-Galaxy-S24-Ultra_id12151/benchmarks",
            "exact_extract": "Combined battery life: 15h 30min",
            "subscore": 9.20
            // SCORING GUIDELINE: source is PhoneArena.
            // • WHERE TO FIND IT: PhoneArena.com device specs page, under "Ratings and Benchmarks".
            // • EXTRACTION RULE: Use the "Combined battery life" estimate.
            // SCORING GUIDELINE: subscore = 10 * (value - Battery_PhoneArena_Hours_Min) / (Battery_PhoneArena_Hours_Max - Battery_PhoneArena_Hours_Min), clamped 0-10.
            // If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
          }
        },
        
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Technical Prediction Model (Tertiary / baseline for Method B)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_Battery": {
          "scores": {
            "subscore_LayerA": { "subscore_path": "8_1_battery_endurance_score.method_c_prediction_model_Battery.layer_a_energy_score.value",               "weight_LayerA": 0.45 },
            "subscore_LayerB": { "subscore_path": "8_1_battery_endurance_score.method_c_prediction_model_Battery.layer_b_hardware_efficiency_score.value", "weight_LayerB": 0.35 },
            "subscore_LayerC": { "subscore_path": "8_1_battery_endurance_score.method_c_prediction_model_Battery.layer_c_software_optimization_score.value", "weight_LayerC": 0.20 }
          },
          "layer_a_energy_score": {
            "value": 8.50
            // SCORING GUIDELINE: Theoretical capacity vs drain.
          },
          "layer_b_hardware_efficiency_score": {
            "value": 8.00,
            "value_path": "theoretical_calculation"
            // SCORING GUIDELINE (Section 8.1 Layer B): HEI = (0.40 * SoC) + (0.40 * Display) + (0.10 * Connectivity) + (0.10 * Thermal).
            // • B.1 SoC: (0.50 * Node) + (0.30 * CPU) + (0.20 * GPU).
            // • B.2 Display: (0.35 * Tech) + (0.35 * Refresh) + (0.30 * Res).
            // • B.3 Connectivity: (0.70 * Cellular) + (0.30 * WiFi).
            
            "hei_model": {
              "identifier": "HEI_v1.0",
              // GUIDELINE: Matches the versioned weight set identifier in §8.1.0 (8_1_0_battery_efficiency_model_weights.identifier).
              "reference_table": "8_1_0_battery_efficiency_model_weights",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Weight",
              // GUIDELINE: Description of the column being retrieved.
              "value": 1.0
              // GUIDELINE: Value retrieved from the Weight Table by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
            },
            "soc_efficiency": {
              "identifier": "Snapdragon 8 Gen 3",
              // GUIDELINE: Standardized SoC identifier matching the record in §1.1 (identity.hardware_configuration.chipset.value).
              "reference_table": "6_3_0_graphics_processing_unit_architecture_reference",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Efficiency",
              // GUIDELINE: Description of the column being retrieved.
              "value": 9.00,
              "weight_mapping": {
                "identifier": "HEI_v1.0",
                // GUIDELINE: Matches the versioned weight set identifier in §8.1.0 (8_1_0_battery_efficiency_model_weights.identifier).
                "reference_table": "8_1_0_battery_efficiency_model_weights",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "Weight",
                // GUIDELINE: Description of the column being retrieved.
                "value": 0.40
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              }
            },
            "display_efficiency": {
              "identifier": "LTPO AMOLED",
              // GUIDELINE: Standardized display panel technology matching the record in §2.1 (2_1_panel_technology_scoring_table.identifier).
              "reference_table": "2_1_panel_technology_scoring_table",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Score",
              // GUIDELINE: Description of the column being retrieved.
              "value": 10.00,
              // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              "weight_mapping": {
                "identifier": "HEI_v1.0",
                // GUIDELINE: Matches the versioned weight set identifier in §8.1.0 (8_1_0_battery_efficiency_model_weights.identifier).
                "reference_table": "8_1_0_battery_efficiency_model_weights",
                // GUIDELINE: Path to the authoritative §8.1.0 Weight Table for the Hardware Efficiency Index (HEI).
                "lookup_parameter": "Weight",
                // GUIDELINE: Description of the column being retrieved.
                "value": 0.40
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              }
            },
            "thermal_node_efficiency": {
              "identifier": "4nm (TSMC)",
              // GUIDELINE: Matches the combined process node and foundry identifier in §6.10 (node_efficiency_score.identifier).
              "reference_table": "6_10_thermal_dissipation_stability",
              // GUIDELINE: Path to the authoritative lookup table for mapping.
              "lookup_parameter": "Node Score",
              // GUIDELINE: Description of the column being retrieved.
              "value": 7.63,
              // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              "weight_mapping": {
                "identifier": "HEI_v1.0",
                // GUIDELINE: Matches the versioned weight set identifier in §8.1.0 (8_1_0_battery_efficiency_model_weights.identifier).
                "reference_table": "8_1_0_battery_efficiency_model_weights",
                // GUIDELINE: Path to the authoritative lookup table for mapping.
                "lookup_parameter": "Weight",
                // GUIDELINE: Description of the column being retrieved.
                "value": 0.20
                // GUIDELINE: Value retrieved from the `reference_table` by matching the `identifier` and selecting the column disclosed in `lookup_parameter`.
              }
            },
            "predicted_score": 9.13
            // SCORING GUIDELINE: predicted_score = Sum(component.value * component.weight_mapping.value).
          },
          "layer_c_software_optimization_score": {
            "value": 9.00
            // SCORING GUIDELINE: OS level power management.
          },
          "predicted_score": 8.82,
          // SCORING GUIDELINE (Section 8.1 Method C): Weighted average of layers A, B, and C. This is the score used for Method B neighbors.
          // IMPORTANT: Always use Predicted Scores (before any Boosters), not Final Scores, to ensure hardware-only comparison.
          "scores": {
            "subscore_LayerA": { "subscore_path": "method_c_prediction_model_Battery.layer_a_energy_score.value" },
            "subscore_LayerB": { "subscore_path": "method_c_prediction_model_Battery.layer_b_hardware_efficiency_score.predicted_score" },
            "subscore_LayerC": { "subscore_path": "method_c_prediction_model_Battery.layer_c_software_optimization_score.value" }
          }
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_Battery": {
          // SCORING GUIDELINE (Section 8.1 Method B): Method B is populated for ALL phones (even if Method A is available) for precision validation. Search space: all Reference Phones that have BOTH GSMArena and PhoneArena scores (Condition 1 phones), excluding the target device itself. The interpolation MUST use exactly 3 distinct neighbor devices.
          // Step 1: Find the 3 distinct devices with the smallest weighted Euclidean distance, excluding the target device itself.
          //         Distance = √( 0.45 * (Diff_LayerA)² + 0.35 * (Diff_LayerB)² + 0.20 * (Diff_LayerC)² )
          //         - Where each "Diff" term represents the absolute score difference (|Target − Neighbor|) for the component scores retrieved via the `subscore_path` entries in `method_c_prediction_model_Battery.scores`.
          // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
          "neighbors": [
            {
              // Neighbor1
              "device_id_1": "xiaomi_14_ultra",
              // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
              "euclidean_distance_1": 0.0500,
              // GUIDELINE: Weighted Euclidean distance from Step 1.
              "predicted_score_1": 8.40,
              // GUIDELINE: The neighbor's own Method C predicted score.
              "benchmark_score_1": 9.10
              // GUIDELINE: The average of the neighbor's Method A subscores (GSMArena + PhoneArena).
            },
            {
              // Neighbor2
              "device_id_2": "oneplus_12",
              "euclidean_distance_2": 0.0800,
              "predicted_score_2": 8.45,
              "benchmark_score_2": 9.40
            },
            {
              // Neighbor3
              "device_id_3": "asus_rog_phone_8_pro",
              "euclidean_distance_3": 0.1000,
              "predicted_score_3": 8.35,
              "benchmark_score_3": 9.20
            }
          ],
          "avg_predicted_neighbors": 8.4000,
          "avg_benchmark_neighbors": 9.2333,
          // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
          "correction_ratio": 1.0030,
          // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_Battery.predicted_score / avg_predicted_neighbors.
          "interpolated_score": 9.26
          // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
        },

        "scores": {
          "predicted": 8.82,
          // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_Battery.predicted_score.
          "final": {
            "value": 9.3250,
            // SCORING GUIDELINE (Section 8.1): Use Method A if method_a_benchmark_Battery is available (the average of GSMArena + PhoneArena subscores becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_Battery.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_Battery.predicted_score).
            "method_used": "Benchmark (GSMArena + PhoneArena)",
            // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
            //   • Benchmark (GSMArena + PhoneArena) → Method A (documented GSMArena/PhoneArena scores)
            //   • Neighbor Interpolation            → Method B (similar device benchmarks)
            //   • Predictor                         → Method C (weighted spec calculation)
            "booster": "No",
            // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
            "confidence": "N/A"
            // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
          }
        }
      },
      "8_2_wired_charging_speed": {
        // SCORING GOAL: Evaluates maximum wired charging input.
        "watts": {
          "value": 45,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Apply Section 8.2 Inverse Proportional formula. Score = 10 * ((1/Min) - (1/value)) / ((1/Min) - (1/Max)). Min=5W, Max=120W.
        },
        "scores": {
          "predicted": 8.00,
          // SCORING GUIDELINE: scores.predicted directly inherits watts.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 8.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "8_3_wireless_charging_speed": {
        // SCORING GOAL: Evaluates maximum wireless charging input.
        "watts": {
          "value": 15,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 5.00
          // SCORING GUIDELINE: Apply Section 8.3 Inverse Proportional formula. Score = 10 * ((1/Min) - (1/value)) / ((1/Min) - (1/Max)). Min=7.5W, Max=50W. Set to 0 if unsupported.
        },
        "scores": {
          "predicted": 5.00,
          // SCORING GUIDELINE: scores.predicted directly inherits watts.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 5.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
        "scores": {
          "predicted": 0.00,
          // SCORING GUIDELINE: scores.predicted directly inherits watts.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 0.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
        "scores": {
          "predicted": 5.00,
          // SCORING GUIDELINE: scores.predicted directly inherits watts.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 5.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "8_6_charger_in_box": {
        // SCORING GOAL: Rewards devices that include a high-speed charger in the box.
        "included_watts": {
          "value": "Tier 5: None",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.00
          // SCORING GUIDELINE: Apply Section 8.6 Ratio formula. subscore = 10 * (Included_Watts / Max_Wired_Watts). Max_Wired_Watts retrieved from Sec 8.2.
        },
        "scores": {
          "predicted": 0.00,
          // SCORING GUIDELINE: scores.predicted directly inherits included_watts.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 0.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
          // SCORING GUIDELINE: Calculate the Logarithmic Cost Score (Section 9.1). Score = 10 - 10 * (log(Price) - log(Min)) / (log(Max) - log(Min)). Min=100, Max=1600.
        },
        "scores": {
          "predicted": 0.80,
          // SCORING GUIDELINE: scores.predicted directly inherits usd.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 0.80,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      },
      "9_2_manufacturer_warranty_commitment": {
        // SCORING GOAL: Evaluates standard included warranty length.
        "months": {
          "value": "Tier 3: 12 Months",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 3.00
          // SCORING GUIDELINE: Map months to scores using the following exact Tier Names for "value":
          //   • "Tier 1: >= 36 Months" → 10.00
          //   • "Tier 2: 24 Months"    → 7.00
          //   • "Tier 3: 12 Months"    → 3.00
          //   • "Tier 4: < 12 Months"  → 0.00
        },
        "scores": {
          "predicted": 3.00,
          // SCORING GUIDELINE: scores.predicted directly inherits months.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 3.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
        "scores": {
          "predicted": 7.50,
          // SCORING GUIDELINE: scores.predicted directly inherits european_union_repairability_index.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 7.50,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      }
    },
    "10_miscellaneous": {
      "10_1_stylus_hardware_system_support": {
        // SCORING GOAL: Evaluates native stylus presence and hardware digitizer support.
        "support_tier": {
          "value": "Tier 1: Integrated active stylus + dedicated digitizer + Bluetooth features",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Identify the stylus support level. Use the following exact Tier Names for "value" with related scores as subscore (always apply the highest applicable tier):
          //   • "Tier 1: Integrated active stylus + dedicated digitizer + Bluetooth features" → 10.00
          //     Definition: Stylus is stored inside the device (silo), uses an active digitizer layer for pressure/tilt, and has a battery for remote Bluetooth gestures.
          //   • "Tier 2: Active stylus support (dedicated digitizer, no silo)"              → 7.00
          //     Definition: Device has a dedicated digitizer layer for high-precision active pens (e.g., Apple Pencil, S Pen) but no internal storage for the pen.
          //   • "Tier 3: Passive stylus or basic touch pen"                                  → 3.00
          //     Definition: No dedicated digitizer; works with generic capacitive pens that mimic finger touch.
          //   • "Tier 4: None"                                                               → 0.00
          //     Definition: No official stylus support or secondary digitizer layer.
        },
        "scores": {
          "predicted": 10.00,
          // SCORING GUIDELINE: scores.predicted directly inherits support_tier.subscore.
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 10.00,
            "method_used": "Predictor",
            "booster": "No",
            "confidence": "N/A"
          }
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
