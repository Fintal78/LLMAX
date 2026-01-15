"""
Battery Score Calculator - New Phone(s) Mode (Fast Method)

DESCRIPTION:
This script scores ONE OR MORE newly added phones using the existing scored phones
as potential neighbors. This is the FAST method for adding new phones.

WORKFLOW:
1. Identifies all unscored phones (those without battery_scores)
2. For each unscored phone:
   - Calculates predicted score
   - Finds 3 nearest neighbors from EXISTING scored phones
   - Applies interpolation if no benchmarks available
3. Updates ONLY the new phone(s)' scores

SCORING METHODOLOGY:
- Case 1: Phone with both benchmarks → Use benchmark average
- Case 2: Phone with one benchmark → Use that benchmark  
- Case 3: Phone with no benchmarks → Interpolate from 3 nearest EXISTING neighbors

ADVANTAGES:
⚡ Fast - processes only new phone(s) (not entire database)
✓ Good for rapid additions of 1-4 phones
✓ No need to re-score entire database
✓ Uses proper interpolation (unlike battery_score_single_test.py)

LIMITATIONS:
⚠️ Does not update other phones' scores
⚠️ Neighbor constellation for existing phones unchanged
⚠️ Less precise than full database rescore
⚠️ Only works if there are already 3+ phones with benchmarks in database

WHEN TO USE:
✓ Adding 1-4 new phones quickly
✓ Testing/development scenarios
✓ When speed is more critical than maximum precision
✓ When database already has good benchmark coverage
✓ When you don't want to update existing phones' neighbor relationships

FOR MAXIMUM PRECISION:
Use battery_score_full_database.py instead - it will re-score all phones
and update neighbor relationships across the entire database.

USAGE:
    python battery_score_new_phone.py
    
RUNTIME: <1 second per phone (~3 seconds for 5 phones)

OUTPUT: Updates data/phones_db.json with battery_scores for ONLY the new phone(s)

SEE ALSO:
- battery_score_full_database.py - Score entire database (precise method)
- battery_score_single_test.py - Test scoring on single phone from markdown
- docs/BATTERY_SCORING_PROCESS.md - Complete lifecycle documentation
"""

import json
import re
import os
import sys

# Import the scoring functions from the full database script
# We can reuse all the layer calculation functions
sys.path.insert(0, os.path.dirname(__file__))
from battery_score_full_database import (
    calc_layer_a, calc_layer_b, calc_layer_c,
    calc_benchmarks, find_nearest_neighbors
)

def find_newest_unscored_phone(phones):
    """
    Find phones that don't have battery_scores yet.
    
    Returns:
        List of phones without battery_scores, or None if all are scored
    """
    unscored = [p for p in phones if 'battery_scores' not in p]
    
    if not unscored:
        return None
    
    return unscored

