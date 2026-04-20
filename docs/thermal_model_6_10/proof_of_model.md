# DEEP DIVE: TRANSIENT THERMODYNAMIC ANALYSIS (RC MODEL)

To answer your exact question: **"where does that 4 cm² hotspot come from?"**

This is the most critical part of the model. It represents the **Characteristic Spreading Length**—the physical distance heat can travel through a material before it is "defeated" by air convection.

Here is the A to Z physics derivation using **Fin Theory**.

---

### Step 1: Characteristic Spreading Length (L-c)

Heat in a smartphone back panel has two choices:
1.  **Conduction:** Move sideways through the material (k).
2.  **Convection:** Jump into the air (h).

The parameter `m = (h / (k * t))^0.5` defines the decay of temperature as you move away from the chip. The inverse of this, `L-c = (k * t / h)^0.5`, is the **Characteristic Spreading Length**. 

This length tells us how far the heat travels before the temperature drops to a point where it is effectively ambient.

---

### Step 2: Comparison for 0.6mm Materials

We use standard air convection `h = 5.0 W/m²·K` and thickness `t = 0.0006 m`.

#### A. Glass (The Hotspot)
*   **Conductivity (k):** 1.1 W/m·K
*   `L-c = (1.1 * 0.0006 / 5.0)^0.5 = (0.000132)^0.5 = 0.0115 meters (1.15 cm)`
*   **Effective Area:** A circle with radius L-c.
    `Area = pi * (L-c)^2 = 3.14 * (0.0115)^2 = 0.00041 m² (4.1 cm²)`
*   **Physical Meaning:** Because glass is an insulator, the heat "gives up" after traveling only 1.15 cm. It creates a small, intense **4 cm² hotspot** directly over the chip. The rest of the phone is cold and useless for cooling.

#### B. Aluminum (The Radiator)
*   **Conductivity (k):** 200 W/m·K
*   `L-c = (200 * 0.0006 / 5.0)^0.5 = (0.024)^0.5 = 0.155 meters (15.5 cm)`
*   **Effective Area:** `pi * (0.155)^2 = 0.075 m² (750 cm²)`
*   **Constraint:** Since the total back of a phone is only ~150 cm², the aluminum easily covers the **Entire Device Area**.
*   **Physical Meaning:** Aluminum is so conductive that the heat spreads across the entire back panel instantly. The entire phone becomes a single active radiator.

---

---

### Step 3: Dimensional Analysis (Why "Area" is Mandatory)

To answer the technical query: **"Why add an area to the resistance formula?"**

Normally, we think of thermal resistance in terms of **Material Flux** (R''), which has units of m2 . K/W.
- `R'' = Thickness / Conductivity` (m2 . K/W)

However, to solve the **Differential Equation** for a device, we need the **Total Thermal Resistance** (R) in units of **Kelvin per Watt (K/W)**. 
Watts (W) is energy per second. Without the area (A), you cannot know how many Watts are flowing.

#### The Conductive Resistance (R-cond)
For heat to move *through* the back panel:
> **R-cond = Thickness / (k * Area-eff)**

Units Check: meter / ( (W/m.K) * m2 ) = meter / (W.m / K) = K/W. (Correct)

#### The Convective Resistance (R-conv)
For heat to leave the chassis to the air:
> **R-conv = 1 / (h * Area-eff)**

Units Check: 1 / ( (W/m2.K) * m2 ) = 1 / (W/K) = K/W. (Correct)

#### Total System Resistance (R-total)
The heat must do both: move through the glass, then into the air. 
`R-total = R-cond + R-conv`

**Why Area-eff dictates the score:**
If you have a 4 cm2 hotspot (Glass), your Area-eff is 0.0004 m2.
- R-cond approx 1.3 K/W
- R-conv approx 500.0 K/W (The bottleneck!)
- **Total Resistance: 501.3 K/W**

If you have a metal unibody spread across 150 cm2:
- **Total Resistance: 13.3 K/W**

**Conclusion:** The presence of Area-eff in the denominator is not a "modification"; it is a dimensional requirement to convert **Material Properties** (Conductivity) into **System Performance** (Temperature rise per Watt).

---

### Step 4: The Transient ODE (The 600s Test)

Heat generation, storage (Capacitance), and dissipation happen simultaneously. The temperature rise over time is:
`Delta-T(time) = (Power * Resistance) * (1 - e^(-time / (Resistance * Capacitance)))`

#### Sustained Power Threshold (The Score)
If we set the limit to a **20°C rise** and the time to **600 seconds**:
`Sustainable-Watts = 20 / (Resistance * (1 - e^(-600 / (Resistance * Capacitance))))`

1.  **Aluminum:** Because its Resistance is only 13.3 K/W, it can handle **~1.7 Watts** for 10 minutes.
2.  **Glass:** Because its Resistance is 487 K/W, it hits 20°C almost instantly. To stay safe, the chip must throttle down to **~0.04 Watts**.

### Conclusion
The **4 cm² hotspot** is the reason glass phones feel hot but don't cool down. The heat is physically unable to reach the rest of the surface. By moving to **Sustainable Watts**, we capture this "area bottleneck" in a single, rigorous physical metric.
