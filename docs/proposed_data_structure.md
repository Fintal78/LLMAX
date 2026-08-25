# Ultimate Smartphone Data Structure Proposal (v5.1)

This schema is the primary, self-contained "Recipe" for AI-automated classification and scoring. It is strictly aligned with the file `scoring_rules.md`.

> [!IMPORTANT]
> ### 🚨 Handling Missing Data, Unlisted Features & Scoring Blockers
> If a required parameter's value cannot be found after an exhaustive search, OR if a feature is found but is not scorable using the provided options (e.g., a newly released codec not yet listed):
> - **Value Entry**: Set the `value` field strictly to `"Not found"` (if missing data) or the raw unlisted feature name (if unlisted feature). Do NOT use `null`, `0`, or empty strings. For missing data, set `source` and `exact_extract` fields to `"N/A"`.
> - **Scoring Procedure**: If the missing data or unlisted feature blocks the formula and NO fallback or benchmark override is possible:
>     1. Set `subscore`, `scores.predicted`, `scores.final.value`, `scores.final.method_used`, `scores.final.booster`, and `scores.final.confidence` to `"N/A"`.
>     2. **Top-Level Alert**: You MUST place a GFM alert at the very top of the generated file (above the JSON block) following one of these exact templates:
>        `> [!CAUTION]`
>        `> ### 🚨 SCORING BLOCKER: UNRESOLVED DATA GAP`
>        `> **Subsection [X.Y] ([Name])**: Score calculation is blocked due to missing required data: [Parameter Name]. No valid fallback exists.`
>        *OR*
>        `> [!CAUTION]`
>        `> ### 🚨 SCORING BLOCKER: UNLISTED FEATURE DETECTED`
>        `> **Subsection [X.Y] ([Name])**: A feature was found ([Feature Name]) but is not scorable using the provided options in the guidelines. This feature needs to be evaluated.`
> [!NOTE]
> ### 📜 Universal Data Source Verification Precedence Hierarchy
> To guarantee complete score reproducibility, objectivity, and a standardized resolution protocol whenever technical data points conflict across public specification databases, all evaluators MUST adhere strictly to the following data verification precedence hierarchy across all scoring categories:
> - **Priority 1 (Highest):** Official Manufacturer Technical Specification Sheets & Product Landing Pages.
> - **Priority 2:** Official Manufacturer User Manuals, Developer Documentation & Regulatory Filings (e.g. FCC, TENAA, CE certifications).
> - **Priority 3:** Official Operating System / Firmware Release Notes (for software-enabled feature updates).
> - **Priority 4:** Verified Hardware Teardowns & Professional Laboratory Testing Reviews (e.g. iFixit, TechInsights, GSMArena, NotebookCheck, AnandTech, Android Authority when tested).
> - **Priority 5:** Structured Specification Databases (e.g. DeviceSpecifications, PhoneArena).
> - **Priority 6 (Lowest):** Verified Community Testing (only if consistent across multiple independent sources).
> *Governance Rule:* If data sources conflict, the specification provided by the highest-precedence source strictly governs and overrides lower-tier sources.

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
  //     "value": <number>,              → The definitive score for this subsection.
  //     "calculation_formula": <string> → [OPTIONAL] Formula used to derive the value (e.g. "predicted * booster_11.X").
  //                                       If no booster is applied, value = predicted score, i.e. scores.predicted (multiplier is 1.0).
  //                                       If there is one booster:
  //                                       value = scores.predicted * booster_multiplier
  //                                       If there are several boosters:
  //                                       value = scores.predicted * booster_multiplier_1 * booster_multiplier_2 * ... 
  //                                       Each booster multiplier comes from the corresponding Section 11 entry.
  //                                       CLAMPING: The result of this calculation is ALWAYS clamped to [0.00, 10.00].
  //     "method_used": "Predictor"      → Always "Predictor" for spec-calculated scores (no Benchmark or Neighbor Interpolation).
  //     "booster": "No"                 → Which Section 11 adjustment(s) are applied to the predicted score:
  //                                      • "No"                    = No booster applied (value = scores.predicted).
  //                                      • "Section #"             = Single booster (e.g., "11.1").
  //                                      • "Section # + Section #" = Multiple boosters applied in sequence (e.g., "11.1 + 11.2").
  //     "confidence": "N/A"             → Always "N/A" for Predictor methods.
  //   }
  // ─────────────────────────────────────────────────────────────────────────────
  
  // GUIDELINE (meta): Tracks the state of this document itself. Update both fields every time you modify this file.
  "meta": {
    "schema_version": "6.8",
    // GUIDELINE: Version of the data structure schema. Increment only when a structural change is made (new fields added, renamed, or removed). Use semantic versioning (Major.Minor).
    "last_updated": "2026-08-24"
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
    "target_region": {
      "value": "Global",
      "source": "TBD",
      "exact_extract": "Proof pending"
      // GUIDELINE: The target region/market of this specific hardware SKU under review. Allowed values: "Global", "US" (United States), "China" (includes Hong Kong and Macau), "EU" (European Union), "CA" (Canada), or "Other". Use this field in Section 7.2 to resolve regional hardware variations.
    },
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
        // GUIDELINE: System-on-Chip (SoC) name as marketed (e.g. "Snapdragon 8 Gen 3", "Apple A18 Pro", "Exynos 2400"). Include the brand prefix. Use the variant that matches the region/carrier of this record. VERY IMPORTANT: Verify that the name is present in the SoC reference tables listed in references/soc_reference.md. If it is not present, then add a line to the matching table with a mention "To be completed" and raise an alert.  
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
          //   • "Stainless Steel"                      → 9.10  (316L, 304, Surgical Grade Steel)
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
          //   6. METAL RESOLUTION (GENERIC): Marketing terms like "Metal", "Aluminum", "Metal Unibody", or "Metal Panel" MUST default to "Die-Cast Aluminum (ADC12)". Any explicit mention of "Steel", "Stainless Steel", or "Surgical Grade" MUST be categorized as "Stainless Steel".
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
    "1_4_ergonomics": {
      // SCORING GOAL: Evaluates device physical handling comfort using thickness (depth) and width (one-handed usability). Thickness scores device thickness in millimeters (mm) as a measure of pocketability and hand comfort. Width scores device width as a measure of one-handed ergonomics; beyond a critical threshold, phones become difficult to grip and operate single-handedly.
      "thickness_mm": {
        "value": 8.6,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 4.36
        // SCORING GUIDELINE: Score = 10 * (Thickness_mm_Max − value) / (Thickness_mm_Max − Thickness_mm_Min), clamped 0–10.
      },
      "width_mm": {
        "value": 79.0,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.00
        // SCORING GUIDELINE: Score = 10 * (1 − ((value − Width_mm_Min) / (Width_mm_Max − Width_mm_Min))²), clamped 0–10.
      },
      "scores": {
        "predicted": 2.18,
        // SCORING GUIDELINE: Score = (0.5 * thickness_mm.subscore) + (0.5 * width_mm.subscore).
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 2.18,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "1_5_weight_g": {
      // SCORING GOAL: Scores total device weight in grams as a measure of long-term holding comfort. Lighter phones cause less wrist and arm fatigue during extended use.
      "value": 232,
      "source": "TBD",
      "exact_extract": "Proof pending",
      "scores": {
        "predicted": 2.33,
        // SCORING GUIDELINE: Score = 10 * (Weight_g_Max − value) / (Weight_g_Max − Weight_g_Min), clamped 0–10.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 2.33,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    }
  },
  "2_display": {
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
        // with diagonal_inches = 2_9_screen_size_diagonal_inches.value and in that case set "source" to "Derived from resolution_width_px, resolution_height_px, and diagonal_inches" and set "exact_extract" to "N/A".
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
    "2_9_screen_size_diagonal_inches": {
      // SCORING GOAL: Scores the physical display diagonal in inches as a measure of immersion and media consumption experience. Larger screens offer more real estate for video, gaming, and productivity.
      "value": 6.8,
      "source": "TBD",
      "exact_extract": "Proof pending",
      "scores": {
        "predicted": 6.93,
        // SCORING GUIDELINE: Score = 10 * ((value^2 − Display_Size_Inch_Min^2) / (Display_Size_Inch_Max^2 − Display_Size_Inch_Min^2)), clamped 0–10.
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
          //   • Predictor              → Method C (parametric spec calculation)
          "booster": "No",
          // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
          "confidence": "N/A"
          // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
        }
      }
    },
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
        // GUIDELINE: end_of_support_date.value = Max(os_end_date.value, security_end_date.value).
      },
      "scores": {
        "predicted": "[DYNAMIC_CALCULATION]", // to be updated continuously, score varies every day.
        // GUIDELINE: 
        //   1. Determine Remaining_Years: end_of_support_date.value - Current_Date where Current_Date is the current date expressed in YYYY-MM-DD format.
        //   2. Calculate the score: 10 * (log(Remaining_Years) - log(Support_Years_Min)) / (log(Support_Years_Max) - log(Support_Years_Min)), clamped 0-10.
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": "[DYNAMIC_CALCULATION]", // to be updated continuously, score varies every day.
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "5_2_system_cleanliness_control": {
      // SCORING GOAL: Evaluates the out-of-box software experience by analyzing Preinstalled App Load (PAL), User Control (UC), and System Advertisements (SA).
      "skin": {
        "value": "Samsung One UI",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "alert": "N/A"
        // DATA GUIDELINE: Record the software skin / platform name. The value MUST exactly match one of the entries in the `SKIN_LOOKUP_TABLE` below to enable automated mapping.
        // For regional builds (e.g., Chinese Read-Only Memory (ROM) vs. European Union (EU) ROM vs. Global ROM builds), the cleanliness scores can differ significantly from the consumer baseline.
        // If a specific regional build deviates from the baseline in the lookup table (for example, a Chinese build having pre-installed apps or advertisements not present in the Global build),
        // then the scores can be adjusted accordingly. In that case the field "alert" must justify the overrides with verified references (valid URLs). If no override, set the field "alert" to "N/A".
        //
        // █ SKIN_LOOKUP_TABLE:
        // | Platform / Skin              | preinstalled_app_load_score (40%) | user_control_score (30%) | system_ads_score (30%) | *Composite* |
        // | :--------------------------- | :-------------------------------: | :----------------------: | :--------------------: | :---------: |
        // | **iOS**                      | **10.0**                          | **10.0**                 | **10.0**               | *10.00*     |
        // | **Pixel UI**                 | **10.0**                          | **10.0**                 | **10.0**               | *10.00*     |
        // | **Stock Android**            | **10.0**                          | **10.0**                 | **10.0**               | *10.00*     |
        // | **AOSP**                     | **10.0**                          | **10.0**                 | **10.0**               | *10.00*     |
        // | **Fairphone OS**             | **10.0**                          | **10.0**                 | **10.0**               | *10.00*     |
        // | **Nothing OS**               | **10.0**                          | **10.0**                 | **10.0**               | *10.00*     |
        // | **Motorola MyUX**            | **6.0**                           | **10.0**                 | **10.0**               | *8.40*      |
        // | **Motorola Hello UI**        | **6.0**                           | **10.0**                 | **10.0**               | *8.40*      |
        // | **Sony Xperia UI**           | **6.0**                           | **10.0**                 | **10.0**               | *8.40*      |
        // | **Sharp AQUOS UI**           | **6.0**                           | **10.0**                 | **10.0**               | *8.40*      |
        // | **Nokia UI**                 | **6.0**                           | **10.0**                 | **10.0**               | *8.40*      |
        // | **ASUS ZenUI**               | **6.0**                           | **10.0**                 | **10.0**               | *8.40*      |
        // | **ROG UI**                   | **6.0**                           | **10.0**                 | **10.0**               | *8.40*      |
        // | **Redmagic OS**              | **3.0**                           | **10.0**                 | **10.0**               | *7.20*      |
        // | **Funtouch OS**              | **6.0**                           | **5.0**                  | **10.0**               | *6.90*      |
        // | **LG UX**                    | **6.0**                           | **5.0**                  | **5.0**                | *5.40*      |
        // | **HTC Sense**                | **6.0**                           | **5.0**                  | **5.0**                | *5.40*      |
        // | **OxygenOS**                 | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **Samsung One UI**           | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **ColorOS**                  | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **Realme UI**                | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **OriginOS**                 | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **Vivo UI**                  | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **Honor MagicOS**            | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **ZTE MiFavor UI**           | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **ZTE MyOS**                 | **3.0**                           | **5.0**                  | **5.0**                | *4.20*      |
        // | **HyperOS**                  | **0.0**                           | **5.0**                  | **0.0**                | *1.50*      |
        // | **Huawei EMUI**              | **0.0**                           | **5.0**                  | **0.0**                | *1.50*      |
        // | **MIUI**                     | **0.0**                           | **0.0**                  | **0.0**                | *0.00*      |
        // | **Tecno HiOS**               | **0.0**                           | **0.0**                  | **0.0**                | *0.00*      |
        // | **Infinix XOS**              | **0.0**                           | **0.0**                  | **0.0**                | *0.00*      |
        // | **Itel OS**                  | **0.0**                           | **0.0**                  | **0.0**                | *0.00*      |
      },
      "cleanliness_scores": {
        "identifier": "Samsung One UI",
        "identifier_path": "5_2_system_cleanliness_control.skin.value",
        "reference_table": "SKIN_LOOKUP_TABLE",
        "preinstalled_app_load_score": 3.00,
        "user_control_score": 5.00,
        "system_ads_score": 5.00
        // GUIDELINE: Values retrieved from the `reference_table` by matching the `identifier`.
      },
      "scores": {
        "predicted": 4.20,
        "calculation_formula": "(0.40 * cleanliness_scores.preinstalled_app_load_score) + (0.30 * cleanliness_scores.user_control_score) + (0.30 * cleanliness_scores.system_ads_score)",
        // SCORING GUIDELINE: scores.predicted = weighted sum of the 3 cleanliness scores. Alternatively, use the *Composite* score from the SKIN_LOOKUP_TABLE directly.
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
    // Defines CAS (Core Architecture Score) and Ref Freq (Reference Frequency in Gigahertz [GHz]).
    // 
    // SCORING RATIONALE (Linear IPC): The CAS (Core Architecture Score) values in this table are linear performance scores representing relative IPC (Instructions Per Cycle) capabilities, anchored to a 10.00 ceiling for top-tier modern cores (Oryon Gen 2 / Apple Everest). 
    // • WHY LINEAR? The scores must remain linear to ensure mathematically valid multi-core scaling in Step 3, where cluster effective throughputs are summed to compute the aggregate RCTS (Raw CPU Throughput Score). 
    // • AVOID DOUBLE LOGARITHMS: Because the global logarithmic normalization to map human perception (Weber-Fechner Law) is performed later in Step 4, keeping these base architecture scores strictly linear prevents a mathematically incorrect "double logarithmic" compression, which would otherwise flatten the final scoring spectrum and penalize high-performance flagships.
    // • MATH FLOOR: A floor of ~0.5 is enforced for legacy/efficiency cores strictly to prevent errors during subsequent logarithmic normalization in Step 4.
    // • TYPICAL L2 KB: The standardized Level 2 cache capacity assigned to this specific core architecture across the majority of SoC implementations. This is used strictly by the Single-Core Method C penalty module. 
    // • ISA GEN: The Instruction Set Architecture generation of the core. Used to apply a hardware efficiency multiplier.
    // • ISA GEN SCORE: The numerical multiplier assigned to the specific ISA generation, representing its physical hardware efficiency.
    // • INFERRED FIELDS: The `reference_frequency_ghz`, `typical_l2_kb`, and internal core codenames act as internal mathematical normalization anchors for the model's baseline framework, not universally authoritative public vendor specifications.
    // 
    // ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    // │ PERFORMANCE / PRIME CORES — Flagship tier (highest IPC, used in prime and high-performance clusters)             │
    // └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    // | CPU Core Architecture        | core_architecture_score | reference_frequency_ghz  | typical_l2_kb |  isa_gen  | isa_gen_score | idle_efficiency_score |
    // |:-----------------------------|:-----------------------:|:------------------------:|:-------------:|:---------:|:-------------:|:---------------------:|
    // | C1-Ultra (Lumex)             |          10.00          |           4.21           |      2048     |  ARMv9.3  |      1.10     |          0.30         |
    // | Apple Everest (A18/Pro)      |          10.00          |           4.05           |     16384     |  ARMv9.2  |      1.08     |          1.30         |
    // | Oryon Gen 2                  |           9.80          |           4.32           |     12288     |  ARMv8.7  |      1.05     |          1.00         |
    // | Apple A17 Pro Cores          |           9.10          |           3.78           |     16384     |  ARMv8.6  |      1.04     |          1.10         |
    // | Cortex-X925                  |           9.00          |           3.60           |      3072     |  ARMv9.2  |      1.08     |          0.80         |
    // | C1-Premium (Lumex)           |           8.45          |           3.50           |      1024     |  ARMv9.3  |      1.10     |          0.60         |
    // | Apple A16 Bionic             |           8.25          |           3.46           |     16384     |  ARMv8.6  |      1.04     |          0.90         |
    // | Cortex-X4                    |           7.95          |           3.30           |      2048     |  ARMv9.2  |      1.08     |          0.50         |
    // | Apple A15 Bionic             |           7.30          |           3.22           |     12288     |  ARMv8.6  |      1.04     |          0.80         |
    // | Cortex-X3                    |           7.15          |           3.20           |      1024     |  ARMv9.0  |      1.06     |          0.30         |
    // | Apple A14 Bionic             |           6.70          |           3.10           |      8192     |  ARMv8.4  |      1.02     |          0.60         |
    // | Cortex-X2                    |           6.40          |           3.00           |      1024     |  ARMv9.0  |      1.06     |          0.10         |
    // | Apple A13 Lightning          |           5.80          |           2.65           |      8192     |  ARMv8.4  |      1.02     |          0.40         |
    // | Cortex-X1                    |           5.60          |           2.84           |      1024     |  ARMv8.2  |      1.00     |          0.00         |
    // | Apple A12 Vortex             |           4.95          |           2.49           |      8192     |  ARMv8.3  |      1.01     |          0.30         |
    // | Apple A11 Monsoon            |           4.15          |           2.39           |      8192     |  ARMv8.2  |      1.00     |          0.20         |
    // | Qualcomm Kryo 585            |           3.60          |           2.84           |       512     |  ARMv8.2  |      1.00     |          2.30         |
    // | Exynos M5 (Lion)             |           3.30          |           2.73           |       512     |  ARMv8.2  |      1.00     |          1.30         |
    // | Qualcomm Kryo 485            |           3.00          |           2.84           |       512     |  ARMv8.2  |      1.00     |          2.60         |
    // | Apple A10 Hurricane          |           2.90          |           2.34           |      3072     |  ARMv8.1  |      0.97     |          0.10         |
    // | Exynos M4 (Cheetah)          |           2.65          |           2.73           |       512     |  ARMv8.2  |      1.00     |          1.00         |
    // | Qualcomm Kryo 385            |           2.30          |           2.80           |      2048     |  ARMv8.2  |      1.00     |          2.00         |
    // | Exynos M3 (Meerkat)          |           2.20          |           2.70           |       512     |  ARMv8.0  |      0.96     |          0.80         |
    // | Qualcomm Kryo 280            |           1.90          |           2.45           |      2048     |  ARMv8.0  |      0.96     |          1.80         |
    // | Exynos M2                    |           1.80          |           2.30           |      2048     |  ARMv8.0  |      0.96     |          0.60         |
    // | Exynos M1 (Mongoose)         |           1.70          |           2.30           |      2048     |  ARMv8.0  |      0.96     |          0.30         |
    // | Qualcomm Kryo (2.40 GHz)     |           1.76          |           2.40           |      1024     |  ARMv8.0  |      0.96     |          1.40         |
    // | Qualcomm Kryo (2.15 GHz)     |           1.60          |           2.15           |      1024     |  ARMv8.0  |      0.96     |          1.30         |
    // |------------------------------+-------------------------+--------------------------+---------------+-----------+---------------+-----------------------|
    // ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    // │ PERFORMANCE / MID CORES — Used in performance clusters (high IPC but lower than prime cores)                     │
    // └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    // | CPU Core Architecture        | core_architecture_score | reference_frequency_ghz  | typical_l2_kb |  isa_gen  | isa_gen_score | idle_efficiency_score |
    // |:-----------------------------|:-----------------------:|:------------------------:|:-------------:|:---------:|:-------------:|:---------------------:|
    // | C1-Pro (Lumex)               |           5.35          |           2.70           |       512     |  ARMv9.3  |      1.10     |          5.20         |
    // | Cortex-A725                  |           5.25          |           2.80           |       512     |  ARMv9.2  |      1.08     |          5.00         |
    // | Cortex-A720                  |           5.00          |           2.80           |       512     |  ARMv9.2  |      1.08     |          4.80         |
    // | Cortex-A715                  |           4.40          |           2.50           |       512     |  ARMv9.0  |      1.06     |          4.50         |
    // | Cortex-A710                  |           4.15          |           2.50           |       512     |  ARMv9.0  |      1.06     |          4.20         |
    // | Cortex-A78                   |           3.80          |           2.40           |       512     |  ARMv8.2  |      1.00     |          4.00         |
    // | Cortex-A77                   |           3.55          |           2.40           |       512     |  ARMv8.2  |      1.00     |          3.50         |
    // | Cortex-A76                   |           2.90          |           2.20           |       512     |  ARMv8.2  |      1.00     |          3.00         |
    // | Cortex-A75                   |           2.20          |           2.00           |       512     |  ARMv8.2  |      1.00     |          2.50         |
    // | Cortex-A73                   |           1.80          |           2.00           |      1024     |  ARMv8.0  |      0.96     |          2.00         |
    // | Cortex-A72                   |           1.60          |           2.50           |      1024     |  ARMv8.0  |      0.96     |          1.50         |
    // | Cortex-A57                   |           1.45          |           2.00           |      2048     |  ARMv8.0  |      0.96     |          1.00         |
    // |------------------------------+-------------------------+--------------------------+---------------+-----------+---------------|
    // ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    // │ EFFICIENCY CORES — ARM standard efficiency cores (low IPC, optimized for power savings)                          │
    // └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    // | CPU Core Architecture        | core_architecture_score | reference_frequency_ghz  | typical_l2_kb |  isa_gen  | isa_gen_score | idle_efficiency_score |
    // |:-----------------------------|:-----------------------:|:------------------------:|:-------------:|:---------:|:-------------:|:---------------------:|
    // | C1-Nano (Lumex)              |           1.00          |           2.00           |       128     |  ARMv9.3  |      1.10     |         10.00         |
    // | Cortex-A525                  |           1.00          |           2.00           |       128     |  ARMv9.2  |      1.08     |         10.00         |
    // | Cortex-A520                  |           1.00          |           2.00           |       128     |  ARMv9.2  |      1.08     |         10.00         |
    // | Cortex-A510                  |           1.00          |           2.00           |       128     |  ARMv9.0  |      1.06     |         10.00         |
    // | Cortex-A55                   |           0.60          |           1.80           |       128     |  ARMv8.2  |      1.00     |          8.00         |
    // | Cortex-A53                   |           0.50          |           1.80           |       512     |  ARMv8.0  |      0.96     |          7.00         |
    // | Cortex-A35                   |           0.45          |           1.50           |       512     |  ARMv8.0  |      0.96     |          8.00         |
    // |------------------------------+-------------------------+--------------------------+---------------+-----------+---------------|
    // ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    // │ APPLE EFFICIENCY CORES — Apple custom efficiency cores (used in the efficiency cluster of Apple SoCs)            │
    // │ NOTE: Apple efficiency cores differ substantially from their performance counterparts in IPC and pipeline        │
    // │ width. They MUST be listed separately to ensure correct multi-core throughput calculations for all iPhones.      │
    // └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    // | CPU Core Architecture        | core_architecture_score | reference_frequency_ghz  | typical_l2_kb |  isa_gen  | isa_gen_score | idle_efficiency_score |
    // |:-----------------------------|:-----------------------:|:------------------------:|:-------------:|:---------:|:-------------:|:---------------------:|
    // | Apple A18 E-core (Sawtooth)  |           1.00          |           2.42           |      4096     |  ARMv9.2  |      1.08     |         10.00         |
    // | Apple A17 Pro E-core         |           1.00          |           2.11           |      4096     |  ARMv8.6  |      1.04     |         10.00         |
    // | Apple A16 E-core (Sawtooth)  |           1.00          |           2.02           |      4096     |  ARMv8.6  |      1.04     |         10.00         |
    // | Apple A15 E-core (Blizzard)  |           1.00          |           2.02           |      4096     |  ARMv8.6  |      1.04     |         10.00         |
    // | Apple A14 E-core (Icestorm)  |           0.80          |           1.80           |      4096     |  ARMv8.4  |      1.02     |          9.50         |
    // | Apple A13 E-core (Thunder)   |           0.80          |           1.80           |      4096     |  ARMv8.4  |      1.02     |          9.00         |
    // | Apple A12 E-core (Tempest)   |           0.60          |           1.60           |      2048     |  ARMv8.3  |      1.01     |          8.50         |
    // | Apple A11 E-core (Mistral)   |           0.55          |           1.42           |      1024     |  ARMv8.2  |      1.00     |          8.00         |
    // | Apple A10 E-core (Zephyr)    |           0.45          |           1.05           |      3072     |  ARMv8.1  |      0.97     |          7.00         |
    // |------------------------------+-------------------------+--------------------------+---------------+-----------+---------------|
    // ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
    // │ LEGACY APPLE PERFORMANCE CORES — Pre-2016 borderline entries retained for completeness                           │
    // └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
    // | CPU Core Architecture        | core_architecture_score | reference_frequency_ghz  | typical_l2_kb |  isa_gen  | isa_gen_score | idle_efficiency_score |
    // |:-----------------------------|:-----------------------:|:------------------------:|:-------------:|:---------:|:-------------:|:---------------------:|
    // | Apple A9 (Twister)           |           0.50          |           1.85           |      3072     |  ARMv8.0  |      0.96     |          4.00         |
    // ---------------------------------------------------------------------------------------------------------------------------------------

    "6_1_0_system_on_chip_reference": {
      // SCORING GOAL: Serves as the authoritative hardware reference for the SoC (System on Chip) architecture, including core counts and architectural types.
      "value": "Snapdragon 8 Gen 3",
      // GUIDELINE: Inherits the chipset model name from the device identity record.
      "value_path": "identity.hardware_configuration.chipset.value",
      // GUIDELINE: Absolute path to the chipset identifier in the device identity section.
      "clusters": {
        // GUIDELINE: The cluster structure is FIXED with 4 named keys to cover all modern SoC architectures. Do NOT add or remove keys. If a SoC uses fewer than 4 clusters, set all fields in the unused keys to "N/A". Clusters MUST be strictly ordered from strongest ("best") to weakest ("fourth_best") according to their physical capability. The primary sorting criterion is the core_architecture_score (CAS) of the core architecture from the CPU_CORE_ARCHITECTURE_LOOKUP_TABLE. If two clusters have the exact same core_architecture_score, they must be ordered by their ratio of actual to reference frequency (higher ratio ordered first). Any unused clusters (which are set to "N/A") must be placed at the end of the ordering (e.g., in the "third_best" and "fourth_best" keys).
        "best": {
          "architecture": "Cortex-X4",
          // GUIDELINE: The specific CPU core architecture name. The value MUST exactly match one of the entries in the `CPU_CORE_ARCHITECTURE_LOOKUP_TABLE` above to enable mapping (e.g., "Cortex-X4"). VERY IMPORTANT: The "best" cluster is characterized by having the highest computational throughput, hence among the different clusters of the SoC this cluster MUST always be the one with the highest core_architecture_score.
          "count": 1,
          // GUIDELINE: The number of cores contained in this specific cluster.
          "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
          // GUIDELINE: Direct source URL for architectural data (type and count).
          "exact_extract": "Cortex-X4"
          // GUIDELINE: The verbatim proof from the source confirming architecture type and core count.
        },
        "second_best": {
          "architecture": "Cortex-A720",
          "count": 5,
          "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
          "exact_extract": "Cortex-A720"
        },
        "third_best": {
          "architecture": "Cortex-A520",
          "count": 2,
          "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
          "exact_extract": "Cortex-A520"
        },
        "fourth_best": {
          "architecture": "N/A",
          "count": "N/A",
          "source": "N/A",
          "exact_extract": "N/A"
        }
      }
    },
    "6_1_cpu_multi_core_performance": {
      // SCORING GOAL: Measures the actual delivered CPU performance during intense, multi-threaded workloads to ensure the device can handle heavy multitasking, gaming physics, and background processing. A three-method hierarchy (A→B→C) is used. Method A uses the Geekbench 6 Multi-Core benchmark when available. Method B uses Nearest Neighbor Interpolation when only similar devices have benchmarks. Method C (Predictor) is the fallback predicted score based on physical core scaling parameters.
      
      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD A — Direct Benchmark (Primary)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_a_benchmark_CPU_multi": {
        "value": 7200,
        "source": "https://browser.geekbench.com/android-benchmarks",
        "exact_extract": "Samsung Galaxy S24 Ultra [...] 7200",
        "subscore": 9.11
        // SCORING GUIDELINE: Primary benchmark is Geekbench 6 (GB6) Multi-Core.
        // • WHERE TO FIND IT: Query browser.geekbench.com for the host SoC (System on Chip) or exact device model.
        // • EXTRACTION RULE: Use the "Multi-Core Score" from the "Android" or "iOS" category. Verify version is 6.x. Do NOT use v4/v5 or Single-Core scores.
        // SCORING GUIDELINE: subscore = 10 * (log(method_a_benchmark_CPU_multi.value) − log(CPU_GB6_Multi_Score_Min)) / (log(CPU_GB6_Multi_Score_Max) − log(CPU_GB6_Multi_Score_Min)), clamped 0–10. If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD C — Throughput Prediction Model (Tertiary / baseline for Method B)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_c_prediction_model_CPU_multi": {
        // SCORING GOAL: Predicts the CPU (Central Processing Unit) Multi-Core Performance score using the 5-Step Performance Pipeline. The model accounts for core-frequency soft-saturation, local intra-cluster scaling, Raw CPU Throughput Score (RCTS) aggregation, global logarithmic normalization, and dynamic non-linear deficit penalties from adjacent physical subsystems.
        // GUIDELINE: The number of cluster objects is FIXED at 4 to maintain structural parity with Section 6.1.0 SoC (System on Chip) Reference. Do NOT add or remove blocks. If a SoC uses fewer than 4 clusters (e.g., 2 for Apple, 3 for most Snapdragon), then for the remaining unused cluster block(s):
        // - leave the fields containing internal paths or calculation formula unchanged ("identifier_path", "reference_table", "value_path", "calculation_formula") as these always remain valid
        // - set the Cluster Effective Throughput (cluster_effective_throughput.value) to 0
        // - set all remaining fields to "N/A"
        "clusters": {
          "best": {
            "architecture_mapping": {
              "identifier": "Cortex-X4",
              "identifier_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.best.architecture",
              "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
              "core_architecture_score": 7.95,
              // GUIDELINE: Performance score from the lookup table representing IPC (Instructions Per Cycle) capability.
              "reference_frequency_ghz": 3.30
              // GUIDELINE: Reference frequency in GHz (Gigahertz) from the lookup table.
            },
            "core_count": {
              "value": 1,
              "value_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.best.count"
              // GUIDELINE: Number of physical CPU cores in this specific cluster.
            },
            "actual_frequency_ghz": {
              "value": 3.3,
              "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
              "exact_extract": "1x 3.3 GHz"
              // GUIDELINE: The maximum advertised frequency for this specific core cluster in GHz.
            },
            "soft_saturation_exponent": {
              "value": 0.93,
              "calculation_formula": "gamma = Look up based on cluster core count (best.core_count.value): 1 core = 0.93, 2 = 0.95, 3 = 0.96, 4 = 0.97, 5-6 = 0.98, 7 or more = 0.99"
              // GUIDELINE: Saturation factor (gamma) modeling frequency scaling dimishing returns.
            },
            "core_yield": {
              "value": 7.9500,
              "calculation_formula": "best.architecture_mapping.core_architecture_score * ((best.actual_frequency_ghz.value / best.architecture_mapping.reference_frequency_ghz) ^ best.soft_saturation_exponent.value)"
              // GUIDELINE: Yield = CAS (Core Architecture Score) * ((Actual Freq / Ref Freq) ^ gamma). Models frequency scaling soft-saturation. Keep 4 decimal places.
            },
            "pacc_decay_exponent": {
              "value": 1.0000,
              "calculation_formula": "Look up based on cluster core count (best.core_count.value): 1 core = 1, 2 = 0.94, 3 = 0.90, 4 = 0.87, 5 = 0.85, 6 = 0.83, 7 = 0.81, 8 = 0.80"
              // GUIDELINE: Cluster scaling exponent (alpha) modeling thread communication and resource contention decay.
            },
            "parallel_adjusted_core_count": {
              "value": 1.0000,
              "calculation_formula": "best.core_count.value ^ best.pacc_decay_exponent.value"
              // GUIDELINE: Models cluster multi-thread capability.
            },
            "cluster_effective_throughput": {
              "value": 7.9500,
              "calculation_formula": "best.core_yield.value * best.parallel_adjusted_core_count.value"
              // GUIDELINE: Cluster Effective Throughput = Core Yield * Parallel-Adjusted Core Count. Total multi-core contribution of this cluster. Keep 4 decimal places.
            }
          },
          "second_best": {
            "architecture_mapping": {
              "identifier": "Cortex-A720",
              "identifier_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.second_best.architecture",
              "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
              "core_architecture_score": 5.00,
              "reference_frequency_ghz": 2.80
            },
            "core_count": {
              "value": 5,
              "value_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.second_best.count"
            },
            "actual_frequency_ghz": {
              "value": 3.2,
              "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
              "exact_extract": "5x 3.2 GHz"
              // GUIDELINE: The maximum advertised frequency for this specific core cluster in GHz.
            },
            "soft_saturation_exponent": {
              "value": 0.98,
              "calculation_formula": "gamma = Look up based on cluster core count (second_best.core_count.value): 1 core = 0.93, 2 = 0.95, 3 = 0.96, 4 = 0.97, 5-6 = 0.98, 7 or more = 0.99"
            },
            "core_yield": {
              "value": 5.6990,
              "calculation_formula": "second_best.architecture_mapping.core_architecture_score * ((second_best.actual_frequency_ghz.value / second_best.architecture_mapping.reference_frequency_ghz) ^ second_best.soft_saturation_exponent.value)"
            },
            "pacc_decay_exponent": {
              "value": 0.85,
              "calculation_formula": "Look up based on cluster core count (second_best.core_count.value): 1 core = 1, 2 = 0.94, 3 = 0.90, 4 = 0.87, 5 = 0.85, 6 = 0.83, 7 = 0.81, 8 = 0.80"
            },
            "parallel_adjusted_core_count": {
              "value": 3.9276,
              "calculation_formula": "second_best.core_count.value ^ second_best.pacc_decay_exponent.value"
            },
            "cluster_effective_throughput": {
              "value": 22.3834,
              "calculation_formula": "second_best.core_yield.value * second_best.parallel_adjusted_core_count.value"
            }
          },
          "third_best": {
            "architecture_mapping": {
              "identifier": "Cortex-A520",
              "identifier_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.third_best.architecture",
              "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
              "core_architecture_score": 1.00,
              "reference_frequency_ghz": 2.00
            },
            "core_count": {
              "value": 2,
              "value_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.third_best.count"
            },
            "actual_frequency_ghz": {
              "value": 2.3,
              "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
              "exact_extract": "2x 2.3 GHz"
              // GUIDELINE: The maximum advertised frequency for this specific core cluster in GHz.
            },
            "soft_saturation_exponent": {
              "value": 0.95,
              "calculation_formula": "gamma = Look up based on cluster core count (third_best.core_count.value): 1 core = 0.93, 2 = 0.95, 3 = 0.96, 4 = 0.97, 5-6 = 0.98, 7 or more = 0.99"
            },
            "core_yield": {
              "value": 1.1420,
              "calculation_formula": "third_best.architecture_mapping.core_architecture_score * ((third_best.actual_frequency_ghz.value / third_best.architecture_mapping.reference_frequency_ghz) ^ third_best.soft_saturation_exponent.value)"
            },
            "pacc_decay_exponent": {
              "value": 0.94,
              "calculation_formula": "Look up based on cluster core count (third_best.core_count.value): 1 core = 1, 2 = 0.94, 3 = 0.90, 4 = 0.87, 5 = 0.85, 6 = 0.83, 7 = 0.81, 8 = 0.80"
            },
            "parallel_adjusted_core_count": {
              "value": 1.9185,
              "calculation_formula": "third_best.core_count.value ^ third_best.pacc_decay_exponent.value"
            },
            "cluster_effective_throughput": {
              "value": 2.1909,
              "calculation_formula": "third_best.core_yield.value * third_best.parallel_adjusted_core_count.value"
            }
          },    
          "fourth_best": {
            "architecture_mapping": {
              "identifier": "N/A",
              "identifier_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.fourth_best.architecture",
              "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
              "core_architecture_score": "N/A",
              "reference_frequency_ghz": "N/A"
            },
            "core_count": {
              "value": "N/A",
              "value_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.fourth_best.count"
            },
            "actual_frequency_ghz": {
              "value": "N/A",
              "source": "N/A",
              "exact_extract": "N/A"
              // GUIDELINE: The maximum advertised frequency for this specific core cluster in GHz.
            },
            "soft_saturation_exponent": {
              "value": "N/A",
              "calculation_formula": "gamma = Look up based on cluster core count (fourth_best.core_count.value): 1 core = 0.93, 2 = 0.95, 3 = 0.96, 4 = 0.97, 5-6 = 0.98, 7 or more = 0.99"
            },
            "core_yield": {
              "value": "N/A",
              "calculation_formula": "fourth_best.architecture_mapping.core_architecture_score * ((fourth_best.actual_frequency_ghz.value / fourth_best.architecture_mapping.reference_frequency_ghz) ^ fourth_best.soft_saturation_exponent.value)"
            },
            "pacc_decay_exponent": {
              "value": "N/A",
              "calculation_formula": "Look up based on cluster core count (fourth_best.core_count.value): 1 core = 1, 2 = 0.94, 3 = 0.90, 4 = 0.87, 5 = 0.85, 6 = 0.83, 7 = 0.81, 8 = 0.80"
            },
            "parallel_adjusted_core_count": {
              "value": "N/A",
              "calculation_formula": "fourth_best.core_count.value ^ fourth_best.pacc_decay_exponent.value"
            },
            "cluster_effective_throughput": {
              "value": 0.0000,
              "calculation_formula": "fourth_best.core_yield.value * fourth_best.parallel_adjusted_core_count.value"
            }
          }
        },
        "raw_performance_throughput_score": {
          "value": 32.5243,
          "calculation_formula": "clusters.best.cluster_effective_throughput.value + clusters.second_best.cluster_effective_throughput.value + clusters.third_best.cluster_effective_throughput.value + clusters.fourth_best.cluster_effective_throughput.value"
          // GUIDELINE: RCTS (Raw CPU Throughput Score) = Sum of all Cluster Effective Throughputs (CET). Keep 4 decimal places.
        },
        "normalized_throughput_score": {
          "value": 8.8379,
          "calculation_formula": "10.0 * (log(raw_performance_throughput_score.value) - log(CPU_RCTS_Min)) / (log(CPU_RCTS_Max) - log(CPU_RCTS_Min)), clamped [0.0, 10.0]."
        },
        "memory_subsystem_penalty": {
          "deficit": {
            "value": 0.0145,
            "calculation_formula": "max(0, normalized_throughput_score.value - 6_processing_power_and_performance.6_5_ram_technology.scores.predicted)" 
          },
          "penalty": {
            "value": 0.0002,
            "calculation_formula": "0.09 * (memory_subsystem_penalty.deficit.value ^ 1.4)"
            // GUIDELINE: Memory bandwidth starvation penalty. The Memory Support Score inherits the Section 6.5 predicted score. Penalty = 0.09 * (Deficit ^ 1.4). Keep 4 decimal places.
          },
        },
        "thermal_subsystem_penalty": {
          "deficit": {
            "value": 4.5979,
            "calculation_formula": "max(0, normalized_throughput_score.value - 6_processing_power_and_performance.6_10_thermal_dissipation_stability.scores.final.value)"
          },
          "penalty": {
            "value": 0.1269,
            "calculation_formula": "0.015 * (thermal_subsystem_penalty.deficit.value ^ 1.4)"
            // GUIDELINE: Thermodynamic throttling penalty. TDSI (Thermal Dissipation Stability Index) inherits the Section 6.10 final score. Penalty = 0.015 * (Deficit ^ 1.4). Keep 4 decimal places.
          },
        },
        "cache_subsystem_penalty": {
          "identifier": "Snapdragon 8 Gen 3",
          "identifier_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.value",
          "reference_table": "references/soc_reference.md",
          "shared_cache_mb": 18.0,
          // GUIDELINE: The sum of Level 3 (L3) and System Level Cache (SLC) capacity fetched from references/soc_reference.md.
          "CFEI": {
            "value": 8.6165,
            "calculation_formula": "10.0 * (log(shared_cache_mb) - log(CPU_CFEI_Min)) / (log(CPU_CFEI_Max) - log(CPU_CFEI_Min)) - interconnect_latency_penalty"
            // GUIDELINE: CFEI (Cache & Fabric Efficiency Index) is calculated continuously using a logarithmic formula from the effective shared cache, minus interconnect_latency_penalty. This penalty is defined as 0.5 for the Snapdragon 8 Elite and 0 for all other cases. Keep 4 decimal places.
            // SPECIAL RULES:
            // 1. For Snapdragon 8 Elite, CFEI capacity is combined: 24 MB L2 + 8 MB SLC = 32 MB. A flat penalty of -0.5 is applied directly to the calculated score due to split cluster coherency latency.
            // 2. If the SoC has no cache data (indicated by '?' or is missing), set CFEI value to 'N/A' and set deficit to 0 and penalty to 0 (no penalty).
          },
          "deficit": {
            "value": 0.2214,
            "calculation_formula": "max(0, normalized_throughput_score.value - cache_subsystem_penalty.CFEI.value)"
          },
          "penalty": {
            "value": 0.0028,
            "calculation_formula": "0.02 * (cache_subsystem_penalty.deficit.value ^ 1.3)"
            // GUIDELINE: Cache Penalty = 0.02 * (Deficit ^ 1.3). Keep 4 decimal places.
          },
        }, 
        "predicted_score": 8.71,
        "calculation_formula": "normalized_throughput_score.value - (memory_subsystem_penalty.penalty.value + thermal_subsystem_penalty.penalty.value + cache_subsystem_penalty.penalty.value)"
        // SCORING GUIDELINE: The final predicted performance score is computed by adjusting the raw normalized throughput score through the subtraction of the active dynamic penalties from the memory, thermal and cache supporting subsystems.
        // BOUNDS CHECK ABORT PROCEDURE: Under no circumstances should the system silently clamp or allow an out-of-bounds score in production. If the raw calculation predicted_score yields a value outside the physical standard range of [0.00, 10.00] (less than 0 or greater than 10), the entire scoring pipeline for the target device MUST BE ABORTED IMMEDIATELY. The system must immediately raise a high-priority exception: "CRITICAL ANOMALY ALERT: Raw multi-core CPU score ({predicted_score}) is outside physical standard bounds [0, 10]. Halting scoring process." and halt execution.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD B — Nearest Neighbor Interpolation (Secondary)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_b_neighbor_interpolation_CPU_multi": {
        // SCORING GUIDELINE: Method B is populated for ALL phones (even if Method A is available) for precision validation. Search space: all phones with a known Geekbench 6 (GB6) Multi-Core score (Method A), excluding the target device itself. The interpolation MUST use exactly 3 distinct neighbor devices.
        // Step 1 (Neighbor Selection): Find the 3 distinct candidate devices with the smallest Euclidean Distance, excluding the target device itself. Distance is calculated as:
        // Distance = Sqrt( (RCTS_norm_Diff)^2 + (Penalty_MTI_Diff)^2 + (Penalty_TDSI_Diff)^2 + (Penalty_CFEI_Diff)^2 )
        // Where the metric component differences are defined by the following precise value paths:
        // • RCTS_norm_Diff = (target.method_c_prediction_model_CPU_multi.normalized_throughput_score.value) - (neighbor.method_c_prediction_model_CPU_multi.normalized_throughput_score.value)
        // • Penalty_MTI_Diff = (target.method_c_prediction_model_CPU_multi.memory_subsystem_penalty.penalty.value) - (neighbor.method_c_prediction_model_CPU_multi.memory_subsystem_penalty.penalty.value)
        // • Penalty_TDSI_Diff = (target.method_c_prediction_model_CPU_multi.thermal_subsystem_penalty.penalty.value) - (neighbor.method_c_prediction_model_CPU_multi.thermal_subsystem_penalty.penalty.value)
        // • Penalty_CFEI_Diff = (target.method_c_prediction_model_CPU_multi.cache_subsystem_penalty.penalty.value) - (neighbor.method_c_prediction_model_CPU_multi.cache_subsystem_penalty.penalty.value)
        // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
        "neighbors": [
          {
            // Neighbor1
            "device_id_1": "xiaomi_14_ultra",
            // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
            "euclidean_distance_1": 0.2315,
            // GUIDELINE: Euclidean distance from Step 1. Keep 4 decimal places.
            "predicted_score_1": 7.94,
            // GUIDELINE: The neighbor's own Method C predicted score (overall Multi-Core).
            "benchmark_score_1": 8.60
            // GUIDELINE: The neighbor's Method A subscore.
          },
          {
            // Neighbor2
            "device_id_2": "oneplus_12",
            "euclidean_distance_2": 0.1482,
            "predicted_score_2": 7.86,
            "benchmark_score_2": 8.55
          },
          {
            // Neighbor3
            "device_id_3": "asus_rog_phone_8_pro",
            "euclidean_distance_3": 0.5230,
            "predicted_score_3": 8.32,
            "benchmark_score_3": 8.65
          }
        ],
        "avg_predicted_neighbors": 8.0400,
        // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3. Keep 4 decimal places.
        "avg_benchmark_neighbors": 8.6000,
        // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3. Keep 4 decimal places.
        "correction_ratio": 1.0833,
        // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_CPU_multi.predicted_score / avg_predicted_neighbors. Keep 4 decimal places.
        "interpolated_score": 9.32
        // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
      },

      "scores": {
        "predicted": 8.71,
        // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_CPU_multi.predicted_score.
        "final": {
          "value": 9.11,
          // SCORING GUIDELINE: Use Method A if method_a_benchmark_CPU_multi is available (method_a_benchmark_CPU_multi.subscore becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_CPU_multi.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_CPU_multi.predicted_score).
          "method_used": "Benchmark (Geekbench 6)",
          // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
          //   • Benchmark (Geekbench 6) → Method A (documented Geekbench 6 score)
          //   • Neighbor Interpolation  → Method B (similar device benchmarks)
          //   • Predictor               → Method C (spec-based performance model)
          "booster": "No",
          // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
          "confidence": "N/A"
          // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
        }
      }
    },
    "6_2_cpu_architecture_single_core": {
      // SCORING GOAL: Evaluates individual CPU (Central Processing Unit) core capability and IPC efficiency (Instructions Per Cycle—a measure of how many tasks a CPU can perform in every clock tick), representing the perceived snappiness of the UI (User Interface) and single-threaded application speed.
      
      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD A — Direct Benchmark (Primary)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_a_benchmark_CPU_single": {
        "value": 2200,
        "source": "https://browser.geekbench.com/android-benchmarks",
        "exact_extract": "Samsung Galaxy S24 Ultra [...] 2200",
        "subscore": 8.53
        // SCORING GUIDELINE: The primary benchmark is Geekbench 6 (GB6) Single-Core.
        // • WHERE TO FIND IT: Query browser.geekbench.com for the host SoC (System on Chip) or exact device model.
        // • EXTRACTION RULE: Use the "Single-Core Score" from the "Android" or "iOS" category. Verify version is 6.x. Do NOT use older versions (e.g. Geekbench 4 or 5) or Multi-Core scores.
        // • SCORING GUIDELINE: subscore = 10 * (log(value) - log(CPU_GB6_Single_Score_Min)) / (log(CPU_GB6_Single_Score_Max) - log(CPU_GB6_Single_Score_Min)), clamped 0–10.
        // If no benchmark score is available, set value to "Not found" and source, exact_extract, and subscore to "N/A".
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD C — Single-Thread Efficiency Prediction Model (Tertiary / baseline for Method B)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_c_prediction_model_CPU_single": {
        "architecture_mapping": {
          "identifier": "Cortex-X4",
          "identifier_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.best.architecture",
          "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
          "core_architecture_score": 7.95,
          // GUIDELINE: The CAS (Core Architecture Score) retrieved from the lookup table representing linear IPC (Instructions Per Cycle) capability. VERY IMPORTANT: Ensure this core architecture score is the highest among all the core architecture scores of the SoC.
          "reference_frequency_ghz": 3.30,
          // GUIDELINE: The reference frequency in GHz (Gigahertz) from the lookup table.
          "typical_l2_kb": 2048,
          // GUIDELINE: The standardized private Level 2 (L2) cache capacity in KB (Kilobytes) from the lookup table.
          "isa_gen": "ARMv9.2",
          // GUIDELINE: The ISA (Instruction Set Architecture) generation from the lookup table.
          "isa_gen_score": 1.08
          // GUIDELINE: The ISA hardware efficiency multiplier from the lookup table.
        },
        "actual_frequency_ghz": {
          "value": 3.3,
          "value_path": "6_processing_power_and_performance.6_1_cpu_multi_core_performance.method_c_prediction_model_CPU_multi.clusters.best.actual_frequency_ghz.value"
          // GUIDELINE: The maximum advertised actual clock frequency in GHz (Gigahertz) of the best performing core cluster from Section 6.1.
        },
        "core_yield": {
          "value": 8.5860,
          "calculation_formula": "core_yield.value = architecture_mapping.core_architecture_score * ((actual_frequency_ghz.value / architecture_mapping.reference_frequency_ghz) ^ 0.93) * architecture_mapping.isa_gen_score",
          // GUIDELINE: Core Yield (CY) = CAS * (Actual_Freq / Ref_Freq)^gamma * ISA_Multiplier. Fixed single-core frequency scaling soft-saturation exponent (gamma) of 0.93 representing the extreme burst behavior of the best core pushed to physical limits. Keep 4 decimal places.
        },
        "normalized_core_yield": {
          "value": 9.1300,
          "calculation_formula": "normalized_core_yield.value = 10.0 * (log(core_yield.value) - log(CPU_STRS_Score_Min)) / (log(CPU_STRS_Score_Max) - log(CPU_STRS_Score_Min)), clamped 0–10."
          // GUIDELINE: Converts Core Yield into a human-perceptual score (STRS_norm [Single-Threaded Raw Score Normalized]) utilizing logarithmic scaling to model the Weber-Fechner Law. Keep 4 decimal places.
        },
        "cache_subsystem_penalty": {
          "l2_cache_score": {
            "value": 5.7143,
            "calculation_formula": "l2_cache_score.value = 10.0 * (log(architecture_mapping.typical_l2_kb) - log(CPU_L2_KB_Min)) / (log(CPU_L2_KB_Max) - log(CPU_L2_KB_Min)), clamped 0–10."
            // GUIDELINE: L2CS Score represents the standardized L2 Cache Subsystem capability normalized logarithmically between CPU_L2_KB_Min (128 KB) and CPU_L2_KB_Max (16384 KB). Keep 4 decimal places.
          },
          "deficit": {
            "value": 3.4157,
            "calculation_formula": "deficit.value = max(0, normalized_core_yield.value - cache_subsystem_penalty.l2_cache_score.value)"
            // GUIDELINE: Calculates the deficit between the normalized CPU core requirements (normalized_core_yield) and the cache subsystem capability (l2_cache_score). Keep 4 decimal places.
          },
          "penalty": {
            "value": 0.3350,
            "calculation_formula": "penalty.value = 0.06 * (cache_subsystem_penalty.deficit.value ^ 1.4)"
            // GUIDELINE: Models non-linear memory-stall performance penalties caused by cache capacity constraints using a scaling factor of 0.06 and exponent of 1.4. Keep 4 decimal places.
          }
        },
        "memory_subsystem_penalty": {
          "deficit": {
            "value": 0.3066,
            "calculation_formula": "deficit.value = max(0, normalized_core_yield.value - 6_processing_power_and_performance.6_5_ram_technology.scores.predicted)"
            // GUIDELINE: Calculates the deficit between normalized CPU core requirements and the supporting system DRAM (Dynamic Random-Access Memory) Technology score (from Section 6.5). Keep 4 decimal places.
          },
          "penalty": {
            "value": 0.0065,
            "calculation_formula": "penalty.value = 0.03 * (memory_subsystem_penalty.deficit.value ^ 1.3)"
            // GUIDELINE: Models fabric latency and transfer bandwidth bottlenecks under peak single-core throughput using a scaling factor of 0.03 and exponent of 1.3. Keep 4 decimal places.
          }
        },
        "predicted_score": 8.79,
        "calculation_formula": "predicted_score = normalized_core_yield.value - (cache_subsystem_penalty.penalty.value + memory_subsystem_penalty.penalty.value)",
        // SCORING GUIDELINE: The predicted CPU single-core score, computed by subtracting both private cache and memory subsystem penalties from the normalized core yield.
        // BOUNDS CHECK ABORT PROCEDURE: If the predicted score is outside the physical standard bounds of [0.00, 10.00] (less than 0.00 or greater than 10.00), the scoring system MUST HALT execution immediately to prevent data pollution. The engine MUST raise a high-priority exception: "CRITICAL ANOMALY ALERT: Raw single-core CPU score ({Predicted_Score}) is outside physical standard bounds [0, 10]. Halting scoring process."
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD B — Nearest Neighbor Interpolation (Secondary)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_b_neighbor_interpolation_CPU_single": {
        // SCORING GUIDELINE: Method B is calculated for ALL phones (even if Method A is available) for precision validation. The interpolation search space includes all distinct phones in the database with a verified Geekbench 6 Single-Core score (Method A), excluding the target device itself. The interpolation MUST utilize exactly 3 distinct neighbor devices.
        // Step 1 (Neighbor Selection): Find the 3 distinct candidate devices with the smallest Euclidean Distance, calculated as:
        // Distance = Sqrt( (STRS_norm_Diff)^2 + (Penalty_L2CS_Diff)^2 + (Penalty_MTI_Diff)^2 )
        // Where the metric component differences are derived from the following paths:
        // • STRS_norm_Diff (Single-Threaded Raw Score Normalized Difference) = (target.method_c_prediction_model_CPU_single.normalized_core_yield.value) - (neighbor.method_c_prediction_model_CPU_single.normalized_core_yield.value)
        // • Penalty_L2CS_Diff (Level 2 Cache Subsystem Penalty Difference) = (target.method_c_prediction_model_CPU_single.cache_subsystem_penalty.penalty.value) - (neighbor.method_c_prediction_model_CPU_single.cache_subsystem_penalty.penalty.value)
        // • Penalty_MTI_Diff (Memory Technology Index Penalty Difference) = (target.method_c_prediction_model_CPU_single.memory_subsystem_penalty.penalty.value) - (neighbor.method_c_prediction_model_CPU_single.memory_subsystem_penalty.penalty.value)
        // Step 2: Compute the average predicted and average benchmark scores of the neighbors, calculate the correction ratio, and apply it to derive the final interpolated score.
        "neighbors": [
          {
            // Neighbor1
            "device_id_1": "xiaomi_14_ultra",
            // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
            "euclidean_distance_1": 0.2315,
            // GUIDELINE: Calculated Euclidean distance between the target device and the neighbor (Step 1). Keep 4 decimal places.
            "predicted_score_1": 8.24,
            // GUIDELINE: The neighbor's Method C predicted single-core CPU score.
            "benchmark_score_1": 8.49
            // GUIDELINE: The neighbor's Method A subscore.
          },
          {
            // Neighbor2
            "device_id_2": "oneplus_12",
            "euclidean_distance_2": 0.1482,
            "predicted_score_2": 8.12,
            "benchmark_score_2": 8.45
          },
          {
            // Neighbor3
            "device_id_3": "asus_rog_phone_8_pro",
            "euclidean_distance_3": 0.5230,
            "predicted_score_3": 8.32,
            "benchmark_score_3": 8.57
          }
        ],
        "avg_predicted_neighbors": 8.2267,
        // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
        "avg_benchmark_neighbors": 8.5033,
        // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
        "correction_ratio": 1.0685,
        // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_CPU_single.predicted_score / avg_predicted_neighbors. Keep 4 decimal places.
        "interpolated_score": 9.09
        // SCORING GUIDELINE: The final interpolated score. Formula: correction_ratio * avg_benchmark_neighbors.
      },
      "scores": {
        "predicted": 8.79,
        // SCORING GUIDELINE: Directly inherits method_c_prediction_model_CPU_single.predicted_score.
        "final": {
          "value": 8.53,
          // SCORING GUIDELINE: Resolved strictly by the A->B->C hierarchy: Use Method A if method_a_benchmark_CPU_single is available (method_a_benchmark_CPU_single.subscore becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_CPU_single.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_CPU_single.predicted_score).
          "method_used": "Benchmark (Geekbench 6)",
          // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
          //   • "Benchmark (Geekbench 6)" → Method A (documented Geekbench 6 score)
          //   • "Neighbor Interpolation"  → Method B (similar device benchmarks)
          //   • "Predictor"               → Method C (spec-based performance model)
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
    // | GPU Model                  | Standard Graphics | Ray Tracing | Ref Freq (MHz) | efficiency |
    // | :------------------------- | :---------------: | :---------: | :------------: | :--------: |
    // | Immortalis-G925 MC12       |       9.50        |    10.00    |      1612      |    10.0    |
    // | Adreno 830                 |       9.50        |    9.80     |      1100      |    10.0    |
    // | Apple GPU (A18 Pro)        |       9.00        |    8.80     |      1490      |    10.0    |
    // | Adreno 750                 |       8.90        |    8.50     |      903       |    9.0     |
    // | Immortalis-G720 MC12       |       8.80        |    8.40     |      1300      |    10.0    |
    // | Apple GPU (A18)            |       8.70        |    8.20     |      1490      |    10.0    |
    // | Immortalis-G715 MC11       |       8.50        |    7.60     |      981       |    9.0     |
    // | Xclipse 940                |       8.50        |    8.00     |      1109      |    7.0     |
    // | Adreno 740                 |       8.30        |    7.00     |      680       |    9.0     |
    // | Apple GPU (A17 Pro)        |       8.10        |    7.50     |      1398      |    9.0     |
    // | Adreno 735                 |       7.90        |    5.50     |      950       |    8.0     |
    // | Adreno 732                 |       7.80        |    4.20     |      900       |    8.0     |
    // | Adreno 730                 |       7.80        |    4.00     |      900       |    7.0     |
    // | Adreno 725                 |       7.80        |    3.80     |      580       |    9.0     |
    // | Apple GPU (A16 Bionic)     |       7.50        |    0.00     |      1398      |    8.0     |
    // | Apple GPU (A15 Bionic)     |       6.80        |    0.00     |      1296      |    8.0     |
    // | Mali-G715 MC9              |       6.80        |    2.20     |      850       |    9.0     |
    // | Xclipse 920                |       6.50        |    2.50     |      1306      |    6.0     |
    // | Mali-G710 MC10             |       6.50        |    0.00     |      850       |    8.0     |
    // | Adreno 660                 |       6.50        |    0.00     |      840       |    5.0     |
    // | Mali-G715 (Tensor G3)      |       6.20        |    2.00     |      890       |    6.0     |
    // | Mali-G715 MC7              |       6.00        |    1.80     |      850       |    9.0     |
    // | Apple GPU (A14 Bionic)     |       5.80        |    0.00     |      1086      |    7.0     |
    // | Adreno 720                 |       5.20        |    0.00     |      800       |    8.0     |
    // | Apple GPU (A13 Bionic)     |       5.00        |    0.00     |      979       |    6.0     |
    // | Adreno 710                 |       4.80        |    0.00     |      800       |    8.0     |
    // | Adreno 650                 |       4.80        |    0.00     |      587       |    6.0     |
    // | Mali-G610 MC6              |       4.80        |    0.00     |      850       |    8.0     |
    // | Mali-G77 MC9               |       4.80        |    0.00     |      850       |    6.0     |
    // | Adreno 642L                |       4.50        |    0.00     |      490       |    8.0     |
    // | Mali-G610 MC4              |       4.00        |    0.00     |      850       |    7.0     |
    // | Adreno 640                 |       3.80        |    0.00     |      585       |    5.0     |
    // | Mali-G76 MC12              |       3.60        |    0.00     |      800       |    5.0     |
    // | Apple GPU (A12 Bionic)     |       3.50        |    0.00     |      1050      |    6.0     |
    // | Mali-G76 MC4               |       3.20        |    0.00     |      800       |    5.0     |
    // | Adreno 620                 |       3.20        |    0.00     |      625       |    6.0     |
    // | Mali-G68 MC4               |       3.20        |    0.00     |      900       |    6.0     |
    // | Adreno 619                 |       3.00        |    0.00     |      825       |    6.0     |
    // | Adreno 618                 |       2.80        |    0.00     |      610       |    5.0     |
    // | Mali-G57 MC3               |       2.80        |    0.00     |      950       |    5.0     |
    // | Adreno 613                 |       2.50        |    0.00     |      955       |    6.0     |
    // | Apple GPU (A11 Bionic)     |       2.40        |    0.00     |      1000      |    5.0     |
    // | Mali-G72 MP12              |       2.30        |    0.00     |      800       |    4.0     |
    // | Mali-G72 MP3               |       2.10        |    0.00     |      800       |    5.0     |
    // | Adreno 610                 |       2.00        |    0.00     |      600       |    8.0     |
    // | Mali-G57 MC2               |       1.80        |    0.00     |      950       |    5.0     |
    // | Apple GPU (A10 Fusion)     |       1.70        |    0.00     |      900       |    4.0     |
    // | Adreno 530                 |       1.60        |    0.00     |      624       |    3.0     |
    // | Mali-G71 MP8               |       1.50        |    0.00     |      850       |    4.0     |
    // | Mali-G71 MP2               |       1.20        |    0.00     |      770       |    4.0     |
    // | Mali-G52 MP2               |       1.00        |    0.00     |      850       |    4.0     |
    // | Adreno 512                 |       0.90        |    0.00     |      725       |    4.0     |
    // | Adreno 509                 |       0.75        |    0.00     |      650       |    4.0     |
    // | Adreno 506                 |       0.60        |    0.00     |      650       |    5.0     |
    // | Adreno 505                 |       0.50        |    0.00     |      450       |    3.0     |
    // | PowerVR GE8320             |       0.40        |    0.00     |      680       |    2.0  => 0 ?????   |
    // ----------------------------------------------------------------------------------------------
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
    
    "6_3_0_gpu_architecture_reference": {
      // SCORING GOAL: Serves as the authoritative hardware reference for the GPU architecture. Links the SoC to its specific GPU model.
      "value": "Snapdragon 8 Gen 3",
      // GUIDELINE: Inherits the chipset model name from the device identity record to link with GPU architecture.
      "value_path": "identity.hardware_configuration.chipset.value",
      // GUIDELINE: Absolute path to the chipset identifier in the device identity section.
      "gpu_model": {
        "value": "Adreno 750",
        // GUIDELINE: Must exactly match an entry in the `GPU_ARCHITECTURE_LOOKUP_TABLE` above. If the spec sheet uses a generic name (e.g. "Adreno GPU"), use the "AMBIGUOUS SPECIFICATION RESOLUTION" procedure to identify the canonical model.
        "source": "https://www.qualcomm.com/products/mobile/snapdragon/smartphones/snapdragon-8-series-mobile-platforms/snapdragon-8-gen-3-mobile-platform",
        // GUIDELINE: Direct source URL for GPU model data.
        "exact_extract": "Qualcomm® Adreno™ GPU"
        // GUIDELINE: The verbatim proof from the source confirming the GPU identifier.
      }
    },
    "6_3_graphics_and_ray_tracing_performance": {
      // SCORING GOAL: Scores raw GPU compute capability using standard graphics tasks and hardware ray tracing.
      // ═══════════════════════════════════════════════════════════════════════════
      // STANDARD GRAPHICS PERFORMANCE
      // ═══════════════════════════════════════════════════════════════════════════
      "standard_graphics": {
        // SCORING GOAL: Focuses on traditional "Raster" rendering (Geometry, Textures, and Shaders) and API efficiency. This represents the vast majority of current mobile gaming workloads. A three-method hierarchy (A→B→C) is used.
        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Direct Benchmark (Primary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_GPU": {
          "value": 1430,
          "source": "https://www.3dmark.com/search",
          "exact_extract": "Samsung Galaxy S24 Ultra [...] 1430",
          "subscore": 8.21
          // SCORING GUIDELINE: Primary benchmark is 3DMark Steel Nomad Light.
          // • WHERE TO FIND IT: Search 3dmark.com search index or GSMArena/NotebookCheck reviews.
          // • EXTRACTION RULE: Use the "Steel Nomad Light" score. Ensure it is not the desktop "Steel Nomad" or older "Wild Life" benchmarks.
          // SCORING GUIDELINE: subscore = 10 * (log(method_a_benchmark_GPU.value) − log(GPU_SteelNomad_Score_Min)) / (log(GPU_SteelNomad_Score_Max) − log(GPU_SteelNomad_Score_Min)), clamped 0–10. If no benchmark score is available set value to "Not found" and source, exact_extract and subscore to "N/A".
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Graphics Performance Prediction Model (Tertiary / baseline for Method B)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_GPU": {
          // SCORING RATIONALE: This model predicts rasterization performance by analyzing the hardware's peak theoretical throughput (GPU Yield) modified by software API efficiency (AFM), and applying dynamic non-linear deficit penalties for supporting subsystems: system memory bandwidth availability (MTI) and chassis-level thermal burst capacity (via TDSI). CPU orchestration overhead is neglected from the active graphics penalty model as the primary benchmark is GPU-bound.
          "architecture_mapping": {
            "identifier": "Adreno 750",
            "identifier_path": "6_3_0_gpu_architecture_reference.gpu_model.value",
            "reference_table": "GPU_ARCHITECTURE_LOOKUP_TABLE",
            "standard_graphics_score": 8.90,
            // GUIDELINE: Performance score from the "Standard Graphics" column of the lookup table.
            "reference_frequency_mhz": 903.00
            // GUIDELINE: Reference frequency from the "Ref Freq (MHz)" column of the lookup table in Megahertz (MHz).
          },
          "actual_frequency_mhz": {
            "value": 1000,
            "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
            "exact_extract": "Adreno 750 (1 GHz)"
            // GUIDELINE: The maximum advertised frequency of the GPU in MHz (Megahertz). Note: 1 GHz (Gigahertz) = 1000 MHz.
          },
          "gpu_yield": {
            "value": 9.7859,
            "calculation_formula": "gpu_yield = architecture_mapping.standard_graphics_score * ((actual_frequency_mhz.value / architecture_mapping.reference_frequency_mhz) ^ 0.93)"
            // GUIDELINE: Models raw silicon throughput capability. Keep 4 decimal places.
          },
          "api_modifier": {
            // GPU API Support Lookup Table (GPU_API_SUPPORT_LOOKUP_TABLE)
            // | Vulkan (Android) | Metal (iOS) | OpenGL ES (Leg) | DirectX (Win Mob) | Score    |
            // | :--------------- | :---------- | :-------------- | :---------------- | :------: |
            // | Vulkan 1.4       | Metal 4.0   | —               | —                 | **10.0** |
            // | —                | Metal 3.3   | —               | —                 | **9.8**  |
            // | —                | Metal 3.2   | —               | —                 | **9.6**  |
            // | —                | Metal 3.1   | —               | —                 | **9.4**  |
            // | Vulkan 1.3       | Metal 3.0   | —               | —                 | **9.2**  |
            // | —                | Metal 2.4   | —               | —                 | **8.8**  |
            // | —                | Metal 2.3   | —               | —                 | **8.6**  |
            // | Vulkan 1.2       | —           | —               | —                 | **8.5**  |
            // | —                | Metal 2.2   | —               | —                 | **8.4**  |
            // | —                | Metal 2.1   | —               | —                 | **8.2**  |
            // | —                | Metal 2.0   | —               | —                 | **8.0**  |
            // | Vulkan 1.1       | Metal 1.2   | —               | —                 | **7.5**  |
            // | —                | Metal 1.1   | —               | —                 | **7.2**  |
            // | Vulkan 1.0       | Metal 1.0   | —               | D3D 12 (FL 11_0)  | **7.0**  |
            // | —                | —           | —               | D3D 11.2          | **6.8**  |
            // | —                | —           | —               | D3D 11.1          | **6.5**  |
            // | —                | —           | —               | D3D 11.0          | **6.0**  |
            // | —                | —           | —               | D3D 10.1          | **5.5**  |
            // | —                | —           | OpenGL ES 3.2   | —                 | **5.0**  |
            // | —                | —           | —               | D3D 9.3           | **4.0**  |
            // | —                | —           | —               | D3D 9.2           | **3.5**  |
            // | —                | —           | OpenGL ES 3.1   | —                 | **3.0**  |
            // | —                | —           | —               | D3D 9.1           | **2.5**  |
            // | —                | —           | —               | D3D 9.0c          | **2.0**  |
            // | —                | —           | OpenGL ES 3.0   | —                 | **1.0**  |
            // | —                | —           | OpenGL ES 2.0   | —                 | **0.0**  |
            // | —                | —           | OpenGL ES 1.1   | —                 | **0.0**  |
            //
              // AMBIGUOUS API RESOLUTION (MANDATORY FALLBACK CENSUS)
              // If the explicit API version is NOT disclosed on the primary spec sheet, the agent MUST resolve the score using the following OS/Architecture fallback matrices.
              // Note that all operating system version listings in these fallback resolution matrices are fully aligned and synchronized with the canonical reference file references/os_version_reference.md.
            //
              // RATIONALE ON HARDWARE VS OS: Can identical SoCs (System on Chips) have different APIs? YES. An API is a software abstraction layer. A capable hardware chip (e.g., Apple A7 or Snapdragon 800) will support newer API versions (e.g., moving from OpenGL ES to Metal, or D3D (Direct3D) 9.3 to D3D 11) when the device receives major OS updates that upgrade the graphics stack. These matrices resolve ambiguity by finding the intersection of Hardware architecture and OS version.
            //
            // MATRIX 1: APPLE / iOS (Deep Coverage Mirror)
            // | OS Version Baseline | Apple SoC Generation | Inferred API Version |
            // | :------------------ | :------------------- | :------------------- |
            // | iOS 19+             | A19, M5 (Future)     | Metal 4.0            |
            // | iOS 18.x            | A18, M4              | Metal 3.3            |
            // | iOS 17.x            | A17 Pro, M3          | Metal 3.2            |
            // | iOS 16.x            | A16, M2              | Metal 3.1            |
            // | iOS 15.x            | A14 - A15, M1        | Metal 3.0            |
            // | iOS 14.x            | A12 - A13            | Metal 2.4            |
            // | iOS 13.x            | A11 Bionic           | Metal 2.3            |
            // | iOS 12.x            | A10 / A10X Fusion    | Metal 2.2            |
            // | iOS 11.x            | A9 / A9X             | Metal 2.1            |
            // | iOS 10.x            | A8 / A8X             | Metal 2.0            |
            // | iOS 10.x - 12.x     | A7 (64-bit Baseline) | Metal 1.2            |
            // | iOS 9.x             | A7 (64-bit Baseline) | Metal 1.1            |
            // | iOS 8.x             | A7 (64-bit Baseline) | Metal 1.0            |
            // | iOS 7.x             | A7 (64-bit Baseline) | OpenGL ES 3.0        |
            // | iOS 6.x             | A6 / A6X             | OpenGL ES 2.0        |
            // | iOS 4.x - 5.x       | A4 / A5 / A5X        | OpenGL ES 2.0        |
            // | iPhone OS 1 - 3     | iPhone 1st Gen / 3G  | OpenGL ES 1.1        |
            //
            // MATRIX 2: ANDROID (Deep Coverage Mirror)
            // | Android Launch OS | GPU Architecture Baseline     | Inferred API  |
            // | :---------------- | :---------------------------- | :------------ |
            // | Android 15+       | Adreno 8xx+, Immortalis G92x+ | Vulkan 1.4    |
            // | Android 13 - 14   | Adreno 7xx, Mali-G71x         | Vulkan 1.3    |
            // | Android 12        | Adreno 66x, Mali-G710         | Vulkan 1.2    |
            // | Android 10 - 11   | Adreno 6xx, Mali-G77/G78      | Vulkan 1.1    |
            // | Android 7.0 - 9.0 | Adreno 5xx, Mali-G71/G72      | Vulkan 1.0    |
            // | Android 6.0       | Adreno 430 (Snapdragon 810)   | OpenGL ES 3.2 |
            // | Android 5.0 - 5.1 | Adreno 405/418/420, Mali-T7xx | OpenGL ES 3.1 |
            // | Android 4.3 - 4.4 | Adreno 3xx, Mali-T6xx         | OpenGL ES 3.0 |
            // | Android 2.0 - 4.2 | Adreno 2xx, Mali-400          | OpenGL ES 2.0 |
            // | Android 1.x       | Adreno 1xx (Adreno 130)       | OpenGL ES 1.1 |
            //
            // MATRIX 3: WINDOWS MOBILE & WINDOWS PHONE (Deep Coverage Mirror)
            // | Windows OS Version     | Era / Reference Hardware        | Inferred API     |
            // | :--------------------- | :------------------------------ | :--------------- |
            // | Windows 10 Mobile (RS) | Snapdragon 820 (HP Elite x3)    | D3D 12 (FL 11_0) |
            // | Windows 10 Mobile      | Lumia 950 / 950 XL              | D3D 11.2         |
            // | Windows Phone 8.1      | Lumia 930 / 1520                | D3D 11.1         |
            // | Windows Phone 8 GDR    | Snapdragon 800 / 400 (Late WP8) | D3D 11.0         |
            // | Windows Phone 8.0      | Lumia 520 / 620 (Entry Adreno)  | D3D 10.1         |
            // | Windows Phone 8.0      | Lumia 920 / 1020 (Baseline)     | D3D 9.3          |
            // | Windows Phone 8.0      | Early builds / Dev hardware     | D3D 9.2          |
            // | Windows Phone 7.x      | Lumia 800 / 900                 | D3D 9.1          |
            // | Windows Phone 7.0      | Samsung Focus / LG Quantum      | D3D 9.0c         |
            // | Pre-WP7 Legacy         | Pre-2010 HTC / Samsung          | OpenGL ES 1.1    |
            // --------------------------------------------------------------------------------- 
            "identifier": "Vulkan 1.3",
            // GUIDELINE: Standardized API version supported by the GPU.
            "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2667.php",
            "exact_extract": "Vulkan 1.3 support",
            "reference_table": "GPU_API_SUPPORT_LOOKUP_TABLE",
            "score": 9.20,
            // GUIDELINE: Sourced from the GPU_API_SUPPORT_LOOKUP_TABLE or via the AMBIGUOUS API RESOLUTION fallback matrix in comments.
            "factor": {
              "value": 0.9840,
              "calculation_formula": "factor = 0.80 + 0.02 * api_modifier.score"
              // GUIDELINE: Models driver-level draw call efficiency. Keep 4 decimal places.
            }
          },
          "gpu_yield_adjusted": {
            "value": 9.6293,
            "calculation_formula": "gpu_yield_adjusted = gpu_yield.value * api_modifier.factor.value"
            // GUIDELINE: Models hardware potential combined with API efficiency. Keep 4 decimal places.
          },
          "normalized_yield_score": {
            "value": 9.8094,
            "calculation_formula": "normalized_yield_score = 10.0 * (log(gpu_yield_adjusted.value) - log(GPU_Yield_Adjusted_Min)) / (log(GPU_Yield_Adjusted_Max) - log(GPU_Yield_Adjusted_Min)), clamped [0.0, 10.0]"
            // GUIDELINE: Logarithmic normalization to map physical throughput to human perception (Weber-Fechner Law). Keep 4 decimal places.
          },
          "memory_subsystem_penalty": {
            "deficit": {
              "value": 0.9860,
              "calculation_formula": "deficit.value = max(0, normalized_yield_score.value - 6_processing_power_and_performance.6_5_ram_technology.scores.predicted)"
              // GUIDELINE: Deficit between the normalized GPU yield score requirements and the supporting Memory Throughput Index (MTI) from Section 6.5 (predicted score). Keep 4 decimal places.
            },
            "penalty": {
              "value": 0.0980,
              "calculation_formula": "penalty.value = 0.10 * (memory_subsystem_penalty.deficit.value ^ 1.4)"
              // GUIDELINE: Models execution stalls from memory bandwidth starvation using a scaling factor of 0.10 and exponent of 1.4. Keep 4 decimal places.
            }
          },
          "thermal_subsystem_penalty": {
            "deficit": {
              "value": 5.5694,
              "calculation_formula": "deficit.value = max(0, normalized_yield_score.value - 6_processing_power_and_performance.6_10_thermal_dissipation_stability.scores.final.value)"
              // GUIDELINE: Deficit between the normalized GPU yield score requirements and the Thermal Dissipation Stability Index (TDSI) from Section 6.10 (final score). Keep 4 decimal places.
            },
            "penalty": {
              "value": 0.1993,
              "calculation_formula": "penalty.value = 0.0180 * (thermal_subsystem_penalty.deficit.value ^ 1.4)"
              // GUIDELINE: Models thermal throttling impact under burst graphics testing using a scaling factor of 0.0180 and exponent of 1.4. Keep 4 decimal places.
            }
          },
          "predicted_score": 9.51,
          "calculation_formula": "predicted_score = normalized_yield_score.value - (memory_subsystem_penalty.penalty.value + thermal_subsystem_penalty.penalty.value)"
          // SCORING GUIDELINE: The predicted SGS (Standard Graphics Score), computed by subtracting both memory and thermal subsystem penalties from the normalized yield score.
          // BOUNDS CHECK ABORT PROCEDURE: If the predicted score is outside the physical standard bounds of [0.00, 10.00] (less than 0.00 or greater than 10.00), the scoring system MUST HALT execution immediately to prevent data pollution. The engine MUST raise a high-priority exception: "CRITICAL ANOMALY ALERT: Standard Graphics Score ({Predicted_Score}) is outside physical standard bounds [0, 10]. Halting scoring process."
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_GPU": {
          // SCORING GUIDELINE: Method B is calculated for ALL phones (even if Method A is available) for precision validation. The interpolation search space includes all distinct phones in the database with a verified 3DMark Steel Nomad Light score (Method A), excluding the target device itself. The interpolation MUST utilize exactly 3 distinct neighbor devices.
          // Step 1 (Neighbor Selection): Find the 3 distinct candidate devices with the smallest Euclidean Distance, calculated as:
          // Distance = Sqrt( (GPU_Yield_norm_Diff)^2 + (Penalty_MTI_Diff)^2 + (Penalty_TDSI_Diff)^2 )
          // Where the metric component differences are derived from the following paths:
          // • GPU_Yield_norm_Diff (Normalized GPU Yield Difference) = (target.method_c_prediction_model_GPU.normalized_yield_score.value) - (neighbor.method_c_prediction_model_GPU.normalized_yield_score.value)
          // • Penalty_MTI_Diff (MTI Penalty Difference) = (target.method_c_prediction_model_GPU.memory_subsystem_penalty.penalty.value) - (neighbor.method_c_prediction_model_GPU.memory_subsystem_penalty.penalty.value)
          // • Penalty_TDSI_Diff (TDSI Penalty Difference) = (target.method_c_prediction_model_GPU.thermal_subsystem_penalty.penalty.value) - (neighbor.method_c_prediction_model_GPU.thermal_subsystem_penalty.penalty.value)
          // Step 2: Compute the average predicted and average benchmark scores of the neighbors, calculate the correction ratio, and apply it to derive the final interpolated score.
          "neighbors": [
            {
              // Neighbor1
              "device_id_1": "xiaomi_14_ultra",
              // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
              "euclidean_distance_1": 0.2713,
              // GUIDELINE: Weighted Euclidean distance from Step 1.
              "predicted_score_1": 9.40,
              // GUIDELINE: The neighbor's own Method C predicted score.
              "benchmark_score_1": 7.82
              // GUIDELINE: The neighbor's Method A subscore.
            },
            {
              // Neighbor2
              "device_id_2": "asus_rog_phone_8_pro",
              "euclidean_distance_2": 0.2980,
              "predicted_score_2": 9.46,
              "benchmark_score_2": 7.98
            },
            {
              // Neighbor3
              "device_id_3": "oneplus_12",
              "euclidean_distance_3": 0.3125,
              "predicted_score_3": 9.40,
              "benchmark_score_3": 7.88
            }
          ],
          "avg_predicted_neighbors": 9.4200,
          // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3. Keep 4 decimal places.
          "avg_benchmark_neighbors": 7.8933,
          // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3. Keep 4 decimal places.
          "correction_ratio": 1.0096,
          // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_GPU.predicted_score / avg_predicted_neighbors. Keep 4 decimal places.
          "interpolated_score": 7.97
          // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
        },
        "scores": {
          "predicted": 9.51,
          // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_GPU.predicted_score.
          "final": {
            "value": 8.21,
            // GUIDELINE: Resolved strictly by the A->B->C hierarchy: Use Method A if method_a_benchmark_GPU (Method A GPU Benchmark) is available (method_a_benchmark_GPU.subscore becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_GPU.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_GPU.predicted_score).
            "method_used": "Benchmark (3DMark)",
            // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
            //   • Benchmark (3DMark)     → Method A (documented 3DMark score)
            //   • Neighbor Interpolation → Method B (similar device benchmarks)
            //   • Predictor              → Method C (spec-based performance model)
            "booster": "No",
            // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
            "confidence": "N/A"
            // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
          }
        }
      },
      
      // ═══════════════════════════════════════════════════════════════════════════
      // Ray Tracing 
      // ═══════════════════════════════════════════════════════════════════════════
      "ray_tracing": {
        // This measures dedicated hardware acceleration for lighting and reflections.
        "architecture_mapping": {
          "identifier": "Adreno 750",
          "identifier_path": "6_3_0_gpu_architecture_reference.gpu_model.value",
          "reference_table": "GPU_ARCHITECTURE_LOOKUP_TABLE",
          "ray_tracing_score_raw": 8.50
          // GUIDELINE: Maps to the "Ray Tracing" column in the GPU Architecture Lookup Table (GPU_ARCHITECTURE_LOOKUP_TABLE).
        },
        "subscore": 8.50,
        "calculation_formula": "min(architecture_mapping.ray_tracing_score_raw, (architecture_mapping.ray_tracing_score_raw * 0.70) + (6_processing_power_and_performance.6_5_ram_technology.scores.predicted * 0.30)), clamped 0–10."
        // GUIDELINE: Sourced from the Ray Tracing Performance bottleneck formula. Final Ray Tracing Score = min(RT_Score, 0.70 * RT_Score + 0.30 * MTI).
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // Final score (STANDARD GRAPHICS PERFORMANCE & Ray Tracing) 
      // ═══════════════════════════════════════════════════════════════════════════
      "scores": {
        "predicted": 9.41,
        // SCORING GUIDELINE: Final predicted graphics score including ray tracing. Formula: (standard_graphics.scores.predicted * 0.90) + (ray_tracing.subscore * 0.10).
        "final": {
          "value": 8.24,
          // SCORING GUIDELINE: Final Score combines rasterization via Standard Graphics Score (according to the A→B→C hierarchy) and ray tracing capability. Formula: (standard_graphics.scores.final.value * 0.90) + (ray_tracing.subscore * 0.10).
          "method_used": "Benchmark (3DMark)",
          // SCORING GUIDELINE: inherits standard_graphics.scores.final.method_used
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
    // | #   | SoC Model              | NPU / AI Engine         | TOPS(INT8) | Arch Gen       |  Precision  |
    // | :-: | :--------------------- | :---------------------- | :--------: | :------------- | :---------: |
    // |   1 | Snapdragon 8 Elite     | Hexagon (Oryon NPU)     |         45 | Gen AI Native  | INT4+8+FP16 |
    // |   2 | Snapdragon 8 Gen 3     | Hexagon (2024)          |         45 | Gen AI Capable | INT4+8+FP16 |
    // |   3 | Google Tensor G4       | Google TPU (2024)       |         45 | ML Optimized   | INT8+FP16   |
    // |   4 | Apple A19              | 16-Core Neural Engine   |        ~40 | Gen AI Native  | INT4+8+FP16 |
    // |   5 | Apple A19 Pro          | 16-Core Neural Engine   |        ~40 | Gen AI Native  | INT4+8+FP16 |
    // |   6 | Dimensity 9400         | APU 890                 |        ~40 | Gen AI Native  | INT4+8+FP16 |
    // |   7 | Dimensity 9400+        | APU 890 (OC)            |        ~40 | Gen AI Native  | INT4+8+FP16 |
    // |   8 | Exynos 2500            | NPU 6th-gen             |        ~40 | Gen AI Native  | INT4+8+FP16 |
    // |   9 | Apple A18              | 16-Core Neural Engine   |         35 | Gen AI Native  | INT4+8+FP16 |
    // |  10 | Apple A18 Pro          | 16-Core Neural Engine   |         35 | Gen AI Native  | INT4+8+FP16 |
    // |  11 | Apple A17 Pro          | 16-Core Neural Engine   |         35 | Gen AI Capable | INT4+8+FP16 |
    // |  12 | Exynos 2400            | NPU 5th-gen             |       34.7 | Gen AI Capable | INT4+8+FP16 |
    // |  13 | Exynos 2400e           | NPU 5th-gen             |       34.7 | Gen AI Capable | INT4+8+FP16 |
    // |  14 | Dimensity 8400         | APU 790                 |        ~30 | Gen AI Capable | INT4+8+FP16 |
    // |  15 | Dimensity 9300         | APU 790                 |        ~30 | Gen AI Capable | INT4+8+FP16 |
    // |  16 | Dimensity 9300+        | APU 790 (OC)            |        ~30 | Gen AI Capable | INT4+8+FP16 |
    // |  17 | Snapdragon 7+ Gen 3    | Hexagon (Mid 2024)      |        ~30 | Gen AI Capable | INT4+8+FP16 |
    // |  18 | Snapdragon 8s Gen 3    | Hexagon (Mid 2024)      |        ~30 | Gen AI Capable | INT4+8+FP16 |
    // |  19 | Google Tensor G3       | Google TPU (2023)       |         27 | ML Optimized   | INT8+FP16   |
    // |  20 | Snapdragon 8 Gen 1     | Hexagon (2022)          |         27 | ML Optimized   | INT8+FP16   |
    // |  21 | Snapdragon 8+ Gen 1    | Hexagon (2022 OC)       |         27 | ML Optimized   | INT8+FP16   |
    // |  22 | Snapdragon 8 Gen 2     | Hexagon (2023)          |         26 | Gen AI Capable | INT4+8+FP16 |
    // |  23 | Snapdragon 888         | Hexagon 780             |         26 | ML Accelerated | INT8+FP16   |
    // |  24 | Snapdragon 888+        | Hexagon 780 (OC)        |         26 | ML Accelerated | INT8+FP16   |
    // |  25 | Dimensity 8300 Ultra   | APU 780                 |         20 | Gen AI Capable | INT4+8+FP16 |
    // |  26 | Snapdragon 7s Gen 3    | Hexagon (Late 2024)     |         20 | Gen AI Capable | INT4+8+FP16 |
    // |  27 | Dimensity 9200         | APU 690                 |        ~18 | ML Optimized   | INT8+FP16   |
    // |  28 | Dimensity 9200+        | APU 690 (OC)            |        ~18 | ML Optimized   | INT8+FP16   |
    // |  29 | Apple A16 Bionic       | 16-Core Neural Engine   |         17 | ML Optimized   | INT8+FP16   |
    // |  30 | Apple A15 Bionic       | 16-Core Neural Engine   |       15.8 | ML Optimized   | INT8+FP16   |
    // |  31 | Exynos 2100            | NPU                     |        ~15 | ML Accelerated | INT8+FP16   |
    // |  32 | Exynos 990             | Dual-core NPU           |        ~15 | ML Accelerated | INT8+FP16   |
    // |  33 | Snapdragon 865         | Hexagon 698             |         15 | ML Accelerated | INT8+FP16   |
    // |  34 | Snapdragon 865+        | Hexagon 698 (OC)        |         15 | ML Accelerated | INT8+FP16   |
    // |  35 | Snapdragon 870         | Hexagon 698             |         15 | ML Accelerated | INT8+FP16   |
    // |  36 | Exynos 1580            | NPU (6K MAC)            |       14.7 | ML Accelerated | INT8+FP16   |
    // |  37 | Snapdragon 7+ Gen 2    | Hexagon (Mid 2023)      |        ~13 | ML Optimized   | INT8+FP16   |
    // |  38 | Kirin 9010             | Da Vinci (Refined)      |        ~12 | ML Optimized   | INT8+FP16   |
    // |  39 | Dimensity 9000         | APU 590                 |        ~12 | ML Accelerated | INT8+FP16   |
    // |  40 | Dimensity 9000+        | APU 590 (OC)            |        ~12 | ML Accelerated | INT8+FP16   |
    // |  41 | Snapdragon 778G        | Hexagon 770             |         12 | ML Accelerated | INT8+FP16   |
    // |  42 | Snapdragon 778G+       | Hexagon 770             |         12 | ML Accelerated | INT8+FP16   |
    // |  43 | Snapdragon 780G        | Hexagon 770             |         12 | ML Accelerated | INT8+FP16   |
    // |  44 | Apple A14 Bionic       | 16-Core Neural Engine   |         11 | ML Accelerated | INT8+FP16   |
    // |  45 | Kirin 9000             | Da Vinci 2.0 (2+1 core) |        ~10 | ML Optimized   | INT8+FP16   |
    // |  46 | Exynos 1480            | NPU (6K MAC)            |         10 | ML Accelerated | INT8+FP16   |
    // |  47 | Exynos 2200            | Xclipse NPU             |        ~10 | ML Accelerated | INT8+FP16   |
    // |  48 | Snapdragon 7 Gen 3     | Hexagon (Mid 2024)      |        ~10 | ML Accelerated | INT8+FP16   |
    // |  49 | Snapdragon 7 Gen 1     | Hexagon (Mid 2022)      |         ~9 | ML Accelerated | INT8+FP16   |
    // |  50 | Kirin 9000S            | Da Vinci (1+1 core)     |         ~8 | ML Accelerated | INT8+FP16   |
    // |  51 | Kirin 990 5G           | Da Vinci 1.0 (2+1 core) |         ~8 | ML Accelerated | INT8+FP16   |
    // |  52 | Unisoc T820            | Dedicated NPU           |          8 | ML Accelerated | INT8+FP16   |
    // |  53 | Snapdragon 855         | Hexagon 690             |          7 | ML Accelerated | INT8 only   |
    // |  54 | Snapdragon 855+        | Hexagon 690 (OC)        |          7 | ML Accelerated | INT8 only   |
    // |  55 | Apple A13 Bionic       | 8-Core Neural Engine    |         ~6 | ML Accelerated | INT8+FP16   |
    // |  56 | Dimensity 8200         | APU 580                 |         ~6 | ML Accelerated | INT8+FP16   |
    // |  57 | Dimensity 8100         | APU 580                 |       ~5.5 | ML Accelerated | INT8+FP16   |
    // |  58 | Exynos 1080            | NPU                     |       ~5.5 | ML Accelerated | INT8+FP16   |
    // |  59 | Apple A12 Bionic       | 8-Core Neural Engine    |          5 | ML Accelerated | INT8+FP16   |
    // |  60 | Dimensity 7300         | APU 650+                |         ~5 | ML Accelerated | INT8 only   |
    // |  61 | Dimensity 8000         | APU 580                 |         ~5 | ML Accelerated | INT8+FP16   |
    // |  62 | Exynos 1380            | NPU                     |        4.9 | ML Accelerated | INT8 only   |
    // |  63 | Dimensity 1300         | APU 3.0 (6-core OC)     |       ~4.5 | ML Accelerated | INT8 only   |
    // |  64 | Exynos 1280            | NPU                     |        4.3 | ML Accelerated | INT8 only   |
    // |  65 | Dimensity 1080         | APU 3.0                 |         ~4 | ML Accelerated | INT8 only   |
    // |  66 | Dimensity 1200         | APU 3.0 (6-core)        |         ~4 | ML Accelerated | INT8 only   |
    // |  67 | Dimensity 7200         | APU 650                 |         ~4 | ML Accelerated | INT8 only   |
    // |  68 | Dimensity 920          | APU 3.0                 |         ~4 | ML Accelerated | INT8 only   |
    // |  69 | Google Tensor          | Google TPU (2021)       |          4 | ML Accelerated | INT8+FP16   |
    // |  70 | Google Tensor G2       | Google TPU (2022)       |          4 | ML Accelerated | INT8+FP16   |
    // |  71 | Kirin 980              | Cambricon (Dual-NPU)    |         ~4 | ML Accelerated | INT8+FP16   |
    // |  72 | Snapdragon 6 Gen 3     | Hexagon (Mid-tier)      |         ~4 | ML Accelerated | INT8 only   |
    // |  73 | Unisoc T770            | Imagination NNA         |         ~4 | ML Accelerated | INT8 only   |
    // |  74 | Dimensity 7050         | APU 650                 |       ~3.5 | ML Accelerated | INT8 only   |
    // |  75 | Snapdragon 680         | Hexagon 686             |        3.3 | DSP/HVX        | INT8 only   |
    // |  76 | Snapdragon 695         | Hexagon 686             |        3.3 | DSP/HVX        | INT8 only   |
    // |  77 | Unisoc T760            | Dedicated NPU           |        3.2 | ML Accelerated | INT8 only   |
    // |  78 | Snapdragon 480         | Hexagon 686             |         ~3 | DSP/HVX        | INT8 only   |
    // |  79 | Snapdragon 6 Gen 1     | Hexagon (Mid-tier)      |         ~3 | DSP/HVX        | INT8 only   |
    // |  80 | Snapdragon 662         | Hexagon 686             |         ~3 | DSP/HVX        | INT8 only   |
    // |  81 | Snapdragon 685         | Hexagon 686             |         ~3 | DSP/HVX        | INT8 only   |
    // |  82 | Snapdragon 845         | Hexagon 685             |          3 | DSP/HVX        | INT8 only   |
    // |  83 | Kirin 970              | Cambricon (Single-NPU)  |         ~2 | ML Accelerated | INT8+FP16   |
    // |  84 | Dimensity 6100+        | APU (Budget)            |         ~2 | DSP/HVX        | INT8 only   |
    // |  85 | Dimensity 6300         | APU (Budget)            |         ~2 | DSP/HVX        | INT8 only   |
    // |  86 | Snapdragon 4 Gen 2     | Hexagon (Budget)        |         ~2 | DSP/HVX        | INT8 only   |
    // |  87 | Exynos 9820            | Dual-core NPU           |        1.9 | DSP/HVX        | INT8 only   |
    // |  88 | Exynos 9825            | Dual-core NPU           |        1.9 | DSP/HVX        | INT8 only   |
    // |  89 | Snapdragon 4 Gen 1     | Hexagon (Budget)        |       ~1.5 | DSP/HVX        | INT8 only   |
    // |  90 | Snapdragon 4s Gen 2    | Hexagon (Budget)        |       ~1.5 | DSP/HVX        | INT8 only   |
    // |  91 | Snapdragon 7s Gen 2    | Hexagon (Late 2023)     |        1.5 | DSP/HVX        | INT8 only   |
    // |  92 | Snapdragon 835         | Hexagon 682             |        1.5 | DSP/HVX        | INT8 only   |
    // |  93 | Exynos 1330            | NPU                     |        1.2 | ML Accelerated | INT8 only   |
    // |  94 | Exynos 850             | Minimal NPU             |         ~1 | DSP/HVX        | INT8 only   |
    // |  95 | Helio G99              | APU 2.0                 |         ~1 | DSP/HVX        | INT8 only   |
    // |  96 | Snapdragon 820         | Hexagon 680             |        1.0 | DSP/HVX        | INT8 only   |
    // |  97 | Helio G96              | APU 2.0                 |       ~0.8 | DSP/HVX        | INT8 only   |
    // |  98 | Helio G95              | APU 2.0                 |       ~0.7 | DSP/HVX        | INT8 only   |
    // |  99 | Apple A11 Bionic       | 2-Core Neural Engine    |        0.6 | ML Accelerated | INT8+FP16   |
    // | 100 | Apple A10 Fusion       | None                    |        0.5 | CPU-Only       | None        |
    // | 101 | Exynos 9810            | None                    |        0.5 | CPU-Only       | None        |
    // | 102 | Helio G85              | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 103 | Helio G88              | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 104 | Kirin 960              | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 105 | Kirin Legacy           | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 106 | MediaTek Legacy        | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 107 | Qualcomm Legacy        | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 108 | Unisoc T606            | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 109 | Unisoc T612            | CPU-only emulation      |        0.5 | CPU-Only       | None        |
    // | 110 | Unisoc T616            | CPU-only emulation      |        0.5 | CPU-Only       | None        |
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
        "npu": {
          "architecture_mapping": {
            "identifier": "Snapdragon 8 Gen 3",
            "identifier_path": "identity.hardware_configuration.chipset.value",
            "reference_table": "SOC_NEURAL_PROCESSING_UNIT_(NPU)_/_AI_ACCELERATOR_LOOKUP_TABLE",
            "tops_int8": 45,
            // GUIDELINE: Retrieve raw TOPS from the "TOPS(INT8)" column in the lookup table by matching the chipset identifier.
            "architecture_generation": "Gen AI Capable",
            // GUIDELINE: Retrieve the architecture generation from the "Arch Gen" column in the lookup table by matching the chipset identifier.
            "precision_support": "INT4+8+FP16"
            // GUIDELINE: Retrieve the precision support format from the "Precision" column in the lookup table by matching the chipset identifier.
          },
          "tops_normalized": {
            "value": 9.7712,
            "calculation_formula": "tops_normalized = 10.0 * (log(architecture_mapping.tops_int8) - log(NPU_TOPS_Min)) / (log(NPU_TOPS_Max) - log(NPU_TOPS_Min))"
            // GUIDELINE: Logarithmic normalization of TOPS relative to minimum (NPU_TOPS_Min) and maximum (NPU_TOPS_Max) constants. Keep 4 decimal places.
          },
          "architecture_generation_score": {
            "value": 8.00,
            "calculation_formula": "Translate generation tier (architecture_mapping.architecture_generation) to score: Gen AI Native = 10.00, Gen AI Capable = 8.00, ML Optimized = 6.00, ML Accelerated = 4.00, DSP/HVX = 2.00, CPU-Only = 0.00"
          },
          "precision_support_score": {
            "value": 10.00,
            "calculation_formula": "Translate precision format (architecture_mapping.precision_support) to score: INT4+8+FP16 = 10.00, INT8+FP16 = 7.00, INT8 only = 4.00, None = 0.00"
          },
          "subscore": 9.29,
          "calculation_formula": "subscore = 0.50 * tops_normalized.value + 0.30 * architecture_generation_score.value + 0.20 * precision_support_score.value"
          // GUIDELINE: Composite NPU score calculated as the weighted sum of normalized TOPS (50%), architecture generation (30%), and precision support (20%).
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
          //         *   `IF (SoC_Family == "Google Tensor" OR SoC_Model starts with "Google Tensor")` → Score 10.0.
          //         *   `IF (Device_Brand == "Apple" AND (Arch_Gen IN ["Gen AI Native", "Gen AI Capable", "ML Optimized", "ML Accelerated"]))` → Score 10.0.
          //         *   `IF ((OS == "HarmonyOS" OR OS == "HarmonyOS NEXT") AND SoC_Manufacturer == "HiSilicon" AND (Arch_Gen IN ["Gen AI Native", "Gen AI Capable", "ML Optimized", "ML Accelerated"]))` → Score 10.0.
          //
          //  • "Tier 2: SDK Co-Optimized"                          → 8.00
          //     *   *Definition:* The device uses a modern 3rd-party SoC supported by a robust, vendor-specific optimization SDK that bridges the OS and hardware (e.g., **Qualcomm QNN**, **MediaTek NeuroPilot**, **Samsung ENN**).
          //     *   *Agent Validation Rule (Concrete boolean check):*
          //         *   `IF (SoC_Manufacturer IN ["Qualcomm", "MediaTek", "Samsung", "HiSilicon"]) AND (Arch_Gen IN ["Gen AI Native", "Gen AI Capable", "ML Optimized", "ML Accelerated"])` → Score 8.0.
          //         *   `IF (Device Specs contain custom Co-processor ("MariSilicon", "Vivo V-series", "Xiaomi Surge"))` → Score 8.0.
          //
          //  • "Tier 3: Hardware Accelerated / Optimized Fallback" → 5.50
          //     *   *Definition:* The device lacks a modern dedicated NPU but features an OS-level API highly optimized for bare-metal GPU acceleration or standard fixed-function blocks (e.g., **Apple Metal Performance Shaders (MPS)**, **Qualcomm SNPE**).
          //     *   *Agent Validation Rule (Concrete boolean check):*
          //         *   `IF (Arch_Gen IN ["Gen AI Native", "Gen AI Capable", "ML Optimized", "ML Accelerated"]) AND NOT (Rule_Match == Tier 1 OR Rule_Match == Tier 2)` → Score 5.5 (e.g. Budget NPU Standard Fallback).
          //         *   `IF (Device_Brand == "Apple" AND SoC_Model IN ["Apple A8", "Apple A9", "Apple A10 Fusion", "Apple A10X Fusion"])` → Score 5.5.
          //         *   `IF (Arch_Gen == "DSP/HVX")` → Score 5.5 (Qualcomm SNPE / MediaTek APU 2.0 / Exynos DSP vectors).
          //
          //  • "Tier 4: CPU/GPU Fallback"                          → 3.00
          //     *   *Definition:* The device relies entirely on generic runtime translation (e.g., standard **Android NNAPI** or early OpenGL kernels). Operations are emulated slowly without pipeline-specific silicon.
          //     *   *Agent Validation Rule (Concrete boolean check):*
          //         *   `IF (OS_Family IN ["Android", "Custom", "Apple iOS", "Windows"] OR OS IN ["Android", "HarmonyOS", "HyperOS", "iOS", "Windows Mobile", "Windows Phone", "BlackBerry OS", "Tizen"])` AND NOT (Previous Tier Match) → Score 3.0.
          //         *   *Examples:* Budget Unisoc/Helio CPU-only chipsets, legacy 32-bit/early 64-bit iPhones (e.g. iPhone 4S through 5s with A4-A7 chipsets).
          //
          //  • "Tier 5: Minimal / None"                            → 0.00
          //     *   *Definition:* Device lacks any software framework capable of ML execution.
          //     *   *Agent Validation Rule (Concrete boolean check):*
          //         *   `IF (OS IN ["KaiOS", "Series 30+", "Symbian", "Proprietary"]) OR (Form_Factor == "Feature Phone")` → Score 0.0.
          //         *   `IF (SoC_Family == "Pre-A4 Apple" OR SoC_Model IN ["Apple A4", "Apple A5", "Apple A5X", "Apple A6", "Apple A6X"] OR CPU_Architecture_ISA_Gen == "ARMv6 and older")` → Score 0.0.
          //
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all applicable marketing names/technologies found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        },
        "scores": {
          "subscore_NPU":      { "subscore_path": "6_4_ai_hardware_performance.method_c_prediction_model_AI.npu.subscore",                  "weight_NPU": 0.40 },
          "subscore_RAM_tech": { "subscore_path": "6_5_ram_technology.scores.predicted",                                                    "weight_RAM_tech": 0.20 },
          "subscore_Software": { "subscore_path": "6_4_ai_hardware_performance.method_c_prediction_model_AI.software_stack.subscore",       "weight_Software": 0.15 },
          "subscore_GPU":      { "subscore_path": "6_3_graphics_and_ray_tracing_performance.standard_graphics.scores.final.value",          "weight_GPU": 0.15 },
          "subscore_CPU":      { "subscore_path": "6_2_cpu_architecture_single_core.scores.final.value",                                    "weight_CPU": 0.10 }, 
          // IMPORTANT: For RAM (subscore_RAM_tech) always use Predicted Scores (before any Boosters), not Final Scores, to ensure hardware-only comparison.
          // IMPORTANT: For GPU (subscore_GPU), use strictly the Standard Graphics component (SGS) as Ray Tracing does not contribute to AI workloads.
          // These inputs are used to calculate the predicted score (Method C):
          "predicted": 8.77,
          // SCORING GUIDELINE: Sum(subscore_X * weight_X) for all 5 entries above. This is the score used for Method B neighbors.
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
        "correction_ratio": 1.0257,
        // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_AI.scores.predicted / avg_predicted_neighbors.
        "interpolated_score": 8.53
        // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
      },
      "scores": {
        "predicted": 8.24,
        // SCORING GUIDELINE: Final weighted predicted score. Formula: (method_c_prediction_model_AI.scores.predicted * 0.75) + (6_6_ram_capacity.scores.predicted * 0.10) + (6_10_thermal_dissipation_stability.scores.final.value * 0.075) + (6_8_storage_capacity.scores.predicted * 0.05) + (6_7_storage_technology.scores.predicted * 0.025).
        "final": {
          "value": 7.92,
          // SCORING GUIDELINE: Final Score combines the AI System Score with residency factors (RAM/Storage) and thermal stability (TDSI) according to the Method A→B→C priority hierarchy. Formula: (AI_System_Score * 0.75) + (6_6_ram_capacity.scores.predicted * 0.10) + (6_10_thermal_dissipation_stability.scores.final.value * 0.075) + (6_8_storage_capacity.scores.predicted * 0.05) + (6_7_storage_technology.scores.predicted * 0.025). 
          // AI_System_Score is derived from Method A (method_a_benchmark_AI.subscore) if available; if not, Method B (method_b_neighbor_interpolation_AI.interpolated_score); if not, Method C (method_c_prediction_model_AI.scores.predicted). 
          "method_used": "Benchmark (Geekbench AI)",
          // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
          //   • Benchmark (Geekbench AI) → Method A (documented Geekbench AI score)
          //   • Neighbor Interpolation   → Method B (similar device benchmarks)
          //   • Predictor                → Method C (weighted component model)
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
      // Newer technologies like LPDDR (Low Power Double Data Rate) standard LPDDR5X allow for significantly faster data transfer speeds—measured in MT/s (Megatransfers per second).
      //
      // ═══════════════════════════════════════════════════════════════════════════
      // MTEI SCORING & RESOLUTION MATRIX (AUTONOMOUS REFERENCE)
      // ═══════════════════════════════════════════════════════════════════════════
      // | Denomination               | MT/s  | Marketing Terms & Keywords                                  |
      // | :------------------------- | :---: | :---------------------------------------------------------- |
      // | LPDDR5X-10667              | 10667 | 10.7 Gbps (Gigabits per second), Ultra-peak                 |
      // | LPDDR5T / LPDDR5X-9600     |  9600 | Turbo (SK Hynix/Vivo), 9.6 Gbps, Enhanced 5X Peak           |
      // | LPDDR5X-8533               |  8533 | Full-blooded (Xiaomi/Redmi), Peak, 8.5 Gbps                 |
      // | LPDDR5X-7500               |  7500 | Power Optimized, 7.5 Gbps, Standard 5X, Optimized           |
      // | LPDDR5-6400                |  6400 | Unified Memory (Apple A16/A17 Pro), 6.4 Gbps, High-speed 5  |
      // | LPDDR5-5500                |  5500 | Standard LPDDR5, 5.5 Gbps, Mainstream 5                     |
      // | LPDDR4X-4266               |  4266 | Enhanced 4X, Peak 4X, 4.2 Gbps, High-speed 4X               |
      // | LPDDR4X-3733               |  3733 | Standard LPDDR4X, 3.7 Gbps, Mainstream 4X                   |
      // | LPDDR4-3200                |  3200 | High-speed LPDDR4, 3.2 Gbps, Standard 4                     |
      // | LPDDR4-2133                |  2133 | Budget LPDDR4, 2.1 Gbps, Entry LPDDR4                       |
      // | LPDDR3-1600                |  1600 | Baseline, Legacy, Obsolete, 1.6 Gbps, LPDDR3/2/1            |
      //
      // DATA PRIORITY RULES (Authoritative Logic Hierarchy):
      // To ensure absolute scoring neutrality and prevent speculative "peak-speed" awarding for undisclosed hardware, the following hierarchy MUST be followed:
      //
      //   EXHAUSTIVE SOURCE VERIFICATION MANDATE: Before falling back to Level 3 or Level 4 resolution methods, the agent/classifier MUST perform an exhaustive search across at least three (3) independent, reputable specification databases or official manufacturer documentation pages to verify that the exact MT/s (Megatransfers per second) speed or marketing terminology is truly unrecorded in public sources.
      //
      //   JEDEC (Joint Electron Device Engineering Council) BASELINE SPEEDS REFERENCE:
      //     - LPDDR5X   -> resolve to 7500 MT/s (LPDDR5X-7500 baseline)
      //     - LPDDR5    -> resolve to 5500 MT/s (LPDDR5-5500 baseline)
      //     - LPDDR4X   -> resolve to 3733 MT/s (LPDDR4X-3733 baseline)
      //     - LPDDR4    -> resolve to 3200 MT/s (LPDDR4-3200 baseline; resolving to 3200 MT/s is justified because the vast majority of mobile Systems on Chip (SoCs) and smartphones released from 2016 onwards utilizing LPDDR4 implement the standard 3200 MT/s JEDEC speed grade, whereas the 2133 MT/s speed grade is limited to legacy pre-2016 architectures or specific low-power embedded platforms)
      //     - LPDDR3    -> resolve to 1600 MT/s (LPDDR3-1600 or older baseline)
      //
      //   1. LEVEL 1: VERBATIM SPECIFICATION (PRIMARY)
      //      - Use only if the exact MT/s (Megatransfers per second) (e.g., "8533 MT/s") is found in the official technical specification or verified hardware teardown.
      //   2. LEVEL 2: DETERMINISTIC MARKETING BIN (SECONDARY)
      //      - If MT/s is missing but qualified marketing terms (e.g., "Turbo", "9.6 Gbps", "Full-blooded") are used, match them directly to the Resolution Matrix above.
      //   3. LEVEL 3: CONSERVATIVE GENERATIONAL FALLBACK (TERTIARY)
      //      - If only a generic generation is disclosed (e.g., "LPDDR5X", "LPDDR5"), resolve directly to the baseline speed defined in the JEDEC BASELINE SPEEDS REFERENCE defined above.
      //      - Peak bin speeds (e.g., 8533 MT/s, 9600 MT/s, 10667 MT/s) are strictly PROHIBITED for generic disclosures without explicit Level 1/2 verification.
      //   4. LEVEL 4: SYSTEM-ON-CHIP (SoC) PARITY RESOLUTION (QUATERNARY)
      //      - If the RAM technology and speed are completely undisclosed but the SoC (System on Chip) model is verified, map to the SoC's reference configuration according to manufacturer-approved standards:
      //        a. Apple Silicon (Unified Memory):
      //           - Apple A18 / A18 Pro (3nm) -> resolve to LPDDR5X-7500 (7500 MT/s)
      //           - Apple A17 Pro (3nm) / Apple A16 Bionic (4nm) -> resolve to LPDDR5-6400 (6400 MT/s)
      //           - Apple A15 Bionic (5nm) through Apple A11 Bionic (10nm) -> resolve to LPDDR4X-4266 (4266 MT/s)
      //           - Apple A10 Bionic (16nm) -> resolve to LPDDR4-3200 (3200 MT/s)
      //           - Apple A9 Bionic and older -> resolve to LPDDR3-1600 or older (1600 MT/s)
      //        b. Non-Apple / Android SoCs (Qualcomm, MediaTek, Exynos, Tensor, Unisoc):
      //           - Identify the maximum RAM standard officially supported by the verified SoC, and resolve it strictly to its corresponding baseline speed defined in the JEDEC BASELINE SPEEDS REFERENCE defined above.
      //
      "effective_speed_mts": {
        "value": 8533,
        // GUIDELINE: The effective transfer rate in MT/s (Megatransfers per second).
        // TRACEABILITY RULE: Identify the device's verified specification and match it using the DATA PRIORITY RULES above to determine the speed in MT/s. Record the marketing name/data rate, source, and exact extract proof inside value_details.
        "value_details": [
          { "name": "Full-blooded LPDDR5X", "source": "TBD", "exact_extract": "Proof pending" }
        ],
      },
      "scores": {
        "predicted": 8.8234,
        "calculation_formula": "scores.predicted = 10.0 * (log(effective_speed_mts.value) - log(RAM_MTS_Min)) / (log(RAM_MTS_Max) - log(RAM_MTS_Min)), clamped 0–10.",
        // SCORING GUIDELINE: The predicted MTEI (Memory Technology Efficiency Index) score, computed by logarithmically normalizing the effective speed in MT/s (Megatransfers per second) between the minimum speed RAM_MTS_Min and the maximum speed RAM_MTS_Max to capture diminishing performance returns. Clamped to [0.00, 10.00].
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.8234,
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
      // SCORING GOAL: Evaluates internal storage protocol efficiency and sequential throughput using the STEI (Storage Technology Efficiency Index).
      // Faster storage directly impacts system boot times, app installation speed, and overall OS (Operating System) responsiveness.
      // Storage protocols evaluated include UFS (Universal Flash Storage), eMMC (embedded MultiMediaCard), and NVMe (Non-Volatile Memory express) used over a PCIe (Peripheral Component Interconnect Express) bus.
      // Performance features include WB (Write Booster) and HPB (Host Performance Booster).
      // Storage throughput is measured in MB/s (Megabytes per second), representing the data bottleneck between the flash memory and the SoC (System on Chip).
      //
      // ═══════════════════════════════════════════════════════════════════════════
      // STEI SCORING & RESOLUTION MATRIX (AUTONOMOUS REFERENCE)
      // ═══════════════════════════════════════════════════════════════════════════
      // | Denomination (Logic Key)      | MB/s  | Marketing Terms & Keywords                                  |
      // | :---------------------------- | :---: | :---------------------------------------------------------- |
      // | UFS 4.1                       | 4200  | UFS 4.1 Standard (Temporary estimation, see note below)     |
      // | UFS 4.0 Peak / NVMe (A17/18)  | 4200  | 4.2 GB/s (Gigabytes per second), UFS 4.0 Peak, NVMe Peak    |
      // | UFS 4.0 Base / NVMe (A16)     | 3000  | UFS 4.0 Base, NVMe Gen 4 Base                               |
      // | UFS 3.1 (Enhanced - WB+HPB)   | 2100  | UFS 3.1 with Write Booster (WB) & Host Performance Booster  |
      // | UFS 3.1 Standard / NVMe (A15) | 1750  | UFS 3.1 Standard, NVMe Gen 3 Peak                           |
      // | UFS 3.0 / NVMe (A14)          | 1450  | UFS 3.0 Standard, NVMe Gen 3 Base                           |
      // | UFS 2.2 / NVMe (A13)          | 1000  | UFS 2.2 Standard, NVMe Gen 2 Peak                           |
      // | UFS 2.1 (Peak)                |  850  | UFS 2.1 with Turbo Write / Write Booster (WB)               |
      // | UFS 2.1 Standard / NVMe (A12) |  600  | UFS 2.1 Standard, NVMe Gen 2 Base                           |
      // | UFS 2.0 / NVMe (A11)          |  450  | UFS 2.0 Standard, NVMe Gen 1 Peak                           |
      // | eMMC 5.1 HS400 / NVMe (A10)   |  300  | eMMC 5.1 HS400 (High Speed 400) mode, NVMe Gen 1 Base       |
      // | eMMC 5.1 Standard / NVMe (A9) |  220  | eMMC 5.1 Standard JEDEC baseline, NVMe Gen 1 Entry          |
      // | eMMC 5.0                      |  150  | eMMC 5.0 Standard                                           |
      // | eMMC <= 4.5 / NVMe (A8/Older) |  100  | eMMC legacy, PCIe / NVMe legacy                             |
      //
      // NOTE ON UFS 4.1 SPECIFICATION & METHODOLOGY:
      //   Published by JEDEC (Joint Electron Device Engineering Council) in December 2024 (JESD220G), UFS 4.1 retains the physical link layer of UFS 4.0 (MIPI M-PHY 5.0, 23.2 Gbps/lane), meaning its theoretical throughput limit remains 4200 MB/s. Because commercial chips and devices featuring UFS 4.1 are not yet available in the market, this mapping represents the current best estimation to prevent scoring range distortions.
      //
      // DATA PRIORITY RULES (Authoritative Logic Hierarchy):
      // To ensure absolute scoring neutrality and prevent speculative "peak-speed" awarding for undisclosed hardware, the following hierarchy MUST be followed:
      //
      //   EXHAUSTIVE SOURCE VERIFICATION MANDATE: Before falling back to Level 3 or Level 4 resolution methods, the agent/classifier MUST perform an exhaustive search across at least three (3) independent, reputable specification databases or official manufacturer documentation pages to verify that the exact storage technology or protocol is truly unrecorded in public sources.
      //
      //   JEDEC BASELINE SPEEDS REFERENCE:
      //     - UFS 4.1     -> resolve to 4200 MB/s (UFS 4.1 Standard baseline)
      //     - UFS 4.0     -> resolve to 3000 MB/s (UFS 4.0 Base baseline)
      //     - UFS 3.1     -> resolve to 1750 MB/s (UFS 3.1 Standard baseline)
      //     - UFS 3.0     -> resolve to 1450 MB/s (UFS 3.0 baseline)
      //     - UFS 2.2     -> resolve to 1000 MB/s (UFS 2.2 baseline)
      //     - UFS 2.1     -> resolve to 600 MB/s (UFS 2.1 Standard baseline)
      //     - UFS 2.0     -> resolve to 450 MB/s (UFS 2.0 baseline)
      //     - eMMC 5.1    -> resolve to 220 MB/s (eMMC 5.1 Standard baseline)
      //     - eMMC 5.0    -> resolve to 150 MB/s (eMMC 5.0 baseline)
      //     - eMMC <= 4.5 -> resolve to 100 MB/s (eMMC <= 4.5 baseline)
      //
      //   1. LEVEL 1: VERBATIM THROUGHPUT SPECIFICATION (PRIMARY)
      //      - Use only if the exact sequential read throughput (e.g., "3500 MB/s", "4.2 GB/s") is officially published by the manufacturer or measured in verified benchmark tests (e.g., AndroBench 5.1 or CPDT using documented testing methodology).
      //      - Match the exact speed to the closest speed value in the resolution matrix. If conflicting benchmark results exist, the classifier must choose the most conservative verified throughput.
      //   2. LEVEL 2: DETAILED PROTOCOL & MARKETING BIN MATCHING (SECONDARY)
      //      - If exact throughput is missing, but a specific protocol generation and detailed performance subtype or marketing bin is explicitly disclosed, match it to the Resolution Matrix:
      //        - UFS 4.0 Peak / NVMe (A17/18) -> resolve to 4200 MB/s (assigning peak bin speeds requires direct evidence of the peak implementation, not just the protocol name).
      //        - UFS 3.1 Enhanced (featuring verified Write Booster (WB) and Host Performance Booster (HPB) performance profiles) -> resolve to 2100 MB/s.
      //        - UFS 2.1 Peak (with verified Turbo Write/Write Booster) -> resolve to 850 MB/s.
      //        - eMMC 5.1 HS400 -> resolve to 300 MB/s.
      //        - For standard/base configurations without peak modifiers (e.g., "UFS 4.0 Base", "UFS 3.1 Standard"), resolve directly to the baseline speed defined in the JEDEC BASELINE SPEEDS REFERENCE.
      //   3. LEVEL 3: CONSERVATIVE GENERATIONAL FALLBACK (TERTIARY)
      //      - If only a generic generation is disclosed (e.g., "UFS 4.1", "UFS 4.0", "UFS 3.1", "eMMC 5.1"), resolve directly to the baseline speed defined in the JEDEC BASELINE SPEEDS REFERENCE.
      //      - Peak-performance bins (e.g., UFS 4.0 Peak at 4200 MB/s, UFS 3.1 Enhanced at 2100 MB/s, eMMC 5.1 HS400 at 300 MB/s) are strictly PROHIBITED for generic disclosures without explicit Level 1/2 verification.
      //   4. LEVEL 4: SYSTEM-ON-CHIP (SoC) PARITY RESOLUTION (QUATERNARY)
      //      - If the storage protocol and throughput are completely undisclosed but the SoC (System on Chip) model is verified, map to the SoC's reference configuration according to the empirically established reference configuration or maximum supported standard:
      //        a. Apple Silicon (Unified NVMe / PCIe interface):
      //           - iPhones are resolved according to empirically established reference configurations based on historical performance benchmarks (since Apple does not officially publish NVMe throughput specs):
      //             - Apple A18 / A18 Pro / A17 Pro (3nm) -> resolve to 4200 MB/s (NVMe Gen 4 Peak equivalent)
      //             - Apple A16 Bionic (4nm) -> resolve to 3000 MB/s (NVMe Gen 4 Base equivalent)
      //             - Apple A15 Bionic (5nm) -> resolve to 1750 MB/s (NVMe Gen 3 Peak equivalent)
      //             - Apple A14 Bionic (5nm) -> resolve to 1450 MB/s (NVMe Gen 3 Base equivalent)
      //             - Apple A13 Bionic (7nm) -> resolve to 1000 MB/s (NVMe Gen 2 Peak equivalent)
      //             - Apple A12 Bionic (7nm) -> resolve to 600 MB/s (NVMe Gen 2 Base equivalent)
      //             - Apple A11 Bionic (10nm) -> resolve to 450 MB/s (NVMe Gen 1 Peak equivalent)
      //             - Apple A10 Bionic (16nm) -> resolve to 300 MB/s (NVMe Gen 1 Base empirical equivalent)
      //             - Apple A9 Bionic (16nm) -> resolve to 220 MB/s (NVMe Gen 1 Entry empirical equivalent)
      //             - Apple A8 Bionic and older -> resolve to 100 MB/s (legacy NVMe/PCIe empirical equivalent)
      //        b. Non-Apple / Android SoCs (Qualcomm, MediaTek, Exynos, Tensor, Unisoc):
      //           - Identify the maximum storage standard officially supported by the verified SoC, and resolve it strictly to its corresponding baseline speed defined in the JEDEC BASELINE SPEEDS REFERENCE.
      //
      "effective_sequential_read_mbps": {
        "value": 4200,
        // GUIDELINE: The effective sequential throughput in MB/s (Megabytes per second).
        // TRACEABILITY RULE: Identify the device's verified specification and match it using the DATA PRIORITY RULES above to determine the speed in MB/s. Record the marketing name/data rate, source, and exact extract proof inside value_details.
        "value_details": [
          { "name": "UFS 4.0 Peak", "source": "TBD", "exact_extract": "Proof pending" }
        ]
      },
      "scores": {
        "predicted": 10.0000,
        "calculation_formula": "scores.predicted = 10.0 * (log(effective_sequential_read_mbps.value) - log(STORAGE_MBPS_Min)) / (log(STORAGE_MBPS_Max) - log(STORAGE_MBPS_Min)), clamped 0–10.",
        // SCORING GUIDELINE: The predicted STEI (Storage Technology Efficiency Index) score, computed by logarithmically normalizing the effective sequential read throughput in MB/s (Megabytes per second) between the minimum speed STORAGE_MBPS_Min and the maximum speed STORAGE_MBPS_Max to capture human-perceptual speed scaling and Amdahl's Law saturation. Clamped to [0.00, 10.00].
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.0000,
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
      // SCORING GOAL: Evaluates the device's physical ability to dissipate heat and maintain consistent performance during sustained workloads. It validates the hardware's theoretical cooling capacity (Thermodynamic RC Model) against empirical gaming stability from the 3DMark Benchmark to ensure a transparent, physics-based thermal score.

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD A — Direct Benchmark (Primary Standard: 3DMark Wild Life Extreme)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_a_benchmark_TDSI": {
        "value": 59.0,
        // GUIDELINE: The "Stability %" result from a 20-minute 3DMark Wild Life Extreme Stress Test. MANDATORY: Only extract the percentage value (e.g., 59.0) representing the ratio between the lowest and highest loops. This value must be ≤ 100.0. CRITICAL: Do NOT use the raw performance "Score" (e.g., 5230) or FPS values.
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 4.24
        // SCORING GUIDELINE: subscore = 10 * (log(value) - log(Thermal_Stability_Min)) / (log(Thermal_Stability_Max) - log(Thermal_Stability_Min)), clamped 0-10.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD C — Thermodynamic RC Prediction Model (Tertiary)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_c_prediction_model_TDSI": {
        // SCORING GOAL: Predicts the Thermal Dissipation Stability Index (TDSI) using a multi-physics model.
        // The model evaluates geometric bounds, three-path thermal resistance (resistance_total_k_w), and the net System-on-Chip (SoC) power budget.
        //
        // --- [1] GEOMETRIC BOUNDARY INPUTS ---
        "height_mm": {
          "value": 162.3,
          "source": "TBD",
          "exact_extract": "Proof pending"
          // GUIDELINE: Overall device height in mm. Critical for radiator surface area calculation.
        },
        "width_mm": {
          "value": 79.0,
          "value_path": "1_design_and_build_quality.1_4_ergonomics.width_mm.value"
          // GUIDELINE: Overall device width in mm. Critical for radiator surface area calculation.
        },
        "aspect_ratio": {
          "value": 2.1667, // Numerical value of the screen aspect ratio (Height / Width).
          "value_details": "19.5 / 9",
          "source": "TBD",
          "exact_extract": "Proof pending"
          // GUIDELINE: Standard screen aspect ratio R (Height / Width) from specs (20:9, 19.5:9, etc.).
        },
        "footprint_area_m2": {
          "value": 0.01282,
          "calculation_formula": "(height_mm * width_mm) / 1000000"
          // GUIDELINE: Total flat surface area (in m^2) of the device's footprint (Height * Width). Represents the theoretical maximum radiator area for BOTH the front and back panels.
        },
        "frame_radiator_area_m2": {
          "value": 0.00353,
          "calculation_formula": "2 * (height_mm + width_mm) * 1_design_and_build_quality.1_4_ergonomics.thickness_mm.value * 0.85 / 1000000"
          // GUIDELINE: Effective convection area (in m^2) of the device's perimeter frame. The 0.85 (Chi factor) accounts for ergonomic corner chamfers and display curves that reduce the effective frame band height.
        },
        "display_surface_area_cm2": {
          "value": 113.5,
          "calculation_formula": "(2_9_screen_size_diagonal_inches.value * 2.54)^2 * (aspect_ratio.value / (aspect_ratio.value^2 + 1))"
          // GUIDELINE: Calculated active screen area (in cm^2). Used to determine the radiant Joule heating contribution of the panel to the system base heat.
        },

        // --- [2] THERMAL RESISTANCE PARAMETERS ---
        "cooling_hardware": {
          // Inventory of passive and active cooling modules. Phase Change Materials (PCM) are excluded from this block as they function via heat absorption and are accounted for separately in the pcm_buffer field.
          "vapor_chamber": {
            // Definition: A two-dimensional heat pipe that uses liquid-to-vapor phase change within a vacuum-sealed flat chamber to rapidly spread heat away from the SoC (System on Chip) across a larger surface area.
            // Marketing Names: Vapor Chamber, VC Cooling, Stainless Steel VC, Copper Vapor Chamber, Dual Vapor Chamber, Mega VC, IceLoop, Ice-cool, Super VC, VC Liquid Cooling, 3D Vapor Chamber.
            "coverage_area_mm2": {
              "value": 4050, 
              "source": "TBD",
              "exact_extract": "Proof pending", 
              // GUIDELINE: total surface area (footprint) of the Vapor Chamber in mm^2, if no Vapor Chamber is present set "value" to 0 and "source" and "exact_extract" to N/A.               
            },
            "phi": {
              "value": 0.3159,
              "calculation_formula": "phi = coverage_area_mm2 / (height_mm * width_mm)"
              // GUIDELINE: Thermal Coverage Factor (ratio of Vapor Chamber footprint to device footprint).
            },
            // NOTE: Regarding the Technological Spreading Constant for Vapor Chambers (alpha), a constant value is directly used in the formula calculating the effective spreading efficiency (s_eff).
          },
          "graphite_or_graphene_layer": {
            // Definition: High-conductivity carbon-based sheets (Natural/Synthetic Graphite or Graphene) used to spread heat laterally. Graphite is the industry standard, while Graphene offers higher thermal conductivity in thinner layers.
            "identifier": "Multi-layer Graphite",
            "source": "TBD",
            "exact_extract": "Proof pending",
            "alpha": 0.8,
            "phi": 0.50,               
            // GUIDELINE: Maps the "Cooling Technology Class" to "alpha" and "phi" based on the provided table. Search for the graphite or graphene cooling technology that applies. Use the following EXACT strings present in the first column (from the lookup table below) for "identifier" with related "alpha" and "phi". Use "None (SoC Only)" if no dedicated sheets are present.
            // | Cooling Technology Class | alpha | phi  |
            // | :------------------------| :---: | :--: |
            // | None (SoC Only)          |  0.0  | 0.00 |
            // | Standard Graphite Sheet  |  0.6  | 0.40 |
            // | Multi-layer Graphite     |  0.8  | 0.50 |
            // | Synthetic Graphene Film  |  1.2  | 0.50 |
            //
          },
          "fan": {
            // GUIDELINE: An integrated mechanical fan can be used to force airflow across internal heat sinks or through the device chassis to enhance convective heat dissipation.
            "max_speed_rpm": {
              "value": 0, 
              "source": "TBD",
              "exact_extract": "Proof pending"
              // GUIDELINE: Fetch the maximum rated rotational speed of the internal fan in RPM. If no internal fan is present, set "value" to 0 and "source" and "exact_extract" to N/A. If unknown but a fan is present, set "value" to "Not found" but you HAVE to provide a valid "source" and "exact_extract" that prove the fan exists.
            },
            "diameter_mm": {
              "value": 0.0,
              "source": "TBD",
              "exact_extract": "Proof pending"
              // GUIDELINE: Fetch the internal fan's diameter in millimeters (mm). If no internal fan is present, set "value" to 0 and "source" and "exact_extract" to N/A. If unknown but a fan is present, set "value" to "Not found" but you HAVE to provide a valid "source" and "exact_extract" that prove the fan exists.
            },
            "h_fan": {
              "value": 0,
              "calculation_formula": "10 + 100 * (max_speed_rpm * diameter_mm / 240000)^0.8"
              // GUIDELINE: Convective intensity within the cooling duct. If max_speed_rpm or diameter_mm are missing (set to "Not found") for a confirmed fan, use a default h_fan = 80 which is a slightly conservative value vs baseline fan (110). value = 0 if no fan is present.
            },
          },
        },
        "back_panel": { 
          "material": {
            "identifier": "Armor-Class Glass",
            "identifier_path": "1_design_and_build_quality.1_1_materials.back_material.value",
            "s_0": 0.05,
            "s_max": 0.95
            // GUIDELINE: Selects the material class based on the back panel identity to determine s_0 and s_max.
            // | Materials (Section 1.1)      | Material Class                | s_0  | s_max |
            // | :--------------------------- | :-----------------------------| :--: | :---: |
            // | **7000 Series Aluminum**     | Class 1 (Conductive Metal)    | 0.60 | 1.00  |
            // | **6000 Series Aluminum**     | Class 1 (Conductive Metal)    | 0.60 | 1.00  |
            // | **Die-Cast Aluminum (ADC12)**| Class 1 (Conductive Metal)    | 0.60 | 1.00  |
            // | **Zinc Alloy (Zamak 3)**     | Class 1 (Conductive Metal)    | 0.60 | 1.00  |
            // | **Stainless Steel**          | Class 2 (Moderate Alloy)      | 0.25 | 1.00  |
            // | **Specialized Ceramic**      | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Armor-Class Glass**        | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Shield-Class Glass**       | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Reinforced Glass**         | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Standard Glass**           | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Reinforced Polymer**       | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Flexible Membrane**        | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Composite Sheet**          | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **High-Performance Polymer** | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Standard Polymer**         | Class 3 (Insulating Material) | 0.05 | 0.95  |
            // | **Not Disclosed**            | Class 3 (Insulating Material) | 0.05 | 0.95  |
            //
          },
          "s_eff": {
            // GUIDELINE: s_eff is the effective spreading efficiency of the back panel.
            "value": 0.6929,
            "calculation_formula": "material.s_0 + (material.s_max - material.s_0) * [ 1 - exp(-2.7 * vapor_chamber.phi - graphite_or_graphene_layer.alpha * graphite_or_graphene_layer.phi)]"
            // GUIDELINE: Continuous Saturation Model of thermal diffusion. Quantifies how effectively the internal spreaders (Vapor Chamber/Graphite/Graphene) utilize the back panel area for convection. The constant 2.7 represents the 'alpha' (spreading intensity) for Vapor Chambers, which is significantly higher than solid graphite due to the near-isothermal behavior of phase-change cycles.
          },    
        },
        "resistance_back_k_w": {
          "value": 11.26,
          "calculation_formula": "1 / [ footprint_area_m2 * ( fan.h_fan * f_fan + 10.0 * (back_panel.s_eff - f_fan) ) ]"
          // GUIDELINE: Thermal resistance of the back panel path. Uses an Area Model to sum dissipation from the forced duct (fan.h_fan over f_fan) and the remaining passive spread surface (h = 10.0 over back_panel.s_eff - f_fan). 
          // f_fan = 0.1 (meaning 10% of the back surface area) if fan.max_speed_rpm > 0, else f_fan = 0.
        },
        "resistance_front_k_w": {
          "value": 31.20,
          "calculation_formula": "1 / (10.0 * footprint_area_m2 * 0.25)"
          // GUIDELINE: 0.25 (s_eff_front) is constant for front-path due to the PCB (Printed Circuit Board) Thermal Wall.
        },
        "frame_material": {
          "identifier": "Titanium Alloy",
          "identifier_path": "1_design_and_build_quality.1_1_materials.frame_material.value",
          "s_eff": 0.40
          // GUIDELINE: Defines lateral perimeter spreading based on the structural frame identity.
          // | Materials (Section 1.1)      | Material Class                | s_eff |
          // | :--------------------------- | :---------------------------- | :---: |
          // | **7000 Series Aluminum**     | Class 1 (Conductive Metal)    | 1.00  |
          // | **6000 Series Aluminum**     | Class 1 (Conductive Metal)    | 1.00  |
          // | **Zinc Alloy (Zamak 3)**     | Class 1 (Conductive Metal)    | 1.00  |
          // | **Die-Cast Aluminum (ADC12)**| Class 1 (Conductive Metal)    | 1.00  |
          // | **Magnesium Alloy**          | Class 1 (Conductive Metal)    | 1.00  |
          // | **Stainless Steel**          | Class 2 (Moderate Alloy)      | 0.40  |
          // | **Amorphous Alloy**          | Class 2 (Moderate Alloy)      | 0.40  |
          // | **Titanium Alloy**           | Class 2 (Moderate Alloy)      | 0.40  |
          // | **Specialized Ceramic**      | Class 3 (Insulating Material) | 0.05  |
          // | **Reinforced Polymer**       | Class 3 (Insulating Material) | 0.05  |
          // | **High-Performance Polymer** | Class 3 (Insulating Material) | 0.05  |
          // | **Standard Polymer**         | Class 3 (Insulating Material) | 0.05  |
          // | **Material Not Disclosed**   | Class 3 (Insulating Material) | 0.05  |
          //
        },
        "resistance_frame_k_w": {
          "value": 70.82,
          "calculation_formula": "1 / (10.0 * frame_radiator_area_m2 * frame_material.s_eff)"
          // GUIDELINE: Thermal resistance of the perimeter frame path (K/W).
        },
        "resistance_total_k_w": {
          "value": 7.41,
          "calculation_formula": "(1/resistance_back_k_w + 1/resistance_front_k_w + 1/resistance_frame_k_w)^-1"
          // GUIDELINE: Unified system thermal resistance (Parallel sum of Back, Front, and Mid-Frame paths). Defines the chassis's global ability to expel thermal wattage to the environment.
        },

        // --- [3] ENERGY BALANCE & TIME CONSTANT ---
        "pcm_buffer": {
          // SCORING GOAL: Evaluates the latent heat storage capacity of the device to buffer high-power transients.
          // Phase Change Materials (PCM) (typically organic hydrocarbons/paraffin) absorb thermal energy during their solid-liquid phase transition, effectively increasing the system's thermal capacitance (C).
          //
          // SCORING GUIDELINE: Identify the PCM implementation strictly via the structural form factor (3D Matrix vs. 2D Interface). 
          // Match the device's verified architecture to the corresponding Tier below. Use the following exact Tier Names for "value" and the related numerical factor for "subscore":
          //
          // • Tier 1: 3D Structural PCM Matrix                → subscore = 0.75
          //   Physical Definition: The PCM (paraffin) is integrated into a 3D conductive lattice (e.g., metal honeycomb, graphene foam, or conductive pillar). This architecture allows for rapid volumetric heat absorption.
          //   AI Detection Logic: Classify as Tier 1 ONLY if descriptions imply a 'structure', 'matrix', '3D foam', 'encapsulation', or 'volumetric pillar'.
          //   Illustrative Examples: Xiaomi's "Honeycomb PCM", "PCM Matrix", "Graphene-PCM Foam", "Aerospace-grade PCM matrix", "Rapid-cooling Conductor (Pillar)".
          //
          // • Tier 2: 2D Interfacial PCM Layer                → subscore = 0.50
          //   Physical Definition: The PCM is applied as a thin interfacial layer (gel, sheet, or film) to improve contact between the SoC (System-on-Chip) and the heat spreader. It lacks a 3D structural matrix.
          //   AI Detection Logic: Classify as Tier 2 if the material is described as a 'gel', 'pad', 'sheet', 'film', 'paste', or 'thermal interface'.
          //   Illustrative Examples: Realme's "Diamond Thermal Gel", "Phase-change gel", "Organic hydrocarbon pad/sheet", "Solid-liquid transition interface", "Paraffin wax sheet".
          //
          // • Tier 3: High-Temp PCM (Melting Point > 45°C)    → subscore = 0.00
          //   Physical Definition: The material is a verified Phase Change Material but its melting point is above the 45°C safety threshold. Because it remains in a solid state throughout the ergonomic evaluation window, it provides zero latent heat capacitance benefit for this model.
          //
          // • Tier 4: None / Standard                         → subscore = 0.00
          //   Physical Definition: No latent heat storage material is utilized beyond standard Thermal Paste (also known as TIM — Thermal Interface Material). Standard TIM fills microscopic air gaps between the SoC (System-on-Chip) and the heat spreader to improve conduction, but remains in a single state; it does not change phase at 40°C–45°C and thus provides no latent heat capacitance. Note: Only in this case (Tier 4) set "source" and "exact_extract" to "N/A".
          //
          // NEUTRALITY & DIFFERENTIATION RULES:
          // 1. VC EXCLUSIVITY: A Vapor Chamber (VC) is a heat TRANSPORT mechanism (Phase Change: Liquid/Vapor). It is already accounted for in Spreading Efficiency (s_eff). 
          //    A PCM Buffer is a heat STORAGE mechanism (Phase Change: Solid/Liquid). Categorizing a VC as a PCM Buffer constitutes double-counting and is strictly forbidden.
          // 2. MELTING POINT CONSTRAINT: Credits only apply if the melting phase is verified to occur between ambient (25°C) and the safety threshold (45°C). Any melting within this window successfully absorbs the latent buffer and delays the thermal throttling point. Above 45°C (Tier 3), the benefit is zero.
          //
          "value": "Tier 4: None / Standard",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.00
        },
        "thermal_capacitance_j_k": {
          "value": 197.2,
          "calculation_formula": "(1_design_and_build_quality.1_5_weight_g.value * 0.850) + (pcm_buffer.subscore * 25)"
          // GUIDELINE: Unified system thermal capacitance (J/K). Defines the "soak capacity" or ability to buffer heat spikes. 850 J/kg-K is the standard bulk specific heat.
        },
        "time_constant_s": {
          "value": 1461,
          "calculation_formula": "resistance_total_k_w * thermal_capacitance_j_k"
          // GUIDELINE: System time constant (seconds). Quantifies the transient lag before the system reaches steady-state equilibrium.
        },
        "power_admissible_w": {
          "value": 4.82,
          "calculation_formula": "20 / (resistance_total_k_w * (1 - exp(-1200 / time_constant_s)))"
          // GUIDELINE: Total Admissible Thermal Power (Watts). The maximum wattage allowed for the entire system to reach exactly the safety threshold (20K rise) at the end of the 1200-second (20-minute) evaluation window. 
        },

        // --- [4] SoC (SYSTEM-ON-CHIP) POWER BUDGET & PREDICTION ---
        "panel_efficiency": {
          "identifier": "Tier 2: LTPO OLED",
          "identifier_path": "2_1_panel_architecture.panel_type.value",
          "c_panel_w_cm2": 0.0035
          // GUIDELINE: Technology-dependent panel constant representing the base power draw to illuminate 1 square centimeter (cm²) of screen at 200 nits.
          // Maps the display panel type to the panel constant c_panel_w_cm2 (Watts per square centimeter - W/cm²) using the following table:
          // | Display Panel Type (Section 2.1)       | c_panel_w_cm2 (W/cm²) |
          // | :------------------------------------- | :-------------------: |
          // | **Tier 1: Tandem OLED**                |        0.0035         |
          // | **Tier 2: LTPO OLED**                  |        0.0035         |
          // | **Tier 3: Standard OLED/AMOLED (LTPS)**|        0.0045         |
          // | **Tier 4: IPS LCD**                    |        0.0060         |
          // | **Tier 5: TFT or PLS LCD**             |        0.0060         |
          // | **Tier 6: TN LCD or Legacy**           |        0.0060         |
        },
        "f_refresh_intensive": {
          "value": 1.1500,
          "calculation_formula": "1 + 0.0025 * (2_6_motion_smoothness.maximum_refresh_rate_hz.value - 60)"
          // GUIDELINE: Refresh Rate Factor. Evaluated at maximum refresh rate (max_hz) in Hertz (Hz) because gaming locks screen refresh to its peak.
        },
        "display_megapixels_mp": {
          "value": 4.4928,
          "calculation_formula": "2_5_resolution_density.resolution_width_px.value * 2_5_resolution_density.resolution_height_px.value / 1000000"
          // GUIDELINE: Screen resolution in Megapixels (MP).
        },
        "f_resolution": {
          "value": 1.0623,
          "calculation_formula": "1 + 0.025 * (display_megapixels_mp.value - 2)"
          // GUIDELINE: Resolution Factor. Accounts for rendering and aperture ratio overhead centered around a 2 Megapixels (MP) baseline.
        },
        "power_display_heat_w": {
          "value": 1.1526,
          "calculation_formula": "display_surface_area_cm2.value * (panel_efficiency.c_panel_w_cm2 * 2.5) * f_refresh_intensive.value * f_resolution.value * 0.95"
          // GUIDELINE: Thermal heat generated by display panel. Brightness scaling multiplier is 2.5 (from 200 to 500 nits) and heat conversion factor is 0.95.
        },
        "power_base_needs_w": {
          "value": 1.5526,
          "calculation_formula": "0.4 + power_display_heat_w.value"
          // GUIDELINE: Heat (in Watts) generated by non-SoC components. Logic Board Baseline (constant 0.4W) + Display radiant heat.
        },
        "power_admissible_soc_w": {
          "value": 3.2674,
          "calculation_formula": "power_admissible_w.value - power_base_needs_w.value"
          // GUIDELINE: Net admissible wattage available exclusively for the SoC workload after accounting for baseline system heat.
        },
        "system_on_chip": {
          // GUIDELINE: Peak SoC Thermal Power (Watts). Represents the maximum heat generated by the chipset during unrestricted high-performance workloads (intensive gaming/benchmarks).
          "identifier": "Snapdragon 8 Gen 3",
          "identifier_path": "identity.hardware_configuration.chipset.value",
          "reference_table": "references/soc_reference.md",
          "power_peak_soc_w": 14.0
          // GUIDELINE: Maps to the "power_peak_soc_w" column based on the SoC identity in references/soc_reference.md.
        },
        "power_ratio": {
          "value": 0.2334,
          "calculation_formula": "power_admissible_soc_w.value / system_on_chip.power_peak_soc_w"
          // GUIDELINE: Raw thermal headroom ratio. Defines the percentage of the SoC's peak power draw (system_on_chip.power_peak_soc_w) that the chassis can sustain throughout the 1200-second (20-minute) evaluation window within ergonomic safety limits. A ratio > 1.0 indicates a surplus cooling margin.
        },
        "predicted_stability_percentage": {
          "value": 61.6,
          "calculation_formula": "100 * (power_ratio.value ^ 0.333) (Clamped 0-100)"
          // GUIDELINE: Cube root law bridging thermal power to physical Stability (Frames per second (FPS)). Capped at 100.
        },
        "predicted_tdsi_score": {
          "value": 4.71,
          "calculation_formula": "10 * (log(predicted_stability_percentage.value) - log(Thermal_Stability_Min)) / (log(Thermal_Stability_Max) - log(Thermal_Stability_Min)), clamped 0-10."
          // GUIDELINE: Final score mapping. Normalizes the predicted stability percentage against industry thresholds (Thermal_Stability_Min/Max).
        }
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD B — Nearest Neighbor Interpolation (Secondary)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_b_neighbor_interpolation_TDSI": {
        // SCORING GUIDELINE: Method B is populated for ALL phones (even if Method A is available) to evaluate the precision of the interpolation model. The interpolation MUST be performed using exactly 3 distinct neighbor devices, explicitly excluding the target device itself.
        // Step 1: Find the 3 distinct devices with the smallest Euclidean distance in the 3-component homogeneous power space (expressed in Watts - W), excluding the target device itself.
        //         Formula: Distance = Sqrt( (Diff_P_soc_peak)^2 + (Diff_P_base)^2 + (Diff_P_admissible)^2 )
        //         Where the metric component differences are derived from the following paths:
        //         - Diff_P_soc_peak (Peak SoC Power Difference) = (target.method_c_prediction_model_TDSI.system_on_chip.power_peak_soc_w) - (neighbor.method_c_prediction_model_TDSI.system_on_chip.power_peak_soc_w)
        //         - Diff_P_base (Base System Power Difference) = (target.method_c_prediction_model_TDSI.power_base_needs_w.value) - (neighbor.method_c_prediction_model_TDSI.power_base_needs_w.value)
        //         - Diff_P_admissible (Total Admissible Power Difference) = (target.method_c_prediction_model_TDSI.power_admissible_w.value) - (neighbor.method_c_prediction_model_TDSI.power_admissible_w.value)
        //         - Target: The device currently being scored.
        //         - Neighbor: Any device in the database with a known benchmark score (Method A), except the Target itself.
        //         Search space: all phones that have a known 3DMark Wild Life Extreme score (Method A), excluding the target device itself.
        // Step 2: Calculate the correction ratio and apply it to the average neighbor benchmark.
        "neighbors": [
          {
            // Neighbor1
            "device_id_1": "apple_iphone_15_pro_max",
            // GUIDELINE: The identity.id of the neighbor device (e.g., "apple_iphone_15_pro_max").
            "euclidean_distance_1": 0.0450,
            // GUIDELINE: Euclidean distance in Watts from Step 1.
            "predicted_score_1": 4.65,
            // GUIDELINE: The neighbor's own Method C predicted score.
            "benchmark_score_1": 4.40
            // GUIDELINE: The neighbor's Method A subscore.
          },
          {
            // Neighbor2
            "device_id_2": "xiaomi_14_pro",
            "euclidean_distance_2": 0.0620,
            "predicted_score_2": 5.10,
            "benchmark_score_2": 4.85
          },
          {
            // Neighbor3
            "device_id_3": "google_pixel_8_pro",
            "euclidean_distance_3": 0.0850,
            "predicted_score_3": 4.80,
            "benchmark_score_3": 4.15
          }
        ],
        "avg_predicted_neighbors": 4.8500,
        // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
        "avg_benchmark_neighbors": 4.4667,
        // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
        "correction_ratio": 0.9711,
        // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_TDSI.predicted_tdsi_score.value / avg_predicted_neighbors.
        "interpolated_score": 4.34
        // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
      },

      "scores": {
        "predicted": 4.71,
        // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_TDSI.predicted_tdsi_score.value.
        "final": {
          "value": 4.24,
          // SCORING GUIDELINE: Use Method A if method_a_benchmark_TDSI is available (method_a_benchmark_TDSI.subscore becomes the final value). Otherwise use Method B (method_b_neighbor_interpolation_TDSI.interpolated_score). Otherwise fall back to Method C (method_c_prediction_model_TDSI.predicted_tdsi_score.value).
          "method_used": "Benchmark (3DMark)",
          // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
          //   • Benchmark (3DMark)     → Method A (documented 3DMark Wild Life Extreme stability score)
          //   • Neighbor Interpolation → Method B (similar device benchmarks)
          //   • Predictor              → Method C (thermodynamic heat dissipation and power limit model)
          "booster": "No",
          // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
          "confidence": "N/A"
          // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
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
        //     - Definition: Supports both mmWave (millimeter-Wave) and Sub-6 (Sub-6 Gigahertz) 5G (5th Generation) spectrums, covering all major global frequency bands.
        //     - Specification Parsing: Specs explicitly list "5G mmWave", "mmWave", or high-frequency band codes (e.g., n257, n258, n260, n261), AND support Sub-6 bands.
        //   • "Tier 2: 5G Sub-6 (Full Global Bands)"              → 9.00
        //     - Definition: Supports 5G on Sub-6 GHz frequencies with extensive band coverage (typically 10+ bands) for global roaming.
        //     - Specification Parsing: Specs list "5G" or band codes starting with lowercase "n" (e.g., n1, n3, n78), with 10 or more distinct Sub-6 bands including major global roaming bands (n1, n3, n78, n28, n77).
        //   • "Tier 3: 5G Sub-6 (Limited/regional bands)"         → 8.00
        //     - Definition: Supports 5G on Sub-6 GHz but with band coverage limited to specific markets/regions (typically < 10 bands).
        //     - Specification Parsing: Specs list "5G" or band codes starting with lowercase "n", but with fewer than 10 distinct Sub-6 bands or restricted to regional configurations (e.g., carrier-locked model).
        //   • "Tier 4: 4G LTE-Advanced Pro"                       → 6.00
        //     - Definition: 4G (4th Generation) LTE (Long-Term Evolution) Advanced Pro supporting Category (Cat) 16 or higher modems (speeds >= 1.0 Gigabits per second / Gbps download).
        //     - Specification Parsing: Specs list "4G", "LTE", or "LTE-A" (LTE-Advanced), AND explicitly document Category 16 or higher or download speeds of 1.0 Gbps or higher, without 5G.
        //   • "Tier 5: 4G LTE (Basic)"                            → 4.00
        //     - Definition: Standard 4G LTE supporting up to Category 15 modems (speeds < 1.0 Gbps download) without advanced carrier aggregation.
        //     - Specification Parsing: Specs list "4G" or "LTE", AND document Category 1 to 15 or download speeds below 1.0 Gbps, without 5G.
        //   • "Tier 6: 3G"                                        → 2.00
        //     - Definition: Limited to 3G (3rd Generation) or older technologies, without 4G LTE support.
        //     - Specification Parsing: Specs list "3G", "UMTS", "HSDPA", "WCDMA", "CDMA2000", or "HSPA", without 4G/5G.
        //   • "Tier 7: 2G"                                        → 0.00
        //     - Definition: Limited to 2G (2nd Generation) technologies only.
        //     - Specification Parsing: Specs list only "2G", "GSM", "GPRS", or "EDGE", without 3G/4G/5G.
        //
        // AMBIGUITY RESOLUTION & MAPPING RULES (MANDATORY):
        //   Automated agents must resolve incomplete or ambiguous cellular specifications using the following 3-step logic hierarchy:
        //
        //   1. Step 1: Secondary Resolution (SoC Lookup)
        //      If any parameters (e.g. mmWave support, 5G band count, 4G Category/speed, or overall generation) are unstated or ambiguous in the specs, retrieve the chipset name from identity.hardware_configuration.chipset.value, look it up in the canonical System-on-Chip (SoC) Reference (references/soc_reference.md), and check its cellular_tier column:
        //        • If the SoC's cellular_tier is "Tier 1" but device specs do not confirm mmWave bands, default to Tier 3 (or Tier 2 if 10+ global bands are explicitly verified).
        //        • If the SoC's cellular_tier is "Tier 2" or "Tier 3" but specs do not confirm global bands, default to Tier 3.
        //        • If the SoC's cellular_tier is "Tier 4" → Map to Tier 4.
        //        • If the SoC's cellular_tier is "Tier 5" → Map to Tier 5.
        //        • If the SoC's cellular_tier is "Tier 6" → Map to Tier 6.
        //        • If the SoC's cellular_tier is "Tier 7" → Map to Tier 7.
        //        • Resolving 4G-Only Device Models with 5G Chipsets: If the primary specification parsing determines the device is 4G-only (disclosing 4G/LTE bands but no 5G bands) but the specific Category or speed is unstated, look up its SoC. If the SoC is listed as a 5G chipset (cellular_tier of "Tier 1", "Tier 2", or "Tier 3"), map the device to Tier 4: 4G LTE-Advanced Pro (since the SoC's integrated modem backend natively supports Advanced Pro speeds when operating on 4G networks).
        //
        //   2. Step 2: Tertiary Resolution (Generic Generation Fallbacks)
        //      If the SoC is unknown or not listed in references/soc_reference.md, but the cellular generation has been verified (e.g., specs state "5G" or "4G LTE" but lack any other technical details):
        //        • 5G Verified → Default to Tier 3: 5G Sub-6 (Limited/regional bands).
        //        • 4G Verified → Default to Tier 5: 4G LTE (Basic).
        //        • 3G Verified → Default to Tier 6: 3G.
        //        • 2G Verified → Default to Tier 7: 2G.
        //
        //   3. Step 3: Quaternary Fail-Safe (Absolute Fallback)
        //      If the cellular specifications are completely missing, and the device's SoC is unknown or not listed in references/soc_reference.md, assign the device to Tier 7: 2G as a strict fail-safe to prevent over-scoring, and flag the entry for manual verification.
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
      // SCORING GOAL: Evaluates subscriber identity module format support, network flexibility, and hardware transceiver concurrency.
      "slot_configuration": {
        "value": "Tier 1: Dual eSIM / iSIM + Physical Slot",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 8.00
        // SCORING GUIDELINE: Identify the physical slot and digital SIM configuration for the specific regional variant/SKU (Stock Keeping Unit) under review.
        // Match the device's verified specifications to the highest matching Tier below. Mappings require verifying both digital SIM capability and physical tray presence. Use the following exact Tier Names for "value" and related numbers for "subscore":
        //
        // • "Tier 1: Dual eSIM / iSIM + Physical Slot" → 8.00
        //   Condition: Must support (at least) two simultaneously active digital profiles (Multiple Enabled Profiles - MEP) AND contain a physical Nano-SIM slot.
        //   Verification Rules:
        //     1. Dual active eSIM/iSIM is confirmed (keywords: "Dual eSIM", "Dual iSIM", "MEP support", "multiple enabled profiles on eSIM", "supports two active eSIMs", "eSIM + eSIM", "iSIM + iSIM", "eSIM + iSIM").
        //     2. AND a physical slot is verified (keywords: "Nano-SIM", "physical SIM slot", "SIM card slot").
        //
        // • "Tier 2: Single eSIM / iSIM + Physical Slot" → 7.00
        //   Condition: Must support one active digital profile alongside a physical Nano-SIM slot.
        //   Verification Rules:
        //     1. Single active eSIM/iSIM is confirmed (keywords: "eSIM", "embedded SIM", "iSIM", "integrated SIM").
        //     2. AND a physical slot is verified (keywords: "Nano-SIM", "physical SIM slot", "SIM card slot").
        //     3. AND the device does NOT support dual active eSIM/iSIM (if dual active eSIM/iSIM + physical SIM is supported, map to Tier 1).
        //
        // • "Tier 3: Dual Physical Nano-SIM Slots" → 5.50
        //   Condition: Must support two physical Nano-SIM slots with NO electronic/programmable SIM (eSIM/iSIM) support.
        //   Verification Rules:
        //     1. Two physical slots are verified (keywords: "Dual SIM (Nano-SIM)", "2x Nano-SIM", "Dual physical Nano-SIM slots", "Dual SIM (2 Nano-SIMs)").
        //     2. AND no eSIM or iSIM is supported.
        //
        // • "Tier 4: Dual eSIM / iSIM Only" → 5.00
        //   Condition: Must support two active digital profiles but contain NO physical SIM card slot.
        //   Verification Rules:
        //     1. Dual active eSIM/iSIM is confirmed (keywords: "Dual eSIM", "two active eSIMs", "Dual iSIM", "MEP support", "eSIM + eSIM", "iSIM + iSIM", "eSIM + iSIM").
        //     2. AND the lack of a physical slot is verified (keywords: "no physical SIM slot", "eSIM-only", "eSIM only - USA", "no SIM card slot").
        //
        // • "Tier 5: Single eSIM / iSIM Only" → 1.50
        //   Condition: Must support one active digital profile and contain NO physical SIM card slot.
        //   Verification Rules:
        //     1. Single active eSIM/iSIM is confirmed (keywords: "eSIM", "embedded SIM", "iSIM", "integrated SIM").
        //     2. AND the lack of a physical slot is verified (keywords: "eSIM only", "no physical SIM slot").
        //     3. AND the device does NOT support dual active eSIM/iSIM (if dual active eSIM/iSIM is supported, map to Tier 3).
        //
        // • "Tier 6: Single Physical Nano-SIM Only" → 0.00
        //   Condition: Must support exactly one physical Nano-SIM slot with NO dual-SIM or eSIM/iSIM support.
        //   Verification Rules:
        //     1. One physical slot is verified (keywords: "Single SIM (Nano-SIM)", "Nano-SIM", "1x Nano-SIM slot").
        //     2. AND no eSIM, iSIM, or second physical slot is supported.
        //
        // AMBIGUITY RESOLUTION & FALLBACK RULES (MANDATORY):
        // Automated agents must resolve incomplete, ambiguous, or missing slot specifications using the following 4-step logic hierarchy.
        // Steps are applied in order. Once a step produces a definitive Tier mapping, subsequent steps are skipped.
        //
        // 1. Step 1: Regional Variant Override (Stock Keeping Unit - SKU)
        //    • SIM hardware differs by region for the same device model. Retrieve the regional target from identity.target_region.value to identify the specific regional Stock Keeping Unit (SKU) of the device under review before applying any other rule.
        //    • Chinese / Hong Kong / Macau regional SKUs (identity.target_region.value is "China"): Regardless of the model's eSIM capability in other markets, devices sold in mainland China, Hong Kong, and Macau typically have eSIM disabled or omitted entirely, and instead ship with two physical Nano-SIM slots. If the device under review is a Chinese / Hong Kong / Macau SKU, map to "Tier 3: Dual Physical Nano-SIM Slots". Exception: if the SKU is verified as single-SIM only (e.g., iPhone XS, iPhone 12 mini in these regions), map to "Tier 6: Single Physical Nano-SIM Only".
        //    • US iPhone 14 and all subsequent iPhone models (US regional SKUs, identity.target_region.value is "US"): These specific SKUs have removed the physical Nano-SIM tray entirely and operate exclusively via eSIM. Map to "Tier 4: Dual eSIM / iSIM Only".
        //    • If the regional SKU target is not "China" and is not a US eSIM-only iPhone model, proceed to Step 2.
        //
        // 2. Step 2: eSIM / iSIM Detection
        //    • If the device specifications mention eSIM or iSIM support (keywords: "eSIM", "iSIM", "embedded SIM", "integrated SIM", "Dual eSIM", "MEP"):
        //        - First, resolve whether the device supports Multiple Enabled Profiles (MEP), which allows two digital SIM profiles to be active simultaneously:
        //            • MEP is supported if any of these conditions are met:
        //                - Specs explicitly state "Dual eSIM", "Dual iSIM", "MEP", "two active eSIMs", "two active iSIMs", "eSIM + eSIM", "iSIM + iSIM", "eSIM + iSIM", or similar dual-profile keywords.
        //                - OR the device belongs to a series that natively supports MEP (see the MEP Reference Table below).
        //            • MEP is NOT supported if the device does not match any of the above conditions (i.e., specs only mention generic "eSIM" without dual-profile keywords, and the device is not in the MEP Reference Table).
        //        - Then, combine the MEP resolution with the physical slot status:
        //            • MEP supported + physical Nano-SIM slot present → Map to "Tier 1: Dual eSIM / iSIM + Physical Slot".
        //            • MEP supported + no physical slot → Map to "Tier 4: Dual eSIM / iSIM Only".
        //            • MEP NOT supported + physical Nano-SIM slot present → Map to "Tier 2: Single eSIM / iSIM + Physical Slot".
        //            • MEP NOT supported + no physical slot → Map to "Tier 5: Single eSIM / iSIM Only".
        //    • If the device specifications do NOT mention eSIM or iSIM at all, proceed to Step 3.
        //
        //    MEP REFERENCE TABLE (devices with native Multiple Enabled Profiles support, by brand and series):
        //    ┌─────────────────────┬────────────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────┐
        //    │ Brand               │ MEP-Capable Series (and all subsequent models)                 │ Non-MEP eSIM Series (single active profile only)         │
        //    ├─────────────────────┼────────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
        //    │ Apple               │ iPhone 13, 14, 15, 16 series and subsequent                    │ iPhone XR, XS, XS Max, 11, 12 series, SE 2nd/3rd Gen     │
        //    │ Google              │ Pixel 7, 7 Pro, 7a, 8, 9 series and subsequent                 │ Pixel 3a, 4, 4a, 5, 5a, 6, 6 Pro, 6a                     │
        //    │ Samsung             │ Galaxy S23, S24, S25, S26 series; Z Fold5, Z Flip5             │ Galaxy S20, S21, S22 series; Z Fold2/3/4, Z Flip/3/4;    │
        //    │                     │ and subsequent Galaxy S / Z Fold / Z Flip series               │ Galaxy A-series (A54, A55, etc.); Galaxy FE series       │
        //    │ OnePlus             │ OnePlus 11 and subsequent series                               │ No earlier OnePlus models support eSIM                   │
        //    │ Xiaomi              │ Xiaomi 13, 13T, 14, 14T, 15 series and subsequent              │ No earlier Xiaomi models support eSIM                    │
        //    │ Sony                │ Xperia 1 V, 5 V and subsequent series                          │ Xperia 1 IV, 5 IV, 1 III (single eSIM profile only)      │
        //    │ Motorola            │ Razr 40, Razr 50; Edge 40 Pro, Edge 50 Pro and subsequent      │ Earlier Motorola models with eSIM (single profile only)  │
        //    │ All other brands    │ No verified MEP support. If specs explicitly confirm           │ If eSIM is mentioned without MEP keywords, treat as      │
        //    │                     │ "Dual eSIM" or "MEP", treat as MEP-capable.                    │ single profile. If no eSIM mentioned, proceed to Step 3. │
        //    └─────────────────────┴────────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────┘
        //    Note: This table applies to Global / US / European Union - EU / Canada - CA variants only. Chinese / Hong Kong / Macau variants of any of these models do not support eSIM (handled by Step 1).
        //
        // 3. Step 3: Physical-Only SIM Detection
        //    • If the device has no eSIM/iSIM but specifications confirm physical SIM slot(s):
        //        - Two physical Nano-SIM slots (keywords: "Dual SIM (Nano-SIM)", "2x Nano-SIM"): Map to "Tier 3: Dual Physical Nano-SIM Slots".
        //          Note: "Hybrid Dual SIM" trays (where the user must choose between a second SIM and a microSD card) are physically capable of dual-SIM usage. Map to "Tier 3: Dual Physical Nano-SIM Slots". The microSD trade-off is scored separately in Section 6.9 (Storage Expandability).
        //        - One physical Nano-SIM slot only (keywords: "Single SIM (Nano-SIM)", "1x Nano-SIM"): Map to "Tier 6: Single Physical Nano-SIM Only".
        //    • If no SIM information is available at all, proceed to Step 4.
        //
        // 4. Step 4: Absolute Fallback (Missing Specifications)
        //    • If SIM slot specifications are completely missing and no SIM-related keywords appear anywhere in the device's specifications:
        //        - Release year before 2018: Default to "Tier 6: Single Physical Nano-SIM Only".
        //        - Release year 2018 or later: Default to "Tier 3: Dual Physical Nano-SIM Slots".
        //          Rationale: Step 4 is only reached when SIM specifications are completely missing (Step 2 found no eSIM keywords, and Step 3 found no physical SIM keywords). While the physical SIM configuration is unstated, dual physical Nano-SIM is the most likely configuration for devices released in 2018 or later, hence map to "Tier 3: Dual Physical Nano-SIM Slots". However, because mapping to Tier 3 risks artificially over-scoring devices that might actually be single physical SIM (Tier 6), this is a tentative "most likely" fallback and the entry MUST be flagged for manual verification to maintain conservative data integrity.
        //    • Flag the entry for manual verification.
      },
      "concurrency_mode": {
        "value": "Tier 2: Dual SIM Dual Standby (DSDS)",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 1.00
        // SCORING GUIDELINE: Identify the transceiver hardware capability that manages concurrent cellular connections.
        // Match the verified specifications to the highest applicable Tier below:
        //
        // • "Tier 1: Dual SIM Dual Active (DSDA)" → 2.00
        //   Description: Dedicated dual radio transceivers allowing simultaneous voice/data sessions on both lines.
        //   Keywords in Specs: "Dual active", "DSDA", "Dual SIM Dual Active", "concurrent calls on both SIMs".
        //
        // • "Tier 2: Dual SIM Dual Standby (DSDS)" → 1.00
        //   Description: Shared single transceiver. One line goes temporarily offline when the other is actively on a call.
        //   Keywords in Specs: "dual stand-by", "DSDS", "Dual SIM Dual Standby", "Dual SIM (Nano-SIM, dual stand-by)".
        //
        // • "Tier 3: Single Standby / None" → 0.00
        //   Description: No concurrent standby capability (Single-SIM devices).
        //   Keywords in Specs: "Single SIM", "Single Standby", "1x Nano-SIM Only".
        //
        // AMBIGUITY RESOLUTION & FALLBACK RULES (MANDATORY):
        // Automated agents must resolve incomplete, ambiguous, or missing transceiver concurrency specifications using the following 2-step logic hierarchy:
        //
        // 1. Step 1: Default DSDS for Dual-SIM Devices
        //    • If the device is determined to be dual-SIM (whether physical dual-SIM, eSIM + physical, or dual eSIM) but the transceiver concurrency mode (DSDA vs. DSDS) is not explicitly stated, default to "Tier 2: Dual SIM Dual Standby (DSDS)".
        //    • Upgrading to "Tier 1: Dual SIM Dual Active (DSDA)" is strictly forbidden unless the device specification sheet or trusted third-party technical reviews explicitly confirm concurrent voice or concurrent voice+data sessions on both lines simultaneously.
        //
        // 2. Step 2: Single-SIM Override
        //    • If the slot_configuration resolved to a single-SIM tier (Tier 5 or Tier 6), map concurrency_mode to "Tier 3: Single Standby / None" (regardless of any missing or ambiguous specifications), since concurrent standby is physically impossible with only one active SIM profile.
      },
      "scores": {
        "predicted": 9.00,
        // SCORING GUIDELINE: scores.predicted = slot_configuration.subscore + concurrency_mode.subscore
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 9.00,
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
        //   • "Tier 1: Wi-Fi 7"    → 10.00
        //     - Definition: 802.11be standard (Extremely High Throughput). Supports 320 Megahertz (MHz) channels, 4K Quadrature Amplitude Modulation (QAM), and Multi-Link Operation (MLO).
        //     - Specification Parsing: Specs list "Wi-Fi 7", "802.11be", or "Wi-Fi be".
        //   • "Tier 2: Wi-Fi 6E"   → 8.00
        //     - Definition: 802.11ax standard adding support for the 6 Gigahertz (GHz) spectrum, reducing congestion.
        //     - Specification Parsing: Specs list "Wi-Fi 6E", "802.11ax (6 GHz)", "6 GHz band support", or "Tri-band" (2.4 GHz + 5 GHz + 6 GHz).
        //   • "Tier 3: Wi-Fi 6"    → 7.00
        //     - Definition: 802.11ax standard on 2.4 GHz and 5 GHz bands. Improved efficiency and performance in dense environments.
        //     - Specification Parsing: Specs list "Wi-Fi 6", "802.11ax" (generically without 6 GHz or tri-band specified), or "Wi-Fi ax".
        //   • "Tier 4: Wi-Fi 5"    → 5.00
        //     - Definition: 802.11ac standard.
        //     - Specification Parsing: Specs list "Wi-Fi 5", "802.11ac", or "Wi-Fi ac".
        //   • "Tier 5: Wi-Fi 4"    → 3.00
        //     - Definition: 802.11n standard.
        //     - Specification Parsing: Specs list "Wi-Fi 4", "802.11n", or "Wi-Fi n".
        //   • "Tier 6: Wi-Fi ≤ 3"   → 0.00
        //     - Definition: 802.11g or older legacy wireless technologies.
        //     - Specification Parsing: Specs list "802.11a/b/g", "802.11b/g", or any older wireless standard.
        //
        // AMBIGUITY RESOLUTION & MAPPING RULES (MANDATORY):
        //   If the Wi-Fi standard is completely unstated or missing in the device specifications, assign a conservative standard based on the device's release year:
        //     - Release year 2024 or later → Default to Tier 3: Wi-Fi 6.
        //     - Release year 2019 to 2023  → Default to Tier 4: Wi-Fi 5.
        //     - Release year 2016 to 2018  → Default to Tier 5: Wi-Fi 4.
        //     - Release year before 2016   → Default to Tier 6: Wi-Fi ≤ 3.
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
      // SCORING GOAL: Evaluates Bluetooth (BT) version and high-fidelity wireless audio codec support.
      "bluetooth_version": {
        "value": "Tier 2: 5.3",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 4.50
        // SCORING GUIDELINE: Identify the physical Bluetooth (BT) version supported by the transceiver. Use the following exact Tier Names for "value" with related scores for "subscore" (apply the highest applicable tier):
        //   • "Tier 1: 5.4"               → 5.00
        //     Definition: Supports Bluetooth (BT) 5.4 standards.
        //   • "Tier 2: 5.3"               → 4.50
        //     Definition: Supports Bluetooth (BT) 5.3 standards.
        //   • "Tier 3: 5.2"               → 4.00
        //     Definition: Supports Bluetooth (BT) 5.2 standards.
        //   • "Tier 4: 5.1"               → 2.50
        //     Definition: Supports Bluetooth (BT) 5.1 standards.
        //   • "Tier 5: 5.0"               → 2.00
        //     Definition: Supports Bluetooth (BT) 5.0 standards.
        //   • "Tier 6: 4.2 / 4.1 / 4.0"   → 1.00
        //     Definition: Supports Bluetooth (BT) 4.2, 4.1, or 4.0 legacy standards.
        //   • "Tier 7: < 4.0"             → 0.00
        //     Definition: Supports Bluetooth (BT) standards older than 4.0.
        //
        // AMBIGUITY RESOLUTION & FALLBACK RULES (MANDATORY):
        // Automated agents must resolve incomplete, ambiguous, or missing Bluetooth (BT) version specifications using the following 3-step logic hierarchy, applied sequentially:
        //
        // 1. Step 1: Secondary Resolution (System-on-Chip [SoC] Platform Mapping)
        //    Retrieve the chipset name from identity.hardware_configuration.chipset.value. Look up the native Bluetooth (BT) version using the bluetooth_version column defined for this chipset in the canonical reference file references/soc_reference.md, then map this version to the corresponding tier.
        //
        // 2. Step 2: Tertiary Resolution (Temporal Era Fallback)
        //    If both specifications and chipset name are unstated or unmapped, apply defaults based on the device's release year retrieved from the year component of identity.release_date.value:
        //      - Release year >= 2024: Default to "Tier 2: 5.3".
        //      - Release year 2021 to 2023: Default to "Tier 3: 5.2".
        //      - Release year 2018 to 2020: Default to "Tier 5: 5.0".
        //      - Release year 2016 to 2017: Default to "Tier 6: 4.2 / 4.1 / 4.0".
        //      - Release year before 2016: Default to "Tier 7: < 4.0".
        //
        // 3. Step 3: Quaternary Fail-Safe (Absolute Fallback)
        //    If the release year is also unknown, default to "Tier 7: < 4.0" and flag for manual verification.
      },
      "codec_supported": {
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
        "subscore": 3.50
        // SCORING GUIDELINE: Identify the highest supported Bluetooth (BT) audio codec tier. Use the following exact Tier Names for "value" with related scores for "subscore" (apply the highest applicable tier):
        //   • "Tier 1: Lossless"   → 5.00
        //     Definition: CD-quality audio without data loss. Qualifying terms: Qualcomm aptX Lossless, Savitech LHDC V5 (LHDC V5 Lossless), Huawei L2HC 3.0.
        //   • "Tier 2: High-Res"   → 3.50
        //     Definition: High-resolution lossy transmission up to 990 Kilobits per second (kbps). Qualifying terms: Sony LDAC, Savitech LHDC (v1/v2/v3/v4), Qualcomm aptX Adaptive, Qualcomm aptX HD, Samsung Seamless Codec (SSC), Samsung Scalable Codec, Samsung UHQ-BT, Huawei L2HC (1.0/2.0).
        //   • "Tier 3: Standard"   → 0.00
        //     Definition: Standard lossy compression. Qualifying terms: Advanced Audio Coding (AAC), Subband Codec (SBC), Low Complexity Communication Codec (LC3) for LE Audio, Qualcomm aptX Classic, Qualcomm aptX Low Latency (aptX LL).
        //
        // VALUE_DETAILS GUIDELINE (Advanced Traceability): List all specific supported Bluetooth (BT) codecs found in specs. To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}. IMPORTANT: Be exhaustive and include all terms that apply, for all tiers.
        //
        // AMBIGUITY RESOLUTION & FALLBACK RULES (MANDATORY):
        // If no codecs are explicitly declared in the specifications or reviews (which is the default case for most databases), automated agents must execute the following 4-step logic hierarchy, applied sequentially. Each step is only reached if all prior steps failed to resolve:
        //
        // 1. Step 1: Apple Ecosystem Override
        //    Retrieve the brand string from identity.brand. If the brand is Apple (any iPhone model, any year): Apple's iOS restricts Bluetooth audio transmission to AAC and SBC codecs. So far no iPhone has ever natively supported LDAC, aptX, or any High-Res/Lossless codec over its internal Bluetooth stack. Force map to "Tier 3: Standard".
        //
        // 2. Step 2: Android OS Version Check (AOSP LDAC Baseline)
        //    If the device is NOT Apple, retrieve the Android OS version from 5_software_and_longevity.operating_system_version.value. Since Android 8.0 (Oreo, released 2017), the Android Open Source Project (AOSP) natively integrates Sony LDAC as a system-level Bluetooth audio codec. This means ALL non-Apple devices running Android 8.0 or later — regardless of brand, model, or price tier — natively support LDAC transmission. This includes all Samsung Galaxy phones (S-series, A-series, M-series, J-series running Android 8.0+), all Xiaomi/Redmi, all OnePlus, all Oppo/Realme, all Vivo, all Google Pixel, all Motorola, all Sony Xperia, all Nothing, all Fairphone, and all other Android 8.0+ devices.
        //    Default to "Tier 2: High-Res".
        //    Exception: Devices running Android Go Edition may have LDAC disabled in their stripped-down Bluetooth stack. If the device is verified as running Android Go Edition, map to "Tier 3: Standard" instead.
        //    If the device is running Android 7.x or earlier (or the OS version is unknown), proceed to Step 3.
        //
        // 3. Step 3: Temporal Era Fallback
        //    If the Android OS version is unknown or below 8.0, fall back to the release year retrieved from the year component of identity.release_date.value:
        //      - Release year >= 2018: Default to "Tier 2: High-Res" (rationale: Android 8.0+ adoption was near-universal for new devices from 2018 onward, making LDAC support the statistical baseline).
        //      - Release year before 2018: Default to "Tier 3: Standard" (rationale: pre-Android 8.0 devices did not include LDAC in the AOSP base).
        //
        // 4. Step 4: Absolute Fallback
        //    If the release year is also unknown, default to "Tier 3: Standard" and flag for manual verification.
      },
      "perceived_quality_bonus": {
        "value": "Samsung Seamless Codec (SSC) Optimization",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.50
        // SCORING GUIDELINE: Identify any applicable perceived quality or ecosystem audio optimization bonuses. Use the following exact names for "value" and related scores for "subscore":
        //   • "Apple iOS AAC Optimization"                 → 1.50
        //   • "Samsung Seamless Codec (SSC) Optimization"  → 0.50
        //   • "None"                                       → 0.00
        //
        // RESOLUTION & MAPPING RULES (MANDATORY):
        // Automated agents must map the perceived quality bonus based on the device's brand and operating system:
        //   1. Apple iOS AAC Optimization (+1.50): Map if the brand is Apple (any iPhone model, any year).
        //   2. Samsung Seamless Codec (SSC) Optimization (+0.50): Map if the brand is Samsung (any Galaxy model running Android 8.0 or later).
        //   3. None (+0.00): Map for all other brands, models, or configurations.
      },
      "scores": {
        "predicted": 8.50,
        // SCORING GUIDELINE: scores.predicted = Clamp(bluetooth_version.subscore + codec_supported.subscore + perceived_quality_bonus.subscore, 0.00, 10.00).
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
      // SCORING GOAL: Evaluates secure unlock mechanisms. The overall score is calculated as:
      //   Biometrics Score = Primary Biometric Subscore (Max 8.00) + Redundancy Premium (Max 2.00)
      "primary_biometric": {
        "value": "Tier 1: Ultrasonic Under-Display Fingerprint",
        "value_details": {
          "Tier 1: Ultrasonic Under-Display Fingerprint": [
            { "name": "Qualcomm 3D Sonic Gen 2", "source": "TBD", "exact_extract": "Proof pending" }
          ],
          "Tier 2: 3D Face Unlock (Structured Light/ToF)": [],
          "Tier 3: Capacitive Physical Fingerprint (Side/Rear/Front)": [],
          "Tier 4: Optical Under-Display Fingerprint": [],
          "Tier 5: Secure 2D Face Unlock (Class 3 Certified)": [],
          "Tier 6: Iris Scanner (Dedicated IR Hardware)": [],
          "Tier 7: Legacy Swipe Fingerprint Sensor": [],
          "Tier 8: No Secure Biometrics (PIN/Pattern Only)": []
        },
        "subscore": 8.00
        // SCORING GUIDELINE: Identify the highest available secure biometric unlock method.
        // Use the following exact Tier Names for "value" with related scores as subscore:
        //   • "Tier 1: Ultrasonic Under-Display Fingerprint"              → 8.00
        //     - Definition: Three-Dimensional (3D) acoustic fingerprint scanner reading ridges and pores under the screen via sound waves.
        //     - Keywords: "Ultrasonic fingerprint", "Qualcomm 3D Sonic", "3D Sonic Max", "sonic sensor".
        //     - Hardware Reference List (Devices uniquely matching this tier):
        //         * Samsung Galaxy S Series (main flagships): Galaxy S10, S10+, S10 5G, S20, S20+, S20 Ultra, S21, S21+, S21 Ultra, S22, S22+, S22 Ultra, S23, S23+, S23 Ultra, S24, S24+, S24 Ultra, S25, S25+, S25 Ultra, and S25 Slim.
        //         * Samsung Galaxy Note Series (flagships): Galaxy Note 10, Note 10+, Note 10+ 5G, Note 20, and Note 20 Ultra.
        //         * Google Pixel Series (main flagships): Google Pixel 9, Pixel 9 Pro, Pixel 9 Pro XL, and Pixel 10 series.
        //         * Vivo Premium Series: Vivo X Note, X80 Pro, X90 Pro+, X100 Ultra, X200 Pro, X200 Pro Mini, X200 Ultra, X Fold, X Fold+, X Fold 2, and X Fold 3 Pro.
        //         * iQOO Premium Series: iQOO 9 Pro, 10 Pro, 11 Pro, 12 Pro, and 13.
        //         * Xiaomi Premium Series: Xiaomi 15, Xiaomi 15 Pro, and Xiaomi 15 Ultra.
        //         * OnePlus Premium Series: OnePlus 13.
        //         * Oppo Premium Series: Oppo Find X8 Ultra.
        //         * Honor Premium Series: Honor Magic 7, Magic 7 Pro, and Magic 7 Ultimate.
        //         * Meizu Premium Series: Meizu 18, 18 Pro, 18s, 18s Pro, 20, 20 Pro, 20 Infinity, 21, and 21 Pro.
        //         * Sharp Aquos Series: Sharp Aquos R6, R7, R8 Pro, and R9 Pro.
        //   • "Tier 2: 3D Face Unlock (Structured Light/ToF)"             → 8.00
        //     - Definition: Three-Dimensional (3D) depth-mapped facial scanning projecting an infrared (IR) dot grid or measuring Time-of-Flight (ToF).
        //     - Keywords: "3D Face ID", "Structured Light", "ToF 3D camera", "infrared camera" (when verified acting as biometric unlock).
        //     - Hardware Reference List (Devices uniquely matching this tier):
        //         * Apple TrueDepth camera system in iPhone X, XR, XS, XS Max, 11, 11 Pro, 11 Pro Max, 12, 12 mini, 12 Pro, 12 Pro Max, 13, 13 mini, 13 Pro, 13 Pro Max, 14, 14 Plus, 14 Pro, 14 Pro Max, 15, 15 Plus, 15 Pro, 15 Pro Max, 16, 16 Plus, 16 Pro, and 16 Pro Max.
        //         * Huawei Mate Series: Mate 20 Pro, Mate 30, Mate 30 Pro, Mate 40, Mate 40 Pro, Mate 50, Mate 50 Pro, Mate 60, Mate 60 Pro, and Mate XT.
        //         * Honor Magic Series: Magic 3 Pro, Magic 4 Pro, Magic 5 Pro, Magic 6 Pro, and Magic 7 Pro/Ultimate.
        //         * Xiaomi Series: Mi 8 Explorer Edition and Mi 9 Explorer Edition.
        //   • "Tier 3: Capacitive Physical Fingerprint (Side/Rear/Front)" → 7.00
        //     - Definition: Standard physical capacitive fingerprint sensor integrated in buttons or outer chassis (includes under-glass capacitive sensors).
        //     - Keywords: "Side-mounted fingerprint", "rear-mounted fingerprint", "front-mounted fingerprint", "capacitive fingerprint".
        //     - Hardware Reference List (Devices uniquely matching this tier):
        //         * Apple Touch ID devices: iPhone 5s, 6, 6 Plus, 6s, 6s Plus, 7, 7 Plus, 8, 8 Plus, and all iPhone Special Edition (SE) models.
        //         * Samsung: Galaxy S10e (utilizing side-mounted capacitive fingerprint sensor).
        //         * Google: Pixel 9 Pro Fold (utilizing side-mounted capacitive fingerprint sensor), and all legacy Pixel 1 to 5a series (utilizing rear-mounted capacitive fingerprint sensors).
        //         * Vivo: X Fold 3 standard model (utilizing side-mounted capacitive fingerprint sensor).
        //   • "Tier 4: Optical Under-Display Fingerprint"                 → 6.00
        //     - Definition: Under-glass camera capturing a Two-Dimensional (2D) optical image of the fingerprint using display light illumination.
        //     - Keywords: "Optical under-display fingerprint", "under-display optical", "under-screen fingerprint".
        //     - Hardware Reference List (Devices uniquely matching this tier):
        //         * Samsung: Galaxy S10 Lite, Note 10 Lite, and all Fan Edition (FE) variants (including Galaxy S20 FE, S21 FE, and S23 FE).
        //         * Google: Google Pixel 6, 6 Pro, 6a, 7, 7 Pro, 7a, 8, 8 Pro, and 8a.
        //         * Vivo: X80, X80 Lite, X90, X90 Pro, X100, X100 Pro, X100s, X100s Pro, and X200 standard model.
        //         * Xiaomi: All under-display models earlier than Xiaomi 15 (including Xiaomi 12, 13, and 14 series).
        //         * OnePlus: All under-display models earlier than OnePlus 13 (including OnePlus 8, 9, 10, 11, and 12 series).
        //         * Oppo: All under-display models earlier than Find X8 Ultra (including Find X2, X3, X5, X6, and X7 series).
        //   • "Tier 5: Secure 2D Face Unlock (Class 3 Certified)"         → 5.50
        //     - Definition: Front-facing camera face unlock officially certified for Android Class 3 (Strong) security, allowing payment and banking authentication.
        //     - Keywords: "Class 3 face unlock", "payment-grade face unlock" (verified with secure chip hardware processing, e.g., Titan M2).
        //     - Hardware Reference List (Devices uniquely matching this tier):
        //         * Google: Pixel 8, Pixel 8 Pro, Pixel 8a, Pixel 9, Pixel 9 Pro, Pixel 9 Pro XL, and Pixel 10 series.
        //   • "Tier 6: Iris Scanner (Dedicated IR Hardware)"              → 4.50
        //     - Definition: Dedicated infrared (IR) sensor mapping iris details.
        //     - Keywords: "Iris scanner", "iris recognition".
        //     - Hardware Reference List (Devices uniquely matching this tier):
        //         * Samsung: Galaxy S8, S8+, Note 8, S9, S9+, and Note 9.
        //   • "Tier 7: Legacy Swipe Fingerprint Sensor"                   → 1.50
        //     - Definition: Obsolete capacitive sensor strip requiring dragging the finger across it.
        //     - Keywords: "Swipe fingerprint sensor".
        //     - Hardware Reference List (Devices uniquely matching this tier):
        //         * Samsung: Galaxy S5 and Galaxy Note 4.
        //   • "Tier 8: No Secure Biometrics (PIN/Pattern Only)"           → 0.00
        //     - Definition: Relying on Personal Identification Number (PIN), pattern, password, or basic insecure software-only Two-Dimensional (2D) front-camera face unlock.
        //     - Keywords: "2D face unlock", "face recognition" (without secure Class 3 certification).
        //     - Clarification: Includes all standard software-only 2D face unlocks on brands like standard Samsung (e.g., S-series and A-series), OnePlus, Xiaomi, Motorola, Oppo, and Realme.
        //
        // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are arrays of objects.
        // To ensure proof for each value, each item in the array MUST be an object: {"name": "Marketing Name", "source": "URL", "exact_extract": "Verbatim proof"}.
        // ALL supported biometric methods present on the device must be entered under their respective tiers (e.g. if the device has both Optical Fingerprint and standard 2D Face, both must be documented in their respective array), not just the highest-scoring method.
        // If a software-based secure Face Unlock is downgraded due to regional software/ecosystem overrides, its entry MUST be documented under "Tier 8: No Secure Biometrics (PIN/Pattern Only)" instead of "Tier 5: Secure 2D Face Unlock (Class 3 Certified)". To ensure strict traceability, the "exact_extract" field for this entry MUST include both the verified source statement and the specific justification for the downgrade (e.g., "Downgraded from Tier 5 to Tier 8: Regional GMS [Google Mobile Services] or payment API absence in mainland China").
        //
        // AMBIGUITY RESOLUTION & FALLBACK RULES (MANDATORY):
        // Automated agents must resolve incomplete, ambiguous, or regional biometric specifications using the following 3-step logic hierarchy:
        //
        // 1. Step 1: Regional Software & Ecosystem Override
        //    Software-based facial recognition (specifically Tier 5: Secure 2D Face Unlock (Class 3 Certified)) depends on OS vendor APIs (such as Google Mobile Services / GMS) to perform payment-grade authentication.
        //    • Check the target region of the device SKU (Stock Keeping Unit) from identity.target_region.value:
        //      - For models targeted at regions where payment API integration is absent by default (e.g., mainland China SKUs where GMS is absent, identity.target_region.value is "China"), software-based secure Face Unlock MUST be downgraded. Map the face unlock method to "Tier 8: No Secure Biometrics (PIN/Pattern Only)" instead of Tier 5.
        //      - If the manufacturer's regional product documentation indicates that software-based face unlock cannot be used for Google Wallet / payment authentication in that specific market, downgrade it to "Tier 8: No Secure Biometrics (PIN/Pattern Only)".
        //    • Hardware-based depth sensors (Tier 2: 3D Face Unlock) and secure fingerprint readers (Tiers 1, 3, and 4) are NOT subject to this regional software downgrade, as their security is hardware-enforced and integrated with local payment apps (e.g., WeChat Pay and Alipay in China).
        //
        // 2. Step 2: Component Fallback Rules
        //    If specifications are ambiguous:
        //      - Under-display or generic fingerprint (unspecified location/technology): Fallback to Tier 4 (Optical Under-Display Fingerprint).
        //      - Physical key fingerprint (side/rear/front button): Map to Tier 3 (Capacitive Physical Fingerprint).
        //      - Face unlock / facial recognition (unspecified class): Fallback to Tier 8 (No Secure Biometrics).
        //
        // 3. Step 3: Quaternary Fail-Safe (Absolute Fallback)
        //    - Complete absence of biometric specifications: Fallback to Tier 8 (No Secure Biometrics).
      },
      "redundancy_premium": {
        "value": 0.00,
        "source": "TBD",
        "exact_extract": "Proof pending"
        // SCORING GUIDELINE: Bonus value (0.00 or 2.00) indicating if the device features a secondary secure unlock method.
        // Set value to 2.00 if premium is awarded, otherwise 0.00.
        //
        // MAPPING & CONCURRENCY RULES (MANDATORY):
        //   1. Redundancy requires combining a fingerprint sensor with a face or iris scanner. Two fingerprint sensors (e.g., side capacitive + under-display optical) or dual face unlock methods do NOT qualify.
        //   2. Set to 2.00 ONLY if BOTH a secure fingerprint sensor (Ultrasonic, Capacitive Physical, or Optical Under-Display Fingerprint; subscore >= 6.00) AND a secure face/iris scanner (3D Face Unlock, Secure 2D Face Unlock, or Iris Scanner; subscore >= 4.50) are present and supported.
        //   3. Cascading Regional Downgrade: If the software-based secure Face Unlock (Tier 5) is downgraded to standard 2D Face (Tier 8) under the Regional Software & Ecosystem Override, it no longer meets the secondary security threshold (subscore >= 4.50). In this case, the redundancy premium MUST be set to 0.00, unless the device has another qualified secure face scanner (e.g. 3D Face ID).
      },
      "scores": {
        "predicted": 8.00,
        // SCORING GUIDELINE: scores.predicted = Clamp(primary_biometric.subscore + redundancy_premium.value, 0.00, 10.00).
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
      // SCORING GOAL: Evaluates physical hardware sensors integrated into the device, divided across three distinct sub-suites: Inertial & Motion Sensing Suite (Max 4.50 pts), Environmental & Ambient Sensing Suite (Max 3.50 pts), and Advanced Spatial, Optical & Specialized Suite (Max 2.00 pts). Total score is the sum of subscores, strictly clamped between 0.00 and 10.00 points.
      //
      // DATA VERIFICATION PRECEDENCE & OMNI-SCAN RULES:
      // 1. DEDICATED HARDWARE EXCLUSIVITY: Points are awarded ONLY to dedicated physical silicon ICs or hardware photodiodes. Software features, AI algorithms, ISP post-processing, sensor fusion, and software emulation ALWAYS score 0.00.
      // 2. OMNI-SCAN CROSS-REFERENCE: Primary spec repositories (GSMArena, PhoneArena, DeviceSpecifications) occasionally omit standard physical sensors (e.g. Ambient Light Sensor or Compass). The evaluator MUST cross-reference official manufacturer datasheets or teardown reports before marking a sensor as absent.
      // 3. ABSENCE / FALLBACK RULE: If a sensor is not explicitly documented in manufacturer technical specs, official datasheets, or reputable public repositories, it MUST be scored as 0.00 (absent/unsupported).
      //
      "inertial_and_motion_sensing_suite": {
        // SCORING GOAL: Evaluates physical motion, rotation, and direction telemetry sensors (Inertial Measurement Unit / IMU). Maximum available subscore is 4.50 points.
        "gyroscope": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 2.00
          // SCORING GUIDELINE: Evaluates physical 3-axis rotational angular velocity sensing capability.
          //   • true  → 2.00 (Dedicated physical Micro-Electro-Mechanical Systems / MEMS gyroscope IC measuring rotational angular velocity).
          //   • false → 0.00 (Virtual gyroscope software emulation or absent).
          //   Keywords & Evidence (true): "Gyroscope", "3-axis gyro", "MEMS gyro", "hardware gyro", "gyro sensor".
          //   Keywords & Evidence (false): "Virtual Gyro", "Software Gyro", "Gyro emulated", "No physical gyro".
          //   AI DECISION TREE: If official specs or hardware teardowns explicitly state "Virtual gyro", "Software gyroscope", or confirm the absence of a physical MEMS gyro IC, set value: false (0.00 pt).
        },
        "magnetometer": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.50
          // SCORING GUIDELINE: Evaluates physical geomagnetic field sensing for map heading direction.
          //   • true  → 1.50 (Dedicated physical Hall-effect or magnetoresistive digital compass IC measuring Earth's magnetic field).
          //   • false → 0.00 (No magnetic sensor IC present).
          //   Keywords & Evidence: "Compass", "Magnetometer", "Digital compass", "e-compass", "3-axis compass", "geomagnetic sensor".
        },
        "accelerometer": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.00
          // SCORING GUIDELINE: Evaluates physical linear acceleration and orientation sensing capability.
          //   • true  → 1.00 (Dedicated physical MEMS accelerometer IC measuring linear acceleration forces and gravity vectors).
          //   • false → 0.00 (Lacks physical acceleration sensing hardware).
          //   Keywords & Evidence: "Accelerometer", "g-sensor", "3-axis accelerometer", "motion sensor".
        }
      },
      "environmental_and_ambient_sensing_suite": {
        // SCORING GOAL: Evaluates hardware sensors detecting surrounding environmental conditions (light, proximity distance, atmospheric pressure, magnetic covers). Maximum available subscore is 3.50 points.
        "proximity_sensor": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.25
          // SCORING GUIDELINE: Evaluates call screen state and face distance detection.
          //   • true  → 1.25 (Dedicated physical Infrared / IR LED emitter + photodiode under display glass for <5cm detection).
          //   • false → 0.00 (Virtual software, ultrasonic audio algorithm e.g. Elliptic Labs AI Virtual Proximity, or touch digitizer).
          //   Keywords & Evidence (true): "Proximity sensor", "Hardware proximity", "IR proximity", "Optical proximity".
          //   Keywords & Evidence (false): "Virtual proximity", "Elliptic Labs", "Software proximity", "Ultrasonic proximity".
          //   AI DECISION TREE: If official specs, GSMArena, or teardowns state "Virtual proximity sensing" or Elliptic Labs algorithms, set value: false (0.00 pt).
        },
        "ambient_light_and_color_sensor": {
          "value": "Hardware Ambient Light Sensor + Hardware Color Sensor",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 1.25
          // SCORING GUIDELINE: Evaluates front-facing display auto-brightness lux sensing and screen color tint matching (e.g. Apple True Tone). Strictly dedicated to display visual adaptation, separate from rear camera photo spectral sensors.
          // Use the following exact string values with related scores:
          //   • "Hardware Ambient Light Sensor + Hardware Color Sensor" → 1.25 (Physical Ambient Light Sensor / ALS plus dedicated multi-channel ambient color/spectrum IC, e.g. Apple True Tone, Red-Green-Blue-Clear-Infrared / RGBCIR sensor).
          //   • "Standard Hardware Ambient Light Sensor"                → 1.00 (Standard single-channel monochrome/RGB physical light sensor for standard auto-brightness).
          //   • "Virtual / Camera-Based Light Sensing"                  → 0.00 (Periodic front-camera image sampling or absence of auto-brightness hardware).
        },
        "barometer": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.75
          // SCORING GUIDELINE: Evaluates atmospheric pressure and elevation tracking capability.
          //   • true  → 0.75 (Dedicated physical MEMS pressure sensor IC with 0.1 hPa precision for stair elevation and GNSS altitude lock).
          //   • false → 0.00 (Lacks physical barometric pressure hardware).
          //   Keywords & Evidence: "Barometer", "Altimeter", "Pressure sensor", "Barometric pressure".
        },
        "hall_effect_sensor": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.25
          // SCORING GUIDELINE: Evaluates magnetic proximity sensing for accessories and foldables.
          //   • true  → 0.25 (Dedicated magnetic field sensor IC for flip cover closure, Moto Mods, and foldable lid closure state).
          //   • false → 0.00 (Lacks magnetic cover proximity hardware).
          //   Keywords & Evidence: "Hall sensor", "Hall effect", "Magnetic flip sensor".
        }
      },
      "advanced_spatial_optical_and_specialized_suite": {
        // SCORING GOAL: Evaluates optional photography-assist, 3D spatial scanning, multi-spectral, and specialized industrial/health hardware sensors. Maximum available subscore is capped at 2.00 points.
        "spatial_depth_and_laser_autofocus": {
          "value": "Laser Autofocus Rangefinder",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.35
          // SCORING GUIDELINE: Evaluates 3D spatial mesh scanning, Time-of-Flight depth sensing, and camera Laser Autofocus rangefinding.
          // Use the following exact string values with related scores:
          //   • "LiDAR Scanner / 3D Spatial"        → 1.00 (Real-time 3D spatial laser scanner emitting point-cloud laser arrays, e.g. Apple iPhone 12–16 Pro LiDAR Scanner).
          //   • "3D ToF Camera / DepthVision"       → 0.60 (3D Time-of-Flight / ToF infrared depth sensor module, e.g. Samsung Galaxy S10 5G/S20 Ultra, Note 10+, Huawei P30/P40 Pro DepthVision).
          //   • "Laser Autofocus Rangefinder"       → 0.35 (Standalone infrared laser rangefinder diode dedicated to fast low-light and macro camera focus lock, e.g. Google Pixel 2–9, Samsung Galaxy S21–25 Ultra, LG G3–G8).
          //   • "Standard Dual Camera / None"       → 0.00 (Standard dual-camera parallax software bokeh or no optical depth hardware).
        },
        "spectral_and_color_assist": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.50
          // SCORING GUIDELINE: Evaluates rear camera photo/video multi-channel spectral sensing and AC artificial light flicker frequency detection. Strictly dedicated to camera capture quality (eliminating fluorescent banding and calibrating white balance), separate from display ambient light sensors.
          //   • true  → 0.50 (Dedicated multi-channel color spectrum sensor or photodiode measuring ambient light spectrum and AC flicker frequency).
          //   • false → 0.00 (Standard camera auto white balance without auxiliary spectral hardware).
          //   Keywords & Evidence: "Spectral sensor", "Flicker sensor", "Color spectrum sensor", "Multi-spectral sensor", "Hasselblad color calibration sensor", "LG color spectrum".
        },
        "industrial_and_health_sensors": {
          "value": "Tier 6: Standard Consumer Suite / None",
          "value_details": {
            "Tier 1: Active Microbolometer Thermal": [],
            "Tier 2: Dedicated Physiological Suite": [],
            "Tier 3: Standalone Infrared Temperature Sensor": [],
            "Tier 4: Volatile Organic Compounds Air Quality Sensor": [],
            "Tier 5: Ultraviolet Sensor": [],
            "Tier 6: Standard Consumer Suite / None": [
              { "name": "None", "source": "N/A", "exact_extract": "N/A" }
            ]
          },
          "subscore": 0.00
          // SCORING GUIDELINE: Identify all active specialized industrial and health hardware sensors present on the device.
          // Use the following exact Tier Names with related scores to be added together for the subscore:
          //   • "Tier 1: Active Microbolometer Thermal"                 → 0.50
          //     - Definition: Integrated FLIR or Infiray Long-Wave Infrared / LWIR microbolometer thermal imaging camera module.
          //     - Keywords: "Thermal camera", "FLIR Lepton", "Infiray thermal", "Microbolometer", "LWIR thermal".
          //     - Hardware Reference List (Devices uniquely matching this tier):
          //         * CAT Rugged Series: CAT S60, CAT S62 Pro.
          //         * Blackview Armor Thermal Series: Blackview BV9800 Pro, BV9900 Pro, BL8800 Pro, Armor 19T, Armor 27T Pro.
          //         * Ulefone Armor Thermal Series: Ulefone Armor 9, Armor 11T 5G, Armor 18T, Armor 25T Pro.
          //         * AGM Series: AGM G1 Pro, AGM G2 Guardian.
          //   • "Tier 2: Dedicated Physiological Suite"                 → 0.35
          //     - Definition: Physical optical photodiode sensor array measuring Heart Rate Monitor (HRM) and Blood Oxygen Saturation (SpO2).
          //     - Keywords: "Heart rate sensor", "HRM sensor", "SpO2 sensor", "Pulse oximeter", "Heart rate photodiode".
          //     - Hardware Reference List (Devices uniquely matching this tier):
          //         * Samsung Galaxy S Series: Galaxy S5, S6, S6 edge, S7, S7 edge, S8, S8+, S9, S9+, S10, and S10+.
          //         * Samsung Galaxy Note Series: Galaxy Note 4, Note 5, Note 8, and Note 9.
          //   • "Tier 3: Standalone Infrared Temperature Sensor"        → 0.20
          //     - Definition: Non-contact infrared skin and object surface temperature measurement sensor.
          //     - Keywords: "Infrared temperature sensor", "Skin temperature sensor", "Thermometer sensor", "IR temp sensor".
          //     - Hardware Reference List (Devices uniquely matching this tier):
          //         * Google Pixel Series: Google Pixel 8 Pro, Pixel 9 Pro, Pixel 9 Pro XL, and Pixel 9 Pro Fold.
          //         * Honor Series: Honor V40 5G.
          //   • "Tier 4: Volatile Organic Compounds Air Quality Sensor" → 0.20
          //     - Definition: Dedicated Volatile Organic Compounds (VOC) indoor air quality gas sensor Integrated Circuit (IC) chip.
          //     - Keywords: "VOC sensor", "Air quality sensor", "Gas sensor", "Sensirion VOC sensor".
          //     - Hardware Reference List (Devices uniquely matching this tier):
          //         * CAT Rugged Series: CAT S61.
          //   • "Tier 5: Ultraviolet Sensor"                            → 0.20
          //     - Definition: Dedicated Ultraviolet (UV) index photodiode sensor Integrated Circuit (IC) chip measuring solar UV radiation intensity.
          //     - Keywords: "UV sensor", "Ultraviolet sensor", "UV index sensor".
          //     - Hardware Reference List (Devices uniquely matching this tier):
          //         * Samsung Galaxy Series: Galaxy Note 4 and Galaxy S5.
          //   • "Tier 6: Standard Consumer Suite / None"                → 0.00
          //     - Definition: No specialized thermal, physiological, or environmental hardware sensors.
          //     - Keywords: "No thermal camera", "No heart rate sensor", "Standard sensor suite".
          //
          // VALUE_DETAILS GUIDELINE (Advanced Traceability): Dictionary where keys are Tier Names and values are arrays of objects.
          // To ensure technical proof for each present hardware component, each item in an active tier array MUST be an object containing the specific component's Marketing Name or Integrated Circuit (IC) chip designation: {"name": "Marketing / Hardware Component Name", "source": "URL", "exact_extract": "Verbatim proof"}. Do NOT repeat the Tier Name string itself in the "name" field.
          // ALL detected active specialized sensors present on the device MUST be entered under their respective tier array keys for multi-sensor hardware traceability (e.g. CAT S61 having {"name": "FLIR Lepton Thermal Camera", ...} under Tier 1 and {"name": "Sensirion VOC Gas Sensor", ...} under Tier 4).
          // For devices with no specialized sensors (Tier 6: Standard Consumer Suite / None), populate Tier 6 in value_details with {"name": "None", "source": "N/A", "exact_extract": "N/A"} to ensure all mandatory fields are fully present.
          //
          // 🚨 *** VERY IMPORTANT *** FEATURE STACKING & TRACEABILITY RULE: The field "value" takes the primary highest-scoring tier name. The subscore is calculated as the additive sum of subscores across all active tiers present in value_details (e.g. FLIR Thermal 0.50 + VOC Gas 0.20 = 0.70 pts).
        }
      },
      "scores": {
        "predicted": 8.85,
        "calculation_formula": "Clamp(inertial_and_motion_sensing_suite.gyroscope.subscore + inertial_and_motion_sensing_suite.magnetometer.subscore + inertial_and_motion_sensing_suite.accelerometer.subscore + environmental_and_ambient_sensing_suite.proximity_sensor.subscore + environmental_and_ambient_sensing_suite.ambient_light_and_color_sensor.subscore + environmental_and_ambient_sensing_suite.barometer.subscore + environmental_and_ambient_sensing_suite.hall_effect_sensor.subscore + advanced_spatial_optical_and_specialized_suite.spatial_depth_and_laser_autofocus.subscore + advanced_spatial_optical_and_specialized_suite.spectral_and_color_assist.subscore + advanced_spatial_optical_and_specialized_suite.industrial_and_health_sensors.subscore, 0.00, 10.00)",
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 8.85,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "7_7_nfc_and_uwb": {
      // SCORING GOAL: Evaluates short-range wireless communication (Near-Field Communication / NFC) and precision spatial positioning hardware (Ultra-Wideband / UWB). The overall score is calculated as the sum of physical NFC presence (Max 6.00 pts), dedicated UWB transceiver presence (Max 3.50 pts), and off-state power reserve card emulation (+0.50 pt), strictly clamped between 0.00 and 10.00 points.
      "nfc_hardware_capability": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.00
        // SCORING GUIDELINE: Identify physical Near-Field Communication (NFC) hardware controller presence from official specification sheets or public specification repositories (GSMArena, PhoneArena).
        //   • true  → 6.00 (Physical 13.56 MHz Near-Field Communication controller and antenna present. Enables touchless mobile wallet payments, public transit pass-through, smart tag scanning, and device pairing).
        //   • false → 0.00 (Device completely omits physical Near-Field Communication radio hardware).
        //   Specification Keywords (true): "NFC: Yes", "NFC: Supported", "NFC: Yes (market/region dependent)", "NFC", "Near Field Communication", "NFC-enabled".
        //   Specification Keywords (false): "NFC: No", "NFC: Unsupported", "NFC: Absent", or omitted from connectivity specs.
        //
        // AMBIGUITY RESOLUTION & REGIONAL SKU LOGIC TREE (MANDATORY):
        // Automated agents MUST resolve incomplete or regional NFC specifications using the following 3-step logic hierarchy:
        //
        // 1. Step 1: Regional Stock Keeping Unit (SKU) Resolution
        //    NFC presence varies by region for certain mid-range and budget smartphone lines (e.g. Xiaomi Redmi Note, Samsung Galaxy A, Motorola Moto G, Poco, Realme series).
        //    • Retrieve the target region and exact regional model alias (SKU code) from identity.target_region.value and identity.model_aliases.
        //    • If official specification sheets list regional SKU variation (e.g., "Yes (market/region dependent)"):
        //        - Automated agents MUST verify the official regional product page, regional datasheet, or regulatory filing (CE, FCC, TELEC) for that specific regional SKU model code (e.g., verifying whether the specific EU/US/East Asia model suffix features NFC vs. IN/LATAM/SEA model suffix).
        //        - Set value: true (6.00 pts) ONLY if official documentation for that exact regional SKU model code explicitly confirms physical NFC hardware presence.
        //        - Set value: false (0.00 pts) if official regional documentation confirms NFC absence or omits NFC for that specific regional SKU model code.
        //        - If the exact regional SKU specification cannot be conclusively verified for the target region across 3+ sources, default to false (0.00 pts) as a conservative fail-safe to prevent unverified score inflation.
        //
        // 2. Step 2: Secondary Spec Verification (Omni-Scan Rule)
        //    If a primary database (e.g., GSMArena) omits the NFC field, cross-reference at least two (2) secondary sources (official product spec page, regulatory filings, PhoneArena, DeviceSpecifications).
        //    • If any verified source confirms physical NFC hardware present → Set value: true (6.00 pts).
        //    • If all sources confirm NFC absence → Set value: false (0.00 pts).
        //
        // 3. Step 3: Quaternary Fail-Safe (Absolute Fallback)
        //    If NFC presence cannot be verified after exhaustive search across 3+ sources:
        //      • Default to false (0.00 pts) as a conservative fail-safe to prevent unverified score inflation.
      },
      "uwb_spatial_ranging": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 3.50
        // SCORING GUIDELINE: Identify physical Ultra-Wideband (UWB) pulse radio hardware transceiver presence from official specs or the Hardware Reference List.
        //   • true  → 3.50 (Physical high-frequency pulse radio transceiver present operating at 3.1–10.6 GHz, delivering ~10cm Time-of-Flight spatial distance positioning and 3D directional bearing).
        //   • false → 0.00 (Device lacks UWB pulse radio silicon, specs state "UWB: No"/omit UWB, or device model is unlisted on the Reference List).
        //   Specification Keywords (true): "UWB: Yes", "Ultra Wideband (UWB) support", "Ultra-Wideband", "Apple U1 chip", "Apple U2 chip", "NXP Trimension UWB", "Qorvo UWB".
        //   Hardware Reference List (Comprehensive List of Verified UWB Devices across ALL Brands):
        //       * Apple: iPhone 11, 11 Pro, 11 Pro Max, 12, 12 mini, 12 Pro, 12 Pro Max, 13, 13 mini, 13 Pro, 13 Pro Max, 14, 14 Plus, 14 Pro, 14 Pro Max, 15, 15 Plus, 15 Pro, 15 Pro Max, 16, 16 Plus, 16 Pro, 16 Pro Max, and subsequent main iPhone series (excluding SE series).
        //       * Samsung: Galaxy Note 20 Ultra; Galaxy S21+, S21 Ultra, S22+, S22 Ultra, S23+, S23 Ultra, S24+, S24 Ultra, S25+, S25 Ultra; Galaxy Z Fold 2, Z Fold 3, Z Fold 4, Z Fold 5, Z Fold 6, and subsequent Z Fold series.
        //       * Google: Pixel 6 Pro, Pixel 7 Pro, Pixel 8 Pro, Pixel 9 Pro, Pixel 9 Pro XL, Pixel 9 Pro Fold, and subsequent Pro/Fold Pixel series.
        //       * Xiaomi: Xiaomi MIX 4, Xiaomi 13 Ultra, Xiaomi 14 Ultra, Xiaomi 15 Ultra, Xiaomi Fold 3, Fold 4.
        //       * Vivo: Vivo X Fold 2, X Fold 3 Pro, X100 Pro, X100 Ultra, X200 Pro.
        //       * Oppo / OnePlus: Oppo Find X5 Pro, Find X6 Pro, Find X7 Ultra, Find N3; OnePlus 12, OnePlus 13.
        //       * Motorola: Moto Edge 50 Ultra, Moto Razr 50 Ultra / Razr+ (2024).
        //       * Honor: Honor Magic 6 Ultimate, Magic 6 RSR, Magic V2 RSR, Magic V3.
        //       * Meizu: Meizu 20 Pro, Meizu 20 Infinity, Meizu 21 Pro.
      },
      "depleted_battery_power_reserve": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.50
        // SCORING GUIDELINE: Identify hardware micro-power routing that allows NFC card emulation, digital vehicle/home key unlocking, or offline device finding for up to 5 hours after primary OS shutdown due to 0% battery.
        //   • true  → 0.50 (Official documentation confirms off-state micro-power reserve, or device is listed on the Power Reserve Hardware Reference List).
        //   • false → 0.00 (Off-state power reserve is unconfirmed, unstated, or device model is unlisted on the Reference List).
        //   Specification Keywords (true): "Express Cards with Power Reserve", "Reserve power for transit cards", "Offline Digital Key power reserve", "Powered Off Finding", "Off-state card emulation".
        //   Hardware Reference List (Comprehensive List of Verified Power Reserve Devices across ALL Brands):
        //       * Apple: All iPhones from iPhone XS/XR (2018) onward (iPhone XS, XS Max, XR, 11, 11 Pro, 11 Pro Max, 12, 12 mini, 12 Pro, 12 Pro Max, 13, 13 mini, 13 Pro, 13 Pro Max, 14, 14 Plus, 14 Pro, 14 Pro Max, 15, 15 Plus, 15 Pro, 15 Pro Max, 16, 16 Plus, 16 Pro, 16 Pro Max, SE 2nd Gen, SE 3rd Gen, and subsequent main iPhone series). Legacy iPhones (iPhone X, 8, 7, 6s) lack power reserve (0.00 pt).
        //       * Samsung: Galaxy Note 20 Ultra; Galaxy S20 Ultra, S21+, S21 Ultra, S22+, S22 Ultra, S23+, S23 Ultra, S24+, S24 Ultra, S25+, S25 Ultra; Galaxy Z Fold 2, Z Fold 3, Z Fold 4, Z Fold 5, Z Fold 6, and subsequent Z Fold series.
        //       * Google: Pixel 8, Pixel 8 Pro, Pixel 8a, Pixel 9, Pixel 9 Pro, Pixel 9 Pro XL, Pixel 9 Pro Fold, and subsequent Pro/Fold Pixel series.
        //       * Xiaomi: Xiaomi MIX 4, Xiaomi 12 Pro, 13, 13 Pro, 13 Ultra, 14, 14 Pro, 14 Ultra, 15, 15 Pro, 15 Ultra, MIX Fold 2, Fold 3, Fold 4.
        //       * Vivo: Vivo X Fold 2, X Fold 3 Pro, X90 Pro+, X100 Pro, X100 Ultra, X200 Pro.
        //       * Oppo / OnePlus: Oppo Find X5 Pro, Find X6 Pro, Find X7 Ultra, Find N2, Find N3; OnePlus 11, OnePlus 12, OnePlus 13, OnePlus Open.
        //       * Honor: Honor Magic 4 Pro, Magic 5 Pro, Magic 6 Pro, Magic 6 Ultimate, Magic V2, Magic V3.
        //       * Huawei: Huawei Mate 30 Pro, Mate 40 Pro, Mate 50 Pro, Mate 60 Pro, Mate X3, Mate X5, P40 Pro, P50 Pro, Pura 70 Pro, Pura 70 Ultra.
        //       * Motorola: Moto Edge 50 Ultra, Moto Razr 50 Ultra / Razr+ (2024).
      },
      "scores": {
        "predicted": 10.00,
        "calculation_formula": "Clamp(nfc_hardware_capability.subscore + uwb_spatial_ranging.subscore + depleted_battery_power_reserve.subscore, 0.00, 10.00)",
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 10.00,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "7_8_usb_port_speed_and_external_display_capabilities": {
      // SCORING GOAL: Evaluates physical Universal Serial Bus (USB) port data transfer protocol speeds, native DisplayPort Alternate Mode (DP Alt Mode) wired video output capabilities, and native windowed desktop operating system (OS) software environments.
      // SCOPE: Evaluates the maximum hardware capability supported by the smartphone device itself, NOT the bundled inbox cable.
      //
      "usb_protocol_and_interface_speed": {
        "value": "Tier 2: USB 3.2 Gen 2 / USB 3.1 Gen 2 | 10 Gbps SuperSpeed+",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.00
        // SCORING GUIDELINE: Identify the physical USB protocol version and maximum data transfer bus bandwidth supported by the port controller. Use the following exact Tier Names for "value" with related scores as subscore:
        //   • "Tier 1: USB4 / USB 3.2 Gen 2x2 / Thunderbolt-compatible | 20–40 Gbps"          → 8.00
        //     - Definition: Physical port supporting 20 to 40 Gigabits per second (Gbps) data throughput via Universal Serial Bus 4 (USB4), Universal Serial Bus 3.2 Gen 2x2 (USB 3.2 Gen 2x2), or Thunderbolt 3/4 (TB3/TB4) over Universal Serial Bus Type-C (USB Type-C).
        //     - Keywords: "USB4", "Thunderbolt 3", "Thunderbolt 4", "USB 3.2 Gen 2x2", "40Gbps", "20Gbps".
        //   • "Tier 2: USB 3.2 Gen 2 / USB 3.1 Gen 2 | 10 Gbps SuperSpeed+"                   → 7.00
        //     - Definition: Physical port supporting 10 Gbps SuperSpeed+ data throughput via USB 3.2 Gen 2 or USB 3.1 Gen 2 standards over USB Type-C.
        //     - Specification Keywords: "USB 3.2 Gen 2", "USB 3.1 Gen 2", "10Gbps", "SuperSpeed+", "USB 3.2 Gen2", "USB 3.1 Gen2".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Apple: iPhone 15 Pro, iPhone 15 Pro Max, iPhone 16 Pro, iPhone 16 Pro Max, and subsequent Pro/Pro Max iPhone series.
        //         * Samsung: Galaxy S24 Ultra, Galaxy S25 Ultra, Galaxy Z Fold 5, Galaxy Z Fold 6, and subsequent Ultra/Z Fold flagship series.
        //         * Asus: ROG Phone 8 Pro, ROG Phone 7 Ultimate.
        //         * Sony: Xperia 1 VI, Xperia 1 V.
        //         * Vivo: Vivo X100 Ultra, Vivo X200 Pro.
        //         * Xiaomi: Xiaomi 14 Ultra, Xiaomi 15 Ultra.
        //   • "Tier 3: USB 3.2 Gen 1 / USB 3.1 Gen 1 / USB 3.0 | 5 Gbps SuperSpeed"           → 5.50
        //     - Definition: Physical port supporting 5 Gbps SuperSpeed data throughput via USB 3.2 Gen 1, USB 3.1 Gen 1, or USB 3.0 standards over USB Type-C.
        //     - Specification Keywords: "USB 3.2 Gen 1", "USB 3.1 Gen 1", "USB 3.0", "5Gbps", "SuperSpeed", "USB 3.2 Gen1", "USB 3.1 Gen1", "USB 3.0 Type-C".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Google: Pixel 8, Pixel 8 Pro, Pixel 9, Pixel 9 Pro, Pixel 9 Pro XL, Pixel 9 Pro Fold, and subsequent Pro/Fold Pixel series.
        //         * Samsung: Galaxy S24 base, Galaxy S24+, Galaxy S23, Galaxy S23+, Galaxy S22 series, Galaxy S21 series, Galaxy S20 series, Galaxy S10 series, Galaxy S9 series, Galaxy S8 series, Galaxy Note 20, Galaxy Note 10, Galaxy Note 9, Galaxy Note 8.
        //         * OnePlus: OnePlus 12, OnePlus 11, OnePlus 10 Pro, OnePlus 9 Pro, OnePlus 8 Pro.
        //         * Motorola: Edge 50 Pro, Edge 50 Ultra, ThinkPhone.
        //   • "Tier 4: USB 3.0 10-pin Micro-B | 5 Gbps SuperSpeed"                            → 4.50
        //     - Definition: Legacy 10-pin Micro Universal Serial Bus 3.0 (10-pin Micro-USB 3.0) physical connector supporting 5 Gbps SuperSpeed data throughput.
        //     - Specification Keywords: "Micro-USB 3.0", "USB 3.0 Micro-B", "10-pin Micro-USB", "microUSB v3.0".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Samsung: Galaxy Note 3, Galaxy S5.
        //   • "Tier 5: USB 2.0 High Speed over USB Type-C | 480 Mbps"                         → 2.50
        //     - Definition: Reversible USB Type-C physical connector limited internally to Universal Serial Bus 2.0 (USB 2.0) High Speed protocol throughput (480 Megabits per second / Mbps).
        //     - Specification Keywords: "USB 2.0 Type-C", "USB Type-C 2.0", "USB Type-C", "USB-C", "Type-C 2.0", "480Mbps".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Apple: iPhone 15 base, iPhone 15 Plus, iPhone 16 base, iPhone 16 Plus, and subsequent base/Plus Type-C iPhones.
        //         * Samsung: Galaxy A55, Galaxy A35, Galaxy A54, Galaxy A34, Galaxy A15, Galaxy M series, Galaxy F series.
        //         * Xiaomi / Poco / Redmi: Redmi Note 13 Pro, Poco X6 Pro, Poco F6, Xiaomi 13 Lite.
        //         * OnePlus: OnePlus Nord 3, Nord 4, OnePlus 12R.
        //         * Nothing: Nothing Phone (1), Nothing Phone (2), Nothing Phone (2a).
        //   • "Tier 6: USB 2.0 High Speed over Apple Lightning | 480 Mbps"                    → 2.25
        //     - Definition: Legacy proprietary Apple 8-pin Lightning physical connector limited to USB 2.0 High Speed protocol throughput (480 Mbps).
        //     - Specification Keywords: "Lightning", "8-pin Lightning", "Lightning connector", "USB 2.0 Lightning".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Apple: All iPhones from iPhone 5 (2012) through iPhone 14 Pro Max (2022) (e.g., iPhone 14, 14 Plus, 14 Pro, 14 Pro Max, iPhone 13 series, iPhone 12 series, iPhone 11 series, iPhone XS/XR, iPhone X, iPhone 8, iPhone 7, iPhone 6s, iPhone 6, iPhone SE 1st/2nd/3rd Gen).
        //   • "Tier 7: USB 2.0 High Speed over 5-pin Micro-USB | 480 Mbps"                    → 1.50
        //     - Definition: Legacy non-reversible 5-pin Micro Universal Serial Bus (5-pin Micro-USB) physical connector supporting USB 2.0 High Speed protocol throughput (480 Mbps).
        //     - Specification Keywords: "microUSB 2.0", "Micro-USB", "5-pin Micro-USB", "microUSB".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Samsung: Galaxy J7, Galaxy J5, Galaxy A10 (2019).
        //         * Xiaomi: Redmi 9A, Redmi 9C, Redmi 7A.
        //         * Motorola: Moto G6 Play, Moto E5.
        //   • "Tier 8: Micro-USB 1.1 / Charge-only pinout / Legacy 30-pin | < 12 Mbps / None" → 0.00
        //     - Definition: Obsolete physical connectors (Apple 30-pin, Micro-USB 1.1) supporting under 12 Mbps Full Speed data throughput, or connectors lacking data pin wiring (charge-only).
        //     - Specification Keywords: "USB 1.1", "Apple 30-pin", "Charge-only", "No data transfer".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Apple: iPhone 4s, iPhone 4, iPhone 3GS, iPhone 3G, original iPhone (30-pin dock connector).
        //
        // AMBIGUITY RESOLUTION & LOGIC TREE FOR PROTOCOL & CONNECTOR (MANDATORY):
        // Automated agents MUST execute the following 4-step logic hierarchy sequentially to categorize usb_protocol_and_interface_speed:
        //
        // 1. Step 1: Generic "USB 3.x" Specification Disambiguation
        //    • If specs state "USB 3.0", "USB 3.1", "USB 3.2", or "USB 3.2 Gen 1" without explicitly advertising "10 Gbps", "Gen 2", or "10Gbps": Default to Tier 3 (5 Gbps) for USB Type-C, or Tier 4 for 10-pin Micro-B.
        //    • Assign Tier 2 (10 Gbps) STRICTLY when "10 Gbps", "10Gbps", "USB 3.2 Gen 2", or "USB 3.1 Gen 2" is explicitly documented in official product specifications or verified by hardware review teardowns.
        //
        // 2. Step 2: Unstated Protocol / Generic "USB Type-C" Default Rule
        //    • If official specifications list "USB Type-C", "USB-C", or "USB 2.0 Type-C" without explicitly advertising "USB 3.0", "USB 3.1", "USB 3.2", "5Gbps", "10Gbps", or "USB4": Default to Tier 5 (USB 2.0 over USB Type-C).
        //
        // 3. Step 3: Connector Type Identification & Fallback Hierarchy
        //    If protocol version is specified in datasheet text but physical connector type is omitted:
        //      • Determine connector type from official device hardware specifications.
        //      • Apple iPhone released in 2023 or later (via identity.release_date.value) → USB Type-C.
        //      • Apple iPhone released between 2012 and 2022 (via identity.release_date.value) → Apple 8-pin Lightning (Tier 6).
        //      • Apple iPhone released before 2012 (via identity.release_date.value) → Apple 30-pin (Tier 8).
        //      • Android / non-Apple devices released in 2021 or later (via identity.release_date.value) → USB Type-C.
        //      • Android / non-Apple devices released between 2011 and 2020 (via identity.release_date.value) → Cross-reference official hardware specs for 5-pin Micro-USB (Tier 7) vs USB Type-C.
        //      • Android / non-Apple devices released before 2011 (via identity.release_date.value) → Cross-reference official hardware specs for Micro-USB 1.1 / Charge-only (Tier 8) vs 5-pin Micro-USB 2.0 (Tier 7).
        //
        // 4. Step 4: Absolute Fail-Safe Fallback
        //    If USB specifications are completely unstated and connector type cannot be physically verified across 3+ sources:
        //      • Apple iPhone released in 2023 or later (via identity.release_date.value) → Default to Tier 5 (USB 2.0 over USB Type-C).
        //      • Apple iPhone released between 2012 and 2022 (via identity.release_date.value) → Default to Tier 6 (USB 2.0 over Apple Lightning).
        //      • Apple iPhone released before 2012 (via identity.release_date.value) → Default to Tier 8 (Apple 30-pin).
        //      • Android / non-Apple devices released in 2021 or later (via identity.release_date.value) → Default to Tier 5 (USB 2.0 over USB Type-C).
        //      • Android / non-Apple devices released between 2011 and 2020 (via identity.release_date.value) → Default to Tier 7 (USB 2.0 over 5-pin Micro-USB).
        //      • Android / non-Apple devices released before 2011 or charge-only pinout (via identity.release_date.value) → Default to Tier 8 (Micro-USB 1.1 / Charge-only pinout).
      },
      "wired_display_output": {
        "value": "Tier 1: Native DisplayPort Alternate Mode / Direct USB-C Video Output",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 1.50
        // SCORING GUIDELINE: Identify the physical video output pipeline over the USB port. Part 2 evaluates hardware presence of native video output capability only, independent of UI software implementation. Use the following exact Tier Names for "value" with related scores as subscore:
        //   • "Tier 1: Native DisplayPort Alternate Mode / Direct USB-C Video Output" → 1.50
        //     - Definition: Dedicated physical multiplexing hardware enabling native DisplayPort Alternate Mode (DP Alt Mode) video signal output directly over USB Type-C to external displays.
        //     - Specification Keywords & Evidence: "DisplayPort Alt Mode", "DP Alt Mode", "DisplayPort over Type-C", "DisplayPort", "USB-C Video Output", "HDMI over USB-C", "External Display Support", "Display Out", "Native wired video output over USB-C", or official confirmation of wired workstation environments (wired Samsung DeX, wired Motorola Ready For / Smart Connect, wired Huawei EMUI Desktop, wired Honor Magic Desktop, wired LG Screen+, wired Xiaomi Workstation Mode).
        //     - Hardware Reference List (Devices matching this tier):
        //         * Apple: iPhone 15, iPhone 15 Plus, iPhone 15 Pro, iPhone 15 Pro Max, iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, and all subsequent Type-C iPhones.
        //         * Samsung: Galaxy S8, S8+, S9, S9+, S10, S10+, S10e, S20, S20+, S20 Ultra, S21, S21+, S21 Ultra, S22, S22+, S22 Ultra, S23, S23+, S23 Ultra, S24, S24+, S24 Ultra, S25, S25+, S25 Ultra; Galaxy Note 8, Note 9, Note 10, Note 10+, Note 20, Note 20 Ultra; Galaxy Z Fold 2, Z Fold 3, Z Fold 4, Z Fold 5, Z Fold 6 (excluding Z Flip series, which omit DP Alt Mode).
        //         * Google: Pixel 8, Pixel 8 Pro, Pixel 8a, Pixel 9, Pixel 9 Pro, Pixel 9 Pro XL, Pixel 9 Pro Fold (enabled via official Android 15 firmware update).
        //         * Motorola: Edge+, Edge 20 Pro, Edge 30 Pro, Edge 40 Pro, Edge 50 Pro, Edge 50 Ultra, ThinkPhone.
        //         * OnePlus: OnePlus 7, 7 Pro, 7T, 7T Pro, 8, 8 Pro, 9, 9 Pro, 10 Pro, 11, 12, OnePlus Open.
        //         * Asus: ROG Phone 2, 3, 5, 6, 7, 8; Zenfone 9, 10, 11 Ultra.
        //         * Sony: Xperia 1 series (I through VI), Xperia 5 series (I through V).
        //         * Huawei: Mate 10, 20, 30, 40, 50, 60 series; P20, P30, P40, P50, Pura 70 series.
        //         * LG: LG G5, G6, G7, G8, V20, V30, V40, V50, V60, Velvet, Wing.
        //   • "Tier 2: Legacy Wired Display Output / MHL / SlimPort"                     → 0.75
        //     - Definition: Legacy wired video output technologies (Mobile High-Definition Link / MHL or SlimPort) operating over Micro-USB or early Type-C connectors requiring powered external active converter adapters.
        //     - Specification Keywords & Evidence: "MHL", "Mobile High-Definition Link", "SlimPort", "MHL 2.0", "MHL 3.0", "MHL support".
        //     - Hardware Reference List (Devices matching this tier):
        //         * Samsung: Galaxy S3, S4, S5, Note 2, Note 3, Note 4.
        //         * HTC: One M7, One M8, One M9.
        //         * Sony: Xperia Z1, Z2, Z3, Z5.
        //         * LG: Nexus 4, Nexus 5, LG G2, LG G3 (SlimPort).
        //   • "Tier 3: No Wired Video Output / Audio / Data / Charge Only"                → 0.00
        //     - Definition: Lacks physical DisplayPort multiplexing hardware. Video output over native USB cable is unsupported (requires wireless casting via Miracast / Chromecast or active DisplayLink USB graphics adapters).
        //     - Specification Keywords & Evidence: "No video output", "DisplayPort: No", "DP Alt Mode: No", or omitted video output specs.
        //     - Hardware Reference List (Devices matching this tier):
        //         * Apple: All Lightning-connector iPhones (iPhone 14 Pro Max and older; Lightning-to-HDMI adapter uses AirPlay video decoding IC inside adapter, not native DP Alt Mode).
        //         * Google: Pixel 1, Pixel 2, Pixel 3, Pixel 4, Pixel 5, Pixel 6, Pixel 7 series (disabled at hardware/kernel level prior to Pixel 8 / Android 15).
        //         * Samsung: All Galaxy Z Flip series (Z Flip 1 through Z Flip 6 omit DP Alt Mode hardware), all Galaxy A series, Galaxy M series, Galaxy F series.
        //         * Xiaomi / Poco / Redmi: Almost all Xiaomi standard/Pro models (e.g. Xiaomi 13, 14, Redmi Note series, Poco series omit DP Alt Mode; only selected Ultra models include it).
        //
        // AMBIGUITY RESOLUTION & FIRMWARE QUALIFICATION LOGIC TREE FOR DISPLAY OUTPUT (MANDATORY):
        // Automated agents MUST resolve wired video output specifications using the following 3-step logic hierarchy:
        //
        // 1. Step 1: Firmware Baseline Policy
        //    Evaluate devices according to the latest official manufacturer firmware or OS update supported by the model.
        //    • Example (Google Pixel 8 Series): Google Pixel 8 launched with DP Alt Mode disabled in software, but Google officially enabled native DisplayPort Alternate Mode in the official Android 15 OS update. Therefore, Google Pixel 8, 8 Pro, 8a, 9, 9 Pro, 9 Pro XL, and 9 Pro Fold qualify for "Tier 1: Native DisplayPort Alternate Mode / Direct USB-C Video Output".
        //
        // 2. Step 2: Indirect Workstation Confirmation Rule
        //    If technical specifications do not explicitly list "DP Alt Mode", but officially confirm a qualifying native wired desktop environment (wired Samsung DeX, wired Motorola Ready For / Smart Connect, wired Huawei EMUI Desktop, wired Honor Magic Desktop, wired LG Screen+, wired Xiaomi Workstation Mode), the device MUST be assigned to "Tier 1: Native DisplayPort Alternate Mode / Direct USB-C Video Output", because these desktop software environments physically require the underlying DisplayPort Alternate Mode hardware pipeline to function.
        //
        // 3. Step 3: Unstated Video Output Fallback Rule
        //    If specifications make no mention of DisplayPort, DP Alt Mode, video output, MHL, or wired desktop modes:
        //      • Cross-reference the device model against the Hardware Reference Lists above.
        //      • If unlisted and specifications do not explicitly confirm video output capability: Default to "Tier 3: No Wired Video Output / Audio / Data / Charge Only".
      },
      "desktop_mode_software_environment": {
        "value": "Tier 1: Native Windowed Desktop OS Environment",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.50
        // SCORING GUIDELINE: Identify native operating system software support for windowed desktop workstation environments when connected to external displays. Use the following exact Tier Names for "value" with related scores as subscore:
        //   • "Tier 1: Native Windowed Desktop OS Environment"  → 0.50
        //     - Definition: Native operating system desktop interface featuring windowed multitasking, desktop browser rendering, taskbar navigation, and desktop mouse/keyboard interface when connected to an external display.
        //     - Qualifying Software Interfaces:
        //         * Samsung DeX (wired Samsung Desktop eXperience)
        //         * Motorola Ready For / Motorola Smart Connect (wired windowed desktop mode)
        //         * Huawei Desktop Mode / EMUI Desktop
        //         * Honor Desktop Mode / Magic Desktop
        //         * LG Screen+ (LG windowed desktop OS)
        //         * Xiaomi Workstation Mode (on supported tablet/foldable/flagship OS)
        //         * Android Native Developer Desktop Mode (when officially enabled in production OS)
        //     - Specification Keywords & Evidence: "Samsung DeX", "DeX", "Ready For", "Smart Connect", "Desktop Mode", "EMUI Desktop", "Magic Desktop", "LG Screen+", "Workstation Mode".
        //   • "Tier 2: No Native Desktop OS Mode"               → 0.00
        //     - Definition: Lacks native windowed desktop operating system mode. Output is restricted to basic screen mirroring, media player casting, or PC companion utilities.
        //     - Non-Qualifying Technologies for Tier 1 (Maps to Tier 2 with 0.00 pts): Standard screen mirroring, AirPlay, Chromecast, Miracast, PC companion file-transfer apps (e.g. Link to Windows, Phone Link, PC Connect, Easy Projection window on PC), remote desktop apps (TeamViewer, AnyDesk).
        //     - Specification Keywords & Evidence: "Screen Mirroring", "No Desktop Mode", "Mirroring only".
        //
        // AMBIGUITY RESOLUTION & QUALIFICATION LOGIC TREE FOR DESKTOP MODE (MANDATORY):
        // Automated agents MUST resolve desktop OS environment specifications using the following 2-step logic hierarchy:
        //
        // 1. Step 1: Strict Windowed OS Qualification Rule
        //    To qualify for "Tier 1: Native Windowed Desktop OS Environment" (0.50 pt), the smartphone MUST run a native windowed desktop interface directly driven by the phone's operating system when connected to an external monitor via wire.
        //    • Standard screen mirroring (which simply duplicates the portrait phone UI onto a TV or monitor) does NOT qualify.
        //    • PC companion apps that display a phone window inside a Windows/Mac PC screen (e.g. Microsoft Link to Windows, Link to PC, Lenovo PC Connect) do NOT qualify for Part 3, as they rely on the host PC's operating system rather than generating a native external desktop environment from the phone.
        //
        // 2. Step 2: Unstated Desktop Mode Default Rule
        //    If specifications or review notes do not explicitly confirm any of the above-mentioned qualifying native desktop software environments:
        //      • Default to "Tier 2: No Native Desktop OS Mode" (0.00 pts).
      },
      "scores": {
        "predicted": 9.00,
        "calculation_formula": "Clamp(usb_protocol_and_interface_speed.subscore + wired_display_output.subscore + desktop_mode_software_environment.subscore, 0.00, 10.00)",
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
      // METHOD A — Benchmark Validation (Primary Path)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_a_benchmark_Battery": {
        "gsmarena_active_use_score_v2": {
          "value": 13.80,
          "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2670p3.php",
          "exact_extract": "Active use score: 13:48h"
          // SCORING GUIDELINE: Sourced from Global System for Mobile Communications Arena (GSMArena) review (Battery page). Use the "Active use score" (format HH:MM). Convert format HH:MM to decimal hours (e.g., 13:48 = 13.80) for the value. If not available, set value to "Not found" and source/exact_extract to "N/A".
          // In November 2023, GSMArena updated its battery test from Version 1.0 (v1.0) to Version 2.0 (v2.0). The v2.0 Active Use Score (gsmarena_active_use_score_v2) measures continuous active runtime in hours (representing Screen-On Time under calls, web browsing, YouTube streaming, and gaming, completely excluding standby time). The legacy v1.0 Endurance Rating (gsmarena_endurance_rating_v1) measures total elapsed hours including 21 hours of daily standby. The v2.0 score is the primary metric and must be used whenever available.
        },
        "gsmarena_endurance_rating_v1": {
          "value": "Not found",
          "source": "N/A",
          "exact_extract": "N/A"
          // SCORING GUIDELINE: Sourced from Global System for Mobile Communications Arena (GSMArena) review (Battery page) legacy tests. Use the "Endurance Rating" in hours (e.g., 140). If not available, set value to "Not found" and source/exact_extract to "N/A".
          // Both fields for v1.0 and v2.0 must always be populated if their respective data can be found on GSMArena (even when v2.0 is available, extracting v1.0 is highly valuable to help validate and fine-tune the conversion ratio of 8.4).
        },
        "t_unified_hours": {
          "value": 13.80,
          "calculation_formula": "gsmarena_active_use_score_v2.value != 'Not found' ? gsmarena_active_use_score_v2.value : (gsmarena_endurance_rating_v1.value != 'Not found' ? gsmarena_endurance_rating_v1.value / 8.4 : 'Not found')",
          // SCORING GUIDELINE: Converts the legacy Endurance Rating (ER) to an Active Use Score (AUS) equivalent if v2 is missing by dividing by the conversion constant of 8.4.
        },
        "subscore": 3.98,
        "calculation_formula": "10 * (t_unified_hours.value - Battery_GSMArena_Hours_Min) / (Battery_GSMArena_Hours_Max - Battery_GSMArena_Hours_Min), clamped 0-10."
        // SCORING GUIDELINE: Normalized score (subscore) is calculated using linear bounds from scoring_constants.md (clamped to [0, 10]). Set subscore to "N/A" if t_unified_hours.value is "Not found".
      },
      
      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD C — Technical Prediction Model (Tertiary / baseline for Method B)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_c_prediction_model_Battery": {
        // SCORING GOAL: Predicts the active battery runtime in hours using a physical supply-and-demand model and converts it to a predicted score.
        
        // --- [1] SUPPLY MODELING (E_supply) ---
        "battery_capacity_mah": {
          "value": 5000,
          "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
          "exact_extract": "BATTERY [...] Li-Ion 5000 mAh, non-removable"
          // SCORING GUIDELINE: Battery capacity in mAh. This value must be mathematically compatible with battery_nominal_voltage_v so that their product represents the complete physical battery pack.
          //
          // EXTRACTION & PROVENANCE RULES:
          //   1. Total Combined Pack Capacity: If the published capacity represents the complete battery pack (e.g. '5000 mAh' or '5000 mAh total'), store the total pack capacity.
          //   2. Per-Cell Capacity: If the published capacity explicitly represents one cell of a series battery (e.g. '2 x 2500 mAh' or '2500 mAh per cell'), store the per-cell capacity.
          //   3. Illegal Pairing Prohibitions: Never combine total pack capacity with series-pack voltage (7.70V). Never combine per-cell capacity with single-cell voltage (3.85V) when cells are connected in series.
          //   4. Missing Data Handling: If no capacity specifications exist in any source, set value = "Not found", source = "N/A", exact_extract = "N/A". If Wh is directly published and mAh capacity is completely unstated, set value = "N/A", source = "N/A", exact_extract = "N/A".
        },
        "peak_charging_power_w": {
          "value": 45.0,
          "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
          "exact_extract": "45W wired charging"
          // SCORING GUIDELINE: Maximum peak rated continuous wired charging input power accepted by the smartphone hardware in Watts (W) (P_peak). Sourced according to the 4-Tier Evidence Hierarchy: (1) Measured input power [e.g. ChargerLAB/Notebookcheck], (2) Original Equipment Manufacturer (OEM) published accepted wattage, (3) Documented charging mode, (4) Inferred from charger [least reliable].
        },
        "battery_cell_architecture": {
          "value": "Single-Cell (1S)",
          "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
          "exact_extract": "45W wired charging",
          "classification_method": "Power-Inferred",
          "confidence_level": "Low"
          // SCORING GUIDELINE: Physical battery cell architecture used by the charging model to distinguish single-cell, parallel multi-cell, and series multi-cell charging systems (governs c0_base in Section 8.2).
          //
          // PERMITTED VALUES:
          //   • value: ["Single-Cell (1S)", "Dual-Cell Series (2S)", "Dual-Cell Parallel", "Multi-Cell Series (3S+)", "Unknown"]
          //   • classification_method: ["Direct", "Technical Secondary Source", "Power-Inferred", "Default"]
          //   • confidence_level: ["High", "Medium", "Low"]
          //
          // DETERMINISTIC CLASSIFICATION & PROVENANCE RULES:
          //   1. DIRECT EVIDENCE: If an official manufacturer document, official technical specification, regulatory filing, service documentation, or technically credible teardown explicitly identifies the cell architecture, use the documented architecture. classification_method = "Direct" or "Technical Secondary Source". confidence_level = "High". Populate source with the document URL and exact_extract with the verbatim architecture quote.
          //   2. EXPLICIT CELL-COUNT EVIDENCE: If a reliable source explicitly states '2 x X mAh', 'dual-cell', 'two cells in series', '2S', 'dual-cell parallel', '1S2P', 'split-cell battery', or equivalent, classify the documented architecture. confidence_level = "High" when configuration is unambiguous. Populate source with document URL and exact_extract with verbatim text.
          //   3. POWER-INFERRED DUAL-CELL: If no direct architecture evidence is available and P_peak >= 65 W, classify as "Dual-Cell Series (2S)". classification_method = "Power-Inferred". confidence_level = "Medium". Inherit source from peak_charging_power_w.source and exact_extract from peak_charging_power_w.exact_extract.
          //   4. POWER-INFERRED SINGLE-CELL: If no direct architecture evidence is available and P_peak < 65 W, classify as "Single-Cell (1S)" with classification_method = "Power-Inferred". Set confidence_level = "Medium" if P_peak < 45 W, or confidence_level = "Low" if 45 W <= P_peak < 65 W (lower confidence transition band). Inherit source from peak_charging_power_w.source and exact_extract from peak_charging_power_w.exact_extract.
          //   5. MISSING POWER DEFAULT: If architecture evidence is unavailable and P_peak is unknown, classify as "Single-Cell (1S)" using default baseline. classification_method = "Default". confidence_level = "Low". Set source = "N/A", exact_extract = "N/A".
          //   6. CONFLICTING EVIDENCE: If direct evidence contradicts power-based inference, always use direct evidence and ignore power-based inference.
          //   7. UNKNOWN: "Unknown" should be used ONLY when available evidence explicitly establishes that architecture cannot be determined AND applying default single-cell baseline would create a demonstrably misleading result. Otherwise use appropriate inferred/default classification so device remains scorable. Set source = "N/A", exact_extract = "N/A", confidence_level = "Low".
          //
          // POWER-INFERENCE RATIONALE: Charging power is an inference signal, not proof of architecture. The 65 W threshold is an operational classification threshold selected to maximize automated coverage of modern split-cell implementations while limiting false dual-cell classifications. It is not a physical law.
          // IMPORTANT: Never infer Dual-Cell Series solely because a manufacturer advertises a proprietary fast-charging protocol. When direct architecture evidence exists, it always overrides power-based inference.
        },
        "battery_nominal_voltage_v": {
          "value": 3.85,
          "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
          "exact_extract": "45W wired charging"
          // SCORING GUIDELINE: Nominal battery voltage multiplier in Volts (V) used to calculate stored battery energy. Established or confirmed referencing battery_cell_architecture.
          //
          // PRIORITY & PROVENANCE RULES:
          //   1. Explicit Pack Voltage: If an explicit nominal voltage for the battery pack is publicly documented, use that value. Populate source with the voltage URL and exact_extract with the verbatim voltage text.
          //   2. Per-Cell Voltage Scale (Dual-Cell Series 2S): If battery_cell_architecture is classified as Dual-Cell Series (2S), capacity is explicitly given per cell, and per-cell nominal voltage is documented, use 2 x the per-cell nominal voltage (e.g. 7.70 V). Populate source with battery_cell_architecture.source and exact_extract with battery_cell_architecture.exact_extract.
          //   3. Dual-Cell Total Capacity Baseline (Dual-Cell Series 2S): If battery_cell_architecture is classified as Dual-Cell Series (2S) but published capacity is total pack capacity (e.g. 5000 mAh total), use the standard 3.85 V system baseline. Populate source with battery_cell_architecture.source and exact_extract with battery_cell_architecture.exact_extract.
          //   4. Single-Cell Baseline (Single-Cell 1S or Dual-Cell Parallel): If battery_cell_architecture is classified as Single-Cell (1S) or Dual-Cell Parallel (1S2P), use documented nominal voltage when available; otherwise use standard 3.85 V baseline. Populate source with battery_cell_architecture.source and exact_extract with battery_cell_architecture.exact_extract.
          //   5. Multi-Cell Series Baseline (3S/4S Gaming/Foldable Architectures): If battery_cell_architecture is classified as Multi-Cell Series (3S or 4S), use N x per-cell nominal voltage (e.g. 3 x 3.85 V = 11.55 V) when capacity is per-cell, or standard 3.85 V baseline when capacity is total pack capacity. Populate source with battery_cell_architecture.source and exact_extract with battery_cell_architecture.exact_extract.
          //   6. Effective Voltage Provenance: When Effective Voltage Override is applied (derived from Published Wh), record Published Wh source URL in source and Published Wh verbatim text in exact_extract.
        },
        "energy_capacity_wh": {
          "value": 19.2500,
          "calculation_formula": "(battery_capacity_mah.value * battery_nominal_voltage_v.value) / 1000",
          "source": "N/A",
          "exact_extract": "N/A"
          // SCORING GUIDELINE: Stored nominal battery energy in Watt-hours (Wh). The value can either be calculated from calculation_formula, or directly obtained from source when an official published Wh rating is available.
          //
          // VALIDATION & PROVENANCE RULES:
          //   1. VALUE DETERMINATION PATHS:
          //      1a. Calculated Energy (Standard Path): Calculate energy from matched mAh/voltage pair using calculation_formula. Set source = "N/A", exact_extract = "N/A".
          //      1b. Direct Published Wh Sourcing (Authoritative Path): If energy capacity is directly extracted from published Wh rating, set value to published Wh, populate source with Wh URL, exact_extract with verbatim Wh text, and set calculation_formula = "Directly extracted from specification".
          //
          //   2. PUBLISHED Wh CONSISTENCY CHECK & 5% ERROR REMEDIATION:
          //      2a. Relative Difference Calculation: If a reliable published Wh value exists alongside mAh/voltage, calculate relative difference: |energy_capacity_wh.value - Published_Wh| / Published_Wh.
          //      2b. Acceptable Variance (Difference <= 5%): Retain the calculated value for field "value" and keep calculation_formula = "(battery_capacity_mah.value * battery_nominal_voltage_v.value) / 1000".
          //      2c. Unacceptable Variance (Difference > 5% Remediation Procedure): If difference > 5%, execute the following steps in sequence:
          //          - Step 1 (Capacity Representation Check): Re-check whether published mAh represents total pack capacity vs per-cell capacity.
          //          - Step 2 (Voltage Scale Check): Re-check whether nominal voltage represents single-cell voltage vs series-pack voltage.
          //          - Step 3 (Effective Voltage Override): If capacity representation and architecture are verified correct but published Wh still differs by > 5%, set energy_capacity_wh.value = Published_Wh, set calculation_formula = "Directly extracted from specification", and derive an effective nominal voltage stored in battery_nominal_voltage_v.value = (Published_Wh * 1000) / battery_capacity_mah.value. Also store Published Wh source URL in battery_nominal_voltage_v.source and Published Wh verbatim quote in battery_nominal_voltage_v.exact_extract.
          //      2d. Physical Architecture Integrity: Never modify battery_cell_architecture (e.g. changing 1S to 2S or vice versa) solely to force mathematical agreement with a published Wh rating. Physical cell layout is governed independently by battery_cell_architecture classification rules.
          //
          //   3. MISSING DATA HANDLING:
          //      If battery capacity (battery_capacity_mah.value) is missing ("Not found"), set value = "Not found", source = "N/A", exact_extract = "N/A", calculation_formula = "N/A".
        },

        // --- [2] DEMAND MODELING (P_demand) ---
        "display_power_demand_w": {
          "refresh_rate_min_hz": {
            "value": 1,
            "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2670p3.php",
            "exact_extract": "The Galaxy S24 Ultra's display refresh rate can vary in the 1Hz to 120Hz range"
            // SCORING GUIDELINE: Minimum display refresh rate in Hertz (Hz) for variable displays (Low-Temperature Polycrystalline Oxide (LTPO) panels). Set to "N/A" if the display does not support adaptive dynamic refresh rates.
          },
          "effective_frequency_hz": {
            "value": 42.6500,
            "calculation_formula": "refresh_rate_min_hz.value != 'N/A' ? (0.65 * refresh_rate_min_hz.value + 0.35 * 2_display.2_6_motion_smoothness.maximum_refresh_rate_hz.value) : 2_display.2_6_motion_smoothness.maximum_refresh_rate_hz.value",
            // SCORING GUIDELINE: Time-weighted dynamic display refresh rate. Under adaptive display, effective_frequency_hz models the 65% static (min refresh rate) and 35% peak (max refresh rate) motion duty cycle. Without adaptive display, the maximum refresh rate is used instead.
          },
          "f_refresh": {
            "value": 0.9566,
            "calculation_formula": "1 + 0.0025 * (effective_frequency_hz.value - 60)",
            // SCORING GUIDELINE: Refresh Rate Factor. Adjusts panel draw based on dynamic frequency.
          },
          "f_resolution": {
            "value": 1.0623,
            "calculation_formula": "1 + 0.025 * (6_processing_power_and_performance.6_10_thermal_dissipation_stability.method_c_prediction_model_TDSI.display_megapixels_mp.value - 2)"
            // SCORING GUIDELINE: Resolution Factor. Models pixel density driving current and GPU rendering overhead, centered around a standard 2.0 Megapixels (MP) baseline. References Megapixels from Section 6.10. Note: While f_resolution could be directly fetched from Section 6.10 (as it shares the same base formula), it is kept as a separate calculation here because Section 8.1 battery endurance modeling and Section 6.10 thermal dissipation modeling may require different correction factors or scaling behaviors in the future, allowing for independent model fine-tuning.
          },
          "p_display": {
            "value": 0.4037,
            "calculation_formula": "6_processing_power_and_performance.6_10_thermal_dissipation_stability.method_c_prediction_model_TDSI.display_surface_area_cm2.value * 6_processing_power_and_performance.6_10_thermal_dissipation_stability.method_c_prediction_model_TDSI.panel_efficiency.c_panel_w_cm2 * f_refresh.value * f_resolution.value"
            // SCORING GUIDELINE: Display active power demand in Watts (W). Directly references display surface area and panel efficiency constant from Section 6.10.
          }
        },

        "soc_power_demand_w": {
          "soc_mapping": {
            "identifier": "Snapdragon 8 Gen 3",
            "identifier_path": "identity.hardware_configuration.chipset.value",
            "reference_table": "references/soc_reference.md",
            "power_peak_soc_w": 14.0,
            "node_nm": 4.0
            // SCORING GUIDELINE: Retrieve the peak SoC power in Watts (W) and the process node size in nanometers (nm) from references/soc_reference.md by matching the chipset identifier.
          },
          "f_node_static": {
            "value": 1.0667,
            "calculation_formula": "0.80 + 0.20 * (soc_mapping.node_nm / 3.0)"
            // SCORING GUIDELINE: Process Node Static Factor. Models silicon-level static leakage scaling, anchored on a 3.0 nm fabrication baseline.
          },
          "f_node_active": {
            "value": 1.1167,
            "calculation_formula": "0.65 + 0.35 * (soc_mapping.node_nm / 3.0)"
            // SCORING GUIDELINE: Process Node Active Factor. Models silicon-level dynamic power scaling, anchored on a 3.0 nm fabrication baseline.
          },
          "cpu_background_score": {
            "identifier": "Cortex-A520",
            "identifier_path": "6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters.third_best.architecture",
            // GUIDELINE: Note that this path is not fixed and must be adjusted from device to device depending on the number of clusters, always pointing to the architecture of the weakest active CPU core cluster on the SoC (which is the last non-N/A cluster in the ordered 6_processing_power_and_performance.6_1_0_system_on_chip_reference.clusters).
            "reference_table": "CPU_CORE_ARCHITECTURE_LOOKUP_TABLE",
            "idle_efficiency_score": 10.00
            // SCORING GUIDELINE: Retrieve the idle_efficiency_score from the CPU_CORE_ARCHITECTURE_LOOKUP_TABLE by matching the core architecture name from cpu_background_score.identifier.
          },
          "f_static_cpu": {
            "value": 1.0000,
            "calculation_formula": "1 + 0.04 * (10 - cpu_background_score.idle_efficiency_score)"
            // SCORING GUIDELINE: CPU Static Architecture Factor. Scales static power based on CPU microarchitectural core efficiency.
          },
          "cpu_burst_score": {
            "value": 7.3748,
            "calculation_formula": "10 * (6_processing_power_and_performance.6_2_cpu_architecture_single_core.method_c_prediction_model_CPU_single.core_yield.value - CPU_STRS_Score_Min) / (CPU_STRS_Score_Max - CPU_STRS_Score_Min)"
            // SCORING GUIDELINE: CPU Burst Score. Sourced from Section 6.2 and normalized linearly to preserve physical power scaling.
          },
          "cpu_sustained_score": {
            "value": 5.8051,
            "calculation_formula": "10 * (6_processing_power_and_performance.6_1_cpu_multi_core_performance.method_c_prediction_model_CPU_multi.raw_performance_throughput_score.value - CPU_RCTS_Min) / (CPU_RCTS_Max - CPU_RCTS_Min)"
            // SCORING GUIDELINE: CPU Sustained Score. Sourced from Section 6.1 and normalized linearly to preserve physical power scaling.
          },
          "cpu_active_score": {
            "value": 6.3545,
            "calculation_formula": "0.35 * cpu_burst_score.value + 0.65 * cpu_sustained_score.value"
            // SCORING GUIDELINE: CPU Active Score. Weighted average of burst (35%) and sustained (65%) scores representing active performance.
          },
          "f_active_cpu": {
            "value": 1.1458,
            "calculation_formula": "1 + 0.04 * (10 - cpu_active_score.value)"
            // SCORING GUIDELINE: CPU Active Architecture Factor. Scales dynamic power based on CPU active efficiency.
          },
          "gpu_mapping": {
            "identifier": "Adreno 750",
            "identifier_path": "6_processing_power_and_performance.6_3_0_gpu_architecture_reference.gpu_model.value",
            "reference_table": "GPU_ARCHITECTURE_LOOKUP_TABLE",
            "efficiency": 9.0
            // SCORING GUIDELINE: Sourced from the "efficiency" column in the GPU_ARCHITECTURE_LOOKUP_TABLE by matching the GPU model from Section 6.3.0.
          },
          "f_gpu": {
            "value": 1.0100,
            "calculation_formula": "1 + 0.01 * (10 - gpu_mapping.efficiency)"
            // SCORING GUIDELINE: GPU Architecture Factor. Adjusts active dynamic power based on GPU microarchitectural efficiency.
          },
          "p_soc": {
            "value": 0.6981,
            "calculation_formula": "0.40 * f_static_cpu.value * f_node_static.value + 0.0150 * soc_mapping.power_peak_soc_w * f_active_cpu.value * f_gpu.value * f_node_active.value"
            // SCORING GUIDELINE: System on Chip (SoC) average power demand in Watts (W). 0.40W is static base board leakage. 0.0150 is the overall SoC utilization coefficient representing the time-weighted average active workload level under standard daily mixed usage.
          }
        },

        "connectivity_power_demand_w": {
          "cellular_modem": {
            "identifier": "Tier 1: 5G mmWave + Sub-6 (Global band coverage)",
            "identifier_path": "7_connectivity_and_sensors.7_1_cellular_capabilities.network_technology.value",
            "power_w": 0.1800
            // SCORING GUIDELINE: Retrieves cellular active power based on Section 7.1 cellular category:
            // 
            // | Cellular Tier / Category                         | power_w |
            // | :----------------------------------------------- | :-----: |
            // | Tier 1: 5G mmWave + Sub-6 (Global band coverage) |   0.18  |
            // | Tier 2: 5G Sub-6 (Full Global Bands)             |   0.14  |
            // | Tier 3: 5G Sub-6 (Limited/regional bands)        |   0.14  |
            // | Tier 4: 4G LTE-Advanced Pro                      |   0.09  |
            // | Tier 5: 4G LTE (Basic)                           |   0.09  |
            // | Tier 6: 3G                                       |   0.05  |
            // | Tier 7: 2G                                       |   0.05  |
          },
          "wifi": {
            "identifier": "Tier 1: Wi-Fi 7",
            "identifier_path": "7_connectivity_and_sensors.7_3_wifi_standard.standard.value",
            "power_w": 0.0500
            // SCORING GUIDELINE: Retrieves Wireless Fidelity (Wi-Fi) active power based on Section 7.3 Wi-Fi standard:
            // 
            // | Wi-Fi Tier / Standard | power_w |
            // | :-------------------- | :-----: |
            // | Tier 1: Wi-Fi 7       |   0.05  |
            // | Tier 2: Wi-Fi 6E      |   0.04  |
            // | Tier 3: Wi-Fi 6       |   0.04  |
            // | Tier 4: Wi-Fi 5       |   0.03  |
            // | Tier 5: Wi-Fi 4       |   0.03  |
            // | Tier 6: Wi-Fi ≤ 3     |   0.03  |
          },
          "p_connectivity": {
            "value": 0.0710,
            "calculation_formula": "0.20 * cellular_modem.power_w + 0.70 * wifi.power_w"
            // SCORING GUIDELINE: Average connectivity active power draw in Watts (W) under mixed workloads. Cellular modem has a 20% active voice call duty cycle. Wi-Fi has a 70% duty cycle. During the remaining 10%, the modems run at idle standby, which is absorbed into the static baseboard power.
          }
        },

        "modifiers": {
          "f_software_overhead": {
            "os_mapping": {
              "identifier": "Android 14",
              "identifier_path": "5_software_and_longevity.operating_system_version.value",
              "reference_table": "references/os_version_reference.md",
              "generation_score": 8.5
              // SCORING GUIDELINE: Sourced from references/os_version_reference.md by matching the operating system version.
            },
            "value": 1.0730,
            "calculation_formula": "1 + 0.01 * (10 - os_mapping.generation_score) + 0.01 * (10 - 5_software_and_longevity.5_2_system_cleanliness_control.scores.predicted)"
            // SCORING GUIDELINE: Software Inefficiency Modifier. Captures Operating System (OS) execution and background bloatware draw. OS generation score is mapped via os_mapping. Cleanliness uses the predicted score from Section 5.2.
          },
          "f_thermal_overhead": {
            "value": 1.0246,
            "calculation_formula": "1 + 0.03 * ((Thermal_Stability_Max / 100) ^ 3 - 6_processing_power_and_performance.6_10_thermal_dissipation_stability.method_c_prediction_model_TDSI.power_ratio.value) / ((Thermal_Stability_Max / 100) ^ 3 - (Thermal_Stability_Min / 100) ^ 3)"
            // SCORING GUIDELINE: Thermal Efficiency Modifier. Sourced from Section 6.10 power_ratio. Models silicon static leakage increase and elevated battery internal resistance at high operating temperatures.
          }
        },

        "p_demand": {
          "value": 1.2592,
          "calculation_formula": "(display_power_demand_w.p_display.value + (soc_power_demand_w.p_soc.value + connectivity_power_demand_w.p_connectivity.value) * modifiers.f_software_overhead.value) * modifiers.f_thermal_overhead.value"
          // SCORING GUIDELINE: Total physical active power consumption under daily mixed workload in Watts (W). Software overhead scales SoC and connectivity active cycles without scaling display hardware base draw.
        },

        // --- [3] RUNTIME PREDICTION (T_predicted) ---
        "t_predicted": {
          "value": 15.2875,
          "calculation_formula": "energy_capacity_wh.value / p_demand.value"
          // SCORING GUIDELINE: Predicted active mixed-use runtime in hours.
        },
        "predicted_score": {
          "value": 4.99,
          "calculation_formula": "10 * (t_predicted.value - Battery_Predictor_Hours_Min) / (Battery_Predictor_Hours_Max - Battery_Predictor_Hours_Min)"
          // SCORING GUIDELINE: Predicted score is normalized linearly using bounds from scoring_constants.md (clamped to [0, 10]).
        }
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // METHOD B — Nearest Neighbor Interpolation (Secondary Path)
      // ═══════════════════════════════════════════════════════════════════════════
      "method_b_neighbor_interpolation_Battery": {
        // SCORING GUIDELINE: Evaluated for all devices to validate prediction precision. The search space is restricted to all Reference Phones with verified GSMArena benchmarks (Method A), excluding the target device itself. Interpolation must use exactly 3 distinct neighbors.
        // Step 1: Compute weighted Euclidean distance (Distance) to all candidate neighbors in the 4-component physical space:
        //   Formula: Distance = Sqrt( (Diff_P_battery_equiv)^2 + (Diff_P_display_eff)^2 + (Diff_P_soc_eff)^2 + (Diff_P_connectivity_eff)^2 )
        //   Where the metric component differences are derived from the following paths:
        //   - Diff_P_battery_equiv (Equivalent Battery Power Difference) = (target.method_c_prediction_model_Battery.p_demand.value / target.method_c_prediction_model_Battery.energy_capacity_wh.value) * (target.method_c_prediction_model_Battery.energy_capacity_wh.value - neighbor.method_c_prediction_model_Battery.energy_capacity_wh.value)
        //   - Diff_P_display_eff (Effective Display Power Difference) = (target.method_c_prediction_model_Battery.display_power_demand_w.p_display.value * target.method_c_prediction_model_Battery.modifiers.f_thermal_overhead.value) - (neighbor.method_c_prediction_model_Battery.display_power_demand_w.p_display.value * neighbor.method_c_prediction_model_Battery.modifiers.f_thermal_overhead.value)
        //   - Diff_P_soc_eff (Effective SoC Power Difference) = (target.method_c_prediction_model_Battery.soc_power_demand_w.p_soc.value * target.method_c_prediction_model_Battery.modifiers.f_software_overhead.value * target.method_c_prediction_model_Battery.modifiers.f_thermal_overhead.value) - (neighbor.method_c_prediction_model_Battery.soc_power_demand_w.p_soc.value * neighbor.method_c_prediction_model_Battery.modifiers.f_software_overhead.value * neighbor.method_c_prediction_model_Battery.modifiers.f_thermal_overhead.value)
        //   - Diff_P_connectivity_eff (Effective Connectivity Power Difference) = (target.method_c_prediction_model_Battery.connectivity_power_demand_w.p_connectivity.value * target.method_c_prediction_model_Battery.modifiers.f_software_overhead.value * target.method_c_prediction_model_Battery.modifiers.f_thermal_overhead.value) - (neighbor.method_c_prediction_model_Battery.connectivity_power_demand_w.p_connectivity.value * neighbor.method_c_prediction_model_Battery.modifiers.f_software_overhead.value * neighbor.method_c_prediction_model_Battery.modifiers.f_thermal_overhead.value)
        //   - Target: The device currently being scored.
        //   - Neighbor: Any reference phone in the database with a verified GSMArena benchmark, excluding the target device itself.
        // Step 2: Select the 3 neighbors with the smallest distance.
        // Step 3: Compute average neighbor predicted score and average benchmark score.
        // Step 4: Calculate the correction ratio and apply it to the average neighbor benchmark.
        "neighbors": [
          {
            // Neighbor1
            "device_id_1": "xiaomi_14_ultra",
            // GUIDELINE: The identity.id of the neighbor device (e.g., "xiaomi_14_ultra").
            "euclidean_distance_1": 0.0500,
            // GUIDELINE: Euclidean distance from Step 1.
            "predicted_score_1": 5.27,
            // GUIDELINE: The neighbor's own Method C predicted score.
            "benchmark_score_1": 6.97
            // GUIDELINE: The neighbor's Method A subscore.
          },
          {
            // Neighbor2
            "device_id_2": "oneplus_12",
            "euclidean_distance_2": 0.0800,
            "predicted_score_2": 5.30,
            "benchmark_score_2": 7.20
          },
          {
            // Neighbor3
            "device_id_3": "asus_rog_phone_8_pro",
            "euclidean_distance_3": 0.1000,
            "predicted_score_3": 5.24,
            "benchmark_score_3": 7.05
          }
        ],
        "avg_predicted_neighbors": 5.2700,
        // SCORING GUIDELINE: (predicted_score_1 + predicted_score_2 + predicted_score_3) / 3.
        "avg_benchmark_neighbors": 7.0733,
        // SCORING GUIDELINE: (benchmark_score_1 + benchmark_score_2 + benchmark_score_3) / 3.
        "correction_ratio": 0.9469,
        // SCORING GUIDELINE: ratio between the target's predicted score and the average predicted score of the neighbors. Formula: method_c_prediction_model_Battery.predicted_score.value / avg_predicted_neighbors.
        "interpolated_score": 6.70
        // SCORING GUIDELINE: correction_ratio * avg_benchmark_neighbors.
      },

      "scores": {
        "predicted": 4.99,
        // SCORING GUIDELINE: scores.predicted directly inherits method_c_prediction_model_Battery.predicted_score.value.
        "final": {
          "value": 3.98,
          "calculation_formula": "method_a_benchmark_Battery.subscore != 'N/A' ? method_a_benchmark_Battery.subscore : (method_b_neighbor_interpolation_Battery.interpolated_score != 'N/A' ? method_b_neighbor_interpolation_Battery.interpolated_score : method_c_prediction_model_Battery.predicted_score.value)",
          // SCORING GUIDELINE: Use Method A if available (value = method_a_benchmark_Battery.subscore). Otherwise use Method B (value = method_b_neighbor_interpolation_Battery.interpolated_score). Otherwise default to Method C (value = method_c_prediction_model_Battery.predicted_score.value).
          "method_used": "Benchmark (GSMArena)",
          // SCORING GUIDELINE: Set based on the A→B→C hierarchy. Use the following terms exclusively:
          //   • Benchmark (GSMArena)   → Method A (documented GSMArena active use score or converted endurance rating)
          //   • Neighbor Interpolation → Method B (similar device benchmarks)
          //   • Predictor              → Method C (physical active power demand and runtime model)
          "booster": "No",
          // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
          "confidence": "N/A"
          // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
        }
      }
    },
    "8_2_wired_charging_system": {
      // SCORING GOAL: Evaluates the smartphone wired charging system using three distinct, non-overlapping hardware components: 1) Pure Wired Charging Speed (evaluated via Method A GSMArena empirical benchmark, Method B Nearest Neighbor Interpolation, or Method C Analytical Physics Predictor), 2) Universal Protocol Interoperability, and 3) Hardware Bypass Charging / Direct Drive capability.

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 1: PURE WIRED CHARGING SPEED
      // Evaluated via 3-Method Hierarchy: Method A (Primary) -> Method B (Secondary) -> Method C (Tertiary)
      // ═══════════════════════════════════════════════════════════════════════════

      // --- METHOD A: Empirical GSMArena Benchmark (Primary Path) ---
      "method_a_benchmark_Wired_Speed": {
        "gsmarena_charging_time": {
          "value": 65.0,
          "source": "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2670p3.php",
          "exact_extract": "Using the Samsung 45W adapter, our S24 Ultra got to 69% (nice) in 30 minutes and took 65 minutes to reach 100%."
          // SCORING GUIDELINE: Sourced strictly from Global System for Mobile Communications Arena (GSMArena) Wired Charging Speed Benchmark. Extracted value is full charge duration T_final in minutes (mins) (0% to 100% State of Charge - SoC). If missing, set value to "Not found" and source/exact_extract to "N/A".
        },
        "subscore": 3.99,
        "calculation_formula": "10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(gsmarena_charging_time.value)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins)), clamped 0.0 to 10.0"
        // SCORING GUIDELINE: Logarithmic Utility Normalization converting full charge duration in minutes into a normalized speed score (clamped 0.0 to 10.0). Uses shared constants from scoring_constants.md. Set subscore to "N/A" if gsmarena_charging_time.value is "Not found".
      },

      // --- METHOD C: Technical Predictor Model (Tertiary / Baseline for Method B) ---
      "method_c_prediction_model_Wired_Speed": {
        // SCORING GOAL: Predicts full charge duration in minutes (T_predicted) using an analytical power retention model and converts it to a predicted speed score.

        "battery_energy_wh": {
          "value": 19.2500,
          "value_path": "8_battery_and_charging.8_1_battery_endurance_score.method_c_prediction_model_Battery.energy_capacity_wh.value"
          // SCORING GUIDELINE: Total stored nominal battery energy capacity E_supply in Watt-hours (Wh).
        },
        "peak_charging_power_w": {
          "value": 45.0,
          "value_path": "8_battery_and_charging.8_1_battery_endurance_score.method_c_prediction_model_Battery.peak_charging_power_w.value"
          // SCORING GUIDELINE: Maximum peak rated continuous wired charging input power accepted by the smartphone hardware in Watts (W) (P_peak).
        },
        "c0_base": {
          "value": 0.4051,
          "calculation_formula": "(8_battery_and_charging.8_1_battery_endurance_score.method_c_prediction_model_Battery.battery_cell_architecture.value == 'Dual-Cell Series (2S)' || 'Multi-Cell Series (3S+)') ? 2.6813 : 0.4051"
          // SCORING GUIDELINE: Baseline thermal saturation onset threshold C0_base in reciprocal hours (h^-1). Sourced directly from Section 8.1 battery cell architecture:
          //   • If Section 8.1 battery_cell_architecture == "Dual-Cell Series (2S)" or "Multi-Cell Series (3S+)" → c0_base = 2.6813 h^-1 (series multi-cell baseline threshold).
          //   • Otherwise ("Single-Cell (1S)", "Dual-Cell Parallel", or "Unknown") → c0_base = 0.4051 h^-1.
          //
          // MODEL UPDATE ALERT PROCEDURE: The C0_base thermal onset threshold has been empirically calibrated for Single-Cell (1S) and Dual-Cell Series (2S) architectures. If battery_cell_architecture is classified as "Multi-Cell Series (3S+)" (e.g., 3+ cells in series), c0_base inherits the series dual-cell baseline value (2.6813 h^-1) but the engine MUST raise a high-priority alert: "MODEL UPDATE ALERT: Multi-Cell Series (3S+) architecture detected for device ({device_id}). Empirical C0_base thermal saturation onset model requires calibration update."
        },
        "c_rate": {
          "value": 2.3377,
          "calculation_formula": "peak_charging_power_w.value / battery_energy_wh.value"
          // SCORING GUIDELINE: Continuous charge rate normalized by battery energy capacity in reciprocal hours (h^-1). Keep 4 decimal places.
        },
        "power_retention_factor_f_system": {
          "value": 0.4339,
          "calculation_formula": "min(1, 0.9679 / (1 + 1.1265 * max(0, c_rate.value - c0_base.value) ^ 0.1344))"
          // SCORING GUIDELINE: Continuous full-cycle peak-to-average power retention factor F_system. Evaluates tapering dynamics using calibrated physical parameters. Keep 4 decimal places.
        },
        "effective_average_power_w": {
          "value": 19.5255,
          "calculation_formula": "peak_charging_power_w.value * power_retention_factor_f_system.value"
          // SCORING GUIDELINE: Average effective charging power P_effective delivered over the full 0% to 100% charge cycle in Watts (W). Keep 4 decimal places.
        },
        "t_predicted": {
          "value": 59.1534,
          "calculation_formula": "(battery_energy_wh.value / effective_average_power_w.value) * 60"
          // SCORING GUIDELINE: Predicted full 0% to 100% charge duration in minutes (mins). Keep 4 decimal places.
        },
        "predicted_score": {
          "value": 4.27,
          "calculation_formula": "10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(t_predicted.value)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins)), clamped 0.0 to 10.0"
          // SCORING GUIDELINE: Method C predicted charging speed score normalized logarithmically using shared constants from scoring_constants.md.
        }
      },

      // --- METHOD B: Nearest Neighbor Interpolation (Secondary Path) ---
      "method_b_neighbor_interpolation_Wired_Speed": {
        // SCORING GUIDELINE: Evaluated for all devices to validate precision. The search space includes all reference phones with verified GSMArena charging benchmarks (Method A), excluding the target device itself. Interpolation must use exactly 3 distinct neighbors.
        // Step 1: Compute Log-Standardized Euclidean Distance in the 3-component physical charging space (battery_energy_wh, peak_charging_power_w, t_predicted):
        //   Formula: Distance = Sqrt( (log(target.method_c_prediction_model_Wired_Speed.battery_energy_wh.value) - log(neighbor.method_c_prediction_model_Wired_Speed.battery_energy_wh.value))^2 + (log(target.method_c_prediction_model_Wired_Speed.peak_charging_power_w.value) - log(neighbor.method_c_prediction_model_Wired_Speed.peak_charging_power_w.value))^2 + (log(target.method_c_prediction_model_Wired_Speed.t_predicted.value) - log(neighbor.method_c_prediction_model_Wired_Speed.t_predicted.value))^2 )
        // Step 2: Select the 3 distinct neighbors with the smallest distance.
        // Step 3: Compute average neighbor predicted duration (avg_predicted_neighbors_mins) and average neighbor benchmark duration (avg_benchmark_neighbors_mins).
        // Step 4: Calculate correction_ratio and interpolated_duration_mins.
        // Step 5: Calculate interpolated_score.
        "neighbors": [
          {
            // Neighbor1
            "device_id_1": "google_pixel_9_pro_xl",
            // GUIDELINE: The identity.id of the neighbor device (e.g., "google_pixel_9_pro_xl").
            "euclidean_distance_1": 0.0421,
            // GUIDELINE: Log-Standardized Euclidean distance from Step 1.
            "predicted_duration_mins_1": 61.50,
            // GUIDELINE: The neighbor's own Method C predicted full charge duration in minutes (t_predicted.value).
            "benchmark_duration_mins_1": 67.00
            // GUIDELINE: The neighbor's Method A GSMArena verified full charge benchmark duration in minutes (gsmarena_charging_time.value).
          },
          {
            // Neighbor2
            "device_id_2": "samsung_galaxy_s23_ultra",
            "euclidean_distance_2": 0.0512,
            "predicted_duration_mins_2": 58.80,
            "benchmark_duration_mins_2": 59.00
          },
          {
            // Neighbor3
            "device_id_3": "nothing_phone_2",
            "euclidean_distance_3": 0.0684,
            "predicted_duration_mins_3": 57.20,
            "benchmark_duration_mins_3": 55.00
          }
        ],
        "avg_predicted_neighbors_mins": {
          "value": 59.1667,
          "calculation_formula": "(predicted_duration_mins_1 + predicted_duration_mins_2 + predicted_duration_mins_3) / 3"
          // SCORING GUIDELINE: Arithmetic average of the 3 selected nearest neighbors' predicted durations in minutes.
        },
        "avg_benchmark_neighbors_mins": {
          "value": 60.3333,
          "calculation_formula": "(benchmark_duration_mins_1 + benchmark_duration_mins_2 + benchmark_duration_mins_3) / 3"
          // SCORING GUIDELINE: Arithmetic average of the 3 selected nearest neighbors' Method A benchmark durations in minutes.
        },
        "correction_ratio": {
          "value": 0.9998,
          "calculation_formula": "target.method_c_prediction_model_Wired_Speed.t_predicted.value / avg_predicted_neighbors_mins.value"
          // SCORING GUIDELINE: Ratio between target predicted duration and average predicted duration of nearest neighbors.
        },
        "interpolated_duration_mins": {
          "value": 60.3212,
          "calculation_formula": "correction_ratio.value * avg_benchmark_neighbors_mins.value"
          // SCORING GUIDELINE: Interpolated full charge duration in minutes derived by applying correction ratio to average benchmark duration.
        },
        "interpolated_score": {
          "value": 4.21,
          "calculation_formula": "10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(interpolated_duration_mins.value)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins)), clamped 0.0 to 10.0"
          // SCORING GUIDELINE: Logarithmic utility normalization converting interpolated duration in minutes into a normalized speed score (clamped 0.0 to 10.0). Uses shared constants from scoring_constants.md.
        }
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 2: UNIVERSAL PROTOCOL INTEROPERABILITY
      // ═══════════════════════════════════════════════════════════════════════════
      "universal_protocol_interoperability": {
        "p_universal_usb_pd_w": {
          "value": 45.0,
          "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
          "exact_extract": "USB Power Delivery 3.0 PPS up to 45W"
          // SCORING GUIDELINE: Maximum open universal USB Power Delivery (USB-PD 3.0/3.1 Programmable Power Supply - PPS or fixed PD) power input in Watts (W) accepted by the device (p_universal_usb_pd_w.value).
          // SOURCING HIERARCHY (Tiers 1–6): (1) Official Datasheet, (2) USB Implementers Forum (USB-IF) Database, (3) ChargerLAB POWER-Z Protocol Analyzer Logs, (4) GSMArena Laboratory Reviews, (5) Notebookcheck Reviews, (6) AndroidAuthority Deep-Dives.
          //
          // DETERMINISTIC MULTI-TIER FALLBACK RULES & DECISION TREE (MANDATORY):
          // When explicit empirical/manufacturer data (Tiers 1–6) is omitted, resolve p_universal_usb_pd_w.value deterministically using the following hierarchy:
          //   1. Step 1: Explicit Measured / Documented Power (P_measured): If verified data exists in Tiers 1–6 → set p_universal_usb_pd_w.value = P_measured. Explicit empirical evidence MUST NEVER be overridden by fallbacks.
          //      - Provenance: Populate source with the document/benchmark URL from Tiers 1–6 and exact_extract with the verbatim wattage quote.
          //   2. Step 2: USB-PD Supported, but Maximum Wattage Unspecified:
          //      If official specs confirm USB Power Delivery (USB-PD / PPS) support but omit numerical wattage limit:
          //      p_universal_usb_pd_w.value = min(method_c_prediction_model_Wired_Speed.peak_charging_power_w.value, P_era)
          //      Where P_era is determined by launch year from identity.release_date.value:
          //        - 2016–2017: P_era = 10.0 W (Legacy 5V/2A early USB-PD 2.0)
          //        - 2018–2019: P_era = 15.0 W (Standard 5V/3A baseline USB-PD)
          //        - 2020–2021: P_era = 20.0 W (USB-PD 3.0 / early PPS)
          //        - 2022–2023: P_era = 25.0 W (Mainstream PD 3.0 PPS)
          //        - 2024–2026: P_era = 30.0 W (Mature PD 3.1 PPS ecosystem)
          //      - Provenance: Populate source with the spec URL confirming USB-PD/PPS support and exact_extract with the verbatim USB-PD quote (e.g., "Supports USB Power Delivery").
          //   3. Step 3: USB Type-C Present, but No Evidence of USB-PD Support:
          //      If device features Universal Serial Bus Type-C (USB Type-C) port but lacks documented USB-PD protocol support:
          //      p_universal_usb_pd_w.value = min(method_c_prediction_model_Wired_Speed.peak_charging_power_w.value, 15.0 W) (USB Type-C spec max without PD: 5V/3A via Configuration Channel - CC pin).
          //      - Provenance: Populate source with the spec URL confirming USB Type-C port presence and exact_extract with verbatim Type-C text (e.g., "USB Type-C 2.0").
          //   4. Step 4: Legacy Micro-USB / Proprietary Connector without Universal Fast Charging:
          //      If device uses Micro Universal Serial Bus (Micro-USB) port without universal fast-charging support:
          //      p_universal_usb_pd_w.value = min(method_c_prediction_model_Wired_Speed.peak_charging_power_w.value, 5.0 W) (Standard 5V/1A USB Battery Charging 1.2 - USB BC 1.2 trickle charging).
          //      - Provenance: Populate source with the spec URL confirming Micro-USB port presence and exact_extract with verbatim Micro-USB text (e.g., "microUSB 2.0").
          //   5. Step 5: No Open/Universal USB Charging Compatibility:
          //      If device completely lacks open USB charging compatibility: p_universal_usb_pd_w.value = 0.0 W.
          //      - Provenance: Set source = "N/A", exact_extract = "N/A".
        },
        "subscore": 8.30,
        "calculation_formula": "10 * (log(p_universal_usb_pd_w.value + 1) - log(Battery_Universal_Wired_W_Min + 1)) / (log(Battery_Universal_Wired_W_Max + 1) - log(Battery_Universal_Wired_W_Min + 1)), clamped 0.0 to 10.0"
        // SCORING GUIDELINE: Interoperability score.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 3: HARDWARE BYPASS CHARGING / DIRECT DRIVE (S_bypass)
      // ═══════════════════════════════════════════════════════════════════════════
      "hardware_bypass_charging": {
        "value": true,
        "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
        "exact_extract": "Pause USB Power Delivery",
        "subscore": 10.00
        // SCORING GUIDELINE: Evaluates physical/firmware battery bypass direct drive capability routing wall power directly to Power Management Integrated Circuit (PMIC) / logic board skipping battery:
        //   • true  → 10.00 (Native hardware/firmware bypass supported; routes wall power directly to PMIC/logic board, skipping battery to eliminate heat during plugged-in heavy use. Exhaustive OEM marketing terms & evidence keywords include: Samsung "Pause USB Power Delivery", ASUS ROG "Bypass Charging" / "Direct Power Supply", Sony Xperia "H.S. Power Control" [Heat Suppression], Xiaomi/Black Shark "Direct Power Supply" / "Bypass Charge", ZTE/RedMagic "Charge Bypass" / "Direct Power Mode", Infinix/TECNO "Bypass Charge", Lenovo Legion "Bypass Charging", Realme/Oppo/OnePlus "Bypass Charging" / "Direct Drive Power", Vivo/iQOO "Direct Power Supply").
        //   • false → 0.00 (Lacks bypass charging; always routes current through the battery cell).
        //
        // AMBIGUITY RESOLUTION & LOGIC TREE (MANDATORY):
        //   1. Step 1: Official / Empirical Documentation Proof (value: true): Set value: true (10.00 pts) ONLY if official datasheets, user manuals, OEM gaming settings, or verified review logs explicitly confirm battery bypass support.
        //      - Provenance: Populate source with the document/manual/review URL and exact_extract with verbatim feature quote (e.g., "Pause USB Power Delivery").
        //   2. Step 2: Default Rule (value: false): If no official documentation or review log verifies bypass charging → set value: false (0.00 pts).
        //      - Provenance: Set source = "N/A", exact_extract = "N/A".
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // SECTION 8.2 COMPOSITE SCORE CALCULATION
      // ═══════════════════════════════════════════════════════════════════════════
      "scores": {
        "predicted": 4.80,
        "calculation_formula": "0.88 * method_c_prediction_model_Wired_Speed.predicted_score.value + 0.09 * universal_protocol_interoperability.subscore + 0.03 * hardware_bypass_charging.subscore",
        // SCORING GUIDELINE: Predicted composite score combining Method C predicted pure wired charging speed (88%), universal protocol interoperability (9%), and hardware bypass charging (3%).
        "final": {
          "value": 4.56,
          "calculation_formula": "Clamp(0.88 * (method_a_benchmark_Wired_Speed.subscore != 'N/A' ? method_a_benchmark_Wired_Speed.subscore : (method_b_neighbor_interpolation_Wired_Speed.interpolated_score != 'N/A' ? method_b_neighbor_interpolation_Wired_Speed.interpolated_score : method_c_prediction_model_Wired_Speed.predicted_score.value)) + 0.09 * universal_protocol_interoperability.subscore + 0.03 * hardware_bypass_charging.subscore, 0.00, 10.00)",
          // SCORING GUIDELINE: Resolved strictly by the A->B->C hierarchy for pure wired charging speed (S_speed):
          //   1. Use Method A if method_a_benchmark_Wired_Speed is available (and method_used is "Benchmark (GSMArena)").
          //   2. Otherwise, use Method B if method_b_neighbor_interpolation_Wired_Speed is available (and method_used is "Neighbor Interpolation").
          //   3. Otherwise, fall back to Method C (and method_used is "Predictor").
          // The selected S_speed is then combined into the final composite score combining pure wired charging speed (88%), universal protocol interoperability (9%), and hardware bypass charging (3%).
          "method_used": "Benchmark (GSMArena)",
          // SCORING GUIDELINE: Set based on the A→B→C hierarchy used for S_speed. Use the following terms exclusively:
          //   • Benchmark (GSMArena)   → Method A (empirical GSMArena full charge duration benchmark)
          //   • Neighbor Interpolation → Method B (similar device benchmarks)
          //   • Predictor              → Method C (analytical physics predictor model)
          "booster": "No",
          // SCORING GUIDELINE: Must always be set to "No". No booster allowed for scoring sections using Benchmarks.
          "confidence": "N/A"
          // SCORING GUIDELINE: "N/A" for single benchmark source or Predictor.
        }
      }
    },
    "8_3_wireless_charging_system": {
      // SCORING GOAL: Comprehensive evaluation of the wireless charging system, prioritizing real-world convenience and compatibility. Scores are derived from a theoretical speed prediction, universal interoperability with public standards (Qi/Qi2), and the physical convenience and efficiency of magnetic alignment.
      
      "wireless_charging_supported": {
        "value": "Yes",
        "source": "TBD",
        "exact_extract": "Proof pending"
        // SCORING GUIDELINE: Evaluates whether the device supports any form of wireless charging.
        //   • "Yes" → Device supports wireless charging.
        //   • "No"  → Device lacks wireless charging (either explicitly confirmed absent or not found in documentation).
        //
        // AMBIGUITY RESOLUTION & LOGIC TREE (MANDATORY):
        //   1. CONFIRMED ABSENT: If an authoritative source (e.g., manufacturer specifications, official support documents, certification databases, or reputable technical reviews) explicitly confirms the device lacks wireless charging, set value to "No". Put "N/A" in all data blocks of the 3 components (`pure_wireless_charging_speed`, `universal_open_standard_interoperability`, `magnetic_alignment_capability`) for their values, sources, extracts, and subscores. Then follow the guidelines of SECTION 8.3 COMPOSITE SCORE CALCULATION for the rating.
        //   2. INSUFFICIENT DATA: If the agent simply cannot find any documentation confirming presence or absence (common for white-label ODMs), set value to "No" by default, but you MUST tag this by setting source to "Insufficient Data - Routed to manual review" and exact_extract to "N/A". Do NOT silently assume it is confirmed absent.
        //   3. NO MATERIAL INFERENCE: Do NOT infer the presence of wireless charging merely from a "glass back" or "flagship status".
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 1: PURE WIRELESS CHARGING SPEED (S_speed)
      // ═══════════════════════════════════════════════════════════════════════════
      "pure_wireless_charging_speed": {
        "battery_energy_wh": {
          "value": 19.2500,
          "value_path": "8_battery_and_charging.8_1_battery_endurance_score.method_c_prediction_model_Battery.energy_capacity_wh.value"
          // SCORING GUIDELINE: Total stored nominal battery energy capacity E_supply in Watt-hours (Wh). Inherited from Section 8.1.
        },
        "peak_wireless_charging_power_w": {
          "value": 15.0,
          "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/specs/",
          "exact_extract": "15W wireless charging"
          // SCORING GUIDELINE: Maximum absolute wireless charging power input in Watts (W) accepted by the smartphone hardware.
          //
          // AMBIGUITY RESOLUTION & LOGIC TREE (MANDATORY):
          //   1. EVIDENCE HIERARCHY: Always pull wireless parameters in the following order: Tier 1 (Manufacturer Specs) → Tier 2 (Official Support Docs/Limits) → Tier 3 (Certification) → Tier 4 (Technical Reviews) → Tier 5 (Historical Fallback).
          //   2. RECEIVE-SIDE ONLY: Spec sheets routinely list receive-side wireless charging and reverse/share wireless charging together. You MUST explicitly exclude reverse/share wattage from this field.
          //   3. SOFTWARE-UNLOCK TIMING: When a device's wireless wattage was raised via an official post-launch software update (e.g., iPhone 8 unlocking 7.5W via iOS 11.2), use the maximum post-update wattage, NOT the launch day figure. Flag the score with a note in exact_extract when they differ.
          //   4. HISTORICAL FALLBACK: If a pre-2020 phone lists "Qi wireless charging" but no wattage is documented, fallback to 5.0 W. This MUST be visibly logged as a Tier 5 deduction in source/exact_extract, clearly distinguishable from a phone that explicitly lists 5W on a Tier 1 spec sheet.
          //   5. ABSENT WIRELESS CHARGING: If wireless_charging_supported.value is "No", set value, source, exact_extract, and subscore across all data blocks in this component to "N/A".
        },
        "c_rate_wireless": {
          "value": 0.7792,
          "calculation_formula": "peak_wireless_charging_power_w.value / battery_energy_wh.value"
          // SCORING GUIDELINE: Continuous charge rate normalized by battery energy capacity in reciprocal hours (h^-1). Keep 4 decimal places.
        },
        "thermal_factor": {
          "value": 0.7901,
          "calculation_formula": "1 / (1 + 1.1232 * max(0, c_rate_wireless.value - 0.7778) ^ 0.2194)"
          // SCORING GUIDELINE: Dedicated wireless thermal throttling curve modeling heat from induction coils (F_thermal_wireless). Keep 4 decimal places.
        },
        "transfer_efficiency": {
          "value": "Tier 3: Advanced Passive",
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 0.78
          // SCORING GUIDELINE: Standardized transfer efficiency framework default assigned based on the verified wireless technology class.
          // PRECEDENCE RULE: If a device qualifies for multiple tiers, assign the highest applicable Tier.
          // Use the following exact strings for "value" and related coefficient for "subscore":
          //   • "Tier 1: Active Cooling"         → 0.83 (Condition: Requires a built-in active cooling fan in the official charging base/stand)
          //   • "Tier 2: Magnetic Alignment"     → 0.82 (Condition: Requires a native magnetic alignment ring built into the phone hardware. e.g., MagSafe, Qi2, proprietary magnetic)
          //   • "Tier 3: Advanced Passive"       → 0.78 (Condition: Any wireless charging protocol >5W that lacks a built-in fan and lacks magnetic alignment. e.g., Qi EPP 15W, Apple 7.5W, Samsung Fast Charge, proprietary >15W chargers)
          //   • "Tier 4: Basic Qi (5W BPP)"      → 0.72 (Condition: Limited to legacy 5W Qi Baseline Power Profile (BPP) only)
          //
          // AMBIGUITY RULES: 
          //   1. Do NOT infer "Magnetic Alignment" merely from a "magnetic case". The phone hardware itself must have the magnetic ring.
          //   2. FALLBACK: If the charging protocol or physical charger design is undocumented, assume the absence of premium hardware features (no fan, no magnets). Categorize the tier strictly based on the extracted peak wattage (e.g., Tier 3 if >5W, Tier 4 if exactly 5W).
        },
        "effective_average_power_w": {
          "value": 9.2442,
          "calculation_formula": "peak_wireless_charging_power_w.value * transfer_efficiency.subscore * thermal_factor.value"
          // SCORING GUIDELINE: Average effective wireless charging power delivered over the full 0% to 100% charge cycle in Watts (W). Keep 4 decimal places.
        },
        "t_predicted_wireless_mins": {
          "value": 124.9433,
          "calculation_formula": "60 * (battery_energy_wh.value / effective_average_power_w.value)"
          // SCORING GUIDELINE: Predicted wireless 0% to 100% charge duration in minutes (mins). Keep 4 decimal places.
        },
        "subscore": 4.26,
        "calculation_formula": "10 * (log(Battery_Wireless_Charge_Time_Max_Mins) - log(t_predicted_wireless_mins.value)) / (log(Battery_Wireless_Charge_Time_Max_Mins) - log(Battery_Wireless_Charge_Time_Min_Mins)), clamped 0.0 to 10.0"
        // SCORING GUIDELINE: Pure Wireless Charging Speed Score (S_speed). Logarithmic utility normalization converting duration in minutes into a normalized speed score. Uses constants from scoring_constants.md.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 2: UNIVERSAL OPEN STANDARD INTEROPERABILITY
      // ═══════════════════════════════════════════════════════════════════════════
      "universal_open_standard_interoperability": {
        "p_universal_wireless_w": {
          "value": 15.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
          // SCORING GUIDELINE: Highest explicitly documented manufacturer-supported wattage for Qi/Qi2-compatible wireless charging, subject to the proprietary/fallback rules below (P_universal_wireless).
          // This must be the charging input power the smartphone receives using a publicly interoperable WPC Qi-family standard (Qi or Qi2), without requiring a manufacturer-specific wireless charging transmitter, dock, authentication mechanism, or proprietary charging protocol.
          // Note: The field should accept ANY documented manufacturer-supported Qi power (e.g., 7.5W, 11W, 12W, 15W, 25W).
          // 
          // EVIDENCE HIERARCHY (Log the applied tier and evidence type in `source` and `exact_extract`):
          //   Tier 1: Manufacturer specification (Official tech specs, product page, user manual).
          //   Tier 2: WPC certification (Certified Product Database, Qi/Qi2 profile info).
          //   Tier 3: Reliable independent technical documentation (Reputable review/testing site, regulatory docs).
          //   Tier 4: Retail/carrier documentation (Only when higher tiers are unavailable).
          //   Tier 5: Methodological fallback (The predetermined 5W / 15W fallback rules below).
          // 
          // AMBIGUITY RESOLUTION & LOGIC TREE (MANDATORY):
          //   1. EXPLICIT QI/QI2 WATTAGE: Prefer manufacturer specifications. If an authoritative source explicitly states a Qi/Qi2 wattage (e.g., "Qi2 wireless charging up to 25 W"), use that exact value.
          //   2. SOFTWARE-UNLOCK TIMING: When a device's open wireless wattage was raised via an official post-launch software update (e.g., iPhone 8 unlocking 7.5W Qi via iOS 11.2, or iPhone 13/14 unlocking 15W Qi2 via iOS 17.2), use the maximum post-update wattage, NOT the launch day figure. Flag the score with a note in exact_extract when they differ.
          //   3. QI2 CERTIFICATION: Qi2 / MPP implies 15.0 W, unless the device is specifically certified for the newer 25 W profile (Qi2 25W / Qi v2.2.1 / MPP25), which implies 25.0 W. WPC states the original Qi2 delivered 15 W, while Qi2 25W launched in July 2025.
          //   4. NO INFERENCE FROM MAGSAFE/PROPRIETARY: Never infer open Qi wattage from proprietary MagSafe or other proprietary wireless charging wattages. Apple explicitly distinguishes MagSafe and Qi (e.g., iPhone 12 supports 15W MagSafe but only 7.5W Qi). MagSafe ≠ Qi2 for scoring purposes unless explicitly documented as supporting Qi2 at that power.
          //   5. DETERMINISTIC FALLBACKS: If a device supports wireless charging but lacks an explicitly documented standard Qi/Qi2 wattage, use the following deterministic inferences (must be labeled as Tier 5 estimates in `exact_extract`):
          //      - Explicit Qi2 25W         → 25.0 W
          //      - Explicit Qi2, no wattage → 15.0 W
          //      - Explicit Qi, no wattage  → 5.0 W
          //      - Proprietary wireless >15 W + no disclosed Qi fallback, released ≥2020 → 15.0 W (Note: 15 W is the relevant upper bound for the original Qi EPP class; newer Qi2/Qi v2.2 profiles can support higher power).
          //      - Proprietary wireless >15 W + no disclosed Qi fallback, released <2020 → 5.0 W
          //      - Qi mentioned but no wattage and no proprietary fast wireless protocol → 5.0 W
          //      - No wireless charging → "N/A" (value, source, exact_extract, and subscore are set to "N/A")
        },
        "subscore": 8.51,
        "calculation_formula": "10 * (log(p_universal_wireless_w.value + 1) - log(Battery_Universal_Wireless_W_Min + 1)) / (log(Battery_Universal_Wireless_W_Max + 1) - log(Battery_Universal_Wireless_W_Min + 1)), clamped 0.0 to 10.0"
        // SCORING GUIDELINE: Universal Open Standard Interoperability Score.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 3: MAGNETIC ALIGNMENT CAPABILITY (S_alignment)
      // ═══════════════════════════════════════════════════════════════════════════
      "magnetic_alignment_capability": {
        "value": "Tier 4: No official magnetic alignment",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 0.00
        // SCORING GUIDELINE: Measures the device's official magnetic alignment capability (how reliably the charging system maintains optimal coil alignment). Use the following exact strings for "value" and related score for "subscore":
        //   • "Tier 1: Native Qi2 (MPP) / MagSafe"           → 10.00 (Requires native Magnetic Power Profile (MPP) hardware built into the phone. Includes Apple MagSafe on iPhone 12-17 and Qi2 MPP certified Androids).
        //   • "Tier 2: Native Proprietary Magnetic"          → 8.00 (Requires built-in magnets intended for charging alignment, but relies on a proprietary ecosystem rather than Qi2 MPP. e.g., Realme MagDart).
        //   • "Tier 3: OEM Magnetic Case Required"           → 5.00 (The phone lacks built-in charging magnets but officially supports a first-party/OEM-certified magnetic case to achieve alignment. Generic third-party aftermarket rings/cases do NOT qualify).
        //   • "Tier 4: No official magnetic alignment"       → 0.00 (Standard induction coil only. Device supports wireless charging but lacks any qualifying native or OEM magnetic alignment).
        //   • ABSENT WIRELESS CHARGING: If wireless_charging_supported.value is "No", set value, source, exact_extract, and subscore to "N/A" instead of Tier 4.
        //   • INSUFFICIENT EVIDENCE: If wireless charging is supported but sources are inaccessible or contradictory regarding magnets, set value to "N/A — Insufficient evidence" during research rather than prematurely assigning 0.00.
        // 
        // EVIDENCE HIERARCHY (Log the applied tier and evidence type in `source` and `exact_extract`):
        //   Tier A: Manufacturer technical documentation (Tech specs, manuals, official accessory docs).
        //   Tier B: WPC certification (Crucial for verifying Qi2 MPP).
        //   Tier C: Reliable physical/technical testing (Teardowns).
        //   Tier D: Retail listings / secondary sources (Do NOT treat a retailer's "MagSafe compatible" label as evidence of native hardware).
        // 
        // CRITICAL AMBIGUITY RULES:
        //   1. "Magnetic accessory compatible" ≠ native magnetic: Do not award Tier 1 or 2 just because a manufacturer sells a magnetic mount or wallet. Evidence must show the phone or qualifying OEM case creates the charging alignment mechanism.
        //   2. Case behavior ≠ Native behavior: A phone without magnets + an official magnetic case is Tier 3, not Tier 1. Do not infer native hardware from the assembled phone+case behavior.
        //   3. Proprietary ≠ Qi2: A proprietary magnetic system remains Tier 2 unless independently documented as Qi2 MPP.
        //   4. Magnet presence alone is insufficient: Teardowns finding speaker or camera magnets do not qualify. Magnets must be explicitly for wireless-charging alignment.
        //   5. "Qi2 Ready": A phone marketed as "Qi2 Ready" that achieves this via an approved accessory case is Tier 3. Do not automatically convert "Qi2 Ready" to Tier 1 without native MPP hardware.
        //   6. Magnetic Strength Irrelevant: Do not score based on holding force or magnet count; this metric evaluates categorical capability.
        //   7. Tier 4 Assignment Protocol: Tier 4 may ONLY be assigned after verifying the manufacturer's specs, manuals, official accessories, and WPC certification, with no qualifying native or OEM magnetic mechanism found. Absence of immediate documentation is not automatic proof of absence.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // SECTION 8.3 COMPOSITE SCORE CALCULATION
      // ═══════════════════════════════════════════════════════════════════════════
      "scores": {
        "predicted": 5.11,
        "calculation_formula": "(wireless_charging_supported.value == 'Yes') ? Clamp(0.40 * pure_wireless_charging_speed.subscore + 0.40 * universal_open_standard_interoperability.subscore + 0.20 * magnetic_alignment_capability.subscore, 0.00, 10.00) : 0.00",
        // SCORING GUIDELINE: Composite score combining pure wireless charging speed (40%), universal open standard interoperability (40%), and magnetic alignment capability (20%). If wireless_charging_supported.value is 'No', the score is mathematically zeroed (0.00).
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 5.11,
          "method_used": "Predictor",
          "booster": "No",
          "confidence": "N/A"
        }
      }
    },
    "8_4_wired_reverse_charging": {
      // SCORING GOAL: Evaluates the device's capability to act as a wired power bank (source) for external devices. The score combines pure power output and standard protocol interoperability.
      
      "reverse_wired_charging_supported": {
        "value": "Yes",
        "source": "TBD",
        "exact_extract": "Proof pending"
        // SCORING GUIDELINE: Evaluates whether the device supports wired reverse charging (acting as a power source to externally connected devices via its physical port).
        //   • "Yes" → Device supports wired reverse charging (e.g., Universal Serial Bus On-The-Go — USB OTG power output, Power Share, Reverse Charging).
        //   • "No"  → Device explicitly lacks or is blocked from sourcing power.
        //
        // AMBIGUITY RESOLUTION & LOGIC TREE (MANDATORY):
        //   1. CONFIRMED ABSENT: If an authoritative source (e.g., spec sheet, review) explicitly confirms the device cannot source power to external devices, set value to "No". Put "N/A" for values, sources, and exact_extracts in `p_reverse_wired` and `s_protocol` data blocks, and set their subscores to 0.00.
        //   2. INSUFFICIENT DATA / OMISSION: Most primary databases (like GSMArena) often omit reverse wired charging if it's a baseline feature (like standard 5V Universal Serial Bus On-The-Go — USB OTG, a protocol standard enabling the phone to act as a host and supply power to connected USB devices). You MUST proactively scan at least three distinct sources (e.g., GSMArena, Official Specs, Wikipedia, Notebookcheck, external reviews) to cross-reference (Omni-Scan Rule). If no source mentions it, but the device has a physical port (such as USB Type-C, Micro-USB, or Lightning) supporting USB OTG, set value to "Yes" (baseline 5V power sourcing). Do NOT blindly assume "No" without proof.
        //   3. SOURCE VS SINK SEPARATION: Inbound charging capability (e.g., accepting 45W from a wall charger) MUST NEVER be used to infer outbound reverse charging capability.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 1: PURE POWER OUTPUT
      // ═══════════════════════════════════════════════════════════════════════════
      "p_reverse_wired": {
        "value": 7.5,
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 6.23,
        // SCORING GUIDELINE: The highest explicitly documented or lab-tested continuous source power output available from the physical port in Watts (W).
        //
        // AMBIGUITY RESOLUTION & FALLBACK HIERARCHY (MANDATORY):
        // Always extract the exact peak outbound wattage (e.g., 10W, 15W, 27W) from Tier 1 (Manufacturer Specs) or Tier 2/3 (Reviews/Datasheets). CRUCIAL WARNING: Ensure you do NOT accidentally extract the device's inbound wall-charging speed (e.g., 45W or 65W Fast Charging) as the reverse wired wattage. The wattage MUST explicitly apply to OUTBOUND / reverse charging.
        // Independent Lab Tests: To use a lab measurement as Tier 2/3 evidence, the test must demonstrate stable, continuous power delivery to a sink device (e.g., measuring 5.1V x 1.47A), not just a momentary transient spike or a basic confirmation of OTG host mode.
        // If the exact wattage is unlisted, resolve `value` deterministically based on protocol support and connector type:
        //   1. Explicit Wattage Documented: If verified data exists (e.g., "15W reverse charging") → set value = Documented Wattage.
        //   2. Explicit Source Profile Documented: If the source outputs are listed as voltage/current profiles (e.g., 9V/2A), calculate P = V × A and use the highest supported continuous source wattage.
        //   3. USB Power Delivery (PD) Source Supported (No Wattage): If device explicitly supports USB Power Delivery (PD) Source mode but omits max wattage → set value = 15.0 (Standard USB-PD baseline output for phones).
        //   4. Standard USB Type-C OTG (No PD): If device has a USB Type-C port and supports reverse charging/OTG but lacks USB Power Delivery (PD) source confirmation → set value = 4.5 (Standard 5V/0.9A USB 3.0 output) for devices released before 2020, or 7.5 (5V/1.5A Type-C Current Advertisement (Rp)) for devices released in 2020 or later. Default fallback for unknown release dates is 4.5.
        //   5. Legacy Micro-USB OTG: If device uses Micro-USB and supports OTG power → set value = 2.5 (Standard 5V/500mA legacy USB 2.0 output).
        //   6. Not Supported: If reverse_wired_charging_supported.value is "No" → set value = "N/A", source = "N/A", exact_extract = "N/A", and subscore = 0.00.
        "calculation_formula": "10 * (log(p_reverse_wired.value + 1) - log(Battery_Reverse_Wired_W_Min + 1)) / (log(Battery_Reverse_Wired_W_Max + 1) - log(Battery_Reverse_Wired_W_Min + 1)), clamped 0.0 to 10.0"
        // SCORING GUIDELINE: Normalizes the output logarithmically using constants from scoring_constants.md.
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // COMPONENT 2: STANDARD PROTOCOL INTEROPERABILITY
      // ═══════════════════════════════════════════════════════════════════════════
      "s_protocol": {
        "value": "Tier 2: USB Type-C Current Advertisement Source",
        "source": "TBD",
        "exact_extract": "Proof pending",
        "subscore": 7.50
        // SCORING GUIDELINE: Evaluates the verified source-side negotiation standards of the reverse charging connection.
        // Use the following exact Tier Names for "value" with related scores as subscore:
        //   • "Tier 1: USB Power Delivery (PD) Source"                   → 10.00
        //     Definition & Evidence: The host device contains Dual-Role Power (DRP) controllers capable of broadcasting active USB-PD Power Data Objects (PDOs) over the Configuration Channel (CC) line. Assign this tier ONLY if source-side USB-PD is explicitly documented or verified (e.g., "USB-PD Reverse Charging" or "Output: 5V/3A, 9V/2A PD"). CRUCIAL WARNING: General mentions of "USB-PD" usually refer to inbound wall charging (Sink). To qualify for Tier 1, the device MUST explicitly support USB-PD as an OUTBOUND or SOURCE capability.
        //   • "Tier 2: USB Type-C Current Advertisement (Rp) Source"     → 7.50
        //     Definition & Evidence: Utilizes standardized Type-C Configuration Channel (CC) pin pull-up resistors (Rp) to advertise source current levels (e.g., 5V/1.5A or 5V/3.0A) without full USB-PD protocol messaging. Assign this tier if source-side CC/Rp current advertisement is explicitly documented or verified, unless Tier 1 is established. To qualify, the device MUST explicitly support this as an OUTBOUND or SOURCE capability.
        //   • "Tier 3: Legacy USB On-The-Go (OTG) Source"                → 3.00
        //     Definition & Evidence: Legacy host power output via 5V VBUS rails (e.g., 500mA or 900mA standard). This acts as the baseline fallback: Assign this tier if wired reverse output is confirmed to be working, but neither PD source nor CC/Rp source advertisement is established in public evidence. To qualify, the device MUST explicitly support On-The-Go (OTG) as an OUTBOUND or SOURCE capability.
        //   • "Tier 4: No Wired Reverse Source"                          → 0.00
        //     Definition & Evidence: Physically or firmware-blocked from sourcing power.
        //
        // PROHIBITED INFERENCES (MANDATORY):
        //   - WATTAGE IS NOT PROTOCOL: Never infer protocol tiers purely from P_reverse_wired output capability (e.g., >15W ≠ PD, 15W/7.5W ≠ Type-C CC, ≤5W ≠ OTG). The documentation must explicitly establish the negotiation mechanism.
        //   - CONNECTOR TYPE IS NOT PROTOCOL: A USB-C connector does not prove Tier 1 or Tier 2. A Micro-USB connector does not automatically prove Tier 3 (the device must explicitly support OTG).
      },

      // ═══════════════════════════════════════════════════════════════════════════
      // SECTION 8.4 COMPOSITE SCORE CALCULATION
      // ═══════════════════════════════════════════════════════════════════════════
      "scores": {
        "predicted": 6.48,
        "calculation_formula": "0.80 * p_reverse_wired.subscore + 0.20 * s_protocol.subscore",
        // SCORING GUIDELINE: The final score balances raw power output (80%) with protocol safety and universal interoperability (20%).
        "final": {
          // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
          "value": 6.48,
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
        // SCORING GUIDELINE: Apply Section 8.6 Ratio formula. subscore = 10 * (Included_Watts / Max_Wired_Watts). Max_Wired_Watts retrieved from 8_battery_and_charging.8_2_wired_charging_system.method_c_prediction_model_Wired_Speed.peak_charging_power_w.value.
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
