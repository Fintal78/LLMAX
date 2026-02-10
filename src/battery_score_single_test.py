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
# Format: "Core Name": (Score, Reference_Frequency_GHz)
CPU_SCORES = {
    "Cortex-X925": (10, 3.60), "Cortex-X4": (10, 3.30), 
    "Apple A18": (10, 3.78), "Apple A17": (10, 3.78), "Apple A17 Pro": (10, 3.78),
    "Cortex-X3": (9, 3.20),
    "Cortex-X2": (8, 3.00),
    "Cortex-A720": (7, 2.80), "Cortex-A715": (7, 2.80),
    "Cortex-A710": (6, 2.50), "Cortex-A78": (6, 2.40), "Cortex-A77": (6, 2.40),
    "Cortex-A76": (5, 2.20), "Cortex-A75": (5, 2.20),
    "Cortex-A73": (4, 2.00),
    "Cortex-A55": (2, 1.80), "Cortex-A520": (2, 2.00), "Cortex-A510": (2, 2.00),
    "Cortex-A53": (0, 1.50), "Cortex-A7": (0, 1.50)
}

# Layer B.1.3 GPU Class (See Section 3.3.1 of scoring_rules.md)
GPU_SCORES = {
    "Apple GPU": (10, 1398), "A18 Pro": (10, 1398), "A17 Pro": (10, 1398),
    "Immortalis-G720": (10, 1300), "Immortalis-G720 MC12": (10, 1300),
    "Adreno 750": (9, 903),
    "Adreno 740": (9, 680), "Immortalis-G715": (9, 981), "Immortalis-G715 MC11": (9, 981),
    "Adreno 730": (8, 900),
    "Mali-G715": (8, 850), "Mali-G715 MC9": (8, 850), "Mali-G715 MC7": (7, 850),
    "Mali-G710": (7, 850), "Mali-G710 MC10": (7, 850), "Adreno 660": (7, 840),
    "Adreno 642L": (6, 490), "Mali-G610": (6, 850), "Mali-G610 MC6": (6, 850),
    "Mali-G610 MC4": (5, 850),
    "Mali-G68": (4, 900), "Mali-G68 MC4": (4, 900),
    "Adreno 619": (4, 825),
    "Mali-G57": (3, 950), "Mali-G57 MC3": (3, 950), "Mali-G57 MC2": (2, 950),
    "Adreno 610": (2, 600),
    "Mali-G52": (1, 850), "Mali-G52 MP2": (1, 850),
    "PowerVR": (0, 680)
}
    
