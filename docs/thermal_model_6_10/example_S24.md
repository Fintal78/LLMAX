# Case Study: Samsung Galaxy S24 Ultra Thermal Modelization (Section 6.10)

This document demonstrates the full A to Z physics-based model for Section 6.10, showing how the multi-surface chassis properties, cooling technologies, and exposure coefficients unify into a single **Admissible Thermal Power (P_adm)**.

---

## 1. Input Specifications (The Physical Reality)

| Data Point                  | Specification                | Physical Value                 |
| :-------------------------- | :--------------------------- | :----------------------------- |
| **Material (A1)**           | Titanium Frame / Glass Back  | k=1.1 (Glass), k=17 (Titanium) |
| **Thickness**               | Standard Flagship            | 0.6 mm Glass, 2.0 mm Ti Wall   |
| **Total Footprint Area**    | 162.3 mm x 79.0 mm           | 0.0128 m² (Front and Back)     |
| **Frame Dimensions**        | Perimeter x Thickness (8.6mm)| 0.00415 m²                     |
| **Device Weight (A2)**      | Official Spec                | 0.232 kg                       |
| **Internal Cooling (Part B)**| Vapor Chamber (XL)           | Full-body footprint coverage   |
| **Processor Node (Part C)** | Snapdragon 8 Gen 3           | TSMC 4nm                       |

---

## 2. Step-by-Step Thermal Calculation

### Step A: Multi-Surface Active Areas
Heat dissipates across three independent surfaces. The active radiating area for each is throttled by its Spreading Efficiency (**Spreading_efficiency**) and its Environmental Exposure (**E_ratio**). 
`Area_active = Area_surface * Spreading_efficiency * E_ratio`

1.  **Front Screen:**
    *   **Spreading_efficiency:** 0.25 (Insulating PCB bottleneck from rear-mounted SoC).
    *   **E_ratio:** 1.0 (Fully exposed).
    *   *Area_active:* 0.0128 * 0.25 * 1.0 = **0.00320 m²**
2.  **Mid-Frame (Titanium):**
    *   **Spreading_efficiency:** 1.00 (Conductive Metal instantly shares perimeter heat).
    *   **E_ratio:** 1.0 (Sides fully exposed).
    *   *Area_active:* 0.00415 * 1.00 * 1.0 = **0.00415 m²**
3.  **Back Panel (Glass + VC XL):**
    *   **Spreading_efficiency:** 0.90 (VC greatly overrides glass thermal insulation).
    *   **E_ratio:** 0.30 (Compromise: Blocked by hands / smothered by desk).
    *   *Area_active:* 0.0128 * 0.90 * 0.30 = **0.00346 m²**

### Step B: Parallel Resistance Network (R_total)
Heat escapes via the easiest path (Parallel Circuit Law). `h = 10.0` for all external surfaces.

**Path 1: Front Screen ($R_{path} = R_{cond} + R_{conv}$)**
- `R_cond` = 0.0006 / (1.1 * 0.00320) = 0.17 K/W
- `R_conv` = 1 / (10.0 * 0.00320) = 31.25 K/W
- **R_path_front = 31.42 K/W**

**Path 2: Mid-Frame**
- `R_cond` = 0.002 / (17 * 0.00415) = 0.03 K/W
- `R_conv` = 1 / (10.0 * 0.00415) = 24.10 K/W
- **R_path_frame = 24.12 K/W**

**Path 3: Back Panel**
- `R_cond` = 0.0006 / (1.1 * 0.00346) = 0.16 K/W
- `R_conv` = 1 / (10.0 * 0.00346) = 28.90 K/W
- **R_path_back = 29.09 K/W**

**Total System Resistance (R_total):**
- `1 / R_total = (1 / 31.42) + (1 / 24.12) + (1 / 29.09)`
- `1 / R_total = 0.0318 + 0.0414 + 0.0344 = 0.1076`
- **R_total = 9.29 K/W**

### Step C: Thermal Capacitance & Time Constant
How much energy can the unified physical mass absorb?
- `C = Mass * Standard_Bulk_Cp (850 J/kg·K)`
- **C** = 0.232 * 850 = **197.2 J/K**
- `Tau = R_total * C` = 9.29 * 197.2 = **1831.9 seconds**

---

## 3. Admissible Thermal Power (P_adm @ 1200s)

We calculate the maximum continuous power the S24 Ultra can handle for 1200 seconds before hitting the 20°C safety threshold using the exact Thermal Impedance (Z_th).

- `Z_th(t) = R_total * (1 - e^(-1200 / Tau))`
- `Z_th(1200)` = 9.29 * (1 - e^(-1200 / 1831.9))
- `Z_th(1200)` = 9.29 * (1 - 0.52) = **4.46 K/W**

**P_adm (Watts):**
- `P_adm = Delta_T / Z_th(1200)`
- `P_adm = 20 / 4.46` = **4.48 Watts**

---

## 4. Part C Interaction: Thermal Stability Ratio

Finally, compare the calculated Chassis Supply (P_adm) to the SoC Demand, accounting for the dynamic System Base Heat.

- **System Base Heat (P_base_heat):** 0.40W + (0.0075 * 114cm²) = **1.26W**
- **Admissible SoC Budget (P_adm_soc):** 4.48W - 1.26W = **3.22W**
- **Peak SoC Demand (Snapdragon 8 Gen 3):** **13.3 Watts**

- **Predicted Power Ratio:** 3.22 / 13.3 = **0.242** (24.2%)
- **Predicted FPS Stability (Gamma 0.33):** 0.242 ^ 0.33 = **62.6%**

### Benchmark Verification
- **Measured 3DMark Wild Life Extreme Reality:** **60.1%**
- **Alignment:** Sub-3% discrepancy. The rigorous multi-surface model correctly captures why the S24 Ultra throttles significantly despite an elite Vapor Chamber: the titanium frame limits the side bottleneck, while the front and rear faces struggle against heat path barriers and exposure compromises. 

**Conclusion:** The formal 6.10 score is driven by its rigorous derivation predicting exactly how the system reacts in a 20-minute physical window.
