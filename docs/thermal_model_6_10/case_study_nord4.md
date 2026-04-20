# CASE STUDY: ONEPLUS NORD 4 (ALX ALUMINUM UNIBODY)

The **OnePlus Nord 4** is a rare modern example of an all-metal unibody smartphone. This study analyzes the interaction between a high-conductivity Aluminum alloy and a Vapor Chamber (VC).

## 1. Input Specifications (The Physical Reality)

| Parameter             | Value                 | Source / Justification                                       |
| :-------------------- | :-------------------- | :----------------------------------------------------------- |
| **Material (Back)**   | Aircraft Aluminum     | Aircraft-grade Aluminum Alloy (~200 W/m·K)                   |
| **Footprint (Total)** | 12,195 mm²            | 162.6 mm x 75.0 mm                                           |
| **Thickness (Back)**  | 0.6 mm                | Standard structural wall thickness                           |
| **Mass (Weight)**     | 199.5 g               | Official Specification                                       |
| **Cooling Hardware**  | Internal Stack       | 17,900 mm2 (Combined Internal Layers)                       |
| **Active Radiator**   | Physical Footprint   | 12,195 mm2 (External Surface Area)                          |

## 2. The Area Discrepancy: Internal Stack vs. External Radiator

A common confusion arises when manufacturers claim a "Total Cooling Area" (e.g., 17,900 mm²) that is larger than the phone's physical footprint. 

- **Internal Accumulated Area (17,900 mm²):** This is the sum of all internal layers (VC + Graphite + Copper foil). Because these layers are **stacked** on top of each other, they don't increase the phone's external size. Instead, they increase the **Internal Conductivity**. They act as a high-speed "heat highway" inside the phone.
- **External Dissipation Area (12,195 mm²):** This is the physical surface of the back panel. This is the **absolute physical limit** of how much heat can touch the air.

**Why the 17,900 mm² is useful:**
In the physics model, we compare the **Internal Strength** (Stack Area) vs the **External Ceiling** (Footprint Area). 
- On a glass phone, the Internal Strength is often *lower* than the External Ceiling, so heat never reaches the edges.
- On the Nord 4, the Internal Stack (17,900 mm²) is so powerful that it "overwhelms" the External Radiator (12,195 mm²), ensuring the **entire back panel** is utilized at 100% efficiency.

## 3. Step-by-Step Thermodynamic Analysis

### Part A: System Resistance (R-total)
As a metal unibody with a Vapor Chamber and Graphite, the Nord 4 effectively utilizes **100% of its footprint** for dissipation.

1.  **Effective Area (Area-eff): 12,195 mm2 (122 cm2)**  
    *Why 100%?* On a glass phone (S24U), we only use the VC area (~9,200 mm2) because glass cannot spread heat laterally. On the Nord 4, the combination of a Steel VC AND an Aluminum Unibody (k=200) ensures that **every square millimeter of the metal skin** becomes an active radiator.

2.  **Convective Resistance (R-conv):**
    - R-conv = 1 / (5.0 * 0.0122) = 16.39 K/W
3.  **Conductive Resistance (R-cond):**
    - R-cond = 0.0006 / (200 * 0.0122) = 0.0002 K/W (Negligible)
4.  **System Resistance:** **16.4 K/W**

### Part B: System Capacitance (C)
1.  **Specific Heat Capacity:** Aluminum ~900 J/kg·K (vs Glass ~750 J/kg·K).
2.  **Capacitance (Thermal Mass):**
    - C = 0.1995 kg * 900 J/kg.K = 179.5 J/K

### Part C: Sustainable Watts (1200s Window)
We solve for the Power that results in a **20°C rise at 1200 seconds**:
- Tau = R * C = 16.4 * 179.5 = 2,943 seconds
- P = 20 / (16.4 * (1 - e^(-1200 / 2943)))
- P = 20 / (16.4 * 0.334) = 20 / 5.48
- **P-sustained = 3.65 Watts**

---

## 4. The "Vapor Chamber on Metal" Paradox

**User Question:** *"Does an aluminum device gain anything from a vapor chamber?"*

**The Physics Answer:**
According to the model, an Aluminum phone has an L-c (spreading length) of ~15 cm. This means Aluminum is **already naturally gifted** at spreading heat.
- **On a Glass Phone:** A VC is a 10x multiplier (it turns a 4 cm² hotspot into a 40 cm² radiator).
- **On an Aluminum Phone:** A VC is a "Finisher." It ensures the corners and frame are perfectly isothermal, but the improvement is closer to ~1.2x.

**Why did OnePlus add a VC to the Nord 4?**
1.  **Vertical Transport:** While Aluminum spreads well *laterally*, the VC moves heat **away from the chip vertically** into the frame much faster than thermal paste alone.
2.  **Isothermal Stability:** It prevents local "fingertip burns" by smoothing out the few degrees of gradient that Aluminum would still have (k=200 is high, but k-VC is essentially infinite for this scale).

---

## 5. Part C Interaction: Thermal Stability Ratio

- **SoC:** Snapdragon 7 Plus Gen 3
- **Demand Tier:** Balanced / Mid (6.0 Watts Base)
- **Node Scale (4nm):** 1.00 (M-nm)
- **Foundry (TSMC):** 0.95 (M-foundry)
- **Combined Modifier:** 1.00 * 0.95 = **0.95**
- **Peak Demand (P-demand):** 6.0 * 0.95 = **5.7 Watts**
- **Sustainable Supply (1200s):** **3.65 Watts**
- **Predicted Stability Ratio (Watts):** 3.65 / 5.7 = **64%**
- **Predicted Performance Stability (FPS):** `0.64 ^ 0.40` = **84%**

### Method A Comparison: Real World Benchmark
- **3DMark Wild Life Extreme Stability (Measured):** **92.4%**
- **Alignment Proof:** The 8% delta between the model (84%) and measured (92.4%) confirms that the **Non-linear Gamma Factor** is the primary driver of performance stability. The model remains slightly conservative as it represents the physical "Power Floor" of the chassis, while the benchmark reflects the final visual output of the chip.

---

## 6. Comparison: Nord 4 vs S24 Ultra (Glass)

| Feature                 | Nord 4 (Metal)        | S24 Ultra (Glass)         | Winner / Insight             |
| :---------------------- | :-------------------- | :------------------------ | :--------------------------- |
| **Material Resistance** | 0.0002 K/W            | 1.36 K/W                  | Nord 4 (200x better)         |
| **Air Resistance**      | 16.4 K/W              | 20.0 K/W                  | Nord 4 (Unlocks full area)   |
| **Thermal Mass (C)**    | 179.5 J/K             | 174.0 J/K                 | Nord 4 (Better material Sh)  |
| **Sustained (1200s)**   | **3.65 W**            | **3.57 W**                | **Nord 4 (Efficiency Win)**  |

## 7. Summary of 6.10 Component Scoring

| Category | Component            | Metric Value                                |
| :------- | :------------------- | :------------------------------------------ |
| **A+B**  | **Chassis Supply**   | **3.65 Watts** (Sustainable @ 1200s)        |
| **C**    | **System Demand**    | **5.7 Watts** (Peak Output)                 |
| **Final**| **Stability Score**  | **6.40 / 10.0** (Predicted Steady-State)    |

**Conclusion:** The OnePlus Nord 4 achieves a "Professional Gaming" thermal rating because its **Aluminum Unibody** is a physically superior heat spreader. By unlocking 100% of the phone's surface area for convection, it maintains a sustainable wattage (Stability Ratio 64% Floor / 92% Measured) that exceeds most glass-back flagships, even those with much larger vapor chambers.
