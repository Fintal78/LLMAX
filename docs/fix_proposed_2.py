import codecs

file_path = "c:\\Users\\Ion\\.gemini\\antigravity\\scratch\\smartphone_db\\docs\\proposed_data_structure.md"
with codecs.open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content_str = """      "8_2_wired_charging_speed": {
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
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 10.00
          // SCORING GUIDELINE: Section 10.1 table: Integrated Active -> 10.0, Active (No Silo) -> 7.0, Passive/Basic -> 3.0, None -> 0.0.
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
"""

# Replace lines 2048 to 2143 (which is slice [2048:2144])
lines[2048:2144] = [l + '\n' for l in new_content_str.split('\n')[:-1]]

with codecs.open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
