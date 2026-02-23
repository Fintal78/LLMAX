import os
import re

SRC_DIR = r"c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\src"

NEW_TOP_LEVEL = {
    "1_design_and_build_quality": "1_design_and_build_quality",
    "2_display": "2_display",
    "8_audio": "3_audio",
    "4_camera_systems": "4_camera_systems",
    "6_software_and_longevity": "5_software_and_longevity",
    "3_processing_power_and_performance": "6_processing_power_and_performance",
    "7_connectivity_and_sensors": "7_connectivity_and_sensors",
    "5_battery_and_charging": "8_battery_and_charging",
    "9_financial_and_economic_value": "9_financial_and_economic_value",
    "10_miscellaneous": "10_miscellaneous",
    "11_reviews_and_performance_boosters": "11_reviews_and_performance_boosters"
}

SUB_KEY_MAP = {
    "2_1_panel_architecture": "2_1_panel_architecture",
    "2_3_brightness": "2_2_brightness",
    "2_4_color_gamut_coverage": "2_3_color_gamut_coverage",
    "2_5_hdr_format_support": "2_4_hdr_format_support",
    "2_2_resolution_density": "2_5_resolution_density",
    "2_6_refresh_rate_max_hz": "2_6_refresh_rate_max_hz",
    "2_7_touch_responsiveness": "2_7_touch_responsiveness",
    "2_10_screen_to_body_ratio": "2_8_screen_to_body_ratio",
    "2_9_screen_size": "2_9_screen_size",
    "2_8_eye_comfort": "2_10_eye_comfort",
    "2_11_display_benchmark_final_scoring": "2_11_display_benchmark_final_scoring",
    "8_1_speaker_quality": "3_1_speaker_quality",
    "8_2_playback_audio_processing_immersion": "3_2_playback_audio_processing_immersion",
    "8_3_wired_audio_capability": "3_3_wired_audio_capability",
    "8_4_microphone_audio_recording": "3_4_microphone_audio_recording",
    "4_1_main_sensor_size": "4_1_main_sensor_size",
    "4_2_main_camera_aperture": "4_2_main_camera_aperture",
    "4_3_main_camera_resolution": "4_3_main_camera_resolution",
    "4_4_image_stabilization": "4_4_image_stabilization",
    "4_6_ultrawide_capability": "4_5_ultrawide_capability",
    "4_5_zoom_capability": "4_6_zoom_capability",
    "4_7_macro_capability": "4_7_macro_capability",
    "4_13_front_camera_resolution": "4_8_front_camera_resolution",
    "4_14_front_camera_focus": "4_9_front_camera_focus",
    "4_8_rear_video_resolution": "4_10_rear_video_resolution",
    "4_9_rear_video_fps": "4_11_rear_video_fps",
    "4_10_video_hdr": "4_12_video_hdr",
    "4_11_video_encoding": "4_13_video_encoding",
    "4_12_slow_motion": "4_14_slow_motion",
    "4_15_front_camera_video": "4_15_front_camera_video",
    "4_16_multiframe_photo": "4_16_multiframe_photo",
    "4_17_semantic_ai": "4_17_semantic_ai",
    "4_18_generative_ai_tools": "4_18_generative_ai_tools",
    "6_1_support_longevity": "5_1_support_longevity",
    "6_3_system_cleanliness_control": "5_2_system_cleanliness_control",
    "6_2_ai_feature_suite": "5_3_ai_feature_suite",
    "3_1_cpu_multi_core_performance": "6_1_cpu_multi_core_performance",
    "3_2_cpu_architecture_single_core": "6_2_cpu_architecture_single_core",
    "3_3_gpu_performance": "6_3_gpu_performance",
    "3_10_npu_hardware_performance": "6_4_npu_hardware_performance",
    "3_5_ram_technology": "6_5_ram_technology",
    "3_6_ram_capacity": "6_6_ram_capacity",
    "3_7_storage_technology": "6_7_storage_technology",
    "3_8_storage_capacity": "6_8_storage_capacity",
    "3_9_storage_expandability": "6_9_storage_expandability",
    "3_4_thermal_dissipation_stability": "6_10_thermal_dissipation_stability",
    "3_1_0_soc_reference": "6_1_0_soc_reference",
    "3_3_0_gpu_architecture_reference": "6_3_0_gpu_architecture_reference",
    "7_1_cellular_capabilities": "7_1_cellular_capabilities",
    "7_2_sim_capabilities": "7_2_sim_capabilities",
    "7_3_wifi_standard": "7_3_wifi_standard",
    "7_4_bluetooth_codecs": "7_4_bluetooth_codecs",
    "7_6_biometrics": "7_5_biometrics",
    "7_7_sensors": "7_6_sensors",
    "7_5_nfc_uwb": "7_7_nfc_uwb",
    "7_9_ecosystem_continuity": "7_8_ecosystem_continuity",
    "7_8_usb_port_speed": "7_9_usb_port_speed",
    "5_1_battery_endurance": "8_1_battery_endurance",
    "5_2_wired_charging_speed": "8_2_wired_charging_speed",
    "5_3_wireless_charging_speed": "8_3_wireless_charging_speed",
    "5_5_reverse_wired": "8_4_reverse_wired",
    "5_4_reverse_wireless": "8_5_reverse_wireless",
    "5_6_charger_in_box": "8_6_charger_in_box",
    "9_1_price": "9_1_price",
    "9_3_manufacturer_warranty_commitment": "9_2_manufacturer_warranty_commitment",
    "9_2_repairability": "9_3_repairability",
}

# Merge all mappings into one mega dict
ALL_MAPPINGS = {**NEW_TOP_LEVEL, **SUB_KEY_MAP}

# Sort by length descending to prevent partial replacements (e.g. replacing '3_1' inside '3_10')
sorted_keys = sorted(ALL_MAPPINGS.keys(), key=len, reverse=True)

for root, _, files in os.walk(SRC_DIR):
    for f in files:
        if f.endswith(".py"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            
            original = content
            # Apply replacements, ensuring we only match inside string quotes to be safe
            for old_key in sorted_keys:
                new_key = ALL_MAPPINGS[old_key]
                if old_key != new_key:
                    # Match "old_key" or 'old_key'
                    content = re.sub(rf'"{old_key}"', f'"{new_key}"', content)
                    content = re.sub(rf"'{old_key}'", f"'{new_key}'", content)
            
            if content != original:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(content)
                print(f"Updated {f}")

print("Python source files refactored!")
