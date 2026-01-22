# Ultimate Smartphone Data Structure Proposal (v5.1)

This schema is strictly aligned with the `scoring_rules.md` v8.0.
It includes all previously removed parameters, categorized as:
1.  **Numbered Keys:** Directly scorable criteria (e.g., `1_1_materials`).
2.  **Unnumbered Keys:** Contextual metadata (e.g., `colors`, `dimensions`).
3.  **"To be scored":** Parameters that need new scoring rules (e.g., `npu_tops`).

```json
{
  "meta": {
    "schema_version": "5.1",
    "updated_at": "2025-12-14T21:00:00Z",
    "data_source": "Multi-source aggregation",
    "completeness_score": 1.0
  },
  "identity": {
    "id": "samsung_galaxy_s24_ultra",
    "brand": "Samsung",
    "model_name": "Galaxy S24 Ultra",
    "series": "Galaxy S",
    "model_aliases": ["SM-S928B", "SM-S928U"],
    "codename": "Eureka",
    "release_date": "2024-01-24",
    "announce_date": "2024-01-17",
    "status": "Available",
    "market_regions": ["Global"]
  },
  "1_design_and_build_quality": {
    "form_factor": "Bar",
    "1_1_materials": {
      "frame": "Titanium",
      "back": "Glass",
      "description": "Titanium Frame + Gorilla Glass Armor Back",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "1_2_durability": {
      "ip_rating": "IP68",
      "details": "1.5m for 30 mins",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "1_3_glass_protection": {
      "value": "Gorilla Glass Armor",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "1_4_dimensions": {
      "thickness_mm": 8.6,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "height_mm": 162.3,
    "width_mm": 79.0,
    "1_5_weight": {
      "weight_g": 232,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "1_6_ergonomics": {
      "value": "Boxy / Sharp Corners",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "1_7_aesthetics": {
      "value": "Matte Glass + Minimal Wobble",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "colors": [
      {
        "name": "Titanium Black",
        "hex": "#1C1C1C"
      },
      {
        "name": "Titanium Blue",
        "hex": "#4B5D7E"
      }
    ]
  },
  "2_display": {
    "aspect_ratio": "19.5:9",
    "panel_type": "OLED",
    "2_1_technology": {
      "value": "LTPO OLED",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_2_resolution_density": {
      "ppi": 505,
      "class": "QHD+",
      "width_px": 1440,
      "height_px": 3120,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_3_brightness": {
      "peak_nits": 2600,
      "hbm_nits": 1750,
      "typical_nits": 1200,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_4_eye_comfort": {
      "pwm_dimming_hz": 492,
      "certification": "Eye Care Certified",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_5_touch_responsiveness": {
      "sampling_rate_hz": 240,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_6_refresh_rate": {
      "max_hz": 120,
      "min_hz": 1,
      "adaptive": true,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_7_color_accuracy_hdr": {
      "features": ["HDR10+", "100% DCI-P3"],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_8_screen_size": {
      "diagonal_inches": 6.8,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "2_9_screen_to_body_ratio": {
      "percent": 88.5,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    }
  },
  "3_processing_power_and_performance": {
    "3_1_soc_performance": {
      "geekbench_6_multi_score": 7200,
      "chipset_model": "Snapdragon 8 Gen 3",
      "manufacturer": "Qualcomm",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_2_cpu_structure": {
      "prime_core_ghz": 3.39,
      "config": "1x3.39GHz X4 + 3x3.1GHz A720 + 2x2.9GHz A720 + 2x2.2GHz A520",
      "clusters": [
        {
          "type": "Prime",
          "cores": 1,
          "name": "Cortex-X4",
          "ghz": 3.39
        },
        {
          "type": "Performance",
          "cores": 3,
          "name": "Cortex-A720",
          "ghz": 3.1
        },
        {
          "type": "Performance",
          "cores": 2,
          "name": "Cortex-A720",
          "ghz": 2.9
        },
        {
          "type": "Efficiency",
          "cores": 2,
          "name": "Cortex-A520",
          "ghz": 2.2
        }
      ],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_3_gpu_performance": {
      "model": "Adreno 750",
      "features": "HW Ray Tracing",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_4_efficiency_node": {
      "process_nm": 4,
      "foundry": "TSMC",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_5_thermal_management": {
      "value": "Vapor Chamber",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "thermal_system_size_mm2": 9000,
    "3_6_ram_technology": {
      "value": "LPDDR5X",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_7_ram_capacity": {
      "max_gb": 12,
      "variants_gb": [12],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_8_storage_technology": {
      "value": "UFS 4.0",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_9_storage_capacity": {
      "max_gb": 1024,
      "variants_gb": [256, 512, 1024],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "3_10_storage_expandability": {
      "value": "No Expansion Slot",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    }
  },
  "4_camera_systems": {
    "camera_hardware_specs": {
      "rear": [
        {
          "role": "Main",
          "sensor": "ISOCELL HP2",
          "mp": 200,
          "aperture": "f/1.7",
          "ois": true
        },
        {
          "role": "Tele 5x",
          "sensor": "IMX854",
          "mp": 50,
          "aperture": "f/3.4",
          "ois": true
        },
        {
          "role": "Tele 3x",
          "sensor": "IMX754",
          "mp": 10,
          "aperture": "f/2.4",
          "ois": true
        },
        {
          "role": "Ultrawide",
          "sensor": "IMX564",
          "mp": 12,
          "aperture": "f/2.2",
          "fov": 120
        }
      ]
    },
    "4_1_main_sensor_size": {
      "value": "1/1.3 inches",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_2_main_camera_aperture": {
      "value": "f/1.7",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_3_main_camera_resolution": {
      "mp": 200,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_4_image_stabilization": {
      "value": "Standard OIS",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_5_zoom_capability": {
      "optical_zoom_x": 5,
      "type": "Dual Periscope (3x + 5x)",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_6_ultrawide_capability": {
      "presence": true,
      "fov_degrees": 120,
      "sensor_size": "1/2.0",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_7_macro_capability": {
      "ultrawide_af": true,
      "min_focus_distance_cm": 2.5,
      "dedicated_macro_mp": 0,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_8_front_camera": {
      "value": "High Res + AF + 4K60",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_8_rear_video_resolution": {
      "max_resolution": "8K",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_9_rear_video_fps": {
      "max_fps_1080p_plus": 120,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_10_video_hdr": {
      "capability": "Dolby Vision",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_11_video_encoding": {
      "codecs": ["ProRes", "Log"],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_12_slow_motion": {
      "max_fps": 120,
      "resolution_mp": 8.3,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_13_front_camera_resolution": {
      "mp": 12,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_14_front_camera_focus": {
      "type": "Autofocus",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_15_front_camera_video": {
      "max_resolution": "4K",
      "max_fps": 60,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_16_multiframe_photo": {
      "features": ["Advanced HDR", "Night Mode"],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_17_semantic_ai": {
      "features": ["Semantic Segmentation"],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "4_18_generative_ai": {
      "features": ["Magic Editor"],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    }
  },
  "5_battery_and_charging": {
    "5_1_battery_capacity": {
      "mah": 5000,
      "battery_voltage_v": "Not available",
      "scoring_components": {
        "layer_a_energy": {
          "wh": 19.25,
          "score": 6.62
        },
        "layer_b_hei": {
          "soc_efficiency": {
            "process_node_score": 9.41,
            "cpu_architecture_score": 10,
            "gpu_architecture_score": 9,
            "total_soc_score": 9.51
          },
          "display_efficiency": {
            "panel_technology_score": 10,
            "refresh_efficiency_score": 7.74,
            "resolution_efficiency_score": 5.22,
            "total_display_score": 7.77
          },
          "connectivity_efficiency": {
            "cellular_score": 0,
            "wifi_score": 0,
            "total_connectivity_score": 0.0
          },
          "thermal_efficiency": {
            "cooling_system_score": 8,
            "thickness_score": 6.5,
            "total_thermal_score": 7.4
          },
          "charging_stress_efficiency": {
            "wired_charging_score": 7.5,
            "wireless_charging_score": 7.0,
            "total_charging_stress_score": 7.35
          },
          "total_hei_score": 7.16
        },
        "layer_c_soi": {
          "os_skin_score": 7,
          "scc_score": 10.0,
          "total_soi_score": 8.2
        }
      },
      "predicted_score": 7.12,
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
      "score_adjustment": {
        "booster": 1.029,
        "source": "GSMArena Active Use + PhoneArena Battery Life"
      },
      "final_score": 7.33
    },
    "5_2_wired_charging_speed": {
      "watts": 45,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "5_3_wireless_charging_speed": {
      "watts": 15,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "5_4_reverse_wireless": {
      "watts": 4.5,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "5_5_reverse_wired": {
      "watts": 0,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "5_6_charger_in_box": {
      "included_watts": 0,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    }
  },
  "6_software_and_longevity": {
    "os_version": "Android 14",
    "skin": "One UI 6.1",
    "6_1_support_longevity": {
      "years_os": 7,
      "years_security": 7,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "6_2_ai_user_capability_index": {
      "afb": {
        "domains_enabled": ["Text", "Image", "Voice", "System", "Productivity"],
        "score": 10.0
      },
      "aei": {
        "execution_model": "Fully On-Device",
        "score": 10.0
      },
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "6_3_system_cleanliness_control": {
      "pal": {
        "third_party_apps_count": 0,
        "score": 10.0
      },
      "rdc": {
        "removable_count": 0,
        "disableable_count": 0,
        "score": 10.0
      },
      "sap": {
        "ads_status": "No system ads",
        "score": 10.0
      },
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    }
  },
  "7_connectivity_and_sensors": {
    "7_1_cellular_capabilities": {
      "features": ["5G mmWave", "5G Sub-6"],
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_2_sim_capabilities": {
      "value": "Dual SIM (Nano + eSIM)",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_3_wifi_standard": {
      "value": "Wi-Fi 7",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_4_bluetooth_codecs": {
      "value": "BT 5.3 + LDAC/aptX HD",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_5_nfc_uwb": {
      "value": "NFC + UWB (Precision)",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_6_biometrics": {
      "value": "Ultrasonic Fingerprint",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_7_sensors": {
      "value": "Full (Gyro, Compass, Baro)",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_8_usb_port_speed": {
      "version": "USB 3.2 Gen 2 (10Gbps)",
      "video_out": true,
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "7_9_ecosystem_continuity": {
      "value": "Seamless (Handoff/DeX/Super)",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    }
  },
  "8_audio": {
    "8_1_speaker_quality": {
      "value": "Balanced Stereo (Hybrid)",
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 0.0
    },
    "8_2_playback_audio_processing_immersion": {
      "audio_format_decode": {
        "dolby_atmos": true,
        "dts_x": false,
        "multichannel_surround": true,
        "score": 8.0
      },
      "spatial_audio_rendering": {
        "head_tracking": false,
        "static_spatial": true,
        "score": 7.0
      },
      "predicted_score": 7.5,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 7.5
    },
    "8_3_wired_audio_capability": {
      "value": "USB-C digital audio only (dongle required)",
      "headphone_jack_3_5mm": false,
      "usb_c_analog_audio": false,
      "usb_c_digital_only": true,
      "predicted_score": 3.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 3.0
    },
    "8_4_microphone_audio_recording": {
      "mhc": {
        "microphone_count": 3,
        "score": 8.0
      },
      "rcm": {
        "recording_channels": "Stereo",
        "score": 8.0
      },
      "acf": {
        "features": ["Directional/Audio Zoom", "Wind noise reduction"],
        "score": 5.0
      },
      "predicted_score": 7.0,
      "score_adjustment": {
        "booster": 1.0,
        "source": "None"
      },
      "final_score": 7.0
    },
    "microphones_count": 3
  },
  "9_financial_and_economic_value": {
    "9_1_price": {
      "usd": 1299
    },
    "price_to_value_ratio": "Fair Price",
    "resale_value": "Good Retention",
    "9_2_repairability": {
      "ifixit_score": 8,
      "eu_repairability_index": 4.0,
      "eu_converted_score": 8.0,
      "predicted_score": 8.0,
      "confidence": "High"
    },
    "9_3_service_ecosystem_support": {
      "support_level": "Self-repair program + parts + manuals",
      "predicted_score": 10.0
    },
    "9_4_warranty_length": "1 Year Standard",
  },
  "10_miscellaneous": {
    "10_1_haptics_quality": "X-Axis Linear (Large)",
    "10_2_stylus_hardware_system_support": "Integrated active stylus + dedicated digitizer + BT features"
  },
  "11_reviews_and_performance_boosters": {
    "11_1_dxomark_camera": {
      "score": 144,
      "url": "https://www.dxomark.com/..."
    },
    "11_2_gsm_arena_battery": {
      "endurance_rating": "Active Use Score",
      "url": "https://www.gsmarena.com/..."
    },
    "11_3_jerryrigeverything": {
      "result": "Passed",
      "url": "https://www.youtube.com/..."
    },
  },
}
```