# Layer B.1.3 GPU Efficiency (See Section 3.3.0 Efficiency Score Column)
GPU_EFFICIENCY_SCORES = {
    "A18 Pro": 10, "A17 Pro": 9, "A17": 9,
    "Immortalis-G720": 10, "Adreno 750": 9, "Adreno 740": 9,
    "Immortalis-G715": 9, "Adreno 730": 7, "Mali-G715": 9,
    "Mali-G710": 8, "Adreno 660": 5, "Mali-G715 (Tensor G3)": 6,
    "Mali-G715 MC7": 9, "Adreno 650": 6, "Adreno 642L": 8,
    "Mali-G77": 6, "Mali-G68": 6, "Adreno 640": 5,
    "Adreno 620": 6, "Adreno 619": 6, "Mali-G57": 5,
    "Adreno 618": 5, "Adreno 610": 8, "Mali-G52": 4,
    "PowerVR": 2
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

def get_val(data, path, default=None):
    """Helper to safely extract value from nested dicts with {value: X, ...} wrapper"""
    curr = data
    for key in path:
        if not isinstance(curr, dict):
            return default
        curr = curr.get(key, {})
    
    # Check if we landed on a wrapper or the value itself
    if isinstance(curr, dict) and 'value' in curr:
        return curr['value']
    # If the last key pointed to the value directly
    return curr if curr != {} else default

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
    # Handle wrapped value: if value is a dict, try to extract 'value' or string representation
    if isinstance(value, dict):
        value = value.get("value", value)
    
    if not value or isinstance(value, dict): return default # If still a dict (empty wrapper?), return default
    
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
    # Extract inputs from 5_1_battery_endurance.layer_a_energy
    battery_data = data.get("5_battery_and_charging", {}).get("5_1_battery_endurance", {})
    layer_a_data = battery_data.get("layer_a_energy", {})
    
    wh_raw = layer_a_data.get("wh", {}).get("value", 0)
    
    # mah, voltage, type moved to root of 5_battery_and_charging
    battery_root = data.get("5_battery_and_charging", {})
    mah = battery_root.get("mah", {}).get("value", 0)
    voltage_raw = battery_root.get("battery_voltage_v", {}).get("value", "Not available")
    # battery_type renamed to battery_cell_configuration
    battery_cell_configuration = battery_root.get("battery_cell_configuration", {}).get("value", "")
    
    wired_watts = data.get("5_battery_and_charging", {}).get("5_2_wired_charging_speed", {}).get("watts", {}).get("value", 0)
    
    wh = 0
    voltage = 3.85  # Default single-cell

    # Priority 0: Explicit Wh provided
    if isinstance(wh_raw, (int, float)) and wh_raw > 0:
        wh = wh_raw
        
        # Still try to detect voltage for completeness/logging if possible, but it's not needed for Wh
        if isinstance(voltage_raw, (int, float)):
            voltage = voltage_raw
        elif isinstance(battery_cell_configuration, str):
            config_lower = battery_cell_configuration.lower()
            if "dual-cell" in config_lower or "2s" in config_lower:
                voltage = 7.7
        elif isinstance(wired_watts, (int, float)) and wired_watts >= 120:
             voltage = 7.7

    else:
        # Calculate Wh from mAh * Voltage
        
        # 1. Explicit voltage
        if isinstance(voltage_raw, (int, float)):
            voltage = voltage_raw
        
        # 2. Dual cell detection by config name
        elif isinstance(battery_cell_configuration, str) and ("dual-cell" in battery_cell_configuration.lower() or "2s" in battery_cell_configuration.lower()):
            voltage = 7.7
            
        # 3. High power charging heuristic (fallback)
        elif isinstance(wired_watts, (int, float)) and wired_watts >= 120:
            voltage = 7.7
        
        wh = (mah * voltage) / 1000

    
    score = normalize_linear(wh, 8, 25)
    
    return {"wh": round(wh, 2), "score": round(score, 2)}

def calc_layer_b(data):
    # B.1 SoC
    # Path: 3_processing_power_and_performance... -> 3_4_efficiency_node -> process_nm -> value
    process_nm = get_val(data, ["3_processing_power_and_performance", "3_4_efficiency_node", "process_nm"], 4)
    foundry = get_val(data, ["3_processing_power_and_performance", "3_4_efficiency_node", "foundry"], "Samsung")
    
    # Unified logarithmic formula
    import math
    if not isinstance(process_nm, (int, float)): process_nm = 4
    base_score = 10 * (math.log(20) - math.log(process_nm)) / (math.log(20) - math.log(3)) - 0.3
    
    foundry_modifier = 0.0
    if isinstance(foundry, str):
        if "TSMC" in foundry:
            foundry_modifier = 0.3
        elif "SMIC" in foundry or foundry in ["Other", "Unknown"]:
            foundry_modifier = -0.3
    
    process_score = clamp(base_score + foundry_modifier, 0, 10)

    # CPU
    # CPU: Architecture Efficiency Score (AES)
    # Try to fetch pre-calculated AES from 3.1
    # Try to fetch pre-calculated AES from 5.1
    batt_endurance = data.get("5_battery_and_charging", {}).get("5_1_battery_endurance", {})
    layer_b = batt_endurance.get("layer_b_hardware_efficiency", {})
    b_1_soc = layer_b.get("b_1_soc_efficiency", {})
    breakdown = b_1_soc.get("breakdown", {})
    aes_stored = breakdown.get("cpu_architecture_score_aes")
    
    if isinstance(aes_stored, (int, float)) and aes_stored > 0:
        cpu_score = aes_stored
    else:
        # Fallback: Calculate if not present (Test Script Logic)
        clusters = data.get("3_processing_power_and_performance", {}).get("3_0_cpu_architecture_reference", {}).get("clusters", [])
        total_score = 0
        total_cores = 0
        
        if clusters and len(clusters) > 0:
            facs_list = []
            for cluster in clusters:
                # Handle name extraction
                raw_name = cluster.get("name", {})
                c_name = raw_name.get("value") if isinstance(raw_name, dict) else raw_name
                if not isinstance(c_name, str): c_name = ""
                
                # Handle count extraction
                raw_count = cluster.get("count", {})
                c_count = raw_count.get("value") if isinstance(raw_count, dict) else raw_count
                if not isinstance(c_count, (int, float)): c_count = 0
                
                # Handle frequency extraction
                raw_freq = cluster.get("freq_ghz", {})
                c_freq = raw_freq.get("value") if isinstance(raw_freq, dict) else raw_freq
                if not isinstance(c_freq, (int, float)): c_freq = 0

                # Lookup score & ref freq
                c_data = get_best_match(c_name, CPU_SCORES, default=(5, 2.0))
                if isinstance(c_data, tuple):
                    c_score = c_data[0]
                    ref_freq = c_data[1]
                else:
                    c_score = c_data
                    ref_freq = 2.0 # Default if tuple not found

                # Calculate FSF
                fsf = 1.0
                if c_freq > 0 and ref_freq > 0:
                    fsf = 1 + (c_freq - ref_freq) / ref_freq
                
                # Clamp FSF for safety (0.5x to 1.5x)
                if fsf < 0.5: fsf = 0.5
                if fsf > 1.5: fsf = 1.5

                # Apply FSF to score
                fsf_adjusted_score_per_core = c_score * fsf
                total_cluster_score = fsf_adjusted_score_per_core * c_count
                
                # Update data structure with adjusted score
                if "adjusted_score" in cluster:
                    del cluster["adjusted_score"] # Remove from 3.0 if present from previous run

                # Add to FACS list for 3.1
                facs_entry = {
                    "name": c_name,
                    "value": round(total_cluster_score, 2),
                    "description": "Frequency-Adjusted Core Score (Section 3.1 Method C)"
                }
                facs_list.append(facs_entry)
                
                total_score += total_cluster_score
                total_cores += c_count
                
        cpu_score = (total_score / total_cores) if total_cores > 0 else 5

        # Update 3.1 Scoring Components with FACS
        scoring_components = data.get("3_processing_power_and_performance", {}).get("3_1_cpu_multi_core_performance", {}).get("scoring_components", {})
        
        # Remove old fields if present
        if "cps" in scoring_components: del scoring_components["cps"]
        if "fsf" in scoring_components: del scoring_components["fsf"]
        
        # Add new FACS list
        scoring_components["facs"] = facs_list
        
        # Ensure the structure exists in data
        if "3_processing_power_and_performance" not in data: data["3_processing_power_and_performance"] = {}
        if "3_1_cpu_multi_core_performance" not in data["3_processing_power_and_performance"]: data["3_processing_power_and_performance"]["3_1_cpu_multi_core_performance"] = {}
        if "scoring_components" not in data["3_processing_power_and_performance"]["3_1_cpu_multi_core_performance"]:
             data["3_processing_power_and_performance"]["3_1_cpu_multi_core_performance"]["scoring_components"] = scoring_components # Should point to same obj


    # GPU
    gpu_model = get_val(data, ["3_processing_power_and_performance", "3_3_0_gpu_architecture_reference", "gpu_model"], "")
    # Use GPU_SCORES for Performance/Reference if needed, but for Battery we use Efficiency
    gpu_score = get_best_match(gpu_model, GPU_SCORES, default=5) # Tuple (Score, Freq)
    if isinstance(gpu_score, tuple): gpu_perf_score = gpu_score[0]
    else: gpu_perf_score = gpu_score
    
    gpu_eff_score = get_best_match(gpu_model, GPU_EFFICIENCY_SCORES, default=5)

    soc_total = 0.5 * process_score + 0.3 * cpu_score + 0.2 * gpu_eff_score

    # B.2 Display
    # Path: 2_display -> 2_1_panel_architecture -> value
    panel_tech = get_val(data, ["2_display", "2_1_panel_architecture"], "")
        
    panel_score = get_best_match(panel_tech, PANEL_SCORES, default=5)

    # 2_6_refresh_rate is now flattened to 2_6_refresh_rate_max_hz
    max_hz = get_val(data, ["2_display", "2_6_refresh_rate_max_hz"], 60)
    # min_hz and adaptive moved to root of 2_display
    min_hz = get_val(data, ["2_display", "refresh_rate_min_hz"], 60)
    adaptive = get_val(data, ["2_display", "refresh_rate_adaptive"], False)
    
    if not isinstance(max_hz, (int, float)): max_hz = 60
    if not isinstance(min_hz, (int, float)): min_hz = 60
    
    effective_refresh = (min_hz + max_hz) / 2 if adaptive else max_hz
    refresh_score = clamp(10 - 10 * (effective_refresh - 30) / (165 - 30), 0, 10)

    # Resolution
    # Path: 2_display -> megapixels_mp
    pixel_mp = get_val(data, ["2_display", "megapixels_mp"], 0)
    if not pixel_mp or pixel_mp == 0:
        # Fallback to width/height calculation from root
        w = get_val(data, ["2_display", "resolution_width_px"], 1080)
        h = get_val(data, ["2_display", "resolution_height_px"], 2400)
        pixel_mp = (w * h) / 1_000_000
    
    res_score = clamp(10 - 10 * (pixel_mp - 1.0) / (8.3 - 1.0), 0, 10)

    display_total = 0.35 * panel_score + 0.35 * refresh_score + 0.30 * res_score

    # B.3 Connectivity
    cell_feats_wrapped = get_val(data, ["7_connectivity_and_sensors", "7_1_cellular_capabilities", "features"], [])
    # If it's a list of strings, use it. If list of dicts/wrappers? 
    # Usually 'features' value is [ "5G", ... ]
    cellular_feats = cell_feats_wrapped if isinstance(cell_feats_wrapped, list) else []
    
    cell_scores = [get_best_match(f, CELLULAR_SCORES, default=6) for f in cellular_feats]
    cell_score = min(cell_scores) if cell_scores else 6

    wifi_val = get_val(data, ["7_connectivity_and_sensors", "7_3_wifi_standard"], "")
    wifi_score = get_best_match(wifi_val, WIFI_SCORES, default=6)

    conn_total = 0.7 * cell_score + 0.3 * wifi_score

    # B.4 Thermal
    frame_material = get_val(data, ["3_processing_power_and_performance", "3_5_thermal_dissipation_stability", "frame_material"], "")
    frame_score = get_best_match(frame_material, FRAME_MATERIAL_SCORES, default=4)
    
    weight_g = get_val(data, ["3_processing_power_and_performance", "3_5_thermal_dissipation_stability", "weight_g"], 200)
    if not isinstance(weight_g, (int, float)): weight_g = 200
    weight_score = clamp(10 * (weight_g - 140) / (250 - 140), 0, 10)
    
    h_mm = get_val(data, ["3_processing_power_and_performance", "3_5_thermal_dissipation_stability", "height_mm"], 160)
    w_mm = get_val(data, ["3_processing_power_and_performance", "3_5_thermal_dissipation_stability", "width_mm"], 75)
    if not isinstance(h_mm, (int, float)): h_mm = 160
    if not isinstance(w_mm, (int, float)): w_mm = 75
    surface_area = h_mm * w_mm
    surface_score = clamp(10 * (surface_area - 6000) / (9000 - 6000), 0, 10)
    
    thick_mm = get_val(data, ["3_processing_power_and_performance", "3_5_thermal_dissipation_stability", "thickness_mm"], 8.0)
    if not isinstance(thick_mm, (int, float)): thick_mm = 8.0
    thickness_score = clamp(10 * (thick_mm - 6) / (10 - 6), 0, 10)
    
    part_a_total = (0.40 * frame_score) + (0.25 * weight_score) + (0.20 * surface_score) + (0.15 * thickness_score)
    
    cooling_system = get_val(data, ["3_processing_power_and_performance", "3_5_thermal_dissipation_stability", "cooling_system"], "")
    cooling_score = get_best_match(cooling_system, COOLING_SCORES, default=4)
    
    gb6_score = data.get("3_processing_power_and_performance", {}).get("3_1_cpu_multi_core_performance", {}).get("geekbench_6_multi_score", 3000)
    # GB6 score is currently direct float in schema B (line 394 in file view)
    if isinstance(gb6_score, dict): gb6_score = gb6_score.get("value", 3000) # Safety
    
    soc_perf_score = calc_soc_performance_score(gb6_score)
    part_c_bonus = clamp((10 - soc_perf_score) * 0.5, 0, 5)

    base_physical = (0.5 * part_a_total) + (0.5 * cooling_score)
    thermal_total = clamp(base_physical + part_c_bonus, 0, 10)

    hei_total = (0.40 * soc_total + 0.40 * display_total + 
                 0.10 * conn_total + 0.10 * thermal_total)

    return {
        "soc_efficiency": {
            "process_node_score": round(process_score, 2),
            "cpu_architecture_score": round(cpu_score, 2),
            "gpu_efficiency_score": round(gpu_eff_score, 2),
            "gpu_performance_score": round(gpu_perf_score, 2),
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
    os_ver_str = get_val(data, ["6_software_and_longevity", "os_version"], "")
    
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
    # Prioritize pre-calculated score if valid
    scc_final = data.get("6_software_and_longevity", {}).get("6_3_system_cleanliness_control", {}).get("final_score")
    
    if scc_final is None:
        # Calculate from components if available
        scc_data = data.get("6_software_and_longevity", {}).get("6_3_system_cleanliness_control", {})
        pal_count = get_val(scc_data, ["pal", "third_party_apps_count"], 10)
        rdc_removable = get_val(scc_data, ["rdc", "removable_count"], 0)
        rdc_disableable = get_val(scc_data, ["rdc", "disableable_count"], 0)
        sap_status = get_val(scc_data, ["sap", "ads_status"], "Persistent ads")
        scc_score = calculate_scc(pal_count, rdc_removable, rdc_disableable, sap_status)
    else:
        scc_score = scc_final

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
    
    gsm_data = benchmarks.get("gsmarena_active_use", {})
    gsm_hours = gsm_data.get("hours", 0)
    
    pa_data = benchmarks.get("phonearena_battery_life", {})
    pa_hours = pa_data.get("hours", 0)
    
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
    
    # Update computed scores in their respective layers
    if "layer_a_energy" not in battery_section: battery_section["layer_a_energy"] = {}
    battery_section["layer_a_energy"]["score"] = layer_a["score"]
    
    if "layer_b_hardware_efficiency" not in battery_section: battery_section["layer_b_hardware_efficiency"] = {}
    
    b_struct = battery_section["layer_b_hardware_efficiency"]
    
    # B.1 SoC
    if "b_1_soc_efficiency" not in b_struct: b_struct["b_1_soc_efficiency"] = {}
    b_struct["b_1_soc_efficiency"]["score"] = layer_b["soc_efficiency"]["total_soc_score"]
    b_struct["b_1_soc_efficiency"]["breakdown"] = {
        "process_node_score": layer_b["soc_efficiency"]["process_node_score"],
        "gpu_efficiency_score": layer_b["soc_efficiency"]["gpu_efficiency_score"],
        "gpu_performance_score": layer_b["soc_efficiency"]["gpu_performance_score"],
        "cpu_architecture_score_aes": layer_b["soc_efficiency"]["cpu_architecture_score"]
    }
    
    # B.2 Display
    if "b_2_display_efficiency" not in b_struct: b_struct["b_2_display_efficiency"] = {}
    b_struct["b_2_display_efficiency"]["score"] = layer_b["display_efficiency"]["total_display_score"]
    b_struct["b_2_display_efficiency"]["breakdown"] = {
        "panel_technology_score": layer_b["display_efficiency"]["panel_technology_score"],
        "refresh_efficiency_score": layer_b["display_efficiency"]["refresh_efficiency_score"],
        "resolution_efficiency_score": layer_b["display_efficiency"]["resolution_efficiency_score"]
    }

    # B.3 Connectivity
    if "b_3_connectivity_efficiency" not in b_struct: b_struct["b_3_connectivity_efficiency"] = {}
    b_struct["b_3_connectivity_efficiency"]["score"] = layer_b["connectivity_efficiency"]["total_connectivity_score"]
    b_struct["b_3_connectivity_efficiency"]["breakdown"] = {
        "cellular_score": layer_b["connectivity_efficiency"]["cellular_score"],
        "wifi_score": layer_b["connectivity_efficiency"]["wifi_score"]
    }
    
    # B.4 Thermal
    if "b_4_thermal_efficiency" not in b_struct: b_struct["b_4_thermal_efficiency"] = {}
    b_struct["b_4_thermal_efficiency"]["score"] = layer_b["thermal_efficiency"]["tdsi_score"]
    # No breakdown for B.4 as per user request (redundant with 3.5)
    
    b_struct["total_hei_score"] = layer_b["total_hei_score"]
    
    # Layer C
    if "layer_c_software_optimization" not in battery_section: battery_section["layer_c_software_optimization"] = {}
    battery_section["layer_c_software_optimization"]["breakdown"] = {
        "c_1_os_generation": layer_c["os_skin_score"],
        "c_2_bloatware": layer_c["scc_score"]
    }
    battery_section["layer_c_software_optimization"]["total_soi_score"] = layer_c["total_soi_score"]
    
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
