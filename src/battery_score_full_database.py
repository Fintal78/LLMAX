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

def calc_layer_a(specs):
    """Calculate Layer A: Battery Energy (45%)"""
    battery = specs.get("Battery", {})
    
    # Extract mAh from battery type string (e.g., "Li-Ion 5000 mAh, non-removable")
    mah = 0
    battery_type = battery.get("Type", "")
    if battery_type:
        match = re.search(r'(\d+)\s*mAh', battery_type)
        if match:
            mah = int(match.group(1))
    
    # Default voltage
    voltage = 3.85
    
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
    
    process_score = 10 - 10 * (process_nm - 3) / (20 - 3)
    process_score = clamp(process_score, 0, 10)
    
    cpu_score = get_best_match(cpu_name, CPU_SCORES, default=5)
    gpu_score = get_best_match(gpu_model, GPU_SCORES, default=5)
    
    soc_total = 0.5 * process_score + 0.3 * cpu_score + 0.2 * gpu_score
    
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
    
    # B.4 Thermal - Default values
    cooling_score = 4  # Default passive
    
    body = specs.get("Body", {})
    thickness = 8.0
    dim_str = body.get("Dimensions", "")
    if dim_str:
        thick_match = re.search(r'(\d+\.?\d*)\s*mm.*?\(\d+\.\d+\s*in\)$', dim_str)
        if thick_match:
            thickness = float(thick_match.group(1))
    
    thick_score = 10 * (thickness - 6) / (10 - 6)
    thick_score = clamp(thick_score, 0, 10)
    
    thermal_total = 0.6 * cooling_score + 0.4 * thick_score
    
    # B.5 Charging
    wired_w = 25  # Default
    wireless_w = 0
    
    battery = specs.get("Battery", {})
    charging = battery.get("Charging", "")
    if charging:
        wired_match = re.search(r'(\d+)W', charging)
        if wired_match:
            wired_w = int(wired_match.group(1))
    
    wired_score = 10 - 10 * (wired_w - 10) / (150 - 10)
    wired_score = clamp(wired_score, 0, 10)
    
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

def calc_layer_c(specs):
    """Calculate Layer C: Software & Optimization Index (20%)"""
    
    # Default to moderate skin and bloat
    skin_score = 6
    bloat_score = 6
    
    platform = specs.get("Platform", {})
    os_str = platform.get("OS", "")
    
    if os_str:
        if "iOS" in os_str:
            skin_score = 10
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
                avg_pred_neighbors = sum(
                    n['battery_scores']['predicted_score'] for n in neighbors
                ) / len(neighbors)
                
                # Calculate average final score of neighbors
                avg_final_neighbors = sum(
                    n['battery_scores'].get('final_score', n['battery_scores']['predicted_score']) 
                    for n in neighbors
                ) / len(neighbors)
                
                # Calculate correction ratio
                ratio = predicted_score / avg_pred_neighbors if avg_pred_neighbors > 0 else 1.0
                
                # Apply ratio to neighbor average
                final_score = ratio * avg_final_neighbors
                
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
