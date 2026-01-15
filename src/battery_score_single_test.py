"""
Battery Score Calculator - Single Phone Test Mode

DESCRIPTION:
This script is for TESTING and DOCUMENTATION purposes only.
It calculates battery scores for a single phone defined in a markdown file
(docs/proposed_data_structure.md).

IMPORTANT LIMITATIONS:
❌ Does NOT have access to full database
❌ Cannot perform nearest neighbor interpolation (Case 3)
❌ Falls back to predicted score when no benchmarks available
❌ NOT suitable for production scoring

SCORING METHODOLOGY:
- Case 1: Phone with both benchmarks → Use benchmark average
- Case 2: Phone with one benchmark → Use that benchmark  
- Case 3: Phone with no benchmarks → FALLBACK to predicted score (NO interpolation)

USE CASES:
✓ Testing scoring logic on example phone in docs/proposed_data_structure.md
✓ Validating layer calculations (A, B, C)
✓ Documentation and explanation purposes
✓ Debugging individual phone score calculations
✓ Quick verification of scoring formulas

FOR PRODUCTION USE:
- To score all phones: Use battery_score_full_database.py
- To score one new phone: Use battery_score_new_phone.py

USAGE:
    python battery_score_single_test.py
    
INPUT: Reads from docs/proposed_data_structure.md
OUTPUT: Updates the markdown file with calculated scores

SEE ALSO:
- battery_score_full_database.py - Score entire database with interpolation
- battery_score_new_phone.py - Fast method for scoring single new phone
- docs/BATTERY_SCORING_PROCESS.md - Complete lifecycle documentation
"""

import json
import re

# --- Constants & Tables ---

# Layer B.1.1 Process Node (Continuous)
PROCESS_NODE_MIN = 3
PROCESS_NODE_MAX = 20

# Layer B.1.2 CPU Class
CPU_SCORES = {
    "Cortex-X4": 10, "Cortex-X925": 10, "Apple A17": 10, "Apple A18": 10,
    "Cortex-X3": 9,
    "Cortex-X2": 8,
    "Cortex-A720": 7, "Cortex-A715": 7, "Cortex-A710": 7, "Cortex-A78": 7,
    "Cortex-A77": 6, "Cortex-A76": 6,
    "Cortex-A75": 5, "Cortex-A73": 5,
    "Cortex-A55": 2,
    "Cortex-A53": 0, "Cortex-A7": 0
}

# Layer B.1.3 GPU Class
GPU_SCORES = {
    "Apple GPU": 10,
    "Adreno 750": 9, "Adreno 740": 9, "Immortalis-G720": 9,
    "Adreno 730": 8, "Mali-G715": 8,
    "Adreno 660": 6, "Mali-G610": 6,
    "Mali-G57": 2,
    "Mali-G52": 0
}

# Layer B.2.1 Panel Technology
PANEL_SCORES = {
    "LTPO OLED": 10, "LTPO AMOLED": 10,
    "OLED": 10, "AMOLED": 9, "Super AMOLED": 9, "Dynamic AMOLED": 9, "Dynamic AMOLED 2X": 9,
    "IPS LCD": 6, "IPS": 6,
    "TFT": 2, "PLS": 2,
    "LCD": 0
}

# Layer B.3.1 Cellular (Inverted)
CELLULAR_SCORES = {
    "2G": 10,
    "3G": 8,
    "4G": 6, "LTE": 6,
    "5G": 4, "5G Sub-6": 4,
    "5G mmWave": 0
}

# Layer B.3.2 Wi-Fi (Inverted)
WIFI_SCORES = {
    "Wi-Fi 4": 10, "802.11n": 10,
    "Wi-Fi 5": 8, "802.11ac": 8,
    "Wi-Fi 6": 6, "802.11ax": 6,
    "Wi-Fi 6E": 4,
    "Wi-Fi 7": 0, "802.11be": 0
}

