"""
Battery Score Calculator - Full Database Mode

DESCRIPTION:
This script processes the ENTIRE phone database and calculates battery scores
for all phones using the complete 3-case scoring methodology defined in
docs/battery_scoring_model.md.

SCORING METHODOLOGY:
- Case 1: Phones with both benchmarks → Use benchmark average
- Case 2: Phones with one benchmark → Use that benchmark  
- Case 3: Phones with no benchmarks → Interpolate from 3 nearest neighbors

KEY FEATURES:
- Processes all phones in database
- Implements nearest neighbor interpolation (Case 3)
- Updates phones_db.json with complete battery_scores object
- Two-phase approach: predicted scores first, then final scores

WHEN TO USE:
✓ Initial database setup (first-time scoring)
✓ After adding new phones (Precise Method - recommended for accuracy)
✓ Periodic re-scoring to ensure maximum accuracy
✓ When neighbor constellation has changed significantly
✓ When adding 5+ phones at once

USAGE:
    python battery_score_full_database.py

RUNTIME: ~5-10 seconds for 60 phones

OUTPUT: Updates data/phones_db.json with battery_scores for all phones

SEE ALSO:
- battery_score_new_phone.py - Fast method for scoring single new phone
- battery_score_single_test.py - Test scoring on single phone from markdown
- docs/BATTERY_SCORING_PROCESS.md - Complete lifecycle documentation
"""

import json
import re
import os

# --- Constants & Tables ---

# Layer B.1.1 Process Node (Continuous)
PROCESS_NODE_MIN = 3
PROCESS_NODE_MAX = 20

# Layer B.1.2 CPU Class (See Section 3.1 of scoring_rules.md)
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
    "Apple GPU": 10, "Immortalis-G720": 10,
    "Adreno 750": 9, "Adreno 740": 9,
    "Adreno 730": 8, "Mali-G715": 8,
    "Mali-G710": 7, "Adreno 660": 7,
    "Adreno 642L": 6, "Mali-G610": 6,
    "Adreno 619": 4, "Mali-G68": 4,
    "Mali-G57": 2, "Adreno 610": 2,
    "Mali-G52": 0
}

# Layer B.2.1 Panel Technology
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

# --- Layer Calculation Functions ---

def calc_layer_a(specs):
    """Calculate Layer A: Battery Energy (45%)"""
    battery = specs.get("Battery", {})
    
    # Priority 0: Explicit Wh provided in specs (if available in future structure)
    # Using 'Energy_Wh' key as purely hypothetical, or checking for it in Type string
    wh = 0
    
    # Extract Wh directly from battery type string if possible (e.g., "19.25 Wh")
    battery_type = battery.get("Type", "")
    if battery_type:
        match_wh = re.search(r'(\d+(?:\.\d+)?)\s*Wh', battery_type, re.IGNORECASE)
        if match_wh:
            wh = float(match_wh.group(1))

    # If Wh found, verify voltage for consistency but skip calculation
    if wh > 0:
        pass # wh is already set
    else:
        # Fallback: Calculate from mAh and Voltage
        # Extract mAh from battery type string (e.g., "Li-Ion 5000 mAh, non-removable")
        mah = 0
        if battery_type:
            match = re.search(r'(\d+)\s*mAh', battery_type)
            if match:
                mah = int(match.group(1))
        
        # Voltage detection with dual-cell support
        voltage = 3.85  # Default single-cell
        
        # Priority 1: Check for dual-cell indicators in battery type string
        if battery_type:
            battery_type_lower = battery_type.lower()
            if "dual-cell" in battery_type_lower or "dual cell" in battery_type_lower or "2s" in battery_type_lower:
                voltage = 7.7  # Dual-cell configuration (2 × 3.85V in series)
        
        # Priority 2: High-power charging heuristic (≥120W almost always means dual-cell)
        if voltage == 3.85:  # Only apply if not already detected as dual-cell
            charging = battery.get("Charging", "")
            if charging:
                wired_match = re.search(r'(\d+)W', charging)
                if wired_match:
                    wired_w = int(wired_match.group(1))
                    if wired_w >= 120:
                        voltage = 7.7
        
        wh = (mah * voltage) / 1000
        
    score = normalize_linear(wh, 8, 25)
    
    return {"wh": round(wh, 2), "score": round(score, 2)}

