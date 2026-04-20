# TECHNICAL GUIDE: INTERNAL SPREADING EFFICIENCY (PART B)

This document defines the mathematical mapping for Section 6.10 Part B. It explains how internal cooling hardware translates from marketing terminology into the variables of the **Transient RC Model**.

---

## 1. The Interaction Matrix (Part A + Part B)

The **Efficiency Factor (Beta)** is not a fixed number for each technology. It is a **synergistic result** of the internal spreader and the external radiator material. 

### Spreading Efficiency Matrix (Beta)

| Internal Technology (Part B)| **Insulating Back** (Glass/Polymer) | **Conductive Back** (Metal Unibody) |
| :-------------------------- | :---------------------------------- | :---------------------------------- |
| **None (SoC Only)**         | 0.05 (Hotspot: 4 cm2)               | **0.60** (Inherent Metal Spread)    |
| **Standard Graphite**       | 0.25 (Spreading: ~30 cm2)           | **0.80** (High utilization)         |
| **Vapor Chamber (Medium)**  | 0.70 (Limited to VC area)           | **0.95** (Near-complete isothermal) |
| **Vapor Chamber (XL)**      | 0.90 (Large footprint)              | **1.00** (Full-body radiator)       |
| **Active Fan (Max)**        | **1.00** (Active bypass)            | **1.00** (Active bypass)            |

---

## 2. Master Model Integration Guide

The model solves for **Sustainable Watts** by mapping cooling solutions to three core system variables:

### A. Built-in Internal Fan
- **Variable Modified:** h (Convection)
- **Mathematical Impact:** Increases h from 5.0 to 15.0 - 25.0.
- **Example Logic:** Forced air movement slashes convective air resistance by up to 80%.

### B. Vapor Chamber
- **Variable Modified:** Area-eff (Beta)
- **Mathematical Impact:** Increases the Spreading Coefficient (Beta).
- **Example Logic:** Maximizes the active surface of the external radiator.

### C. Graphite / Graphene
- **Variable Modified:** Area-eff (Beta)
- **Mathematical Impact:** Moderate Beta increase (Material dependent).
- **Example Logic:** Graphene maintains higher average edge temperatures.

### D. Phase Change Materials (PCM)
- **Variable Modified:** C (Capacitance)
- **Mathematical Impact:** Increases C temporarily (Latent Heat).
- **Example Logic:** Absorbs power spikes without temperature rise until the wax melts.

### E. Metal Unibody
- **Variable Modified:** R-cond and Beta
- **Mathematical Impact:** Reduces material resistance and boosts Base Beta.
- **Example Logic:** Aluminum removes the "hotspot" bottleneck by default.

---

## 3. Why Material Matters (The Physical Reason)

- **Scenario A: Glass Back + No VC**: Glass is a thermal insulator. Heat cannot travel sideways through it. Without an internal spreader, the heat remains trapped in a **4 cm² pinpoint** exactly where the chip touches the glass.
- **Scenario B: Aluminum Back + No VC**: Aluminum is a thermal conductor. Even without a dedicated Vapor Chamber, the metal atoms themselves carry the heat sideways. According to **Fin Theory**, a standard aluminum back has a spreading length (Lc) of ~15 cm, meaning it naturally uses **~60-70% of the phone's area** without any help.

**Rule for Scoring Agent:** When evaluating a phone's thermal capacity, always cross-reference the Part B tech with the Part A material listed in Section 6.10 A1.2.

---

## 4. Physical Integration Equations

The Section 6.10 model calculates the system state using three primary physical vectors. Each internal solution maps to one or more of these vectors:

### Vector 1: Convection (h) — The Active Gate
- **Formula:** `R-air = 1 / (h * Area-eff)`
- **Integration:**
  - `IF (Internal-Fan == True)` -> `h = h-base + h-active` (e.g. 5.0 + 20.0 = 25.0)
  - `IF (External-Accessory == True)` -> `h` is updated in the **Booster Layer** (Section 11) only.

### Vector 2: Spreading (Beta) — The Surface Window
- **Formula:** `Area-eff = Footprint * Beta`
- **Integration:**
  - `Beta = Base-Beta (Material) + Spreader-Bonus (VC/Graphite)`
  - **Metal (Aluminum) Base-Beta:** 0.60
  - **Glass Base-Beta:** 0.05
  - **Spreader-Bonus:** XL VC (+0.40), Med VC (+0.25), Graphite (+0.10).
  - *Constraint:* `Beta` is capped at 1.00.

