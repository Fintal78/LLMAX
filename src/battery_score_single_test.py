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

# Layer B.1.2 CPU Class (See Section 3.1.1 of scoring_rules.md)
CPU_SCORES = {
    "Cortex-X925": 10, "Cortex-X4": 10, "Apple A18": 10, "Apple A17": 10, "Apple A17 Pro": 10,
    "Cortex-X3": 9,
    "Cortex-X2": 8,
    "Cortex-A720": 7, "Cortex-A715": 7,
    "Cortex-A710": 6, "Cortex-A78": 6, "Cortex-A77": 6,
    "Cortex-A76": 5, "Cortex-A75": 5,
    "Cortex-A73": 4,
    "Cortex-A55": 2, "Cortex-A520": 2, "Cortex-A510": 2,
    "Cortex-A53": 0, "Cortex-A7": 0
}

# Layer B.1.3 GPU Class (See Section 3.3.1 of scoring_rules.md)
GPU_SCORES = {
    "Apple GPU": 10, "Immortalis-G720": 10,
    "Adreno 750": 9, "Adreno 740": 9,
    "Adreno 730": 8, "Mali-G715": 8,
    "Mali-G710": 7, "Adreno 660": 7,
    "Adreno 642L": 6, "Mali-G610": 6,
    "Adreno 619": 4, "Mali-G68": 4,
    "Mali-G57": 2, "Adreno 610": 2,
    "Mali-G52": 0
}

