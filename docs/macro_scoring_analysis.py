"""
Macro Scoring Model — Iteration 3 (Full parameter optimization)
================================================================
Key insight from Iteration 2: the main errors come from:
  1. UW-FF phones scoring too high (AF tier=6.0 is too generous for FF)
  2. Telemacro needing a principled bonus
  
This iteration:
  - Tests lower FF tier values (3.0, 4.0 instead of 6.0)
  - Tests bonus values (5-7) for telemacro 
  - Tests both the original approach (bonus = floor) and the new approach
    (bonus = additive on zoom+MFD composite)
"""

import math

phones = [
    # FLAGSHIP: Ultrawide AF Macro only
    {"name": "iPhone 16 Pro Max",        "uw_af": "AF", "uw_mfd_cm": 2.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 9.0},
    {"name": "iPhone 15 Pro Max",        "uw_af": "AF", "uw_mfd_cm": 2.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 8.5},
    {"name": "Google Pixel 9 Pro",       "uw_af": "AF", "uw_mfd_cm": 3.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 8.0},
    {"name": "Google Pixel 8 Pro",       "uw_af": "AF", "uw_mfd_cm": 3.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 7.5},
    {"name": "Samsung Galaxy S25 Ultra", "uw_af": "AF", "uw_mfd_cm": 2.5,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 8.0},
    {"name": "Samsung Galaxy S24 Ultra", "uw_af": "AF", "uw_mfd_cm": 2.5,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 7.5},
    {"name": "Samsung Galaxy S23 Ultra", "uw_af": "AF", "uw_mfd_cm": 3.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 7.0},
    {"name": "OnePlus 13",               "uw_af": "AF", "uw_mfd_cm": 3.5,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 7.0},
    {"name": "Huawei Pura 70 Ultra",     "uw_af": "AF", "uw_mfd_cm": 2.5,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 8.5},

    # FLAGSHIP: Ultrawide AF + Telemacro
    {"name": "Vivo X200 Pro",            "uw_af": "AF", "uw_mfd_cm": 2.5,  "tm_zoom_x": 3.7, "tm_mfd_cm": 15, "ded_mp": 0, "expert_rank": 10.0},
    {"name": "Xiaomi 14 Ultra",          "uw_af": "AF", "uw_mfd_cm": 5.0,  "tm_zoom_x": 3.0, "tm_mfd_cm": 10, "ded_mp": 0, "expert_rank": 9.5},
    {"name": "Xiaomi 15 Ultra",          "uw_af": "AF", "uw_mfd_cm": 5.0,  "tm_zoom_x": 3.0, "tm_mfd_cm": 10, "ded_mp": 0, "expert_rank": 9.5},
    {"name": "OnePlus 12",               "uw_af": "AF", "uw_mfd_cm": 3.5,  "tm_zoom_x": 3.0, "tm_mfd_cm": 20, "ded_mp": 0, "expert_rank": 8.5},
    {"name": "Vivo X Fold3 Pro",         "uw_af": "AF", "uw_mfd_cm": 3.0,  "tm_zoom_x": 3.0, "tm_mfd_cm": 15, "ded_mp": 0, "expert_rank": 8.5},
    {"name": "Xiaomi 14",                "uw_af": "AF", "uw_mfd_cm": 4.0,  "tm_zoom_x": 2.6, "tm_mfd_cm": 10, "ded_mp": 0, "expert_rank": 8.0},
    {"name": "S24 Ultra (3x tele)",      "uw_af": "AF", "uw_mfd_cm": 2.5,  "tm_zoom_x": 3.0, "tm_mfd_cm": 18, "ded_mp": 0, "expert_rank": 8.0},

    # MID-RANGE: Ultrawide FF
    {"name": "Samsung Galaxy A55",       "uw_af": "FF", "uw_mfd_cm": 4.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 5, "expert_rank": 4.0},
    {"name": "Google Pixel 8a",          "uw_af": "FF", "uw_mfd_cm": 5.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 4.5},
    {"name": "OnePlus Nord 3",           "uw_af": "FF", "uw_mfd_cm": 4.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 2, "expert_rank": 3.0},
    {"name": "Nothing Phone (2)",        "uw_af": "FF", "uw_mfd_cm": 4.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 3.5},

    # BUDGET: Dedicated Macro Only
    {"name": "Redmi Note 13",            "uw_af": "FF", "uw_mfd_cm": 5.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 2, "expert_rank": 2.0},
    {"name": "Redmi Note 13 Pro",        "uw_af": "FF", "uw_mfd_cm": 5.0,  "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 2, "expert_rank": 2.5},
    {"name": "OPPO A78",                 "uw_af": None,  "uw_mfd_cm": None, "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 2, "expert_rank": 1.5},
    {"name": "Moto G Power 2025",        "uw_af": None,  "uw_mfd_cm": None, "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 2, "expert_rank": 1.5},
    {"name": "Samsung Galaxy A16",       "uw_af": None,  "uw_mfd_cm": None, "tm_zoom_x": None, "tm_mfd_cm": None, "ded_mp": 0, "expert_rank": 0.5},
]

MACRO_DIST_CM_MIN = 1.5
MACRO_DIST_CM_MAX = 10.0
TELEMACRO_X_MIN   = 2.0
TELEMACRO_X_MAX   = 5.0
TM_MFD_CM_MIN     = 5.0
TM_MFD_CM_MAX     = 30.0

def clamp(val, lo=0.0, hi=10.0):
    return max(lo, min(hi, val))

def log_score(val, val_min, val_max, inverted=False):
    if val <= 0: return 0.0
    if inverted:
        return clamp(10 * (math.log(val_max) - math.log(val)) / (math.log(val_max) - math.log(val_min)))
    else:
        return clamp(10 * (math.log(val) - math.log(val_min)) / (math.log(val_max) - math.log(val_min)))

def model(phone, ff_tier, uw_af_w, uw_mfd_w, tm_bonus, tm_zoom_w, tm_mfd_w, ded_cap):
    scores = []
    if phone["uw_af"] is not None:
        af = 10.0 if phone["uw_af"] == "AF" else ff_tier
        mfd = phone["uw_mfd_cm"] if phone["uw_mfd_cm"] else MACRO_DIST_CM_MAX
        mfd_s = log_score(mfd, MACRO_DIST_CM_MIN, MACRO_DIST_CM_MAX, inverted=True)
        scores.append(("UW", clamp(uw_af_w * af + uw_mfd_w * mfd_s)))
    
    if phone["tm_zoom_x"] is not None and phone["tm_mfd_cm"] is not None:
        z = log_score(phone["tm_zoom_x"], TELEMACRO_X_MIN, TELEMACRO_X_MAX, inverted=False)
        m = log_score(phone["tm_mfd_cm"], TM_MFD_CM_MIN, TM_MFD_CM_MAX, inverted=True)
        rest = (10.0 - tm_bonus) * (tm_zoom_w * z + tm_mfd_w * m) / 10.0
        scores.append(("TM", clamp(tm_bonus + rest)))
    
    if phone["ded_mp"] > 0:
        scores.append(("DED", clamp(phone["ded_mp"], 0, ded_cap)))
    
    if not scores:
        return 0.0, "NONE"
    best = max(scores, key=lambda x: x[1])
    return best[1], best[0]


def evaluate(params, label, verbose=False):
    ff_tier, uw_af_w, uw_mfd_w, tm_bonus, tm_zoom_w, tm_mfd_w, ded_cap = params
    errs = []
    if verbose:
        print(f"\n{'='*120}")
        print(f"  MODEL: {label}")
        print(f"  FF_tier={ff_tier}, UW={uw_af_w}/{uw_mfd_w}, TM_bonus={tm_bonus}, TM={tm_zoom_w}/{tm_mfd_w}, DED_cap={ded_cap}")
        print(f"{'='*120}")
        print(f"{'Phone':<30} {'Expert':>6} | {'Score':>7} {'Path':>4} | {'Err':>5}")
        print(f"{'-'*80}")
    
    for p in phones:
        s, path = model(p, ff_tier, uw_af_w, uw_mfd_w, tm_bonus, tm_zoom_w, tm_mfd_w, ded_cap)
        e = p["expert_rank"]
        err = abs(s - e)
        errs.append(err)
        if verbose:
            flag = " !!" if err > 2.0 else ""
            print(f"{p['name']:<30} {e:>6.1f} | {s:>7.2f} {path:>4} | {err:>5.2f}{flag}")
    
    mae = sum(errs) / len(errs)
    rmse = math.sqrt(sum(x**2 for x in errs) / len(errs))
    if verbose:
        print(f"\n  MAE: {mae:.2f}    RMSE: {rmse:.2f}")
    return mae, rmse


# ─────────────────────────────────────────────────────────────────────────────
# GRID SEARCH over key parameters
# ─────────────────────────────────────────────────────────────────────────────
# (ff_tier, uw_af_w, uw_mfd_w, tm_bonus, tm_zoom_w, tm_mfd_w, ded_cap)

best_mae = float('inf')
best_config = None
best_label = ""

results = []
for ff_tier in [3.0, 4.0, 5.0, 6.0]:
    for tm_bonus in [5.0, 5.5, 6.0, 6.5, 7.0]:
        for ded_cap in [3.0, 4.0]:
            for tm_z_w, tm_m_w in [(0.6, 0.4), (0.7, 0.3), (0.5, 0.5)]:
                params = (ff_tier, 0.4, 0.6, tm_bonus, tm_z_w, tm_m_w, ded_cap)
                label = f"FF={ff_tier} Bonus={tm_bonus} TM_z/m={tm_z_w}/{tm_m_w} DED={ded_cap}"
                mae, rmse = evaluate(params, label, verbose=False)
                results.append((mae, rmse, label, params))
                if mae < best_mae:
                    best_mae = mae
                    best_config = params
                    best_label = label

# Sort by MAE and show top 10
results.sort(key=lambda x: x[0])

print("=" * 100)
print("TOP 10 CONFIGURATIONS (sorted by MAE)")
print("=" * 100)
print(f"{'#':>3} {'MAE':>6} {'RMSE':>6}  Configuration")
print("-" * 100)
for i, (mae, rmse, label, params) in enumerate(results[:10]):
    marker = " <-- BEST" if i == 0 else ""
    print(f"{i+1:>3} {mae:>6.3f} {rmse:>6.3f}  {label}{marker}")

# Also show the current model for reference
cur_params = (6.0, 0.4, 0.6, 7.0, 1.0, 0.0, 6.0)
cur_mae, cur_rmse = evaluate(cur_params, "CURRENT", verbose=False)
print(f"\n  REF: CURRENT model:  MAE={cur_mae:.3f}  RMSE={cur_rmse:.3f}")

# Show detailed output for the best model
print("\n\n")
evaluate(best_config, f"BEST: {best_label}", verbose=True)

# Verify constraint: dedicated never beats ultrawide-AF or telemacro
print(f"\n\nCONSTRAINT CHECK (DED cap = {best_config[6]}):")
ff_tier, uw_af_w, uw_mfd_w, tm_bonus, tm_zoom_w, tm_mfd_w, ded_cap = best_config
violations = False
for p in phones:
    if p["ded_mp"] > 0:
        ded_s = clamp(p["ded_mp"], 0, ded_cap)
        uw_s = None
        if p["uw_af"] == "AF":
            mfd = p["uw_mfd_cm"] if p["uw_mfd_cm"] else MACRO_DIST_CM_MAX
            mfd_s = log_score(mfd, MACRO_DIST_CM_MIN, MACRO_DIST_CM_MAX, inverted=True)
            uw_s = clamp(uw_af_w * 10.0 + uw_mfd_w * mfd_s)
        if uw_s is not None and ded_s > uw_s:
            print(f"  VIOLATION: {p['name']}: DED={ded_s:.2f} > UW-AF={uw_s:.2f}")
            violations = True
if not violations:
    print("  All constraints satisfied.")

print(f"\n\n{'='*80}")
print("RECOMMENDED SCORING CONSTANTS (from best model):")
print(f"{'='*80}")
print(f"  UW FF Tier Score       = {best_config[0]}")
print(f"  UW weights (AF/MFD)    = {best_config[1]}/{best_config[2]}")
print(f"  TM Architectural Bonus = {best_config[3]}")
print(f"  TM weights (Zoom/MFD)  = {best_config[4]}/{best_config[5]}")
print(f"  DED Macro Cap          = {best_config[6]}")
print()
print("  TM Formula: Score = Bonus + (10 - Bonus)/10 * (Zoom_w * Zoom_Score + MFD_w * MFD_Score)")
print(f"  With Bonus={best_config[3]}: Score = {best_config[3]} + {10-best_config[3]}/10 * composite")
print(f"  This replaces the old arbitrary floor of 7.0 with a data-driven bonus of {best_config[3]}.")