### Vector 3: Capacitance (C) — The Thermal Sponge
- **Formula:** `C-total = (Mass * Cp) + C-latent`
- **Integration:**
  - **Sensible Heat (Mass):** Standard 800 J/kg.K.
  - **Latent Heat (PCM):** `C-latent` (J/K) is added based on the specific heat of fusion of the internal PCM sleeve. This allows for longer stability *before* reaching the 20°C limit.

---

## 5. Advanced & "Forgotten" Technologies

### A. Active Cooling (Internal vs. External Fans)

There are two distinct types of active cooling that affect the model differently:

1.  **Built-in Internal Fans (The "Active" Score):**
    - **Description:** A physical fan integrated *inside* the phone's chassis with dedicated air intake and exhaust vents (e.g., **Nubia RedMagic** series).
    - **Model Impact:** This is a permanent hardware feature. It modifies the **Convection Coefficient (h)** from 5.0 (natural) to ~25.0 (forced).
    - **Scoring:** This contributes directly to the **Section 6.10 base score**.

2.  **External Cooling Accessories (The "Booster"):**
    - **Description:** Clip-on fans or Peltier coolers sold separately or as accessories (e.g., **Asus ROG AeroActive Cooler**).
    - **Model Impact:** These are NOT permanent parts of the phone. They are treated as **Thermal Boosters** in Section 11.
    - **Scoring:** They do not affect the 6.10 Base Score, but they allow the phone to reach its "Peak Stability" during benchmark/gaming sessions when the accessory is attached.

- **Example (Internal):** Nubia RedMagic 9S Pro (Continuous 20,000 RPM fan).
- **Example (External):** Asus ROG Phone 8 (Requires the AeroActive Cooler X for max stability).

### B. Phase Change Materials (PCM / Wax Sleeves)
PCMs absorb heat by melting at a specific temperature (e.g., 40°C).
- **Model Impact:** Periodically increases **Capacitance (C)**.
- **Mapping:** During the "melting window," the device behaves as if its mass is 5x higher (Latent Heat of Fusion).
- **Caveat:** Once the wax is melted, the benefit is 0. This is "Burstable" efficiency, not "Sustained."
- **Example:** High-reliability industrial handhelds / specialized thermal cases.

### C. Graphene & Dual-Layer Graphite
Graphene has in-plane conductivity up to 5000 W/m.K (vs 1500 for Graphite).
- **Model Impact:** Increases the **Isothermal Uniformity** of the Active Window.
- **Clarification:** While 80% Area-eff is a static measurement, **Graphene** ensures that the temperature gradient across that 80% is nearly flat. 
- **The Result:** A perfectly isothermal 80% area dissipates more heat than a "peaked" 80% area because the average surface temperature is higher. It also reduces "Thermal Lag," moving heat from the chip to the radiator edges 3x faster than standard graphite.
- **Example:** Xiaomi 13 Ultra (Dual Graphite/Graphene stack).

### D. Loop LiquidCool (Oscillating Heat Pipes)
Uses a separate vapor and liquid line to avoid "counter-current" friction found in standard VCs.
- **Model Impact:** Reduces **Internal Resistance (R-internal)** and allows for longer spreading distances without "dry-out."
- **Result:** Beta remains at 0.95+ even during 20W+ peak loads.
- **Example:** Xiaomi 14 Ultra.

### E. Radiator Expansion (Screen & Frame Dissipation)

Some manufacturers use secondary paths to move heat away from the core:

1.  **Display-Side Graphite:** A secondary layer under the OLED panel that dumps heat through the phone's front.
    - **Model Impact:** Effectively adds a second "Active Radiator" in parallel.
    - **Integration:** The `Area-eff` is increased by a factory (e.g., +20% footprint) to reflect the front-facing heat flux.
2.  **Chassis-Frame Bridge:** Thermal putty/pads bridging the SoC directly to the side rails.
    - **Model Impact:** Increases the "Fin Efficiency" of the metal frame.
    - **Integration:** Reduces `R-total` by providing a low-resistance path to the perimeter of the device.

---

## 6. Logical Constraints & Rules

1.  **The Footprint Ceiling:** `Area-eff` can never exceed the physical surface area of the device back (Footprint). Internal "Total Areas" (e.g. 17,900 mm2) are stacked-area multipliers for internal conductivity, not external dissipation.
2.  **Insulation Penalty:** If a device uses a **Thermal Barrier** (e.g., Aerogel/Plastic spacer) to protect the user's hand, this adds a **Penalty Resistance** to the Conductive path.
    - R-total = R-cond + R-conv + R-barrier.
3.  **Active Bonus:** If a phone has a fan, the model calculates P-sustained twice: once for h = 5 (Fan Off) and once for h = 25 (Fan Max). This shows the quantifiable benefit of active cooling.
