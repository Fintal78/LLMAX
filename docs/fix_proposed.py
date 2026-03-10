import codecs

file_path = "c:\\Users\\Ion\\.gemini\\antigravity\\scratch\\smartphone_db\\docs\\proposed_data_structure.md"
with codecs.open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content_str = """        "ray_tracing_score": {
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
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Look up the value in Section 6.10 Part B table. Active Cooling (Fan) -> 10.0, Large VC -> 8.0, Vapor Chamber -> 7.0, Multi-layer Graphite -> 5.0, Single Heat Spreader -> 3.0, None -> 0.0.
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
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 4.00
          // SCORING GUIDELINE: Look up highest codec tier in Section 7.4 Part 2 table. Lossless -> 5.0, High-Res -> 4.0, Standard -> 1.5.
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
          "source": "TBD",
          "exact_extract": "Proof pending",
          "subscore": 8.00
          // SCORING GUIDELINE: Look up best available biometric method in Section 7.5 table.
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
      },\n"""

# We replace lines 1602 to 1665 (inclusive) in the 0-indexed terms.
# So index 1601 to 1665 (which is slice [1601:1666]).
lines[1601:1665] = [l + '\n' for l in new_content_str.split('\n')[:-1]]
# the split leaves an empty string at the end, so [:-1] handles the trailing \n

with codecs.open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