# Layer B.2.1 Panel Technology (See Section 2.1 of scoring_rules.md)
PANEL_SCORES = {
    "Tandem OLED": 10,
    "LTPO OLED": 9, "LTPO AMOLED": 9,
    "OLED": 9, "AMOLED": 9, "Super AMOLED": 9, "Dynamic AMOLED": 9, "Dynamic AMOLED 2X": 9, "P-OLED": 9, "LTPS OLED": 9,
    "IPS LCD": 6, "IPS": 6,
    "TFT": 2, "PLS": 2, "TFT LCD": 2, "PLS LCD": 2,
    "LCD": 0, "TN LCD": 0
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

# TDSI - Frame Material (Part A1)
FRAME_MATERIAL_SCORES = {
    "Titanium": 10, "Stainless Steel": 10,
    "Aluminum": 8, "Magnesium": 8,
    "Plastic": 4,
    "Polymer": 0, "Rubber": 0
}

# TDSI - Cooling System (Part B)
COOLING_SCORES = {
    "Active Cooling (Fan)": 10, "Active fan": 10,
    "Large Vapor Chamber": 8, "Vapor chamber": 7, "Vapor Chamber (Standard)": 7,
    "Multi-layer Graphite/Copper": 5, "Graphite": 5, "Copper foil": 5,
    "Single Heat Spreader": 3, "Heat pipe": 3,
    "No Thermal System Disclosed": 0, "None": 0
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

def calc_soc_performance_score(geekbench_multi):
    """
    Calculates Section 3.1 SoC Performance Score (0-10) based on Geekbench 6 Multi-Core.
    Formula: 10 * (log(Score) - log(1500)) / (log(7500) - log(1500))
    """
    import math
    if geekbench_multi <= 0: return 0
    
    gb_min = 1500
    gb_max = 7500
    
    score = 10 * (math.log(geekbench_multi) - math.log(gb_min)) / (math.log(gb_max) - math.log(gb_min))
    return clamp(score, 0, 10)

# --- Layer Calculation Functions ---

def calc_layer_a(data):
    mah = data.get("5_battery_and_charging", {}).get("5_1_battery_endurance", {}).get("mah", 0)
    voltage_raw = data.get("5_battery_and_charging", {}).get("5_1_battery_endurance", {}).get("battery_voltage_v", "Not available")
    battery_type = data.get("5_battery_and_charging", {}).get("5_1_battery_endurance", {}).get("battery_type", "")
    wired_watts = data.get("5_battery_and_charging", {}).get("5_2_wired_charging_speed", {}).get("watts", 0)
    
    # Voltage detection with dual-cell support
    voltage = 3.85  # Default single-cell
    
    # Priority 1: Explicit voltage specified
    if isinstance(voltage_raw, (int, float)):
        voltage = voltage_raw
    # Priority 2: Dual-cell indicators in battery type
    elif isinstance(battery_type, str):
        battery_type_lower = battery_type.lower()
        if "dual-cell" in battery_type_lower or "dual cell" in battery_type_lower or "2s" in battery_type_lower:
            voltage = 7.7  # Dual-cell configuration (2 × 3.85V in series)
    # Priority 3: High-power charging heuristic (≥120W almost always means dual-cell)
    if voltage == 3.85 and wired_watts >= 120:
        voltage = 7.7
    
    wh = (mah * voltage) / 1000
    score = normalize_linear(wh, 8, 25)
    
    return {"wh": round(wh, 2), "score": round(score, 2)}

def calc_layer_b(data):
    # B.1 SoC
    process_nm = data.get("3_processing_power_and_performance", {}).get("3_4_efficiency_node", {}).get("process_nm", 4)
    foundry = data.get("3_processing_power_and_performance", {}).get("3_4_efficiency_node", {}).get("foundry", "Samsung")
    
    # Unified logarithmic formula (see Section 3.4 of scoring_rules.md)
    import math
    base_score = 10 * (math.log(20) - math.log(process_nm)) / (math.log(20) - math.log(3)) - 0.3
    
    # Foundry modifier: TSMC +0.3, Samsung 0.0, SMIC -0.3
    foundry_modifier = 0.0
    if "TSMC" in foundry:
        foundry_modifier = 0.3
    elif "SMIC" in foundry or foundry in ["Other", "Unknown"]:
        foundry_modifier = -0.3
    
    process_score = base_score + foundry_modifier
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

    # B.4 Thermal Efficiency = TDSI (Thermal Dissipation & Stability Index)
    # Reference: Section 3.5 of scoring_rules.md
    
    # Part A: Chassis Thermal Capacity (50% of TDSI)
    # A1: Frame Material (40% of Part A)
    tdsi_data = data.get("3_processing_power_and_performance", {}).get("3_5_thermal_dissipation_stability", {})
    frame_material = tdsi_data.get("frame_material", "")
    frame_score = get_best_match(frame_material, FRAME_MATERIAL_SCORES, default=4)
    
    # A2: Device Thermal Mass / Weight (25% of Part A)
    weight_g = tdsi_data.get("weight_g", data.get("1_design_and_build_quality", {}).get("1_5_weight", {}).get("weight_g", 200))
    # Assuming Weight_Lightest_Phone = 140g, Weight_Heaviest_Phone = 250g
    weight_score = 10 * (weight_g - 140) / (250 - 140)
    weight_score = clamp(weight_score, 0, 10)
    
    # A3: Heat Dissipation Surface Area (20% of Part A)
    height_mm = tdsi_data.get("height_mm", 160)
    width_mm = tdsi_data.get("width_mm", 75)
    surface_area = height_mm * width_mm
    surface_score = 10 * (surface_area - 6000) / (9000 - 6000)
    surface_score = clamp(surface_score, 0, 10)
    
    # A4: Device Thickness (15% of Part A)
    thickness_mm = tdsi_data.get("thickness_mm", data.get("1_design_and_build_quality", {}).get("1_4_dimensions", {}).get("thickness_mm", 8.0))
    thickness_score = 10 * (thickness_mm - 6) / (10 - 6)
    thickness_score = clamp(thickness_score, 0, 10)
    
    # Part A Total
    part_a_total = (0.40 * frame_score) + (0.25 * weight_score) + (0.20 * surface_score) + (0.15 * thickness_score)
    
    # Part B: Internal Cooling System Class (40% of TDSI)
    cooling_system = tdsi_data.get("cooling_system", "")
    cooling_score = get_best_match(cooling_system, COOLING_SCORES, default=4)
    
    # Part C: Thermal Demand Compensation (20% of TDSI - Additive)
    # Get Geekbench 6 Multi-Core Score to calculate Thermal Load
    gb6_score = data.get("3_processing_power_and_performance", {}).get("3_1_soc_performance", {}).get("geekbench_6_multi_score", 3000)
    soc_perf_score = calc_soc_performance_score(gb6_score)
    
    # Bonus Formula: (10 - SoC_Perf) * 0.5
    # Logic: Low performance (2.0) -> Bonus (4.0). High performance (10.0) -> Bonus (0.0).
    part_c_bonus = (10 - soc_perf_score) * 0.5
    part_c_bonus = clamp(part_c_bonus, 0, 5)

    # Final TDSI = Thermal Efficiency for battery scoring
    # Prior Formula: (0.5 * A) + (0.5 * B)
    # New Formula: A/B Average + Bonus
    base_physical = (0.5 * part_a_total) + (0.5 * cooling_score)
    thermal_total = base_physical + part_c_bonus
    thermal_total = clamp(thermal_total, 0, 10)

    # Total HEI
    # Weights: SoC 40%, Display 40%, Connectivity 10%, Thermal 10%
    hei_total = (0.40 * soc_total + 0.40 * display_total + 
                 0.10 * conn_total + 0.10 * thermal_total)

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
            "frame_material_score": round(frame_score, 2),
            "weight_score": round(weight_score, 2),
            "surface_area_score": round(surface_score, 2),
            "thickness_score": round(thickness_score, 2),
            "part_a_chassis_score": round(part_a_total, 2),
            "cooling_system_score": round(cooling_score, 2),
            "thermal_demand_bonus": round(part_c_bonus, 2),
            "tdsi_score": round(thermal_total, 2)
        },
        "total_hei_score": round(hei_total, 2)
    }

def calc_layer_c(data):
    os_ver_str = data.get("6_software_and_longevity", {}).get("os_version", "")
    
    # Default to modern standard (8)
    skin_score = 8
    
    if os_ver_str:
        # Check Android
        android_match = re.search(r'Android\s+(\d+)', os_ver_str, re.IGNORECASE)
        if android_match:
            ver = int(android_match.group(1))
            if ver >= 14: skin_score = 10
            elif ver == 13: skin_score = 9
            elif ver == 12: skin_score = 8
            elif ver >= 10: skin_score = 6
            elif ver >= 8: skin_score = 4
            else: skin_score = 0
            
        # Check iOS
        ios_match = re.search(r'iOS\s+(\d+)', os_ver_str, re.IGNORECASE)
        if ios_match:
            ver = int(ios_match.group(1))
            if ver >= 17: skin_score = 10
            elif ver == 16: skin_score = 9
            elif ver == 15: skin_score = 8
            elif ver >= 13: skin_score = 6
            elif ver >= 11: skin_score = 4
            else: skin_score = 0

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
    
    benchmarks = data.get("5_battery_and_charging", {}).get("5_1_battery_endurance", {}).get("benchmarks", {})
    
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
    
    battery_section = data["5_battery_and_charging"]["5_1_battery_endurance"]
    
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
