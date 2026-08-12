"""
Section 8.2 Method C Parameter Calibration & Optimization Study
---------------------------------------------------------------
Data Integrity & Hardware Verification Protocol:
1. Strict 4-Tier Evidence Hierarchy for Maximum Input Power (P_peak):
   - Tier 1: Measured DC/AC input power from laboratory meters (ChargerLAB / Notebookcheck).
   - Tier 2: Manufacturer-published official accepted phone input wattage.
   - Tier 3: Documented charging mode capabilities.
   - Tier 4: Inferred from bundled wall charger rating (strictly avoided if phone input differs).

2. Cell Architecture Verification Protocol (1S vs 2S):
   - Cell architecture is verified via teardowns and official hardware specs.
   - Dual-cell series (2S) battery packs operating at 7.70V nominal reduce per-cell electrical
     current and internal resistive heating (I^2 * R) by 75%, pushing thermal onset boundary C0_dual to 2.66 h^-1.
   - Motorola Edge 50 Pro (125W), OnePlus 12R (80W), and Asus ROG Phone 7 (65W) are verified 2S dual-cell series implementations.
"""

import os
import re
import numpy as np
from scipy.optimize import differential_evolution

def parse_and_correct_dataset():
    filepath = r"C:\Users\Ion\.gemini\antigravity\scratch\smartphone_db\docs\modeling\NOT_USED\section_8_2_method_c_mse_huber_optimization_study\section_8_2_method_c_mse_huber_optimization_study.md"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    devices = {}
    
    in_table_1 = False
    for line in lines:
        if "| Battery (Wh) | P_peak (W) |" in line:
            in_table_1 = True
            continue
        if in_table_1 and line.startswith("| **"):
            cols = [c.strip() for c in line.split('|')]
            if len(cols) > 5:
                name = cols[1].replace('**', '').strip()
                battery_wh = float(re.sub(r'[^\d.]', '', cols[2]))
                p_peak = float(re.sub(r'[^\d.]', '', cols[3]))
                arch = cols[5].replace('`', '').strip()
                devices[name] = {
                    'name': name,
                    'battery_wh': battery_wh,
                    'p_peak': p_peak,
                    'arch': arch,
                }
        elif in_table_1 and line.startswith("---") and len(devices) > 0:
            in_table_1 = False
            
    in_table_2 = False
    for line in lines:
        if "| T_A (mins) |" in line:
            in_table_2 = True
            continue
        if in_table_2 and line.startswith("| **"):
            cols = [c.strip() for c in line.split('|')]
            if len(cols) > 4:
                name = cols[1].replace('**', '').strip()
                t_a = float(re.sub(r'[^\d.]', '', cols[3]))
                if name in devices:
                    devices[name]['t_a'] = t_a
        elif in_table_2 and line.startswith("---") and len(devices) > 0:
            in_table_2 = False

    # Apply verified hardware architecture corrections
    corrections = {
        "Motorola Edge 50 Pro": "dual",
        "OnePlus 12R": "dual",
        "Asus ROG Phone 7": "dual"
    }
    
    for dev_name, true_arch in corrections.items():
        if dev_name in devices:
            devices[dev_name]['arch'] = true_arch

    return list(devices.values())

def huber_loss(error, delta):
    abs_err = np.abs(error)
    if delta == 0:
        return abs_err
    return np.where(abs_err <= delta, 0.5 * error**2, delta * abs_err - 0.5 * delta**2)

def objective_function(params, dataset, delta):
    eta_low, c0_single, c0_dual, k, p = params
    t_handshake = 0.5
    
    total_loss = 0
    for d in dataset:
        e_supply = d['battery_wh']
        p_peak = d['p_peak']
        c_rate = p_peak / e_supply
        arch = d['arch']
        t_a = d['t_a']
        
        c0 = c0_dual if arch == 'dual' else c0_single
        
        diff = max(0.0, c_rate - c0)
        f_system = eta_low / (1.0 + k * (diff ** p))
        f_system = min(1.0, max(0.01, f_system))
        
        p_effective = p_peak * f_system
        t_c = (e_supply / p_effective) * 60.0 + t_handshake
        
        error = t_c - t_a
        total_loss += np.sum(huber_loss(error, delta))
        
    return total_loss / len(dataset)

def run_corrected_sweep():
    dataset = parse_and_correct_dataset()
    print(f"Loaded {len(dataset)} verified devices.")
    
    max_c_rate = max(d['p_peak'] / d['battery_wh'] for d in dataset)
    print(f"Max C_rate in dataset: {max_c_rate:.2f} h^-1")
    
    delta_values = [0.0, 1.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0]
    
    print("\n--- RE-SWEEPING HUBER DELTA ON AUDITED CORRECTED DATA ---")
    print(f"{'Delta':<8} | {'eta_low':<8} | {'C0_sing':<8} | {'C0_dual':<8} | {'k':<8} | {'p':<8} | {'MAE_T':<8} | {'RMSE_T':<8} | {'Max_Err':<8} | {'Boundary Status':<15}")
    print("-" * 115)
    
    results = []
    for delta in delta_values:
        # Search bounds with room for expansion
        current_bounds = [
            (0.50, 1.00),   # eta_low
            (0.00, 15.00),  # c0_single
            (0.00, 15.00),  # c0_dual
            (0.00, 10.00),  # k
            (0.01, 5.00)    # p
        ]
        
        for attempt in range(5):
            res = differential_evolution(
                objective_function,
                current_bounds,
                args=(dataset, delta),
                strategy='best1bin',
                maxiter=4000,
                popsize=40,
                seed=42
            )
            
            p_val = res.x
            hit_boundary = False
            
            for idx, (val, (b_low, b_high)) in enumerate(zip(p_val, current_bounds)):
                if abs(val - b_low) < 1e-3 or abs(val - b_high) < 1e-3:
                    hit_boundary = True
                    range_width = b_high - b_low
                    new_low = max(0.0, b_low - range_width * 0.5) if idx != 0 else max(0.5, b_low - 0.1)
                    new_high = b_high + range_width * 1.5
                    current_bounds[idx] = (new_low, new_high)
            
            if not hit_boundary:
                break
                
        errors = []
        for d in dataset:
            e_supply = d['battery_wh']
            p_peak = d['p_peak']
            c_rate = p_peak / e_supply
            arch = d['arch']
            t_a = d['t_a']
            
            c0 = p_val[2] if arch == 'dual' else p_val[1]
            diff = max(0.0, c_rate - c0)
            f_system = p_val[0] / (1.0 + p_val[3] * (diff ** p_val[4]))
            f_system = min(1.0, max(0.01, f_system))
            p_effective = p_peak * f_system
            t_c = (e_supply / p_effective) * 60.0 + 0.5
            errors.append(t_c - t_a)
            
        errors = np.array(errors)
        mae = np.mean(np.abs(errors))
        rmse = np.sqrt(np.mean(errors**2))
        max_err = np.max(np.abs(errors))
        
        b_status = "OK (Interior)" if not hit_boundary else "Hit Boundary"
        
        print(f"{delta:<8.1f} | {p_val[0]:<8.4f} | {p_val[1]:<8.4f} | {p_val[2]:<8.4f} | {p_val[3]:<8.4f} | {p_val[4]:<8.4f} | {mae:<8.2f} | {rmse:<8.2f} | {max_err:<8.2f} | {b_status:<15}")
        
        results.append((delta, p_val, mae, rmse, max_err, errors))
        
    return dataset, results

if __name__ == "__main__":
    run_corrected_sweep()
