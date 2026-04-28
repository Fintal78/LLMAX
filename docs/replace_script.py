import json

content = """      "6_10_thermal_dissipation_stability": {
        // SCORING GOAL: Evaluates internal cooling capability and sustained performance using the Thermodynamic RC Model.
        // This section bridges physical heat dissipation capacity (Watts) to visual stability (FPS) using a 0.333 Gamma scaling factor.

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD A — Direct Benchmark (Primary Standard: 3DMark Wild Life Extreme)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_a_benchmark_TDSI": {
          "value": 59.0,
          // GUIDELINE: Stability percentage from a 20-minute 3DMark Wild Life Extreme Stress Test.
          "source": "https://benchmarks.ul.com/hardware/phone/Samsung+Galaxy+S24+Ultra+review",
          "exact_extract": "Median Wild Life Extreme Stability: 59%",
          "subscore": 4.24
          // SCORING GUIDELINE: subscore = 10 * (log(value) - log(Thermal_Stability_Min)) / (log(Thermal_Stability_Max) - log(Thermal_Stability_Min)), clamped 0-10. (Min=40, Max=100).
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD B — Nearest Neighbor Interpolation (Secondary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_b_neighbor_interpolation_TDSI": {
          "neighbors": [
            {
              "device_id_1": "apple_iphone_15_pro_max",
              "predicted_score_1": 4.65,
              "benchmark_score_1": 4.40
            },
            {
              "device_id_2": "xiaomi_14_pro",
              "predicted_score_2": 5.10,
              "benchmark_score_2": 4.85
            },
            {
              "device_id_3": "google_pixel_8_pro",
              "predicted_score_3": 4.80,
              "benchmark_score_3": 4.15
            }
          ],
          "avg_predicted_neighbors": 4.85,
          "avg_benchmark_neighbors": 4.46,
          "correction_ratio": 1.037,
          "interpolated_score": 4.62
          // SCORING GUIDELINE: standard correction ratio interpolation based on Method C predicted scores.
        },

        // ═══════════════════════════════════════════════════════════════════════════
        // METHOD C — Thermodynamic RC Prediction Model (Tertiary)
        // ═══════════════════════════════════════════════════════════════════════════
        "method_c_prediction_model_TDSI": {
          "phase_a_geometric_volume": {
             // SCORING GUIDELINE: Base geometric bounds that dictate potential cooling area.
             "height_mm": { "value_path": "1_identity_and_materials.1_2_dimensions_and_weight.height_mm.value", "value": 162.3 },
             "width_mm": { "value_path": "1_identity_and_materials.1_2_dimensions_and_weight.width_mm.value", "value": 79.0 },
             "thickness_mm": { "value_path": "1_identity_and_materials.1_2_dimensions_and_weight.thickness_mm.value", "value": 8.6 },
             "diagonal_inch": { "value_path": "2_display.2_1_display_size.size.value", "value": 6.8 },
             "aspect_ratio": { "value": 2.16, "calculation": "19.5 / 9", "description": "Derived from screen resolution or explicitly stated." },
             "footprint_area_m2": {
                "value": 0.01282,
                "calculation": "(height_mm * width_mm) / 1000000"
             },
             "frame_radiator_area_m2": {
                "value": 0.00353,
                "calculation": "2 * ((height_mm/1000) + (width_mm/1000)) * (thickness_mm/1000) * 0.85",
                "description": "0.85 (Chi factor) accounts for ergonomic chamfers."
             },
             "display_surface_area_cm2": {
                "value": 113.5,
                "calculation": "(diagonal_inch * 2.54)^2 * (aspect_ratio / (aspect_ratio^2 + 1))"
             }
          },
          "phase_b_multi_path_thermal_resistance": {
            // SCORING GUIDELINE: Evaluation of three primary parallel heat paths. Conductive resistance (R_cond) is safely omitted physically as it contributes <2% to resistance compared to ambient convection (R_conv).
            "cooling_stack_configuration": [
              {
                "technology": "High-Volume VC",
                "source": "https://www.samsung.com/global/galaxy/galaxy-s24-ultra/",
                "exact_extract": "1.9x larger Vapor Chamber",
                "coverage_area_mm2": 4050,
                "alpha_constant": 2.7,
                "phi_factor": 0.316
                // SCORING GUIDELINE: Alpha and Phi are defined in the Calibration Table.
                // | Technology Class               |  alpha  |      phi      |
                // | :----------------------------- | :------ | :------------ |
                // | None (SoC Only)                | 0.0     | 0.0           |
                // | Standard Graphite Sheet        | 0.6     | 0.40          |
                // | Multi-layer Graphite           | 0.8     | 0.50          |
                // | Synthetic Graphene Film        | 1.2     | 0.50          |
                // | Professional Vapor Chamber     | 2.7     | Area_VC / Area_face_mm2 |
              },
              {
                "technology": "Multi-layer Graphite",
                "source": "https://www.samsung.com/global/galaxy/",
                "exact_extract": "Multi-layer graphite sheets",
                "coverage_area_mm2": null,
                "alpha_constant": 0.8,
                "phi_factor": 0.50
              }
            ],
            "back_panel_material_class": {
              "value_path": "1_identity_and_materials.1_1_structural_build.back_panel.value",
              "value": "Tier 3: Basic Glass",
              "s_0_baseline": 0.05,
              "s_max_ceiling": 0.95
              // SCORING GUIDELINE: s_0 and s_max defined by material class.
              // Class 1 (Conductive Metal): s_0 = 0.60, s_max = 1.00
              // Class 2 (Moderate Alloy): s_0 = 0.25, s_max = 1.00
              // Class 3 (Insulating Glass/Polymer): s_0 = 0.05, s_max = 0.95
            },
            "back_spreading_efficiency_s_eff": {
              "value": 0.693,
              "calculation": "s_0_baseline + (s_max_ceiling - s_0_baseline) * [ 1 - exp(-Sum(alpha_i * phi_i)) ]"
              // SCORING GUIDELINE: Cumulate the efforts of all technologies in cooling_stack_configuration.
            },
            "path_1_front_screen": {
               "s_eff_front": 0.25,
               // SCORING GUIDELINE: Front screen spreading efficiency is always constant 0.25 due to PCB Thermal Wall.
               "area_active_m2": {
                  "value": 0.00320,
                  "calculation": "footprint_area_m2 * s_eff_front"
               },
               "r_path_front": {
                  "value": 31.25,
                  "calculation": "1 / (10.0 * area_active_m2)"
               }
            },
            "path_2_mid_frame": {
               "frame_material_class": {
                 "value_path": "1_identity_and_materials.1_1_structural_build.frame.value",
                 "value": "Tier 2: Titanium Grade 1-4",
                 "s_eff_frame": 0.40
                 // SCORING GUIDELINE: Frame spreading efficiency depends strictly on material class:
                 // Class 1 (Metal): 1.00
                 // Class 2 (Alloy): 0.40
                 // Class 3 (Polymer): 0.05
               },
               "area_active_m2": {
                  "value": 0.00141,
                  "calculation": "frame_radiator_area_m2 * s_eff_frame"
               },
               "r_path_frame": {
                  "value": 70.92,
                  "calculation": "1 / (10.0 * area_active_m2)"
               }
            },
            "path_3_back_panel": {
               "h_conv": {
                  "value": 10.0,
                  "calculation": "Passive baseline is 10.0. If integrated fan is active: 10.0 + [ 7.0 * (Fan_RPM / 20000)^0.8 ]"
               },
               "area_active_m2": {
                  "value": 0.00888,
                  "calculation": "footprint_area_m2 * back_spreading_efficiency_s_eff"
               },
               "r_path_back": {
                  "value": 11.26,
                  "calculation": "1 / (h_conv * area_active_m2)"
               }
            },
            "total_system_resistance_r_total": {
               "value": 7.41,
               "calculation": "(1/r_path_front + 1/r_path_frame + 1/r_path_back)^-1"
               // SCORING GUIDELINE: Parallel thermal resistance circuit combining Front, Mid-Frame, and Back paths.
            }
          },
          "phase_c_foundational_energy_balance": {
            "thermal_capacitance_c": {
               "chassis_mass_kg": { "value_path": "1_identity_and_materials.1_2_dimensions_and_weight.weight_g.value", "value": 0.232 },
               "pcm_buffer_constant_sigma": 0.0,
               // SCORING GUIDELINE: Advanced modifier for Phase Change Materials (PCM). Sigma = 0.75 for Advanced PCM Matrix, 0.50 for Basic PCM Pad, 0.0 otherwise.
               "value": 197.2,
               "calculation": "(chassis_mass_kg * 850) + (pcm_buffer_constant_sigma * 25)"
            },
            "time_constant_tau_s": {
               "value": 1461,
               "calculation": "total_system_resistance_r_total * thermal_capacitance_c"
            },
            "admissible_thermal_power_p_adm_watts": {
               "value": 4.82,
               "calculation": "20 / (total_system_resistance_r_total * (1 - exp(-1200 / time_constant_tau_s)))"
               // SCORING GUIDELINE: 20 is Delta_T_limit safety threshold (ergonomic limit for 25C ambient). 1200 is evaluation window (20mins).
            }
          },
          "phase_d_net_soc_budget_and_prediction": {
            "system_base_heat_p_base_watts": {
               "p_static": 0.40,
               "k_display_heat": 0.0075,
               // SCORING GUIDELINE: Joule heating factor from display normalized via k_display_heat = 0.0075.
               "display_area_cm2": { "value_path": "6_10_thermal_dissipation_stability.method_c_prediction_model_TDSI.phase_a_geometric_volume.display_surface_area_cm2.value", "value": 113.5 },
               "value": 1.25,
               "calculation": "p_static + (display_area_cm2 * k_display_heat)"
            },
            "admissible_soc_power_p_adm_soc_watts": {
               "value": 3.57,
               "calculation": "admissible_thermal_power_p_adm_watts - system_base_heat_p_base_watts"
            },
            "heat_generation_soc_p_gen_watts": {
               // █ SOC_PEAK_POWER_MATRIX:
               // | SoC Model                                 | Peak Power (W) | Node  | Foundry |
               // | :---------------------------------------- | :------------: | :---: | :-----: |
               // | **Snapdragon 8 Elite**                    | **19.5**       | 3nm   | TSMC    |
               // | **Snapdragon 8 Gen 1**                    | **16.5**       | 4nm   | Samsung |
               // | **Dimensity 9400**                        | **15.5**       | 3nm   | TSMC    |
               // | **Apple A18 Pro**                         | **14.5**       | 3nm   | TSMC    |
               // | **Snapdragon 8 Gen 3**                    | **14.0**       | 4nm   | TSMC    |
               // | **Exynos 2400**                           | **12.5**       | 4nm   | Samsung |
               // | **Dimensity 9300**                        | **12.0**       | 4nm   | TSMC    |
               // | **Apple A17 Pro**                         | **11.5**       | 3nm   | TSMC    |
               // | **Snapdragon 888**                        | **10.5**       | 5nm   | Samsung |
               // | **Google Tensor G3**                      | **9.5**        | 4nm   | Samsung |
               // | **Snapdragon 8 Gen 2**                    | **9.0**        | 4nm   | TSMC    |
               // | **Apple A16 Bionic**                      | **8.5**        | 4nm   | TSMC    |
               // | **Snapdragon 8+ Gen 1**                   | **8.0**        | 4nm   | TSMC    |
               // | **Apple A15 Bionic**                      | **7.5**        | 5nm   | TSMC    |
               // | **Snapdragon 865**                        | **6.2**        | 7nm   | TSMC    |
               // | **Apple A14 Bionic**                      | **5.8**        | 5nm   | TSMC    |
               // | **Snapdragon 855**                        | **5.2**        | 7nm   | TSMC    |
               "identifier": "Snapdragon 8 Gen 3",
               "reference_table": "SOC_PEAK_POWER_MATRIX",
               "lookup_parameter": "Peak Power (P_peak) [Watts]",
               "value": 14.0
            },
            "power_ratio": {
               "value": 0.255,
               "calculation": "admissible_soc_power_p_adm_soc_watts / heat_generation_soc_p_gen_watts"
               // SCORING GUIDELINE: Power ratio is capped at a maximum of 1.0 (100%).
            },
            "predicted_stability_percentage": {
               "value": 63.4,
               "calculation": "(power_ratio ^ 0.333) * 100"
               // SCORING GUIDELINE: Cube root law bridging thermal power throttling to physical FPS gaming stability.
            },
            "predicted_tdsi_score": {
               "value": 5.03,
               "calculation": "10 * (log(predicted_stability_percentage) - log(Thermal_Stability_Min)) / (log(Thermal_Stability_Max) - log(Thermal_Stability_Min))"
               // SCORING GUIDELINE: Logarithmic normalization from 40 to 100 range. (Min=40, Max=100).
            }
          }
        },

        "scores": {
          "predicted": 5.03,
          "final": {
            // ⚠ MANDATORY: This block follows FINAL_SCORE_PREDICTOR_TEMPLATE (defined in file header). Do NOT add inline scoring guidelines here.
            "value": 4.24,
            "method_used": "Benchmark (3DMark)",
            "booster": "No",
            "confidence": "N/A"
          }
        }
      }"""

with open("C:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/proposed_data_structure.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_index = -1
end_index = -1

for i, line in enumerate(lines):
    if '"6_10_thermal_dissipation_stability": {' in line:
        start_index = i
        break

if start_index != -1:
    brace_count = 0
    for i in range(start_index, len(lines)):
        brace_count += lines[i].count('{') - lines[i].count('}')
        if brace_count == 0:
            end_index = i
            break

if start_index != -1 and end_index != -1:
    lines[start_index:end_index+1] = [content + '\n']
    with open("C:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/proposed_data_structure.md", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Replaced lines {start_index+1} to {end_index+1}.")
else:
    print("Could not find start or end index.")
