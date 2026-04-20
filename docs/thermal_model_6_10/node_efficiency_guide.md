# TECHNICAL GUIDE: PROCESS NODE & HEAT GENERATION (PART C)

This document defines how to characterize the **Thermal Demand** (heat generated) of a smartphone using publicly available data. This is the final component of the Section 6.10 Thermodynamic Model.

---

## 1. The Core Philosophy
The stability of a phone is a ratio:
**Stability Ratio = Sustainable Power (Supply) / Peak Thermal Demand (Demand)**

- **Supply (Parts A + B):** How much heat the chassis and cooling system can move (e.g., 6 Watts). 
- **Demand (Part C):** How much heat the SoC generates under a heavy workload (e.g., 10 Watts).

If Supply >= Demand, stability is 100%. If Supply < Demand, the phone must throttle.

---

## 2. Required Inputs (Public Data)
To calculate Part C without internal diagnostic tools, the scoring agent requires only two inputs:
1.  **SoC Model Name** (e.g., Snapdragon 8 Gen 3).
2.  **Process Node & Foundry** (e.g., 4nm TSMC).

### Why Frequency is Not Enough
Frequency only tells you the "speed" of the clock. It doesn't tell you the **Energy per Instruction**. A 3 GHz chip on a 10nm node burns ~3x more power than a 3 GHz chip on a 3nm node due to transistor leakage and voltage requirements. Therefore, the **Node (nm)** is the primary coefficient for heat generation efficiency.

---

## 3. SoC Thermal Demand Tiers
SoCs are categorized into "Demand Tiers" based on their measured peak power draw in aggregate reviews (Geekerwan, Golden Reviewer, AnandTech).

| Demand Tier          | Peak Power (P-peak) | Example SoCs                         |
| :------------------- | :------------------ | :----------------------------------- |
| **Max / Ultra**      | **12W - 15W**       | Snapdragon 8 Elite, Apple A18 Pro    |
| **High Performance** | **9W - 11W**        | Snapdragon 8 Gen 2, Dimensity 9200   |
| **Balanced / Mid**   | **5W - 7W**         | Snapdragon 7+ Gen 2, Apple A15 (Non-Pro)|
| **Efficiency / Lo**  | **3W - 4W**         | Snapdragon 4 Gen 1, Helio G99        |
| **Ultra Low Power**  | **< 2W**            | Unisoc T606, wearable chips          |

---

## 4. The Node Efficiency Multiplier
The total heat multiplier (**M-total**) is the product of the physical node scale and the foundry's implementation quality.

**Formula:** `M-total = M-nm * M-foundry`

### 4.1 Table: Node Scale Multiplier (M-nm)
Represents the theoretical benefit of the nanometer shrink.

| Process Node (nm) | Modifier (M-nm) | Physical Rationale                    |
| :---------------- | :-------------- | :------------------------------------ |
| **3nm**           | **0.90**        | Highest transistor density.           |
| **4nm**           | **1.00**        | Current Reference Standard.           |
| **5nm / 6nm**     | **1.20**        | Mainstream efficiency baseline.       |
| **7nm / 8nm**     | **1.50**        | Planar/FinFET hybrid limits.          |
| **10nm+**         | **2.00+**       | Legacy; high performance-to-watt gap. |

### 4.2 Table: Foundry Quality Multiplier (M-foundry)
Represents the implementation efficiency (leakage/yield) of the specific foundry.

| Foundry / Process      | Modifier (M-foundry) | Technical Justification              |
| :--------------------- | :------------------ | :----------------------------------- |
| **TSMC (N-series)**    | **0.95**            | Industry leader in thermal leakage control. |
| **Intel (Intel 4+)**   | **1.00**            | Reference implementation baseline.   |
| **Samsung (LPP/LPU)**  | **1.10**            | Historically higher parasitic leakage. |

---

## 5. Combined Multiplier Examples (M-total)

- **3nm TSMC:** `0.90 * 0.95` = **0.85** (Final Modifier)
- **4nm TSMC:** `1.00 * 0.95` = **0.95** (Final Modifier)
- **4nm Samsung:** `1.00 * 1.10` = **1.10** (Final Modifier)
- **5nm Samsung:** `1.20 * 1.10` = **1.32** (Final Modifier)

**Final Demand Formula:**
`P-demand = Base-Tier-Power * M-node`

---

## 6. Concrete Example (Part C in Action)

### Unit 1: OnePlus Nord 4 (Snapdragon 7 Plus Gen 3)
- **SoC Tier:** Balanced / Mid -> **6.0 Watts (Base)**
- **Node:** 4nm TSMC -> **0.95 (Modifier)**
- **P-demand:** `6.0 * 0.95` = **5.7 Watts**
- **System Stability:** If A+B Supply = 6.0 Watts -> **100% Stability**.

### Unit 2: Samsung S24 Ultra (Snapdragon 8 Gen 3)
- **SoC Tier:** Max / Ultra -> **14.0 Watts (Base)**
- **Node:** 4nm TSMC -> **0.95 (Modifier)**
- **P-demand:** `14.0 * 0.95` = **13.3 Watts**
- **System Stability:** If A+B Supply = 6.6 Watts -> **49.6% Stability** (Expected throttling).

---

## 7. Practical Implementation Rules
1.  **Race to Sleep:** For burst tasks (<30s), Part C is ignored. The "Thermal Mass" (Capacitance) handles the spike.
2.  **Sustained Load:** For tasks >300s, Part C is the master limit.
3.  **Ambiguity:** If the SoC is unlisted, find its closest relative in **Section 6.1 (CPU Architecture)** and match its generation.
4.  **Foundry Matters:** Always distinguish between Samsung and TSMC nodes for the same "nm" class (e.g., Snapdragon 8 Gen 1 [Samsung] vs 8+ Gen 1 [TSMC]).

---

## 8. Logical Integration in Section 6.10
The final TDSI Score uses this stability ratio to scale the raw performance potential:
`Final-Stability-Score = (P-sustained / P-demand) * 10` (Capped at 10.0)