# Layer B.4.1 Cooling
COOLING_SCORES = {
    "Active fan": 10,
    "Vapor chamber": 8,
    "Heat pipe": 6, "Graphite": 4, "Copper foil": 4,
    "None": 0
}

# Layer C.1 OS/Skin
OS_SKIN_SCORES = {
    "iOS": 10,
    "Stock Android": 9, "Pixel UI": 9,
    "MyUX": 8, "Xperia UI": 8, "ZenUI": 8,
    "One UI": 7,
    "HyperOS": 6, "MIUI": 6, "ColorOS": 6, "OxygenOS": 6, "Funtouch OS": 6, "Realme UI": 6, "MagicOS": 6,
    "Go Edition": 2,
    "Android 10": 0, "Android 9": 0
}

# Layer C.2 Bloatware
# Layer C.2 System Cleanliness & Control (SCC)
# Formula: SCC = 0.4 * PAL + 0.35 * RDC + 0.25 * SAP
# Note: This is now calculated dynamically, not via a simple dict lookup.

# --- Helper Functions ---

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def calculate_scc(pal_count, rdc_removable, rdc_disableable, sap_status):
    """
    Calculates System Cleanliness & Control (SCC) score.
    """
    # 1. Preinstalled App Load (PAL)
    # Formula: clamp(10 - 1 * Third_Party_Apps, 0, 10)
    pal_score = clamp(10 - 1 * pal_count, 0, 10)
    
    # 2. Removability & Disable Control (RDC)
    # Formula: 10 * (Removable + 0.5 * Disableable) / Total_Preinstalled
    # Special case: If Total_Preinstalled = 0 -> RDC = 10
    total_apps = pal_count # Assuming pal_count is the total relevant preinstalled apps
    if total_apps == 0:
        rdc_score = 10.0
    else:
        rdc_score = 10 * (rdc_removable + 0.5 * rdc_disableable) / total_apps
        rdc_score = clamp(rdc_score, 0, 10)
        
    # 3. System-Level Advertising Presence (SLAP)
    # Scoring: 10 (None), 5 (Optional), 0 (Persistent)
    sap_scores = {
        "No system ads": 10.0,
        "Optional / Disableable": 5.0,
        "Persistent": 0.0
    }
    # Fallback to old keys just in case, mapping to nearest new score
    sap_scores.update({
        "Disabled by one toggle": 5.0,
        "Disabled by multiple toggles": 5.0,
        "Cannot be fully disabled": 0.0,
        "Persistent ads": 0.0
    })
    
    sap_score = sap_scores.get(sap_status, 0.0)
    
    # Final SCC Calculation
    # Formula: SCC = (0.4 * PAL) + (0.35 * RDC) + (0.25 * SLAP)
    scc_final = (0.4 * pal_score) + (0.35 * rdc_score) + (0.25 * sap_score)
    return round(scc_final, 1)

def normalize_linear(value, min_val, max_val, min_score=0, max_score=10):
    if max_val == min_val: return min_score
    score = min_score + (max_score - min_score) * (value - min_val) / (max_val - min_val)
    return clamp(score, 0, 10)

def get_best_match(value, score_dict, default=5):
    if not value: return default
    # Direct match
    if value in score_dict: return score_dict[value]
    # Partial match (longest match wins)
    matches = [k for k in score_dict.keys() if k.lower() in str(value).lower()]
    if matches:
        best_match = max(matches, key=len)
        return score_dict[best_match]
    return default

# --- Layer Calculation Functions ---

def calc_layer_a(data):
    mah = data.get("5_battery_and_charging", {}).get("5_1_battery_capacity", {}).get("mah", 0)
    voltage_raw = data.get("5_battery_and_charging", {}).get("5_1_battery_capacity", {}).get("battery_voltage_v", "Not available")
    
    voltage = 3.85
    if isinstance(voltage_raw, (int, float)):
        voltage = voltage_raw
    
    wh = (mah * voltage) / 1000
    score = normalize_linear(wh, 8, 25)
    
    return {"wh": wh, "score": round(score, 2)}

