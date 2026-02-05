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
    "id": {
      "value": "samsung_galaxy_s24_ultra",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "brand": {
      "value": "Samsung",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "model_name": {
      "value": "Galaxy S24 Ultra",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "series": {
      "value": "Galaxy S",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "model_aliases": {
      "value": [
        "SM-S928B",
        "SM-S928U"
      ],
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "codename": {
      "value": "Eureka",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "release_date": {
      "value": "2024-01-24",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "announce_date": {
      "value": "2024-01-17",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "status": {
      "value": "Available",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "market_regions": {
      "value": [
        "Global"
      ],
      "source": "TBD",
      "exact_extract": "Proof pending"
    }
  },
  "1_design_and_build_quality": {
    "form_factor": {
      "value": "Bar",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "1_1_materials": {
      "frame_material": {
        "value": "Titanium Alloy Frame",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "back_material": {
        "value": "Strengthened Glass Back",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "description": {
        "value": "Titanium Frame + Gorilla Glass Armor Back",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "1_2_durability": {
      "ip_rating": {
        "value": "IP68",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "dust_protection_digit": {
        "value": 6,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "water_protection_digit": {
        "value": 8,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "1_3_glass_protection": {
      "value": {
        "value": "Gorilla Glass Armor",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "1_4_dimensions": {
      "thickness_mm": {
        "value": 8.6,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
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
    "1_5_weight": {
      "weight_g": {
        "value": 232,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "1_6_ergonomics": {
      "width_mm": {
        "value": 79.0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "colors": [
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
    ]
  },
  "2_display": {
    "aspect_ratio": {
      "value": "19.5:9",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "panel_type": {
      "value": "OLED",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "2_1_panel_architecture": {
      "value": {
        "value": "LTPO OLED",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_2_resolution_density": {
      "ppi": {
        "value": 505,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "megapixels_mp": {
        "value": 6.9,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_3_brightness": {
      "peak_nits": {
        "value": 2600,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_4_color_gamut_coverage": {
      "dci_p3_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "srgb_percent": {
        "value": 100,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "score_adjustment": {
        "booster_1": {
          "value": 1.05,
          "booster_title": "11_2_toms_guide_display_factory_calibration"
        }
      },
      "final_score": 0.0
    },
    "2_5_hdr_format_support": {
      "formats": {
        "value": [
          "HDR10+",
          "HDR10",
          "HLG"
        ],
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_6_refresh_rate": {
      "max_hz": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "min_hz": {
        "value": 1,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "adaptive": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_7_touch_responsiveness": {
      "sampling_rate_hz": {
        "value": 240,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_8_eye_comfort": {
      "pwm_dimming_hz": {
        "value": 492,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_9_screen_size": {
      "diagonal_inches": {
        "value": 6.8,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "2_10_screen_to_body_ratio": {
      "percent": {
        "value": 88.5,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    }
  },
  "3_processing_power_and_performance": {
    "cpu_specifications": {
      "clusters": [
        {
          "name": {
            "value": "Cortex-X4",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "count": {
            "value": 1,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "freq_ghz": {
            "value": 3.4,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        {
          "name": {
            "value": "Cortex-A720",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "count": {
            "value": 3,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "freq_ghz": {
            "value": 3.15,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        {
          "name": {
            "value": "Cortex-A720",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "count": {
            "value": 2,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "freq_ghz": {
            "value": 2.96,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        },
        {
          "name": {
            "value": "Cortex-A520",
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "count": {
            "value": 2,
            "source": "TBD",
            "exact_extract": "Proof pending"
          },
          "freq_ghz": {
            "value": 2.27,
            "source": "TBD",
            "exact_extract": "Proof pending"
          }
        }
      ]
    },
    "3_1_soc_performance": {
      "geekbench_6_multi_score": 7200,
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_2_cpu_architecture_single_core": {
      "geekbench_6_single_score": 2200,
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_3_gpu_performance": {
      "gpu_model": {
        "value": "Adreno 750",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
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
      "ray_tracing_support": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_4_efficiency_node": {
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
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_5_thermal_dissipation_stability": {
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
      "final_score": 0.0
    },
    "3_6_ram_technology": {
      "value": {
        "value": "LPDDR5X",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_7_ram_capacity": {
      "max_gb": {
        "value": 12,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_8_storage_technology": {
      "value": {
        "value": "UFS 4.0",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_9_storage_capacity": {
      "max_gb": {
        "value": 1024,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "3_10_storage_expandability": {
      "value": {
        "value": "No Expansion Slot",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
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
      "value": {
        "value": "1/1.3 inches",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_2_main_camera_aperture": {
      "value": {
        "value": "f/1.7",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_3_main_camera_resolution": {
      "mp": {
        "value": 200,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_4_image_stabilization": {
      "value": {
        "value": "Standard OIS",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_5_zoom_capability": {
      "optical_zoom_x": {
        "value": 5,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_6_ultrawide_capability": {
      "presence": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "fov_degrees": {
        "value": 120,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "ultrawide_sensor_size": {
        "value": "1/2.0",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_7_macro_capability": {
      "ultrawide_af": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "min_focus_distance_cm": {
        "value": 2.5,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "dedicated_macro_mp": {
        "value": 0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "4_8_rear_video_resolution": {
      "max_resolution": {
        "value": "8K",
        "source": "TBD",
        "exact_extract": "Proof pending"
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
      "pcs": {
        "professional_codec_support": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "codec_name": {
          "value": "ProRes",
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 10.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "lcps": {
        "log_profile_available": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "profile_name": {
          "value": "Log",
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 10.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "cbd": {
        "bit_depth": {
          "value": 10,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 10.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
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
  "5_battery_and_charging": {
    "5_1_battery_endurance": {
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
      "battery_type": {
        "value": "Li-Ion 5000 mAh, non-removable",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "scoring_components": {
        "layer_a_energy": {
          "wh": 19.25,
          "score": 6.62
        },
        "layer_b_hei": {
          "soc_efficiency": {
            "process_node_score": 8.48,
            "cpu_architecture_score": 5,
            "gpu_architecture_score": 5,
            "total_soc_score": 6.74
          },
          "display_efficiency": {
            "panel_technology_score": 5,
            "refresh_efficiency_score": 3.33,
            "resolution_efficiency_score": 7.82,
            "total_display_score": 5.26
          },
          "connectivity_efficiency": {
            "cellular_score": 0,
            "wifi_score": 0,
            "total_connectivity_score": 0.0
          },
          "thermal_efficiency": {
            "frame_material_score": 10,
            "weight_score": 8.36,
            "surface_area_score": 10,
            "thickness_score": 6.5,
            "part_a_chassis_score": 9.07,
            "cooling_system_score": 7,
            "thermal_demand_bonus": 0.13,
            "tdsi_score": 8.16
          },
          "total_hei_score": 5.62
        },
        "layer_c_soi": {
          "os_skin_score": 10,
          "scc_score": 10.0,
          "total_soi_score": 10.0
        }
      },
      "predicted_score": 6.95,
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
        "booster": 1.055,
        "source": "GSMArena Active Use + PhoneArena Battery Life"
      },
      "final_score": 7.33
    },
    "5_2_wired_charging_speed": {
      "watts": {
        "value": 45,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "5_3_wireless_charging_speed": {
      "watts": {
        "value": 15,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "5_4_reverse_wireless": {
      "watts": {
        "value": 4.5,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "5_5_reverse_wired": {
      "watts": {
        "value": 0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "5_6_charger_in_box": {
      "included_watts": {
        "value": 0,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    }
  },
  "6_software_and_longevity": {
    "os_version": {
      "value": "Android 14",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "skin": {
      "value": "One UI 6.1",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "6_1_support_longevity": {
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
    "6_2_ai_user_capability_index": {
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
    },
    "6_3_system_cleanliness_control": {
      "platform_score": 6.0,
      "predicted_score": 6.0,
      "final_score": 6.0
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
    "7_5_nfc_uwb": {
      "value": {
        "value": "NFC + UWB (Precision)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_6_biometrics": {
      "value": {
        "value": "Ultrasonic Fingerprint",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_7_sensors": {
      "value": {
        "value": "Full (Gyro, Compass, Baro)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "7_8_usb_port_speed": {
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
    },
    "7_9_ecosystem_continuity": {
      "value": {
        "value": "Seamless (Handoff/DeX/Super)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    }
  },
  "8_audio": {
    "8_1_speaker_quality": {
      "value": {
        "value": "Balanced Stereo (Hybrid)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 0.0,
      "final_score": 0.0
    },
    "8_2_playback_audio_processing_immersion": {
      "audio_format_decode": {
        "dolby_atmos": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "dts_x": {
          "value": false,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "multichannel_surround": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 8.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "spatial_audio_rendering": {
        "head_tracking": {
          "value": false,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "static_spatial": {
          "value": true,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 7.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "predicted_score": 7.5,
      "final_score": 7.5
    },
    "8_3_wired_audio_capability": {
      "value": {
        "value": "USB-C digital audio only (dongle required)",
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "headphone_jack_3_5mm": {
        "value": false,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "usb_c_analog_audio": {
        "value": false,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "usb_c_digital_only": {
        "value": true,
        "source": "TBD",
        "exact_extract": "Proof pending"
      },
      "predicted_score": 3.0,
      "final_score": 3.0
    },
    "8_4_microphone_audio_recording": {
      "mhc": {
        "microphone_count": {
          "value": 3,
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 8.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "rcm": {
        "recording_channels": {
          "value": "Stereo",
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 8.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "acf": {
        "features": {
          "value": [
            "Directional/Audio Zoom",
            "Wind noise reduction"
          ],
          "source": "TBD",
          "exact_extract": "Proof pending"
        },
        "score": {
          "value": 5.0,
          "source": "TBD",
          "exact_extract": "Proof pending"
        }
      },
      "predicted_score": 7.0,
      "final_score": 7.0
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
    "price_to_value_ratio": {
      "value": "Fair Price",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "resale_value": {
      "value": "Good Retention",
      "source": "TBD",
      "exact_extract": "Proof pending"
    },
    "9_2_repairability": {
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
    },
    "9_3_manufacturer_warranty_commitment": {
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
        "unaccounted_reason": "Section 4.3 scores sensor resolution (48MP hardware), and Section 4.16 scores multi-frame processing presence (Always-on HDR + Night stacking). However, neither captures the quality impact of Apple's decision to output 24MP images by default rather than standard 12MP binned images, which the review explicitly credits for improved texture preservation.",
        "observed_justification": "The camera in Apple's new flagship device comes with an entirely new texture rendering management, and in our tests the results were outstanding. With most lighting conditions resulting in 24MP images, finest details were preserved much better than on most competitors. [...] The Apple iPhone 15 Pro Max provided very natural skin rendering with subtle local contrast and pleasant rendering of the finest details like hair, lips, wrinkles, etc."
      }
    },
    "11_2_toms_guide_display_factory_calibration": {
      "source_link": "https://www.tomsguide.com/reviews/iphone-15-pro-max",
      "impacted_subsection": "2.4",
      "booster": 1.05,
      "justification": {
        "unaccounted_feature": "it earned a Delta-E score of 0.14 (where zero is perfect)",
        "unaccounted_reason": "Section 2.4 scores DCI-P3 coverage percentage, which measures what colors the display *can* show. It does not measure factory calibration accuracy (Delta-E), which determines how *correctly* those colors are rendered. A display with 100% DCI-P3 coverage but poor calibration will show inaccurate colors.",
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
