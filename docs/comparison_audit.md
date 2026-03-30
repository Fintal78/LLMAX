# Comparison Audit: Benchmark-Driven Sections

This document identifies inconsistencies between `proposed_data_structure.md` (PDS) and `scoring_rules.md` (SR) for subsections 2.11, 6.1, 6.2, 6.3, 6.4, and 8.1.

## 📊 Summary of Major Discrepancies

| Section | Component | `scoring_rules.md` (SR) | `proposed_data_structure.md` (PDS) | Status |
| :--- | :--- | :--- | :--- | :--- |
| **6.3** | GPU API Table | Simple (Vulkan 1.3 = 10.0) | Detailed + Matrices (Vulkan 1.4 = 10.0) | **PDS is better** |
| **6.3** | GPU Architecture Table| Standard models | Includes 2025 models (Adreno 830) | **PDS is better** |
| **6.4** | AI Method A Formula | Logarithmic (INT8 Score) | Placeholder (`XXXX`) | **SR is better** |
| **8.1** | Layer B (HEI) Logic | Weighted Sum (SoC, Disp, Conn, Therm) | Simplistic Multiplier (SoC * Disp) | **SR is better** |
| **8.2/8.3**| Charging Formula | **Inverse Proportional** (1/W) | Logarithmic | **SR is better** |
| **8.6** | Charger Adequacy | **Ratio** (Included / Max) | Tiered (Tiers 1-5) | **SR is better** |
| **9.1** | Price Formula | Logarithmic | Linear | **SR is better** |

---

## 🔍 Detailed Analysis & Recommendations

### 1. Section 6.3: GPU API & Reference Data
*   **Discrepancy:** PDS contains a future-proofed API table (supporting Vulkan 1.4 / Metal 4.0) and granular fallback matrices for ambiguous specs. SR uses a simplified version and lacks fallback rules.
*   **Recommendation:** **Keep PDS version.** It is significantly more robust for autonomous scoring.
*   **Action:** Update `scoring_rules.md` to reflect the PDS table and include the matrices.

### 2. Section 6.4: AI Hardware Performance
*   **Discrepancy:** PDS has a placeholder (`subscore = XXXX`) for Method A. SR provides the correct logarithmic normalization formula.
*   **Recommendation:** **Keep SR version.**
*   **Action:** Transpose the SR formula into the PDS guideline.

### 3. Section 8.1: Battery Endurance (HEI Layer)
*   **Discrepancy:** SR uses a sophisticated weighted model (40% SoC, 40% Display, 10% Conn, 10% Therm). PDS uses a legacy "SoC * Display" logic which is mathematically inconsistent with the weighted Euclidean distance in Method B.
*   **Recommendation:** **Keep SR version.**
*   **Action:** Refactor PDS Section 8.1 to include sub-fields for HEI components and update the guideline.

### 4. Section 8.2 & 8.3: Charging Physics
*   **Discrepancy:** PDS uses Logarithmic formulas. SR uses **Inverse Proportional** formulas.
*   **Justification:** Charging time ($T$) is inversely proportional to wattage ($T \propto 1/W$). A log scale misrepresents the real-world benefit (diminishing time-savings at high watts).
*   **Recommendation:** **Keep SR version.**
*   **Action:** Update PDS guidelines to use the inverse formula.

### 5. Section 8.6: Charger Adequacy
*   **Discrepancy:** SR uses a continuous ratio (`Included/Max`). PDS uses fixed tiers. 
*   **Justification:** The ratio method is future-proof (e.g., if max speed is 45W, a 45W charger gets 10/10). Tiers penalize flagships with proprietary speeds.
*   **Recommendation:** **Keep SR version.**
*   **Action:** Update PDS to use the ratio formula.

### 6. Section 9.1: Price Sensitivity
*   **Discrepancy:** PDS uses Linear scaling. SR uses Logarithmic.
*   **Justification:** Price utility is inherently relative (logarithmic). $50 has more impact on a budget phone than a flagship.
*   **Recommendation:** **Keep SR version.**
*   **Action:** Update PDS guideline.

---

## 🛠 Next Steps

1.  **Synchronize Reference Tables**: Copy new GPU models and API Tiers from PDS to SR.
2.  **Harmonize PDS Guidelines**: Update PDS with the superior formulas from SR.
3.  **Refactor Section 8.1**: Update the PDS JSON structure for the Battery Efficiency Layer (HEI) to support the weighted calculation.