def calc_layer_b(data):
    # B.1 SoC
    process_nm = data.get("3_processing_power_and_performance", {}).get("3_4_efficiency_node", {}).get("process_nm", 4)
    process_score = normalize_linear(process_nm, 20, 3, min_score=0, max_score=10) # Inverted logic in normalize params? No, standard normalize is value-min/max-min. Here smaller is better.
    # Correct continuous inverted: 10 - 10 * (nm - 3) / (20 - 3)
    process_score = 10 - 10 * (process_nm - 3) / (20 - 3)
    process_score = clamp(process_score, 0, 10)

    cpu_name = data.get("3_processing_power_and_performance", {}).get("3_2_cpu_structure", {}).get("clusters", [{}])[0].get("name", "")
    cpu_score = get_best_match(cpu_name, CPU_SCORES, default=5)

    gpu_model = data.get("3_processing_power_and_performance", {}).get("3_3_gpu_performance", {}).get("model", "")
    gpu_score = get_best_match(gpu_model, GPU_SCORES, default=5)

    soc_total = 0.5 * process_score + 0.3 * cpu_score + 0.2 * gpu_score

    # B.2 Display
    panel_tech = data.get("2_display", {}).get("2_1_technology", {}).get("value", "")
    panel_score = get_best_match(panel_tech, PANEL_SCORES, default=5)

    refresh_data = data.get("2_display", {}).get("2_6_refresh_rate", {})
    max_hz = refresh_data.get("max_hz", 60)
    min_hz = refresh_data.get("min_hz", 60)
    adaptive = refresh_data.get("adaptive", False)
    effective_refresh = (min_hz + max_hz) / 2 if adaptive else max_hz
    # Score: 10 - 10 * (effective - 30) / (165 - 30)
    refresh_score = 10 - 10 * (effective_refresh - 30) / (165 - 30)
    refresh_score = clamp(refresh_score, 0, 10)

    res_data = data.get("2_display", {}).get("2_2_resolution_density", {})
    width = res_data.get("width_px", 1080)
    height = res_data.get("height_px", 2400)
    pixel_mp = (width * height) / 1_000_000
    # Score: 10 - 10 * (pixel_mp - 1.0) / (8.3 - 1.0)
    res_score = 10 - 10 * (pixel_mp - 1.0) / (8.3 - 1.0)
    res_score = clamp(res_score, 0, 10)

    display_total = 0.35 * panel_score + 0.35 * refresh_score + 0.30 * res_score

    # B.3 Connectivity
    cellular_feats = data.get("7_connectivity_and_sensors", {}).get("7_1_cellular_capabilities", {}).get("features", [])
    # Find worst score (min) because newer = lower score
    cell_scores = [get_best_match(f, CELLULAR_SCORES, default=6) for f in cellular_feats]
    cell_score = min(cell_scores) if cell_scores else 6

    wifi_val = data.get("7_connectivity_and_sensors", {}).get("7_3_wifi_standard", {}).get("value", "")
    wifi_score = get_best_match(wifi_val, WIFI_SCORES, default=6)

    conn_total = 0.7 * cell_score + 0.3 * wifi_score

    # B.4 Thermal
    cooling_val = data.get("3_processing_power_and_performance", {}).get("3_5_thermal_management", {}).get("value", "")
    cooling_score = get_best_match(cooling_val, COOLING_SCORES, default=4)

    thickness = data.get("1_design_and_build_quality", {}).get("1_4_dimensions", {}).get("thickness_mm", 8.0)
    # Score: 10 * (thickness - 6) / (10 - 6)
    thick_score = 10 * (thickness - 6) / (10 - 6)
    thick_score = clamp(thick_score, 0, 10)

    thermal_total = 0.6 * cooling_score + 0.4 * thick_score

    # B.5 Charging
    wired_w = data.get("5_battery_and_charging", {}).get("5_2_wired_charging_speed", {}).get("watts", 25)
    # Score: 10 - 10 * (W - 10) / (150 - 10)
    wired_score = 10 - 10 * (wired_w - 10) / (150 - 10)
    wired_score = clamp(wired_score, 0, 10)

    wireless_w = data.get("5_battery_and_charging", {}).get("5_3_wireless_charging_speed", {}).get("watts", 0)
    # Score: 10 - 10 * (W - 0) / (50 - 0)
    wireless_score = 10 - 10 * (wireless_w - 0) / (50 - 0)
    wireless_score = clamp(wireless_score, 0, 10)

    charging_total = 0.7 * wired_score + 0.3 * wireless_score

    # Total HEI
    hei_total = (0.35 * soc_total + 0.35 * display_total + 
                 0.15 * conn_total + 0.10 * thermal_total + 0.05 * charging_total)

    return {
        "soc_efficiency": {
            "process_node_score": round(process_score, 2),
            "cpu_architecture_score": round(cpu_score, 2),
            "gpu_architecture_score": round(gpu_score, 2),
            "total_soc_score": round(soc_total, 2)
        },
        "display_efficiency": {
            "panel_technology_score": round(panel_score, 2),
            "refresh_efficiency_score": round(refresh_score, 2),
            "resolution_efficiency_score": round(res_score, 2),
            "total_display_score": round(display_total, 2)
        },
        "connectivity_efficiency": {
            "cellular_score": round(cell_score, 2),
            "wifi_score": round(wifi_score, 2),
            "total_connectivity_score": round(conn_total, 2)
        },
        "thermal_efficiency": {
            "cooling_system_score": round(cooling_score, 2),
            "thickness_score": round(thick_score, 2),
            "total_thermal_score": round(thermal_total, 2)
        },
        "charging_stress_efficiency": {
            "wired_charging_score": round(wired_score, 2),
            "wireless_charging_score": round(wireless_score, 2),
            "total_charging_stress_score": round(charging_total, 2)
        },
        "total_hei_score": round(hei_total, 2)
    }