def calc_layer_b(specs):
    """Calculate Layer B: Hardware Efficiency Index (35%)"""
    
    # B.1 SoC - Default values for missing data
    process_nm = 4  # Default modern process
    cpu_name = ""
    gpu_model = ""
    
    # Try to extract from Platform
    platform = specs.get("Platform", {})
    chipset = platform.get("Chipset", "")
    
    # Extract process node from chipset (e.g., "Qualcomm Snapdragon 8 Gen 3 (4 nm)")
    if chipset:
        nm_match = re.search(r'\((\d+)\s*nm\)', chipset)
        if nm_match:
            process_nm = int(nm_match.group(1))
    
    # Extract CPU name
    cpu_str = platform.get("CPU", "")
    if cpu_str:
        # Look for Cortex or Apple patterns
        if "Cortex-X4" in cpu_str:
            cpu_name = "Cortex-X4"
        elif "Cortex-X3" in cpu_str:
            cpu_name = "Cortex-X3"
        elif "Cortex-X2" in cpu_str:
            cpu_name = "Cortex-X2"
        elif "Cortex-A720" in cpu_str:
            cpu_name = "Cortex-A720"
        elif "Cortex-A710" in cpu_str:
            cpu_name = "Cortex-A710"
        elif "Cortex-A78" in cpu_str:
            cpu_name = "Cortex-A78"
        elif "Apple" in cpu_str or "A17" in cpu_str or "A18" in cpu_str:
            cpu_name = "Apple A17"
    
    # Extract GPU
    gpu_str = platform.get("GPU", "")
    if gpu_str:
        if "Adreno 750" in gpu_str:
            gpu_model = "Adreno 750"
        elif "Adreno 740" in gpu_str:
            gpu_model = "Adreno 740"
        elif "Adreno 730" in gpu_str:
            gpu_model = "Adreno 730"
        elif "Apple" in gpu_str:
            gpu_model = "Apple GPU"
    
    # Extract foundry from chipset string (e.g., "Snapdragon 8 Gen 3 (4 nm, TSMC)")
    foundry = "Samsung"  # Default
    if chipset:
        if "TSMC" in chipset:
            foundry = "TSMC"
        elif "SMIC" in chipset:
            foundry = "SMIC"
    
    # Unified logarithmic formula (see Section 3.4 of scoring_rules.md)
    import math
    base_score = 10 * (math.log(20) - math.log(process_nm)) / (math.log(20) - math.log(3)) - 0.3
    
    # Foundry modifier: TSMC +0.3, Samsung 0.0, SMIC -0.3
    foundry_modifier = 0.0
    if foundry == "TSMC":
        foundry_modifier = 0.3
    elif foundry == "SMIC":
        foundry_modifier = -0.3
    
    process_score = base_score + foundry_modifier
    process_score = clamp(process_score, 0, 10)
    
    # refined CPU scoring with FSF
    cpu_score_final = 0
    
    # Try to parse clusters from CPU string for detailed FSF calculation
    # Format typically: "Octa-core (1x3.3 GHz Cortex-X4 & 3x3.2 GHz Cortex-A720 & 2x3.0 GHz Cortex-A720 & 2x2.3 GHz Cortex-A520)"
    if cpu_str and "x" in cpu_str and "GHz" in cpu_str:
        total_cluster_score = 0
        total_cores = 0
        
        # Split by '&' or ',' to get clusters
        cluster_strs = re.split(r'[&,]', cpu_str)
        valid_clusters = False
        
        for c_str in cluster_strs:
            # Parse "1x3.3 GHz Cortex-X4" or "4x2.8 GHz Kryo 385"
            # Regex: (\d+)x([\d.]+) GHz (.*)
            match = re.search(r'(\d+)x([\d.]+)\s*GHz\s+(.*)', c_str.strip())
            if match:
                valid_clusters = True
                count = int(match.group(1))
                freq = float(match.group(2))
                name_part = match.group(3).strip()
                
                # Lookup score & ref freq
                c_data = get_best_match(name_part, CPU_SCORES, default=(5, 2.0))
                if isinstance(c_data, tuple):
                    score = c_data[0]
                    ref = c_data[1]
                else:
                    score = c_data
                    ref = 2.0
                
                # Calc FSF
                fsf = 1.0
                if freq > 0 and ref > 0:
                    fsf = 1 + (freq - ref) / ref
                
                fsf = clamp(fsf, 0.5, 1.5)
                
                total_cluster_score += (score * count * fsf)
                total_cores += count
        
        if valid_clusters and total_cores > 0:
            cpu_score_final = total_cluster_score / total_cores
            
    # Fallback if parsing failed or simple format
    if cpu_score_final == 0:
        cpu_data = get_best_match(cpu_name, CPU_SCORES, default=5)
        if isinstance(cpu_data, tuple):
            cpu_score_final = cpu_data[0]
        else:
            cpu_score_final = cpu_data
            
    cpu_score = cpu_score_final
    # GPU Score Calculation
    # Reference: scoring_rules.md Section 3.3
    import math
    
    # Method A: Benchmark (Primary) - Dual Benchmark Support
    tdm_score_raw = specs.get("3DMark_WLE", None)
    gfx_score_raw = specs.get("GFXBench_Manhattan31_Offscreen", None)
    
    tdm_score = None
    gfx_score = None
    
    # Benchmark 1: 3DMark Wild Life Extreme
    if tdm_score_raw and tdm_score_raw > 0:
        tdm_score = 10 * (math.log(tdm_score_raw) - math.log(500)) / (math.log(5000) - math.log(500))
        tdm_score = clamp(tdm_score, 0, 10)
    
    # Benchmark 2: GFXBench Manhattan 3.1 Offscreen
    if gfx_score_raw and gfx_score_raw > 0:
        gfx_score = 10 * (math.log(gfx_score_raw) - math.log(15)) / (math.log(150) - math.log(15))
        gfx_score = clamp(gfx_score, 0, 10)
    
    # Scoring Logic
    gpu_confidence = "Unknown"
    
    # Case 1: Both benchmarks available
    if tdm_score is not None and gfx_score is not None:
        gpu_score = (tdm_score + gfx_score) / 2
        diff = abs(tdm_score - gfx_score)
        if diff <= 1.0:
            gpu_confidence = "High"
        elif diff <= 2.5:
            gpu_confidence = "Medium"
        else:
            gpu_confidence = "Low"
    
    # Case 2: One benchmark available
    elif tdm_score is not None:
        gpu_score = tdm_score
        gpu_confidence = "Unknown"
    elif gfx_score is not None:
        gpu_score = gfx_score
        gpu_confidence = "Unknown"
    
    # Case 3: No benchmarks → Use Method C (Predicted)
    else:
        # GPU_DATA maps to (Arch_Score_0_10, Ref_Freq_MHz)
        GPU_DATA = {
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
    
        gpu_match_data = get_best_match(gpu_model, GPU_DATA, default=(5, 800))
        if isinstance(gpu_match_data, (int, float)):
            gas = float(gpu_match_data)
            ref_freq = 800.0
        else:
            gas = float(gpu_match_data[0])
            ref_freq = float(gpu_match_data[1])
    
        # Step 2: FSF (Frequency Scaling Factor)
        gpu_freq = specs.get("GPU_Freq", 0)
        if gpu_freq and gpu_freq > 0:
            fsf = 1 + (gpu_freq - ref_freq) / ref_freq
        else:
            fsf = 1.0  # Use reference if unknown
        fsf = clamp(fsf, 0.5, 2.0)
        
        # Step 3: AFM (API & Feature Modifier)
        gpu_features = specs.get("GPU_Features", "")
        
        # Part A: API Score (0-10)
        api_score = 5.0  # Default OpenGL ES 3.2
        if "Vulkan 1.3" in gpu_features:
            api_score = 10.0
        elif "Vulkan 1.2" in gpu_features:
            api_score = 8.0
        elif "Vulkan 1.1" in gpu_features:
            api_score = 6.0
        elif "OpenGL ES 3.2" in gpu_features:
            api_score = 5.0
        elif "OpenGL ES 3.1" in gpu_features:
            api_score = 3.0
        elif "OpenGL ES 3.0" in gpu_features:
            api_score = 2.0
        
        # Part B: RT Score (0-10)
        rt_score = 0.0
        if "Ray Tracing" in gpu_features or "RT" in gpu_model:
            rt_score = 10.0
        
        # AFM Formula: 0.7 + (0.2 * API/10) + (0.1 * RT/10)
        afm = 0.7 + (0.2 * api_score / 10) + (0.1 * rt_score / 10)
        
        # Step 4: Calculate Final Score
        # RC (Raw Capability) = GAS * FSF * AFM
        rc = gas * fsf * afm
        
        # Logarithmic Normalization: 10 * (log(RC) - log(2)) / (log(20) - log(2))
        if rc < 2: rc = 2
        gpu_score = 10 * (math.log(rc) - math.log(2)) / (math.log(20) - math.log(2))
        gpu_score = clamp(gpu_score, 0, 10)
        gpu_confidence = "Predicted"
    
    # GPU Efficiency Score (New for Battery Model)
    # Reference: Section 3.3.0 Efficiency Score Column
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
    
    gpu_eff_score = get_best_match(gpu_model, GPU_EFFICIENCY_SCORES, default=5)
    
    # Use Efficiency Score for SoC Calculation (not Performance Score)
    soc_total = 0.5 * process_score + 0.3 * cpu_score + 0.2 * gpu_eff_score
    
    # B.2 Display
    display = specs.get("Display", {})
    panel_tech = display.get("Type", "")
    panel_score = get_best_match(panel_tech, PANEL_SCORES, default=5)
    
    # Extract refresh rate - default to 60Hz
    max_hz = 60
    min_hz = 60
    adaptive = False
    
    if "120Hz" in panel_tech or "120 Hz" in panel_tech:
        max_hz = 120
        if "LTPO" in panel_tech:
            min_hz = 1
            adaptive = True
    elif "90Hz" in panel_tech or "90 Hz" in panel_tech:
        max_hz = 90
    
    effective_refresh = (min_hz + max_hz) / 2 if adaptive else max_hz
    refresh_score = 10 - 10 * (effective_refresh - 30) / (165 - 30)
    refresh_score = clamp(refresh_score, 0, 10)
    
    # Extract resolution
    width = 1080
    height = 2400
    res_str = display.get("Resolution", "")
    if res_str:
        res_match = re.search(r'(\d+)\s*x\s*(\d+)', res_str)
        if res_match:
            width = int(res_match.group(1))
            height = int(res_match.group(2))
    
    pixel_mp = (width * height) / 1_000_000
    res_score = 10 - 10 * (pixel_mp - 1.0) / (8.3 - 1.0)
    res_score = clamp(res_score, 0, 10)
    
    display_total = 0.35 * panel_score + 0.35 * refresh_score + 0.30 * res_score
    
    # B.3 Connectivity - Default to mid-range
    cell_score = 6  # Default 4G
    wifi_score = 6  # Default Wi-Fi 6
    
    comms = specs.get("Comms", {})
    wlan = comms.get("WLAN", "")
    if "Wi-Fi 7" in wlan or "802.11be" in wlan:
        wifi_score = 1
    elif "Wi-Fi 6E" in wlan:
        wifi_score = 4
    elif "Wi-Fi 6" in wlan or "802.11ax" in wlan:
        wifi_score = 6
    elif "Wi-Fi 5" in wlan or "802.11ac" in wlan:
        wifi_score = 8
    
    network = specs.get("Network", {})
    tech = network.get("Technology", "")
    if "5G" in tech:
        cell_score = 4
    elif "LTE" in tech or "4G" in tech:
        cell_score = 6
    elif "3G" in tech:
        cell_score = 8
    
    conn_total = 0.7 * cell_score + 0.3 * wifi_score
    
    # B.4 Thermal Efficiency = TDSI (Thermal Dissipation & Stability Index)
    # Reference: Section 3.5 of scoring_rules.md
    
    # Part A: Chassis Thermal Capacity (50% of TDSI)
    # A1: Frame Material (40% of Part A)
    body = specs.get("Body", {})
    build = body.get("Build", "")
    frame_score = get_best_match(build, FRAME_MATERIAL_SCORES, default=4)
    
    # A2: Device Thermal Mass / Weight (25% of Part A)
    weight_g = 200  # Default
    weight_str = body.get("Weight", "")
    if weight_str:
        weight_match = re.search(r'(\d+)\s*g', weight_str)
        if weight_match:
            weight_g = int(weight_match.group(1))
    # Assuming Weight_Lightest_Phone = 140g, Weight_Heaviest_Phone = 250g
    weight_score = 10 * (weight_g - 140) / (250 - 140)
    weight_score = clamp(weight_score, 0, 10)
    
    # A3: Heat Dissipation Surface Area (20% of Part A)
    height_mm = 160
    width_mm = 75
    dim_str = body.get("Dimensions", "")
    if dim_str:
        # Parse dimensions like "162.3 x 79 x 8.6 mm (6.39 x 3.11 x 0.34 in)"
        dim_match = re.search(r'([\d.]+)\s*x\s*([\d.]+)\s*x\s*([\d.]+)\s*mm', dim_str)
        if dim_match:
            height_mm = float(dim_match.group(1))
            width_mm = float(dim_match.group(2))
    surface_area = height_mm * width_mm
    surface_score = 10 * (surface_area - 6000) / (9000 - 6000)
    surface_score = clamp(surface_score, 0, 10)
    
    # A4: Device Thickness (15% of Part A)
    thickness = 8.0  # Default
    if dim_str:
        thick_match = re.search(r'x\s*([\d.]+)\s*mm.*?\(\d+\.\d+\s*in\)$', dim_str)
        if thick_match:
            thickness = float(thick_match.group(1))
    thickness_score = 10 * (thickness - 6) / (10 - 6)
    thickness_score = clamp(thickness_score, 0, 10)
    
    # Part A Total
    part_a_total = (0.40 * frame_score) + (0.25 * weight_score) + (0.20 * surface_score) + (0.15 * thickness_score)
    
    # Part B: Internal Cooling System Class (40% of TDSI)
    # Note: Cooling system data not typically in GSMArena specs, default to passive
    cooling_score = 4  # Default passive
    
    # Part C: Thermal Demand Compensation (20% of TDSI - Additive)
    # In full database mode, we may not have Geekbench scores for all phones.
    # We use the CPU Architecture Score (cpu_score) as a proxy for Performance/Thermal Load.
    # Logic: High Architecture Score (10) = High Load -> Bonus 0.
    #        Low Architecture Score (0) = Low Load -> Bonus 5.
    soc_perf_proxy = cpu_score
    part_c_bonus = (10 - soc_perf_proxy) * 0.5
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
            "gpu_efficiency_score": round(gpu_eff_score, 2),
            "gpu_performance_score": round(gpu_score, 2),
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

def calc_layer_c(specs):
    """Calculate Layer C: Software & Optimization Index (20%)"""
    
    # Default to modern standard (8) if unknown
    skin_score = 8
    
    platform = specs.get("Platform", {})
    os_str = platform.get("OS", "")
    
    if os_str:
        # Check Android
        android_match = re.search(r'Android\s+(\d+)', os_str, re.IGNORECASE)
        if android_match:
            ver = int(android_match.group(1))
            if ver >= 14: skin_score = 10
            elif ver == 13: skin_score = 9
            elif ver == 12: skin_score = 8
            elif ver >= 10: skin_score = 6
            elif ver >= 8: skin_score = 4
            else: skin_score = 0
            
        # Check iOS
        ios_match = re.search(r'iOS\s+(\d+)', os_str, re.IGNORECASE)
        if ios_match:
            ver = int(ios_match.group(1))
            if ver >= 17: skin_score = 10
            elif ver == 16: skin_score = 9
            elif ver == 15: skin_score = 8
            elif ver >= 13: skin_score = 6
            elif ver >= 11: skin_score = 4
            else: skin_score = 0
    # C.2 System Cleanliness & Control (SCC)
    # Default values (worst case)
    pal_count = 10
    rdc_removable = 0
    rdc_disableable = 0
    sap_status = "Persistent ads"
    
    # Try to extract from specs if available (structure might vary)
    # For now, we'll assume defaults or simple mapping if needed
    
    # Calculate SCC
    scc_score = calculate_scc(pal_count, rdc_removable, rdc_disableable, sap_status)
    
    soi_total = 0.6 * skin_score + 0.4 * scc_score
    
    return {
        "os_skin_score": round(skin_score, 2),
        "scc_score": round(scc_score, 2),
        "total_soi_score": round(soi_total, 2)
    }

def calc_benchmarks(phone):
    """Extract and normalize benchmark scores if they exist"""
    # This will be populated from actual benchmark data if available
    # For now, return empty scores
    return {
        "gsmarena_active_use": {
            "hours": 0,
            "normalized_score": 0
        },
        "phonearena_battery_life": {
            "hours": 0,
            "normalized_score": 0
        }
    }

def find_nearest_neighbors(target_predicted_score, all_phones, count=3):
    """
    Find the nearest neighbor phones that have both benchmarks.
    
    Args:
        target_predicted_score: Predicted score of the target phone
        all_phones: List of all phone objects with battery_scores calculated
        count: Number of neighbors to find (default 3)
    
    Returns:
        List of neighbor phones, or None if insufficient neighbors found
    """
    # Filter phones that have both benchmarks
    benchmarked_phones = []
    for phone in all_phones:
        battery_scores = phone.get('battery_scores', {})
        benchmarks = battery_scores.get('benchmarks', {})
        gsm_score = benchmarks.get('gsmarena_active_use', {}).get('normalized_score', 0)
        pa_score = benchmarks.get('phonearena_battery_life', {}).get('normalized_score', 0)
        
        if gsm_score > 0 and pa_score > 0:
            benchmarked_phones.append(phone)
    
    if len(benchmarked_phones) < count:
        return None
    
    # Sort by distance to target predicted score
    benchmarked_phones.sort(
        key=lambda p: abs(p.get('battery_scores', {}).get('predicted_score', 0) - target_predicted_score)
    )
    
    # Return top N nearest neighbors
    return benchmarked_phones[:count]

def process_database(db_path):
    """
    Process entire database and calculate battery scores for all phones.
    
    Args:
        db_path: Path to phones_db.json
    """
    print(f"Loading database from {db_path}...")
    
    # Load database
    with open(db_path, 'r', encoding='utf-8') as f:
        db_data = json.load(f)
    
    phones = db_data.get('phones', [])
    print(f"Found {len(phones)} phones in database")
    
    # Phase 1: Calculate predicted scores for all phones
    print("\nPhase 1: Calculating predicted scores...")
    for i, phone in enumerate(phones):
        specs = phone.get('specs', {})
        
        layer_a = calc_layer_a(specs)
        layer_b = calc_layer_b(specs)
        layer_c = calc_layer_c(specs)
        
        predicted_score = (0.45 * layer_a["score"] + 
                          0.35 * layer_b["total_hei_score"] + 
                          0.20 * layer_c["total_soi_score"])
        
        benchmarks = calc_benchmarks(phone)
        
        # Inject cpu_architecture_score_aes into SoC Efficiency structure (consolidated)
        if 'soc_efficiency' in layer_b:
            layer_b['soc_efficiency']['cpu_architecture_score_aes'] = layer_b['soc_efficiency'].get('cpu_architecture_score', 0)

        # Store results in phone object
        phone['battery_scores'] = {
            'layer_a_energy': layer_a,
            'layer_b_hei': layer_b,
            'layer_c_soi': layer_c,
            'predicted_score': round(predicted_score, 2),
            'benchmarks': benchmarks
        }
        
        if (i + 1) % 50 == 0:
            print(f"  Processed {i + 1}/{len(phones)} phones...")
    
    print(f"  Completed predicted scores for all {len(phones)} phones")
    
    # Phase 2: Calculate final scores using the 3-case logic
    print("\nPhase 2: Calculating final scores...")
    
    stats = {"case1": 0, "case2": 0, "case3": 0, "case3_fallback": 0}
    
    for i, phone in enumerate(phones):
        battery_scores = phone['battery_scores']
        predicted_score = battery_scores['predicted_score']
        benchmarks = battery_scores['benchmarks']
        
        gsm_score = benchmarks['gsmarena_active_use']['normalized_score']
        pa_score = benchmarks['phonearena_battery_life']['normalized_score']
        
        final_score = 0
        source = "None"
        
        # Case 1: Both benchmarks available
        if gsm_score > 0 and pa_score > 0:
            final_score = (gsm_score + pa_score) / 2
            source = "GSMArena Active Use + PhoneArena Battery Life"
            stats["case1"] += 1
        
        # Case 2: Only one benchmark available
        elif gsm_score > 0:
            final_score = gsm_score
            source = "GSMArena Active Use"
            stats["case2"] += 1
        elif pa_score > 0:
            final_score = pa_score
            source = "PhoneArena Battery Life"
            stats["case2"] += 1
        
        # Case 3: No benchmarks - Use interpolation
        else:
            neighbors = find_nearest_neighbors(predicted_score, phones)
            
            if neighbors and len(neighbors) >= 3:
                # Calculate average predicted score of neighbors
                avg_predicted_neighbors = sum(
                    n['battery_scores']['predicted_score'] for n in neighbors
                ) / len(neighbors)
                
                # Calculate average final score of neighbors
                avg_benchmark_neighbors = sum(
                    n['battery_scores'].get('final_score', n['battery_scores']['predicted_score']) 
                    for n in neighbors
                ) / len(neighbors)
                
                # Calculate correction ratio
                ratio = predicted_score / avg_predicted_neighbors if avg_predicted_neighbors > 0 else 1.0
                
                # Apply ratio to neighbor average
                final_score = ratio * avg_benchmark_neighbors
                
                neighbor_names = [f"Neighbor{i+1}: {n.get('model_name', 'Unknown')[:20]}" for i, n in enumerate(neighbors)]
                source = f"Interpolated from neighbors (Ratio: {ratio:.3f}): {', '.join(neighbor_names)}"
                stats["case3"] += 1
            else:
                # Fallback if not enough neighbors
                final_score = predicted_score
                source = "Predicted Score (Insufficient benchmark data for interpolation)"
                stats["case3_fallback"] += 1
        
        # Calculate booster for reference
        booster = final_score / predicted_score if predicted_score > 0 else 1.0
        
        # Update battery scores
        battery_scores['final_score'] = round(final_score, 2)
        battery_scores['score_source'] = source
        battery_scores['booster'] = round(booster, 3)
        
        if (i + 1) % 50 == 0:
            print(f"  Processed {i + 1}/{len(phones)} phones...")
    
    print(f"  Completed final scores for all {len(phones)} phones")
    print(f"\nScoring Statistics:")
    print(f"  Case 1 (Both benchmarks): {stats['case1']} phones")
    print(f"  Case 2 (One benchmark): {stats['case2']} phones")
    print(f"  Case 3 (Interpolated): {stats['case3']} phones")
    print(f"  Case 3 (Fallback to predicted): {stats['case3_fallback']} phones")
    
    # Save updated database
    print(f"\nSaving updated database to {db_path}...")
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db_data, f, indent=2)
    
    print("[SUCCESS] Database successfully updated with battery scores!")
    
    return db_data

def main():
    """Main entry point"""
    # Determine database path relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, '..', 'data', 'phones_db.json')
    db_path = os.path.normpath(db_path)
    
    if not os.path.exists(db_path):
        print(f"[ERROR] Database not found at {db_path}")
        return
    
    process_database(db_path)

if __name__ == "__main__":
    main()
