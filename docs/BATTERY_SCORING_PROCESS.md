# Battery Scoring Process - Complete Lifecycle Guide

## Table of Contents
1. [Overview](#overview)
2. [The Three Scripts](#the-three-scripts)
3. [Lifecycle Scenarios](#lifecycle-scenarios)
4. [Decision Matrix](#decision-matrix)
5. [Quick Start Guide](#quick-start-guide)
6. [Advanced Topics](#advanced-topics)

---

## Overview

The battery scoring system calculates performance scores for smartphones based on:
- **Layer A (45%):** Battery Energy (Wh)
- **Layer B (35%):** Hardware Efficiency Index (SoC, Display, Connectivity, Thermal, Charging)
- **Layer C (20%):** Software Optimization Index (OS/Skin, Bloatware)

### Three-Case Scoring Methodology

1. **Case 1:** Phones with **both** GSMArena and PhoneArena benchmarks → Average them
2. **Case 2:** Phones with **one** benchmark → Use it
3. **Case 3:** Phones with **no** benchmarks → Interpolate from 3 nearest neighbors

See [battery_scoring_model.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/battery_scoring_model.md) for complete technical specifications.

---

## The Three Scripts

### 1. battery_score_full_database.py
**Purpose:** Score entire database with full interpolation

**When to use:**
- ✅ Initial database setup
- ✅ Adding new phones (Precise Method)
- ✅ Periodic re-scoring
- ✅ After adding 5+ phones

**Runtime:** ~5-10 seconds for 60 phones

```bash
python src/battery_score_full_database.py
```

---

### 2. battery_score_new_phone.py
**Purpose:** Quickly score newly added phone(s)

**When to use:**
- ✅ Adding 1-4 phones (Fast Method)
- ✅ Development/testing
- ✅ Speed over maximum precision

**Limitations:**
- ⚠️ Doesn't update existing phones' scores which are using interpolation and hence could be impacted 
- ⚠️ Requires 3+ phones with benchmarks already in database

**Runtime:** <1 second

```bash
python src/battery_score_new_phone.py
```

---

### 3. battery_score_single_test.py
**Purpose:** Test scoring on example phone (documentation/debugging)

**When to use:**
- ✅ Testing formulas
- ✅ Validating layer calculations
- ✅ Documentation examples

**Limitations:**
- ❌ NO interpolation (Case 3 falls back to predicted)
- ❌ NOT for production

**Runtime:** <1 second

```bash
python src/battery_score_single_test.py
```

---

## Lifecycle Scenarios

### Scenario 1: Initial Database Setup

**Goal:** Score all phones for the first time

**Steps:**
```bash
# 1. Ensure all phones are in data/phones_db.json
# 2. Run full database scoring
python src/battery_score_full_database.py
```

**What happens:**
- Phase 1: Calculates predicted scores for all phones
- Phase 2: Applies 3-case logic to determine final scores
- All phones get `battery_scores` object added

---

### Scenario 2A: Add 1-4 Phones (Fast Method)

**Goal:** Quickly score newly added phone(s)

**Steps:**
```bash
# 1. Add new phone to data/phones_db.json (no battery_scores)
# 2. Run fast scoring
python src/battery_score_new_phone.py
```

**What happens:**
- Identifies phone without `battery_scores`
- Calculates its predicted score
- Finds 3 nearest neighbors from EXISTING scored phones
- Applies interpolation
- Updates ONLY the new phone

**Pros:**
- ⚡ Very fast
- ✅ Proper interpolation

**Cons:**
- ⚠️ Existing phones not updated
- ⚠️ Less precise than full rescore

---

### Scenario 2B: Add Phone(s) (Precise Method)

**Goal:** Add phone(s) with maximum accuracy

**Steps:**
```bash
# 1. Add new phone to data/phones_db.json (no battery_scores)
# 2. Run full database scoring
python src/battery_score_full_database.py
```

**What happens:**
- Re-calculates predicted scores for ALL phones
- New phone becomes available as neighbor
- Phones near new phone's score may get better interpolations
- ALL scores updated with latest neighbor constellation

**Pros:**
- ✅ Maximum accuracy
- ✅ All neighbor relationships updated

**Cons:**
- 🐌 Slower (~5-10 seconds)

---

### Scenario 3: Add Multiple Phones

**Goal:** Add 5+ new phones

**Recommendation:** Always use **Precise Method** (full database)

**Steps:**
```bash
# 1. Add all new phones to data/phones_db.json
# 2. Run full database scoring
python src/battery_score_full_database.py
```

**Why:** The neighbor constellation changes significantly with multiple additions, making fast method less accurate.

---

### Scenario 4: Periodic Re-Scoring

**Goal:** Ensure accuracy as database grows

**Frequency:** Monthly or after 20+ new phones

**Steps:**
```bash
python src/battery_score_full_database.py
```

**Why:** Maintains optimal neighbor relationships across entire database.

---

### Scenario 5: Adding Benchmark Data

**Goal:** Update phones with newly available benchmark results

**Steps:**
```bash
# 1. Edit phone entry in data/phones_db.json
# 2. Add benchmark data to battery_scores.benchmarks

# 3. Re-score entire database
python src/battery_score_full_database.py
```

**Example benchmark data:**
```json
{
  "battery_scores": {
    "benchmarks": {
      "gsmarena_active_use": {
        "hours": 16.75,
        "normalized_score": 5.84
      },
      "phonearena_battery_life": {
        "hours": 10.5,
        "normalized_score": 8.82
      }
    }
  }
}
```

---

## Decision Matrix

| Scenario | Script to Use | Speed | Precision |
|----------|--------------|-------|-----------|
| **Initial setup** | `battery_score_full_database.py` | Medium | ⭐⭐⭐ |
| **1-4 phones (fast)** | `battery_score_new_phone.py` | ⚡ Fast | ⭐⭐ |
| **1-4 phones (best)** | `battery_score_full_database.py` | Medium | ⭐⭐⭐ |
| **5+ new phones** | `battery_score_full_database.py` | Medium | ⭐⭐⭐ |
| **Test formula** | `battery_score_single_test.py` | Fast | ⭐ (no interpolation) |
| **Monthly rescore** | `battery_score_full_database.py` | Medium | ⭐⭐⭐ |
| **Add benchmarks** | `battery_score_full_database.py` | Medium | ⭐⭐⭐ |

---

## Quick Start Guide

### First Time Setup

```bash
# Navigate to project directory
cd c:\Users\Ion\.gemini\antigravity\scratch\smartphone_db

# Score all phones in database
python src/battery_score_full_database.py
```

### Adding Phone(s) (Choose One)

**Option A - Fast (1-4 phones):**
```bash
# 1. Add phone to data/phones_db.json
# 2. Run fast scorer
python src/battery_score_new_phone.py
```

**Option B - Precise (Recommended):**
```bash
# 1. Add phone to data/phones_db.json
# 2. Run full database scorer
python src/battery_score_full_database.py
```

---

## Advanced Topics

### Data Structure Created

Each phone gets a `battery_scores` object:

```json
{
  "battery_scores": {
    "layer_a_energy": {
      "wh": 19.25,
      "score": 6.62
    },
    "layer_b_hei": {
      "total_hei_score": 7.6
    },
    "layer_c_soi": {
      "total_soi_score": 6.2
    },
    "predicted_score": 6.9,
    "benchmarks": {
      "gsmarena_active_use": {
        "hours": 0,
        "normalized_score": 0
      },
      "phonearena_battery_life": {
        "hours": 0,
        "normalized_score": 0
      }
    },
    "final_score": 6.9,
    "score_source": "Predicted Score (Insufficient benchmark data...)",
    "booster": 1.0
  }
}
```

### How Interpolation Works

1. **Predicted Score:** Calculate technical score (A+B+C) for target phone
2. **Find Neighbors:** Search database for 3 phones with benchmarks closest to target's predicted score
3. **Calculate Ratio:**
   ```
   Ratio = Target_Predicted / Average_Neighbor_Predicted
   ```
4. **Apply Ratio:**
   ```
   Final_Score = Ratio × Average_Neighbor_Final
   ```

This accounts for the gap between predicted and real-world performance.

### Troubleshooting

**"Insufficient benchmark data for interpolation"**
- Means: Database has <3 phones with both benchmarks
- Solution: Add benchmark data to at least 3 phones or accept predicted scores

**"All phones already have battery scores!"**
- Means: No unscored phones found (when using `battery_score_new_phone.py`)
- Solution: Either add a new phone or use `battery_score_full_database.py` to re-score

---

## Best Practices

1. **Initial Setup:** Always use `battery_score_full_database.py` first
2. **Fast Additions:** Use `battery_score_new_phone.py` for 1-4 phones
3. **Bulk Additions:** Use `battery_score_full_database.py` for 5+ phones
4. **Monthly Maintenance:** Re-score with `battery_score_full_database.py`
5. **Testing:** Use `battery_score_single_test.py` only for debugging

---

## Related Documentation

- [battery_scoring_model.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/battery_scoring_model.md) - Technical specification
- [scoring_rules.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_rules.md) - Complete scoring rules
- [proposed_data_structure.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/proposed_data_structure.md) - Database schema

---

## Questions?

The scripts are self-documenting. View their docstrings for more details:

```bash
python src/battery_score_full_database.py --help
python src/battery_score_new_phone.py --help
python src/battery_score_single_test.py --help
```

Or view the source code directly - each script has a comprehensive docstring at the top.