def score_new_phone(db_path):
    """
    Score newly added phone(s) using existing scored phones as neighbors.
    
    Args:
        db_path: Path to phones_db.json
    """
    print(f"Loading database from {db_path}...")
    
    # Load database
    with open(db_path, 'r', encoding='utf-8') as f:
        db_data = json.load(f)
    
    phones = db_data.get('phones', [])
    print(f"Found {len(phones)} phones in database")
    
    # Find unscored phones
    unscored_phones = find_newest_unscored_phone(phones)
    
    if not unscored_phones:
        print("\n[INFO] All phones already have battery scores!")
        print("Nothing to do.")
        return db_data
    
    print(f"\nFound {len(unscored_phones)} unscored phone(s):")
    for phone in unscored_phones:
        print(f"  - {phone.get('model_name', 'Unknown')}")
    
    # Get list of already scored phones for neighbor search
    scored_phones = [p for p in phones if 'battery_scores' in p]
    print(f"\nFound {len(scored_phones)} already scored phones for neighbor matching")
    
    # Score each unscored phone
    print(f"\nScoring {len(unscored_phones)} phone(s)...")
    
    for phone in unscored_phones:
        phone_name = phone.get('model_name', 'Unknown')
        print(f"\n  Processing: {phone_name}")
        
        # Calculate layers
        specs = phone.get('specs', {})
        layer_a = calc_layer_a(specs)
        layer_b = calc_layer_b(specs)
        layer_c = calc_layer_c(specs)
        
        predicted_score = (0.45 * layer_a["score"] + 
                          0.35 * layer_b["total_hei_score"] + 
                          0.20 * layer_c["total_soi_score"])
        
        benchmarks = calc_benchmarks(phone)
        
        print(f"    Predicted score: {predicted_score:.2f}")
        
        # Determine final score using 3-case logic
        gsm_score = benchmarks['gsmarena_active_use']['normalized_score']
        pa_score = benchmarks['phonearena_battery_life']['normalized_score']
        
        final_score = 0
        source = "None"
        
        # Case 1: Both benchmarks available
        if gsm_score > 0 and pa_score > 0:
            final_score = (gsm_score + pa_score) / 2
            source = "GSMArena Active Use + PhoneArena Battery Life"
            print(f"    Case 1: Using both benchmarks")
        
        # Case 2: Only one benchmark available
        elif gsm_score > 0:
            final_score = gsm_score
            source = "GSMArena Active Use"
            print(f"    Case 2: Using GSMArena benchmark")
        elif pa_score > 0:
            final_score = pa_score
            source = "PhoneArena Battery Life"
            print(f"    Case 2: Using PhoneArena benchmark")
        
        # Case 3: No benchmarks - Use interpolation from EXISTING phones
        else:
            print(f"    Case 3: No benchmarks, searching for neighbors...")
            neighbors = find_nearest_neighbors(predicted_score, scored_phones)
            
            if neighbors and len(neighbors) >= 3:
                # Calculate average predicted score of neighbors
                avg_pred_neighbors = sum(
                    n['battery_scores']['predicted_score'] for n in neighbors
                ) / len(neighbors)
                
                # Calculate average final score of neighbors
                avg_final_neighbors = sum(
                    n['battery_scores']['final_score'] for n in neighbors
                ) / len(neighbors)
                
                # Calculate correction ratio
                ratio = predicted_score / avg_pred_neighbors if avg_pred_neighbors > 0 else 1.0
                
                # Apply ratio to neighbor average
                final_score = ratio * avg_final_neighbors
                
                neighbor_names = [n.get('model_name', 'Unknown')[:30] for n in neighbors]
                source = f"Interpolated from neighbors (Ratio: {ratio:.3f}): {', '.join(neighbor_names)}"
                
                print(f"    Found {len(neighbors)} neighbors")
                print(f"    Neighbor avg predicted: {avg_pred_neighbors:.2f}")
                print(f"    Neighbor avg final: {avg_final_neighbors:.2f}")
                print(f"    Correction ratio: {ratio:.3f}")
            else:
                # Fallback if not enough neighbors
                final_score = predicted_score
                source = "Predicted Score (Insufficient benchmark data for interpolation)"
                print(f"    WARNING: Not enough neighbors with benchmarks ({len(neighbors) if neighbors else 0} found, need 3)")
                print(f"    Falling back to predicted score")
        
        # Calculate booster
        booster = final_score / predicted_score if predicted_score > 0 else 1.0
        
        # Store results
        phone['battery_scores'] = {
            'layer_a_energy': layer_a,
            'layer_b_hei': layer_b,
            'layer_c_soi': layer_c,
            'predicted_score': round(predicted_score, 2),
            'benchmarks': benchmarks,
            'final_score': round(final_score, 2),
            'score_source': source,
            'booster': round(booster, 3)
        }
        
        print(f"    Final score: {final_score:.2f}")
    
    # Save updated database
    print(f"\nSaving updated database to {db_path}...")
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(db_data, f, indent=2)
    
    print(f"[SUCCESS] Scored {len(unscored_phones)} new phone(s)!")
    
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
    
    score_new_phone(db_path)

if __name__ == "__main__":
    main()