def calc_layer_c(data):
    skin = data.get("6_software_and_longevity", {}).get("skin", "")
    skin_score = get_best_match(skin, OS_SKIN_SCORES, default=6)

    # C.2 System Cleanliness & Control (SCC)
    scc_data = data.get("6_software_and_longevity", {}).get("6_3_system_cleanliness_control", {})
    
    # Extract sub-metrics (defaulting to worst case if missing, or best case for PAL/RDC if empty to avoid div/0 errors in testing)
    pal_count = scc_data.get("pal", {}).get("third_party_apps_count", 10)
    rdc_removable = scc_data.get("rdc", {}).get("removable_count", 0)
    rdc_disableable = scc_data.get("rdc", {}).get("disableable_count", 0)
    sap_status = scc_data.get("sap", {}).get("ads_status", "Persistent ads")
    
    # Calculate SCC
    scc_score = calculate_scc(pal_count, rdc_removable, rdc_disableable, sap_status)

    soi_total = 0.6 * skin_score + 0.4 * scc_score

    return {
        "os_skin_score": round(skin_score, 2),
        "scc_score": round(scc_score, 2),
        "total_soi_score": round(soi_total, 2)
    }

def calc_benchmarks(data):
    # This part assumes we might have manual entry of hours in the file, 
    # or we just hardcode the hours for this specific phone (S24 Ultra) as per example.
    # Since the file already has the hours, we should read them.
    
    benchmarks = data.get("5_battery_and_charging", {}).get("5_1_battery_capacity", {}).get("benchmarks", {})
    
    gsm_hours = benchmarks.get("gsmarena_active_use", {}).get("hours", 0)
    pa_hours = benchmarks.get("phonearena_battery_life", {}).get("hours", 0)
    
    # GSMArena: 10 * (Hours - 7.8) / (23.12 - 7.8)
    gsm_score = 0
    if gsm_hours > 0:
        gsm_score = 10 * (gsm_hours - 7.8) / (23.12 - 7.8)
        gsm_score = clamp(gsm_score, 0, 10)
    
    # PhoneArena: 10 * (Hours - 3.6) / (11.42 - 3.6)
    pa_score = 0
    if pa_hours > 0:
        pa_score = 10 * (pa_hours - 3.6) / (11.42 - 3.6)
        pa_score = clamp(pa_score, 0, 10)
        
    return {
        "gsmarena_active_use": {
            "hours": gsm_hours,
            "normalized_score": round(gsm_score, 2)
        },
        "phonearena_battery_life": {
            "hours": pa_hours,
            "normalized_score": round(pa_score, 2)
        }
    }

