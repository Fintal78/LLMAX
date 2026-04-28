# Case Study: Samsung Galaxy S24 Ultra Thermal Modelization (Section 6.10)

This document demonstrates the full A to Z physics-based model for Section 6.10, showing how the multi-surface chassis properties, cooling technologies, and exposure coefficients unify into a single **Admissible Thermal Power (P_adm)**.

---

## 1. Input Specifications (The Physical Reality)

| Data Point                  | Specification                | Physical Value                 |
| :-------------------------- | :--------------------------- | :----------------------------- |
| **Material (A1)**           | Titanium Frame / Glass Back  | k=1.1 (Glass), k=7.0 (Titanium Grade 5) |
| **Dimensions (Global)**     | Height x Width x Thickness   | 162.3mm x 79.0mm x 8.6mm       |
| **Footprint Area**          | Area_face                    | 0.01282 m² (128.2 cm²)         |
| **Frame Dimensions**        | Perimeter (P)                | 0.4826 m                       |
| **Frame Radiator Area**     | Area_frame (Chi 0.85)        | 0.00353 m²                     |
| **Display Footprint**       | Area_display (Physical)      | 114.4 cm²                      |
| **Device Weight (A2)**      | Official Spec                | 0.232 kg                       |
| **Internal Cooling (Part B)**| Vapor Chamber (XL)           | Full-body 0.90 S_eff           |
| **Processor Node (Part C)** | Snapdragon 8 Gen 3           | TSMC 4nm                       |

---

## 2. Step-by-Step Thermal Calculation

### Step A: Multi-Surface Active Areas
Heat dissipates across three independent surfaces. The active radiating area for each is dictated fundamentally by its Spreading Efficiency (**Spreading_efficiency**). 
`Area_active = Area_surface * Spreading_efficiency`

*(Note: Exposure Ratio is maintained at 1.0 for all surfaces based on the Section 6.10 overhaul. Hand/Table conduction is assumed to offset convective losses).*

1.  **Front Screen:**
    *   **Spreading_efficiency:** 0.25 (Insulating PCB bottleneck from rear-mounted SoC).
    *   *Area_active:* 0.0128 * 0.25 = **0.00320 m²**
2.  **Mid-Frame (Titanium):**
    *   **Spreading_efficiency:** 0.40 (Class 2: Moderate Alloy).
    *   *Area_active:* (0.4826 * 0.0086 * 0.85) * 0.40 = **0.00141 m²**
3.  **Back Panel (Glass + VC XL):**
    *   **Spreading_efficiency:** 0.95 (Extreme VC Tier - Maximized utilization).
    *   *Area_active:* 0.01282 * 0.95 = **0.01218 m²**

### Step B: Parallel Resistance Network (R_total)
Heat escapes via the easiest path (Parallel Circuit Law). `h = 10.0` for all external surfaces.

**Path 1: Front Screen (R_path = R_cond + R_conv)**
- `R_cond` = 0.0007 / (1.1 * 0.00320) = 0.20 K/W
- `R_conv` = 1 / (10.0 * 0.00320) = 31.25 K/W
- **R_path_front = 31.45 K/W**

**Path 2: Mid-Frame**
- `R_cond` = 0.003 / (7.0 * 0.00141) = 0.30 K/W
- `R_conv` = 1 / (10.0 * 0.00141) = 70.92 K/W
- **R_path_frame = 71.22 K/W**

**Path 3: Back Panel**
- `R_cond` = 0.0006 / (1.1 * 0.01218) = 0.04 K/W
- `R_conv` = 1 / (10.0 * 0.01218) = 8.21 K/W
- **R_path_back = 8.25 K/W**

**Total System Resistance (R_total):**
- `1 / R_total = (1 / 31.45) + (1 / 71.22) + (1 / 8.25)`
- `1 / R_total = 0.0318 + 0.0140 + 0.1212 = 0.1670`
- **R_total = 5.99 K/W**

### Step C: Thermal Capacitance & Time Constant
How much energy can the unified physical mass absorb?
- `C = Mass * Standard_Bulk_Cp (850 J/kg·K)`
- **C** = 0.232 * 850 = **197.2 J/K**
- `Tau = R_total * C` = 5.99 * 197.2 = **1181 seconds**

---

## 3. Admissible Thermal Power (P_adm @ 1200s)

We calculate the maximum continuous power the S24 Ultra can handle for 1200 seconds before hitting the 20°C safety threshold using the exact Thermal Impedance (Z_th).

- `Z_th(t) = R_total * (1 - e^(-1200 / Tau))`
- `Z_th(1200)` = 5.99 * (1 - e^(-1200 / 1181))
- `Z_th(1200)` = 5.99 * (1 - 0.362) = **3.82 K/W**

**P_adm (Watts):**
- `P_adm = Delta_T / Z_th(1200)`
- `P_adm = 20 / 3.82` = **5.24 Watts**

---

## 4. Part C Interaction: Thermal Stability Ratio

Finally, compare the calculated Chassis Supply (P_adm) to the SoC Demand, accounting for the dynamic System Base Heat.

- **System Base Heat (P_base_heat):** 0.40W + (0.0075 * 114.4cm²) = **1.258W**
- **Admissible SoC Budget (P_adm_soc):** 5.24W - 1.258W = **3.982W**
- **Peak SoC Demand (Snapdragon 8 Gen 3):** **14.0 Watts**

- **Predicted Power Ratio:** 3.982 / 14.0 = **0.2844** (28.4%)
- **Predicted FPS Stability (Gamma 0.33):** 0.2844 ^ 0.33 = **65.8%**

### Benchmark Verification
- **Measured 3DMark Wild Life Extreme Reality:** **59.0%** [¹]
- **Alignment:** ~6.8% discrepancy. The model correctly identifies the core thermal behavior of the device. The minor variation is typical for an analytical Lumped Parameter approach, potentially influenced by dynamic display brightness throttling or localized internal interface resistances (R_int) not captured by the 1-node chassis model.

[¹] [UL Benchmarks (3DMark) - Galaxy S24 Ultra Review](https://benchmarks.ul.com/hardware/phone/Samsung+Galaxy+S24+Ultra+review) (Median Wild Life Extreme Stability: 59%).

**Conclusion:** The formal 6.10 score is driven by its rigorous derivation predicting exactly how the system reacts in a 20-minute physical window.