def main():
    file_path = 'docs/proposed_data_structure.md'
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract JSON block
    json_match = re.search(r'```json\n(.*?)\n```', content, re.DOTALL)
    if not json_match:
        print("No JSON block found")
        return
    
    json_str = json_match.group(1)
    data = json.loads(json_str)
    
    # --- Calculations ---
    
    layer_a = calc_layer_a(data)
    layer_b = calc_layer_b(data)
    layer_c = calc_layer_c(data)
    
    predicted_score = (0.45 * layer_a["score"] + 
                       0.35 * layer_b["total_hei_score"] + 
                       0.20 * layer_c["total_soi_score"])
    
    benchmarks = calc_benchmarks(data)
    gsm_score = benchmarks["gsmarena_active_use"]["normalized_score"]
    pa_score = benchmarks["phonearena_battery_life"]["normalized_score"]
    
    # Final Score Logic
    final_score = 0
    source = "None"
    
    if gsm_score > 0 and pa_score > 0:
        final_score = (gsm_score + pa_score) / 2
        source = "GSMArena Active Use + PhoneArena Battery Life"
    elif gsm_score > 0:
        final_score = gsm_score
        source = "GSMArena Active Use"
    elif pa_score > 0:
        final_score = pa_score
        source = "PhoneArena Battery Life"
    else:
        # Case 3: Fallback to predicted score
        # NOTE: True interpolation requires database access - use battery_score_full_database.py instead
        final_score = predicted_score
        source = "Predicted Score (No benchmarks available - use battery_score_full_database.py for interpolation)"
    
    booster = final_score / predicted_score if predicted_score > 0 else 1.0
    
    # --- Update Data Structure ---
    
    battery_section = data["5_battery_and_charging"]["5_1_battery_capacity"]
    
    battery_section["scoring_components"] = {
        "layer_a_energy": layer_a,
        "layer_b_hei": layer_b,
        "layer_c_soi": layer_c
    }
    
    battery_section["predicted_score"] = round(predicted_score, 2)
    battery_section["benchmarks"] = benchmarks
    
    battery_section["score_adjustment"] = {
        "booster": round(booster, 3),
        "source": source
    }
    
    battery_section["final_score"] = round(final_score, 2)
    
    # --- Write Back ---
    
    new_json_str = json.dumps(data, indent=2)
    
    # Post-processing to compact short arrays
    # Matches arrays of primitives (strings, numbers, bools, null)
    def compact_arrays(match):
        content = match.group(0)
        if len(content) > 120: return content # Keep very long arrays expanded
        # Collapse whitespace to single space
        compacted = re.sub(r'\s+', ' ', content)
        # Clean up spaces inside brackets: [ "A", "B" ] -> ["A", "B"]
        compacted = compacted.replace('[ ', '[').replace(' ]', ']')
        return compacted

    # Regex to match arrays containing only primitives (no objects/nested arrays)
    # Matches: [ followed by (values separated by commas) followed by ]
    # Value pattern: "string" OR number OR true/false/null
    # We use a simplified check: content inside [] does not contain { or [
    new_json_str = re.sub(r'\[\s*([^\[\]\{\}]*?)\s*\]', compact_arrays, new_json_str, flags=re.DOTALL)

    new_content = content.replace(json_str, new_json_str)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Successfully updated {file_path}")
    print(f"Predicted Score: {predicted_score:.2f}")
    print(f"Final Score: {final_score:.2f}")

if __name__ == "__main__":
    main()
