# Comprehensive Smartphone Scoring Rules (v8.0) - Let's build the Golden Standard together

This document provides **exhaustive, unit-specific reference tables** for every technical criterion found in the v4.0 Data Structure.
*   **Principle:** Every single data point that differentiates a product must have a corresponding score.
*   **Normalization:** 0 = Worst/Obsolete, 10 = Best/State-of-the-Art.
*   **Units:** All criteria include specific units of measurement.

> **All numerical thresholds and boundary values referenced in this document are defined in [scoring_constants.md].**

> [!CAUTION]
> **Presence Floor Rule (General Scoring Principle)**
> When a subsection uses a **Binary Gate** (feature present / absent) and a scored parameter can be measured on **both sides** of the gate, the **best-performing value from the lower class** (feature absent) must be used as the **0-score floor** for the upper class (feature present).
>
> **Rationale:** Without this rule, the normalization rule leads to score a 0 for the worst phone having the feature — the same as phones without the feature at all. This fails to reward the phone for having the feature, even in its weakest form. The floor ensures that the scoring range for the upper class begins where the lower class's capability ends, so any device with the feature always scores meaningfully above one without it.
>
> **Example:** §4.5.2 Ultrawide Field of View uses `Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max` (≈ 85°) as its 0-score floor, because 85° is the best FOV achievable by a phone without an ultrawide lens (i.e., the main camera only). Any ultrawide delivering more than 85° scores > 0.


## 🟣 1. Design & Build Quality

### 🔹 1.1 Materials (Frame/Back)
*Description:* The physical materials used for the device chassis and rear panel. Affects how premium the phone feels and how well it resists drops.

> [!IMPORTANT]
> **Thermal Properties Not Scored Here:** While materials technically dictate thermal conductivity, a device's thermal capacity and heat dissipation are explicitly scored in **Section 6.10 (TDSI)** and factored into **Section 8.1 (Battery)**. To avoid double-scoring, this section strictly evaluates structural integrity, durability, and premium tactile quality.

*   **Measurement:** Manufacturer specifications and teardown confirmation.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Determines structural integrity, premium tactile quality, and physical durability.

**Predicted Score Formula:**
`Materials Score = (0.6 * Frame Material Score) + (0.4 * Back Material Score)`

> [!NOTE]
> **Why the distinct methodologies? (Structural vs. Surface Engineering)**
> The frame and back panel serve fundamentally different mechanical roles, necessitating two unique physics-based models:
> 1.  **Frame (Structural Chassis):** Acts as the device's "spine." It must resist external loads and maintain structural alignment. Consequently, the **Structural Merit Index** prioritize properties that prevent the device from staying bent forever or "creaking" under pressure: **Yield Strength** (measured in Megapascals or MPa) and **Young's Modulus** (Rigidity, measured in Gigapascals or GPa).
> 2.  **Back Panel (Surface Claddding):** Acts as the "skin." It must protect internals from impact and the exterior from wear. The **Surface Merit Index** prioritize properties that prevent aesthetic and safety failure: **Vickers Hardness** (HV, resistance to scratches) and **Fracture Toughness** (resistance to crack propagation and shattering).
> 
> A "homogenized" single formula would be technically inaccurate; for example, a metal frame is "fail-safe" because it is tough (it bends rather than breaks), while a glass back is "premium" because it is hard (it resists scratches until it reaches its fracture limit). Separating these ensures the final score accurately reflects the engineering reality of each component.

#### 1.1.A Frame Material (Structural Class)
*   **Measurement:** Material of the structural chassis frame as declared in manufacturer specifications.
*   **Unit:** Material Class
*   **Significance:** Evaluates the device's **Structural Rigidity**, **Tactile Premiumness**, and **Long-term Durability**. High-strength alloys that resist bending and offer a high-density hand-feel are prioritized for their engineering excellence and perceived value.

| **Frame Material Class**     | **Score** |
| :--------------------------- | :-------- |
| **Amorphous Alloy**          | **10.00** |
| **Specialized Ceramic**      | **9.46**  |
| **Titanium Alloy**           | **8.80**  |
| **7000 Series Aluminum**     | **7.40**  |
| **Stainless Steel**          | **7.17**  |
| **6000 Series Aluminum**     | **6.45**  |
| **Zinc Alloy (Zamak 3)**     | **5.80**  |
| **Die-Cast Aluminum (ADC12)**| **5.05**  |
| **Magnesium Alloy**          | **4.97**  |
| **Reinforced Polymer**       | **3.68**  |
| **High-Performance Polymer** | **1.16**  |
| **Standard Polymer**         | **0.00**  |
| **Material Not Disclosed**   | **0.00**  |

**Note:** For detailed material identification guidelines and mandatory **Ambiguity Resolution Rules** (e.g., Metal Default, Marketing Finishes vs. Core Materials), refer to the operational documentation in [proposed_data_structure.md].

**Why these scores? (Engineering Justification):**
Scores are derived from a **Structural Merit Index (StMI)** (calculated as 70% Strength + 30% Rigidity), where "Strength" is the Yield Strength (resistance to permanent dents) and "Rigidity" is the Young's Modulus (resistance to elastic bending).
- **Amorphous Alloy (10.00)**: LiquidMetal/Vitreloy. The absolute physics ceiling for structural frames, offering the highest combined elastic limit (~1900 MPa) and rigidity.
- **Specialized Ceramic (9.46)**: Zirconia (ZrO2). Possesses extreme rigidity (210 GPa) and high compressive yield, though brittle, its structural resistance to frame-warping is superior to crystalline alloys.
- **Titanium Alloy (8.80)**: Grade 5. The premium standard, offering peak yield strength for industrial alloys (~900 MPa), ensuring the frame never "takes a set" from accidental bending.
- **7000 Series Aluminum (7.40)**: Aerospace-grade yield (~505 MPa) makes it significantly more resilient to permanent dents than standard alloys.
- **Stainless Steel (7.17)**: Offers a very high rigidity (193 GPa), providing a "rock-solid" feel. However, it scores lower than 7000-Al because its **Yield Strength** (~290 MPa) is lower than that of high-end aluminum alloys, meaning it undergoes permanent deformation (bending) at lower force thresholds.
- **6000 Series Aluminum (6.45)**: The industry structural baseline (Yield ~300 MPa).
- **Zinc Alloy (Zamak 3) (5.80)**: High-density die-cast alloy (Yield ~200 MPa). Primarily used for side-rails in ruggedized devices (e.g., Ulefone Armor series) due to its excellent damping capacity and high density, providing a "solid" hand-feel. However, it is structurally inferior to 6000/7000 series aluminum extrusions, possessing lower absolute yield strength and fracture toughness, necessitating bulkier designs for equivalent structural integrity.
- **Die-Cast Aluminum (ADC12) (5.05)**: The ubiquitous default for unbranded "Metal" or "Aluminum" claims. While offering lower yield strength (~160 MPa) than 6000-series extrusions, it represents the physical reality of the vast majority of mid-range cast chassis.
- **Magnesium Alloy (4.97)**: AZ91D. High strength-to-weight ratio, but penalized by low absolute rigidity (~45 GPa), causing significantly more elastic deflection under load compared to aluminum or steel.
- **Reinforced Polymer (3.68)**: Engineering composites (Glass-fiber PA) that bridge the gap between plastics and metals.
- **High-Performance / Standard Polymer (1.16–0.00)**: Commodity and technical resins with low structural load-bearing capacity.

**Data Sources:** ASTM Standard Alloy datasheets; MatWeb Material Property Database; ASM International Aluminum Database.

> [!IMPORTANT]
> **Cross-Reference: Thermal Scoring Synergy**
> The frame material selected here is also used as the primary input for **Section 6.10 (Part A1: Thermal Conductivity Class)**. However, the scoring logic is fundamentally different: Section 1.1.A rewards **structural rigidity and tactile premiumness**, whereas Section 6.10 rewards **thermal conductivity and soak capacity**. Consequently, any update or addition to the frame material list MUST be synchronized across both sections to maintain architectural integrity.

#### 1.1.B Back Panel Material (Surface Class)
*   **Measurement:** Manufacturer specifications and teardown confirmation.
*   **Unit:** Material Class
*   **Significance:** Evaluates the device's **Surface Hardness**, **Shatter Resistance**, and **Tactile Premiumness**. This section prioritizes materials that offer the best balance of aesthetic longevity (scratch resistance) and high-impact resilience (fracture toughness).

| **Back Material Class**      | **Score** |
| :----------------------------| :-------- |
| **Specialized Ceramic**      | **10.00** |
| **Stainless Steel**          | **9.10**  |
| **7000 Series Aluminum**     | **8.55**  |
| **6000 Series Aluminum**     | **8.33**  |
| **Zinc Alloy (Zamak 3)**     | **8.25**  |
| **Die-Cast Aluminum (ADC12)**| **8.20**  |
| **Armor-Class Glass**        | **6.41**  |
| **Shield-Class Glass**       | **6.25**  |
| **Reinforced Glass**         | **6.00**  |
| **Reinforced Polymer**       | **5.03**  |
| **Flexible Membrane**        | **4.02**  |
| **Standard Glass**           | **3.08**  |
| **Composite Sheet**          | **2.85**  |
| **High-Performance Polymer** | **2.74**  |
| **Standard Polymer**         | **0.00**  |
| **Material Not Disclosed**   | **0.00**  |

**Note:** For detailed material identification guidelines and mandatory **Ambiguity Resolution Rules** refer to the operational documentation in [proposed_data_structure.md].

**Why these scores? (Surface Merit Index):**
The Surface Merit Index is calculated as a balanced logarithmic average of two key physical properties:
1. **Hardness (50% weight):** Resistance to permanent plastic deformation (scratches); calculated as the normalized logarithmic value of the material's Vickers Hardness.
2. **Fracture Toughness (50% weight):** Resistance to unstable crack propagation (shattering); calculated as the normalized logarithmic value of the material's Fracture Toughness.

- **Specialized Ceramic (10.00)**: Zirconia/Alumina. The ultimate surface material, providing high-end scratch resistance (>1200 HV) and superior toughness to glass.
- **Stainless Steel (9.10)**: Based on the Surface Merit Index (SMI), surgical-grade steel (~200 HV) is strictly superior to all aluminum alloys in both hardness and fracture toughness (125 MPa·m^0.5), making it physically impossible to shatter while offering superior scratch resistance.
- **7000 / 6000 Aluminum (8.55–8.33)**: While softer than glass, metals are "fail-safe" due to extreme toughness. They simply do not shatter, making them a superior choice for drop-protection survival. Verified high-grade alloys.
- **Zinc Alloy (Zamak 3) (8.25)**: Precision-cast alloy used for high-impact back-cladding or structural modules in rugged devices. While it offers superior impact resilience (shatter resistance) compared to all glasses, its lower surface hardness (~82 HV) and high density make it less efficient for premium flagship designs than aluminum alloys.
- **Die-Cast Aluminum (ADC12) (8.20)**: Default for unbranded "Metal", "Aluminum", or "Metal Unibody" claims. While physically robust, it lacks the explicit alloying of 7000-series or the hardness of Stainless Steel, serving as the conservative baseline for generic metallic backs.
- **Armor-Class Glass (6.41)**: The scratch-resistance peak for glass surfaces (Ref: Gorilla Armor). Its composition achieves a Vickers Hardness of 750 HV, outperforming Shield-Class (670 HV). While its absolute toughness is slightly lower than Shield-Class, its superior resilience against micro-abrasions secures its 6.41 tier.
- **Shield-Class Glass (6.25)**: The impact-optimized flagship tier (Ref: Victus 2, Kunlun 2). It provides a ~38% leap in fracture toughness (1.05 MPa·m^0.5) over baseline Reinforced variants (0.76 MPa·m^0.5). While it offers the highest drop-protection in the glass category, it scores below Armor-Class (6.41) due to its lower audited surface hardness (670 HV vs 750 HV).
- **Reinforced Glass (6.00)**: The baseline flagship glass (Ref: Victus, Gorilla Glass 6). It serves as the industrial anchor with verified properties (640 HV / 0.76 MPa·m^0.5). It lacks the advanced reinforcement of Shield-Class but remains significantly superior to standard soda-lime glass in both hardness and toughness.
- **Reinforced Polymer (5.03)**: Technical composites (e.g., glass-fiber reinforced resins) that bridge the engineering gap between polymers and minerals. While significantly softer (~45 HV) than glass, its extreme fracture toughness (5.0 MPa·m^0.5) is ~7x higher than standard soda-lime glass, securing its 5.03 score by prioritizing shatter-resistance over mineral hardness.
- **Flexible Membrane (4.02)**: Vegan leather, silicone. A unique tactile class that outscores standard glass (3.08) by possessing "infinite" fracture toughness; it is physically impossible to shatter via drop impact, offsetting its negligible surface hardness in the overall merit index.
- **Standard Glass (3.08)**: Default for generic "Glass" with no verified generation. Represents standard **Soda-Lime glass**. Inherits the penalty-floor for fracture toughness compared to reinforced variants but remains structurally superior to polymers in surface hardness.
- **Composite Sheet (2.85)**: Multi-layer PC/Acrylic mimics. Offers a "glass-like" feel and superior fracture toughness (resistance to shattering) compared to standard glass, but is penalized for low surface hardness (scratch resistance).
- **High-Performance / Standard Polymer (2.74–0.00)**: Engineering and commodity plastics, serving as the durability baseline.

**Data Sources:** Corning Gorilla Glass Product Sheets; Schott AG Technical Glass Database; AGC Inc. Dragontrail Datasheets; *J. Mater. Res., Vol. 31, No. 19, 2016 (Fracture of chemically strengthened glass).*

> [!IMPORTANT]
> **Cross-Reference: Thermal Scoring Synergy**
> The back panel material selected here is also used as the primary input for **Section 6.10 (Part A1.2: Back Panel Thermal Interface)**. However, the scoring logic is fundamentally different: Section 1.1.B rewards **aesthetic longevity and impact resilience**, whereas Section 6.10 rewards **steady-state heat flux and thermal effusivity**. Consequently, any update or addition to the back material list MUST be synchronized across both sections to maintain architectural integrity.

### 🔹 1.2 Durability (Ingress Protection)
*Description:* Ingress Protection rating against dust and water. Dust and water resistance are tested separately under IEC 60529. A phone can be fully dust-sealed but weak against immersion, or vice versa. Treating them independently reflects the actual certification process and physical risks.
*   **Measurement:** Manufacturer IP certification (IEC 60529).
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for device longevity and accident protection.

**Predicted Score Formula:**
`IP Score = (0.5 * Dust Protection Score) + (0.5 * Water Protection Score)`

#### 1.2.A Dust Protection (First Digit of IP Code)
*   **Measurement:** Manufacturer IP certification.
*   **Unit:** IEC 60529 First Digit (0–6)
*   **Significance:** Determines resistance to fine particles that cause long-term mechanical and electrical wear (ports, speakers, buttons, seals).

| IEC Level | Score    | Objective Definition                                       |
| :-------- | :------- | :--------------------------------------------------------- |
| **6**     | **10.0** | Dust-tight — no ingress of dust under vacuum conditions    |
| **5**     | **8.0**  | Dust-protected — limited dust ingress, no harmful deposits |
| **4**     | **6.0**  | Protected against solid objects >1mm (wires, tools)        |
| **3**     | **4.0**  | Protected against solid objects >2.5mm                     |
| **2**     | **2.0**  | Protected against fingers only                             |
| **0–1**   | **0.0**  | No certified protection                                    |

#### 1.2.B Water Protection (Second Digit of IP Code)
*   **Measurement:** Manufacturer IP certification.
*   **Unit:** IEC 60529 Second Digit (0–9)
*   **Significance:** Determines resistance to splashes, rain, jets, and immersion accidents.

| IEC Level | Score    | Objective Definition                                               |
| :-------- | :------- | :------------------------------------------------------------------|
| **9**     | **10.0** | High-pressure, high-temperature water jets (IEC 60529 + ISO 20653) |
| **8**     | **9.0**  | Continuous immersion beyond 1m (manufacturer-defined depth/time)   |
| **7**     | **8.0**  | Immersion up to 1m for 30 minutes                                  |
| **6**     | **6.0**  | Powerful water jets                                                |
| **5**     | **4.0**  | Low-pressure water jets                                            |
| **4**     | **2.0**  | Splashing water                                                    |
| **0–3**   | **0.0**  | No certified protection                                            |

> [!NOTE]
> **Note on Level 9:** IEC 60529 does not define IPX9, but many manufacturers certify both IEC IP68 + ISO 20653 IPX9/9K. This model accepts 9 as a valid "extended water resistance" level when officially documented.

### 🔹 1.3 Display Glass Protection (DGP)
*Description:* Evaluates the protective glass generation used on the display, based on manufacturer-declared glass type and supplier performance class. Newer versions are much harder to crack or scratch when dropped.
*   **Measurement:** Front glass type (manufacturer specification).
*   **Unit:** Glass Protection Tier (0–10)
*   **Significance:** Indicates expected resistance to cracking and surface damage from drops and daily handling.

| Score    | Glass Protection Tier                          | Representative Examples                     |
| :------- | :--------------------------------------------- | :------------------------------------------ |
| **10.0** | **Armor-Class**                                | Gorilla Glass Armor                         |
| **9.5**  | **Shield-Class**                               | Ceramic Shield, Kunlun Glass                |
| **9.0**  | **Ultra-Reinforced**                           | Gorilla Glass Victus 2                      |
| **8.0**  | **Premium Reinforced**                         | Gorilla Glass Victus / Victus+, Star 2      |
| **7.0**  | **Standard Reinforced**                        | Gorilla Glass 5 / 6, Dragontrail Pro / Star |
| **5.0**  | **Entry-Level Reinforced**                     | Gorilla Glass 3, Panda Glass, Dragontrail   |
| **3.0**  | **Tempered Glass**                             | Basic chemically strengthened glass         |
| **2.0**  | **Glass (Unspecified)**                        | Generic glass                               |
| **0.0**  | **Plastic or No Glass**                        | Polymer display covers                      |

### Technical Category Definitions
*   **Armor-Class**: Anti-reflective (AR) coating + ≥2.0m rough-surface drop certification.
*   **Shield-Class**: Ceramic-infused matrix + ≥2.0m drop certification.
*   **Ultra-Reinforced**: Advanced glass optimized for rough-surface drops (≥2.0m class).
*   **Premium Reinforced**: High-end standard chemical tempering with ≥2.0m drop certification.
*   **Standard Reinforced**: Regular flagship-grade chemical tempering with ≥1.6m drop certification.
*   **Entry-Level Reinforced**: Basic chemical tempering with ~1.2m drop certification.


### 🔹 1.4 Ergonomics
*Description:* Evaluates the physical handling comfort and usability of the device based on its thickness and width. Thinner and narrower devices are easier to hold, fit better in pockets, and are more comfortable to operate single-handedly.
*   **Measurement:** Device Thickness (depth) and Width.
*   **Unit:** Composite Score (0.0–10.0)
*   **Significance:** Affects pocketability, hand grip, and one-handed accessibility.
*Formula:* `Score = (0.5 * Thickness_Score) + (0.5 * Width_Score)` (Clamped 0.0–10.0)
*   **Max Score (10.0):** Maximum score on both thickness and width.
*   **Min Score (0.0):** Minimum score on both thickness and width.

#### 1.4.A Thickness (Depth)
*Description:* Device thickness excluding camera bump. Thinner phones are easier to hold and fit better in pockets.
*   **Measurement:** Calipers at the thickest point of the body (excluding camera protrusion).
*   **Unit:** Millimeters (mm)
*   **Significance:** Affects pocketability and hand comfort.
*Formula:* `Score = 10 * ((Thickness_mm_Max - Thickness) / (Thickness_mm_Max - Thickness_mm_Min))` (Clamped 0.0–10.0)
*   **Max Score (10.0):** ≤ Thickness_mm_Min
*   **Min Score (0.0):** ≥ Thickness_mm_Max
> [!NOTE]
> **Why Linear?** The discomfort of carrying a thick phone (in a pocket or in the hand) increases by the same amount with each extra millimeter (mm). Think of it like a book: a 9 millimeters (mm) hardcover is noticeably thicker than an 8 millimeters (mm) one, and a 12 millimeters (mm) brick is noticeably thicker than an 11 millimeters (mm) one — the penalty is constant. There are no diminishing returns in the practical 6–12 millimeters (mm) smartphone range, so a straight linear scale is the most honest model.

#### 1.4.B Width & Handling (One-Handed Usability)
*Description:* Quantifies the ergonomic handling cost of phone width for one-handed use. Wider phones are harder to grip and operate single-handedly, with the discomfort accelerating beyond a critical threshold tied to human hand anatomy. Note: the positive benefit of a wider phone (bigger screen) is already captured in Section 2.9 (Screen Size) and Section 2.8 (Screen-to-Body Ratio).
*   **Measurement:** Device Width
*   **Unit:** Millimeters (mm)
*   **Significance:** Beyond a critical threshold (~75–77 millimeters (mm)), one-handed operation becomes difficult for a large share of users.
*Formula:* `Score = 10 * (1 - ((Width - Width_mm_Min) / (Width_mm_Max - Width_mm_Min))^2)` (Clamped 0.0–10.0)
*   **Max Score (10.0):** ≤ Width_mm_Min
*   **Min Score (0.0):** ≥ Width_mm_Max
> [!NOTE]
> **Why Quadratic (not Linear)?** Research into hand anthropometry shows that phone width comfort is **not a constant penalty per millimeter** — it has a real physical threshold.
>
> **The data:** Average female hand width is 79–83 millimeters; average male is 88–97 millimeters. Modern phones range from 67.3 millimeters (iPhone Special Edition (SE) 4th gen) to 79 millimeters (Galaxy S24 Ultra). This means:
> *   A phone under ~71 millimeters is comfortable for almost every user — a linear scale would unfairly apply the same per-millimeter penalty here as in the uncomfortable range.
> *   A phone crossing 75–77 millimeters starts causing grip adjustments for roughly 30% of users (most women and smaller-handed men).
> *   Beyond 78 millimeters, the majority of users rely on two hands for basic navigation — a steep penalty applies.
>
> **The math:** A quadratic formula `(1 - x²)` stays near 10 in the comfortable narrow range and drops steeply as width approaches the maximum, mirroring this threshold-based reality. A linear scale would naively assign the same cost to going from 68 millimeters to 69 millimeters as to going from 77 millimeters to 78 millimeters, which is factually wrong.
>
> **Real-phone reference scores** (Min = 67.3 millimeters, Max = 79.0 millimeters):
>
> | Phone              | Width  | Score    |
> | :----------------- | :----- | -------: |
> | iPhone SE 4th gen  | 67.3mm | **10.0** |
> | Galaxy S24         | 70.6mm |  **9.2** |
> | iPhone 16          | 71.5mm |  **8.7** |
> | Galaxy S24+        | 75.9mm |  **5.3** |
> | Galaxy S24 Ultra   | 79.0mm |  **0.0** |
>
> *Note: The Galaxy S24 Ultra scoring 0 on this specific metric is correct. Its large screen is already fully rewarded by Section 2.9 (Screen Size) and Section 2.8 (Screen-to-Body Ratio). This metric scores solely the ergonomic handling cost.*

### 🔹 1.5 Weight
*Description:* Total device weight. Lighter phones are more comfortable to hold for long periods (e.g., reading, watching videos) without wrist strain.
*   **Measurement:** Digital scale weight including battery.
*   **Unit:** Grams (g)
*   **Significance:** Determines long-term holding comfort and fatigue.
*Formula:* `Score = 10 * ((Weight_g_Max - Weight) / (Weight_g_Max - Weight_g_Min))` (Clamped 0.0–10.0)
*   **Max Score (10.0):** ≤ Weight_g_Min
*   **Min Score (0.0):** ≥ Weight_g_Max
> [!NOTE]
> **Why Linear?** Wrist and arm fatigue from holding a phone scales approximately proportionally with weight — the same way a 200 grams (g) book feels twice as heavy as a 100 grams (g) booklet after an extended reading session. Within the practical 130–250 grams (g) range that covers all modern smartphones, each additional gram (g) adds a constant ergonomic cost. No diminishing returns apply here.


## 🟣 2. Display

### 🔹 2.1 Display Panel Architecture (DPA)
*Description:* Scores **three hardware properties that no other Section 2 subsection captures**:
1.  **Contrast ratio and black level** — OLED pixels switch fully off for true black (infinite contrast). LCD backlights are always on, producing light leakage and finite contrast (~1000:1 for IPS). This determines visibility in dark scenes, night-mode legibility, and the hardware's ability to render Dolby Vision / HDR10 without a "grey black" floor. Note: §2.3 scores the *measured colour gamut*, §2.4 scores *HDR format certification* — neither scores whether the panel hardware can physically deliver true black.
2.  **Viewing angle colour stability** — TN LCD inverts colours beyond ~30°. IPS maintains acceptable accuracy. OLED maintains full colour accuracy at any angle. Not scored anywhere else in Section 2.
3.  **Local dimming granularity** — OLED achieves pixel-level local dimming with zero bloom. LCD relies on zone-based local dimming, creating a visible glow ("halo") around bright objects on dark backgrounds, especially during HDR playback.

**What §2.1 deliberately excludes (scored elsewhere, no double counting):**
*   **Brightness in nits** → §2.2 scores actual measured peak and HBM nits. A bright IPS scores identically to a bright OLED in §2.2 regardless of panel type.
*   **Colour gamut %** → §2.3 scores the actual measured DCI-P3 coverage. Panel type determines the achievable ceiling, but §2.3 scores the measured value — no structural overlap with §2.1.
*   **HDR format certifications** → §2.4 scores Dolby Vision / HDR10+ support. §2.1 scores the *rendering hardware quality* (black level, local dimming) that makes those formats meaningful.
*   **Maximum refresh rate (Hz)** → §2.6 Motion Smoothness scores the peak refresh rate. §2.1's LTPO vs AMOLED split rewards content-rate matching and Always-On Display quality — not the Hz ceiling.
*   **Battery efficiency of adaptive refresh** → §8.1 Battery (Endurance Model) uses separate dedicated fields (`refresh_rate_min_hz`, `refresh_rate_adaptive`) that live in the battery section. §2.1 rewards the *display quality* dimension of LTPO; §8.1 rewards the *battery efficiency* dimension. Different score categories, different weights, no overlap.
*   **PWM dimming and eye comfort** → §2.10 scores dimming frequency and flicker. §2.1 does not reward or penalise the dimming method.

*   **Measurement:** Manufacturer panel specifications and teardown confirmations.
*   **Unit:** Panel Technology Tier (0–10)
*   **Significance:** Determines three display hardware capabilities absent from all other metrics: (1) contrast ratio and true black quality, (2) off-axis colour stability, and (3) local dimming artefact freedom.

#### Scoring Table

| Score    | Canonical Panel Type               Hardware Basis                                                | Example Models              |
| :------- | :-------------------------------| :--------------------------------------------------------------| :---------------------------|
| **10.0** | **Tandem OLED**                 | Dual-stack emissive OLED (two light-emitting layers)           | iPad Pro M4, OnePlus 12     |
| **9.0**  | **LTPO OLED**                   | True variable refresh rate down to 1 Hz (LTPO backplane)       | S24 Ultra, iPhone 15/16 Pro |
| **8.0**  | **Standard OLED/AMOLED (LTPS)** | Self-emissive, fixed or limited-range refresh (LTPS backplane) | Galaxy A55, iPhone 14       |
| **6.0**  | **IPS LCD**                     | LED-backlit LCD with in-plane switching                        | iPhone 11, Poco X4 GT       |
| **2.0**  | **TFT or PLS LCD**              | Non-IPS LCD, budget (incl. Samsung PLS)                        | Budget devices              |
| **0.0**  | **TN LCD or Legacy**            | Twisted nematic LCD and obsolete technologies                  | Galaxy J1 (Legacy)          |

#### Marketing Name → Canonical Tier Representative Examples
*Use these examples to identify the correct tier.
*   **Tier 10.0 — Tandem OLED:** "Tandem OLED" (OnePlus 12), "Dual-Layer OLED" (iPad Pro M4).
*   **Tier 9.0 — LTPO OLED:** "Dynamic AMOLED 2X" (Samsung Ultra/Fold), "OLED ProMotion" (iPhone Pro), "LTPO OLED" (Pixel Pro).
*   **Tier 8.0 — Standard OLED/AMOLED (LTPS):** "Super AMOLED" (Samsung A-series), "Super Retina XDR" (iPhone 16 non-Pro), "AMOLED" (Generic).
*   **Tier 6.0 — IPS LCD:** "Liquid Retina HD" (iPhone 11), "IPS LCD" (Generic).
*   **Tier 2.0 — TFT or PLS LCD:** "PLS TFT" (Samsung budget), "TFT LCD" (Generic).
*   **Tier 0.0 — TN LCD or Legacy:** "TFT (TN)".

> [!IMPORTANT]
> **Decision rule when the spec sheet is ambiguous:** If a phone is listed as plain "OLED" or "AMOLED" with no LTPO qualifier, default to **Standard OLED/AMOLED (LTPS) (8.0)**. Only assign **LTPO OLED (9.0)** when the LTPO backplane or a marketing name from the Tier 9.0 table above is explicitly confirmed.

**Tandem OLED**: Dual-Stack Organic Light-Emitting Diode (OLED) consisting of two stacked light-emitting layers. This achieves higher peak brightness and superior power efficiency/longevity compared to single-stack designs.\
**LTPO OLED**: Single-stack Organic Light-Emitting Diode (OLED) utilizing a Low-Temperature Polycrystalline Oxide (LTPO) backplane, enabling true variable refresh rate down to **1 Hz** for optimized battery performance, smoother UI transitions, better frame-rate matching with video and less judder.\
**Standard OLED/AMOLED (LTPS)**: Standard Active-Matrix Organic Light-Emitting Diode (AMOLED) or OLED panel with a Low-Temperature Polycrystalline Silicon (LTPS) backplane. While offering true blacks and infinite contrast, the refresh rate is either fixed or limited to a narrower range (cannot reach 1 Hz).\
**IPS LCD**: In-Plane Switching Liquid-Crystal Display (IPS LCD) combined with an LED backlight. Provides wide viewing angles and accurate colors but lacks true black levels because the backlight remains active.\
**TFT or PLS LCD**: Budget Thin-Film Transistor (TFT) or Plane-to-Line Switching (PLS) Liquid-Crystal Display (LCD). These typically feature narrower viewing angles and lower color accuracy than high-end IPS panels.\
**TN LCD or Legacy**: Twisted Nematic (TN) LCD and other obsolete technologies. These suffer from severe color distortion and inversion beyond narrow viewing angles.

### 🔹 2.2 Brightness (Peak & HBM)
*Description:* Maximum brightness. Higher nits mean the screen is easily readable outside and HDR movies look stunning.
*   **Measurement:** High Brightness Mode (HBM) and Peak brightness.
*   **Unit:** Nits (cd/m²)
*   **Significance:** Critical for outdoor visibility (HBM) and watching HDR media (Peak).

**Understanding the Terminology:**
*   **Peak Brightness (For Movies):** This is the absolute maximum brightness the screen can achieve, but usually only on a tiny spot on the screen (e.g., 1% of the screen area, known as **APL** or *Average Picture Level*). This massive marketing number (like 4500 nits) is strictly used for watching **HDR (High Dynamic Range)** movies, where the screen needs to make a tiny explosion or a star look blindingly bright. It does *not* help you read your phone in the sun.
*   **HBM - High Brightness Mode (For the Sun):** This is the maximum brightness when the *entire* screen is lit up (100% APL). When you step outside into the blaring sun, your phone enters HBM to combat the glare so you can read a webpage, look at the camera viewfinder, or view a map. **HBM is the only true measure of outdoor readability.**

**Why Both? (Data Availability & Scoring Logic)**
HBM is increasingly published for all modern mid-range to flagship phones. We heavily weight HBM (70%) because it reflects true daily outdoor usability, while Peak (30%) specifically rewards a screen's media capability. 
*   **Fallback Rule:** For older or budget phones where manufacturers only publish the "Peak" marketing number, our formula safely estimates it: `HBM_Nits = Peak_Nits / 1.5` (a standard thermal limit correlation). This ensures no phone is penalized or biased just because its spec sheet is missing the HBM line item.

*Formulas:* 
*   `HBM_Score = 10 * (log(HBM_Nits) - log(Display_HBM_Nits_Min)) / (log(Display_HBM_Nits_Max) - log(Display_HBM_Nits_Min))` (Clamped 0-10)
*   `Peak_Score = 10 * (log(Peak_Nits) - log(Display_Brightness_Nits_Min)) / (log(Display_Brightness_Nits_Max) - log(Display_Brightness_Nits_Min))` (Clamped 0-10)
*   `Predicted_Score = (0.7 * HBM_Score) + (0.3 * Peak_Score)`
*   **Max Score (10.0):** ≥ Max Nits limits.
*   **Min Score (0.0):** ≤ Min Nits limits.

> [!NOTE]
> **Why Logarithmic?** Brightness perception follows the Weber-Fechner law. A jump from 500 to 1000 nits is perceived as a massive doubling in brightness by the human eye. However, because our eyes are already overwhelmed by the light, a 500-nit jump from 3000 to 3500 nits is barely noticed.

### 🔹 2.3 Color Gamut Coverage (CGC)
*Description:* Measures how much of standard color spaces the display can reproduce. This defines what the screen can physically display in terms of color richness and saturation.
*   **Measurement:** DCI-P3 coverage percentage from manufacturer specs or review databases.
*   **Unit:** Percentage (%)
*   **Significance:** Determines real-world color vibrancy and HDR reproduction capability.

*Formula:* `Score = 10 * (DCI-P3_percent - Display_P3_Coverage_Percent_Min) / (Display_P3_Coverage_Percent_Max - Display_P3_Coverage_Percent_Min)` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Display_P3_Coverage_Percent_Max
*   **Min Score (0.0):** ≤ Display_P3_Coverage_Percent_Min

> [!NOTE]
> **Why Linear?** DCI-P3 is the professional color standard used by cinema and streaming content. Each additional percentage point represents a physically equal slice of extra color the screen can show. Think of it like paint: a painter who can mix 90% of all possible shades has exactly 10% more capability than one at 80%. There are no diminishing returns within the 65–100% range that covers real phones, making a straight linear scale the correct and honest choice.
>
> **sRGB Fallback Conversion:**
> If only sRGB data is available: `DCI-P3_estimate = min(sRGB_percent * 0.75, 100)` as 100% sRGB ≈ 75% DCI-P3
>
> *Example:* 119% sRGB → 89% DCI-P3 (estimate), Score = 6.9
>
> [!IMPORTANT]
> **Gamut vs. Accuracy (Delta-E)**
> *   **Gamut = Quantity:** Measures the *range* of colors a screen is physically capable of showing. Like a painter's palette having more colors available.
> *   **Accuracy (Delta-E) = Quality:** Measures how *correctly* those colors are displayed compared to the source standard. Like the painter using those colors to perfectly match a reference image.
>
> **Why no Delta-E Score?** Factory calibration data (Delta-E) is rarely public in specs. Therefore, excellent color accuracy (e.g., Delta-E < 2.0) is rewarded strictly via **Section 11 (Boosters)** when validated by expert reviews.

### 🔹 2.4 HDR Format Support (HFS)
*Description:* Measures which HDR video formats the display officially supports (decoding capability).
*   **Measurement:** Manufacturer specifications and Digital Rights Management (DRM) certification lists (e.g., Widevine L1 for HD/4K streaming from Netflix, Disney+).
*   **Unit:** Supported Standards (Additive Point-Based Score)
*   **Significance:** Unlocks access to premium, studio-mastered content and ensures the display can render the full visual contrast and colour volume that the content creator intended.

**Scoring Structure (Additive):**
The HDR score is calculated by adding points for each supported format. A device can earn points across multiple formats, up to a maximum of 10.0.

| Supported Format            | Point Value |
| :-------------------------- | :---------- |
| **Base HDR (HDR10 or HLG)** | **+ 5.0**   |
| **Dolby Vision**            | **+ 3.0**   |
| **HDR10+**                  | **+ 2.0**   |

*Formula:* `Score = sum(points_for_detected_formats)` (Clamped 0–10)

> [!NOTE]
> **Understanding HDR Formats and the Additive Scoring Rationale**
>
> Higher scores are awarded to devices that support dynamic metadata formats (which optimize brightness/color frame-by-frame) and have wide compatibility with premium streaming services. The additive scoring ensures each capability is accurately and independently rewarded.
>
> *   **Base HDR (+5.0):** The universal foundation of High Dynamic Range. It includes **HDR10** (static metadata) and **HLG** (Hybrid Log-Gamma, broadcast-standard). Supporting either represents the most critical quality leap over 8-bit **SDR** (Standard Dynamic Range), as it establishes the necessary 10-bit color pipeline. Without this "floor," a device cannot be considered HDR-capable.
> *   **Dolby Vision (+3.0):** The highest-tier licensed dynamic format featuring 12-bit color depth and end-to-end studio calibration. This is the dominant standard used by Netflix, Apple TV, and Disney+. It carries a higher weight than HDR10+ because of its massive premium content library.
> *   **HDR10+ (+2.0):** Samsung's royalty-free dynamic metadata standard. While functionally similar to Dolby Vision, it scores slightly lower due to its significantly smaller premium library (primarily Amazon Prime). 
>
> **Example Scores:**
> *   *Universal (10.0):* Supports HDR10 (5.0) + Dolby Vision (3.0) + HDR10+ (2.0). Guaranteed best possible stream anywhere.
> *   *Primary (8.0):* Supports HDR10 (5.0) + Dolby Vision (3.0). Gives the best experience on most services, but falls back to static HDR10 on Amazon Prime. (e.g., iPhone)
> *   *Alternative (7.0):* Supports HDR10 (5.0) + HDR10+ (2.0). Best experience on Amazon Prime, but static HDR10 on Netflix/Disney+. (e.g., Galaxy S24)
>
> **Why Does HDR Format Matter if the OLED Screen is Already Good?**
> A premium OLED screen *without* a dynamic format (Dolby Vision / HDR10+) will display content using static tone-mapping or a generic SDR fallback, which frequently clips bright highlights or crushes dark shadows if the scene exceeds the panel's capabilities. Dynamic metadata renders each shot perfectly tailored to the panel with its scene-specific brightness curve — the visual difference is clearly visible on high-contrast scenes like fireworks or sunsets.

### 🔹 2.5 Resolution Density
*Description:* Pixel density (sharpness). Higher PPI means text and images look crisp, with no visible pixels.
*   **Measurement:** Pixels Per Inch (PPI)
*   **Unit:** PPI
*   **Significance:** Determines visual sharpness and clarity of text.

*Formula:* `Score = 10 * (log(PPI) - log(Display_PPI_Min)) / (log(Display_PPI_Max) - log(Display_PPI_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Display_PPI_Max
*   **Min Score (0.0):** ≤ Display_PPI_Min
> [!NOTE]
> **Why Logarithmic?** Human visual acuity has diminishing returns. The difference in sharpness between 200 and 300 PPI is immediately obvious, while the difference between 500 and 600 PPI is barely perceptible to the naked eye.

### 🔹 2.6 Motion Smoothness
*Description:* How many times the screen updates per second. 120Hz+ makes scrolling and animations look incredibly smooth compared to standard 60Hz.
*   **Measurement:** High-speed camera analysis or system reporting.
*   **Unit:** Hertz (Hz)
*   **Significance:** Determines the smoothness of motion and animations.
*Formula:* `Score = 10 * (log(Hz) - log(Display_Refresh_Rate_Hz_Min)) / (log(Display_Refresh_Rate_Hz_Max) - log(Display_Refresh_Rate_Hz_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Display_Refresh_Rate_Hz_Max
*   **Min Score (0.0):** ≤ Display_Refresh_Rate_Hz_Min
> [!NOTE]
> **Why Logarithmic?** Motion smoothness perception follows Weber's Law. The +60Hz upgrade from 60Hz to 120Hz is a massive leap in fluidity. An identical +60Hz increase from 120Hz to 180Hz is much harder to perceive for the average user.

### 🔹 2.7 Touch Responsiveness
*Description:* How fast the screen reacts to your touch. Higher rates mean instant response in games and a "glued to your finger" feel.
*   **Measurement:** Touch latency testing (time from touch to signal).
*   **Unit:** Hertz (Hz)
*   **Significance:** Critical for competitive gaming and UI fluidity.
*Formula:* `Score = 10 * (log(Hz) - log(Display_Touch_Sampling_Hz_Min)) / (log(Display_Touch_Sampling_Hz_Max) - log(Display_Touch_Sampling_Hz_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Display_Touch_Sampling_Hz_Max
*   **Min Score (0.0):** ≤ Display_Touch_Sampling_Hz_Min
> [!NOTE]
> **Why Logarithmic?** Input latency perception is non-linear. Increasing sampling rate from 60Hz to 240Hz (+180Hz) provides a noticeably "stickier" feel. However, an identical +180Hz increase from 240Hz to 420Hz provides improvements in reaction time that are smaller than the average human reaction variance.

### 🔹 2.8 Screen-to-Body Ratio (Bezels)
*Description:* How much of the front is screen vs. border. Higher percentage means thinner bezels and a more immersive, modern look.
*   **Measurement:** Pre-calculated ratio published by tech databases (e.g., GSMArena). If missing, calculated via: `(Active Display Area / Total Frontal Area) * 100`.
*   **Unit:** Percentage (%)
*   **Significance:** Aesthetic modernity and immersion.
*Formula:* `Score = 10 * ((Ratio - Display_SBR_Percent_Min) / (Display_SBR_Percent_Max - Display_SBR_Percent_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Display_SBR_Percent_Max
*   **Min Score (0.0):** ≤ Display_SBR_Percent_Min
> [!NOTE]
> **Why Linear?** Each percentage point of Screen-to-Body Ratio directly represents a proportional increase in visible display area, reducing the plastic border around the screen. A gain from 85% to 86% is the same engineering achievement as a gain from 91% to 92% — no single threshold changes the nature of the benefit. The practical range for modern phones (roughly 80–93%) has no diminishing returns, making linear the correct model.

### 🔹 2.9 Screen Size
*Description:* The physical size of the display measured diagonally. Larger screens offer more immersive media and gaming experiences.
*   **Measurement:** Diagonal length of the active display area.
*   **Unit:** Inches (")
*   **Significance:** Determines immersion level and device footprint.
*Formula:* `Score = 10 * ((Size^2 - Display_Size_Inch_Min^2) / (Display_Size_Inch_Max^2 - Display_Size_Inch_Min^2))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Display_Size_Inch_Max
*   **Min Score (0.0):** ≤ Display_Size_Inch_Min
> [!NOTE]
> **Why Quadratic?** The usable screen real estate scales as the *Area* of the display, which is proportional to the square of the diagonal (Area increases quadratically with diagonal size). While a linear penalty treats a 0.5" increase at the bottom of the scale exactly the same as at the top, a true geometric (Quadratic) curve appropriately rewards the massive manufacturing difficulty and user-experience gain of producing massive 6.8"+ "Ultra" screens.

### 🔹 2.10 Eye Comfort (Dimming Technology & Pulse-Width Modulation)
*Description:* How the screen dims at low brightness levels to prevent eye strain, headaches, and fatigue. Different screen technologies require different dimming solutions, which directly impact the user's biological comfort. This section evaluates both DC (Direct Current) Dimming and PWM (Pulse-Width Modulation).

**2.10.1 PWM Dimming (Flicker) Presence**
*   *Why it matters:* OLED screens cannot simply lower the voltage to their pixels without destroying color accuracy. Instead, they rapidly turn the pixels completely off and on (Pulse-Width Modulation). Traditional LCD/IPS displays lower brightness by directly reducing the voltage (Direct Current or DC Dimming), creating a continuous, unbroken stream of light. However, some cheap LCDs still use PWM backlight controllers.

| Presence | Dimming Technology Used | Spec Sheet Verification Rule                                                                   |
| :------- | :---------------------- | :--------------------------------------------------------------------------------------------- |
| **Yes**  | **PWM Dimming active**  | Any OLED/AMOLED panel (inherent), or an LCD specifically tested to have PWM flicker.           |
| **No**   | **DC (Direct Current)** | Standard LCD/IPS panel with confirmed DC (Direct Current) dimming (no measurable PWM flicker). |

**2.10.2 PWM Dimming Frequency**
*   *Why it matters:* If PWM is present, a higher frequency means the flicker is faster and less perceptible to the human eye, reducing strain.
*   **Measurement:** PWM dimming frequency.
*   **Unit:** Hertz (Hz)
*   *Formula:* `Score = 10 * (log(Hz) - log(Display_PWM_Hz_Min)) / (log(Display_PWM_Hz_Max) - log(Display_PWM_Hz_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Display_PWM_Hz_Max 
    *   **Min Score (0.0):** ≤ Display_PWM_Hz_Min

> [!NOTE]
> **Why Logarithmic?** The health benefits of higher PWM frequencies follow a diminishing return curve. The +500Hz jump from 200Hz to 700Hz is transformative, significantly reducing visible flicker and stopping headaches for sensitive eyes. However, an identical +500Hz increase from 3000Hz to 3500Hz provides almost zero perceptible biological benefit.

**Final Formula:**
*   If 2.10.1 Presence = No: `Score = 10.0` *(Perfect, flicker-free standard)*
*   If 2.10.1 Presence = Yes: `Score = Score_2.10.2`

### 🔹 2.11 Display Benchmark & Final Scoring (Methods A/B/C)
*Description:* Calculates the Final Display Score using the **Unified Methods A/B/C Model**.
*   **Measurement:** DXOMARK Display Score.
*   **Unit:** DXO Score (0-160+)
*   **Significance:** Real-world validation of display quality across readability, color accuracy, motion, and touch responsiveness.

#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct DXOMARK Display score is available. It provides the most accurate representation of real-world display quality.
*   **Source:** [DXOMARK Display](https://www.dxomark.com/smartphones/#display)
*   **Normalization:**
    *   **Formula:** `Score = 10 * (log(DXO_Score) - log(Display_DXO_Score_Min)) / (log(Display_DXO_Score_Max) - log(Display_DXO_Score_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Display_DXO_Score_Max
    *   **Min Score (0.0):** ≤ Display_DXO_Score_Min

> [!NOTE]
> **Why Logarithmic?** Visual perception quality follows diminishing returns (Weber-Fechner law). An improvement of **10 points** at the low end (e.g., 60 to 70) represents a fundamental fix to usability flaws (e.g., becoming readable in sunlight). The same **10-point** improvement at the high end (e.g., 140 to 150) represents subtle refinements in peak HDR highlights or calibration that are barely perceptible to the human eye. Logarithmic scaling correctly assigns more value to these early, critical gains.

#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.

**1. Identify Neighbors via Feature Distance (Minimum Variance)**
Instead of just matching the overall predicted score, we find the 3 devices that are statistically closest across the display sub-features that dictate perceptual quality.
*   **Search Space:** All phones with known DXOMARK Display scores (Method A), **excluding the target device** itself.
*   **Distance Metric:** Weighted Euclidean Distance in the 8-dimensional perceptual feature space (Sections 2.1–2.10, explicitly **excluding** 2.8 Screen-to-Body Ratio and 2.9 Screen Size).
    *   `Distance = Sqrt( Sum( Weight_i * (Diff_SubScore_i)^2 ) )`
    *   *Where Diff_SubScore_i = SubScore_Target_i - SubScore_Neighbor_i*
    *   *Where Weight_i represents the DXOMARK alignment weight (see justification below).*
    *   **Important:** Calculation uses **Predicted Scores** (Specs only), not Final Scores (Specs + Boosters). This ensures we compare devices based on intrinsic hardware similarity, unaffected by whether a review exists for them.
*   **Selection:** Pick the 3 distinct neighbors with the smallest `Distance`.

> [!NOTE]
> **Why Weight the Euclidean Distance?**
> DXOMARK's display protocol does not treat every metric equally. It tests six core pillars: Readability, Color, Video, Motion, Touch, and Artifacts. To accurately find a neighbor that fundamentally behaves like the target device, our Euclidean search relies on a weighted algorithm designed to mirror these pillars:
> *   **Primary Pillars (15-20% each):** 2.2 Brightness (DXO Readability) at **20%**, 2.1 Panel Tech (DXO Contrast/Blacks) at **15%**, and 2.6 Motion Smoothness (DXO Motion) at **15%**.
> *   **Secondary Pillars (10% each):** 2.3 Color Gamut (DXO Color), 2.4 HDR (DXO Video), 2.7 Touch Hz (DXO Touch), 2.5 PPI (DXO Aliasing Artifacts), and 2.10 PWM (DXO Flicker Artifacts).
> *   **Excluded (0%):** 2.8 Bezels and 2.9 Screen Size are purely physical aesthetic elements. Including them corrupts the search, as DXOMARK evaluates the panel's *output*, not its dimensions.

**2. Calculate Correction Ratio:**
*   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
    *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
*   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
    *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.

**3. Apply to Benchmark:**
*   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
*   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

#### Method C: Predicted Calculation (Tertiary)
Used as a standalone fallback if no neighbors exist, or as the **Predictor** for Method B.

**Formula:** `Predicted_Score = (0.15 * SubScore_2.1) + (0.20 * SubScore_2.2) + (0.10 * SubScore_2.3) + (0.10 * SubScore_2.4) + (0.10 * SubScore_2.5) + (0.15 * SubScore_2.6) + (0.10 * SubScore_2.7) + (0.10 * SubScore_2.10)`
*   *This is the **overall Predicted Score** for the entire display, calculated as the weighted sum of perceptual sub-section Predicted Scores.*
*   **Important:** Sections 2.8 and 2.9 are excluded from this benchmark prediction as they do not impact perceptual display quality. Use the **Predicted Score** (before boosters) for all included sub-sections. This ensures neutrality and prevents selection bias (reviewed vs. unreviewed phones) from skewing the technical baseline.

> [!IMPORTANT]
> **Terminology Clarification:**
> - **Sub-Section Predicted Score** (e.g., `SubScore_2.3`): Individual score for a single display attribute (Brightness, PPI, etc.) calculated from technical specs in Sections 2.1–2.10. Applicable sub-scores (excluding 2.8 and 2.9) are used in **Method B Step 1** for calculating the weighted Euclidean Distance to find neighbors.
> - **Overall Predicted Score** (`Predicted_Score` from Method C): The aggregate display score, calculated as the weighted sum of the perceptual sub-section Predicted Scores. Used in **Method B Step 2** for calculating the correction ratio.

## 🟣 3. Audio

### 🔹 3.1 Speaker System Capability (SSC)
*Description:* Evaluates the physical speaker configuration of the device. Focuses on speaker count, placement, and channel symmetry. Acoustic tuning and subjective sound quality are intentionally excluded.
*   **Measurement:** Speaker count and placement (manufacturer specs, teardowns, reviews).
*   **Unit:** Hardware Configuration Score (0-10)
*   **Significance:** Determines baseline loudness, stereo separation, and immersion without headphones.

**1. Balanced / Symmetrical Stereo (10.0 pts)**
*   **Definition:** Two identical or near-identical dedicated speaker units (e.g., dual front-facing or matching top/bottom drivers) providing equal volume and tonal balance.
*   **Verification:** Review explicitly states "Symmetrical speakers" or "Balanced stereo".

**2. Standard Hybrid Stereo (7.0 pts)**
*   **Definition:** Uses the earpiece as a second channel (tweeter) combined with a dedicated bottom main driver (woofer). Common in most flagships.
*   **Verification:** Spec sheet lists "Stereo Speakers" without specific "Symmetrical" confirmation.

**3. Mono Speaker (3.0 pts)**
*   **Definition:** Single active loudspeaker, typically bottom-firing only.
*   **Verification:** Spec sheet lists "Loudspeaker" (singular) or reviews confirm lack of stereo effect.

**4. No Usable Speaker (0.0 pts)**
*   **Definition:** Device relies entirely on external audio.
*   **Verification:** No built-in loudspeaker.

**Explanation of Tiers:**
*   **Balanced / Symmetrical:** A rare, hardware-intensive setup (e.g., ROG Phone, Xperia 1) where both left/right drivers are physically identical. This guarantees superior stereo imaging and center-channel stability compared to hybrid setups.
*   **Standard (Hybrid):** The industry standard for flagships (iPhone, Galaxy S, Pixel). While "Stereo", the earpiece is smaller and focuses on highs, while the bottom speaker handles mids/lows. This creates a slight imbalance, hence the lower score than perfect symmetry.
*   **Mono:** Provides no spatial separation; sound comes from a single point.

Note: This section evaluates only physical speaker hardware. Virtual surround, spatial audio, Dolby Atmos, and head tracking are software-level features and are evaluated separately in playback processing sections.

### 🔹 3.2 Playback Audio Processing & Immersion (PAPI)
*Description:* Evaluates the phone's ability to decode modern multichannel audio formats and to render spatialized sound during playback. This section focuses exclusively on playback-side processing, independent of speakers, microphones, or wired audio output.
*   **Measurement:** Supported playback formats, OS-level spatial audio feature support.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Determines compatibility with modern streaming content and immersion during media consumption.

**Structure:**
PAPI is a weighted composite of two subsections:
- **3.2.1 Audio Format Decode Support** — 50% weight
- **3.2.2 Spatial Audio Rendering** — 50% weight

**Predicted Score Formula:**
`PAPI = (0.5 * Score_3.2.1) + (0.5 * Score_3.2.2)`

#### 3.2.1 Audio Format Decode Support
*What it measures:* The range of multichannel or object-based audio formats the device can natively decode.
*Why it matters:* Determines compatibility with modern streaming and video content. A device that cannot decode these formats will downmix the audio to basic flat stereo, losing the spatial positioning intended by the director.

**Feature List (Additive Points, Clamped 0–10):**

*   **3D Spatial Format**
    *   **Dolby Atmos (+5.0):** The defacto standard for premium 3D spatial audio across 90% of commercial streaming services (Netflix, Apple TV+, etc.).
    *   **DTS:X (+1.0):** An alternative object-based 3D spatial audio format. While less common on streaming, it is heavily utilized on Blu-ray rips and IMAX Enhanced digital content, ensuring comprehensive compatibility for local media enthusiasts.

*   **Core Multichannel Format**
    *   **Dolby Digital / Dolby Audio (+3.0):** The core multichannel format. Frequently utilized as the base layer for Dolby Atmos or as the standard 5.1/7.1 surround sound option.
    *   **DTS / DTS-HD (+1.0):** The alternative core multichannel format.

*Formula:* `Score = sum(points_for_supported_formats)` (Clamped 0–10)
*   If the device does not list support for any multichannel/object formats (or explicitly only supports stereo), score is **0.00**.

> [!NOTE]
> **Understanding Audio Formats**
> *   **Object-Based Audio (Atmos / DTS:X):** Unlike traditional surround sound which assigns audio to specific speaker channels (e.g., "Left Rear speaker"), Atmos and DTS:X treat sounds as individual "objects" in 3D space. The phone's decoder dynamically maps these objects to however many speakers or headphones you are using, creating a much more convincing 3D soundscape.
> *   **Multichannel Surround (Dolby Digital / DTS):** Traditional 5.1 or 7.1 channel audio (Dolby Digital or standard DTS). It provides basic directional sound, but lacks the vertical height channels and precise object tracking of modern formats.
> 
> **Why this point distribution?**
> The weighting reflects the **real-world prevalence and immediate utility** of these formats for the average consumer, rather than subjective audio quality. 
> *   **Dolby Ecosystem (8.0 total):** Dolby completely dominates the commercial streaming market. A user with Dolby Atmos and Dolby Digital support will enjoy premium spatial audio on almost every major app (Netflix, Disney+, Apple Music). This guarantees an excellent, friction-free experience for 95% of users.
> *   **DTS Ecosystem (2.0 total):** While DTS:X offers comparable—and sometimes superior—bitrates and audio quality to Atmos, it is almost entirely absent from mainstream mobile streaming platforms. Its utility is restricted to extreme niche use cases: enthusiasts playing high-bitrate local Blu-ray rips or specific IMAX Enhanced app streams. 
> Therefore, while a device supporting all four formats represents the absolute pinnacle of universal compatibility (10.0), a device lacking DTS support only loses a minor fraction of its score, correctly reflecting that the vast majority of consumers will never encounter a file that requires it.

#### 3.2.2 Spatial Audio Rendering (Playback)
*What it measures:* The ability of the operating system to actively virtualize and "spatialize" audio during playback, creating a 3D soundstage (usually over supported headphones or earbuds).
*Why it matters:* Determines immersion and realism during media consumption, making the user feel like they are inside the movie scene rather than just listening to a flat audio stream.

| Score    | Spatial Rendering Capability                 |
| :------- | :------------------------------------------- |
| **10.0** | **Spatial audio with Dynamic Head Tracking** |
| **7.0**  | **Static spatial audio (no head tracking)**  |
| **0.0**  | **No spatial rendering**                     |

> [!NOTE]
> **Format Decode (3.2.1) vs. Spatial Rendering (3.2.2)**
> *   **Format Decode (3.2.1)** measures the phone's ability to merely *read and understand* the raw data file (like a Dolby Atmos movie file).
> *   **Spatial Rendering (3.2.2)** measures the phone's ability to *virtualize* that data into a 3D headphone experience. A phone might decode Atmos (3.2.1), but if it lacks a Spatial Audio rendering engine (3.2.2), you will just hear flat, high-quality stereo through your headphones instead of a 360-degree soundfield.
> 
> **Why is Head Tracking a 10.0?**
> Standard spatial audio (7.0) places sounds in a 3D sphere around your head, but if you physically turn your head to the left, the entire "room" of sound rotates with you. **Dynamic Head Tracking (10.0)** uses gyroscope data to anchor the audio in physical space. If you turn your head to the left, the dialogue stays anchored to the phone screen in front of you, drastically increasing the illusion of being in a physical cinema.

### 🔹 3.3 Wired Audio Capability
*Description:* Evaluates native wired audio output options available without relying on external powered accessories.
*   **Measurement:** Presence of 3.5mm analog audio jack, presence of analog audio output via USB-C, digital-only USB-C audio fallback.
*   **Unit:** Wired Audio Capability Score (0-10)
*   **Significance:** Determines whether users can use wired headphones directly, with minimal friction and without extra hardware.

**Why 3.5mm is superior to USB-C Analog:**
Even though both the 10.0 and 6.0 tiers provide analog audio originating from the phone's internal DAC, the 3.5mm jack is structurally and functionally superior:
*   **Universal Protocol Compatibility:** The 3.5mm TRS (Tip-Ring-Sleeve) connector is the global analog standard for billions of legacy headphones, speakers, and AUX inputs. USB-C always requires a physical adapter to bridge to this ecosystem.
*   **Mechanical Reliability:** 3.5mm ports are specifically designed for audio; they allow the connector to rotate freely without signal loss and are generally more robust for frequent "blind" insertions than the high-density pins of a USB-C port. Relying on a USB-C adapter introduces an additional mechanical point of failure (cable fraying or connection looseness).
*   **Simultaneous Charging & Listening:** Devices with a dedicated 3.5mm jack allow the user to charge the battery while listening to audio natively. USB-C implementations require a multiplexed splitter (dongle) to achieve both, which can introduce electrical interference or limit charging speed.
*   **Signal Isolation:** The 3.5mm jack is a dedicated audio circuit. USB-C multiplexes audio signals across the same pins used for high-speed data and Power Delivery (PD), which can occasionally result in detectable background hiss or "digital noise" if not perfectly shielded.
*   **True Zero-Latency Response:** The 3.5mm path is a direct, hard-wired analog circuit. While USB-C analog is also low-latency, the USB-C ecosystem frequently forces users toward digital-to-analog dongles (due to poor analog pass-through support on many cables), which can introduce signal processing latency and buffering delays.
*   **Zero-Friction UX:** A native jack removes the "dongle tax"—the mental and physical burden of carrying, losing, or forgetting an external accessory to perform a basic core function.

| Score    | Wired Audio Support                              | Example Models               |
| :------- | :----------------------------------------------- | :--------------------------- |
| **10.0** | **3.5mm headphone jack (native analog output)**  | Sony Xperia 1 V, Zenfone 10  |
| **6.0**  | **USB-C with documented analog audio output**    | Select Motorola/Sony models  |
| **3.0**  | **USB-C digital audio only (dongle required)**   | Most Flagships (S24, iPhone) |
| **0.0**  | **No wired audio support**                       | Rare/obsolete devices        |

### 🔹 3.4 Microphone & Audio Recording (MAR)
*Description:* Evaluates the audio capture capability of the device using only publicly verifiable data, without subjective quality judgments. This is a composite score based on hardware count, recording channels, and advanced features.
*   **Measurement:** Microphone count, recording channels/modes, documented audio features.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Determines audio capture quality for calls, videos, and content creation.

**Structure:**
MAR is a weighted composite of three subsections:
- **3.4.1 Microphone Hardware Count (MHC)** — 30% weight
- **3.4.2 Recording Channels & Modes (RCM)** — 30% weight
- **3.4.3 Advanced Capture Features (ACF)** — 40% weight

**Predicted Score Formula:**
`MAR = (0.3 * MHC) + (0.3 * RCM) + (0.4 * ACF)`

#### 3.4.1 Microphone Hardware Count (MHC)
*What it measures:* Physical microphones available for capture (bottom, top, rear, front).
*Why it matters:* More microphones enable better noise separation, spatial capture, and redundancy.

| Score    | Microphone Count      |
| :------- | :---------------------|
| **10.0** | **≥ 4 microphones**   |
| **8.0**  | **3 microphones**     |
| **5.0**  | **2 microphones**     |
| **2.0**  | **1 microphone**      |
| **0.0**  | **None**              |

#### 3.4.2 Recording Channels & Modes (RCM)
*What it measures:* How many audio channels the phone can record and in which modes.
*Why it matters:* Stereo recording dramatically improves realism; multi-channel enables spatial audio and post-processing.

| Score    | Recording Capability                  |
| :------- | :------------------------------------ |
| **10.0** | **Multi-channel / spatial audio**     |
| **8.0**  | **Stereo**                            |
| **5.0**  | **Mono**                              |
| **0.0**  | **Voice-only / unclear**              |

#### 3.4.3 Advanced Capture Features (ACF)
*What it measures:* Presence of clearly documented, named audio-processing features.
*Why it matters:* These features demonstrably improve intelligibility and subject isolation.

**Feature List (Additive, +2.5 pts each, Max 10.0):**
*   **Directional / Audio Zoom (+2.5):** Focuses audio on the zoomed subject (e.g., "Audio Zoom", "Zoom-in Mic").
*   **Wind Noise Reduction (+2.5):** Dedicated toggle or feature to filter wind rumble.
*   **Voice Focus / Isolation (+2.5):** Feature to enhance speech over background noise (e.g., "Speech Enhancement", "Audio Eraser").
*   **Pro Mic Support (+2.5):** The device accepts an external microphone for video recording — wired (USB-C or 3.5mm) or wireless (Bluetooth). Verify via spec sheet listing "external mic input", a documented gain/level control in the camera app, or reviewer confirmation of external mic recording. This is distinct from the three features above, which process the phone's built-in microphones.

*Formula:* `Score = sum(points_for_detected_features)` (Clamped 0–10)


## 🟣 4. Camera Systems

### A. Rear Camera — Photography
*Groups hardware capabilities for taking photos on the back of the phone.*

### 🔹 4.1 Main Sensor Size
*Description:* The size of the camera sensor. Larger sensors capture more light, resulting in much better low-light photos and natural background blur.
*   **Measurement:** Diagonal sensor size (Type 1/x").
*   **Unit:** Optical Format (Inches)
*   **Significance:** The most critical hardware factor for image quality (noise, dynamic range).
*Formula:* `Score = 10 * (log(Size_Inch) - log(Camera_Main_Sensor_Inch_Min)) / (log(Camera_Main_Sensor_Inch_Max) - log(Camera_Main_Sensor_Inch_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Camera_Main_Sensor_Inch_Max
*   **Min Score (0.0):** ≤ Camera_Main_Sensor_Inch_Min
> [!NOTE]
> **Why Logarithmic?** The physical photographic benefits of increased sensor area—specifically dynamic range expansion and photon noise reduction—follow a diminishing return curve. Moving from a tiny entry-level sensor (e.g., 1/2.55") to a large flagship sensor (e.g., 1/1.3") delivers a massive, instantly visible leap in image quality. However, an equivalent increase moving toward an even larger format (e.g., 1.0-inch) yields much smaller relative improvements in daily photography, as the primary bottlenecks shift to lens physics (diffraction, edge softness) and the limits of computational processing. A logarithmic scale perfectly models this non-linear perceptual gain.
> 
> **Why calculate using the Diagonal?** Sensor light-gathering capacity is determined by its **Area** ($Area \propto Diagonal^2$). Because of the power rule of logarithms, $log(x^2) = 2 \times log(x)$. When we put the squared diagonal into our normalization formula: $\frac{log(Size^2) - log(Min^2)}{log(Max^2) - log(Min^2)}$, it expands to $\frac{2 \times log(Size) - 2 \times log(Min)}{2 \times log(Max) - 2 \times log(Min)}$. The factor of $2$ perfectly factors out of both the numerator and denominator and completely cancels out. Therefore, scoring the 1-dimensional diagonal logarithmically is mathematically identical to scoring the 2-dimensional area logarithmically, flawlessly simplifying the calculation.

### 🔹 4.2 Main Camera Aperture
*Description:* The size of the lens opening. Wider apertures (lower f-number) let in more light for brighter night shots and create natural bokeh.
*   **Measurement:** Focal length / Entrance pupil diameter.
*   **Unit:** f-stop (f/number)
*   **Significance:** Determines light gathering and depth of field.
*Formula:* `Score = 10 * (log(Camera_Main_Aperture_f_Max) - log(f_stop)) / (log(Camera_Main_Aperture_f_Max) - log(Camera_Main_Aperture_f_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ Camera_Main_Aperture_f_Min
*   **Min Score (0.0):** ≥ Camera_Main_Aperture_f_Max
> [!NOTE]
> **Why Logarithmic?** The quantity of light is proportional to the area of the camera's pupil, which is $\propto 1/f^2$. 
> 
> If we wanted to score the raw *volume* of light, we would indeed calculate $1/f^2$ and score it linearly. However, just as we established in **Section 4.1 (Main Sensor Size)**, the real-world photographic benefits of gathering more light (expanding dynamic range, reducing noise) follow a diminishing return curve. To score the *photographic benefit* rather than the raw volume, we must apply a logarithmic curve: $log(1/f^2)$.
> 
> Here is the mathematical magic. Because of the algebraic rules of logarithms, $log(1/f^2)$ simplifies perfectly to $-2 \times log(f)$. 
> 
> When we place this into our standard normalization formula to calculate the score: 
> $\frac{-2 \times log(f_{stop}) - (-2 \times log(f_{max}))}{-2 \times log(f_{min}) - (-2 \times log(f_{max}))}$
> 
> The factor of $-2$ completely factors out of both the top and bottom. The negative signs elegantly flip the subtraction direction, leaving us with: 
> $\frac{log(f_{max}) - log(f_{stop})}{log(f_{max}) - log(f_{min})}$

### 🔹 4.3 Main Camera Resolution
*Description:* The maximum pixel count of the primary sensor. Higher resolution allows for more detailed cropping and sharper images in good light.
*   **Measurement:** Total effective pixel count.
*   **Unit:** Megapixels (MP)
*   **Significance:** Allows for digital zooming and fine detail capture.
*Formula:* `Score = 10 * (log(MP) - log(Camera_Main_Resolution_MP_Min)) / (log(Camera_Main_Resolution_MP_Max) - log(Camera_Main_Resolution_MP_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Camera_Main_Resolution_MP_Max
*   **Min Score (0.0):** ≤ Camera_Main_Resolution_MP_Min
> [!NOTE]
> **Why Logarithmic?** Sensor detail exhibits diminishing returns. Moving from 12MP to 50MP (+38MP) provides a significant jump in real-world resolving power. However, an identical +38MP increase from 162MP to 200MP offers almost zero perceptible improvement due to lens diffraction constraints.

### 🔹 4.4 Image Stabilization
*Description:* Hardware and software systems used to compensate for hand movement during image capture and video recording. Essential for sharp low-light photos and smooth video recording.
*   **Measurement:** Manufacturer camera specifications and teardown confirmation (where available).
*   **Unit:** Stabilization Mechanism Class
*   **Significance:** Determines the camera's ability to maintain image sharpness at longer exposure times and reduce motion blur in video.

| Score    | Stabilization Mechanism                                   |
| :------- | :-------------------------------------------------------- |
| **10.0** | **Multi-Axis Mechanical Stabilization (Gimbal)**          |
| **9.0**  | **Sensor-Shift Optical Image Stabilization**              |
| **8.0**  | **Lens-Based Optical Image Stabilization**                |
| **5.0**  | **Software-Only Stabilization (Electronic, no hardware)** |
| **0.0**  | **None**                                                  |

#### Mechanism Explainer

The five tiers correspond to fundamentally different physical (or non-physical) approaches to counteracting camera shake:

*   **Multi-Axis Mechanical Stabilization (Gimbal):** The entire camera module floats on a miniaturized mechanical suspension — conceptually similar to a handheld steadicam — that can rotate on ≥2 axes. This provides the highest correction angle (typically ≥ ±3°) and the smoothest video stabilization. Used by vivo ("Gimbal Stabilization 2.0/3.0"), ASUS ROG ("6-axis gimbal stabilization system"), and Samsung ("Super Steady OIS" hardware variant).

*   **Sensor-Shift Optical Image Stabilization (OIS):** The image sensor itself physically moves inside the camera module to counteract shake, while the lens stays fixed. Because the sensor is significantly lighter than the lens assembly, it allows faster and more precise micro-adjustments (up to 5,000/second on Apple devices) and uniquely corrects for rotational (roll) shake. Currently used by Apple on all iPhones since the iPhone 12 Pro Max / iPhone 13 series. Apple markets this as "Sensor-shift OIS" or "Sensor-shift optical image stabilization."

*   **Lens-Based Optical Image Stabilization (OIS):** A group of optical lens elements physically moves inside the lens barrel to compensate for hand shake. This is the most common form of hardware stabilization found in smartphones, used by the vast majority of Android manufacturers (Samsung, Google, OnePlus, Xiaomi, Motorola). Spec sheets typically list this simply as "OIS" or "Optical Image Stabilization." Periscope zoom modules may use a variant called "Prism Tilt OIS" where a prism rotates to correct shake.

*   **Software-Only Stabilization (Electronic Image Stabilization / EIS):** No moving mechanical parts. Software algorithms detect motion via the phone's gyroscope, then crop the captured video frame and digitally shift it frame-by-frame to compensate for detected movement. This is the cheapest to implement but reduces the usable field of view and can introduce a "jelly" distortion effect. Also called "EIS" (Electronic Image Stabilization), "AIS" (Artificial Image Stabilization), or simply "Digital stabilization."

*   **None:** No stabilization mechanism of any kind is disclosed or present.

#### Spec Sheet Keyword → Tier Lookup

To determine the correct tier, check the device's official specifications, marketing materials, or reliable teardown reviews. Match the found terminology against the recognized keywords below.

---

**10.0 — Multi-Axis Mechanical Stabilization (Gimbal)**
*   **Representative Keywords:** "Gimbal stabilization", "6-axis gimbal", "Micro-gimbal".
*   **Verification Rule:** Manufacturer **explicitly names** a multi-axis mechanical gimbal system. A simple "OIS" label is NOT sufficient.

**9.0 — Sensor-Shift Optical Image Stabilization**
*   **Representative Keywords:** "Sensor-shift OIS", "Sensor-shift optical image stabilization".
*   **Verification Rule:** Manufacturer **explicitly states** the **sensor** (not the lens) moves. Currently primarily found on Apple iPhones (12 Pro Max and newer).

**8.0 — Lens-Based Optical Image Stabilization**
*   **Representative Keywords:** "OIS", "Optical Image Stabilization", "Prism Tilt OIS".
*   **Verification Rule:** **Default tier** for any unspecified "OIS" (Optical Image Stabilization). The vast majority of Optical Image Stabilization systems in smartphones use lens-shifting.

**5.0 — Software-Only Stabilization**
*   **Recognized Keywords:** "EIS" (Electronic Image Stabilization), "Digital stabilization", "AIS" (Artificial Image Stabilization), "Software stabilization", "Video stabilization" (without any "OIS" mention)
*   **Verification Rule:** No physical/hardware stabilization is mentioned. The correction is performed purely through software algorithms and frame cropping.

**0.0 — None**
*   **Recognized Keywords:** No stabilization terms found.
*   **Verification Rule:** No mention of Optical Image Stabilization (OIS) or Electronic Image Stabilization (EIS) in any documentation.

---

#### Ambiguity Rule

> When a spec sheet lists only "OIS" (Optical Image Stabilization) without further qualification — no mention of "sensor-shift", "gimbal", or similar — **default to Lens-Based Optical Image Stabilization (8.00)**. The vast majority of phones listing generic "OIS" use a lens-shift mechanism. Only upgrade to Sensor-Shift (9.0) or Multi-Axis Mechanical (10.0) if the manufacturer **explicitly uses** one of the recognized keywords for those tiers.

### 🔹 4.5 Ultrawide Camera Capability (UCC)
*Description:* How capable the ultrawide camera is for landscapes, architecture, and group shots. This measures hardware potential, not image aesthetics.
*   **Measurement:** Presence, Field of View (FOV), and Sensor Size.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Determines the quality and breadth of wide-perspective photography.

**4.5.1 Ultrawide Presence (Binary Gate)**
*   *Why it matters:* No ultrawide means no wide-perspective photography.

| Presence | Configuration         | Spec Sheet Verification Rule |
| :------- | :-------------------- | :--------------------------- |
| **Yes**  | **Ultrawide present** | Any ultrawide lens.          |
| **No**   | **No ultrawide**      | Main camera only.            |

**4.5.2 Ultrawide Field of View**
*   *Why it matters:* Wider FOV captures more of the scene; this is the primary purpose of an ultrawide lens.
*   **Measurement:** Manufacturer FOV spec (degrees).
*   *Formula:* `Score = 10 * (FOV - Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max) / (Camera_Ultrawide_FOV_Deg_Max - Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Camera_Ultrawide_FOV_Deg_Max
    *   **Min Score (0.0):** ≤ Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max
> [!NOTE]
> **Why Linear?** Field of View is a direct geometric measurement where each degree adds roughly equal value to the composition. The difference between 100° and 110° is perceptually similar to the difference between 110° and 120° in terms of "wideness".

> [!IMPORTANT]
> **Presence Floor Rule applied here.** The 0-score floor (`Camera_Main_Sensor_WITHOUT_Ultrawide_FOV_Deg_Max` = 85°) is the best Field of View achievable by phones **without** an ultrawide lens (main camera only, ≈ 85°). This ensures that any ultrawide lens delivering a wider angle than the main camera always scores above 0, rewarding the phone for having the feature even in its weakest form. See the general Presence Floor Rule at the top of this document.

**4.5.3 Ultrawide Sensor Size**
*   *Why it matters:* Larger sensors perform better in low light and have better dynamic range.
*   **Measurement:** Optical format (e.g., 1/2.0").
*   *Formula:* `Score = 10 * (log(Size) - log(Camera_Ultrawide_Sensor_Inch_Min)) / (log(Camera_Ultrawide_Sensor_Inch_Max) - log(Camera_Ultrawide_Sensor_Inch_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Camera_Ultrawide_Sensor_Inch_Max
    *   **Min Score (0.0):** ≤ Camera_Ultrawide_Sensor_Inch_Min
> [!NOTE]
> **Why Logarithmic?** Sensor area grows quadratically with diagonal size, but photographic benefits (dynamic range, noise) follow a diminishing return curve. Moving from a tiny 1/4" sensor to a 1/2.5" sensor is a massive leap in quality, while moving from 1/2" to 1/1.5" offers smaller relative gains for an ultrawide module.

**Predicted Score Formula:**
*   If Presence = No: `UCC = 0.00`
*   If Presence = Yes: `UCC = (0.6 * FOV_Score) + (0.4 * Sensor_Score)`

> [!NOTE]
> **Why 60/40 (FOV/Sensor)?** The primary purpose of an ultrawide lens is to capture a wider scene, making Field of View (FOV) the dominant factor (60%). Additionally, the Presence Floor Rule (see top of document) can only be applied to the FOV component (where a shared metric exists across the binary gate), not to the sensor size component (where there is no equivalent lower-class value). Giving FOV a higher weight ensures that the floor correction propagates more strongly through the composite score, further rewarding phones that have an ultrawide — even one with a small sensor — over phones with no ultrawide at all. The remaining 40% for sensor size still accounts for low-light performance: a larger sensor absorbs more light and produces cleaner, less grainy photos in the dark.

### 🔹 4.6 Zoom Capability
*Description:* Optical zoom power. Allows you to take sharp, detailed photos of distant objects (like at a concert) without losing quality. Only true optical zoom is considered. Digital/crop zoom are excluded. 
*   **Measurement:** Focal length ratio relative to the main camera.
*   **Unit:** Optical Magnification (x)
*   **Significance:** Enables capturing distant subjects without quality loss.
*Formula:* `Score = 10 * (log(Zoom) - log(Camera_Zoom_Optical_x_Min)) / (log(Camera_Zoom_Optical_x_Max) - log(Camera_Zoom_Optical_x_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Camera_Zoom_Optical_x_Max
*   **Min Score (0.0):** ≤ Camera_Zoom_Optical_x_Min
> [!NOTE]
> **Why Logarithmic?** The difference in reach between 1x and 3x is transformative for composition. The difference between 10x and 12x is much less significant in terms of framing capability.

### 🔹 4.7 Macro Capability & Close-Focus Performance (MCFP)
*Description:* The ability to focus on very close subjects. Evaluates the different hardware combinations phones use to achieve macro photography.

> [!NOTE]
> **Why rarely the Main Camera?**
> Modern flagship main cameras have massive sensors. If you push them 3 centimeters away from a flower, the physical depth of field becomes paper-thin—meaning only a single petal is in focus while the rest of the flower blurs out (spherical aberration). To fix this, manufacturers rely on the **Ultrawide**, a **Dedicated** tiny lens, or **Telemacro**.

**4.7.1 Ultrawide Path**
*Groups the macro hardware performance of the secondary ultrawide lens.*

**4.7.1.1 Ultrawide Autofocus (AF)**
*   *Why it matters:* Standard camera lenses cannot focus on objects inches away. To take a "macro" photo, the lens needs to physically shift its internal glass elements extremely close to the sensor. Adding an Autofocus (AF) motor to the Ultrawide camera allows it to dynamically track subjects centimeters away, turning a standard wide camera into a high-quality macro lens. 
*   *AF vs Fixed Focus:* Even if a Fixed Focus (FF) lens boasts a short minimum focus distance on its spec sheet, it is permanently locked to one razor-thin focal plane. The user is forced to physically shift the phone back and forth until the subject accidentally perfectly aligns with that plane, resulting in mostly blurry shots. An AF motor can lock onto a subject, compensate for shaking hands/wind, and allows the user to tap-focus exactly where they want (e.g., the stamen of a flower instead of a petal). Therefore, AF is mechanically awarded a higher structural score than FF.

| Score    | Focus Type                     | Spec Sheet Verification Rule                               |
| :------- | :----------------------------- | :--------------------------------------------------------- |
| **10.0** | **Ultrawide with Autofocus**   | Specs list "AF", "PDAF", or "Dual Pixel" for the Ultrawide |
| **3.0**  | **Ultrawide with Fixed Focus** | Specs list "FF" or omit AF features for the Ultrawide      |

> [!NOTE]
> **Why 3.0 for Fixed Focus?** Data-driven calibration across 25 phones (see `macro_scoring_analysis.py`) showed that the original tier of 6.0 drastically overscored FF ultrawides. Fixed-focus macro is severely limited: the user must physically slide the phone back and forth to find the single focal plane, with no tap-to-focus, no subject tracking, and no compensation for hand shake. Expert review consensus consistently rates FF macro at 2.0–4.5, and a tier of 3.0 (combined with the MFD score) best fits this range.

*Formula:* 
*   If 4.5.1 Ultrawide Presence = No: `Score = 0.0`
*   If 4.5.1 Ultrawide Presence = Yes: `Score = 10.0` or `3.0` based on the Focus Type table above

**4.7.1.2 Minimum Focus Distance (MFD)**
*   *Why it matters:* The physical limit of how close you can get.
*   **Measurement:** Minimum focus distance (cm).
*   *Formula:* `Score = 10 * (log(Camera_Macro_Dist_cm_Max) - log(Distance)) / (log(Camera_Macro_Dist_cm_Max) - log(Camera_Macro_Dist_cm_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≤ Camera_Macro_Dist_cm_Min
    *   **Min Score (0.0):** ≥ Camera_Macro_Dist_cm_Max
> [!NOTE]
> **Why Logarithmic?** Magnification scales inversely with distance ($M \approx f/d$). Moving from 4cm to 2cm doubles the magnification capability (a massive gain in macro photography). Moving from 10cm to 8cm only increases magnification by ~25%. A logarithmic score flawlessly maps to this non-linear optical reality, heavily rewarding true microscopic lenses beneath 4cm.

**Predicted Score Formula:** 
*Formula for 4.7.1 Ultrawide Path:*
*   If 4.5.1 Presence = No: `Score_4.7.1 = 0.00` *(No ultrawide means no ultrawide distance score)*
*   If 4.5.1 Presence = Yes: `Score_4.7.1 = (0.4 * Score_4.7.1.1) + (0.6 * Score_4.7.1.2)`

**4.7.2 Telemacro (Telephoto Macro)**
*   *Why it matters:* Telemacro offers a distinct perspective advantage over Ultrawide macro. Using a telephoto lens (e.g., 3× or 5×) allows the user to capture macro shots from 10 cm – 15 cm away, preventing the phone from casting a dark shadow over the subject and providing beautiful natural background blur. 
*   *Scoring Logic:* Just having the feature doesn't guarantee a perfect 10 or automatic superiority over an ultrawide. A weak ~2× telephoto macro will score mathematically lower than a flagship ultrawide macro capable of focusing just 2 cm away. The telemacro score scales based on the specific telephoto lens's optical magnification and close-focus distance (both evaluated against telemacro-specific constant ranges), ensuring only extreme-magnification macro lenses hit a perfect 10. Because the final formula uses `Max(Ultrawide, Telemacro)`, the system neutrally evaluates both lenses and guarantees the mathematically superior hardware implementation wins.

**Presence Gate:**

| Presence | Telephoto Focus Capability       | Spec Sheet Verification Rule                                      |
| :------- | :------------------------------- | :---------------------------------------------------------------- |
| **Yes**  | **Telemacro present**            | Specs explicitly confirm "Macro telephoto", "floating elements",  |
|          |                                  | or list a close telephoto focus distance (e.g., 10cm-15cm).       |
| **No**   | **Standard Telephoto or None**   | Telephoto has standard minimum focus distance (usually > 50cm),   |
|          |                                  | or no telephoto lens exists on the device.                        |

**Input Parameters (two scored values):**

1.  **Optical Magnification** (`Magnification_x`)
    *   **What it is:** The optical zoom factor of the specific telephoto lens that provides the telemacro function. This is the native, hardware optical magnification — NOT a digital or hybrid zoom number.
    *   **Unit:** × (times), e.g., 3×, 3.7×, 5×.
    *   **Where to find it:**
        -   **Spec sheet:** Look for the telephoto lens line in the rear camera module. It is typically listed as "3× optical zoom", "5× periscope", "70 mm telephoto", etc. If stated in mm equivalent focal length, divide by the main lens focal length (usually ~24 mm) to get the magnification. Example: a 70 mm telephoto on a phone with a 24 mm main = roughly 3×.
    *   **Important:** Only use the optical magnification of the lens with confirmed telemacro capability. If a phone has a 3× and a 5× telephoto but only the 3× supports macro focus, use 3×.

2.  **Telemacro Minimum Focus Distance** (`Telemacro_MFD_cm`)
    *   **What it is:** The closest distance (in centimeters) at which the telemacro telephoto lens can achieve sharp focus. Unlike the ultrawide MFD (§4.7.1.2) which measures how close the phone can physically get to a tiny subject (typically 2–5 cm), the telemacro MFD is longer (typically 5–30 cm) because telephoto lenses operate at a greater working distance.
    *   **Unit:** cm (centimeters).
    *   **Where to find it:**
        -   **Spec sheet:** Look for "minimum focus distance" or "closest focus distance" listed specifically for the telephoto lens. Some manufacturers note it as "macro focus from X cm" (e.g., Vivo X200 Pro: "15 cm", Xiaomi 14 Ultra 3× lens: "10 cm").
    *   **Important:** A shorter Telemacro MFD is better — it means the telephoto can focus closer, producing higher magnification macro shots.

*Formula:* 
*   If Presence = No: `Score_4.7.2 = 0.00`
*   If Presence = Yes: `Score_4.7.2 = 7.0 + 0.3 * (0.7 * Zoom_Score + 0.3 * MFD_Score)`
    *   `Zoom_Score` = `10 * (log(Magnification_x) − log(Camera_Telemacro_x_Min)) / (log(Camera_Telemacro_x_Max) − log(Camera_Telemacro_x_Min))` — Clamped 0–10
    *   `MFD_Score`  = `10 * (log(Camera_Telemacro_MFD_cm_Max) − log(Telemacro_MFD_cm)) / (log(Camera_Telemacro_MFD_cm_Max) − log(Camera_Telemacro_MFD_cm_Min))` — Clamped 0–10 *(inverted: shorter distance = higher score)*
    *   **Max Score (10.0):** Achieved when the telephoto has the highest zoom (Magnification_x ≥ Camera_Telemacro_x_Max) **and** the closest focus (Telemacro_MFD_cm ≤ Camera_Telemacro_MFD_cm_Min). Both sub-scores hit 10.0, giving 7.0 + 3.0 = 10.0.
    *   **Min Score (7.0):** Achieved when both Zoom_Score and MFD_Score are at their lowest (0.0). The 7.0 base is the "Architectural Bonus" (see below).

> [!NOTE]
> **Why the 7.0 Architectural Bonus?** Data-driven calibration across 25 phones (see `macro_scoring_analysis.py`) independently converged on 7.0 as the optimal bonus. This value reflects the inherent advantages of telemacro hardware: floating telephoto elements enabling close-focus are a rare, high-end feature that produces superior macro images (no shadow casting on the subject, natural background blur, less barrel distortion). The remaining 3.0 points scale based on actual zoom magnification (70%) and minimum focus distance (30%), ensuring differentiation among telemacro implementations.

**4.7.3 Dedicated Macro Lens (Penalty-aware)**
*   *Why it matters:* Dedicated lenses can be useful but are often low-quality gimmicks. We cap the score at 3.0 to ensure they are appropriately ranked below higher-quality macro implementations that use more capable primary or ultrawide sensors.
*   **Measurement:** Sensor Resolution in Megapixels (MP). Dedicated macro lenses typically range from 2 MP (budget) to 5 MP (mid-range), with rare 8 MP outliers.
*   *Formula:* `Score = clamp(3 * Megapixels / Camera_Dedicated_Macro_MP_Max, 0, 3)`
    *   **Max Score (3.0):** ≥ Camera_Dedicated_Macro_MP_Max
    *   **Min Score (0.0):** 0 Megapixel (No dedicated macro lens)
    *   *Examples:* 2 Megapixels → 0.75, 5 Megapixels → 1.88, 8 Megapixels → 3.0
> [!NOTE]
> **Why capped at 3.0?** Data-driven calibration (see `macro_scoring_analysis.py`) found that the original cap of 6.0 allowed gimmick 5 MP sensors to outscore budget phones with real ultrawide macro hardware. Lowering the cap to 3.0 ensures dedicated lenses remain in the entry-level bracket, preventing them from competing with more sophisticated Autofocus Ultrawide or Telemacro solutions. The linear mapping over 0–8 MP ensures differentiation across the actual hardware range.

**Final Formula:**
*   `MCFP Score = Max(Ultrawide_Path, Telemacro_Path, Dedicated_Path)`
*   `MCFP Score = Max(Score_4.7.1, Score_4.7.2, Score_4.7.3)`


### B. Rear Camera — Video Capture & Production
*Groups the hardware video recording capabilities of the rear module.*

### 🔹 4.8 Rear Video Resolution
*Description:* Maximum spatial resolution supported for rear-camera video recording.
*   **Measurement:** Maximum supported rear video resolution.
*   **Unit:** Resolution Tier
*   **Significance:** Higher resolution allows greater detail, cropping flexibility, and higher-quality downscaling.

| Score  | Max Rear Video Resolution |
| :----- | :-------------------------|
| **10** | **≥ 4K (Ultra HD) or 8K** |
| **8**  | **1440p / QHD (2.5K)**    |
| **6**  | **1080p (Full HD)**       |
| **3**  | **720p (HD)**             |
| **0**  | **≤ 480p**                |

> [!NOTE]
> **Why is 8K not a separate tier above 4K?** 8K video (7680×4320) on smartphones (e.g., Samsung Galaxy S-series) is currently a gimmick tier: extreme heat, massive file sizes, and no streaming platform requires it. The perceptual benefit over 4K on a phone screen is zero. Both map to Score 10 as the "best available" practical tier.

### 🔹 4.9 Rear Video Frame Rate
*Description:* Maximum standard frame rate achieved specifically at the device's highest supported resolution (as scored in Section 4.8), capped at 4K (2160p).
*   **Measurement:** Maximum Frames per second (FPS) at Max Resolution capped at 4K.
*   **Unit:** FPS
*   **Significance:** Higher FPS (Frames Per Second) enables smoother motion and better motion clarity.
*Formula:* `Score = 10 * (log(FPS) - log(Camera_Video_FPS_Min)) / (log(Camera_Video_FPS_Max) - log(Camera_Video_FPS_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Camera_Video_FPS_Max
*   **Min Score (0.0):** ≤ Camera_Video_FPS_Min
> [!NOTE]
> **Why Logarithmic?** The perception of smoothness is non-linear. The +30fps jump from 30fps to 60fps is a dramatic, transformative upgrade. However, an identical +30fps increase from 90fps to 120fps is barely noticeable for standard video consumption.

> [!NOTE]
> **Why cap the search at 4K and link it to Section 4.8?** To prevent 'double-dipping', a device must prove its frame rate performance under the load of its maximum claimed resolution from Section 4.8. If a device supports 4K at only 30fps, it cannot submit its 1080p@60fps mode for a higher score here. However, to protect 8K-capable flagships from processing limits inherent to 8K sensors, the evaluation resolution is strictly capped at 4K. An 8K phone is evaluated on its 4K frame rate. This is reinforced by the fact that 8K and 4K resolutions currently receive the exact same maximum score (10.0) in Section 4.8; therefore, it is mathematically consistent that they are both evaluated for frame rate parity at the 4K baseline.  **Important:** Explicitly exclude any frame rates designated for "Slow Motion" or "High-Speed Burst" (e.g., 240fps+), as these are evaluated separately in Section 4.12.

### 🔹 4.10 Video Color & Dynamic Range
*Description:* Ability to capture wide dynamic range and rich color information in video.
*   **Measurement:** Supported **HDR** (High Dynamic Range) standards.
*   **Unit:** Composite Index (0–10)
*   **Significance:** High Dynamic Range video preserves highlights and shadows, improving realism and color grading headroom.

| Supported Format            | Point Value |
| :-------------------------- | :---------- |
| **Base HDR (HDR10 or HLG)** | **+ 5.0**   |
| **Dolby Vision**            | **+ 3.0**   |
| **HDR10+**                  | **+ 2.0**   |

*Formula:* `Score = sum(points_for_detected_formats)` (Clamped 0–10)

> [!NOTE]
> **Understanding Video HDR Formats & Symmetry with Display Playback (§2.4):**
> To ensure mathematical consistency across the project, this section perfectly mirrors the scoring logic from **Section 2.4 (Display HDR Format Support)**. 10-bit color depth is structurally required for all formats listed; therefore, any certified support automatically confirms high-bit-depth hardware capability.
>
> *   **Base HDR (+5.0):** The universal foundation of High Dynamic Range. It includes **HDR10** (static metadata) and **HLG** (Hybrid Log-Gamma, broadcast-standard). Supporting either represents the most critical quality leap over 8-bit **SDR** (Standard Dynamic Range), as it establishes the necessary 10-bit color pipeline. Without this "floor," a device cannot be considered HDR-capable.
> *   **Dolby Vision (+3.0):** A proprietary dynamic metadata format that optimizes brightness, contrast, and color on a *scene-by-scene* or *frame-by-frame* basis. It is the dominant premium standard in mobile ecosystems, featuring native support in social media pipelines (Instagram, TikTok) and professional mastering. 
> *   **HDR10+ (+2.0):** The open-standard royalty-free alternative dynamic **High Dynamic Range** format. Like Dolby Vision, it adjusts tone mapping frame-by-frame, offering a significant improvement over static HDR10. It is awarded fewer points solely due to having a smaller social media and content ecosystem.
>
> **Why does Dynamic Metadata (Score 7.0–10.0) matter?**
> Standard High Dynamic Range (Score 5.0) sets a *single* brightness level for the entire file. If a video has both extremely bright and very dark scenes, static HDR must compromise. Dynamic formats (Dolby Vision, HDR10+) solve this by adjusting the brightness curve for every single shot, preventing blown-out highlights or crushed shadows.
>
> **Example Scores:**
> *   *Universal (10.0):* Supports Base HDR + Dolby Vision + HDR10+. (e.g., Xiaomi 14 Ultra)
> *   *Premium Standard (8.0):* Supports Base HDR + Dolby Vision. (e.g., iPhone 16 Pro, Vivo X100 Pro)
> *   *Dynamic Alternative (7.0):* Supports Base HDR + HDR10+. (e.g., Galaxy S24 Ultra, Pixel 9 Pro)
> *   *Baseline HDR (5.0):* Supports only static Base HDR (HDR10/HLG). Typical for mid-range sensors.

### 🔹 4.11 Video Encoding & Professional Recording
*Description:* Support for professional codecs and recording profiles enabling advanced post-production. This is a composite score evaluating codec quality, color profile support, and bit depth independently.
*   **Measurement:** Supported codecs, color profiles, and bit depth.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Professional codecs preserve detail, reduce compression artifacts, and allow color grading.

**Structure:** `Score = (0.40 * PCS) + (0.35 * LCPS) + (0.25 * CBD)`

#### 4.11.1 Professional Codec Support (PCS) — 40%
*What it measures:* Whether the phone can record in a **RAW** (unprocessed sensor data) or **Mezzanine** (high-quality intermediate) format. These are "production-grade" files designed specifically for high-end video editing rather than just watching or sharing on social media.
*   **Measurement:** Manufacturer specifications, official camera feature lists.
*   **Why it matters:** Standard videos are heavily compressed to save space, which "bakes in" the look and permanently loses data. Professional formats preserve almost all original image detail and color information, allowing for clean "post-production" (video editing) and complex **VFX** (Visual Effects) without the video falling apart or looking "pixelated." **RAW** formats offer the absolute maximum flexibility, allowing editors to completely change things like white balance after filming, while **Mezzanine** formats like ProRes are slightly more compressed but still vastly superior to standard phone video.

| Condition                                                   | Score    |
| :-----------------------------------------------------------| :------- |
| **Supports true RAW video (CinemaDNG, ProRes RAW, BRAW)**   | **10.0** |
| **Supports Mezzanine format (ProRes, APV, DNxHR/HD)**       | **8.0**  |
| **Does not support professional recording formats**         | **0.0**  |
*Formula:* `Score = max(points_for_detected_codecs)`

#### 4.11.2 Log Color Profile Support (LCPS) — 35%
*What it measures:* Whether the phone supports a **Logarithmic** (Log) gamma curve. This is a special way of storing light that makes the image look "flat" or "grey" initially but captures significantly more detail in the brightest and darkest parts of the frame.
*   **Measurement:** Camera feature list, video mode specifications.
*   **Why it matters:** In standard recording, a bright sky or a dark shadow might become pure white or solid black (clipping). Log profiles capture this lost information, giving editors much more flexibility during "color grading" (the process of adjusting colors and contrast) to achieve a cinematic look without the image becoming "noisy" or "distorted."

| Score    | Supported Color Profile                                            |
| :------- | :----------------------------------------------------------------- |
| **10.0** | **True Log: Apple Log / Samsung Log / S-Log3 / V-Log / D-Log....** |
| **5.0**  | **Flat / Cine: S-Cinetone / Cinelike-D / D-Cinelike....**          |
| **0.0**  | **None (Standard contrast only)**                                  |

*Formula:* `Score = max(points_for_detected_profiles)`

> [!NOTE]
> **Log vs. Flat:** True **Log** profiles (10.0 points) mathematically compress the sensor's maximum dynamic range, requiring a specific technical transformation (a LUT) during editing to look normal. **Flat** profiles (5.0 points) simply turn down the contrast and saturation settings of standard video. Flat profiles help retain some highlight/shadow detail compared to normal video, but they do not capture the massive data range of a true Log curve.

#### 4.11.3 Color Bit Depth (CBD) — 25%
*What it measures:* How much individual color information is stored per channel. This is the difference between having thousands of shades vs. millions of shades.
*   **Measurement:** Codec specifications, manufacturer specifications.
*   **Why it matters:** Standard "8-bit" color provides 256 levels of brightness for each color channel. Premium **10-bit** color provides 1,024 levels per channel, dramatically reducing "banding" in smooth gradients (like skies). The cutting-edge **12-bit** color provides 4,096 levels per channel, capturing extreme nuances for heavy post-production and RAW workflows.

| Bit Depth                             | Score    |
| :------------------------------------ | :------- |
| **12-bit color**                      | **10.0** |
| **10-bit color**                      | **5.0**  |
| **8-bit color only (standard)**       | **0.0**  |

*Formula:* `Score = 2.5 * (Bits - 8)` (Clamped 0-10)

> [!NOTE]
> **Why 5.0 for 10-bit?** The raw number of color shades increases exponentially with bit depth ($2^n$), but human perception of these differences follows a **logarithmic scale** (Weber-Fechner law). Because $\log_2(2^{\text{bits}}) = \text{bits}$, the resulting perceived improvement is perfectly linear relative to the bit depth itself. Therefore, the leap from 8 to 10 bits represents the same proportional visual gain as the leap from 10 to 12 bits, cleanly splitting the 10.0 score space in half.

**Final Formula:** `Score = (0.40 * PCS) + (0.35 * LCPS) + (0.25 * CBD)`

### 🔹 4.12 High Frame Rate (Slow Motion)
*Description:* The ability to capture video at very high frame rates in a dedicated camera mode, allowing for extreme deceleration of fast motion.
*   **Measurement:** Maximum slow-motion Frames per Second (FPS) and its corresponding resolution, as explicitly listed in the device's secondary video specifications under marketing terms like "Slow Motion", "Slo-mo", "High Speed Video", or "Super Slow-mo" (Do NOT use standard video frame rates from Section 4.9).
*   **Unit:** Megapixels per Second (MP/s)
*   **Significance:** Enables creative effects and extreme deceleration of fast-moving subjects.
*   **Scoring Rule:** Scanners must calculate the mathematical throughput (`Resolution_MP * FPS`) of *all* available slow-motion configurations (e.g., 4K@120fps vs. 1080p@960fps) and score based exclusively on the combination yielding the **Absolute Maximum MP/s**. If a phone has no dedicated slow-motion mode, the score is **0.0**.
*Formula:* `Score = 10 * (log(MP_s) - log(Camera_SlowMo_MPs_Min)) / (log(Camera_SlowMo_MPs_Max) - log(Camera_SlowMo_MPs_Min))` (Clamped 0-10)
    *   `MP_s = Resolution_MP * FPS`
*   **Max Score (10.0):** ≥ Camera_SlowMo_MPs_Max
*   **Min Score (0.0):** ≤ Camera_SlowMo_MPs_Min
> [!NOTE]
> **Why Logarithmic?** The customer's perception of slow-motion improvements follows diminishing returns. The leap from 120fps to 360fps (+240fps) is a massive, visually transformative upgrade, allowing the user to heavily decelerate everyday fast action in post-production while maintaining perfect playback fluidity. However, an identical +240fps increase from 720fps to 960fps is highly niche; the extra deceleration it provides is practically imperceptible to the human eye unless filming extreme physics like a water balloon popping. A logarithmic curve correctly matches human perception, heavily rewarding the initial leap into high-quality slow motion and offering diminishing returns for extreme speeds.

### C. Front Camera System (Selfie)
*Groups all front-facing hardware and capabilities (both photo and video) into one cohesive chapter.*

### 🔹 4.13 Front Camera Sensor Resolution
*Description:* Spatial resolution of the front-facing camera.
*   **Measurement:** Front camera megapixel count.
*   **Unit:** Megapixels (MP)
*   **Significance:** Determines selfie detail and cropping flexibility.
*Formula:* `Score = 10 * (log(MP) - log(Camera_Front_Resolution_MP_Min)) / (log(Camera_Front_Resolution_MP_Max) - log(Camera_Front_Resolution_MP_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Camera_Front_Resolution_MP_Max
*   **Min Score (0.0):** ≤ Camera_Front_Resolution_MP_Min
> [!NOTE]
> **Why Logarithmic?** Selfie detail benefits diminish rapidly after a certain point. 32MP is sufficient for high-quality prints; beyond that, sensor size matters more than pixel count.
>
> **Homogenization with Rear Camera (Section 4.3):**
> This section mirrors the logarithmic scoring logic of the Main Camera Resolution section (§4.3), using its own front-specific constants (`Camera_Front_Resolution_MP_Max` and `Camera_Front_Resolution_MP_Min`).

### 🔹 4.14 Front Camera Focus System
*Description:* Ability of the front-facing camera to maintain sharp focus across different subject distances.
*   **Measurement:** Focus mechanism and optical configuration.
*   **Unit:** Focus System Tier
*   **Significance:** Autofocus(AF) ensures sharp selfies and vlogs regardless of arm length or group distance.

| Score    | Focus System Tier                                            | Objective Criteria                                         |
| :------- | :----------------------------------------------------------- | :--------------------------------------------------------- |
| **10.0** | **Autofocus (AF) (PDAF / Dual Pixel / Laser AF)**            | Any active Focus mechanism                                 |
| **6.0**  | **Fixed Focus (FF) (Modern Wide-DOF)**                       | Fixed focus AND (Aperture f-number ≥ 2.0 OR Sensor ≤ 1/3") |
| **3.0**  | **Fixed Focus (FF) (Legacy Narrow-DOF)**                     | Fixed focus AND (Aperture f-number < 2.0 AND Sensor > 1/3")|
| **0.0**  | **No Front Camera**                                          | Feature phone                                              |

> [!NOTE]
> **A Beginner's Guide to Focus Systems:**
> *   **Autofocus (AF):** A smart mechanical system where the camera lens physically moves to find the sharpest point. It ensures your face is crisp whether the phone is 10 centimeters away or 1 meter away.
>     *   **PDAF (Phase Detection Auto Focus):** A fast, modern technology that uses special "paired" pixels on the sensor to instantly calculate exactly how much the lens needs to move.
>     *   **Dual Pixel:** An elite version of PDAF where *every single pixel* participates in focusing. This makes it incredibly fast, especially in dim light.
>     *   **Laser AF (Laser Auto Focus):** The phone fires a tiny, invisible laser beam to measure the exact distance to your face. It's the fastest way to focus in total darkness.
> *   **Fixed Focus (FF):** A simple lens with no moving parts. The focus is permanently "locked" at a factory-set distance (usually arm's length).
> *   **Depth of Field (DOF):** This is the "focus zone"—the range of distance within which objects appear sharp.
>     *   **Wide DOF (Score 6):** A large focus zone where everything from your nose to the background is reasonably sharp. Brands achieve this by using smaller apertures (higher f-numbers like f/2.2).
>     *   **Narrow DOF (Score 3):** A tiny focus zone. If you move the phone slightly closer or further, your face becomes blurry. This happens with larger lenses (low f-numbers like f/1.8) that lack an AF motor to adjust themselves.

> [!IMPORTANT]
> **Scoring Guidelines & Mathematical Interpretation:**
> *   **Aperture (f-number):** In optics, the aperture is written as a fraction where the **f-number** is the denominator ($f/2.2$, $f/2.4$). **Because it's a fraction, a larger f-number actually means a smaller physical opening.**
>     *   **f-number ≥ 2.0:** Smaller openings like **f/2.2** or **f/2.4** (which widen the focus zone).
>     *   **f-number < 2.0:** Larger openings like **f/1.8** or **f/1.9** (which narrow the focus zone).
> *   **Sensor Size:** Optical formats are also fractions of an inch (e.g., 1/3"). A larger denominator means a smaller sensor.
>     *   **Sensor ≤ 1/3":** Smaller sizes like **1/3.6"** or **1/4"** (which widen the focus zone).
>     *   **Sensor > 1/3":** Larger sizes like **1/2.8"** or **1/2.0"** (which narrow the focus zone).
> *   **Missing Data Fallback:** If the sensor format is missing from public specifications but the aperture is known, classify the phone based entirely on its f-number.

### 🔹 4.15 Front Camera Video Performance
*Description:* Maximum video capture capability of the front-facing camera, quantifying resolution, frame rate, dynamic range, and professional recording profiles.
*   **Measurement:** Max resolution, Frames per Second (FPS), High Dynamic Range (HDR), and Professional Recording (Codecs and Log).
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for vlogging, video calls, and content creation.
*Formula:* `Score = (0.35 * ResScore) + (0.25 * FPSScore) + (0.20 * HDRScore) + (0.20 * ProRecordScore)`
    *   *Where:* `ProRecordScore = (0.50 * PCS_Score) + (0.50 * LCPS_Score)`

**4.15.1 Video Resolution Score**
*What it measures:* The maximum spatial resolution (pixel count) the front camera can record.
*   **Measurement:** Maximum supported front video resolution.
*   **Why it matters:** Higher resolution provides more detail for cropping, digital stabilization, and future-proofing. 4K allows for 1080p crops without quality loss, while 720p limits editing flexibility.

| Score  | Max Front Video Resolution |
| :----- | :------------------------- |
| **10** | **≥ 4K (Ultra HD) or 8K**  |
| **8**  | **1440p / QHD (2.5K)**     |
| **6**  | **1080p (Full HD)**        |
| **3**  | **720p (HD)**              |
| **0**  | **≤ 480p**                 |

> [!NOTE]
> **Homogenization with Rear Camera (Section 4.8):**
> This scoring table perfectly mirrors the rear camera's Video Resolution section (§4.8), as the principles of perceptual resolution and the 4K standard ceiling apply equally to both modules.
>
> **Why are 8K and 4K scored identically?** Just as with rear cameras, 8K video on smartphones provides a negligible mathematical resolution increase mapped to the human eye on small screens, often at the detriment of storage limits and low-light performance. 4K remains the industry standard ceiling for practical mobile content creation, meaning there is currently no tangible incentive to reward 8K recording over 4K recording.

**4.15.2 Video Frame Rate Score**
*What it measures:* Maximum frame rate achieved specifically at the device's highest supported resolution (as scored in Section 4.15.1), capped at 4K.
*   **Measurement:** Maximum Frames per second (FPS) at Max Resolution capped at 4K.
*   **Why it matters:* Higher frame rates (e.g., 60 FPS) provide smoother motion and better clarity for vlogs and video calls, reducing motion blur and improving the perception of fluidity.
*   *Formula:* `FPSScore = 10 * (log(FPS) - log(Camera_Front_Video_FPS_Min)) / (log(Camera_Front_Video_FPS_Max) - log(Camera_Front_Video_FPS_Min))` (Clamped 0-10)
    *   **Variables:**
        *   `FPS` = Maximum sustained frame rate (e.g., 60, 30, 24)
    *   **Max Score (10.0):** ≥ Camera_Front_Video_FPS_Max
    *   **Min Score (0.0):** ≤ Camera_Front_Video_FPS_Min
> [!NOTE]
> **Why Logarithmic?** Frame rate perception is non-linear. The +30fps jump from 30fps to 60fps is a dramatic, transformative upgrade for smoothness. However, an identical +30fps increase beyond 60fps is barely noticeable for standard social media and video call consumption.
>
> **Homogenization with Rear Camera (Section 4.9):**
> This section perfectly mirrors the scoring process and logarithmic formula of the rear camera's Video Frame Rate section (§4.9). It evaluates the maximum frame rate at the highest resolution (capped at 4K) using its own specific constants (`Camera_Front_Video_FPS_Max` and `Camera_Front_Video_FPS_Min`).

> [!NOTE]
> **Why cap the search at 4K and link it to Section 4.15.1?** To prevent 'double-dipping', a device must prove its frame rate performance under the load of its maximum claimed resolution (from Section 4.15.1). If a device supports 4K at only 30fps, it cannot submit its 1080p@60fps mode for a higher score here. However, to protect high-resolution sensors from processing limits at extreme resolutions (like 8K), the evaluation is strictly capped at 4K. An 8K-capable front camera is evaluated on its 4K frame rate. This ensures mathematical consistency since 8K and 4K receive the same maximum score in Section 4.15.1.

**4.15.3 Front Video Color & Dynamic Range (HDRScore)**

*Description:* Measures which High Dynamic Range (HDR) video formats the front camera can record in to optimize brightness, contrast, and color.
*   **Measurement:** Supported **HDR** (High Dynamic Range) video recording standards.
*   **Unit:** Additive Point System (0–10)
*   **Significance:** Determines highlight retention and dynamic range for selfie video, especially in difficult backlit vlogging scenarios.

| Supported Format            | Point Value |
| :-------------------------- | :---------- |
| **Base HDR (HDR10 or HLG)** | **+ 5.0**   |
| **Dolby Vision**            | **+ 3.0**   |
| **HDR10+**                  | **+ 2.0**   |

*Formula:* `HDRScore = sum(points_for_detected_formats)` (Clamped 0–10)

> [!NOTE]
> **Homogenization with Rear Camera (Section 4.10):**
> This additive scoring logic perfectly mirrors the rear camera's Video HDR section (4.10). Scoring is additive because supporting dynamic metadata formats (Dolby Vision, HDR10+) on top of base HDR provides cumulative benefits for both optimal device playback and social media ecosystem compatibility.

**4.15.4 Front Professional Recording (ProRecordScore)**

*Description:* Support for professional codecs and logarithmic recording profiles on the front camera. This section is fully homogenized with the Rear Camera (§4.11) but simplifies the front module by omitting Bit Depth.
*   **Measurement:** Composite index of Codecs and Log profiles.
*   **Unit:** Recording Index (0–10)
*   **Significance:** Enables high-end vlogging workflows with professional grading flexibility.
*   **Formula:** `Score = (0.50 * PCS) + (0.50 * LCPS)`

#### 4.15.4.1 Professional Codec Support (PCS) — 50%
*What it measures:* Whether the camera records in RAW or Mezzanine (intermediate) formats.
> **Homogenization Note:** This sub-section mirrors the rear camera's **Section 4.11.1** exactly.

| Condition                                                   | Score    |
| :---------------------------------------------------------- | :------- |
| **Supports true RAW video (CinemaDNG, ProRes RAW, BRAW)**   | **10.0** |
| **Supports Mezzanine format (ProRes, APV, DNxHR/HD)**       | **8.0**  |
| **Does not support professional recording formats**         | **0.0**  |

#### 4.15.4.2 Log Color Profile Support (LCPS) — 50%
*What it measures:* Support for Logarithmic gamma curves or Flat profiles.
> **Homogenization Note:** This sub-section mirrors the rear camera's **Section 4.11.2** exactly, including all marketing names.

| Score    | Supported Color Profile                                            |
| :------- | :----------------------------------------------------------------- |
| **10.0** | **True Log: Apple Log / Samsung Log / S-Log3 / V-Log / D-Log....** |
| **5.0**  | **Flat / Cine: S-Cinetone / Cinelike-D / D-Cinelike....**          |
| **0.0**  | **None (Standard contrast only)**                                  |


### D. Computational Photography & AI
*Software features that apply globally to all cameras.*

### 🔹 4.16 Multi-Frame Computational Photography (MFCP)
*Description:* Measures whether the camera system performs automatic multi-frame capture and stacking for still photos to improve noise, dynamic range, and sharpness.
*   **Measurement:** Processing pipeline capability and presence of semantic segmentation.
*   **Unit:** Processing Tier
*   **Significance:** Primary method for smartphones to achieve high dynamic range (HDR) and low noise on small sensors.

| Tier       | Score    | Capability Summary                                   |
| :--------- | :------- | :----------------------------------------------------|
| **Tier 1** | **10.0** | Advanced Semantic & Neural Stacking (Always-on ZSL)  |
| **Tier 2** | **7.5**  | Standard Always-on Multi-Frame HDR                   |
| **Tier 3** | **5.0**  | Conditional / Manual Multi-Frame                     |
| **Tier 4** | **0.0**  | Basic / Single Frame (Legacy)                        |

**Tier Justifications & Rationale:**
*   **Tier 1 (Elite Understanding):** Superior because it *understands* the scene via semantic segmentation (faces, skies, objects). Neural engine integration eliminates shutter lag through continuous background buffering (Zero Shutter Lag (ZSL)).
*   **Tier 2 (Reliable Baseline):** Superior to Tier 3 by guaranteeing highlight retention in every shot without user intervention. Lacks Tier 1's semantic depth, which can occasionally lead to unnatural halos.
*   **Tier 3 (Reactive Processing):** Lack of "always-on" buffering leads to shutter lag or missed highlights if the scene isn't automatically categorized as high-contrast.
*   **Tier 4 (Legacy Capture):** Baseline performance floor. High risk of blown-out highlights and sensor noise due to reliance on traditional single-exposure methods.

> [!NOTE]
> **Why it Matters:** Computational photography allows smaller sensors to perform like larger ones via software-driven stacking. Tier 1 represents the industry ceiling where segmentation is used to treat different parts of the image independently.

### 🔹 4.17 Pipeline Semantic Artificial Intelligence (AI) Processing
*Description:* Automatic, capture-time software logic that understands and segments scenes/subjects **before** the final image file is saved. Enables better portraits, sky processing, skin tones, and subject isolation.
*   **Measurement:** Presence of semantic segmentation features.
*   **Unit:** AI Capability Tier
*   **Significance:** Enables localized High Dynamic Range (HDR) and noise reduction tailored to specific image regions (e.g., skin vs. sky).

> [!NOTE]
> **Capture-Time vs. Gallery-Time AI**
> - **4.17 (Pipeline AI):** Happens **automatically** when you press the shutter (e.g., Apple Photonic Engine). It is invisible to the user and part of the "core" image quality.
> - **4.18 (Post-Capture AI):** Happens **manually** in the gallery/editor (e.g., Samsung Generative Edit). It requires user interaction after the photo is already taken.

| Tier       | Score    | Technical Core                                                                   |
| :--------- | :------- | :--------------------------------------------------------------------------------|
| **Tier 1** | **10.0** | **Neural Semantic Segmentation:** Pixel-level multi-layer classification.        |
| **Tier 2** | **7.5**  | **Object-Based Optimization:** Subject-aware global/local enhancements.          |
| **Tier 3** | **4.0**  | **Basic Metadata AI:** Single-subject face/eye tracking and exposure.            |
| **Tier 4** | **0.0**  | **None:** Legacy pipeline with no scene interpretation.                          |

#### Detailed Justifications & Terms
- **Tier 1:** Performs deep pixel-level differentiation between multiple semantic categories (skin, sky, hair, eyes, teeth, background, and foreground) within the multi-frame pipeline. Enables "Localized Image Processing" where noise reduction and tone-mapping are independently applied per segment. Often requires a dedicated Neural Processing Unit (NPU) for real-time segmentation maps.
- **Tier 2:** Recognizes the high-level subject or "motive" and applies preset global/local enhancements. Effective for visual "pop" (e.g., greener grass, bluer sky) but lacks sub-processing granularity.
- **Tier 3:** Basic focus/exposure priority for human subjects or recognized moving objects. No content-aware color science or segmentation maps are used.


### 🔹 4.18 Post-Capture AI Tools
*Description:* User-initiated editing tools within the gallery/photos app that modify images **after** they have been captured and saved.
*   **Measurement:** Presence of generative and semantic editing tools.
*   **Unit:** Feature Tier
*   **Significance:** Extends creative flexibility by allowing retroactive modifications (erasing objects, expanding backgrounds, relighting).

| Tier       | Score    | Technical Core                                                                    |
| :--------- | :------- | :---------------------------------------------------------------------------------|
| **Tier 1** | **10.0** | **Generative Content Transformation:** Scene-aware creation and outpainting.      |
| **Tier 2** | **7.5**  | **Advanced Semantic Edits:** Content-aware removal and specific-element fixing.   |
| **Tier 3** | **4.0**  | **Basic Algorithmic Fixes:** Standard noise reduction and auto-enhancements.      |
| **Tier 4** | **0.0**  | **None:** No AI-driven editing suite beyond standard crop/filters.                |

#### Detailed Justifications & Terms
- **Tier 1:** Utilizes Large Language Models (LLM) or Diffusion-based generative networks to create new pixel data. Can expand canvases beyond original borders (Outpainting), move/resize objects while reconstructing hidden backgrounds, or "reimagine" the scene via text prompts.
- **Tier 2:** Focuses on sophisticated non-generative fixing. Effectively masks objects using texture patches or re-synthesizes specific elements (like facial expressions) from a burst of shots.
- **Tier 3:** Standard algorithmic fixes that don't use deep generative networks for content creation.


## 🟣 5. Software & Longevity

### 🔹 5.1 Support Longevity
*Description:* The duration of officially promised software support. To ensure relevance for buyers, this score is dynamic and decays as the device ages, focusing on the software life remaining from the current date.
*   **Measurement:** Manufacturer update policy commitment vs. time elapsed since launch.
*   **Unit:** Years (Remaining)
*   **Significance:** Determines the remaining window of security, app compatibility, and feature updates.

#### Scientific Scoring Model (Dynamic Decay)
The longevity score is calculated based on **Remaining Support Years** at the time of evaluation. 

**1. Calculate Remaining Years:**
`Remaining_Years = End_of_Support_Date - Current_Date`
*   **End_of_Support_Date:** The date when official manufacturer support ends (calculated precisely step by step below).
*   **Current_Date:** The present date (dynamic).

**2. Calculate Dynamic Score:**
`Score = 10 * (log(Remaining_Years) - log(Support_Years_Min)) / (log(Support_Years_Max) - log(Support_Years_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Support_Years_Max
*   **Min Score (0.0):** ≤ Support_Years_Min
> [!NOTE]
> **Why Logarithmic?** The value of support diminishes over time as hardware ages. The difference between 1 and 3 years is critical for security. The difference between 5 and 7 years is less impactful as many users upgrade before then.
> **Why Dynamic?** Software support isn't static. A flagship with "7 years of updates" is a 10/10 on day one, but if you buy it 6 years later, it only has 1 year of support left. This model ensures the score accurately reflects the value to a buyer *today*.

#### 🔹 Search & Categorization Recipe (A to Z)
Follow these steps strictly to determine the **End of Support Date** value:

**Step A: Launch Date Identification**
*   Find the **Global Commercial Launch Date** (e.g., January 2024).

**Step B: Search for Raw Manufacturer Terms**
Search for the official commitment for the specific model. Record the verbatim phrases needed to determine:
1.  **OS End Date** (e.g., "4 generations of Operating System (OS) updates").
2.  **Security End Date** (e.g., "Security updates until Jan 2029").

**Step C: Translate Raw Terms to Potential End Dates**
Translate the raw terms from Step B into specific calendar dates:
*   **"X Generations of OS updates"** => **OS End Date** = `Launch Date + X Years` (Note: **1 Gen = 1 Year**, see Justification #1 below).
    *   *Example:* Launch Jan 2024 + "4 generations" = Jan 2028 (**OS End Date**).
*   **"Security updates until [Date]"** => **Security End Date** = `[Date]`.
    *   *Example:* "Until Jan 2029" = Jan 2029 (**Security End Date**).
*   **"X Years of Security Updates"** => **Security End Date** = `Launch Date + X Years`.

**Step D: Apply the "Enterprise Extension" (If applicable)**
If the device is an **Enterprise Edition** or **Business Edition**:
1.  Take the **Security End Date** calculated in Step C.
2.  Add the official **Enterprise Extension (Years)** (usually +1 or +2 years) to that date.
    *   `Final Security End Date = Security End Date + Extension (Years)`.

**Step E: Determine the Final "End of Support Date" Anchor**
Find the **End of Support Date** used in the dynamic formula:
1.  **End of Support Date** = `Max(OS End Date, Final Security End Date)`.
    *   *Note:* Use the standard **Security End Date** if no Enterprise Extension applies.

#### 💡 Justification of Rules & Assumptions
The conversion from marketing terms to numerical years is based on a decade of documented industry data:

1.  **The "1 Generation = 1 Year" Rule:**
    - **Observed Data:** Since 2014, both Google (Android) and Apple (iOS) have released exactly **one major version per year** without exception.
    - **Android Cadence:** 11 (2020), 12 (2021), 13 (2022), 14 (2023), 15 (2024).
    - **iOS Cadence:** 14 (2020), 15 (2021), 16 (2022), 17 (2023), 18 (2024).
    - **Conclusion:** A promise of "4 Generations" is functionally equivalent to a 4-year software shelf-life.

2.  **The "Security-First" Anchor (Why Max(OS End Date, Final Security End Date)?):**
    - **Scoring Rationale:** Using the "earliest" date (**OS End Date**) would be overly conservative and factually misleading. A device that stops receiving OS updates (e.g., stuck on Android 13) but continues to receive security patches is still a **fully functional and safe device** for 99% of use cases.
    - **Hard EOL (End of Life) Definition:** A smartphone's true longevity limit is reached only when it becomes a security liability. At that point, it can no longer be safely used for banking, health data, or work. 
    - **The App Lifecycle:** Major apps stay compatible with older OS versions for several years. For example, Google Play Services often supports Android versions that are 4-5 years old. This means the device remains a "smart" phone as long as it is secure.
    - **Conclusion:** By using the **latest** (most future) date between the OS and Security lifespans, our score accurately reflects the device's **Safe Utility Lifespan**, which is the most critical metric for long-term ownership.

3.  **Enterprise Extension Baseline:**
    - **Standard practice:** Manufacturers like Samsung explicitly market Enterprise Edition extensions as a time-based bonus (e.g., "+1 year of security patches") over the standard consumer model.

### 🔹 5.2 System Cleanliness & Control (SCC)
*Description:* Evaluates the out-of-box software experience in terms of preinstalled bloatware, user control, and presence of system ads.

> [!NOTE]
> **Cross-Reference (Battery Endurance Integration):**
> The composite score calculated in this section (**SCC_Score**) is directly consumed by **Section 8.1 (Software Inefficiency Modifier)** as a proxy for background process power consumption. A lower cleanliness score indicates a higher volume of un-optimized manufacturer background tasks, services, and telemetry, which prevent the hardware processor cores from entering deep low-power sleep states.

#### Design Rationale & Methodology
Traditional SCC metrics require subjective hands-on testing that cannot be automated from public data. However, since bloatware and ad policies are defined universally at the **platform/skin level** (e.g., all Samsung One UI phones share the identical core app bundle and ad policy), we evaluate the **three distinct cleanliness dimensions** natively for each known skin. 

> [!IMPORTANT]
> **ROM (Read-Only Memory) Region Baseline:**
> Since bloatware loads and system advertisement policies can vary significantly between regional software builds (e.g., domestic Chinese ROM variants vs. Global ROM variants), all scores in the lookup tables are based on the **Global Commercial ROM variant** (the software shipped on devices sold in international markets) by default.
> 
> **Handling Regional Builds:**
> If a device explicitly runs a regional software build (e.g., a Chinese domestic model running `ColorOS (China)`):
> 1. **Skin-Level Match:** If a regional skin variant exists in the `SKIN_LOOKUP_TABLE` (e.g., `OriginOS` representing Vivo's Chinese ROM), the lookup matches that row.
> 2. **Manual Override:** If no regional row is defined in the lookup table, the global default row is used as a baseline, but the individual scores (`PAL` (Preinstalled App Load), `UC` (User Control), `SA` (System Advertisements)) **MUST** be manually overridden in the device's JSON  record based on verified review or teardown evidence of that specific regional build's bloatware and advertisement policy.
> 3. **Override Documentation Alert:** When a manual override is performed on the default lookup scores, a dedicated `"alert"` field must be populated in the device's JSON record. This field must contain:
>    - A clear explanation of the engineering rationale behind the override (e.g., specifying the regional build and why it diverges from the Global Commercial ROM baseline).
>    - Detailed justifications for the adjusted scores of the three cleanliness dimensions (Preinstalled App Load [PAL], User Control [UC], and System Advertisements [SA]) citing verified references to valid sources (e.g., specific URLs, forum teardowns).
>    - If no override is performed, this field must be set to `"N/A"` (Not Applicable).

**Final Composite Formula:** 
`SCC = (0.40 * PAL) + (0.30 * UC) + (0.30 * SA)`

---

#### 5.2.1 Preinstalled App Load (PAL) — 40%
*Description:* Measures the absolute volume of non-core applications present at first boot.
*   **Measurement:** Volume of preinstalled first-party duplicates and third-party apps.
*   **Unit:** Tier Score (0-10)
*   **Significance:** Determines the initial storage overhead and system resource consumption by non-essential background processes.

| Tier       | Score    | Definition                                                                                        |
| :--------- | :------- | :------------------------------------------------------------------------------------------------ |
| **Tier 1** | **10.0** | **Minimal / Core Only:** No third-party applications or redundant first-party duplicates.         |
| **Tier 2** | **6.0**  | **Moderate Proprietary:** First-party duplicates present (e.g., two browsers), rare third-party.  |
| **Tier 3** | **3.0**  | **Significant Bloat:** Multiple pre-loaded social media apps, games, and partner software.        |
| **Tier 4** | **0.0**  | **Extreme Bloat:** Dozens of third-party apps and promotional "Hot Apps" folders out-of-box.      |

#### 5.2.2 User Control (UC) — 30%
*Description:* Measures the user's ability to natively rid the system of unwanted apps without developer tools (ADB).
*   **Measurement:** System-level uninstallation permissions.
*   **Unit:** Tier Score (0-10)
*   **Significance:** Empowers the user to reclaim storage and privacy by removing or silencing unwanted manufacturer software.

| Tier       | Score    | Definition                                                                                        |
| :--------- | :------- | :------------------------------------------------------------------------------------------------ |
| **Tier 1** | **10.0** | **Fully Uninstallable:** Almost all non-essential apps can be completely deleted.                 |
| **Tier 2** | **5.0**  | **Disabling Only:** Many apps cannot be deleted but can be natively hidden and "disabled".        |
| **Tier 3** | **0.0**  | **Highly Restrictive:** Core bloatware runs in the background and cannot be turned off normally.  |

#### 5.2.3 System Advertisements (SA) — 30%
*Description:* Measures intrusive monetisation within the OS UI (notifications, settings, native apps).
*   **Measurement:** Presence of advertisements in system-level interfaces.
*   **Unit:** Tier Score (0-10)
*   **Significance:** Impacts user experience and background power draw. The presence of system-level advertisements directly indicates active, background ad-fetching services and telemetry tracking modules. Even when ads are not actively displayed on the screen, these background daemons consume CPU (Central Processing Unit) cycles and trigger network polling, preventing the system from entering deep low-power sleep states (C-states).

| Tier       | Score    | Definition                                                                                        |
| :--------- | :------- | :------------------------------------------------------------------------------------------------ |
| **Tier 1** | **10.0** | **Ad-Free:** Zero system-level advertisements or promotional pushes.                              |
| **Tier 2** | **5.0**  | **Opt-Out / Occasional:** Native app promotions exist but can be permanently deactivated.         |
| **Tier 3** | **0.0**  | **Intrusive / Persistent:** Mandatory UI ads and lock screen promotions that cannot be disabled.  |

---

#### Master Skin Lookup Table

Use this matrix to assign the `subscore` for each of the three dimensions based purely on the `skin` field.

| Platform / Skin                           | PAL Score (40%) | UC Score (30%)  | SA Score (30%)  |
| :---------------------------------------- | :-------------: | :-------------: | :-------------: |
| **iOS**                                   | **10.0**        | **10.0**        | **10.0**        |
| **Pixel UI / Stock Android**              | **10.0**        | **10.0**        | **10.0**        |
| **Samsung One UI**                        | **3.0**         | **5.0**         | **5.0**         |
| [...]                                     | [...]           | [...]           | [...]           |

> [!IMPORTANT]
> **Source of Truth:** For the full list of all 15+ supported software skins and their authoritative scores, refer to the **Skin Lookup Table** in [proposed_data_structure.md].

---

#### Per-Skin Justification

Each entry below explains **why** the specific PAL / UC / SA scores were assigned. All claims are derived from publicly available reviews, manufacturer documentation, and community reports.

**iOS** — PAL 10.0 · UC 10.0 · SA 10.0
Apple does not pre-install any third-party apps. All first-party apps (Tips, Stocks, Compass, etc.) have been fully deletable since iOS 10. Zero system-level advertisements or promotional notifications.

**Pixel UI / Stock Android** — PAL 10.0 · UC 10.0 · SA 10.0
Ships with core Google apps only (Gmail, Maps, Photos). No third-party preloads. All apps are uninstallable or disablable via standard settings. No system-level ads.

**AOSP / Fairphone OS / Nothing OS** — PAL 10.0 · UC 10.0 · SA 10.0
Pure AOSP has minimal apps. Fairphone OS is AOSP-based with no extras. Nothing OS is praised as a "clean, minimal interface" with "lack of carrier bloatware" (GadgetHacks). Nothing reversed Meta preloads after user backlash by making them fully uninstallable. No system ads.

**Motorola MyUX / Hello UI** — PAL 6.0 · UC 10.0 · SA 10.0
Near-stock Android with Moto-specific gesture tools and Ready For desktop mode. Light first-party additions (Moto app, FM Radio). Carrier variants may add more. Most preinstalled apps are fully uninstallable. No system-level ads reported.

**Sony Xperia UI / Sharp AQUOS / Nokia** — PAL 6.0 · UC 10.0 · SA 10.0
Near-stock Android. Sony adds Cinema Pro, PS Remote Play, Music app. Nokia (HMD, now operating as HMD Global) adds My Phone. Sharp AQUOS is near-stock for the Japanese market. All first-party extras are fully uninstallable. No system ads.

**ASUS ZenUI / ROG UI** — PAL 6.0 · UC 10.0 · SA 10.0
Light proprietary additions (MyASUS, Armoury Crate on ROG). Recent ZenUI versions have evolved to a cleaner, more stock-like experience with fewer preinstalls. Most third-party and first-party apps are fully uninstallable via standard settings without needing ADB (confirmed by Droix.net, Cashify). No system-level ads.

**Redmagic OS** — PAL 3.0 · UC 10.0 · SA 10.0
Ships with Facebook, TikTok, and Booking.com preloaded. However, Redmagic officially confirms users can fully uninstall all preloaded apps (redmagic.gg). Users report a clean experience after initial setup cleanup (Reddit). The OS is considered close to stock Android with no system-level ads.

**Funtouch OS (Vivo)** — PAL 6.0 · UC 5.0 · SA 10.0
Vivo's global skin, distinct from OriginOS (China market). Ships with Jovi Home, V-AppStore, and light proprietary apps. Global users report "no ads or bloat" (Reddit r/Vivo). Funtouch OS 14 allows uninstalling some bloatware and disabling "hot apps," but core Vivo services cannot be removed without ADB (Android Debug Bridge), hence UC = 5.0. No system-level ads on global variant.

**LG UX / HTC Sense (Legacy)** — PAL 6.0 · UC 5.0 · SA 5.0
Legacy skins for discontinued brands. LG added SmartWorld, LG Health, Dual App — moderate first-party duplicates. HTC featured BlinkFeed as a default home panel with promotional content. Many apps could be disabled but not fully uninstalled without ADB.

**OxygenOS (OnePlus)** — PAL 3.0 · UC 5.0 · SA 5.0
Historically stock-like, OxygenOS has significantly increased bloatware since merging its codebase with ColorOS. As of 2024, ships with Meta App Installer/Manager/Services, LinkedIn, games (Candy Crush, Block Blast), Amazon apps, and region-specific apps like Zomato and Swiggy (documented by Android Police, Gadgets360). Meta services can only be disabled, not fully removed. Promotional notifications via a "Push" service have been reported, but can be blocked via settings.

**Samsung One UI** — PAL 3.0 · UC 5.0 · SA 5.0
Ships with 30+ preinstalled apps including Samsung duplicates (Browser, Email, Notes, Bixby, Samsung Free, SmartThings), Google suite, and Meta apps (Facebook). Confirmed by ZDNet, Android Police. Many Samsung apps (Bixby, Samsung Internet, SmartThings) can be disabled but not uninstalled. Ads appear in Galaxy Store, Samsung Weather, and Samsung Health but can be opted out of via settings. Samsung committed to reducing ads since 2021 (SamMobile).

**ColorOS / Realme UI / OriginOS / Vivo** — PAL 3.0 · UC 5.0 · SA 5.0
These skins share the same ColorOS codebase (OPPO). Realme devices ship with ~58 apps at boot, including ~12 inessential first-party apps and ~10 third-party apps (UNB.com.bd). "Hot Apps/Games" promotional folders are preloaded. Many apps can be uninstalled, but disabling some core system apps (e.g., Phone Manager) may throttle CPU performance (Reddit). Ads labelled "content recommendations" appear in system apps but can be permanently disabled via settings.

**Honor MagicOS** — PAL 3.0 · UC 5.0 · SA 5.0
Chinese variants have extensive bloat. Global models are described as having a "slimmer skin" (YouTube reviews). Many apps can be disabled or uninstalled, but core Honor services (Magic Mobile Service, Honor ID) cannot be removed (XDA Forums). Reports of ads appearing in Weather, Clock, and Themes apps on certain regions/models (Reddit), though the Magic 6 Pro review noted "no weird ads" (YouTube).

**ZTE MiFavor UI / MyOS** — PAL 3.0 · UC 5.0 · SA 5.0
Moderate bloatware with ZTE-specific apps and some third-party preloads. Apps can be disabled via settings but deep removal requires ADB. Occasional promotions in system apps, though not as aggressive as Xiaomi or Tecno.

**HyperOS (Xiaomi) / Huawei EMUI** — PAL 0.0 · UC 5.0 · SA 0.0
Both ship with extreme bloat. Xiaomi pre-installs GetApps, Mi Video, Mi Browser, Mi Remote, ShareMe, and dozens more. Huawei includes AppGallery, Huawei Browser, Petal Search. Apps can be disabled via settings — Xiaomi's MSA (MIUI System Ads) authorization can be revoked — but deep removal requires ADB. System-wide ads persist in File Manager, Security app, and notification drawer (Gizchina, Android Authority). Huawei EMUI shows ads in AppGallery and Browser.

**MIUI (Legacy Xiaomi)** — PAL 0.0 · UC 0.0 · SA 0.0
Worst-in-class for older Xiaomi devices pre-HyperOS. Dozens of preinstalled apps plus "Hot Apps" auto-download. Many apps cannot be disabled or uninstalled without ADB or root. Lock screen ads, notification spam, and ads embedded in Settings, File Manager, and Security app (Technastic, XDA Forums, Android Authority).

**Tecno HiOS / Infinix XOS / Itel OS** — PAL 0.0 · UC 0.0 · SA 0.0
Heavy preloads: Palm Store, AHA Games, Hola/Phoenix Browser, Visha Player, YoParty, Beats Party, plus multiple auto-installing app folders. Core bloatware is deeply integrated and runs in the background; removal without root or ADB typically fails (PhoneWorld.com.pk). Lock screen ads, notification panel ads, and file manager ads are persistent and often mistaken for malware by users (TechPoint Africa, Reddit).

### 🔹 5.3 AI Feature Suite
*Description:* Evaluates the *software features* and practical AI tools available to the user. This measures "what you can do" (features), distinct from **Section 6.4** which measures "how fast it runs" (hardware power).
*   **Measurement:** Manufacturer feature lists, OS documentation, and verified reviews.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Determines the breadth of AI tools available to the user, regardless of underlying hardware speed.

**Guiding Question:** *"What useful AI features does the user have access to, and how independently can the phone run them?"*

**Structure:** 6 binary features with weighted scoring.

> [!NOTE]
> **Post-capture AI editing** (object removal, fill, etc.) is scored in **Section 4.18** and is excluded here to avoid double-scoring.

#### AI Capability Features

| Feature                          | Weight   | Justification                                                                                |
| :------------------------------- | :------- | :------------------------------------------------------------------------------------------- |
| **Visual Screen Search**         | **20%**  | **#1 Usage:** Identified as the most frequently used AI tool (e.g., Circle to Search).       |
| **Meeting/Call Transcription**   | **20%**  | **Killer App:** Primary driver for professional/student users; high impact for productivity. |
| **Content Summarization**        | **20%**  | **Daily Utility:** Core pillar for triaging information (Mail, Web, Notes). High retention.  |
| **On-Device Reliability**        | **20%**  | **Foundation:** Essential for privacy/offline speed; 75% of users prioritize local AI.       |
| **Live Translation**             | **15%**  | **Value/Frequency:** High perceived value but lower recurring daily usage than search.       |
| **Writing Tools**                | **5%**   | **Utility:** System-wide assistance; lowest recurring necessity among the six features.      |

**Weighting Rationale:**
The weights are calibrated based on 2024 usage studies (e.g., Samsung Galaxy AI survey) and reviewer benchmarks (e.g., Pixel 9 Call Notes). Visual Search and Transcription are prioritized as the most "tangible" and frequently used AI tools, while On-Device reliability serves as the necessary privacy foundation for all data-sensitive operations.

**Formula:**
```
Score_5.3 = (2.0 * VisualSearch) + (2.0 * Transcription) + (2.0 * Summarization) + (2.0 * OnDevice) + (1.5 * Translation) + (0.5 * Writing)
```
Where each feature = 1 if present, 0 if absent. Max score = 10.0.

#### Master AI Marketing Name Reference

Use this reference to map brand-specific terms to the 6 core AI features.

**1. Visual Screen Search (20%)**
*Definition: Identifying on-screen items without leaving the current app.*
- Circle to Search (Google, Samsung, Xiaomi, Oppo, OnePlus, Realme, Honor, Vivo, Motorola, Asus, Nothing)
- Visual Intelligence / Visual Look Up (Apple)
- [...] *(See full list in [proposed_data_structure.md])*

**2. Live Speech Translation (15%)**
*Definition: Real-time voice translation during calls or in-person audio.*
- Live Translate (Samsung, Google)
- Interpreter / Interpreter Mode (Samsung, Google, ...)
- [...] *(See full list in [proposed_data_structure.md])*

**3. Content Summarization (20%)**
*Definition: Distilling key points from articles, notes, or long-form documents.*
- Note Assist / Browsing Assist (Samsung)
- Recorder Summarize (Google)
- [...] *(See full list in [proposed_data_structure.md])*

**4. AI Writing Tools (5%)**
*Definition: System-wide text rewriting, tone adjustment, or proofreading.*
- Chat Assist / Keyboard AI (Samsung)
- Magic Compose / Help me write (Google, Gboard)
- [...] *(See full list in [proposed_data_structure.md])*

**5. Meeting / Call Transcription (20%)**
*Definition: Converting recorded or live speech into text logs with speaker ID.*
- Transcript Assist (Samsung)
- Recorder: AI Transcription (Google)
- [...] *(See full list in [proposed_data_structure.md])*

**6. On-Device Reliability (20%)**
*Definition: Ability to process core AI features offline via local NPU/Models.*
- "Process data only on device" toggle (Samsung, Google, Xiaomi, Apple)
- Gemini Nano (Google, Samsung, Motorola, Realme)
- [...] *(See full list in [proposed_data_structure.md])*

**Unlisted Manufacturers (Sony, Nothing, etc.)**
- Sony Xperia / Nothing Phone: These brands standardly rely on **Google (Circle to Search, Gemini Nano)**. Only score features explicitly confirmed to be active via the Google app suite.


## 🟣 6. Processing Power & Performance

#### 6.1.0 CPU Core Architecture Reference

**Master Scoring Table** (used across all CPU performance calculations)

This table provides the authoritative CPU core architecture scores used throughout the scoring system, including:
- Section 6.1 Method C: Multi-Thread Performance
- Section 6.2 Method C: Single-Thread Performance
- Section 8.1 for Battery Endurance Scoring

**Scoring Basis:** Based on IPC (Instructions Per Cycle—the number of instructions a processor executes in a single clock cycle) performance and modern architecture capabilities.

| CPU Core Architecture        | CPU Score | Ref Freq (GHz) | Typical L2 (KB) |      ISA Gen     | ISA Gen Score |
|:-----------------------------|:---------:|:--------------:|:---------------:|:-----------------|:-------------:|
| **C1-Ultra (Lumex)**         |   10.00   |      4.21      |      2048       |      ARMv9.3     |     1.10      |
| **Apple Everest (A18/Pro)**  |   10.00   |      4.05      |     16384       |      ARMv9.2     |     1.08      |
| **Qualcomm Oryon Gen 2**     |   9.80    |      4.32      |     12288       |      ARMv8.7     |     1.05      |
- [...] *(See full list in [proposed_data_structure.md])*

[!NOTE]
**Internal Normalization Anchors vs. Vendor Specs**
The `reference_frequency_ghz` and `typical_l2_kb` columns, as well as several internal core codenames (e.g., Apple's "Sawtooth" or "Blizzard"), act as **internal mathematical normalization anchors** for the scoring model. They are inferred or approximated fields used to establish a consistent mathematical baseline across vastly different architectures. They should **not** be interpreted as universally authoritative public vendor specifications. 
 
For example: Apple does not officially publish a canonical "reference frequency" or private L2 cache capacity for individual A-series cores, and Qualcomm's Snapdragon 8 Elite documentation explicitly notes that its maximum CPU speed varies depending on the platform version (including a 4.32 GHz variant). These fields exist strictly within this framework to provide a stable mathematical baseline for the `Actual_Frequency / Reference_Frequency` normalization ratio and the penalty prediction modules.


### 🔹 6.1 CPU Multi-Core Performance
*Description:* Measures actual delivered CPU performance in standardized workloads, ensuring the device can handle heavy multitasking and sustained processing.
*   **Measurement:** Geekbench 6 Multi-Core Score.
*   **Unit:** Points (0–10)
*   **Significance:** Primary indicator of sustained CPU workloads, gaming physics, and background multitasking.

#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct Geekbench 6 score is available. It provides the most accurate representation of real-world performance.
*   **Formula:** `Score = 10 * (log(Score) - log(CPU_GB6_Multi_Score_Min)) / (log(CPU_GB6_Multi_Score_Max) - log(CPU_GB6_Multi_Score_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ CPU_GB6_Multi_Score_Max
*   **Min Score (0.0):** ≤ CPU_GB6_Multi_Score_Min
[!NOTE]
**Why Logarithmic?** Performance utility follows diminishing returns. A 1000-point jump between a baseline 1500-point phone and a capable 2500-point mid-ranger is transformative for daily usability. In contrast, a 1000-point jump between a 10000-point flagship and an 11000-point gaming beast is a marginal improvement noticeable only in extreme multitasking or specialized competitive gaming.

#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.
1.  **Identify Neighbors via Feature Distance (Minimum Variance):** Find the 3 devices that are statistically closest across **all** CPU-relevant hardware components.
    *   **Search Space:** All phones with known Geekbench 6 Multi-Core scores (Method A), **excluding the target device** itself.
    *   **Distance Metric:** Euclidean Distance.
        *   `Distance = Sqrt( (RCTS_norm_Diff)² + (Penalty_MTI_Diff)² + (Penalty_TDSI_Diff)² + (Penalty_CFEI_Diff)² )`
        *   *Where "Diff" is the difference between Target and Neighbor values for each component:*
            *   `RCTS_norm` (Raw CPU Throughput Score, normalized, see Method C): The core active compute capability.
            *   `Penalty_MTI` (§6.1 Step 5): The Memory Technology Index (MTI) bandwidth starvation penalty. This isolates the actual active memory bottleneck impact on performance.
            *   `Penalty_TDSI` (§6.1 Step 5): The Thermal Dissipation Stability Index (TDSI) cooling throttle penalty. This captures the active thermal bottleneck currently restricting core capability.
            *   `Penalty_CFEI` (§6.1 Step 5): The Cache & Fabric Efficiency Index (CFEI) penalty. This represents the active fabric latency bottleneck.
        *   **Scientific & Mathematical Rationale:** Since the 5-Step Performance Pipeline from Method C defines the overall performance score as a direct linear subtraction of the penalties from the core compute capacity (`Predicted_Score = RCTS_norm - Sum(Penalty_S)`), every single component enters the final performance metric with an absolute weight of exactly 1.0. While in the vast majority of cases the core compute difference squared (`(RCTS_norm_Diff)²`) will be much greater than the penalty differences, keeping all components allows the model to catch and correctly group highly unbalanced outlier devices that suffer from exceptionally high dynamic penalties.
    *   **Selection:** Pick the 3 distinct neighbors with the smallest `Distance`.
2.  **Calculate Correction Ratio:**
    *   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
        *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
    *   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
        *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.
3.  **Apply to Benchmark:**
    *   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
    *   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

#### Method C: Predicted Calculation (Tertiary)
Used as a standalone fallback if no neighbors exist, or as the **Predictor** for Method B.

##### 📖 Executive Summary & Roadmap: CPU Multi-Core Modeling
Evaluating mobile CPU performance requires much more than simply adding up core speeds or counting cores. Modern smartphones utilize highly complex, **heterogeneous multi-cluster CPU complexes** configured to balance high-burst speeds with strict thermal and battery limitations.
 
To model this physical reality with accuracy, **Method C** uses a **5-Step Pipeline** that transforms raw silicon specifications into a realistic, human-perceptual performance score.
 
###### 🧭 The 5-Step Performance Pipeline Map
Below is the mathematical journey a device's raw CPU specifications take through the modeling framework:
 
1. **Step 1: Core Frequency Soft-Saturation (γ)** 
    * *What it does:* Analyzes each CPU core's clock speed. High overclocked frequencies are scaled down using a core-count-based **γ (gamma)** exponent to model voltage walls and latency overhead.
2. **Step 2: Local Intra-Cluster Scaling (α)** 
    * *What it does:* Groups identical cores into their respective hardware clusters. A parallel-scaling **α (alpha)** exponent is applied to model diminishing parallel returns (cores competing for local Level 2 (L2) cache).
3. **Step 3: Raw Throughput Aggregation (RCTS)**
    * *What it does:* Sums the parallel-adjusted capacities of all clusters to compute the total raw processing throughput demand of the CPU.
4. **Step 4: Global Perceptual Normalization (RCTS_norm)**
    * *What it does:* Converts the raw throughput into a 0.0 to 10.0 scale using a **logarithmic function** to match human sensory perception (diminishing return utility).
5. **Step 5: Non-Linear Deficit Penalties, Final Score & Abort Protocol**
    * *What it does:* Evaluates three support subsystems (Memory, Cooling Thermals and Cache), subtracts non-linear penalties from the normalized demand to compute the final score, and halts execution via a strict **Process Abort Protocol** if the score falls outside `[0.00, 10.00]`.
 
 
##### 🧠 The Physics of CPU Architecture & Heterogeneity
Modern System-on-Chip (SoC) architectures do not use identical cores. Instead, they group different types of specialized cores into **Clusters** to optimize performance:
 *   **Best Performing Cores:** Large, extreme-performance cores dedicated to brief, heavy single-threaded bursts (like launching an app).
 *   **Second Best Performing Cores:** Medium-high speed workhorse cores that handle active multitasking, heavy browsing, and gaming physics.
 *   **Third Best / Fourth Best Performing Cores:** Small, ultra-low power cores that run background syncing, Operating System (OS) maintenance, and music playback while preserving battery.
 
###### 🧪 Standardized Rank-Based CPU Cluster Nomenclature
To enable robust, automated parsing and maintain microarchitectural neutrality across all hardware platforms, this scoring framework adopts a strictly standardized, rank-based nomenclature for CPU core clusters: `best`, `second_best`, `third_best`, and `fourth_best`.
 
These cluster designations are defined in absolute terms of relative peak computing capability (Instructions Per Cycle [IPC] multiplied by maximum clock frequency) rather than vendor-specific marketing terms like "Prime", "Performance", or "Efficiency".

###### Rationale for Rank-Based Nomenclature
1. **Elimination of Schema Ambiguity:** High-performance mobile CPU layouts are highly heterogeneous and vary widely between vendors. For example, some custom architectures (such as Apple Silicon) utilize a symmetric dual-cluster configuration comprising only high-performance cores and highly efficient cores. Under marketing-biased schemas, mapping these designs forces arbitrary decisions—such as classifying the performance cluster as a "Prime" cluster and leaving the "Performance" schema key completely empty or unmapped. This structural asymmetry creates parsing exceptions and data schema fragility.
2. **Prevention of Parsing & Validation Errors:** Automated database parsers and verification loops rely on strict path-referenced JSON hooks. By standardizing the clusters strictly by their relative performance ranking from highest to lowest (`best` to `fourth_best`), the database schemas maintain total structural consistency across all chipsets. The single-core predictive model can always query the highest-performing cluster uniformly via the static path `clusters.best.architecture`, completely avoiding vendor-specific mapping logic and potential parsing failures.
3. **Microarchitectural Neutrality:** Modern designs frequently blur the lines between traditional cluster definitions (e.g., integrating a mix of medium and high cores in a 1+3+4 or 1+5+2 layout). Rank-based neutral naming provides a robust mathematical classification that fits any physical topology, from dual-cluster Apple architectures to complex quad-cluster Snapdragon platforms.

###### Layer 1: Local Intra-Cluster Scaling (Local Silicon Contention)
*   *The Constraint:* Cores within the same cluster are placed next to each other on the silicon die, sharing a local L2 cache and cluster-level fabric. As more cores run concurrently, they contend for L2 cache access and generate local thread synchronization overhead.
*   *How we model it:* In **Step 2**, we apply the **Parallel-Adjusted Core Count (PACC)** (`CoreCount^α`), using a decaying alpha exponent to reduce the incremental value added by each additional core.
 
###### Layer 2: Global Inter-Cluster Scaling (Systemic Platform Support)
*   *The Constraint:* Even if individual clusters are efficient internally, they must communicate via the DynamIQ Shared Unit (DSU — a cluster shared unit coordinating different cores) interconnect. They compete for bandwidth on the Low-Power Double Data Rate (LPDDR) RAM memory bus, share the physical thermal dissipation limits of the phone's chassis, and share a common shared Level 3 (L3) Cache or System Level Cache (SLC).
*   *How we model it:* In **Step 5**, we evaluate these platform-wide dependencies using a non-linear deficit penalty model, treating Memory, Thermals and Cache as strict constraints rather than optional bonuses.

**Method C** calculates performance by scoring every cluster found in the device's SOC reference (§6.1.0) individually before aggregating them into a system-wide throughput model.

**Step 1: Core Frequency Soft-Saturation (γ)**
Before assessing how cores behave in parallel, we must first determine the physical yield of each individual core at its given operating frequency. While frequency scaling is generally linear near a core's sweet spot, pushing cores to extreme frequencies (overclocking) hits a "voltage wall" where heat and power scale exponentially but performance does not. Furthermore, at high clock speeds, internal CPU caches (L2/L3) and memory buses cannot scale in tandem, resulting in nanosecond-level latency mismatches that waste clock cycles.

We model this sub-linear frequency scaling using a soft-saturation exponent **γ (gamma)**.
1.  **Frequency Ratio (R_i):** `Actual_Frequency_i / Reference_Frequency_i`
2.  **Core Yield (CY_i):** `CY_i = CAS_i * (R_i ^ γ)`
    *   `CAS_i`: CPU Architecture Score from the **§6.1.0 Reference Table**.
    *   `γ` is determined by the **number of cores in the cluster**, which serves as a highly accurate proxy for the core's architectural class and typical operating range:
        *   `γ(1 core) = 0.93`: Ultra-high performance cores (typically the "best" cluster) pushed to maximum frequency limits, where frequency scaling is highly saturated due to the physical voltage wall.
        *   `γ(2 cores) = 0.95`: High-performance clusters operating at moderate-to-high frequency bands (often the "best" cluster in dual-prime layouts, or "second_best" cluster).
        *   `γ(3 cores) = 0.96`: Mid-to-high performance clusters operating under standard frequency envelopes.
        *   `γ(4 cores) = 0.97`: Mid-range clusters (typically the "second_best" or "third_best" cluster) operating near the physical linear scaling sweet spot.
        *   `γ(5-6 cores) = 0.98`: High-efficiency clusters running at conservative, highly efficient clock speeds.
        *   `γ(7-8 cores) = 0.99`: Large efficiency clusters or homogeneous budget processors operating in low-frequency bands. Scaling is nearly linear, but a perfect 1.00 is physically impossible due to silicon interconnect and cache latency overheads.

    [!NOTE]
    **Why the Instruction Set Architecture (ISA) Multiplier is Omitted in Section 6.1**
    Instruction Set Architecture (ISA) is the core "dictionary" of hardware commands a Central Processing Unit (CPU) understands. While the ISA multiplier is included in Section 6.2 to model single-threaded peak efficiency, it is omitted in Section 6.1 because multi-core throughput is heavily dominated by systemic hardware limits—specifically memory bandwidth, cache capacity, and thermal stability—rather than individual instruction execution rates. A compressed multi-core ISA modifier (with a small 1% to 3% spread) could be introduced in future revisions of the model, but it is currently neglected due to this extremely low physical impact, which becomes even less significant after the global logarithmic normalization is applied.

**Step 2: Per-Cluster Effective Throughput (CET)**
Core scaling is sub-linear. Doubling the cores does not double the performance due to synchronization overhead, cache contention, and shared memory pressure (Amdahl's Law). We model this physical constraint by calculating a Parallel-Adjusted Core Count before applying the base architecture score.

1.  **Parallel-Adjusted Core Count (PACC):** `PACC_i = CoreCount_i ^ α`
    *   Where **α is determined by core count**, ensuring robust scaling for any cluster topology.
    *   `α(1 core)`  = 1.000 (Identity)
    *   `α(2 cores)` = 0.940 (Minimal overhead)
    *   `α(3 cores)` = 0.900
    *   `α(4 cores)` = 0.870
    *   `α(5 cores)` = 0.850
    *   `α(6 cores)` = 0.830
    *   `α(7 cores)` = 0.810
    *   `α(8 cores)` = 0.800 (Heavy overhead)
> [!NOTE]
    > **Scientific Rationale for α (Local Core Scaling Physics):** 
    > This specific sequence defines a **smooth, monotonic decay** in parallel efficiency *within* a cluster. To see the direct relationship between the exponent **α** and the real-world efficiency of the cluster, we look at the **Total Core Yield** (CoreCount^α), the **Average Scaling Efficiency** (Total Yield / Core Count), and the **Incremental Value** added by each additional core (Yield_N - Yield_N-1):
    > * **Alpha Core Scaling Reference Table:**
    > 
    > | Cores (N) | Alpha (α) | Total Core Yield (N^α) | Average Cluster Efficiency | Incremental Efficiency of Last Core |
    > | :-------: | :-------: | :--------------------: | :------------------------: | :---------------------------------: |
    > |   **1**   |   1.000   |    **1.000** cores     |           100.0%           |         100.0% (Base Core)          |
    > |   **2**   |   0.940   |    **1.919** cores     |           95.9%            |           +0.919 (91.9%)            |
    > |   **3**   |   0.900   |    **2.688** cores     |           89.6%            |           +0.769 (76.9%)            |
    > |   **4**   |   0.870   |    **3.340** cores     |           83.5%            |           +0.652 (65.2%)            |
    > |   **5**   |   0.850   |    **3.924** cores     |           78.5%            |           +0.584 (58.4%)            |
    > |   **6**   |   0.830   |    **4.444** cores     |           74.1%            |           +0.520 (52.0%)            |
    > |   **7**   |   0.810   |    **4.908** cores     |           70.1%            |           +0.464 (46.4%)            |
    > |   **8**   |   0.800   |    **5.278** cores     |           66.0%            |           +0.370 (37.0%)            |
    >  
    > *Physical Ceiling Rationale:* 
    > As more cores are grouped together in a single homogeneous cluster, synchronization overhead (contending for the same shared local L2 cache and cluster-level bus) rises. The incremental value of each core decays smoothly from **91.9%** to **37.0%**. The 5.278x yield for an 8-core cluster represents the maximum physical ceiling of homogeneous scaling in the absence of external system bottlenecks. This aligns well with modern computer science literature on non-SMT parallel scaling (where 8 identical cores typically achieve a maximum scaling factor of ~4.1x to ~5.3x depending on power limits and virtual thread capabilities).
    
    * *Note on SMT (Simultaneous Multithreading):* Simultaneous Multithreading is a CPU design technique that allows a single physical processor core to execute two software threads at the same time. While extremely common in desktop computers (often marketed as "Hyper-Threading"), it is absent in mobile chips where each physical core can only execute a single thread.

2.  **Cluster Effective Throughput (CET):** `CET_i = CY_i * PACC_i`
    *   This combines the frequency-adjusted core yield (`CY_i`) with the parallel cluster overhead (`PACC_i`).

**Step 3: Raw CPU Throughput Score (RCTS)**
Sum all cluster contributions to find the total theoretical silicon demand:
`RCTS = SUM(CET_i)` for all clusters.

**Step 4: Global Perceptual Normalization**
Before evaluating systemic bottlenecks, we normalize the raw throughput to our 0-10 perceptual scale.
`RCTS_norm = 10 * (log(RCTS) - log(CPU_RCTS_Min)) / (log(CPU_RCTS_Max) - log(CPU_RCTS_Min))` (Clamped 0.0 - 10.0)

*   *Note:* The logarithmic scale ensures our scoring model accurately reflects human perception (Weber-Fechner Law), where performance gains at the low end (usability) are weighted heavily, while extreme flagship gains yield diminishing perceptual returns. We normalize the *entire* SoC collectively, rather than per-cluster, because the user perceives the fluidity of the system as a whole.

**Step 5: Non-Linear Deficit Penalties, Final Score & Abort Protocol**
Even if the core CPU complex is exceptionally powerful, it cannot deliver that performance if the rest of the smartphone's hardware acts as a bottleneck. We model these systemic constraints (Memory, Thermals and Cache) using a non-linear deficit penalty system. 
Subsystems are treated as *constraints*, not bonuses. A subsystem only impacts the final score if it fails to meet the demand generated by the CPU (`RCTS_norm`). 

1.  **Identify Deficits:**
    For each supporting subsystem `S` {MTI, TDSI, CFEI}, we calculate the deficit relative to the CPU's normalized demand (`RCTS_norm`):
    `Deficit_S = max(0, RCTS_norm - S)`

2.  **Apply Exponential Penalties:**
    When a bottleneck occurs, its severity compounds non-linearly. We apply specific weights and exponents (`β`) based on the architectural impact of each subsystem:
    `Penalty_S = Weight_S * (Deficit_S ^ β)`

    *   **Memory (MTI - 0.09 Weight, β=1.4):** Modern cooperative workloads are fundamentally memory-bound. If the CPU requests data faster than the RAM can supply it, the cores stall. Sourced from the **Predicted Score** of **Section 6.5 (Memory Technology & Bandwidth)** to isolate the raw hardware capabilities of the memory bus and RAM technology before downstream boosters are applied.
        `Penalty_MTI = 0.09 * (Deficit_MTI ^ 1.4)`

    *   **Thermals (TDSI - 0.015 Weight, β=1.4):** Sustained multi-core saturation generates immense heat. Insufficient cooling will forcibly throttle the CPU regardless of its theoretical peak speed. Sourced from the **Final Score** of **Section 6.10 (Thermal Dissipation Stability Index)** to capture the actual, real-world physical cooling assembly capabilities as proven by sustained hardware performance testing.
        `Penalty_TDSI = 0.015 * (Deficit_TDSI ^ 1.4)`
        
    *   **Cache & Fabric Efficiency (CFEI - 0.02 Weight, β=1.3):** Evaluates the shared on-chip memory (L3 + SLC). A smaller shared cache forces the CPU to rely more heavily on external RAM, increasing latency. Sourced from the **Cache Index Score** derived from the continuous Cache & Fabric Efficiency Index (CFEI) logarithmic scaling formula (§6.1.C) to represent the capacity that minimizes latency-heavy fetches from the external DRAM (Dynamic Random Access Memory).
        `Penalty_CFEI = 0.02 * (Deficit_CFEI ^ 1.3)`

3.  **Compute Final Score & Validate Safety Limits:**
    The final performance score is the normalized demand minus all active system penalties:
    `Predicted_Score_6.1 = RCTS_norm - SUM(Penalty_S)`

[!NOTE]
**Mathematical Design of the Penalty System:**
The non-linear exponents (`β = 1.3 to 1.4`) ensure that minor imbalances are forgiven, but severe starvation crushes the final score. 
 
**Physical Rationale of the Beta Exponents (β):**
The non-linear exponents control how rapidly the penalty scales as a deficit widens:
 
1.  **Memory and Thermals (β = 1.4):** Memory bandwidth starvation and thermal throttling impose hard, cascading physical boundaries. When RAM bandwidth is exhausted, execution pipelines stall completely while waiting for memory access, causing a sharp, non-linear collapse in execution efficiency. Similarly, when thermal thresholds are exceeded, the SoC's hardware-level thermal management triggers aggressive voltage-frequency scaling steps that degrade performance rapidly to protect the silicon. These cascading physical limits are modeled with a high exponent of 1.4.
2.  **Cache Capacity (β = 1.3):** A deficit in cache capacity represents a routing latency penalty rather than a hard physical stop. When a thread misses in the Level 3 (L3) or System Level Cache (SLC), the data must be retrieved from external DRAM. Although DRAM access takes longer, the CPU's out-of-order execution engine can overlap instructions to hide some of the latency. Thus, cache deficits degrade performance at a slightly less aggressive rate than memory bandwidth starvation or thermal throttling, modeled with a slightly lower exponent of 1.3. 

The maximum theoretical penalty (if a perfect 10.0 CPU was paired with 0.0 hardware across the board) is strictly bounded to **3.04** (`0.09*(10^1.4) + 0.015*(10^1.4) + 0.02*(10^1.3)`). 
While this design keeps the penalty system naturally self-limiting under high-performance scenarios, it does not guarantee absolute safety under all possible imbalanced or low-to-mid performance configurations. 

[!CAUTION]
⚠️ **CRITICAL PHYSICAL RANGE VIOLATION — PROCESS ABORT RULE!**
Under no circumstances should the system silently clamp or allow an out-of-bounds score in production. 
If the raw calculation `Predicted_Score_6.1 = RCTS_norm - SUM(Penalty_S)` yields a value outside the physical standard range of `[0, 10]` (e.g., less than 0 or greater than 10), **the entire scoring pipeline for the target device MUST BE ABORTED IMMEDIATELY.** 
The system must immediately raise the following standardized exception alert and halt execution:
 
`CRITICAL ANOMALY ALERT: Raw multi-core CPU score ({Predicted_Score}) is outside physical standard bounds [0, 10]. Halting scoring process.`
 
An out-of-bounds score indicates a structural model breakdown, mathematical overflow, or a highly anomalous physical SoC configuration. The compilation pipeline must throw a high-priority system exception, halt database generation for that device, and emit a detailed error log detailing all pre-clamped coefficients and subsystem deficits. This triggers immediate engineering examination for a potential model update.

 
##### 🔬 Empirical Calibration & Physical Rationale

To approximate alignment with real-world physical throughput, the penalty coefficients (weights) and non-linear exponents (beta values) are calibrated as engineering approximations based on available empirical data and microarchitectural constraints. Because isolating a single hardware variable (such as cache size or memory bandwidth) in commercial smartphones is exceptionally difficult due to confounding differences in silicon design, operating system (OS) governors, and board layouts, these calibrations are inherently imperfect in isolating pure variables and represent target scaling ranges rather than absolute physical constants.

| Bottleneck Type         | Input Metric | Weight | Exponent (β) | Target Workload           |
| :---------------------- | :----------- | :----: | :----------: | :------------------------ |
| **Memory Bandwidth**    | MTI          | 0.0900 |     1.4      | SPEC CPU2017 (Multi-core) |
| **Thermal Dissipation** | TDSI         | 0.0150 |     1.4      | Geekbench 6 Multi-Core    |
| **Cache Capacity**      | CFEI         | 0.0200 |     1.3      | General multi-core mix    |

> [!IMPORTANT]
> **Source of Truth for Subsystem Penalty Calibrations:**
> For the full physical, microarchitectural and empirical calibration rationales, refer directly to [performance_scoring_weights_rationale.md].

[!TIP]
🚀 **POTENTIAL FUTURE MODEL IMPROVEMENTS:**
To capture physical hardware dependencies even more precisely, subsequent model revisions may evaluate replacing the global `RCTS_norm` baseline with targeted physical demand functions and new component integrations. Furthermore, conducting more precise empirical studies and regression analyses across a wider variety of hardware configurations could help to mathematically fine-tune the calibrated weights and non-linear exponents (representing a generalization of the methodology detailed in *Section 6.1.C.B: Subsystem Deficit Calibration* but with the simultaneous optimization of the beta exponents alongside the weights):
 
###### A. Physical Subsystem Demand Functions (Proposed Options)
These proposed formulations isolate core-type sensitivities by replacing flat global demands with specialized physical demand curves:
*   **Thermal Demand Function:** Models thermal load by factoring in high-burst single-core power draw:
     `Thermal_Demand = 0.75 * RCTS_norm + 0.25 * BestClusterStrength`
     *(Rationale: Extremely clocked best performing cores generate concentrated, high-voltage heat flux, spiking cooling demand disproportionately compared to other clusters.)*
*   **Memory Demand Function:** Models memory bus contention by factoring in cooperative background efficiency workloads:
     `Memory_Demand = 0.65 * RCTS_norm + 0.35 * WorstClusterStrength`
     *(Rationale: High concurrency of background threads on the lowest-performing active cluster (the worst cluster) generates heavy random RAM fetches, saturating the system bus and starving fast high-performance clusters.)*
*   **Cache Demand Function:** Models cache demand as a function of workload complexity, core asymmetry, and concurrent task parallelism:
     `Cache_Demand = 0.65 * RCTS_norm + 0.20 * Core_Asymmetry_Index + 0.15 * Parallelism_Index`
     `Deficit_Cache = max(0, Cache_Demand - CFEI)`
     *(Rationale: Cache only becomes critical when active threads exceed private caches and memory synchronization pressure increases. A weaker midrange CPU has fewer cores running less demanding tasks, meaning its data fits easily in private caches and it has very little real-world need for a massive shared cache pool. In contrast, an 8-core flagship running highly parallel threads generates heavy shared-data pressure, making a large cache essential.)*
 
###### B. Dynamic Thread Scheduler Integration (Proposed Option)
A comprehensive structural refinement could introduce the OS (Operating System) thread scheduler not as an independent score, but as a dynamic **scheduler efficiency coefficient** applied to a **Core Asymmetry Index (CAI)**.
*   *Context and Physical Impact:* In highly asymmetric CPU layouts, the thread scheduler acts as the physical "traffic cop" of the processor. If the scheduler places a high-priority, time-critical thread on a tiny lower-performance core, or a trivial background thread on a power-hungry best performing core, the CPU stalls (causing UI micro-stutters) and wastes power (triggering thermal throttling). An inefficient scheduler directly prevents highly capable flagship core complexes from ever realizing their theoretical multi-core throughput.
*   *Core Asymmetry Index (CAI) Formulation:* `CAI = Cluster_Count_Factor * IPC_Disparity * Frequency_Disparity` (where IPC is Instructions Per Cycle). This index mathematically models the physical asymmetry and layout complexity of the CPU core clusters.
*   *Physical System Demand:* `Scheduler_Demand = RCTS_norm * CAI` (scaling the physical scheduling workload demand directly by silicon asymmetry).
*   *Software Scheduler Capability:* `Scheduler_Capability` represents the OS (Operating System) scheduling capability scored on a granular `[0, 10]` scale (evaluating Base OS Tiers, Hardware Telemetry Bonuses like Qualcomm Thread Director or ARM Hardware Feedback Interface (HFI), and Original Equipment Manufacturer (OEM) scheduling engines).
*   *Penalty and Final Score Integration:* Similar to other physical subsystems, the software scheduling capability is compared directly against the physical hardware demand to calculate a deficit: `Deficit_Scheduler = max(0, Scheduler_Demand - Scheduler_Capability)`. If a deficit exists (meaning the OS scheduler is too weak to efficiently orchestrate the physical cluster asymmetry), an exponential penalty is applied (`Penalty_Scheduler = Weight_Scheduler * (Deficit_Scheduler ^ 1.3)`) to directly discount the final multi-core CPU performance score.
 

##### 🧠 Cache & Fabric Efficiency Index (CFEI)
The Cache & Fabric Efficiency Index (CFEI) measures the capacity and physical layout efficiency of the System on Chip (SoC) shared on-chip memory.
 
**Understanding the Cache Hierarchy:**
*   **Level 1 (L1) Cache:** Small, ultra-fast memory private to individual processor cores. Its performance benefit is inherently captured by the CPU Architecture Score (CAS).
*   **Level 2 (L2) Cache:** Faster intermediate memory private to individual cores or shared within core clusters. Unlike L1, the capacity and latency of L2 caches are explicitly evaluated using the Private Cache Penalty (L2CS) in single-core CPU performance calculations (Section 6.2), on top of the CAS baseline.
*   **Level 3 (L3) Cache / System Level Cache (SLC):** Large, shared pools of memory accessible by all cores across the entire SoC. They prevent the CPU from having to fetch data from the much slower external Random Access Memory (RAM), avoiding massive speed penalties.
 
For most Systems on Chip (SoCs), the cache capacity is calculated by summing the Level 3 (L3) Cache and the System Level Cache (SLC):
 
`Effective_Shared_Cache = L3 Cache (MB) + SLC (MB)`
 
Cache capacity benefits follow a logarithmic curve due to diminishing performance returns (doubling the cache size yields progressively smaller reductions in cache miss rates). To perfectly align with the continuous, logarithmic nature of `RCTS_norm`, the cache efficiency score is calculated continuously:
 
`CFEI = 10 * (log(Effective_Shared_Cache) - log(CPU_CFEI_Min)) / (log(CPU_CFEI_Max) - log(CPU_CFEI_Min)) (Clamped 0-10)`
 
*   **Inputs:** `Effective_Shared_Cache = max(0.5000, L3 (MB) + SLC (MB))` (a safety clamp at `0.5000` MB is applied to prevent undefined mathematical operations for SoCs with no shared cache).
  
###### 🔹 CFEI Capacity Calculation & Edge-Case Rules
When calculating the cache efficiency score (`CFEI`), researchers must evaluate specific microarchitectural designs according to these rules:
 
1.  **Combined Manufacturer Reporting:**
     If "L3 + SLC" is reported as a combined figure by the manufacturer, use that figure directly as the `Effective_Shared_Cache` capacity.

2.  **Apple SLC-Only Architecture:**
     Apple SoCs bypass standard Level 3 (L3) caches entirely, utilizing massive cluster-private Level 2 (L2) caches (inherently captured in single-core CPU Architecture Score [CAS]) and a large system-wide System Level Cache (SLC). Since no Level 3 (L3) cache exists, their effective shared cache capacity is defined strictly as `SLC (MB)`.

3.  **Snapdragon 8 Elite Capacity & Coherency Rules:**
     The Snapdragon 8 Elite uses a unique architecture with large private Level 2 (L2) caches per core cluster (12 MB L2 per Oryon cluster, 24 MB total) and a shared 8 MB SLC, but no Level 3 (L3) cache.
     *   *Capacity Equivalence:* Capacity-wise, 24 MB of cluster-shared L2 + 8 MB SLC acts as a 32 MB on-chip Static Random-Access Memory (SRAM) pool. When a thread misses in its private cache, retrieving data from another cluster's L2 or the SLC still avoids a high-latency trip to external Dynamic Random-Access Memory (DRAM). Therefore, in terms of reducing memory bandwidth bottleneck and maximizing cache hit rate, it is structurally equivalent to a 32 MB L3+SLC pool. Hence, its baseline capacity is combined: `24 MB L2 + 8 MB SLC = 32 MB`, which resolves to a baseline score of `10`.
     *   *Coherency Penalty:* Because these L2 caches are physically split per cluster and lack a unified L3 cache, cross-cluster cache coherency incurs a significant latency penalty over the Network-on-Chip (NoC). To reflect this microarchitectural routing latency, a flat penalty of **`-0.5000`** is applied directly to the calculated score, yielding a final score of **`9.5000`**.
     *   *Justification for the -0.5000 Calibration (order of magnitude):* On our 0 to 10 scale, a -0.5 penalty shifts the final CFEI score down from 10 to 9.5. In our continuous logarithmic model, a CFEI score of 9.5 is mathematically equivalent to the efficiency of a unified ~26 MB cache pool. This effectively discounts the split 32 MB total capacity (24 MB L2 + 8 MB SLC) by ~6 MB, which represents a ~25% effective reduction of the 24 MB L2 cache pool (6 MB / 24 MB = 25%). This 25% discount is justified microarchitecturally: because each core cluster only has immediate, low-latency access to its local 12 MB L2 pool, while the remaining 12 MB L2 on the opposite cluster is non-local and requires high-latency NoC fabric traversal. Penalizing this non-local pool's capacity by half (6 MB) provides a good order-of-magnitude estimation of the real-world latency overhead of split caches.

4.  **Entry-Level and Legacy SoCs (No L3, No SLC):**
     Ultra-low-end or legacy chipsets (e.g., Helio G99, Snapdragon 680) have no Level 3 (L3) cache and no SLC. Their Level 2 (L2) caches are strictly private to individual cores or clusters and cannot act as a shared Last Level Cache (LLC) across the fabric. For these chipsets, the effective shared cache capacity is set to the DynamIQ Shared Unit (DSU) shared cache size (usually 512 KB / 0.5 MB or 1 MB). If no DSU shared cache exists, the capacity is set to `0.5` MB (the minimum baseline of our continuous logarithmic model), yielding a `CFEI` score of `0`.
 
[!NOTE]
**Note on Future Modifications:** Additional fabric topology edge cases could be added in the future to fine-tune the model for other architectures (e.g., standard DSU ring-bus variations), but they are not considered for now due to their low overall impact on the final system score.

###### 🔹 Master Cache Capacity Reference
To eliminate redundancy and ensure a single canonical source of truth, the complete, exhaustive database of all shared cache capacities and fabric routing details for mobile chipsets from 2016 to 2026 is maintained in the [System on Chip (SoC) Reference (references/soc_reference.md)]. 
 
Researchers and models **must** refer directly to that document to resolve the Level 3 (L3) cache, System Level Cache (SLC) capacity and effective shared cache for any given SoC model.
 

##### 📝 Worked Example: Snapdragon 8 Gen 3 (Balanced Flagship)
*   **Ref Freqs (§6.1.0):** X4 = 3.3000 GHz, A720 = 2.8000 GHz, A520 = 2.0000 GHz
*   **Actual Specs:** 1x X4 @ 3.3000 GHz, 5x A720 @ 3.2000 GHz, 2x A520 @ 2.3000 GHz
*   **Step 1 (Core Yields with Soft-Saturation):**
     *   Best (X4): `R = 3.3000 / 3.3000 = 1.0000`. `γ(1) = 0.9300`. `CY = 7.9500 * (1.0000^0.9300) = 7.9500`
     *   Second Best (A720): `R = 3.2000 / 2.8000 = 1.1429`. `γ(5) = 0.9800`. `CY = 5.0000 * (1.1429^0.9800) = 5.6993`
     *   Third Best (A520): `R = 2.3000 / 2.0000 = 1.1500`. `γ(2) = 0.9500`. `CY = 1.0000 * (1.1500^0.9500) = 1.1420`
*   **Step 2 (CET with PACC):**
     *   Best: `PACC = 1^1.0000 = 1.0000`. `CET = 7.9500 * 1.0000 = 7.9500`
     *   Second Best: `PACC = 5^0.8500 = 3.9275`. `CET = 5.6993 * 3.9275 = 22.3840`
     *   Third Best: `PACC = 2^0.9400 = 1.9185`. `CET = 1.1420 * 1.9185 = 2.1909`
*   **Step 3 (RCTS):** `7.9500 + 22.3840 + 2.1909 = 32.5249`
*   **Step 4 (Global Normalization):**
     *   `RCTS_norm = 10.0000 * (log(32.5249) - log(0.5487)) / (log(55.6302) - log(0.5487)) = 10.0000 * (1.5122 - (-0.2607)) / (1.7453 - (-0.2607)) = 8.8380`
*   **Step 5 (Penalties, Final Score & Safety Check):**
     *   Assume the device has: `MTI = 8.0000`, `TDSI = 7.0000`, `CFEI = 7.0000`.
     *   `Deficit_MTI = max(0.0000, 8.8380 - 8.0000) = 0.8380`. `Penalty_MTI = 0.0900 * (0.8380^1.4000) = 0.0703`
     *   `Deficit_TDSI = max(0.0000, 8.8380 - 7.0000) = 1.8380`. `Penalty_TDSI = 0.0150 * (1.8380^1.4000) = 0.0352`
     *   `Deficit_CFEI = max(0.0000, 8.8380 - 7.0000) = 1.8380`. `Penalty_CFEI = 0.0200 * (1.8380^1.3000) = 0.0441`
     *   `Total Penalty = 0.0703 + 0.0352 + 0.0441 = 0.1496`
     *   `Final Score = 8.8380 - 0.1496 = 8.6884` (Bounds Check: 8.6884 is within `[0.0000, 10.0000]` → Pass)


### 🔹 6.2 CPU Architecture & Single-Core Efficiency
*Description:* Measures the responsiveness of the CPU for immediate tasks like app launching, web browsing, and UI navigation. This isolates architectural efficiency and single-thread speed.
*   **Measurement:** Geekbench 6 Single-Core Score.
*   **Unit:** Points (0–10)
*   **Significance:** Determines the "snappiness" of the UI and speed of light tasks.

> [!TIP]
> **Why do we need this separate from Section 6.1?**
> *   **Section 6.1 (Multi-Core) measures CAPACITY (The Truck):** Determines if the phone *can* run heavy tasks (rendering, gaming) without bottling up.
> *   **Section 6.2 (Single-Core) measures RESPONSIVENESS (The Sports Car):** Determines how *fast* a single task (like opening an app or scrolling a webpage) happens. 
> A phone with many weak cores (high 6.1) can still feel "laggy" in UI interactions if individual cores are slow (low 6.2). Single-core speed is the primary driver of perceived fluidity in daily use.

#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct Geekbench 6 score is available. It provides the most accurate representation of real-world performance.
`Score = 10 * (log(Score) - log(CPU_GB6_Single_Score_Min)) / (log(CPU_GB6_Single_Score_Max) - log(CPU_GB6_Single_Score_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ CPU_GB6_Single_Score_Max
*   **Min Score (0.0):** ≤ CPU_GB6_Single_Score_Min
> [!NOTE]
> **Why Logarithmic?** Single-core speed has a direct but diminishing impact on UI fluidity. A 500-point jump between a baseline 400-point core and a 900-point mid-range core dramatically reduces UI stutters. In contrast, a 500-point jump between 3000 and 3500 points yields millisecond gains that are harder for the human eye to perceive.

#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.
1.  **Identify Neighbors:** Find **3 distinct Reference Phones** that have **BOTH** Geekbench scores and known specs. Select the ones with the smallest **Distance** to the target device, **excluding the target device** itself:
    *   `Distance = Sqrt( (STRS_norm_Diff)² + (Penalty_L2CS_Diff)² + (Penalty_MTI_Diff)² )`
    *   *Where "Diff" is the difference between Target and Neighbor values for each component:*
        *   `STRS_norm_Diff` (Normalized Core Yield, see Method C Step 2)
        *   `Penalty_L2CS_Diff` (Private Cache Penalty, see Method C Step 3)
        *   `Penalty_MTI_Diff` (Memory Penalty, see Method C Step 3)
    *   **Scientific & Mathematical Rationale:** Since the Single-Core Performance Pipeline from Method C defines the overall performance score as a direct linear subtraction of the penalties from the core compute capacity (`Predicted_Score = STRS_norm - Sum(Penalty_S)`), every single component enters the final performance metric with an absolute weight of exactly 1.0. While in the vast majority of cases the core compute difference squared (`(STRS_norm_Diff)²`) will be much greater than the penalty differences, keeping all components allows the model to catch and correctly group highly unbalanced outlier devices that suffer from exceptionally high dynamic penalties.
2.  **Calculate Correction Ratio:**
    *   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
        *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
    *   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
        *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.
3.  **Apply to Benchmark:**
    *   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
    *   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

> [!NOTE]
> **Why Euclidean Distance?**
> With the introduction of the 4-step pipeline, Single-Core performance is no longer 1-dimensional. It is influenced by the raw core capacity minus specific subsystem bottlenecks (L2 Cache, Memory). Therefore, a 3D Euclidean distance perfectly isolates architectural mismatches from bottleneck discrepancies.

#### Method C: Predicted Calculation (Tertiary)
Used as a standalone fallback or as the **Predictor** for Method B.

### Introduction to the Single-Core Prediction Model
While Section 6.1 (Multi-Core) measures the absolute maximum throughput of all processor cores firing simultaneously, this section (6.2) evaluates the processor's ability to execute a single, intensive task as fast as physically possible. 

Single-core performance is the primary driver of "snappiness" in everyday smartphone use—how quickly an app opens, how fluidly a complex webpage renders, and how instantly the camera shutter reacts. 

To accurately predict this real-world responsiveness without relying on subjective benchmarks, our model utilizes a rigorous 4-step physical pipeline. This pipeline maps the raw microarchitectural capability of the processor and mathematically penalizes it based on real-world hardware bottlenecks:

*   **Step 1: Core Yield (The Engine's Top Speed).** We first calculate the absolute maximum computational power of the single strongest core on the chip. This factors in the core's microarchitectural efficiency (CAS/IPC), its peak clock speed (Frequency), and the efficiency of its underlying instruction set language (ISA Multiplier).
*   **Step 2: Perceptual Normalization (Human Perception).** Because human users cannot easily perceive microscopic, millisecond speed improvements at the highest tiers of performance, we normalize this raw core yield to a 0-10 scale using a logarithmic curve. This aligns the raw math with actual human perception.
*   **Step 3: Subsystem Penalties (The Bottlenecks).** A blindingly fast core is useless if it is constantly waiting for data to process. We subtract points (apply penalties) if the core's private Level 2 (L2) cache is too small to feed it or if the system RAM is too slow.
*   **Step 4: Final Score Validation.** Finally, we subtract the penalties from the normalized yield and run a strict safety check to ensure the final score remains physically grounded within the 0.00 to 10.00 bounds.


> [!IMPORTANT]
> **Why Core Count is Omitted in Section 6.2**
> Unlike Multi-Core throughput (§6.1), the Single-Core prediction model **strictly ignores the core count** of the strongest cluster.
> *   **Single-Thread Physics (The Indivisible Task):** A single-threaded task is, by definition, a single sequential chain of instructions. It is mathematically impossible to split this indivisible chain across multiple cores. Therefore, even if a processor has two identical, equally strong "best" cores (like Apple's A-series or the Snapdragon 8 Elite), the OS scheduler must assign that specific thread to just **one** of them.
> *   **What happens to the second identical core?** The second strong core cannot help execute that single thread. Instead, it is left idle, or the OS uses it to handle completely separate background tasks (like fetching notifications). It contributes absolutely nothing to the "snappiness" of the main foreground task being measured.
> *   **Latency vs. Throughput:** Single-core performance measures *responsiveness* (how fast one single task finishes). Multiplying by the number of cores measures *throughput* (how many separate tasks finish at once), which is handled exclusively in Section 6.1.

**Step 1: Core Yield with Frequency Soft-Saturation & ISA Modifier**
1. **Identify the Best Core:** Select the core with the highest CAS.
2. **Frequency Ratio (R):** `Actual_Frequency / Reference_Frequency`
3. **ISA Multiplier:** Sourced from the ISA Gen column:
   * **ARMv8.0 (Cortex-A53/A72/A73, Apple A9, Exynos M1/M2/M3):** `0.96`
   * **ARMv8.1 (Apple A10):** `0.97` (adds LSE atomic operations, improving multi-core thread scaling)
   * **ARMv8.2 (Cortex-A55/A75/A76/A77/A78/X1, Apple A11, Exynos M4/M5):** `1.00` (adds native FP16 and dot-product, a massive boost for modern float/int math workloads)
   * **ARMv8.3 (Apple A12):** `1.01` (adds pointer authentication and complex number math instructions)
   * **ARMv8.4 (Apple A13/A14):** `1.02` (adds matrix multiplication helper instructions, SHA-512, and LDAPR memory consistency controls)
   * **ARMv8.6 (Apple A15/A16/A17 Pro, Oryon Gen 1):** `1.04` (adds BFloat16 floating-point formats and dedicated matrix math acceleration instructions)
   * **ARMv8.7 (Oryon Gen 2):** `1.05` (adds enhanced pointer authentication and refined WFI/WFE low-power wait efficiency)
   * **ARMv9.0 (Cortex-X2/X3/A710/A715/A510):** `1.06` (introduces SVE2 and hardware-assisted Memory Tagging Extension [MTE])
   * **ARMv9.2 (Cortex-X4/X925/A720/A725/A520/A525, Apple A18):** `1.08` (introduces SME and dynamic SVE2 enhancements)
   * **ARMv9.3 (ARM C1-series / Lumex):** `1.10` (introduces SME2, offering high-throughput 2D matrix compute)

   > [!NOTE]
   > **What is the ISA Multiplier? (Non-Technical Explanation)**
   > ISA stands for "Instruction Set Architecture." Think of it as the core "dictionary" or "language" of commands the processor understands. Newer dictionaries (like ARMv9) allow the CPU to perform complex tasks using fewer, more efficient commands. 
   > 
   > This multiplier objectively rewards newer hardware generations. A CPU running at 3.0 GHz on a modern ARMv9 architecture will inherently perform faster than an older ARMv8 CPU running at the exact same 3.0 GHz, simply because it speaks a more efficient hardware language. This is a pure physical hardware advantage.

4. **Core Yield (CY):** `CY = CAS * (R ^ γ) * ISA_Multiplier`
   * **γ (Soft-Saturation Exponent):** Fixed at `0.93`.

   > [!IMPORTANT]
   > **Why is γ fixed at 0.93 for Single-Core performance?**
   > In a multi-core workload (§6.1), the soft-saturation exponent `γ` varies depending on the cluster size as a proxy for the core's architectural class and clock speed envelope (with third best/fourth best clusters clocked conservatively having nearly linear scaling, i.e., `γ = 0.99`).
   > 
   > However, in a **single-core workload**, only **exactly one physical core** is running the execution thread. Thus, cluster-level contention is non-existent. Instead, the performance scaling is dictated entirely by two physical CPU limits:
   > 1. **The Memory Wall:** As a single high-performance core's clock speed is pushed past its sweet spot into extreme ranges, memory access latencies (which remain constant in absolute nanoseconds) require an exponentially increasing number of CPU clock cycles. The CPU spends more clock cycles stalled waiting for cache misses, causing frequency scaling to saturate sub-linearly.
   > 2. **The Voltage Wall:** Pushing single-core frequencies to their absolute limits requires exponential voltage increases, causing severe leakage and thermal constraints.
   > 
   > Since single-core scoring *always* evaluates the single highest-performing core on the SoC (the best core) pushed to its absolute burst frequency limits, it is fundamentally pinned to the extreme high-performance saturation profile. Therefore, `γ` is fixed at `0.93` (the saturation constant for a single best core pushed to its limit), completely decoupling single-thread performance from multi-threaded cluster scaling models.

**Step 2: Raw Single-Thread Score & Perceptual Normalization (STRS_norm)**
`STRS_norm = 10 * (log(CY) - log(CPU_STRS_Score_Min)) / (log(CPU_STRS_Score_Max) - log(CPU_STRS_Score_Min))` (Clamped 0.0–10.0)
*   **Max Score (10.0):** CY ≥ CPU_STRS_Score_Max
*   **Min Score (0.0):** CY ≤ CPU_STRS_Score_Min

> [!NOTE]
> **Scoring Rationale (Logarithmic vs. Linear)**
> Section 6.2 utilizes a logarithmic scoring model to align with human perception of speed:
> *   **Perceptual Consistency (Weber-Fechner Law):** User perception of latency is relative. A performance jump at the low end (e.g., eliminating UI stutter) is perceived as a massive improvement, whereas an identical raw jump at the high end is often imperceptible.
> *   **Diminishing Returns:** Logarithmic scaling correctly compresses the high-end "vanity" gains while properly rewarding the foundational improvements that move a device from "laggy" to "snappy."
> *   **Mathematical Stability:** A floor of ~ `0.5` is enforced for all architectures in the lookup table to ensure the `log` calculation remains stable and valid for all devices.

**Step 3: Subsystem Penalties (L2 Cache, Memory)**
Single-core tasks are highly sensitive to private cache latency, but demand far less system memory bandwidth and generate negligible heat compared to multi-core workloads. Specifically, the Thermal Subsystem Penalty (TDSI) is completely omitted (0.00 weight) from the Single-Core CPU scoring framework. Standard single-core benchmarks (such as Geekbench 6 Single-Core, which represents Method A) execute workloads in short, transient bursts (typically lasting 1 to 5 seconds per subtest) separated by idle intervals. Due to the smartphone's transient thermal mass (thermal inertia), the chassis absorbs these brief spikes before reaching saturation, preventing the processor from hitting thermal limits. Since burst single-core execution experiences 0.0% physical thermal throttling, omitting the thermal penalty ensures maximum predictive precision and alignment between Method C and the empirical benchmark scores of Method A.

The remaining two subsystem penalties are calibrated as follows:

*   **Private Cache Penalty (L2CS — Level 2 Cache Score) — Weight: 0.06:**
    `L2CS_Score = 10 * (log(Typical_L2_KB) - log(CPU_L2_KB_Min)) / (log(CPU_L2_KB_Max) - log(CPU_L2_KB_Min))`
    `Deficit_L2CS = max(0, STRS_norm - L2CS_Score)`
    `Penalty_L2CS = 0.06 * (Deficit_L2CS ^ 1.4)`
    
    > [!NOTE]
    > **Architectural Justification: Cache Topologies (Shared vs. Private)**
    > Non-technical readers may notice extreme variances in `typical_l2_kb` across different architectures, where some state-of-the-art cores (e.g., ARM Cortex-X925 with `3072 KB` or Cortex-X4 with `2048 KB`) appear to have significantly less L2 cache than Apple designs (e.g., Apple A18 Pro with `16384 KB`) or even some older efficiency cores (e.g., Apple A10 Zephyr sharing a `3072 KB` pool). This reflects two distinct physical design philosophies:
    > *   **Shared L2 Clusters:** Architectures like Apple's P-cores or Qualcomm's Oryon utilize a **cluster-shared** L2 cache where all performance cores share a single massive pool. In a single-core workload, the inactive cores leave the entire shared capacity (e.g., 16 MB) accessible to the single running core. This minimizes cache misses at the expense of higher physical latency (due to complex routing and arbitration logic).
    > *   **Private L2 Cores:** Standard ARM designs (like the Cortex-X or Cortex-A700 series) utilize dedicated **private** L2 caches per core. A single core can only access its own private block (e.g., 2 MB for Cortex-X4, 3 MB for Cortex-X925). While this reduces the absolute capacity available to a single active thread, it physically places the cache immediately adjacent to the core's execution engine, reducing latency to a blazing ~10-12 clock cycles and eliminating cluster contention.
    > *   **Scoring Alignment:** The latency and IPC benefits of the private L2 design are naturally captured in the core's baseline **Core Architecture Score (CAS)** (§6.1.0), while the **L2CS** penalty safely identifies pure capacity deficits relative to peak compute demands.

*   **Memory Subsystem Penalty (MTI) — Weight: 0.03:**
    `Deficit_MTI = max(0, STRS_norm - MTI_Score)` (MTI from §6.5 Predicted)
    `Penalty_MTI = 0.03 * (Deficit_MTI ^ 1.3)`

> [!NOTE]
> **Mathematical Design of the Single-Core Penalty System:**
> The non-linear exponents (`β = 1.3 to 1.4`) ensure that minor imbalances are forgiven, but severe starvation crushes the final score. 
> The maximum theoretical penalty (if a perfect 10.0 CPU was paired with 0.0 hardware across the board) is strictly bounded to **2.1** (`0.06*(10^1.4) + 0.03*(10^1.3)`). 
> While this design keeps the penalty system naturally self-limiting under high-performance scenarios, it does not guarantee absolute safety under all possible imbalanced or low-to-mid performance configurations.

> [!TIP]
> **Understanding the Shift in Subsystem Penalties vs Multi-Core (Section 6.1)**
> Why do the penalty weights here look so different from the Multi-Core model and how can they be justified? It boils down to the physical and mathematical calibration of single-threaded execution bottlenecks. Those are described below for the cache and memory components.
> 
> **1. Cache Penalty Redesign: Severe Sensitivity to Private L2 Cache Capacity (Weight: 0.06, Exponent: 1.4)**
> *   *In Multi-Core (6.1):* We look at the massive shared L3/SLC cache (CFEI), which acts as a traffic controller preventing multiple cores from fighting over RAM. The cache penalty weight is lower because bus bandwidth and thermal density dominate multi-threaded limits.
> *   *In Single-Core (6.2):* There is no fighting. A single thread relies entirely on having its data immediately accessible. L2 cache misses introduce devastating pipeline bubbles: the CPU must stall for **100 to 200+ cycles** waiting to fetch data from L3 or system RAM, reducing execution efficiency by **over 50%** in memory-bound threads. The heavier weight of `0.06` and exponent of `1.4` mathematically reflects this massive latency penalty. We isolate and evaluate the **Private L2 Cache** capacity rather than other memory hierarchy levels for key architectural reasons:
>     *   **Exclusion of Level 1 (L1) Cache:** Although Level 1 cache offers the lowest access latency, its extremely restricted capacity (typically 64KB to 128KB) is tightly integrated directly within the core's execution pipeline. Its latency impact is constant across platforms and is therefore inherently captured by the core's baseline Compute Architecture Score (CAS).
>     *   **Exclusion of Shared Level 3 (L3) / System Level Cache (SLC):** The shared L3/SLC pool resides outside the core boundary, requiring data requests to traverse the chip's interconnect fabric. This fabric traversal introduces variable cross-silicon latency penalty cycles that degrade the immediate, deterministic response speed required for snappy single-threaded user interface (UI) loops.
>     *   **Selection of Private Level 2 (L2) Cache:** Private L2 cache represents the largest memory buffer tightly coupled to a specific CPU core or cluster. Massive L2 allocations (e.g., 16MB on Apple A16 or 12MB on Qualcomm Oryon) allow the best core to retain working sets locally, bypassing fabric transaction delays entirely. L2 capacity therefore serves as the primary hardware-configurable bottleneck dictating single-core IPC scaling and UI fluid responsiveness.

**2. Memory Penalty Optimization: Decreased Single-Thread Bandwidth Sensitivity (Weight: 0.03, Exponent: 1.3)**
*   *In Multi-Core (6.1):* Several cores firing at once will easily saturate and choke standard RAM bandwidth, making memory speed highly critical.
*   *In Single-Core (6.2):* A single active Central Processing Unit (CPU) core rarely saturates modern system memory bandwidth. While clean, same System-on-Chip (SoC) mobile memory speed isolation tests are not available (representing an evidence gap), microarchitectural analysis shows that memory bandwidth changes have a negligible impact on single-threaded performance. Slower legacy Random Access Memory (RAM) still imposes a persistent latency tax, which is why the penalty weight is reduced to a light `0.03`.

> [!IMPORTANT]
> **Calibration Basis for Single-Core Penalty Parameters:**
> Note that [performance_scoring_weights_rationale.md] does not contain formal empirical calibration studies or quantitative System-on-Chip (SoC) isolation tests for single-core Central Processing Unit (CPU) performance. Instead, the single-core penalty parameters are qualitatively estimated by comparing single-threaded microarchitectural constraints—specifically, heightened sensitivity to cache latency versus reduced sensitivity to memory bus bandwidth—against the multi-core baseline.

**Step 4: Final Score & Safety Validation**

The final Single-Core CPU performance score is computed by subtracting the sum of the private cache (L2CS) and memory (MTI) subsystem penalties from the normalized single-thread compute yield:

`Predicted_Score_6.2 = STRS_norm - (Penalty_L2CS + Penalty_MTI)`

> [!CAUTION]
> ⚠️ **CRITICAL PHYSICAL RANGE VIOLATION — PROCESS ABORT RULE!**
> Under no circumstances should the system silently clamp or allow an out-of-bounds score in production. 
> If the raw calculation `Predicted_Score_6.2 = STRS_norm - (Penalty_L2CS + Penalty_MTI)` yields a value outside the physical standard range of `[0.00, 10.00]` (e.g., less than 0.00 or greater than 10.00), **the entire scoring pipeline for the target device MUST BE ABORTED IMMEDIATELY.** 
> The system must immediately raise the following standardized exception alert and halt execution:
> 
> `CRITICAL ANOMALY ALERT: Raw single-core CPU score ({Predicted_Score}) is outside physical standard bounds [0, 10]. Halting scoring process.`
> 
> An out-of-bounds score indicates a structural model breakdown, mathematical overflow, or a highly anomalous physical SoC configuration. The compilation pipeline must throw a high-priority system exception, halt database generation for that device, and emit a detailed error log detailing all pre-clamped coefficients and subsystem deficits. This triggers immediate engineering examination for a potential model update.


#### 6.3.0 GPU Architecture Reference

**Master Scoring Table** (used across all GPU-related calculations)

This table provides the authoritative GPU architecture scores used throughout the scoring system, including:
- Section 6.3 GPU Performance (Base Architecture Score)
- Section 8.1 for Battery Endurance Scoring (Battery efficiency - SoC component)

**Scoring Basis:** Based on GPU generation, compute units, and real-world graphics performance established from cross-platform benchmark analysis (3DMark, GFXBench) across all smartphone GPU generations from 2016 to 2026.

| GPU Model                  |   Standard Graphics   | Ray Tracing | Ref Freq (MHz) | Efficiency |
| :------------------------- | :-------------------: | :---------: | :------------: | :--------: |
| **Immortalis-G925 MC12**   |       **9.50**        |  **10.00**  |    **1612**    |  **10.0**  |
| **Adreno 830**             |       **9.50**        |  **9.80**   |    **1100**    |  **10.0**  |
| **Apple GPU (A18 Pro)**    |       **9.00**        |  **8.80**   |    **1490**    |  **10.0**  |
|           [...]            |         [...]         |    [...]    |      [...]     |    [...]   |

> [!IMPORTANT]
> **Source of Truth:** For the full list of all supported GPU architectures and their authoritative scores, refer to the **GPU_ARCHITECTURE_LOOKUP_TABLE** in [proposed_data_structure.md].

> [!NOTE]
> **The "Higher Number" Fallacy (Flagship vs. Mid-Range):** You may notice that an older **Adreno 660** ranks higher than a newer **Adreno 720**. This is not an error. The Adreno 660 is the flagship GPU from the Snapdragon 888, possessing massive arrays of physical shader cores. The Adreno 720 is the budget/mid-range GPU from the newer Snapdragon 7s Gen 2, which is more efficient but possesses far fewer cores. In raw rasterization throughput, massive older flagships generally outmuscle newer mid-range chips, despite the nomenclature.

> [!NOTE]
> **Why Theoretical Specs (GFLOPS) Are Not Used For Baseline Scoring:** We use empirical benchmarks to establish this table rather than theoretical limits like GFLOPS (Giga Floating-Point Operations Per Second — a measure of how many billions of mathematical operations a chip can theoretically perform each second).
> **Understanding Architectural Diversity (Why Frequencies Differ):** You may notice that GPUs with similar performance scores (e.g., Immortalis-G925 and Adreno 830) have vastly different **Reference Frequencies** (1612 MHz vs. 1100 MHz). This is coherent and reflects different architectural philosophies:
> 1. **High-IPC Designs (e.g., Adreno):** Use fewer but "wider" cores that do more work per cycle (IPC — Instructions Per Cycle), allowing them to achieve elite performance at lower clock speeds.
> 2. **High-Frequency Designs (e.g., Mali/Apple):** Use "narrower" cores that are optimized to run at extremely high clock speeds to achieve the same throughput.
> 
> The **Standard Graphics Score** represents the *resultant* performance of the architecture. The **Reference Frequency** is strictly a normalization anchor used to calculate the **Frequency Scaling Factor (FSF)** for specific device variations; it is not a direct measure of performance.
> 1. **Cross-Architecture Incomparability:** 1,000 GFLOPS on a Qualcomm Adreno chip does *not* equal 1,000 GFLOPS on an ARM Mali chip because their internal pipelines, cache hierarchies, and ALU (Arithmetic Logic Unit) designs process data differently. 
> 2. **Opaque Specifications:** Manufacturers like Apple strictly conceal their GPU clock speeds, core configs, and theoretical GFLOPS. Therefore, only standardized physical testing ensures a level playing field.

> [!NOTE]
> **Understanding Mali/Immortalis "MC" Notation:** ARM Mali and Immortalis GPUs use Multi-Core (MC) configurations. The number after "MC" indicates the shader core count. For example:
> - **Immortalis-G715 MC11** = 11 shader cores (flagship config)
> - **Mali-G715 MC9** = 9 shader cores (high-end config)
> - **Mali-G715 MC7** = 7 shader cores (mid-range config)
> More cores = higher performance. Always match the exact MC count from device specifications (found on GSMArena under "Chipset" details).

### 🔹 6.3 Graphics & Ray Tracing Performance
*Description:* Measures the graphical processing power for gaming, professional rendering, and complex compute tasks. This section evaluates the **Instantaneous Burst Capability**—the maximum power the GPU (Graphics Processing Unit) can output for a short period.
*   **Measurement:** Composite of Standard Graphics (90%) and Ray Tracing (10%).
*   **Unit:** Points (0-10)
*   **Significance:** Critical for high-end gaming, smooth UI animations on 120Hz displays, and future-proofing for next-gen apps.

> [!WARNING]
> **Separation of Concerns: Efficiency & Thermals**
> To avoid double-counting, this section **strictly excludes** measurements of battery efficiency and thermal throttling.
> *   **Sustained Performance (Thermal Throttling):** Evaluated strictly in **Section 6.10 (TDSI — Thermal Dissipation Stability Index)**.
> *   **GPU Energy Efficiency:** Evaluated strictly in **Section 8.1 (Battery)**.

#### 6.3.A Standard Graphics Performance (SGS)
*Focus:* Traditional "Raster" rendering (Geometry, Textures, and Shaders) and API (Application Programming Interface) efficiency. This represents 95% of current mobile gaming workloads.

#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when real-world benchmark data is available.

**Benchmark Source: 3DMark Steel Nomad Light**
*   **Source:** UL Benchmarks Leaderboard
*   **Metric:** Steel Nomad Light Score (Points)
*   **Perimeter Justification:**
    *   **INCLUDES:** Rasterization (Geometry, Textures, Shaders), API Efficiency (Vulkan/Metal driver overhead).
    *   **EXCLUDES:** Ray Tracing (Hardware RT cores are unused). *Why? Steel Nomad Light is designed to run on a wide range of devices including those without RT support. RT performance is measured separately.*
*   **Normalization:**
    *   **Formula:** `SGS_Bench = 10 * (log(Score) - log(GPU_SteelNomad_Score_Min)) / (log(GPU_SteelNomad_Score_Max) - log(GPU_SteelNomad_Score_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ GPU_SteelNomad_Score_Max
    *   **Min Score (0.0):** ≤ GPU_SteelNomad_Score_Min

> [!NOTE]
> **Why Logarithmic?** Graphics performance scales exponentially in user experience. The difference of 400 points in the lower range, from 500 points (entry-level, struggles with basic games) to 900 points (smooth gameplay in most titles), is transformative. However, as we move into the higher range, the returns diminish significantly: the same 400-point difference between 1400 points and 1800 points is barely noticeable in real-world use. In the ultra-high tier, the same 400-point delta (such as 2500 points vs. 2900 points) is virtually imperceptible, as both deliver an elite, maxed-out frame rate experience.

##### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.

**1. Identify Neighbors via Feature Distance (Minimum Variance)**
Instead of just matching the overall predicted score, we find the 3 devices that are statistically closest across the hardware sub-features that dictate graphical throughput. The distance metric mirrors the structure of the Method C prediction pipeline to ensure that Method B bridges Methods A and C coherently.
*   **Search Space:** All phones with known 3DMark Steel Nomad Light scores (Method A), **excluding the target device** itself.
*   **Distance Metric:** Euclidean Distance in the space formed by the directly comparable components of the Method C pipeline (the normalized GPU yield and the three penalty values).
    *   `Distance = Sqrt( (GPU_Yield_norm_Diff)² + (Penalty_MTI_Diff)² + (Penalty_TDSI_Diff)² )`
    *   *Where "Diff" is the absolute difference between the target and the candidate neighbor for each component (Calculated in §6.3.C):*
        *   `GPU_Yield_norm_Diff`: Normalized GPU Yield score.
        *   `Penalty_MTI_Diff`: Memory subsystem penalty value.
        *   `Penalty_TDSI_Diff`: Thermal subsystem penalty value.
*   **Scientific Rationale:** The Method C pipeline decomposes GPU performance into a normalized yield and bottleneck penalties. Because the normalized yield (`GPU_Yield_norm`) and penalties (`Penalty_MTI`, `Penalty_TDSI`) are expressed on the same perceptual 0–10 scale, they are directly comparable. By measuring neighbor distance strictly using these normalized components, Method B selects devices that share the target's specific performance and bottleneck profile — not just its overall score. Two devices with the same final score but very different bottleneck profiles (e.g., one limited by memory, the other by thermals) would be far apart in this space, preventing misleading interpolation.
    *   **Bottleneck Sensitivity & Outlier Detection:** In practice, because architectural differences between generations are the primary driver of performance, `(GPU_Yield_norm_Diff)²` will most often be much larger than all other components, meaning that using only `GPU_Yield_norm_Diff` would be sufficient for typical devices. However, in extreme cases (such as highly unbalanced devices with severe thermal throttling or severe memory bottlenecks), the other penalty components can weigh in significantly. Retaining all components in the distance metric ensures the model successfully detects and groups together these extreme outlier devices with matching subsystem limitations.
*   **Selection:** Pick the 3 distinct neighbors with the smallest `Distance`.

**2. Calculate Correction Ratio:**
*   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
    *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
*   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
    *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.

**3. Apply to Benchmark:**
*   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
*   `Interpolated_Score (SGS) = Correction_Ratio * Avg_Benchmark_Neighbors`

##### Method C: Predicted Standard Graphics Performance (Tertiary)
Used as a standalone fallback or as the **Predictor** for Method B.

The prediction pipeline estimates a device's Standard Graphics Score from its hardware specifications alone, without requiring any benchmark measurement. The pipeline follows a five-step structure that mirrors the CPU performance pipelines in Sections 6.1 and 6.2:

1.  **Step 1 — Core GPU Yield:** Calculate the raw throughput potential of the GPU silicon (architecture score adjusted for frequency).
2.  **Step 2 — API Efficiency Modifier:** Apply a multiplicative adjustment for the software API (Application Programming Interface) capability that modifies the GPU's effective throughput.
3.  **Step 3 — Logarithmic Normalization:** Convert the raw yield to a human-perceptual 0–10 scale using logarithmic compression.
4.  **Step 4 — Deficit Penalties:** Subtract penalty terms for any supporting subsystem (memory, thermal) that fails to keep up with the GPU's demands.
5.  **Step 5 — Final Score & Safety Validation:** Combine the results and validate the output is within physical bounds.

---

**Step 1: Core GPU Yield with Frequency Soft-Saturation**

The Core GPU Yield represents the raw throughput potential of the GPU silicon, calculated from the architecture's baseline performance score adjusted for the specific device's clock frequency.

*   **Formula:** `GPU_Yield = Standard_Graphics_Score × (R ^ γ)`
    *   `Standard_Graphics_Score` **(Standard Graphics Score [0-10]):** Raw architectural graphics throughput. Sourced from the **Section 6.3.0 Reference Table** (Standard Graphics column).
        *   **Proportional to Raw Performance:** Unlike the final user-facing 0–10 score (which uses logarithmic compression to model human perception), the baseline Standard Graphics Score values in the reference table are linear with respect to performance: a GPU scoring 8.0 delivers approximately twice the raw throughput of a GPU scoring 4.0 when both run at their reference frequencies. The logarithmic compression is applied later in Step 3, ensuring a clean separation between the physics layer (the table + frequency scaling) and the human perception layer (normalization).
    *   `R` **(Frequency Ratio):** The ratio between the device's actual GPU clock speed and the architecture's reference frequency: `R = Actual_GPU_Frequency_MHz / Reference_GPU_Frequency_MHz`. Both values are expressed in Megahertz (MHz — millions of cycles per second).
        *   **Reference Frequency (MHz):** Sourced from the **Section 6.3.0 Reference Table** (Ref Freq column). This is the maximum advertised clock frequency of the GPU in its reference implementation. It serves strictly as a normalization anchor: when a specific device runs this GPU at a different frequency (higher or lower), the ratio between the actual frequency and this reference frequency determines the Frequency Scaling Factor.
        *   **Not a Direct Measure of Performance:** Different GPU architectures achieve vastly different amounts of work per clock cycle. The Standard Graphics Score represents the *resultant* performance of the architecture. The reference frequency is strictly a normalization anchor used to calculate the frequency scaling factor; it is not a direct measure of performance.
    *   `γ` **(Gamma — Frequency Soft-Saturation Exponent):** A fixed exponent of **0.93** that models the diminishing returns of increasing clock speed.

> [!NOTE]
> **Why γ = 0.93 (Frequency Soft-Saturation)?**
> In an ideal world, increasing a GPU's clock speed by 10% would yield exactly 10% more performance. In reality, the gains are always less than proportional due to two fundamental physical barriers:
> 1. **The Voltage Wall:** To run a chip at higher frequencies, the supply voltage must increase. Higher voltage causes power consumption — and therefore heat generation — to rise much faster than the frequency increase (approximately following the cube of the voltage). This triggers thermal throttling, which claws back some of the theoretical speed gain.
> 2. **The Bandwidth Wall:** A faster GPU demands data from system memory at a higher rate. When the memory bus cannot deliver data fast enough, the GPU's shader cores stall (sit idle waiting for data), wasting the extra clock cycles.
>
> The exponent γ = 0.93 captures this sub-linear relationship: a 10% frequency increase yields approximately 9.3% effective throughput gain, not 10%. This value is identical to the single-core CPU exponent used in Section 6.2, reflecting the same underlying voltage-wall physics that governs any silicon chip pushed to its burst frequency limits.
>
> *Note:* The bandwidth wall effect is separately captured by the Memory Throughput Index (MTI) penalty in Step 4. The γ exponent models only the inherent voltage-wall saturation of the GPU die itself, preventing double-counting.

---

**Step 2: API Efficiency Modifier (AFM)**

The API (Application Programming Interface) is the software layer through which games and applications communicate with the GPU hardware. More modern APIs allow developers to use more efficient rendering paths, reducing software overhead and directly increasing the GPU's effective throughput.

Unlike the memory and thermal subsystems (which act as ceilings — see Step 4), the API genuinely modifies the GPU's intrinsic throughput capability. A GPU running Vulkan 1.3 genuinely renders more frames per second than the same GPU running OpenGL ES 3.2, even if all other hardware is identical and unconstrained. This makes the API a **property of the GPU execution engine itself**, not an external bottleneck.

*   **Formula:** `GPU_Yield_Adjusted = GPU_Yield × AFM_Factor`
    *   `AFM_Factor` **(API Feature Modifier Factor):** 
        `AFM_Factor = (1 − Sensitivity_AFM) + Sensitivity_AFM × (AFM_Score / 10.0)`
        With the sensitivity coefficient `Sensitivity_AFM = 0.20` substituted, the numerical formula is:
        `AFM_Factor = 0.80 + 0.20 × (AFM_Score / 10.0) = 0.80 + 0.02 × AFM_Score`
        *   `Sensitivity_AFM = 0.20`: The sensitivity coefficient (maximum penalty weight) for graphics API driver overhead. This bounds the modifier range, establishing a safe physical lower limit of 0.80 (20% maximum penalty) for legacy APIs. This sensitivity coefficient is an estimation and intermediate value based on several studies which led to a range of [0.1-0.4]. But those studies (such as the one presented in [AFM_Sensitivity_Calibration_Proposal.md]) do not use sufficiently real world benchmarks and reliable data, hence more work is needed to establish a more accurate estimate of this coefficient.
        *   `AFM_Score`: The API score of the target device, sourced from the **API Support Score Table** below.

**API Support Score Table**
*   **Measurement:** Highest supported Vulkan / Metal / OpenGL ES / DirectX Version.
*   **Unit:** Score (0-10)
*   **Significance:** Modern APIs allow developers to squeeze significantly more performance through advanced features like dynamic rendering and compute shaders.

| Vulkan (Android) | Metal (iOS) | OpenGL ES (Leg) | DirectX (Win Mob) | Score    |
| :--------------- | :---------- | :-------------- | :---------------- | :------: |
| Vulkan 1.4       | Metal 4.0   | —               | —                 | **10.0** |
| —                | Metal 3.3   | —               | —                 | **9.8**  |
| [...]            | [...]       | [...]           | [...]             | [...]    |

> [!IMPORTANT]
> **Source of Truth:** For the full list of all supported Graphics APIs and their authoritative scores, as well as OS (Operating System)/Architecture fallback matrices, refer to the **GPU_API_SUPPORT_LOOKUP_TABLE** and **Ambiguous API Resolution** section in [proposed_data_structure.md]. Note that the operating system version listings in the fallback resolution tables must be fully aligned and synchronized with the canonical reference file [os_version_reference.md].

> [!IMPORTANT]
> **Multi-API Support & Scoring Logic:**
>
> Mobile devices support **BOTH Vulkan and OpenGL ES simultaneously**. Android supports all versions of both APIs, with approximately 85% of active devices supporting Vulkan.
>
> **ANGLE Translation Layer:** Some modern devices (e.g., certain Exynos chipsets) run OpenGL ES on top of Vulkan using the ANGLE translation layer. This **does not** make OpenGL ES better - ANGLE adds translation overhead, making it slower than native Vulkan. It simply means the device doesn't need separate OpenGL ES drivers.
>
> **Scoring Rule:** When a device supports multiple graphics APIs, **use the highest-scoring API** for the predicted score. Developers will always use the most advanced API available to maximize graphics quality and efficiency. A device with Vulkan 1.3 will run games using Vulkan, not OpenGL ES, regardless of whether OpenGL ES is available.
>
**Step 3: Logarithmic Normalization**

The raw GPU Yield (from Steps 1–2) is a physical throughput quantity expressed in arbitrary units. To convert it into a human-perceptual score on the standardized 0–10 scale, it must be normalized using logarithmic compression.

This normalization applies the Weber-Fechner Law — a fundamental principle of human perception stating that the perceived difference between two stimuli is proportional to the logarithm of their ratio, not their absolute difference.

*   **Formula:** `GPU_Yield_norm = 10.0 × (log(GPU_Yield_Adjusted) − log(GPU_Yield_Adjusted_Min)) / (log(GPU_Yield_Adjusted_Max) − log(GPU_Yield_Adjusted_Min))`
    *   Clamped to [0.0, 10.0].
    *   `GPU_Yield_Adjusted_Min`: The minimum GPU Yield value across the entire 2016–2026 device range, corresponding to the lowest-performing underclocked GPU with the lowest API modifier. 
    *   `GPU_Yield_Adjusted_Max`: The maximum GPU Yield value across the 2016–2026 device range, corresponding to the highest-performing GPU at its maximum overclocked frequency with the highest API modifier.

---

**Step 4: Deficit Penalties (Memory, Thermal, CPU Orchestration)**

A GPU cannot operate in isolation. It relies on three supporting subsystems that can each impose a performance ceiling:
1. **System Memory (RAM)** — to supply texture data, vertex buffers, and shader storage.
2. **Thermal Dissipation (Cooling)** — to prevent the chip from overheating and throttling.
3. **CPU Command Submission** — to feed the GPU with draw calls and command buffers.

These subsystems act as **bottlenecks**, not contributors: if any subsystem fails to meet the GPU's demand, performance is reduced. However, having a subsystem that exceeds the GPU's demand provides **no additional benefit** — the GPU cannot render faster than its own silicon allows, regardless of how fast the memory or cooling system is. This ceiling behavior is modeled using a **deficit-penalty** framework:

*   **Step 4.1 — Calculate the Deficit:** For each subsystem, the deficit measures how far below the GPU's demand that subsystem falls. If the subsystem meets or exceeds the demand, the deficit is zero (no bottleneck).
    *   `Deficit_S = max(0.0000, GPU_Yield_norm − S)`
    *   Where `S` is the subsystem's own normalized score, and `GPU_Yield_norm` is the normalized GPU yield from Step 3 (representing the GPU's demand on the system).

*   **Step 4.2 — Calculate the Penalty:** The deficit is converted to a score penalty using a non-linear power function. This models the physical reality that small deficits have modest impact (the GPU can partially compensate via caching and buffering), but large deficits cause severe performance collapse (stalls, throttling).
    *   `Penalty_S = Weight_S × (Deficit_S ^ β_S)`

###### A. GPU Subsystem Deficit Calibration

The subsystem penalty weights in the Standard Graphics Pipeline are calibrated as engineering approximations representing bottleneck severity rather than directly measured physical constants. The active bottlenecks model the impact of memory bandwidth starvation and thermal throttling on graphics throughput, while the Central Processing Unit (CPU) orchestration component is neglected.

*   **Memory Throughput Index (MTI):** Retained in the model (weight **0.1000**, exponent **1.4**). Mobile Graphics Processing Units (GPUs) are highly dependent on memory bandwidth for texture mapping and frame buffer operations. Bandwidth starvation (such as pairing a fast GPU with slow Random Access Memory (RAM)) causes shader cores to stall, directly dropping frame rates.
*   **Thermal Dissipation Stability Index (TDSI):** Retained in the model (weight **0.0180**, exponent **1.4**). While long-term thermal throttling is severe, the primary benchmark (3DMark Steel Nomad Light) is a short-burst test lasting approximately 60 seconds where the chassis thermal mass buffers heat. The small weight compresses the long-term TDSI deficit to its actual short-burst benchmark impact.
*   **CPU Orchestration Index:** Neglected/removed from the active model. The primary graphics benchmark is deliberately GPU-bound to isolate graphics performance, meaning CPU draw call and command submission overhead is negligible in practice.

**Subsystem Penalty Parameters:**

| Subsystem                                              | Source Score (`S`)                  | Weight    | Exponent (β)  |
| :----------------------------------------------------- | :---------------------------------- | :-------: | :-----------: |
| **Memory Throughput Index (MTI)**                      | §6.5 RAM Technology Predicted Score | **0.1000**|    **1.4**    |
| **Thermal Dissipation Stability Index (TDSI)**         | §6.10 TDSI Final Score              | **0.0180**|    **1.4**    |

> [!NOTE]
> **Mathematical Design of the GPU Penalty System:**
> The non-linear exponents (`β = 1.4`) ensure that minor imbalances are forgiven, but severe starvation crushes the final score.
> 
> **Physical Rationale of the Beta Exponents (β):**
> The non-linear exponents control how rapidly the penalty scales as a deficit widens: Memory bandwidth starvation and thermal throttling impose hard, cascading physical boundaries. When Random Access Memory (RAM) bandwidth is exhausted, execution pipelines stall completely while waiting for memory access, causing a sharp, non-linear collapse in execution efficiency. Similarly, when thermal thresholds are exceeded, the System on Chip (SoC) hardware-level thermal management triggers aggressive voltage-frequency scaling steps that degrade performance rapidly to protect the silicon.

> [!IMPORTANT]
> **Source of Truth for Subsystem Penalty Calibrations:**
> For the full physical, microarchitectural and empirical calibration rationales, refer directly to [performance_scoring_weights_rationale.md].
---

**Step 5: Final Predicted Standard Graphics Score (SGS) & Safety Validation**

The final predicted score is computed by subtracting all active deficit penalties from the normalized GPU yield:

`Predicted_Score_SGS = GPU_Yield_norm − (Penalty_MTI + Penalty_TDSI)`

> [!CAUTION]
> ⚠️ **CRITICAL PHYSICAL RANGE VIOLATION — PROCESS ABORT RULE!**
> Under no circumstances should the system silently clamp or allow an out-of-bounds score in production. 
> If the raw calculation `Predicted_Score_SGS = GPU_Yield_norm − (Penalty_MTI + Penalty_TDSI)` yields a value outside the physical standard range of `[0.00, 10.00]` (e.g., less than 0.00 or greater than 10.00), **the entire scoring pipeline for the target device MUST BE ABORTED IMMEDIATELY.** 
> The system must immediately raise the following standardized exception alert and halt execution:
> 
> `CRITICAL ANOMALY ALERT: Standard Graphics Score ({Predicted_Score_SGS}) is outside physical standard bounds [0, 10]. Halting scoring process.`
> 
> An out-of-bounds score indicates a structural model breakdown, mathematical overflow, or a highly anomalous physical hardware configuration. The compilation pipeline must throw a high-priority system exception, halt database generation for that device, and emit a detailed error log detailing all pre-clamped coefficients and subsystem deficits. This triggers immediate engineering examination for a potential model update.

---

#### 6.3.B Ray Tracing Performance (RTS)
*Focus:* Advanced light simulation (Reflections, realistic shadows, and lighting). Requires dedicated **RT (Ray Tracing) Cores** (specialized hardware units inside the GPU designed specifically for calculating how light rays interact with 3D surfaces).

> [!NOTE]
> **Methodology Decision:** Although benchmarks like **3DMark Solar Bay** exist to measure Ray Tracing performance, they have been discarded as primary scoring drivers. Since Ray Tracing currently accounts for only **10%** of the overall Graphics score, the added complexity of a multi-method (A/B/C) model is not justified. Instead, a streamlined Predictive Model is used to assess a device's RT potential based on its RT score and memory bandwidth.

> [!WARNING]
> **Future Alignment Note:** The Ray Tracing model below uses a simplified bottleneck formula (`min(RT_Score, 0.70 * RT_Score + 0.30 * MTI)`) rather than the deficit-penalty framework used by the Standard Graphics pipeline (§6.3.A Method C). This is an acknowledged approximation, accepted because RT currently represents only 10% of the total §6.3 score. When/if RT's weight increases in future model revisions (as mobile ray tracing hardware matures and game adoption grows), this subsection could be refactored to adopt the same deficit-penalty structure as §6.3.A.

##### Ray Tracing Performance (Predictive Model)
The Ray Tracing Score (RTS) is calculated using a two-factor predictive model that accounts for hardware acceleration capability and memory bandwidth bottlenecks.

**Step 1: Determine RT (Ray Tracing) Score**
*   *What is it?* The baseline performance potential of the dedicated silicon blocks responsible for ray-triangle intersection tests (the core mathematical operation in ray tracing — determining whether a simulated light ray hits a 3D surface).
*   **Classification:** Sourced from **Section 6.3.0 Table** (Ray Tracing column).
    *   *Significance:* This is the "Engine" for lighting. Without dedicated RT cores, the score is automatically 0, as software emulation is insufficient for real-time applications.
    
**Step 2: Inherit Memory Throughput Index (MTI)**
*   *What is it?* The already-normalized memory performance score from Section 6.5.
*   **Score:** `MTI = MTEI_Score` (Sourced from **Section 6.5**, use predicted score).
    *   *Significance:* High-speed Ray Tracing requires constant, massive data fetches from RAM (Random Access Memory). MTI ensures the RT score reflects the hardware's true ability to feed the RT cores.
    *   *Rationale:* **BVH (Bounding Volume Hierarchy)** traversal is essentially a large-scale memory search. Think of BVH as a "tree" of boxes: instead of checking every single triangle in a scene, the GPU first checks if a light ray hits a large box containing many objects. If it hits, it checks smaller boxes inside, and so on, until it finds the exact triangle. This "tree-searching" process requires massive, constant data fetches from system RAM. If the memory bandwidth is low, the RT cores spend most of their time waiting for data (stalls), rendering a high RT score useless.

**Step 3: Calculate Ray Tracing Score (RTS)**
*   *Formula:* `RTS = min(RT_Score, (RT_Score * 0.70) + (MTI * 0.30))`, (Clamped 0-10)
    *   *Significance:* This represents the final predicted Ray Tracing capability. The formula ensures that memory bandwidth (MTI) can only degrade the performance (acting as a bottleneck when it falls below the core RT score) but cannot artificially inflate the score when the dedicated hardware itself is the primary limiter.

#### Final Section 6.3 Score Calculation
Weighted combination of Standard Graphics (Raster) and Ray Tracing.
**Formula:** `Predicted_Score = (SGS * 0.9) + (RTS * 0.1)`

> [!NOTE]
> **Why 10% for Ray Tracing?** Ray Tracing (RT) is a technique where the phone's graphics chip simulates how light bounces off real surfaces — creating realistic reflections in mirrors and water, and accurate shadows. While only ~5–10% of current mobile games use it, this **10% weight is intentionally forward-looking**: manufacturers are investing heavily in RT hardware, just as they invested in 5G before streaming services caught up. Phones built today will use RT heavily within 2–3 years.
 

### 🔹 6.4 AI Hardware Performance (Neural Processor)
*Description:* Measures the raw hardware acceleration for AI/ML (Artificial Intelligence / Machine Learning) tasks. The NPU (Neural Processing Unit) or APU (AI Processing Unit) is a dedicated chip that handles AI workloads. This score reflects the device's ability to run on-device generative AI, real-time translation, and advanced image processing *quickly*.
*   **Measurement:** Geekbench AI (Quantized INT8 Score) for benchmark; NPU TOPS (Trillions of Operations Per Second) + hardware analysis for prediction.
*   **Unit:** Points (0-10)
*   **Significance:** Critical for future-proofing and enabling smooth operation of modern "AI Phone" features.

> [!IMPORTANT]
> **Hardware vs. Software:** This section measures **Hardware Capability** (The Engine). It is distinct from **Section 5.3 (AI Feature Suite)** which measures the *features* the software actually provides (The Destination). A powerful NPU (high 6.4 score) is required to run advanced features smoothly, but doesn't guarantee they are installed.

> [!NOTE]
> **Why §6.4 Uses a Different Prediction Model Than §6.1/6.2/6.3**
>
> Sections 6.1 (CPU Multi-Core), 6.2 (CPU Single-Core), and 6.3 (GPU) use **architecture-level decomposition** with frequency scaling — they model *how the silicon works* (architecture score × frequency × core count). This is possible because CPU/GPU specifications (ISA, core count, clock speeds, IPC — Instructions Per Cycle) are publicly documented.
>
> Section 6.4 uses a **weighted-sum of system-level factors** instead, because:
> 1. **NPU architectures are opaque.** Unlike ARM CPU cores (where IPC is well-known), NPU internals (Hexagon tensor units, Apple Neural Engine cores, MediaTek APU MAC — Multiply-Accumulate — arrays) are proprietary and insufficiently documented for frequency-scaled decomposition.
> 2. **Heterogeneous compute delegation.** AI workloads dynamically switch between NPU, GPU, and CPU depending on operator support — varying per model, framework, and driver version.
> 3. **Software stack is critical.** Two chips with identical TOPS can differ 2–3× in real benchmarks due to software optimization (e.g., Apple CoreML vs. generic NNAPI — Android Neural Networks API).
>
> The weighted-sum approach captures the *system-level factors* that collectively determine AI performance — which is exactly what the Geekbench AI benchmark measures.

#### 6.4.0 NPU (Neural Processing Unit) Architecture Reference Table

**Source of Truth:** The full authoritative lookup table is located in [proposed_data_structure.md] under **SOC_NEURAL_PROCESSING_UNIT_(NPU)_/_AI_ACCELERATOR_LOOKUP_TABLE**.

Each NPU is scored using three measurable hardware factors:

*   **Peak INT8 TOPS (50%) — Raw Throughput**
    *   *What it measures:* Theoretical peak computational capacity at 8-bit integer precision.
    *   *Justification:* While TOPS represents the raw "horsepower," it is a theoretical maximum. A high TOPS rating alone can be misleading without structural efficiency, which is why its weight is capped to prevent over-indexing on marketing numbers.

*   **Architecture Generation (30%) — Structural Sophistication**
    *   *What it measures:* The design efficiency of hardware blocks, including operator coverage, tensor scheduling, on-chip SRAM cache size, and dedicated transformer acceleration.
    *   *Justification:* This dictates how effectively the hardware actually utilizes its raw TOPS. Modern generative AI (LLMs) requires specific data-flow patterns that traditional ML accelerators may struggle with, regardless of their TOPS.

*   **Precision Support (20%) — Bandwidth Efficiency**
    *   *What it measures:* The range of numerical precisions (e.g., INT4, INT8, FP16) supported natively by the hardware.
    *   *Justification:* Lower-bit precision (like INT4) drastically reduces memory bandwidth bottlenecks—halving the data payload—which allows for significantly faster token generation and lower power consumption in edge AI tasks.

**NPU Score Formula:**
`TOPS_Normalized = 10 * (log(TOPS) − log(NPU_TOPS_Min)) / (log(NPU_TOPS_Max) − log(NPU_TOPS_Min))`
`NPU_Score = 0.50 * TOPS_Normalized + 0.30 * ArchGen_Score + 0.20 * Precision_Score` (Clamped 0-10)

> [!NOTE]
> **Why logarithmic for TOPS?** The real-world usability impact of TOPS follows a curve of diminishing returns. The jump from 1 TOPS (cannot run any modern AI model locally) to 11 TOPS (can run image classification, voice processing, photo enhancement) is transformative. The jump from 35 TOPS to 45 TOPS improves LLM (Large Language Model) token generation speed by milliseconds — imperceptible for most daily AI tasks.

> [!NOTE]
> **Cross-vendor TOPS comparability:** TOPS are not perfectly comparable across vendors. Apple's 15.8 TOPS Neural Engine may outperform Qualcomm's 26 TOPS Hexagon in real-world benchmarks due to architectural efficiency and software optimization differences. The **Architecture Generation (30%)** and **Precision Support (20%)** weights are explicitly designed to over-index and compensate for this mismatch. They prioritize the chip's intelligence, operator design, and bandwidth efficiency over sheer raw operations, establishing a neutral baseline that confidently normalizes these discrepancies.

**Architecture Generation Score (30% weight)**

This factor captures the sophistication of the NPU's internal design beyond raw throughput. The classification criteria below are designed for neutral, vendor-agnostic scoring by an AI agent.

**Architecture Generation Classification Tiers**

**[ 10.0 ] Gen AI Native**
*   **Technical Definition:** Purpose-built for on-device generative AI and LLM (Large Language Model) inference.
*   **Classification Criteria:** **ALL** of:
    1.  Dedicated hardware transformer acceleration or autoregressive token generation pipeline.
    2.  Dynamic precision scheduling pipeline and high-bandwidth native data flow.
    3.  On-chip model management with large shared memory/SRAM cache (≥ 2 MB) replacing L2 wait-times.
    4.  Vendor explicitly markets the chip design architecture as native for local LLM execution (Llama, Gemini Nano, etc.).
*   **Key indicator:** The chip was designed *from the ground up* for generative AI, utilizing structurally different core clusters than a prior generation ML-focused design.

**[ 8.0 ] Gen AI Capable**
*   **Technical Definition:** Supports generative AI workloads via broad tensor operation capabilities.
*   **Classification Criteria:** **ALL** of:
    1.  Dedicated NPU (Neural Processing Unit) with heavy tensor/matrix calculation hardware.
    2.  Advanced memory routing to emulate missing native pipeline operations.
    3.  Can execute complex quantized LLMs across the system stack (albeit using more generic operations than Gen AI Native).
    4.  Vendor has demonstrated on-device LLM or Stable Diffusion execution.
*   **Key difference from Gen AI Native:** Lacks purpose-built transformer pipeline hardware and extreme SRAM; LLM execution relies entirely on generic matrix multipliers causing higher energy consumption per token.

**[ 6.0 ] ML Optimized**
*   **Technical Definition:** Efficient tensor/matrix acceleration designed strictly for traditional ML (Machine Learning) inference (image classification, object detection).
*   **Classification Criteria:** **ALL** of:
    1.  Dedicated NPU with specific tensor acceleration hardware blocks (not just vector/SIMD — Single Instruction, Multiple Data).
    2.  Comprehensive operator coverage allowing full model execution without CPU assist.
    3.  Efficient silicon layout dedicated to sustained low-power ML camera feeds.
*   **Key difference from Gen AI Capable:** No specific generative AI architecture evolution. The NPU relies on older data-flow structures and excels at fixed-input inference tasks, but the hardware is fundamentally not pipelined for autoregressive token generation.

**[ 4.0 ] ML Accelerated**
*   **Technical Definition:** Dedicated NPU hardware using basic tensor operations.
*   **Classification Criteria:** **ANY** of:
    1.  Named dedicated NPU/AI accelerator (Hexagon 770/780, Neural Engine 8/16-core, APU 3.0/580/590/650, Cambricon, Da Vinci 1.0, Xclipse, Imagination NNA — Neural Network Accelerator).
    2.  NPU provides basic hardware-level tensor multiplication support (INT8) for fixed-function ML tasks.
    3.  Device can accelerate standard ML models (face detection, scene recognition, noise reduction) on the NPU without CPU fallback.
*   **Key difference from ML Optimized:** The NPU has limited mathematical operator coverage and lacks unified on-chip data scheduling. This forces many complex AI operations to fall back to the GPU or CPU.

**[ 2.0 ] DSP/HVX Assisted**
*   **Technical Definition:** Digital Signal Processor (DSP) with vector extensions handling AI tasks.
*   **Classification Criteria:** **ALL** of:
    1.  No dedicated NPU — AI is processed by a DSP with SIMD vector extensions (e.g., Qualcomm HVX — Hexagon Vector eXtensions, MediaTek APU 2.0).
    2.  AI workloads execute via vector math, not tensor-specific hardware.
*   **Key indicator:** The AI accelerator was originally designed for audio/image signal processing and repurposed for basic neural network inference. Limited operator support; many AI models fall back to CPU.

**[ 0.0 ] CPU-Only Emulation**
*   **Technical Definition:** No dedicated AI hardware.
*   **Classification Criteria:** **ALL** of:
    1.  No NPU, no AI-capable DSP, no dedicated accelerator.
    2.  All AI workloads run on general-purpose CPU or GPU.
    3.  Spec sheets and vendor documentation make no mention of AI/NPU/ML hardware acceleration.
*   **Examples:** Helio G85/G88, Unisoc T606/T612/T616.


**Precision Support Score (20% weight)**

This dimension measures the range of mathematical data formats the AI hardware can process natively. It is critical because executing AI models at lower bit depths (e.g. 4-bit vs 16-bit) exponentially reduces the memory bandwidth required, allowing massive Generative AI models to run faster and cooler without draining the battery. If a chip natively supports a wide array of precision formats, it provides developers immense flexibility to optimize specific models exactly to the hardware.

**Precision Support Classification Levels**

**[ 10.0 ] INT4+8+FP16**
*   **Classification Criteria:** Vendor documentation confirms native support for all three precision formats. INT4 (4-bit Integer) support is the key differentiator — verify via official specs or SDK (Software Development Kit) documentation.
*   **Scoring Rationale:** Native INT4 support is the defining hardware capability of modern generative AI chips. Under memory-bandwidth-bound Large Language Model (LLM) execution, reducing weight representation from 8-bit to 4-bit cuts the memory transfer payload in half. This directly doubles token-generation throughput and reduces system power draw, justifying the top score tier (+3.00 over INT8+FP16).

**[ 7.0 ] INT8+FP16**
*   **Classification Criteria:** Standard modern support. Vendor confirms both INT8 (8-bit Integer) and FP16 (Half-Precision Floating Point) on the NPU. No INT4 capability.
*   **Scoring Rationale:** Native FP16 support allows the NPU to execute complex floating-point activation layers (such as Softmax or Layer Normalization) natively, without forcing high-latency fallbacks to the GPU or CPU. This represents a solid general-purpose acceleration tier, earning a +3.00 jump over INT8 only.

**[ 4.0 ] INT8 only**
*   **Classification Criteria:** NPU supports only 8-bit integer operations.
*   **Scoring Rationale:** Transitioning from software emulation to a dedicated hardware execution block represents the single largest shift in processing efficiency. This justifies a solid baseline score of 4.00, representing dedicated silicon acceleration.

**[ 0.0 ] None**
*   **Classification Criteria:** No dedicated precision support (CPU-only emulation).
*   **Scoring Rationale:** AI workloads must run entirely on general-purpose CPU vectors, which lacks pipeline efficiency or dedicated matrix multiply blocks.

*Note: Smartphone NPUs are designed exclusively for energy-efficient edge inference, which mandates quantized integer execution (INT8 and INT4). Floating-point-only execution units (FP16 only) are extremely inefficient for these workloads and are not manufactured for mobile devices; floating-point tasks on such systems are instead processed by the GPU. Thus, there is no FP16-only category in this scoring system.*


**Extract of the NPU Reference Table**:

| SoC Model                 | NPU / AI Engine       | TOPS (INT8) | Arch Gen        | Precision   |
| :------------------------ | :-------------------- | :---------: | :-------------- | :---------- |
| **Snapdragon 8 Elite**    | Hexagon (Oryon NPU)   |      45     | Gen AI Native   | INT4+8+FP16 |
| **Dimensity 9400**        | APU 890               |     ~40     | Gen AI Native   | INT4+8+FP16 |
| [...]                     | [...]                 |    [...]    | [...]           | [...]       |

> [!IMPORTANT]
> **Source of Truth:** For the complete NPU Reference Table refer to **SOC_NEURAL_PROCESSING_UNIT_(NPU)_/_AI_ACCELERATOR_LOOKUP_TABLE** in [proposed_data_structure.md].

#### Scoring Architecture

The AI hardware score is fundamentally built upon the **AI System Score** (Method A/B/C) but incorporates overarching platform constraints that determine real-world utility. While benchmarks measure the "Engine," this model also accounts for the "Fuel" (RAM), the "Hangar" (Storage), and the "Cooling" (Thermals).

> [!NOTE]
> **Throughput vs. Operability (Preventing Double-Counting Risk):**
> To prevent the risk of double-counting physical resources (such as memory modules, processing engines, and thermal solutions), this framework explicitly distinguishes the **Throughput Layer** (active speed) from the **Operability & Utility Layer** (system compatibility and sustainment):
> *   **Throughput Layer (within the AI (Artificial Intelligence) System Score):**
>     *   **RAM (Random Access Memory) Technology** is scored strictly for its **bandwidth** (how fast data transfers).
>     *   **GPU (Graphics Processing Unit)** and **CPU (Central Processing Unit)** are scored strictly for their raw **compute** potential as fallback execution engines.
> *   **Operability & Utility Layer (applied as final composite factors):**
>     *   **RAM Capacity** represents **model-fit** (whether a Large Language Model (LLM) can actually fit in memory to run at all, preventing performance-crushing swap activity).
>     *   **Storage Capacity** represents **model residency** (the capacity to persist multiple large model files locally).
>     *   **Storage Technology** represents **cold-start latency** (how fast model files are loaded from disk storage into memory).
>     *   **Thermal Persistence (TDSI - Thermal Dissipation Stability Index)** represents **sustainment** (the capability to maintain performance over long, continuous tasks without throttling, distinct from short-burst execution).
> 
> This clear division ensures that while the same physical components are evaluated, they are scored for entirely different aspects of system performance (speed vs. capacity/sustainment), avoiding any mathematical or physical double-counting.

**What Geekbench AI Quantized 8-bit Integer (INT8) Measures vs. What It Does Not:**

| Factor                 | In Benchmark?| Impact & Justification                                                                 | How is it captured in scoring  |
|:-----------------------|:------------:|:---------------------------------------------------------------------------------------|:-------------------------------|
| **NPU Raw Throughput** |   **Yes**    | Primary driver for matrix math and tensor operations on the NPU.                       | AI System Score (Method A/B/C) |
| **RAM Bandwidth**      |   **Yes**    | The "Memory Wall": determines if data can reach the NPU fast enough for LLM inference. | AI System Score (Method A/B/C) |
| **GPU/CPU Fallback**   |   **Yes**    | Universal compute fallback for unsupported or floating-point operators.                | AI System Score (Method A/B/C) |
| **Software Stack**     |   **Yes**    | Driver-level optimization (CoreML, QNN) can improve performance by 2-3x.               | AI System Score (Method A/B/C) |
| **RAM Capacity**       |   **No**     | **Primary Residency Factor:** Determines if a model *can* be loaded into memory.       | Added on top of Method A/B/C   |
| **Storage Capacity**   |   **No**     | **Secondary Residency Factor:** Determines if models *can* be persisted locally.       | Added on top of Method A/B/C   |
| **Storage Technology** |   **No**     | **Cold-start Latency:** Determines fixed loading delay from disk to RAM.               | Added on top of Method A/B/C   |
| **Thermal Persistence**|   **No**     | **Sustainability:** Ensures performance doesn't throttle during 10+ minutes tasks.     | Added on top of Method A/B/C   |


#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct Geekbench AI score is available. It provides the most accurate representation of real-world AI system performance, as it tests the full hardware + software stack (NPU, GPU fallback, CPU fallback, memory bandwidth, and driver optimization) simultaneously.
*   **Source:** [Geekbench AI Leaderboard](https://browser.geekbench.com/ai-benchmarks)
*   **Metric:** Quantized Score (INT8)
    *   *Why Quantized?* Mobile NPUs are optimized for integer math (INT8) for efficiency. Evaluating FLOAT32 (Full Precision) often falls back to the CPU/GPU, missing the NPU's true potential.
*   **Normalization:**
    *   **Formula:** `Benchmark_AI_System_Score = 10 * (log(Geekbench_AI_Score) - log(AI_GB_Quant_Score_Min)) / (log(AI_GB_Quant_Score_Max) - log(AI_GB_Quant_Score_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ AI_GB_Quant_Score_Max
    *   **Min Score (0.0):** ≤ AI_GB_Quant_Score_Min

> [!NOTE]
> **Why Logarithmic?** AI performance utility follows a curve of diminishing returns. A **+5,000 point** jump from a legacy 1,000-point score to 6,000 is transformative — enabling the shift from basic cloud-assisted tasks to capable local voice processing and real-time photo object removal. An identical **+5,000 point** jump from 75,000 to 80,000 represents a marginal improvement imperceptible for 99% of daily AI features.

#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.

**1. Identify Neighbors via Feature Distance (Minimum Variance)**
Find the 3 devices that are statistically closest across **all** AI-relevant hardware components.
*   **Search Space:** All phones with known Geekbench AI scores (Method A), **excluding the target device** itself.
*   **Distance Metric:** Weighted Euclidean Distance.
    *   `Distance = Sqrt( 0.40*(NPU_Diff)^2 + 0.20*(RAM_Tech_Diff)^2 + 0.15*(Software_Stack_Diff)^2 + 0.15*(GPU_Diff)^2 + 0.10*(CPU_Diff)^2 )`
    *   *Where "Diff" is the difference between Target and Neighbor scores for each component:*
        *   `NPU` (§6.4 table), `RAM_Tech` (§6.5), `GPU` (§6.3), `CPU` (§6.2), `Software_Stack` (Software Stack tier, see dedicated paragraph below).
    *   **Scientific Rationale:** Weights mirror the proportional Method C AI System Score component weights to ensure neighbors are selected based on the most critical AI performance factors. RAM Capacity, Storage Capacity & Technology and TDSI (Thermal Dissipation & Stability Index) are excluded from this matching stage because they are applied globally *after* interpolation.
    *   **Important:** Component score retrieval rules for calculations and distance matching:
        *   **For Spec-only Components (NPU, RAM Technology and Software Stack):** Use the spec-based predicted/subscore values (specifically for RAM, use the Predicted Score before any boosters) to maintain database neutrality.
        *   **For Benchmark-driven Components (CPU and GPU):** Use the **Final Scores** (which prioritize real-world benchmark data over theoretical specifications).
        *   **⚠️ Specific Component Overrides:**
            *   For the `CPU` component, use the CPU Single-Core Final Score.
            *   For the `GPU` component, use strictly the **Standard Graphics Final Score** (which excludes the Ray Tracing component, as Ray Tracing does not contribute to AI performance). Do NOT use the overall composite GPU Final Score.
*   **Selection:** Pick the 3 distinct neighbors with the smallest `Distance`.

> [!TIP]
> **Why this is robust:** This method ensures we compare apples to apples. A phone with a **High NPU Score + Low RAM Bandwidth** will match with similar devices, rather than matching with a **Low NPU Score + High RAM Bandwidth** device, even if they have the same Overall Predicted Score. This is critical because AI workloads scale differently with compute vs. bandwidth.

**2. Calculate Correction Ratio:**
*   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
    *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
*   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
    *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.

**3. Apply to Benchmark:**
*   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
*   `Interpolated_AI_System_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

#### Method C: Predicted Calculation (Tertiary)
Used as a standalone fallback if no neighbors exist, or as the **Predictor** for Method B.

**Predicted AI System Score Calculation**
The predicted AI System Score is a weighted sum of 5 system-level factors. Unlike §6.1/6.2/6.3 which decompose CPU/GPU architecture at the silicon level, §6.4 captures the *system-level factors* that collectively determine AI performance — because NPU architectures are proprietary and cannot be decomposed from public specifications (see Design Rationale above).

1.  **NPU Core Score (40%) — The Discrete Engine**
    *   **Source:** Retrieve from the **§6.4.0 NPU Lookup Table**.
    *   **Rationale:** The NPU executes the majority of quantized AI operations. Weight is set at 40% (rather than 100%) to acknowledge that NPU performance is useless if throttled by the "Memory Wall" or unoptimized drivers.

2.  **RAM Technology Score (20%) — The Data Highway**
    *   **Source:** Retrieve **Predicted Score** from **Section 6.5**.
    *   **Rationale:** **Memory-Bound vs. Compute-Bound:** Deep learning workloads (especially the "decode" phase of LLMs) are bottlenecked by memory bandwidth. LPDDR5X (8.5 Gbps) vs LPDDR4X (4.2 Gbps) represents a 2x throughput delta. Weight is boosted to 20% to reflect the critical role of the data highway in preventing NPU starvation.

3.  **AI Software Stack Optimization (15%) — The Driver Intelligence**
    *   **Source:** Tiered classification based on the device's AI framework ecosystem (see classification below).
    *   **Rationale:** Two chips with identical hardware can differ 2–3× in benchmarks due to software optimization. Apple's Core ML is tightly integrated with the Neural Engine, extracting near-100% utilization. Qualcomm's QNN (Qualcomm Neural Network SDK) provides optimized NPU delegation. Meanwhile, some devices rely on generic NNAPI delegates that leave significant NPU capability untapped. This factor captures the *efficiency of OS-level hardware utilization*, completely orthogonal to the physical architecture generation.

4.  **GPU Performance Score (15%) — The Compute Fallback**
    *   **Source:** Retrieve the **Final Standard Graphics Score** from **Section 6.3**.
    *   **⚠️ IMPORTANT:** Use the rasterization-only score (SGS) and NOT the overall composite GPU score, as Ray Tracing hardware acceleration does not contribute to AI workloads.
    *   **Rationale (Realized Capability):** GPUs handle complex operators and floating-point tasks that many mobile NPUs avoid. A strong GPU ensures the phone handles complex fallback operations. By using the Final Score, we capture the actual graphical throughput proven by benchmarks. This ensures the AI model reflects the real-world fallback capacity of the system rather than a theoretical silicon limit.

5.  **CPU Single-Core Performance (10%) — The Task Scheduler**
    *   **Source:** Retrieve the **Final Score** from **Section 6.2**.
    *   **Rationale:** Individual operator orchestration and serial fallback tasks rely on the CPU's IPC (Instructions Per Cycle). For budget devices with no dedicated NPU (e.g., Helio G85, Unisoc T606), the CPU is the *sole* processor running AI workloads. Even on flagships, certain unsupported model operators fall back to CPU. *Why §6.2 (Single-Core)?* AI inference pipelines are predominantly serial (one neural network layer feeds the next). Single-thread IPC is the primary determinant of CPU-executed AI operator speed. Using the Final Score (which favors the benchmark score) captures the actual realized single-thread performance (including software/scheduling modifiers) which directly dictates the speed of CPU-executed AI operators.

**AI Software Stack Scoring Guideline:**

To ensure an objective score can be assigned to every phone—from legacy models to upcoming flagships—the classification uses tier-based definitions representing the integration depth of the machine learning (**ML**) software frameworks. 

The detailed programmatic execution checks (boolean rule checks) are defined canonically in [proposed_data_structure.md], which serves as the single source of truth for execution.

#### Rationale & Overview of Software Integration
The raw performance of the physical hardware (such as processing cores and memory) is only one half of the performance equation for mobile artificial intelligence (**AI**). The second, equally critical half is the optimization of the software stack. The software stack functions as the translation layer between high-level machine learning (**ML**) models (e.g., neural networks) and the low-level binary instructions executed by the silicon. 

A highly co-optimized software stack reduces serialization overhead (time lost converting data formats), enables model quantization (shrinking models to fit in memory), optimizes memory throughput to prevent processor starvation, and routes mathematical operations to the most efficient physical hardware block (such as a dedicated neural processing unit (**NPU**)). Two devices with identical silicon hardware can show a 2x to 3x difference in execution speed and battery efficiency solely due to the integration quality of their software drivers and machine learning (**ML**) compilers.

To capture this efficiency, the software stack is categorized into five distinct tiers based on the depth of compiler integration, hardware acceleration application programming interfaces (**APIs**), and driver optimization:

*   **[ 10.0 ] Tier 1: Native Synergistic (Closed-Loop Frameworks)**
    *   *Definition:* The device manufacturer natively designs the operating system (**OS**) framework strictly for their own silicon compiler. This guarantees exclusive high-speed pipelines bypassing generic application programming interface (**API**) translation layers (e.g., **Apple Core ML**, **Google Android AICore + Edge TPU** [Tensor Processing Unit], **Huawei MindSpore**).
    *   *The "Why" & Performance Overview:* A score of 10.0 is allocated because the hardware layout and the operating system (**OS**) framework are co-designed by the same manufacturer in a closed loop. Developers write applications targeting the native OS compiler, which translates models directly into machine instructions tailored for that specific chipset. This eliminates generic runtime translation layers, maximizes physical hardware utilization, and yields the lowest possible latency and battery consumption. Examples include Apple devices running Core ML on the Apple Neural Engine, Google Tensor devices utilizing Android AICore with the built-in Edge **TPU** (Tensor Processing Unit), and Huawei devices running MindSpore on HiSilicon Kirin chipsets.

*   **[ 8.0 ] Tier 2: SDK Co-Optimized (Vendor-Specific Frameworks)**
    *   *Definition:* The device uses a modern 3rd-party System on Chip (**SoC**) supported by a robust, vendor-specific optimization software development kit (**SDK**) that bridges the OS and hardware (e.g., **Qualcomm QNN** [Qualcomm Neural Network], **MediaTek NeuroPilot**, **Samsung ENN** [Exynos Neural Network]). This tier also captures devices containing custom co-processors (e.g., **Oppo MariSilicon**, **Vivo V-series**, or **Xiaomi Surge**).
    *   *The "Why" & Performance Overview:* A score of 8.0 represents highly optimized execution using vendor-specific software development kits (**SDKs**) on modern third-party processors. It is slightly lower than Tier 1 because the operating system (**OS**) must translate calls through the chipmaker's external driver library, introducing minor runtime serialization overhead. However, developers can still target the physical hardware directly. Qualcomm Snapdragon processors using the **QNN** (Qualcomm Neural Network) library, MediaTek Dimensity processors using NeuroPilot, and Samsung Exynos processors using **ENN** (Exynos Neural Network) belong to this tier, as do devices with dedicated custom co-processors like Oppo's MariSilicon.

*   **[ 5.5 ] Tier 3: Hardware Accelerated / Optimized Fallback (Legacy APIs)**
    *   *Definition:* The device lacks a modern dedicated **NPU** (**Neural Processing Unit**) but features an OS-level API highly optimized for bare-metal **GPU** (**Graphics Processing Unit**) acceleration or standard fixed-function blocks (e.g., **Apple Metal Performance Shaders (MPS)**, **Qualcomm SNPE** [Snapdragon Neural Processing Engine]). It also includes legacy vector digital signal processor (**DSP**) configurations (e.g., **Qualcomm DSP/HVX** [Hexagon Vector Extensions]).
    *   *The "Why" & Performance Overview:* A moderate score of 5.5 is assigned to older or budget architectures that do not possess a modern, dedicated NPU but still feature hardware-accelerated processing via older or general-purpose hardware blocks. This includes running machine learning (**ML**) instructions on a graphics processing unit (**GPU**) via optimized frameworks like **MPS** (Metal Performance Shaders) on older iPhones, or using legacy digital signal processors (**DSPs**) via libraries like **SNPE** (Snapdragon Neural Processing Engine) and Hexagon Vector Extensions (**HVX**) on older Qualcomm platforms. While much faster than standard central processing unit (**CPU**) execution, these units incur high memory-copy latency and consume significantly more power, lacking the dedicated hardware math pipelines needed for modern large-scale neural networks.

*   **[ 3.0 ] Tier 4: CPU/GPU Fallback (Generic Emulation)**
    *   *Definition:* The device relies entirely on generic runtime translation (e.g., standard **Android NNAPI** [Neural Networks API] or early OpenGL kernels). Operations are emulated slowly without pipeline-specific silicon (e.g., budget Unisoc/Helio **CPU** [Central Processing Unit] only chipsets, legacy 32-bit/early 64-bit iPhones).
    *   *The "Why" & Performance Overview:* A low score of 3.0 is given because the device contains no hardware acceleration block or vendor-specific compiler support for machine learning (**ML**). Instead, the system relies on general-purpose runtime interpreters, such as standard **NNAPI** (Neural Networks Application Programming Interface) on budget Android devices or generic OpenGL graphic shaders. Computational workloads are slowly executed on standard CPU cores or generic GPU cores, resulting in high latency, extreme thermal generation, and high battery drain, which makes real-time AI usage impractical. Examples include low-end Unisoc and MediaTek Helio processors, and legacy iPhones (such as the iPhone 4S to the iPhone 5s running older Apple A4 to A7 chipsets).

*   **[ 0.0 ] Tier 5: Minimal / None (No Framework)**
    *   *Definition:* Device lacks any software framework capable of **ML** (**Machine Learning**) execution (e.g., feature phones running KaiOS, Series 30+, Symbian, or early proprietary OS, and legacy processors pre-A7).
    *   *The "Why" & Performance Overview:* A score of 0.0 is assigned because the system has no software framework or runtime capable of loading or running machine learning (**ML**) models (e.g., legacy feature phones running operating systems like KaiOS, Series 30+, Symbian, or early proprietary firmware, and devices with vintage hardware architectures pre-dating the Apple A7 processor).

> [!NOTE]
> **On §5.3 interaction:** §5.3 (AI Feature Suite) measures *what AI features exist* — a checklist of tools. The Software Stack score here measures *how efficiently the hardware is utilized* — driver quality. A phone could score 10/10 on Software Stack (excellent CoreML) but 0/10 on §5.3 (no features installed). These are orthogonal dimensions; overall section weights can be adjusted to calibrate the AI domain's total contribution to the system score.

`Predicted_AI_System_Score = (0.40 * NPU) + (0.20 * RAM_Tech) + (0.15 * Software_Stack) + (0.15 * GPU) + (0.10 * CPU)`  (Clamped 0-10)


#### Section 6.4 Score Summary & Final Calculation

The overall Section 6.4 score is a composite of the core processing engine capability and the physical system constraints required for real-world utility.

**Component Weights & Justification:**

1.  **AI System Score (75%):** Derived via the standard **Method A → B → C** priority hierarchy. This represents the "Active Speed" of the runtime environment.
2.  **RAM Capacity Factor (10%):** **Predicted Score** from §6.6. This is the **Primary Residency Factor**. Large on-device models require ~8 Gigabytes (GB) of memory to load; capacity is a hard binary constraint on whether an AI task can even start without immense performance-crushing swap activity. Geekbench AI's test models are small enough that RAM capacity rarely bottlenecks the benchmark — but for real-world use (loading local Large Language Models (LLMs)), it matters. *Note: excess RAM (e.g., 24 GB) doesn't make a small task faster, so this weight is limited to 10%.*
3.  **Thermal Dissipation & Stability (7.5%):** Component score from §6.10. Always use the **Final Score** (final TDSI). Ensures performance does not throttle during sustained generative tasks (high heat generation). Geekbench AI is a burst test (30–90 seconds per workload). For real-world sustained AI usage (running a local LLM for 10+ minutes, continuous AI camera processing), the phone's complete thermal envelope matters: the chassis's ability to absorb heat, the internal cooling system such as vapor chamber or graphite sheet, and the process node efficiency — smaller nanometer = less heat generated for the same level of performance (Captured via the empirical Peak Power measurement).
4.  **Storage Capacity Factor (5.0%):** **Predicted Score** from §6.8. This is the **Secondary Residency Factor**. It determines the maximum size and variety of models the device can persist locally.
5.  **Storage Technology Factor (2.5%):** **Predicted Score** from §6.7. Determines "Cold-start Latency"—the speed at which a model is fetched from disk to RAM.

**Final Formula:**
`Score = (AI_System_Score * 0.75) + (RAM_Capacity_Factor * 0.10) + (TDSI_Score * 0.075) + (Storage_Capacity_Score * 0.05) + (Storage_Technology_Score * 0.025)` (Clamped 0-10)


### 🔹 6.5 RAM Technology - Memory Technology Efficiency Index (MTEI)
*Description:* This section evaluates the efficiency and throughput of the physical RAM (Random Access Memory) module. RAM is the device's "short-term memory" where active data is stored for immediate access. Newer technologies like LPDDR (Low Power Double Data Rate) standard LPDDR5X allow for significantly faster data transfer speeds—measured in **MT/s (Megatransfers per second)**—while consuming less power than older generations.

*   **Measurement:** JEDEC (Joint Electron Device Engineering Council) standard specification and data rate.
*   **Unit:** MT/s (Megatransfers per second) — used to quantify the effective speed of the memory bus.
*   **Significance:** Higher MT/s ratings directly improve app launch speeds, multitasking responsiveness, and AI processing efficiency (§6.4). Modern LPDDR standards also incorporate sophisticated power management features that extend battery life.

#### MTEI Scoring Formula
This section uses a **Logarithmic Scoring Formula** to derive the MTEI score from the effective MT/s.

> **Formula:** `Score = 10 * (log(MT/s) - log(RAM_MTS_Min)) / (log(RAM_MTS_Max) - log(RAM_MTS_Min))`  (Clamped 0-10)
> *   **Max Score (10.0):** ≥ RAM_MTS_Max (LPDDR5X Ceiling)
> *   **Min Score (0.0):** ≤ RAM_MTS_Min (LPDDR3 Baseline)

> [!NOTE]
> **Why Logarithmic?** 
> The real-world performance impact of memory bandwidth follows a curve of diminishing returns. Once bandwidth reaches a specific threshold relative to the system's architecture, the primary performance bottleneck shifts from memory throughput to CPU IPC (Instructions Per Cycle), storage latency, and software efficiency.
>
> **Logarithmic Scaling Rationale:** A **1000 MT/s increase** at entry-level speeds (e.g., from **1600 to 2600 MT/s**) represents a significant **~1.6x jump** in throughput, which significantly transforms system responsiveness. In contrast, the same **1000 MT/s increase** at flagship levels (e.g., from **9600 to 10600 MT/s**) yields only a marginal **~1.1x gain**, providing negligible perceptible benefit for daily tasks or even heavy gaming workloads.

#### Terminology & Autonomous Resolution

**Extract of the MTEI Reference Table** (see full list in [proposed_data_structure.md]):

| Denomination               | MT/s  |
| :------------------------- | :---: |
| **LPDDR5X-10667**          | 10667 |
| **LPDDR5T / LPDDR5X-9600** |  9600 |
| [...]                      | [...] |

> [!IMPORTANT]
> **Authoritative Resolution:** For the 100% precision mapping of marketing terms (e.g., "Full-blooded", "Turbo"), the complete **Data Priority Rules**, and the exhaustive **MTEI Scoring & Resolution Matrix**, refer to **[proposed_data_structure.md]**.


### 🔹 6.6 RAM Capacity - Memory Capacity Index (MCI)
*Description:* Measures the amount of physical memory available for applications and background processes. More RAM improves multitasking, reduces app reloads, and increases system stability under load.

*   **Measurement:** Total physical RAM.
*   **Unit:** Gigabytes (GB)
*   **Significance:** Determines multitasking ceiling and ability to load large AI models (§6.4). 

#### MCI Score Formula
This section uses a **Logarithmic Scoring Formula** to derive the score from physical capacity.

> **Formula:** `Score = 10 * (log(GB) - log(RAM_GB_Min)) / (log(RAM_GB_Max) - log(RAM_GB_Min))` (Clamped 0-10)
> *   **Max Score (10.0):** ≥ RAM_GB_Max
> *   **Min Score (0.0):** ≤ RAM_GB_Min

> [!IMPORTANT]
> **Virtual RAM Exclusion Policy:** To ensure deterministic hardware scoring, any form of "Virtual RAM", "Extended RAM", "Dynamic RAM Expansion", or "RAM Plus" (which uses slower internal storage as swap space) is strictly **EXCLUDED** from the `capacity_gb` input. Only the physical, soldered RAM capacity is scorable.

> [!NOTE]
> **Why Logarithmic?** The utility of RAM follows a curve of diminishing returns. Going from 4GB to 8GB (+4GB) dramatically improves multitasking and system stability. However, an identical +4GB upgrade from 20GB to 24GB offers almost zero tangible benefit for current mobile applications.


### 🔹 6.7 Storage Technology
*Description:* This section evaluates the efficiency and throughput of the device's internal non-volatile storage. Faster storage technology directly impacts system boot times, application installation speed, file transfer rates, and the overall responsiveness of the OS (Operating System) when loading heavy data (e.g., high-resolution textures in games or large AI (Artificial Intelligence) models).

*   **Measurement:** Storage Protocol and Generation.
*   **Unit:** Protocol Class (Discrete) / Sequential Read Speed (MB/s)
*   **Significance:** Determines the data bottleneck between the flash memory and the SoC (System on Chip).

#### Technical Differentiators & Terminology
*   **UFS (Universal Flash Storage):** The modern serial interface standard for mobile storage, succeeding eMMC.
*   **NVMe (Non-Volatile Memory express):** A high-performance transport protocol used by Apple in iPhones, optimized for low latency via the **PCIe** (Peripheral Component Interconnect Express) bus.
*   **eMMC (embedded MultiMediaCard):** A legacy parallel interface standard. It is **half-duplex** (cannot read and write simultaneously), making it a major system bottleneck.
*   **Write Booster (WB):** A performance feature (introduced in **UFS 2.2** and **UFS 3.1** and standard in **UFS 4.0**) that utilizes a high-speed **pSLC** (pseudo Single-Level Cell) cache to accelerate sequential write operations for app installs and large file downloads.
*   **Host Performance Booster (HPB):** A performance extension (introduced with **UFS 3.1** and standard in **UFS 4.0**) that caches the "Logical-to-Physical" address translation map in the system **RAM (Random Access Memory)** to reduce random read latency.
*   **Mbps (Megabits per second) / MB/s (Megabytes per second):** The units used to measure sequential data throughput.

#### Logarithmic Scoring Formula

> **Formula:** `Score = 10 * (log(MB/s) - log(STORAGE_MBPS_Min)) / (log(STORAGE_MBPS_Max) - log(STORAGE_MBPS_Min))` (Clamped 0-10)
> *   **Max Score (10.0):** ≥ **STORAGE_MBPS_Max** 
> *   **Min Score (0.0):** ≤ **STORAGE_MBPS_Min**

> [!NOTE]
> **Why Logarithmic?** 
> 1.  **Perceptual Response Scaling (Weber-Fechner Law):** Human perception of speed jumps (like app loading times) is logarithmic, not linear. A jump from 100 MB/s to 1100 MB/s (11x) is perceived as a massive transformation, whereas a jump from 3200 MB/s to 4200 MB/s (~1.3x) is barely noticeable in daily use, despite the identical +1000 MB/s raw delta.
> 2.  **Bottleneck Shift & Latency Saturation (Amdahl’s Law):** At lower speeds (eMMC), the storage interface is the primary system bottleneck. As throughput exceeds ~1500 MB/s (UFS 3.0) and random read latency hits the sub-millisecond range, the bottleneck shifts to **CPU IPC (Instructions Per Cycle)**, **RAM Latency**, and **OS Kernel/Software overhead**. Further hardware-level speed increases are masked by the time required for the OS to execute the request, providing zero practical benefit for 99% of mobile workloads.

#### Terminology & Autonomous Resolution

**Extract of the STEI Reference Table** (see full list in [proposed_data_structure.md]):

| Denomination (Logic Key)         | MB/s  |
| :------------------------------- | :---: |
| **UFS 4.1**                      | 4200  |
| **UFS 4.0 Peak / NVMe (A17/18)** | 4200  |
| **UFS 4.0 Base / NVMe (A16)**    | 3000  |
| [...]                            | [...] |

> [!NOTE]
> **On UFS 4.1:**
> UFS 4.1 is the current best estimation, temporarily resolved to the UFS 4.0 Peak performance range (4200 MB/s) to ensure scoring stability until the standard is widely implemented and benchmark data matures.

> [!IMPORTANT]
> **Authoritative Source of Truth:** For the full scoring table and detailed **Data Priority Rules**, refer to the comprehensive hardware documentation in **[proposed_data_structure.md]**.

> [!NOTE]
> **On NVMe and iPhone Mapping:**
> Because Apple does not disclose NVMe/PCIe bus details or throughput figures, iPhones are mapped to empirically established reference configurations based on historical sequential read performance benchmarks (by SoC generation), rather than manufacturer-approved specifications.

### 🔹 6.8 Storage Capacity
*Description:* This section evaluates the total physical internal non-volatile memory of the device. More storage allows for the local installation of larger applications, high-resolution media (4K/8K video), and expansive on-device AI models without requiring constant cloud offloading or data deletion.

*   **Measurement:** Total physical internal storage capacity (Advertised spec).
*   **Unit:** Gigabytes (GB)
*   **Significance:** Determines capacity for apps, media, and files.

#### Storage Capacity Scoring Formula
This section uses a **Logarithmic Scoring Formula** to derive the score from the physical capacity.

> **Formula:** `Score = 10 * (log(GB) - log(Storage_GB_Min)) / (log(Storage_GB_Max) - log(Storage_GB_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Storage_GB_Max
*   **Min Score (0.0):** ≤ Storage_GB_Min

> [!NOTE]
> **Why Logarithmic? (The AI & Media Utility Curve)**
> 1.  **AI Local Persistence:** Modern on-device Large Language Models (LLMs) and generative AI features require significant "model weight" space (often 40GB to 60GB). A jump from 64GB to 128GB is transformative because it enables the use of these models alongside essential apps.
> 2.  **Diminishing Returns:** The utility of storage follows a curve of diminishing daily impact. While the transition from 128GB to 256GB prevents "storage full" anxiety for 90% of users, an identical absolute jump at the ultra-high end (e.g., from 768GB to 896GB) provides almost zero perceptible change to the daily user experience.

#### Storage Capacity Benchmarks & Scoring Reference

| Denomination | Basis (GB) | Market Positioning & Use-Case Context          | Score (Log) |
| :----------- | :--------: | :--------------------------------------------- | :---------: |
| **2 TB**     |    2048    | **Extreme Pro**: 2026 State-of-the-Art Ceiling |  **10.00**  |
| **1 TB**     |    1024    | **Unrestricted Pro**: 8K video & AI LLMs       |   **8.75**  |
| **512 GB**   |    512     | **High Density**: Local AI & 4K libraries      |   **7.50**  |
| **256 GB**   |    256     | **Flagship Std**: Overhead for 40GB+ OS        |   **6.25**  |
| **128 GB**   |    128     | **Balanced**: Req. management for 4K media     |   **5.00**  |
| **64 GB**    |     64     | **Restricted**: OS consumes ~50% capacity      |   **3.75**  |
| **32 GB**    |     32     | **Legacy Min**: Limits Android 15 updates      |   **2.50**  |
| **16 GB**    |     16     | **Transition**: Traditional modern floor       |   **1.25**  |
| **≤8 GB**    |      8     | **2016 Baseline**: Modern Era Floor            |   **0.00**  |

> [!IMPORTANT]
> **Physical Only:** Strictly exclude "Cloud Hybrid," "Virtual Storage," or "Network Drive" capacities. Only the physical NAND flash integrated into the main logic board is eligible for scoring.


### 🔹 6.9 Storage Expandability
*Description:* Ability to add a memory card. A dedicated slot lets you cheaply add massive storage for photos and media without sacrificing connectivity.
*   **Measurement:** Slot Architecture (Discrete).
*   **Unit:** Performance Tier (0–10)
*   **Significance:** Critical for users with large media libraries, high-resolution video recording, or offline data needs, offering a significantly lower cost-per-GB compared to internal storage upgrades.

#### Scoring Tiers
| Tier       | Feature              | Key Usability Attribute                                                                       | Score     |
| :--------- | :--------------------| :-------------------------------------------------------------------------------------------- | :-------- |
| **Tier 1** | **Dedicated Slot**   | Simultaneous 2x SIM + 1x microSD usage.                                                       | **10.00** |
| **Tier 2** | **Hybrid Slot**      | Compromise: Physical tray forces choice between SIM 2 or Storage (even if eSIM is supported). | **7.00**  |
| **Tier 3** | **Proprietary Slot** | Restricted to Original Equipment Manufacturer (OEM) cards (e.g., Huawei NM).                  | **5.00**  |
| **Tier 4** | **No Expansion**     | Zero physical expansion capability.                                                           | **0.00**  |

> [!NOTE]
> **Technical Justification for Model Simplification:**
> Earlier iterations of this model considered weighted sub-scores for **Maximum Capacity** (8GB–2TB) and **Protocol Speed** (UHS-I/II, SD Express). These were abandoned for the final scoring framework because:
> 1. **Physical Bottleneck:** Virtually all modern smartphones lack the extra physical pins required for UHS-II/Express speeds, resulting in a universal fallback to UHS-I. For now, scoring the protocol would reward "paper specs" with no real-world performance delta.
> 2. **Current Utility Focus:** While doubling theoretical capacity (e.g. from 1TB to 2TB) represents a significant hardware leap, the primary value differentiator for the current "Modern Era" baseline is the *physical accessibility* and tray logic (Dedicated vs Hybrid). The current model prioritizes the hardware interface utility, but it is architecturally prepared for future updates where granular capacity thresholds or high-speed protocol requirements may be integrated as they become more prevalent in the smartphone market.

> [!IMPORTANT]
> **Authoritative Resolution:** For the mapping of marketing terms (e.g., "Triple slot", "3-card tray"), Detailed **Data Priority Rules**, and the **Autonomous Resolution Matrix**, refer to **[proposed_data_structure.md]**.


### 🔹 6.10 Thermal Dissipation & Stability Index (TDSI)
*Description:* A composite index measuring the device's physical ability to shed heat and sustain performance over time. Standard benchmarks measure instantaneous burst performance, but the TDSI models the thermodynamic reality: how much heat the phone can handle before it must forcefully throttle the processor to prevent overheating.
*   **Measurement:** Heat Dissipation Capacity (Chassis + Cooling) vs. Heat Generation (**SoC (System-on-Chip)**) / Real-world Benchmark Stability.
*   **Unit:** Composite Stability Score (0-10)
*   **Significance:** Predicts sustained frame rates, prevents severe throttling during long gaming sessions, and protects battery longevity.

#### 6.10.A Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct 3DMark Wild Life Extreme stress test score is available. It provides the most accurate snapshot of the final software-hardware thermal interaction.

**Benchmark Source: 3DMark Wild Life Extreme Stress Test**
*   **Source:** [UL Benchmarks Leaderboard](https://benchmarks.ul.com/3dmark)
*   **Metric:** **Stability %** (MUST use the Stability percentage result, NOT the performance "Score").
*   **What is Stability?** 
    *   **Definition:** Stability is the ratio of **FPS (Frames Per Second)** between the **Lowest Loop** (the slowest run recorded within the 20-minute evaluation window) and the **Highest Loop** (the fastest initial run).
    *   **Significance:** It measures the hardware's ability to maintain its peak performance throughout the standardized 20-minute stress test. A high score (e.g., 99%) means the phone handles its internal heat well enough to avoid major performance drops. A low score (e.g., 60%) means the phone had to aggressively "throttle" or slow down its engine to manage the rising heat, resulting in frame drops and stuttering as the test progresses.
    *   **Evaluation Rule:** Always ignore the 3DMark "Score" (which measures raw speed) and only extract the "Stability %" for this section.
*   **Perimeter Justification:**
    *   **INCLUDES:** GPU/CPU thermal throttling, effectiveness of internal spreaders (Vapor Chambers), and chassis convection efficiency. 
    *   **EXCLUDES:** Battery chemical efficiency (Section 8.1); Display panel efficiency (Section 2.2).

*   **Why 3DMark?** It offers the most exhaustive public database spanning iOS, Android, and all major chipsets, ensuring absolute cross-brand parity (see BENCHMARK SELECTION MATRIX below and short presentation here: https://www.xda-developers.com/3dmark-wild-life-extreme/). 

*   **Calibration Note (The "Dual-Standard"):** While 3DMark measures Frames Per Second (FPS) stability, the underlying physics model evaluates thermal Power (Watts). To ensure the model remains physically accurate, the **Burnout Benchmark**—which directly measures sustained SoC Power (Watts)—can be utilized internally by the scoring framework as a secondary calibration standard to validate the baseline power-to-FPS conversion.

# REPORT: BENCHMARK SELECTION MATRIX (Rationale for 3DMark)

| Benchmark                      | Breadth (30%) | Alignment (25%) | Transparency (20%) | Reputation (15%) | Accessibility (10%) | Weighted Total |
| :----------------------------- | :-----------: | :-------------: | :----------------: | :--------------: | :-----------------: | :------------: |
| **3DMark Wild Life Extreme**   |      10       |        6        |         9          |        10        |          9          |    **8.7**     |
| **Burnout Benchmark**          |       5       |       10        |         8          |        7         |          7          |    **7.4**     |
| **GFXBench (Manhattan)**       |       9       |        6        |         7          |        8         |          8          |    **7.6**     |
| **Geekbench 6 (GPU)**          |      10       |        4        |         6          |        10        |         10          |    **7.7**     |

| Criteria           | Description                                                             | Weight  |
| :------------------| :---------------------------------------------------------------------- | :------ |
| **Breadth**        | Number of brands, models, and platforms (iOS/Android/Windows) covered.  | **30%** |
| **Model Alignment**| Ability to measure **Watts** or thermal power directly vs. just FPS.    | **25%** |
| **Transparency**   | Disclosure of measurement methods (Queries vs. Timers) and raw logs.    | **20%** |
| **Reputation**     | Industry adoption and status as a "standard" in tech reviews.           | **15%** |
| **Accessibility**  | Ease of use for typical users/evaluators to verify scores.              | **10%** |

*   **Normalization:**
    *   **Formula:** `Score = 10 * (log(Stability_%) - log(Thermal_Stability_Min)) / (log(Thermal_Stability_Max) - log(Thermal_Stability_Min))` (Clamped 0-10) Where **Stability_%** is the benchmark result; **Min/Max** are anchors representing the full performance spectrum of all evaluated devices, accessible in `scoring_constants.md`.
    *   **Max Score (10.0):** ≥ Thermal_Stability_Max
    *   **Min Score (0.0):** ≤ Thermal_Stability_Min

> [!NOTE]
> **Why Logarithmic?** 
> **Perceptual Response Scaling (Weber-Fechner Law):** Stability loss is not perceived linearly. A drop from 100% to 90% stability transitions a game from 60 FPS to 54 FPS—a difference that is largely imperceptible during active gameplay. However, a drop from 50% to 40% transitions a game from 30 FPS to 24 FPS—crossing the critical threshold from "playable" to "cinematic stutter." The logarithmic scale correctly penalizes these catastrophic drops more heavily while preserving score nuance for minor fluctuations.


#### 6.10.B Method B: Nearest Neighbor Interpolation (Secondary / Validation) 
Method B is populated for **all** phones—even if a direct benchmark is available—to evaluate the precision of the thermodynamic model by comparing its result with empirical behavior.

**1. Identify Neighbors via Feature Distance (Minimum Variance)**
Instead of just matching the overall predicted score, we find the 3 devices that are statistically closest across the physical and thermodynamic factors that dictate thermal persistence.
*   **Search Space:** All devices with known 3DMark Stability scores (Method A), **excluding the target device** itself.
*   **Distance Metric:** Weighted Euclidean Distance in the 6-dimensional granular thermal feature space.
    > [!NOTE]
    > **Methodology Context:** These six components represent the fundamental thermodynamic variables calculated in the **Analytical RC Model (Method C)**. For a detailed breakdown of how each value (e.g., resistance_back, power_peak_soc, thermal_capacitance...) is physically derived from raw device specifications, refer to the extensive technical definitions provided in Section 6.10.C (Method C).
    *   `Distance = Sqrt( 0.40*%Diff(power_peak_soc)^2 + 0.30*%Diff(resistance_total)^2 + 0.20*%Diff(thermal_capacitance)^2 + 0.10*%Diff(power_base_needs)^2 )`
    *   *Where:*
        *   `%Diff(X) = abs(X_Target - X_Neighbor) / X_Target`
        *   **Target:** The device currently being scored.
        *   **Neighbor:** Any device in the search space with a known benchmark result.
    *   **Scientific Rationale:** The 4-parameter model creates a perfect thermodynamic symmetry by balancing the **Heat Load (50%)** against the **Cooling Capacity (50%)**. This ensures that neighbor devices are matched based on their complete energy envelope.
        *   **I. Heat Load (50%):** 
            *   **power_peak_soc (40%):** The Heat Source (SoC workload class).
            *   **power_base_needs (10%):** Parasitic System Heat (Display, PMIC, and logic overhead).
        *   **II. Cooling Capacity (50%):** 
            *   **resistance_total (30%):** Steady-state Dissipation (The Radiator). Consolidated to represent the chassis's total ability to expel heat.
            *   **thermal_capacitance (20%):** Thermal Inertia (The Mass/Inertia). Represents the energy absorption capacity during the 1200s evaluation window.
*   **Selection:** Pick the 3 distinct neighbors with the smallest `Distance`.

> [!NOTE]
> **Why Weighted Euclidean for Thermal?**
> Thermal performance is an equilibrium between independent vectors. A small phone with an efficient chip might have the same score as a large phone with a power-hungry chip, but they are not "thermal neighbors." The weighted Euclidean search ensures we compare devices with similar physical footprints and heat-generation characteristics to maintain interpolation accuracy.

**2. Calculate Correction Ratio:**
*   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
    *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
*   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
    *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.

**3. Apply to Benchmark:**
*   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
*   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`


#### 6.10.C Method C: Predicted Calculation (Tertiary, Analytical Method - The Thermodynamic RC Model)
When physical benchmark data is unavailable, this method calculates the **thermal state of the hardware at the 1200-second mark** using a Transient Resistor-Capacitor (RC) Model. 

##### 1. Model Hypotheses & Boundary Conditions
- **Linear Energy Conservation:** All heat generated by the SoC (power_in) must either be stored in the device's mass (capacitance) or dissipated through the chassis (Resistance).
- **Lumped Parameter Analysis:** The device is modeled as a single thermal node where the temperature is assumed uniform across the active radiator area.
- **Sustainability Window (t):** Performance is evaluated over a continuous 1200-second (20-minute) window. This aligns with the duration of the standardized 3DMark Wild Life Extreme Stress Test to capture "sustained" gaming reality rather than "burst" performance.
- **Psychophysical Perception:** Throttling is converted to FPS perception using the non-linear Gamma Bridge (0.333). This physical bridge coefficient converts the model's raw wattage throttling into a visual **Stability Percentage** directly comparable with 3DMark benchmark results.

The model balances two primary forces:

1.  **Heat Dissipation (Chassis/Radiator):** The maximum power (Watts) the chassis can manage at the 1200-second mark before its surface temperature surpasses the 20°C ergonomic safety threshold. *(Rationale: A 20°C rise over a standard 25°C ambient reaches the 45°C ergonomic comfort limit; above this, skin contact becomes painful over time, in alignment with IEC 62368-1 safety standards).*

> [!IMPORTANT]
> > [!CAUTION]
> > **The 25°C Ambient Constraint & Benchmark Disclosure:**
> > The 20°C safety rise (`temperature_rise_limit`) used in this model is strictly predicated on a **25°C ambient environment**. This is the standard "room temperature" baseline for mobile benchmarking to reach the 45°C physical safety limit.
> >
> > Standard benchmark reports (including 3DMark Wild Life Extreme) **do not record or disclose ambient temperature.** However, it is a critical variable: if the environment is warmer (e.g., 30°C), the admissible thermal rise before hitting the 45°C safety limit is reduced to only 15°C, which will drastically accelerate thermal throttling and lower the resulting stability score. For consistent model validation, tests must be conducted in a controlled, room-temperature environment (~25°C).

2.  **Heat Generation (SoC/Silicon):** The physical amount of heat (Watts) the processor aggressively generates under a maximum performance load.
If Generation exceeds Dissipation, the processor must throttle to prevent the phone from overheating to dangerous levels.

---

##### 2. Dissipation Analysis (The Hardware Chassis) 
The total heat the phone can sequentially dissipate is governed by several factors modeled into a Thermal Resistor-Capacitor (RC) Equation.

###### 2.1 Thermal Resistance (resistance_total) 
The difficulty of moving heat from the processor into the ambient air. Measured in Kelvin per Watt (K/W). Instead of a single thermal path, heat escapes through a **Multi-Surface Parallel Resistor Network** (Front Screen, Back Panel, Mid-Frame). The total system resistance is strictly defined by parallel circuit law:
`1 / resistance_total = (1 / resistance_front) + (1 / resistance_back) + (1 / resistance_frame)`
*   For each surface independently: `resistance_path = resistance_conduction + resistance_convection`
*   **Conductive Resistance (resistance_conduction):** The struggle to pass through the material thickness. `resistance_conduction = thickness / (thermal_conductivity * active_radiator_area)` (Where **thermal_conductivity** is Thermal Conductivity (W/m·K) and **active_radiator_area** is the effective radiator footprint).
*   **Convective Resistance (resistance_convection):** The struggle to transfer heat from the surface into the air. `resistance_convection = 1 / (h_passive * active_radiator_area)` (Where **h_passive** is the convective Heat Transfer Coefficient (W/m²·K)).
*   *Note: Air convection coefficient 'h_passive' is standardized at 10.0 W/m²·K. This value represents the combined natural convection and thermal radiation in still air for a device surface at ~45°C. Built-in active fans modify this to 30.0+.*

> [!NOTE]
> **Technical Justification for Simplifying resistance_path & Modeling internal resistance:**
> While the model formally includes **Conductive Resistance (resistance_conduction)** (through the panel thickness) for physical completeness, simulation results across diverse hardware archetypes (including the S24 Ultra case study below) prove it is mathematically negligible. On average, `resistance_convection` is 50x–1000x larger than `resistance_conduction` because smartphone panels are extremely thin (0.6–3.0 mm), allowing heat to traverse the material almost instantly compared to the slow escape into ambient air. Consequently, practical calculations may safely omit the `resistance_conduction` term, simplifying the external path formula to strictly: `resistance_path = 1 / (h_passive * active_radiator_area)`.
>
> **Modeling Internal Resistance (resistance_internal):** You may note that internal resistance (the resistance to cross from the SoC to the radiator edges) is not represented as an explicit resistor. Instead, it is indirectly modeled through **spreading_efficiency**. A high resistance_internal (poor internal cooling) artificially shrinks the active area, causing a severe localized hot spot that reaches the 45°C limit rapidly and forces throttling. By scaling footprint_area by spreading_efficiency, we accurately capture the thermodynamic consequence of resistance_internal without requiring a computationally heavy multi-node model.

###### 2.2 Sourcing Technical Parameters 
To ensure thermodynamic rigor across the three paths, the following rules apply:
1.  **footprint_area (Total Geometric Area):**
        *   **Front / Back Panel:** `footprint_area = height * width`
        *   **Mid-Frame:** `footprint_area = 2 * (height + width) * thickness * 0.85`
            *(Justification: The **0.85 Height Factor (Chi)** accounts for the structural frame band being physically shorter than the total phone height due to ergonomic chamfers, glass curves, and bezel design).*
2.  **thermal_conductivity (k):**
    *   Values are consolidated from multi-source cross-referencing (MatWeb & Engineering ToolBox) for Section 1.1 materials:
        *   **Aluminum (6k/7k):** **190 W/m·K** (Ref: 6061/7075 alloy average).
        *   **Stainless Steel:** **16 W/m·K** (Ref: SS 304/316 baseline).
        *   **Titanium Alloy (Gr5):** **7.0 W/m·K** (Ref: Ti-6Al-4V peak).
        *   **Front Screen Glass:** **1.1 W/m·K** (Standardized for all front panels).
        *   **Armor/Shield/Standard Glass:** **1.1 W/m·K** (Ref: Li-Al-Si flagship glass).
        *   **Ceramic (ZrO2):** **2.5 W/m·K** (Ref: Zirconia thermal isolation limit).
        *   **Engineering Polymer / Leather:** **0.3 W/m·K** (Ref: Glass-fiber PA range).
3.  **thickness (t) - Conduction Distance:**
    *   The thickness of the frontier material between the heat source and the environment:
        *   **Front Screen:** Constant **0.0007 m** (0.7 mm standard).
        *   **Back Panel:** Constant **0.0006 m** (0.6 mm standard).
        *   **Mid-Frame:** Constant **0.0030 m** (3.0 mm conduction path from internal mount to edge).

###### 2.3 Effective Radiator Area (active_radiator_area) 
Heat must spread across the chassis surfaces. The percentage of the phone's total footprint used as an active radiator (`active_radiator_area`) is dictated fundamentally by the **Spreader × Material Synergy** (spreading_efficiency).
Therefore: `active_radiator_area = footprint_area * spreading_efficiency`

*(Note on Environmental Exposure: We intentionally assume 100% exposure for all surfaces rather than artificially penalizing the back panel for hand or table contact. While hands and tables block natural convection of ambient air, they act as active conductive heat sinks, often dissipating more wattage than still air. Variables in environmental contact are too unpredictable to model cleanly, so the full geometric area of each surface is utilized for dissipation).*

###### 2.4 Spreading Efficiency
Not all internal cooling applies equally to all surfaces. We assess Spreading Efficiency (s_eff) structurally based on three material classes derived from Section 1.1:
-   **Class 1: High Conduction (k > 150):** Aluminum Alloys (6000/7000), Zinc Alloy (Zamak), Magnesium Alloy.
-   **Class 2: Moderate Alloy (5 <= k <= 50):** Titanium Grade 5, Stainless Steel, Amorphous Alloy.
-   **Class 3: Insulating (k < 5):** Glass (Armor/Shield/Std), Polymers (Std/HP/Reinforced), Leather.

**Surface 1: Front Screen (Always Insulating Glass)**
- *Cooling Tech:* Small internal graphite spreaders are present, but the primary heat source (SoC) is rear-mounted on the motherboard.
- **s_eff = 0.25** (Low-Medium Utilization). This correctly bottlenecks its thermal participation compared to the direct SoC-to-BackPanel contact.

> [!NOTE]
> **Why Spreading Efficiency is primarily a Back-Face Variable:**
> Vapor Chambers and heat pipes are positioned to bridge the heat between the SoC and the back panel or frame. The **Printed Circuit Board (PCB) Thermal Wall** acts as a permanent barrier for the front screen: because the SoC is mounted on the rear of the motherboard, heat must traverse the insulating FR-4 substrate to reach the display spreaders. Since the Vapor Chamber does not bypass the motherboard to touch the screen directly, the front screen's utilization remains effectively "capped" by the PCB's low vertical conductivity, regardless of how efficient the internal cooling system is at spreading heat to the back.

> [!NOTE]
> **Physical Justification for Front Screen s_eff = 0.25:**
> The front display is the most thermally bottlenecked path in any smartphone. Three independent lines of evidence converge on this value:
>
> **1. PCB Thermal Wall:** The SoC is rear-mounted on the motherboard. For heat to reach the display, it must traverse the FR-4 PCB substrate, which has a through-plane thermal conductivity of only **0.25–0.4 W/m·K** — comparable to glass. This makes the PCB itself a severe thermal insulator for vertical heat transfer. *(Ref: [MokoTechnology – "FR4 Thermal Conductivity"](https://www.mokotechnology.com/fr4-thermal-conductivity/))*
>
> **2. Graphite Anisotropy:** Internal graphite heat spreaders have extreme directional bias: **1,500–1,900 W/m·K in-plane** (excellent lateral spreading) but only **~3–5 W/m·K through-plane** (poor vertical transfer). They spread heat across the back panel effectively but do not transfer it vertically through the stack to the display side.
>
> **3. Measured CTS Data (Qualcomm/Stanford):** The Coefficient of Thermal Spreading (CTS) — a dimensionless metric quantifying surface temperature uniformity — was measured at **0.50–0.62** for commercial phones by Chiriac et al. (Qualcomm/Stanford, 2015). This means real devices thermally utilize only 50–62% of their total surface. Given that the back panel (direct SoC contact) uses 60–95% of its area and the frame ~40%, the front screen must contribute roughly **20–30%** of its footprint to produce those overall CTS values. Thermal IR imaging confirms this: front-screen heat signatures consistently show a **localized hotspot** directly over the SoC position, with the rest of the display remaining near ambient temperature. *(Ref: V. Chiriac, S. Molloy, J. Anderson, K. Goodson, ["A Figure of Merit for Smart Phone Thermal Management"](https://www.electronics-cooling.com/2015/11/a-figure-of-merit-for-smart-phone-thermal-management/), Electronics Cooling, Nov. 2015)*

**Surface 2: Mid-Frame (Sourcing based on Frame Material Class)**
- *Cooling Tech:* The frame perimeter is natively isolated from the heat source unless it is structural metal.
- **s_eff = 1.00** (Class 1: Conductive Metal): Immediate perimeter heat sharing.
- **s_eff = 0.40** (Class 2: Moderate Alloy): Delayed but significant perimeter utilization.
- **s_eff = 0.05** (Class 3: Insulating Polymer): Heat remains trapped near the SoC footprint.

> [!NOTE]
> **Why Frame Spreading is Material-Bound (Static):**
> Unlike the back panel, which has a large planar surface where cooling tech (such as a Vapor Chamber (VC)) can actively enforce spreading, the mid-frame's utility is governed by its narrow, perimeter-focused geometry. Heat must travel *along* the metal band to reach the radiator edges. Even with a Vapor Chamber bridging the SoC to the frame, the **material's intrinsic conductivity (k)** is the absolute bottleneck for this lateral perimeter distribution. Aluminum (Class 1) allows immediate global sharing (1.00), while Titanium (Class 2) and Polymers (Class 3) bottleneck the heat locally, preventing the spreader from significantly improving the frame's effective radiator area.

**Surface 3: Back Panel (The Variable Spreader)**
Below is the correlation of how internal spreaders strictly interact with the back panel material to dictate the percentage of the surface area utilized for cooling:

*  **Spreading Efficiency (s_eff): Continuous Saturation Model**

Instead of discrete tiers, the spreading efficiency of the device chassis is modeled using a **Saturation Law of Thermal Diffusion**. This physically represents the diminishing returns of cooling surface area: a small Vapor Chamber (VC) provides massive initial gains on an insulating surface, but continued expansion eventually hits a thermodynamic ceiling for that material.

**The Formula (Cumulative Heat Spreading):**
**s_eff = s_0 + (s_max - s_0) * [ 1 - exp(-Sum(alpha_i * phi_i)) ]**

**Parameter Definitions:**
1.  **s_0 (Baseline):** The inherent spreading efficiency of the chassis un-aided by cooling tech.
    *   **Class 1 (Conductive Metal):** 0.60
    *   **Class 2 (Moderate Alloy):** 0.25
    *   **Class 3 (Insulating Glass):** 0.05
2.  **s_max (Ceiling):** The isothermal saturation limit.
    *   **Metals/Alloys (Classes 1 & 2):** 1.00 (Perfect spreading possible).
    *   **Glass/Insulators (Class 3):** 0.95 (Limited by vertical material resistance).
3.  **phi_i (Geometry):** The **Thermal Coverage Factor** of technology `i`.
    *   For **Vapor Chambers**, `phi = coverage_area / area_panel` (Where **coverage_area** is the physical footprint of the Vapor Chamber (VC) cooling module).
    *   For **Graphite/Graphene**, `phi` is a fixed technological coverage constant as less data is publicly available (see table below).
4.  **alpha_i (Physics):** The **Technological Spreading Constant** of technology `i`. This encodes the lateral diffusion speed of the material (Effective k).
    *   **Sum(alpha_i * phi_i):** The cumulative "Spreading Effort" of all active and passive technologies coexisting in the stack.

**Table 1: Technology Calibration (alpha and phi)**

| Technology Class               |  alpha  |      phi      | Physical Rationale                           |
| :----------------------------- | :------ | :------------ | :------------------------------------------- |
| **None (SoC Only)**            | **0.0** |    **0.0**    | Pure baseline radiation from SoC hotspot     |
| **Standard Graphite Sheet**    | **0.6** |    **0.40**   | Standard synthetic sheet covering top half   |
| **Multi-layer Graphite**       | **0.8** |    **0.50**   | Dual-stack or high-density vertical stacking |
| **Synthetic Graphene Film**    | **1.2** |    **0.50**   | Better utilization of SAME footprint         |
| **Professional Vapor Chamber** | **2.7** |   **Dynamic** | Active 2-phase phase-change transport        |

**Table 2: Comparison Matrix (Resulting s_eff scores) with some examples, non exhaustive**

| Cooling Solution              | Glass (Class 3)  | Alloy (Class 2)  | Metal (Class 1)  |
| :---------------------------- | :--------------- | :--------------- | :--------------- |
| **None**                      |      0.05        |       0.25       |       0.60       |
| **Standard Graphite Sheet**   |      0.24        |       0.41       |       0.68       |
| **Multi-layer Graphite**      |      0.35        |       0.50       |       0.73       |
| **Synthetic Graphene**        |      0.46        |       0.59       |       0.78       |
| **Standard VC (4,000 mm²)**   |      0.55        |       0.67       |       0.82       |
| **High-Vol VC (8,000 mm²)**   |      0.77        |       0.85       |       0.92       |
| **Extreme VC (12,000 mm²)**   |      0.87        |       0.93       |       0.96       |
| **Extreme VC + Graphene**     |      0.90        |       0.96       |       0.98       |

*Note: VC phi is calculated assuming a standard 13,500 mm² chassis footprint (phi = coverage_area / 13500).*

**Justification for the Model:**
*   **Diffusion Power (alpha):** We distinguish between technologies because a Vapor Chamber moves heat via high-speed vapor phase-change (alpha=2.7), whereas solid-state spreaders like Graphite or Graphene rely on conductive diffusion (alpha range 0.6 - 1.2).
*   **The Ceiling (s_max):** Glass phones are capped at 0.95 because no matter how good the internal spreader is, the **Vertical Thermal Resistance (Rz)** of the glass skin itself prevents 100% efficient utilization of the external ambient air.

> [!NOTE]
> **The Glass Hotspot:** Why does glass limit cooling? Because glass is a severe thermal insulator, heat travels laterally only very minimally. Natively, it becomes trapped in a tiny hotspot directly over the processor, rendering the rest of the chassis useless. Thus, high-end glass phones mandate massive Vapor Chambers simply to overcome this glass insulation and spread the heat. (Proof: This calculation provides a physical order of magnitude. Based on **Fin Theory**, the Characteristic Spreading Length (Lc) is sqrt((k * t) / h). For standard 0.6mm glass (k=1.1, t=0.0006, h=10.0), Lc is ≈ 0.81 cm. Because the SoC is not a point source but a physical component (package width w ≈ 1.0 cm), the effective radiator area is derived from the **Component Spreader Formula**: Area ≈ (w + 2Lc)² ≈ 6.8 cm². Note: The 2Lc term accounts for bi-lateral expansion—heat spreads outward by Lc from both opposite edges of the SoC along the panel's width and length dimensions. On a standard large flagship footprint (~135 cm²), this converges to the **0.05 (5%)** baseline efficiency used in the matrix).
>
> **The Metal Advantage:** Aluminum structural unibodies conduct heat so rapidly that even without a Vapor Chamber, they natively utilize **~60%** of the back panel as an effective radiator. *(Proof: Aluminum (k=190) yields Lc ≈ 10.7 cm at h=10.0. While this theoretical spreading length implies the physical potential to utilize the entire device footprint, empirical reality for metal-unibody flagships (Coefficient of Thermal Spreading CTS ≈ 0.60) confirms that internal architectural barriers—such as battery isolation and structural cut-outs—cap the native utilization at ~60%).*

> [!TIP]
> **Material Physics - Graphene vs. Graphite:**
> While **Graphite** provides lateral spreading, **Graphene** (used in flagship dual-stack systems) increases the "Isothermal Uniformity". It ensures that the active radiator area has a nearly flat temperature gradient, maximizing heat flux per cm² and reducing "thermal lag" during rapid load transitions.

> [!NOTE]
> **Understanding Vapor Chamber (VC) Tiers:**
> A **Vapor Chamber (VC)** is a planar heat pipe that utilizes a "Phase Change" cooling cycle. Inside a sealed, vacuum-tight copper or stainless steel chamber, a tiny amount of liquid (usually water) evaporates directly over the hot **SoC (System-on-Chip)**. This vapor travels rapidly to cooler areas of the chamber, where it condenses back into liquid, releasing its heat. Capillary action through a porous "wick" structure then pumps the liquid back to the SoC to repeat the cycle.
>
> The effectiveness of a Vapor Chamber is primarily dictated by its internal volume and total surface area (footprint), which determine its maximum heat-carrying capacity and spreading utility:
> - **Standard VC (< 4,000 mm²):** Typical specialized cooling found in mainstream flagships. It provides significantly better spreading than graphite, but its relatively small area means heat is still concentrated in the upper half of the device.
> - **High-Volume VC (4,000–10,000 mm²):** High-end chambers that cover a major portion of the internal layout. These chambers radically reduce thermal resistance by bridging the gap between the SoC and the lower chassis, effectively increasing the active radiator surface.
> - **Extreme/XXL VC (> 10,000 mm²):** Also known as "Full-body" or "3D" Vapor Chambers. These massive units cover essentially the entire internal footprint. They ensure the back panel reaches an almost perfectly Isothermal state with maximum efficiency to expel heat.

###### 2.5 Active Cooling (Integrated Fan)
Built-in fans create a highly efficient internal parallel exhaust path that forcibly ejects thermal wattage. Unlike passive spreaders, which enhance the **surface area** utilized for natural convection, internal fans provide a massive localized boost to the **convective intensity** within a dedicated cooling duct. To model this accurately, we divide the back panel into two distinct convective zones based on the device's physical architecture.

**Parameter Definitions:**
*   **h_fan (Forced Convective Intensity):** The heat transfer coefficient achieved within the cooling duct by the forced airflow. This represents the "intensity" of the active cooling path.
*   **f_fan (Fan Engagement Factor):** The fraction of the total back panel footprint occupied by the internal fan-sink/duct. Based on high-performance gaming phone teardowns, this is standardized at **0.10 (10%)**.
*   **h_passive (Natural Convection Baseline):** The standard baseline for natural convection in ambient air, standardized at **10.0 W/m²K**.
*   **s_eff (Spreading Efficiency):** The fraction of the back panel area utilized for cooling, as derived from internal spreaders (Vapor Chamber/Graphite) in Section 2.4.

**Step-by-Step Physical Proof (Decoupled Area Model):**

1.  **Total Back Dissipation (power_back):**
    The total heat ejected is the sum of the power dissipated by the localized forced-air duct and the remaining spread surface area:
    `power_back = power_forced_convection + power_passive_convection`

2.  **Forced Convection (power_forced_convection):**
    The fan-sink/duct area (f_fan * footprint_area) is cooled at the high-intensity forced convection coefficient (h_fan):
    `power_forced_convection = h_fan * (f_fan * footprint_area) * temperature_rise`

3.  **Remaining Passive Dissipation (power_passive_convection):**
    The rest of the effectively spread area (footprint_area * s_eff) that is NOT covered by the fan-sink is cooled via natural convection (h_passive):
    `power_passive_convection = h_passive * (footprint_area * s_eff - f_fan * footprint_area) * temperature_rise`

4.  **Refactoring for Thermal Resistance (resistance_back):**
    Combining the terms and factoring out common variables (footprint_area and temperature_rise):
    `power_back = footprint_area * temperature_rise * [ h_fan * f_fan + h_passive * (s_eff - f_fan) ]`

By defining an **Effective Convection Coefficient (h_eff)** for the back panel:
`h_eff = h_fan * f_fan + h_passive * (s_eff - f_fan)`
`h_eff = h_fan * 0.10 + 10.0 * (s_eff - 0.10)`

The resulting resistance formula is:
`resistance_back = 1 / (footprint_area * h_eff)`

> [!NOTE]
> **The `s_eff < f_fan` Edge Case (Thermodynamic Reality):**
> Mathematically, the term `(s_eff - f_fan)` could yield a negative value if a device had an internal fan but an extremely poor spreading efficiency (e.g., bare glass with `s_eff = 0.05` and `f_fan = 0.10`). This would imply the fan occupies more area than the heat natively spreads to, creating a "negative" passive area. 
> 
> However, in the real world, this is a non-issue. Exhaustive teardowns of active-cooling smartphones (e.g., **ZTE Nubia RedMagic** series, **Lenovo Legion Phone Duel 2**) prove that mechanical fans are *always* paired with massive Vapor Chambers (often >10,000 mm²) and extensive graphite sheets to bridge the SoC to the duct. Therefore, any phone with a fan will inherently possess an `s_eff` (typically > 0.80) that vastly exceeds the 0.10 fan footprint, ensuring the formula remains physically and mathematically sound without the need for artificial limiters.

**Physics of Forced Convection Scaling (h_fan):**

To ensure high traceability and ease of use, we utilize a simplified semi-empirical model that anchors the cooling intensity boost to a standard high-performance gaming phone reference state.

**Scaling Formula:**
**`h_fan = 10 + 100 * (max_speed_rpm / 20000 * diameter_mm / 12)^0.8`**

which leads to:
**`h_fan = 10 + 100 * (max_speed_rpm * diameter_mm / 240000)^0.8`**

**Justification of Components:**
*   **10 (Natural Baseline):** Represents the standard natural convection baseline (h_passive) for air in ambient conditions, obtained when the fan does not rotate (RPM = 0).
*   **100 (Forced Boost Factor):** The calibrated convective intensity boost provided by the through-flow air channel at the reference state.
*   **Reference State (12 mm / 20,000 RPM):** The boost coefficient is anchored to a high-performance **12 mm** fan (the median size for leading gaming devices) running at a standard **20,000 RPM**.
*   **Velocity Scaling (v^0.8):** Because the actual airflow velocity (v) is directly proportional to the fan blade’s rotational tip speed (v ~ D * RPM), the cooling intensity scales with the 0.8 power of this product. This follows established turbulent flow principles where heat transfer enhancement is non-linearly coupled to air velocity.

*   **Example Case:** A flagship gaming phone with a 12 mm fan running at 20,000 RPM resolves to an effective convective capacity of **110 W/m²K**.

###### 2.6 Thermal Capacitance (C) 
The "Thermal Sponge". `C = Mass(kg) * Specific Heat(J/kg·K)` (Where **Specific Heat** is the material's ability to store thermal energy). Heavier devices buffer intense heat spikes longer before surface temperatures rise.
*   **Standard Bulk Specific Heat:** To simplify and ensure consistency, a standardized value of **850 J/kg·K** is used. *(Rationale: In a Lumped Parameter Model, the entire mass acts as a unified sponge. Because the lithium-ion battery and glass screen constitute the vast majority of the weight in all phones, the volumetric average specific heat converges tightly at ~850. Using this constant prevents minor backend material weight differences from skewing the total heat capacity unphysically).*
*   **Advanced Modifier (Phase Change Materials - PCM):** Devices using internal wax-sleeves (paraffin composites) temporarily increase C during the "melting window," absorbing power spikes without temperature rise. 
    *   **Standardized Thermal Buffer Constant (C_pcm = 25 J/K):** Represents a reference implementation of **~2.5g** of organic paraffin with a **Latent Heat of Fusion** of **200 J/g**, providing a total energy buffer of **500 J** (2.5g * 200 J/g). This energy is mathematically linearized over the full **20K safety window** (from 25°C ambient to 45°C surface) to yield an effective average capacitance boost of **25 J/K** (500 J / 20 K).
    *   *(Note: While paraffin melts over a narrower ~5K window, our specific transient solution for Thermal Impedance (thermal_impedance_k_w(t)) requires a constant Capacitance value (C) to remain mathematically applicable. Linearizing the 500J over the entire 20K rise provides the most accurate 'Effective Average Capacitance' for this LTI (Linear Time-Invariant) approximation.*
    *   **Phase-Change Utilization Factor (subscore_pcm):** Quantifies the thermal contact quality and structural integration of the material.
        *   **subscore = 0.75 (Tier 1: 3D Structural PCM Matrix):** PCM integrated into a 3D conductive lattice (metal honeycomb, graphene foam) for rapid volumetric absorption.
        *   **subscore = 0.50 (Tier 2: 2D Interfacial PCM Layer):** PCM applied as a thin interfacial layer (gel, sheet, or film) to improve contact, lacking a 3D structural matrix.
        *   **subscore = 0.00 (Tier 3: High-Temp PCM):** The PCM is verified but its melting point is above 45°C. It remains solid during the evaluation and provides zero latent benefit.
        *   **subscore = 0.00 (Tier 4: None / Standard TIM):** Standard Thermal Paste used to fill air gaps between the SoC (System-on-Chip) and the heat spreader. It does not change phase at 40°C–45°C and provides zero latent heat capacitance.
    *   **Effective Capacitance Formula:** `thermal_capacitance = (mass * 850) + (subscore_pcm * 25)`
    *   *(Melting Point Constraint: PCM credits are only applicable if the material's melting phase occurs between ambient (25°C) and the safety threshold (45°C). Any melting within this window successfully absorbs the 500J buffer and delays the thermal throttling point. Above 45°C (Tier 3), the material remains solid and provides zero benefit for the safety window).*

> [!IMPORTANT]
> **Neutrality & Differentiation (VC vs. PCM Buffer):** 
> A **Vapor Chamber (VC)** is a heat **transport** mechanism accounted for in Spreading Efficiency (Section 2.4). While it uses phase change (Liquid/Vapor), it does not significantly increase thermal capacitance. A **PCM Buffer** is a heat **storage** mechanism (Solid/Liquid) designed to absorb energy transients. To ensure unbiased scoring, a VC must NEVER be categorized as a PCM Buffer; doing so constitutes double-counting.

###### 2.7 The Multi-Path Transient Solution
The system calculates the **Admissible Thermal Power (power_admissible)**—the maximum continuous wattage allowed to reach the safety threshold (temperature_rise_limit) at the end of the 1200-second evaluation window. 

**Part 1: The Three-Path Parallel Resistance (resistance_total)**
Heat escapes the device through three parallel thermal paths. We calculate the resistance of each path (resistance_path = resistance_conduction + resistance_convection):
1. **Front Path (resistance_front):** Based on Display Area and Glass insulation.
2. **Back Path (resistance_back):** Based on Back Material and Spreading Efficiency.
3. **Frame Path (resistance_frame):** Based on Perimeter area and Frame Conductivity.

**Formula:** `1 / resistance_total = (1 / resistance_front) + (1 / resistance_back) + (1 / resistance_frame)`

**Part 2: Foundational Energy Balance (The Differential Equation)**
`thermal_capacitance * (dT / dt) = power_in - (T - T_amb) / resistance_total`
*Rationale: The rate of heat storage (thermal_capacitance * dT/dt) is the difference between the generated thermal power (power_in) and the heat dissipated into the ambient environment (temperature_rise / resistance_total).*

**Introduction of Thermal Impedance (thermal_impedance):**
The relationship between the temperature rise (temperature_rise) and the input power (power_in) over time (t) is defined by the **Thermal Impedance (thermal_impedance)**. This form assumes a **Step Input Power** (where a constant workload **power_in** is applied instantaneously at **t=0** and sustained for the duration of the evaluation):
`temperature_rise(t) = power_in * thermal_impedance(t)`

**Literal Solution (Transient RC Model):**
`thermal_impedance(t) = resistance_total * (1 - e^(-t / (resistance_total * thermal_capacitance)))`

> [!NOTE]
> **The Thermal Time Constant (time_constant):**
> The product of the system's total resistance and capacitance (`resistance_total * thermal_capacitance`) is known as the **Time Constant (time_constant)**. It represents the time required for the device to reach approximately 63% of its final steady-state temperature rise. A larger time_constant (measured in seconds) indicates higher thermal inertia, meaning the device can "buffer" intense heat spikes for a longer period before thermal throttling must occur.

**Calculating the Admissible Thermal Power (power_admissible):**
`power_admissible = temperature_rise_limit / thermal_impedance(t)`

**Project Parameters:**
- **temperature_rise_limit:** 20°C (The ergonomic safety limit reached at 45°C surface).
- **t (Duration):** 1200 seconds (Standardized 20-minute sustainability window).
- **resistance_total:** Reciprocal of the sum of parallel conductances (K/W).

**Final Calculation:** `power_admissible = 20 / (resistance_total * (1 - e^(-1200 / (resistance_total * (mass * 850 + subscore_pcm * 25)))))`

---

##### 3. Heat Generation Analysis (The SoC "Silicon Engine") 
Peak heat generation is computed by identifying the specific **Peak SoC Thermal Power (power_peak_soc)** of the processor under maximum sustainable synthetic load. 

**Model Rationale:** To maintain absolute neutrality, this model relies on verified **Package Power** measurements—the actual electricity consumed by the silicon during maximum work—rather than manufacturer 'TDP' estimates. By measuring the real wattage drawn from the motherboard (minus system idle), we identify the exact thermal load the chassis must handle. This ensures the score is anchored in physics: the higher the wattage, the more heat the cooling system must dissipate to prevent performance drops.

> [!NOTE]
> **The Efficiency vs. Capacity Paradox:** 
> Readers may notice that modern 3nm chips have higher Peak Power (15–20W) than legacy 10nm chips (4–5W). While modern chips are ~10x more **efficient** (using much less energy for the *same* task), they have nearly 50x the **capacity** (more cores, higher speeds). 
> 
> **Why Efficiency Grows with Node Shrink?** 
> Moving from 10nm to 3nm yields a 2–3x jump in raw electrical efficiency. This is because smaller transistors (FinFET and Gate-All-Around architectures) have much shorter path lengths, reducing the voltage needed to switch and drastically cutting down on wasted "leakage" current. 
> 
> Imagine a modern supercar vs. a 1920s tractor: The supercar is more efficient, but its engine is so much more powerful that it still burns more fuel at top speed. In Table 1, we measure the "Top Speed" (Max Capacity) of each SoC.

**Table 1: Master SoC Peak Power Matrix (Extract)**
*Values represent verified Package Power (Watts) measured under maximum peak synthetic load. For the full exhaustive database of all mobile silicon (2016–2026), refer to the Source of Truth.*

| SoC Model                           | Peak Power (power_peak_soc) [Watts]  | Node  | Foundry |
| :---------------------------------- | :----------------------------------: | :---: | :-----: |
| **Snapdragon 8 Elite**              | **19.5**                             | 3nm   | TSMC    |
| **Snapdragon 8 Gen 1**              | **16.5**                             | 4nm   | Samsung |
| **Dimensity 9400**                  | **15.5**                             | 3nm   | TSMC    |
| **[...]**                           | **[...]**                            | [...] | [...]   |

> [!IMPORTANT]
> **Source of Truth:** The full authoritative lookup table for all smartphone SoCs (2016–2026) is located in [proposed_data_structure.md] under **SOC_PEAK_POWER_MATRIX**.

**Calculated Peak Generation (power_peak_soc):**
`power_peak_soc = Master_Matrix_Value`
*(Note: Use the **power_peak_soc** value from the Master SoC Matrix directly. This is the final wattage measured in laboratory tests, which already encompasses all manufacturing and node characteristics.)*

> [!NOTE]
> **Why Node Multipliers are Omitted:**
> Readers may wonder why the model does not apply an additional "Efficiency Multiplier" based on the process node (e.g., 3nm vs. 4nm). In thermodynamics, a heat sink (the phone chassis) is agnostic to *how* heat is generated; it only responds to the absolute volume of heat (Watts) it must expel. Since **power_peak_soc** is derived from empirical laboratory measurements (real-world Package Power), the node's efficiency — including leakage and voltage characteristics — is already **fully encompassed** in the measured wattage. Applying a secondary multiplier would constitute "double-counting" the node flaw and result in a physically incorrect heat generation value.

---

##### 4. Final Stability Derivation 
Once the exact heat Dissipation limits and the Heat Generation volume are locked in, the thermal stability is calculated and converted to visual gaming stability.

1.  **Define Dynamic System Base Heat (power_base_needs):**
    The chassis must expel 100% of the device's heat. The model calculates the steady-state heat generated by the non-processor components (Display, RAM, logic), which occupies a significant portion of the total cooling budget:
    `power_base_needs = power_static_base + power_display_heat`
    `power_display_heat = display_surface_area * (C_panel * 2.5) * F_refresh_intensive * F_resolution * k_heat_conversion`
    *   **power_static_base (0.40 W):** The "Logic Board Baseline". This consists of Power Management Integrated Circuit (PMIC) conversion efficiency losses (~0.25 Watts - W) — based on a 90% efficiency baseline for modern buck converters under an active system load of ~2.5 Watts (W) — and baseline active logic overhead for memory controllers, sensors, and baseband idle (~0.15 W). Total Baseline Heat: `0.25 W + 0.15 W = 0.40 W`.
    *   **Display Surface Area (display_surface_area, in square centimeters - cm²):** Screen footprint derived from screen diagonal and the standard aspect ratio (R = Height / Width). Formula: `display_surface_area = (diagonal_inch * 2.54)^2 * (R / (R^2 + 1))`. This ensures geometric parity for all modern aspect ratios (19.5:9, 20:9, etc.).
    *   **Panel Efficiency Constant (C_panel, in Watts per square centimeter - W/cm²):** Technology-dependent panel constant representing the base power draw to illuminate 1 square centimeter (cm²) of screen at a standardized reference brightness of 200 nits:
        - **0.0035 W/cm²:** Low-Temperature Polycrystalline Oxide (LTPO) Organic Light-Emitting Diode (OLED) or Tandem OLED panels (highly efficient backplanes).
        - **0.0045 W/cm²:** Standard OLED or Active-Matrix Organic Light-Emitting Diode (AMOLED) panels.
        - **0.0060 W/cm²:** Liquid Crystal Display (LCD) or In-Plane Switching (IPS) panels (requiring continuous, active Light-Emitting Diode (LED) backlights).
    *   **Brightness Scaling Factor (2.5):** Scales the display draw from 200 nits baseline to standard gaming brightness (500 nits).
    *   **Refresh Rate Factor (F_refresh_intensive):** Evaluated at maximum refresh rate (max_hz) in Hertz (Hz) because gaming locks the screen refresh to its peak:
        `F_refresh_intensive = 1.0 + 0.0025 * (max_hz - 60.0)`
        - *Note:* Thermal refresh-rate throttling feedback loops are neglected (assuming a constant lock at the maximum refresh rate - max_hz) to maintain a closed-form, deterministic scoring model and avoid circular iterative dependencies. The Samsung Galaxy S24 Ultra worked case study documented below justifies this choice, proving that performing a feedback iteration on a device with low stability only shifts the final Thermal Dissipation & Stability Index (TDSI) score by 0.14 points. A future version update of the scoring model could introduce a multi-pass iteration loop to provide even greater numerical precision.
    *   **Resolution Factor (F_resolution):** Accounts for rendering and aperture ratio overhead centered around a 2.0 Megapixels (MP) baseline:
        `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0)`
    *   **Thermodynamic Heat Conversion Factor (k_heat_conversion = 0.95):** ~ 95% of screen electrical power becomes internal thermal energy. The rest, about 5% of the electrical energy, is emitted as visible light.

> [!NOTE]
> **Empirical Validation of C_panel and Brightness Scaling (2.5x):**
> 1. **C_panel Baseline Accuracy (at 200 nits):** Proven by real-world display measurements where typical 6.7-inch screens draw approximately 0.38 Watts (W) for Low-Temperature Polycrystalline Oxide (LTPO) Organic Light-Emitting Diode (OLED) panels, 0.49 Watts (W) for standard Low-Temperature Polycrystalline Silicon (LTPS) OLED panels, and 0.65 Watts (W) for Liquid Crystal Display (LCD) panels.
> 2. **Benchmark Brightness (500 nits):** Matches typical screen brightness during sustained 3DMark Wild Life Extreme stress tests in typical testing conditions.
> 3. **Linear Scaling (2.5x):** Grounded in diode physics where luminous intensity scales 1-to-1 with current and power, since voltage remains stable in the 200 to 500 nits active region (2.5x brightness increase from 200 nits baseline to 500 nits gaming brightness).

2.  **Calculate Admissible SoC Budget (power_admissible_soc):**
    `power_admissible_soc = power_admissible - power_base_needs`
    *Rationale: By subtracting the base heat from the total chassis limit (power_admissible), we determine the specific continuous thermal headroom available exclusively for the SoC workload defined in Section 6.10.3.*

3.  **Raw Power Ratio:** 
    `power_ratio = power_admissible_soc / power_peak_soc`
    *(Note: Values greater than 1.0 indicate the device possesses a positive **thermal margin**, meaning its cooling system can dissipate more heat than the SoC generates at peak load).*

4.  **The Physics of Dynamic Power (The Cube Root Law):** 
    The dynamic power consumption of any semiconductor is governed by the equation: `P = C * V^2 * f` (Where P is Power, C is parasitic capacitance, V is Voltage, and f is Frequency).

    **Why P ≈ f^3 in plain language?** 
    At the microscopic level, a transistor is basically a tiny capacitor (a bucket) that must fill up with electrons to switch 'ON', and empty out to switch 'OFF'.
    *   **Frequency (f):** This is how fast we are forcing the bucket to fill and empty. If we double the frequency, we have half the time to fill the bucket.
    *   **Voltage (V):** Voltage is the 'water pressure' pushing the electrons. If we have half the time to fill the bucket, we MUST double the water pressure (Voltage) to force the electrons in fast enough.
    *   **The Result:** Because Voltage (V) must increase proportionally with Frequency (f) to keep the chip stable, any increase in speed hits the power formula twice.
    *   **The Formula:** Power = Capacitance * Voltage^2 * Frequency. 
        - If you double the frequency (f * 2), you must double the voltage (V * 2). 
        - Squaring the doubled voltage gives you * 4.
        - Multiplying that by the doubled frequency gives you * 8.
        - This is mathematically identical to f^3 (2^3 = 8).
    *   Power scales cubically with Frequency. If you want a processor to run twice as fast, it will burn eight times the power.

    By reversing the math: If a smartphone's cooler restricts the processor to a maximum amount of Power (P), the maximum Performance (f, which equals gaming FPS) it can achieve is the **Cube Root** of that power: `P^0.333`.

    `predicted_stability_percentage = 100 * (power_ratio ^ 0.333)` (Clamped 0-100)
    *(Note: Capped at 100%, indicating the device can sustain maximum performance throughout the 1200-second evaluation window without requiring thermal throttling).*

5.  **Final TDSI Score:** 
    The `predicted_stability_percentage` is logarithmically normalized against minimum/maximum thresholds and scaled to a strict **0-10.0** outcome.
    *Formula:* `Score = 10 * (log(predicted_stability_percentage) - log(Thermal_Stability_Min)) / (log(Thermal_Stability_Max) - log(Thermal_Stability_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Thermal_Stability_Max
    *   **Min Score (0.0):** ≤ Thermal_Stability_Min

**Case Study: Samsung Galaxy S24 Ultra**
Below is the physical data demonstrating the physics-based derivation of the S24 Ultra's thermal stability.

| System Variable                                        | Galaxy S24 Ultra         | Physical Interpretation                                           |
| :----------------------------------------------------- | :----------------------- | :---------------------------------------------------------------- |
| **Footprint (Total Area)**                             | 128.2 cm²                | Flagship footprint (6.8" screen).                                 |
| **Chassis Mass (Thermal Inertia)**                     | 0.232 kg                 | High mass to absorb heat spikes.                                  |
| **Back Material (k)**                                  | Glass (~1.1)             | Insulating back face.                                             |
| **Vapor Chamber (VC)**                                 | **High-Volume VC**       | 4,050 mm² active area.                                            |
| **Secondary Spreaders**                                | **Multi-layer Graphite** | Synthetic graphite sheets for motherboard and battery coverage.   |
| **Front Path (resistance_front)**                      | 31.45 K/W                | Total Resistance through the display face (RC Path 1).            |
| **Frame Path (resistance_frame)**                      | 71.22 K/W                | Titanium frame perimeter bottleneck (Path 2).                     |
| **Back Spreading Efficiency (s_eff)**                  | **0.693**                | Derived from 4,050mm² VC + Multi-layer Graphite.                  |
| **Back Path (active_radiator_area)**                   | 0.00888 m²               | Effective radiator footprint (footprint_area * s_eff).            |
| **Back Path (resistance_back)**                        | 11.32 K/W                | Resistance through the rear face (RC Path 3).                     |
| **Total Resistance (resistance_total)**                | **7.45 K/W**             | Defines Chassis ability to expel heat.                            |
| **Heat Dissipation (Chassis, power_admissible):**      | **4.81 Watts**           | The heat the chassis can safely eject at 1200s.                   |
| **System Base Heat (power_base_needs):**               | 1.55 Watts               | The Galaxy's screen and logic board baseline budget.              |
| **Admissible SoC Budget (power_admissible_soc):**      | 4.81 - 1.55 = **3.26 W** | Net wattage available for the CPU/GPU workload.                   |
| **Heat Generation (SoC, power_peak_soc):**             | 14.0 Watts               | Snapdragon 8 Gen 3 peak generation power.                         |
| **power_ratio (power_admissible_soc/power_peak_soc):** | 3.26 / 14.0 = **0.233**  | The system manages ~23.3% of its peak engine demand.              |
| **Bridge (Ratio ^ 0.333) & Prediction:**               | 0.233 ^ 0.333 = **61.5%**| Physical FPS Stability Projection using the Cube Root Law.        |
| **Predicted TDSI Score**                               | **4.69 / 10.0**          | Logarithmic normalization.                                        |
| **3DMark Wild Life Extreme (Stability)**               | **59.0%** [¹]            | Empirical testing (UL Median) is close to the model.              |
| **Benchmark TDSI Score**                               | **4.24 / 10.0**          | Score equivalent of actual test results.                          |

[¹] [UL Benchmarks (3DMark) - Galaxy S24 Ultra Review](https://benchmarks.ul.com/hardware/phone/Samsung+Galaxy+S24+Ultra+review) (Median Wild Life Extreme Stability: 59%).

#### **Step-by-Step Physical Derivation (Galaxy S24 Ultra)**
Below is the transparent "A to Z" derivation of the S24 Ultra's thermal persistence based on standardized 6.10 physical guidelines and publicly available technical specifications.

**Phase A: Geometric Volume Analysis**
- **S1: Device Dimensions (Global):**
  - **height (Y):** 162.3 mm
  - **width (X):** 79.0 mm
  - **thickness (Z):** 8.6 mm
- **S2: Footprint Area (footprint_area):** (height 162.3mm x width 79.0mm) / 1,000,000 = **0.01282 m²** (128.2 cm²).
- **S3: Frame Perimeter (P):** 2 x (height + width) = 2 x (162.3mm + 79.0mm) = 482.6mm -> **0.483 m**.
- **S4: Frame Radiator Area (frame_radiator_area):** (Perimeter 0.483m x thickness 0.0086m) x 0.85 (Chi factor) = **0.00353 m²**.
- **S5: Display Surface Area (display_surface_area):** Using the Diagonal Formula (6.8" at 19.5:9 Aspect Ratio): (6.8 x 2.54)^2 x (2.1667 / (2.1667^2 + 1)) = **113.5 cm²**.

**Phase B: Multi-Path Thermal Resistance (R)**
- **Path 1 (Front):** Conduction through 0.7mm Glass (k=1.1) + Convection (h=10).
  - **Area active derivation:** footprint_area (0.01282) x s_eff (0.25) = **0.00320 m²**.
  - **Resistance (resistance_conduction):** 0.0007 / (1.1 x 0.00320) = **0.20 K/W**.
  - **Resistance (resistance_convection):** 1 / (10.0 x 0.00320) = **31.25 K/W**.
  - **resistance_front:** 0.20 + 31.25 = **31.45 K/W**.
- **Path 2 (Frame):** Conduction through 3.0mm Titanium (k=7.0) + Convection (h=10).
  - **Area active derivation:** frame_radiator_area (0.00353) x s_eff (0.40) = **0.00141 m²**.
  - **Resistance (resistance_conduction):** 0.0030 / (7.0 x 0.00141) = **0.30 K/W**.
  - **Resistance (resistance_convection):** 1 / (10.0 x 0.00141) = **70.92 K/W**.
  - **resistance_frame:** 0.30 + 70.92 = **71.22 K/W**.
- **Path 3 (Back):** Multi-layer Cooling Stack (VC + Graphite) + Convection (h=10).
  - **Cooling Stack Configuration:**
    - **Vapor Chamber:** 4,050 mm² active area providing professional-grade phase-change transport (alpha = 2.7).
    - **Secondary Spreaders:** Multi-layer high-conductivity graphite sheets (alpha = 0.8, phi = 0.50) for secondary lateral diffusion.
  - **s_eff Derivation:** (0.05) + (0.95 - 0.05) x [1 - exp(-(2.7 * (4050 / 12821.7) + 0.8 * 0.5))] = **0.693**.
  - **Area active derivation:** footprint_area (0.01282) x s_eff (0.693) = **0.00888 m²**.
  - **Resistance (resistance_conduction):** 0.0006 / (1.1 x 0.00888) = **0.06 K/W**.
  - **Resistance (resistance_convection):** 1 / (10.0 x 0.00888) = **11.26 K/W**.
  - **resistance_back:** 0.06 + 11.26 = **11.32 K/W**.
- **System Resistance (resistance_total):** (1/resistance_front + 1/resistance_frame + 1/resistance_back)^-1
  - (1/31.45 + 1/71.22 + 1/11.32)^-1 = **7.45 K/W**.

**Phase C: Foundational Energy Balance**
- **Thermal Capacity (thermal_capacitance):** Mass 0.232kg x Standard Specific Heat 850 J/kg-K = **197.2 J/K**.
- **Time Constant (time_constant):** resistance_total 7.45 x thermal_capacitance 197.2 = **1469s**.
- **Dissipation Limit (power_admissible):** Continuous power allowed at t=1200s to reach temperature_rise = 20°C.
  - power_admissible = 20 / (7.45 x (1 - e^(-1200/1469))) = **4.81 Watts**.

**Phase D: Net SoC Budget & Prediction**
- **System Base Heat (power_base_needs):** power_static_base 0.40 W + power_display_heat 1.15 W = **1.55 Watts** (where:
  - `C_panel = 0.0035 W/cm²` — Low-Temperature Polycrystalline Oxide (LTPO) Organic Light-Emitting Diode (OLED) panel constant.
  - `F_refresh_intensive = 1.0 + 0.0025 * (max_hz - 60.0) = 1.0 + 0.0025 * (120 - 60.0) = 1.15` — the S24 Ultra's maximum refresh rate is 120 Hertz (Hz), and gaming locks the panel to this peak rate.
  - `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0) = 1.0 + 0.025 * (4.5 - 2.0) = 1.0625` — the S24 Ultra's Quad High Definition Plus (QHD+) resolution of 3120 × 1440 pixels yields approximately 4.5 Megapixels (MP), centered around the 2.0 MP baseline.
  - `power_display_heat = display_surface_area 113.5 cm² * (C_panel 0.0035 W/cm² * 2.5) * F_refresh_intensive 1.15 * F_resolution 1.0625 * k_heat_conversion 0.95 = 1.15 W`).
- **Admissible SoC Power (power_admissible_soc):** power_admissible 4.81 W - power_base_needs 1.55 W = **3.26 Watts**.
- **Thermodynamic Stability:** Ratio vs Snapdragon 8 Gen 3 (14.0 W Peak SoC Thermal Power, power_peak_soc).
  - power_ratio = Admissible 3.26 / Peak 14.0 = **0.233** (23.3% Watt-Ratio).
  - **Predicted FPS Stability:** 0.233 ^ 0.333 (The Cube Root Law) = **61.5%**.
- **Final TDSI Score:** 10 * (log(61.5) - log(40)) / (log(100) - log(40)) = **4.69 / 10.0**.

- **Thermal Feedback Iteration (Validation of Max-Frequency Approximation):**
  To test whether assuming a constant maximum panel refresh rate of 120 Hertz (Hz) is a valid approximation, we perform a feedback iteration using the first-pass Predicted Frames Per Second (FPS) stability of 61.5%. Under thermal throttling, the screen's actual active refresh rate is assumed to match the sustained game frame rate:
  - **Effective Sustained Refresh Rate:** 120.0 Hz * 61.5% = **73.8 Hz**.
  - **Adjusted Refresh Rate Factor (F_refresh_intensive_iter):** `1.0 + 0.0025 * (73.8 - 60.0) = 1.0345`.
  - **Adjusted Display Power (power_display_heat_iter):** `display_surface_area 113.5 square centimeters (cm²) * (C_panel 0.0035 Watts per square centimeter (W/cm²) * 2.5) * F_refresh_intensive_iter 1.0345 * F_resolution 1.0625 * k_heat_conversion 0.95 = 1.037 W`.
  - **Adjusted System Base Heat (power_base_needs_iter):** `power_static_base 0.40 W + power_display_heat_iter 1.037 W = 1.437 W`.
  - **Adjusted Admissible SoC Power (power_admissible_soc_iter):** `power_admissible 4.81 W - power_base_needs_iter 1.437 W = 3.373 W`.
  - **Adjusted Thermodynamic Stability Ratio (power_ratio_iter):** `power_admissible_soc_iter 3.373 W / power_peak_soc 14.0 W = 0.2409` (24.1% Watt-Ratio).
  - **Iterated Predicted FPS Stability:** `0.2409 ^ 0.333 (The Cube Root Law) = 62.3%` (**62.25%** full precision).
  - **Iterated Final TDSI Score:** `10 * (log(62.25) - log(40)) / (log(100) - log(40)) = **4.83 / 10.0**`.
  
  **Conclusion on Approximation:** 
  The difference between the first-pass score (**4.69 / 10.0**) and the iterated score (**4.83 / 10.0**) is only **0.14 points** on a 10-point scale. Even on a device with a poor Thermal Dissipation & Stability Index (TDSI) score where the frame rate drops significantly, the feedback effect on display power is minimal. This confirms that using the max locked refresh rate (120 Hz) is an acceptable and robust simplification that avoids circular iterative loops in the scoring model.

> [!TIP]
> **Validation of resistance_conduction Negligibility:**
> Comparison between the full model (`resistance_path = resistance_conduction + resistance_convection`) and a simplified version (`resistance_path = resistance_convection`) confirms that conductive resistance has an almost zero impact on the final outcome:
> *   **S24 Ultra Delta:** Removing `resistance_conduction` from the S24 Ultra derivation above results in a stability shift of just **0.06 percentage points** (63.41% Simplified vs 63.35% Full Precision).
> *   **Cross-Archetype Generalization:** This conclusion holds true for other device configurations, including **Aluminum Unibodies**, **Budget Polymers** with insulating frames, and **Gaming Fan Phones** with active cooling.
    *   *Note on Active Cooling:* The slightly higher delta for fan-equipped phones occurs because the active airflow significantly reduces the air-side convective resistance (`resistance_convection`). As this dominant bottleneck is partially removed, the material's internal conductive resistance (`resistance_conduction`) carries a higher relative weight in the total path calculation — yet even in this extreme case, the resulting impact on the final stability score remains negligible.


### 🔹 6.11 System Architecture & Synergy Index (SASI) [⚠️ EXPERIMENTAL / NON-SCORING]
*Description:* This subsection evaluates the performance-enhancing effects of "Vertical Integration"—the technical synergy achieved when the Operating System and System-on-Chip (SoC) are co-designed. This synergy allows a device to potentially outperform competitors with superior raw hardware specs by reducing system overhead and latency.

> [!IMPORTANT]
> **Scoring Status:** This section is for **TECHNICAL DOCUMENTATION ONLY** in Version 5.x. It does not contribute to the Final Score. It is introduced to define the parameters for future scoring recalibrations.

#### SASI Evaluation Parameters
The synergy index is categorized based on the following architectural levels:

1.  **Memory Architecture Class (MAC):**
    *   **Unified Memory (Advanced):** High-speed, low-latency shared memory pool for CPU, GPU, and NPU. Eliminates data copying between discrete buffers (e.g., Apple Silicon UMA).
    *   **Discrete/Pooled (Standard):** Standard segmented memory pools with interconnect overhead.
2.  **OS Kernel Efficiency (OKE):**
    *   **Microkernel (Optimized):** Radical reduction of kernel-space services to minimize background footprint and scheduling jitter (e.g., HarmonyOS Microkernel).
    *   **Monolithic (Standard):** Comprehensive kernel services with standard background resource overhead (e.g., Standard Android/Linux kernel).
3.  **Hardware-Accelerated Software Services (HASS):**
    *   **Deep Integration:** Dedicated silicon blocks (Accelerators) specifically designed for OS-level services like biometric security, real-time translation, or computational photography (e.g., Google Tensor TPU/ISP co-design).
    *   **Software-Emulated:** OS services running on standard general-purpose CPU/GPU cores.
4.  **System Fabric & Interconnect (SFI):**
    *   **Proprietary Fabric:** Custom high-bandwidth interconnects between all SoC components that are specifically tuned to the OS’s interrupt and data flow patterns.

#### Complementary Performance Metrics
To avoid double-scoring with Sections 6.1-6.6, SASI focuses on **System Overhead** and **Inter-Component Latency** rather than raw peak throughput.
*   **Excluded:** Raw Clock Speed (§6.1), Peak TFLOPS (§6.3), Peak MT/s (§6.5).
*   **Included:** Idle Memory Usage, System Inter-Process Communication (IPC) Latency, Component Context-Switching Speed.

#### Industry Context & Literature Baseline
The proposal for SASI is supported by the following industry shifts toward vertical integration:
*   **Apple Silicon UMA (Unified Memory Architecture):** Unlike traditional architectures where CPU and GPU data must be copied across a relatively slow bus, UMA allows all components to access the same high-bandwidth memory pool simultaneously. Literature indicates this "zero-copy" mechanism significantly reduces power consumption and latency during intensive tasks like real-time video processing (Source: *Apple Developer - Unified Memory*).
*   **Huawei HarmonyOS Microkernel:** Transitioning from a monolithic Linux kernel to a microkernel allows for a "Deterministic Latency Engine." By isolating kernel services, the OS can ensure precise task scheduling with microsecond accuracy, effectively reducing "input lag" even on mid-range hardware (Source: *IEEE - HarmonyOS: A Distributed OS for All-Scenario Smart Life*).
*   **Google Tensor Co-Design:** By designing custom silicon (TPU) specifically for the Android Neural Networks API, Google achieves higher throughput for on-device AI models (e.g. Call Screen, Real-time HDR) than generic SoCs with higher raw TOPS (Source: *Google Research - Tensor SoC Architecture*).


## 🟣 7. Connectivity & Sensors

### 🔹 7.1 Cellular Capabilities
*Description:* Network speed and compatibility. Better support means faster downloads and reliable signal in more countries.
*   **Measurement:** Modem specification analysis.
*   **Unit:** Bands / Technology
*   **Significance:** Connectivity speed and global roaming capability.
*   **Battery Model Mapping:** The exact technology string from this table is mapped directly in the battery endurance scoring of **Section 8.1** to determine cellular modem active power consumption (P_cellular).


| Score    | Technology                                   | 
| :------- | :------------------------------------------- | 
| **10.0** | **5G mmWave + Sub-6 (Global band coverage)** | 
| **9.0**  | **5G Sub-6 (Full Global Bands)**             |
| **8.0**  | **5G Sub-6 (Limited/regional bands)**        |
| **6.0**  | **4G LTE-Advanced Pro**                      |
| **4.0**  | **4G LTE (Basic)**                           |
| **2.0**  | **3G fallback only**                         |
| **0.0**  | **2G Only**                                  |

### 🔹 7.2 SIM Capabilities
*Description:* Evaluates the device's support for cellular subscriber identity modules (SIM), prioritizing flexibility and modern standards like eSIM and iSIM. Dual SIM lets you have two numbers (e.g., work/personal) or use a local SIM when traveling.

#### Terminology
*   **SIM (Subscriber Identity Module):** The traditional physical card (Nano-SIM) that authenticates the user on a network.
*   **eSIM (Embedded SIM):** A rewritable chip soldered onto the motherboard. Allows digital profile downloads, instant carrier switching, and multiple stored profiles. Eliminated physical swapping.
*   **iSIM (Integrated SIM):** A newer standard where the SIM capability is integrated directly into the phone's main processor (SoC). It offers the same benefits as eSIM but uses less power and space (`<1mm²`), freeing room for larger batteries or other components. Functionally equivalent to eSIM for the user but represents superior engineering.
*   **Dual Active eSIM:** The ability to have two eSIM lines active simultaneously, without needing a physical card.

*   **Measurement:** Analysis of SIM specifications from manufacturer data.
*   **Unit:** Configuration Tier (0-10)

#### Scoring Table

| Score    | Configuration                                     |
| :------- | :-------------------------------------------------|
| **10.0** | **Dual eSIM / iSIM + Physical Nano-SIM Slot**     |
| **8.0**  | **Single eSIM / iSIM + Physical Nano-SIM Slot**   |
| **6.0**  | **Dual eSIM / iSIM Only (No Physical Slot)**      |
| **4.0**  | **Dual Physical Nano-SIM Slots**                  |
| **0.0**  | **No SIM or Single SIM (Nano, eSIM, or iSIM)**    |

#### Configuration Details

*   **10.0 - Dual eSIM / iSIM + Physical Nano-SIM Slot:** Maximum flexibility. Can run two digital profiles (eSIM/iSIM) simultaneously AND has a physical slot for legacy carriers or travel.
*   **8.0 - Single eSIM / iSIM + Physical Nano-SIM Slot:** Standard flagship configuration. Can use one physical SIM and one digital profile simultaneously.
*   **6.0 - Dual eSIM / iSIM Only (No Physical Slot):** Excellent digital flexibility, but requires carrier eSIM support. No fallback for physical SIM cards.
*   **4.0 - Dual Physical Nano-SIM Slots:** Good for travel/dual lines, but requires physical card swapping. No digital convenience.
*   **0.0 - Single SIM (Nano, eSIM, or iSIM):** Basic connectivity. No second line or travel flexibility.
*   **0.0 - No SIM (Wi-Fi Only):** Not a cellular device. 

> [!NOTE]
> **Why are eSIM and iSIM scored identically?**
> **Avoid Double Scoring:** The benefits of iSIM (integrated directly into the SoC) are strictly related to **Space Savings** (<1mm² vs ~2mm²) and **Power Efficiency**. These physical engineering advantages are already captured and rewarded in **Section 1.4 (Ergonomics) (specifically the thickness sub-metric)** and **Section 8.1 (Battery Endurance)**.
> 
> **Approximation Note:** This is currently an approximation. While **Section 8.1** rewards overall battery life, the theoretical model does not yet strictly quantify the specific µW savings of iSIM vs eSIM, nor do general benchmarks (like GSMArena) typically isolate this specific variable. However, treating them as functionally equivalent in this section prevents double-counting the engineering benefits that don't directly alter the user's *connectivity* options. 

### 🔹 7.3 Wi-Fi Standard
*Description:* Wi-Fi technology. Newer standards (Wi-Fi 7/6E) provide faster, more stable internet, especially in crowded homes.
*   **Measurement:** Supported Wi-Fi protocols.
*   **Unit:** Standard (Generation)
*   **Significance:** Local network speed and congestion management.
*   **Battery Model Mapping:** The exact standard string from this table is mapped directly in the battery endurance scoring of **Section 8.1** to determine Wi-Fi chip active power consumption (P_wifi).


| Score    | Standard     | 
| :------- | :----------- | 
| **10.0** | **Wi-Fi 7**  | 
| **8.0**  | **Wi-Fi 6E** | 
| **7.0**  | **Wi-Fi 6**  | 
| **5.0**  | **Wi-Fi 5**  | 
| **3.0**  | **Wi-Fi 4**  | 
| **0.0**  | **Wi-Fi ≤3** |

> [!NOTE]
> **Understanding the score gaps:** Not all Wi-Fi upgrades are equal leaps, and the scoring reflects this:
>
> *   **Wi-Fi 4 → 5 (+2) and Wi-Fi 5 → 6 (+2):** Both brought significant new architectures. Wi-Fi 6 in particular introduced OFDMA — like switching from a single checkout lane to a supermarket with many lanes open at once — massively improving performance in crowded homes or offices.
> *   **Wi-Fi 6 → 6E (+1):** This is **not a new protocol**. Wi-Fi 6E runs the exact same technology as Wi-Fi 6 (both are 802.11ax), simply extended to an additional frequency band (6GHz) for less congestion. Meaningful, but incremental — hence only a 1-point gap.
> *   **Wi-Fi 6E → 7 (+2):** Wi-Fi 7 is a **brand new protocol** (802.11be) with three fundamental advances: **Multi-Link Operation** (the phone uses 2.4GHz, 5GHz, and 6GHz simultaneously — like having three roads instead of one), **doubled channel width** (320MHz vs 160MHz for faster data bursts), and a new signal encoding that packs ~20% more data per transmission. Real-world speeds roughly double vs. Wi-Fi 6E. This earns its full 2-point gap.

### 🔹 7.4 Bluetooth & Audio Codecs
*Description:* Bluetooth quality. Newer versions offer stability and efficiency, while superior codecs ensure high-fidelity audio.
*   **Measurement:** Supported Bluetooth Version + Highest Supported Codec.
*   **Unit:** Composite Score (0-10)

**Scoring Method: Additive Components**
*Formula:* `Score = Version_Score + Codec_Score` (Max 10.0)

**Part 1: Bluetooth Version Score (Weighted)**
*Reflects technical leaps in power, speed, or architecture.*

| Version      | Score   | Justification for Weighting                                                                     |
| :----------- | :------ | :-----------------------------------------------------------------------------------------------|
| **BT 5.4**   | **5.0** | Latest standard, PAwR (Periodic Advertising with Responses), EAD (Encrypted Advertising Data).  |
| **BT 5.3**   | **4.5** | Connection Subrating (efficiency update).                                                       |
| **BT 5.2**   | **4.0** | **MAJOR LEAP:** LE Audio (Low Energy Audio) foundation (LC3 codec / Auracast broadcast audio).  |
| **BT 5.1**   | **2.5** | Direction Finding (niche usage).                                                                |
| **BT 5.0**   | **2.0** | **MAJOR LEAP:** 2x Speed, 4x Range vs 4.2.                                                      |
| **BT 4.2**   | **1.0** | Legacy Low Energy.                                                                              |
| **< BT 4.0** | **0.0** | Obsolete.                                                                                       |

**Part 2: Codec Capability Score (Tiered)**
*Scored explicitly by the highest tier codec protocol supported. This eliminates mathematical bias against phones lacking numerical bitrate disclosures, as protocols inherently define their bitrate ceilings.*

**Tiered Scoring Table:**
*Identify the highest supported codec and award the corresponding Tier score (Max 5.0).*

| Tier         | Score   | Qualifying Codecs                                     |
| :----------- | :------ | :---------------------------------------------------- |
| **Lossless** | **5.0** | aptX Lossless, LHDC Lossless                          |
| **High-Res** | **4.0** | LDAC, LHDC, aptX HD/Adaptive, SSC, UHQ-BT             |
| **Standard** | **1.5** | AAC, SBC, LC3, aptX Classic, aptX LL (Low Latency)    |

**Common Configuration Reference (overall BT + Codec Score):**

| Score    | Combo Example      | Typical Devices                    |
| :------- | :----------------- | :--------------------------------- |
| **10.0** | **5.4 + Lossless** | Future Flagships, Zenfone 11 Ultra |
| **9.0**  | **5.4 + High-Res** | Galaxy S24/S25 (5.0 + 4.0)         |
| **8.0**  | **5.2 + High-Res** | Older Flagships (4.0 + 4.0)        |
| **6.5**  | **5.4 + Standard** | iPhone 15/16 (5.0 + 1.5)           |
| **3.5**  | **5.0 + Standard** | Older Entry (2.0 + 1.5)            |

### 🔹 7.5 Biometrics
*Description:* Unlocking methods. Secure face/fingerprint unlock is faster and safer than typing a PIN every time.
*   **Measurement:** Hardware check (Sensor type).
*   **Unit:** Technology Type
*   **Significance:** Security and convenience of unlocking.

#### 7.5.1 Technical Definitions & Hierarchy
To ensure objective scoring, we define the hierarchy based on **Security**, **Speed**, and **Usability** (e.g., wet finger performance, darkness).

**1. Face Unlock Technologies:**
*   **3D Face Unlock (Hardware):** Uses dedicated hardware sensors—either **Structured Light** (projecting thousands of invisible infrared dots to map facial depth) or **Time-of-Flight (ToF)** (measuring the time it takes for light to bounce off the face)—to create a secure 3D map. This cannot be fooled by photos or masks and works in total darkness.
*   **2D Face Unlock (Software):** Uses the standard front camera to identify facial features. It is insecure (often fooled by photos), requires good lighting, and is generally not valid for banking apps.

**2. Fingerprint(FP) Sensor Technologies:**
*   **Ultrasonic Fingerprint (Under-Display):** Uses high-frequency sound waves to map the 3D ridges and pores of a fingerprint.
    *   *Why it's Tier 1:* Extremely secure (spoof-resistant), works when screen is off, and works with wet/dirty fingers.
*   **Optical Under-Display Fingerprint:** Uses a camera under the screen to take a 2D photo of the illuminated finger.
    *   *Why it's Tier 2:* Standard modern implementation. Offers clean design integration but struggles with wet fingers and intense sunlight.
*   **Capacitive Fingerprint (Physical):** Uses a dedicated silicon capacitor array (Side/Rear) to map ridge/valley capacitance.
    *   *Why it's Tier 2:* Highly reliable and fast. While it lacks the "invisible" integration of under-display sensors, it is a functional peer to Optical sensors in terms of security and often exceeds them in raw speed.

#### Scoring Criteria
*Score is based on the **Best Available** biometric method on the device.*

| Score    | Technology                               | Justification                                                       |
| :------- | :--------------------------------------- | :------------------------------------------------------------------ |
| **10.0** | **3D Face Unlock + Ultrasonic FP**       | The "Ultimate" combo. Secure 3D face map AND wet-finger-capable FP. |
| **8.0**  | **3D Face Unlock**                       | Secure, effortless unlocking (e.g., Face ID), but no finger option. |
| **8.0**  | **Ultrasonic FP**                        | Best-in-class fingerprint security and usability.                   |
| **5.0**  | **Optical Under-Display FP**             | Modern standard interaction; clean design but wet-finger limitation.|
| **5.0**  | **Capacitive FP**                        | Fast, reliable, and secure. Functional peer to Optical.             |
| **0.0**  | **No Secure Biometrics**                 | PIN/Pattern only. Includes **2D Face Only** devices.                |

> [!NOTE]
> **Why is "2D Face Only" scored as 0.0?**
> A device relying solely on 2D Face Unlock (without a fingerprint sensor) lacks a secure biometric hardware layer. 2D Face is software-based, often spoofable by photos, and usually rejected by banking/payment apps for authentication. Therefore, it is functionally equivalent to having "No Secure Biometrics" for high-security use cases.

### 🔹 7.6 Sensors
*Description:* The breadth of hardware sensors in the phone that enable accurate navigation, motion tracking, environmental awareness, and AR/VR features.
*   **Measurement:** Verified presence in manufacturer specifications or credibility-checked technical reviews.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for navigation accuracy, immersive gaming, health tracking, and photography helpers.

**Scoring Formula:**
`Score = Core_Score + Advanced_Score` (Max 10.0)

#### 7.6.1 Core Sensor Suite (Base Score: Max 5.0)
*Essential sensors for modern smartphone operation.*

**1. Gyroscope (1.5 points)**
*   **Definition:** Measures angular rotational velocity (how fast the device is spinning).
*   **Why it matters:** Critical for precise UI rotation, AR/VR experiences, and camera stabilization. Virtual gyroscopes (software emulation) are laggy and inaccurate.

**2. Magnetometer / Compass (1.0 point)**
*   **Definition:** Detects Earth's magnetic field to determine direction.
*   **Why it matters:** Essential for map navigation orientation. Without it, maps cannot show which way you are facing.

**3. Accelerometer (1.0 point)**
*   **Definition:** Measures linear acceleration and tilt.
*   **Why it matters:** Enables basic step counting and portrait/landscape screen rotation. Found in 99% of phones.

**4. Proximity Sensor (0.75 points)**
*   **Definition:** Detects objects close to the screen using infrared or ultrasonic technology.
*   **Why it matters:** Automatically turns screen off during calls to prevent accidental touches. Virtual versions often fail.

**5. Ambient Light Sensor (0.75 points)**
*   **Definition:** Measures surrounding light intensity.
*   **Why it matters:** Enables auto-brightness adjustment, saving battery and protecting eyes.

#### 7.6.2 Advanced Sensor Capabilities (Bonus Score: Max 5.0)
*Premium sensors that unlock advanced functionality.*

**1. LiDAR / ToF / 3D Depth Sensor (2.0 points)**
*   **Definition:** **LiDAR** (Light Detection and Ranging) or **ToF** (Time-of-Flight) sensors emit light pulses and measure the time it takes to reflect back, creating a 3D depth map.
*   **Why it matters:** Enables instant autofocus in low light, professional-grade portrait mode with accurate depth, and AR applications like room scanning and furniture placement.

**2. Barometer (1.5 points)**
*   **Definition:** Measures atmospheric pressure.
*   **Why it matters:** Provides altitude data for fitness apps (counting floors climbed) and accelerates GPS lock by providing vertical coordinates. Also used for local weather prediction.

**3. Color Spectrum / Flicker Sensor (1.5 points)**
*   **Definition:** 
    *   **Color Spectrum Sensor:** Reads the color temperature of ambient light.
    *   **Flicker Sensor:** Detects light frequency fluctuations from artificial sources (LEDs, fluorescent).
*   **Why it matters:** Enables TrueTone-style display adjustment for natural viewing, accurate camera white balance in mixed lighting, and eliminates banding artifacts in photos/videos shot under artificial light.

> [!NOTE]
> **Public Data Availability:** Core sensors are listed on all major spec sites (GSMArena, PhoneArena). Advanced sensors like Color Spectrum or Flicker are prominently advertised features in flagship devices (e.g., Xiaomi Ultra, iPhone Pro) or listed in detailed review specs. If not explicitly listed, the sensor is presumed absent.

### 🔹 7.7 NFC & Ultra-Wideband (UWB)
*Description:* Evaluates short-range wireless connectivity technologies for contactless payments, data transfer, and precision spatial awareness. Near-Field Communication (NFC) enables tap-to-pay and device pairing, while UWB provides centimeter-level location accuracy for advanced use cases.
*   **Measurement:** Hardware presence verification from manufacturer specifications.
*   **Unit:** Feature Tier (0-10)
*   **Significance:** Determines contactless payment capability, peer-to-peer sharing speed, and precision location tracking.

**Why UWB matters:**
UWB (Ultra-Wideband) uses Time-of-Flight radio pulses to achieve ~10cm positioning accuracy, approximately 100× more precise than Bluetooth LE (Low Energy). This enables:
*   **Precision Finding:** Directional guidance to UWB item trackers (e.g., Apple AirTag, Samsung SmartTag+) with exact distance and bearing
*   **Digital Car Keys:** Secure keyless entry with spatial awareness to prevent relay attacks
*   **Enhanced File Sharing:** Directional AirDrop/Nearby Share (point-to-share)
*   **Indoor Navigation:** Centimeter-accurate positioning where GPS is unavailable

| Score    | Configuration | Technical Capability                                      | Example Models           |
| :------- | :------------ | :-------------------------------------------------------- | :----------------------- |
| **10.0** | **NFC + UWB** | Contactless payments + centimeter-level spatial tracking  | iPhone 15 Pro, S24 Ultra |
| **5.0**  | **NFC Only**  | Contactless payments + basic proximity detection          | Pixel 8, Galaxy A55      |
| **0.0**  | **No NFC**    | No contactless payment capability                         | Budget (region-specific) |

> [!NOTE]
> **Differentiation Analysis:** As of 2024, approximately 94% of smartphones globally include NFC, making it a baseline feature rather than a differentiator. UWB remains exclusive to flagship devices (primarily Apple Pro models, Samsung Ultra/Fold series, and Google Pixel Pro), representing the primary scoring distinction in this category.

### 🔹 7.8 Connectivity & Cross-Device Continuity (CDC) Index
*Description:* Measures the practical, daily-use continuity capabilities that enable a smartphone to function as part of a larger computing ecosystem. Scoring prioritizes high-frequency "seamless" interactions over niche technical features.
*   **Measurement:** Presence of verified, system-level continuity frameworks.
*   **Unit:** Composite Score (0–10)
*   **Significance:** Reduces friction when switching between devices (Phone <-> PC/Tablet) and leverages phone hardware for other systems.

**Scoring Strategy:**
Sum of 5 Key Ecosystem Pillars (2.0 points each). Max Score: 10.0.

#### 1. Native Fast File Transfer (2.0 pts)
*   **Why it matters:** Users repeatedly cite "air-dropping" photos/files as the #1 missing feature when leaving an ecosystem. It solves the frustration of emailing photos to oneself.
*   **Neutral Definition:** A pre-installed system protocol that allows direct, high-speed, peer-to-peer file transfer to nearby devices without requiring internet, cables, or third-party app installation.
*   **Verification (Exact Menu / Feature Name):**
    *   **Apple:** AirDrop
    *   **Android (Universal):** Quick Share
    *   **Huawei:** Huawei Share

#### 2. Cross-Device System Clipboard (2.0 pts)
*   **Why it matters:** A massive productivity multiplier. Allows users to copy a 2FA code, URL, or image on their phone and instantly paste it into a document on their PC/Tablet.
*   **Neutral Definition:** An OS-level service that synchronizes the system clipboard content (text/images) across signed-in devices in near real-time.
*   **Verification (Exact Menu / Feature Name):**
    *   **Apple:** Universal Clipboard (Standard feature, no toggle)
    *   **Samsung:** "Continue apps on other devices" (Settings > Connected devices)
    *   **Motorola:** "Smart Clipboard" (in Smart Connect)
    *   **Honor:** "Shared Clipboard" (in Honor Connect)

#### 3. Task Handoff & Session State (2.0 pts)
*   **Why it matters:** Enables "flow" state. A user can start reading an article or drafting an email on their commute and instantly resume it on their desktop without searching for the tab.
*   **Neutral Definition:** A system framework that broadcasts the current application state (URL, Draft Draft) to nearby devices, offering a "one-click resume" suggestion on the target device.
*   **Verification (Exact Menu / Feature Name):**
    *   **Apple:** Handoff (Settings > General > AirPlay & Handoff)
    *   **Samsung:** "Continue apps on other devices" (Settings > Connected devices)
    *   **Google:** "Recent tabs" (via Chromebook Phone Hub)
    *   **Motorola:** "Cross control" (in Smart Connect)

#### 4. Communication Integration (Calls/SMS) (2.0 pts)
*   **Why it matters:** Allows users to stay focused on their work screen. They can answer phone calls and reply to SMS/OTP messages directly from their Laptop/Tablet without picking up the phone.
*   **Neutral Definition:** Native capability to route cellular phone calls and SMS/RCS messages to a secondary device (Tablet/PC) via local network or cloud relay.
*   **Verification (Exact Menu / Feature Name):**
    *   **Apple:** "Calls on Other Devices" (Settings > Phone) & "Text Message Forwarding" (Settings > Messages)
    *   **Samsung:** "Call & text on other devices" (Settings > Connected devices)
    *   **Google:** "Call casting" (Settings > Google > Devices & sharing > Cross-device services)
    *   **Motorola:** "Cross-device calling" (in Smart Connect)

#### 5. Camera & Accessory Virtualization (2.0 pts)
*   **Why it matters:** Leverages the superior hardware of the phone (Main Camera, Biometrics) to enhance other devices, replacing the need for dedicated peripherals like webcams.
*   **Neutral Definition:** System capability to expose the phone's hardware peripherals (Camera, Microphone, Fingerprint) as virtual input devices for a connected PC or Tablet.
*   **Verification (Exact Menu / Feature Name):**
    *   **Apple:** Continuity Camera (Auto-detected on Mac)
    *   **Android (Universal):** USB Webcam Mode (Android 14+)
    *   **Samsung:** "Camera Sharing" (Settings > Connected devices)
    *   **Motorola:** "Webcam" (in Smart Connect)


### 🔹 7.9 USB Port Speed
*Description:* Wired transfer speed. Fast USB means you can copy 4K videos to a PC in seconds, or connect to a monitor.
*   **Measurement:** Data transfer rate (Gbps).
*   **Unit:** Version / Speed
*   **Significance:** File transfer speed and video output capability.

| Score    | Version / Speed            | Example Models           |
| :------- | :--------------------------| :----------------------- |
| **10.0** | **USB 3.2 Gen 2 (10Gbps)** | S24 Ultra, iPhone 15 Pro |
| **8.0**  | **USB 3.1 / 3.0 (5Gbps)**  | Pixel 8                  |
| **5.0**  | **USB 2.0 (480Mbps)**      | iPhone 14, Galaxy A55    |
| **2.5**  | **Micro-USB**              | Legacy                   |
| **0.0**  | **Proprietary/none**       | Obsolete                 |

## 🟣 8. Battery & Charging

### 🔹 8.1 Battery Endurance Score
*Description:* Evaluates smartphone battery life by prioritizing **real-world performance data** over theoretical specifications via a **Benchmark-First Approach with Physics-Based Predictive Interpolation**.
*   **Measurement:** Standardized battery life tests (or predictive model).
*   **Unit:** Benchmark Score (0.0 to 10.0)
*   **Significance:** Determines how long the phone lasts on a single charge under real-world usage.

The model operates on a hierarchy of data availability:
- **Method A: Canonical Benchmark Validation (Primary Path — §8.1.1):** If real-world benchmark data from the canonical source (GSMArena) is available, it is normalized to determine the final score.
- **Method B: Nearest Neighbor Interpolation (Secondary Path — §8.1.2):** If direct benchmark data is missing, we use a technical predictive model to locate similar "nearest neighbor" devices (devices with similar hardware profiles that *do* have benchmark data) and estimate the target device's performance based on their real-world outcomes.
- **Method C: Technical Predictor Model (Tertiary Path — §8.1.3):** The physical supply/demand model that generates the device's technical profile, serving as the coordinates for finding nearest neighbors in Method B.

---

#### 8.1.1 Method A: Canonical Benchmark Validation (Primary Path)
When real-world battery testing data from GSMArena is available, it is normalized to a 0.0 to 10.0 score.

##### 8.1.1.1 Benchmark Exclusions and Canonical Data Source Justification
To ensure consistency, objectivity, and eliminate statistical noise, the following design decisions have been implemented:

1. **Exclusion of PhoneArena:**
   - *Reason for Removal:* An analysis of database coverage shows that PhoneArena's battery database covers approximately 250 to 300 unique models (focusing strictly on high-profile United States (US) market flagships). This is a strict subset of GSMArena's database, which covers over 1,200+ unique models globally since 2016. Because GSMArena tests all of these flagships in addition to global mid-range and budget models, incorporating a PhoneArena fallback path adds significant mathematical conversion complexity for less than 1% net coverage gain in our database. Therefore, PhoneArena has been removed entirely to prevent statistical alignment noise.
2. **Exclusion of DXOMARK:**
   - *Reason for Removal:* DXOMARK (a commercial technology testing laboratory) publishes a composite battery score. However, this score is heavily weighted toward charging speeds and charging efficiency. Since charging speeds are already fully evaluated in Section 8.2 (Wired Charging) and Section 8.3 (Wireless Charging), including DXOMARK here would double-count charging capabilities and distort the endurance-only metric. Additionally, its database has limited coverage and relies on proprietary testing parameters that are not open or reproducible.
3. **Establishment of GSMArena as the Canonical Source:**
   - *Reason:* GSMArena (a global mobile technology publication) features the most comprehensive, standardized, and publicly available smartphone battery testing database in the world, covering major, minor, and regional brands. This provides a single, clean, and highly reliable target for real-world validation.

##### 8.1.1.2 Unified Active-Equivalent Hours (T_unified)
GSMArena (Global System for Mobile Communications Arena) updated its battery testing protocol from Version 1.0 (v1.0), which reported an "Endurance Rating" (ER) in hours, to Version 2.0 (v2.0), which reports a standardized "Active Use Score" (AUS) in hours.

> [!NOTE]
> **Key Differences between GSMArena v1.0 and v2.0 Protocols:**
> *   **Version 1.0 (v1.0) Endurance Rating (ER):** Simulates how long a device lasts under a light-use daily cycle. It assumes a fixed daily workload of 1 hour of voice calls, 1 hour of web browsing, and 1 hour of local video playback, with the remaining 21 hours spent in idle standby. Consequently, the final rating is heavily driven by idle standby efficiency.
> *   **Version 2.0 (v2.0) Active Use Score (AUS):** Measures continuous active runtime until the battery is fully depleted, representing Screen-On Time (SOT) under active workloads. Standby/idle time is completely excluded. The score is a composite of four active usage pillars: calls over 4G/VoLTE (Voice over Long-Term Evolution) cellular networks, dynamic web browsing (simulating active scrolling/touch interaction), video streaming over Wi-Fi (Wireless Fidelity) via YouTube, and 3D (Three-Dimensional) gaming (testing the Graphics Processing Unit, or GPU, under load).

To reconcile these databases, we use a unified time metric:
- **Case 1: GSMArena Active Use Score (v2.0) is available:**
  `T_unified = GSMArena Active Use Score (v2.0) Hours`
- **Case 2: Only GSMArena Endurance Rating (v1.0) is available:**
  We apply a provisional crosswalk factor to convert the legacy Endurance Rating (ER) to an Active Use Score (AUS) equivalent:
  `T_unified = GSMArena Endurance Rating (v1.0) Hours / C_gsm_conversion`
  - Where `C_gsm_conversion` is a provisional conversion constant set to `8.4` (derived from the median ratio of overlapping bridge devices across generations).

##### 8.1.1.3 Linear Normalization
Battery endurance follows a strictly linear utility curve (a device that lasts 16 hours of active use is exactly twice as valuable to a user as one that lasts 8 hours). Thus, hours are normalized linearly:
- **Formula:**
  `Score = 10 * (T_unified - Battery_GSMArena_Hours_Min) / (Battery_GSMArena_Hours_Max - Battery_GSMArena_Hours_Min)` (Clamped 0.0-10.0)
    *   **Max Score (10.0):** ≥ `Battery_GSMArena_Hours_Max`
    *   **Min Score (0.0):** ≤ `Battery_GSMArena_Hours_Min`

---

#### 8.1.2 Method B: Nearest Neighbor Interpolation (Secondary Path)
When the target device lacks direct benchmark data, we use a technical predictive model to locate the **3 most physically similar reference devices** that *do* have benchmark data, and interpolate the target device's score.

To establish what makes two devices "physically similar," we leverage the core physics-based equations from **Method C: Technical Predictor Model** (detailed in §8.1.3). Under Method C, a device's predicted active battery runtime (`T_predicted`, in hours) is modeled as the ratio of its nominal battery energy capacity (`E_supply`, in Watt-hours - Wh) to its average active power demand (`P_demand`, in Watts - W):

`T_predicted = E_supply / P_demand`

The average active power demand (`P_demand`) is computed by summing the power consumed by the display (`P_display`), processing platform (`P_soc`), and connectivity module (`P_connectivity`), scaled by software efficiency and thermal loss overheads:

`P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead`

We decompose this active power demand into three effective subsystem components:

`P_demand = (P_display * F_thermal_overhead) + (P_soc * F_software_overhead * F_thermal_overhead) + (P_connectivity * F_software_overhead * F_thermal_overhead)`

- **Effective Display Power (`P_display_eff`):** `P_display * F_thermal_overhead`
- **Effective System-on-Chip (SoC) Power (`P_soc_eff`):** `P_soc * F_software_overhead * F_thermal_overhead`
- **Effective Connectivity Power (`P_connectivity_eff`):** `P_connectivity * F_software_overhead * F_thermal_overhead`

Therefore, the total power demand is simply the sum of these three effective subsystem powers:
`P_demand = P_display_eff + P_soc_eff + P_connectivity_eff`

##### 8.1.2.1 The 4-Component Physical Similarity Space
To map devices into a dimensionally homogeneous coordinate system where every dimension is expressed in Watts (W), we combine the three effective power demand differences (`Diff_P_display_eff`, `Diff_P_soc_eff`, and `Diff_P_connectivity_eff`) with a fourth component representing the equivalent battery power difference (`Diff_P_battery_equiv`), which converts the difference in nominal battery energy capacity (`E_supply_target - E_supply_neighbor`) into an equivalent power draw delta.

Projecting devices into this 4-component physical similarity space ensures that similarity is based on real physical operating scales rather than arbitrary normalization. It weights the coordinates naturally 1-to-1 by physical impact and prevents components with large values (such as battery capacity in milliampere-hours, or mAh) from skewing the similarity distance calculation compared to low-numerical-value power metrics.

The 4 physical axes representing the component-level differences in active energy storage and power consumption are:

1. **Equivalent Battery Power Difference (`Diff_P_battery_equiv`, in Watts - W):**
   Converts the difference in nominal battery energy capacity (`E_supply`, in Watt-hours - Wh) between the target device and a candidate neighbor device into an equivalent power draw delta (in Watts - W). This is scaled relative to the target device's specific power-to-energy ratio (which is the inverse of its predicted runtime, `1 / T_predicted`):
   `Diff_P_battery_equiv = (P_demand_target / E_supply_target) * (E_supply_target - E_supply_neighbor)`
   - Where `E_supply_target` is the target device's nominal battery energy capacity in Watt-hours (Wh).
   - `P_demand_target` is the target device's total active power demand in Watts (W).
   - `E_supply_neighbor` is the neighbor device's nominal battery energy capacity in Watt-hours (Wh).

2. **Effective Display Power Difference (`Diff_P_display_eff`, in Watts - W):**
   The difference in display active power consumption scaled by thermal leakage overhead:
   `Diff_P_display_eff = P_display_eff_target - P_display_eff_neighbor`
   - Where `P_display_eff = P_display * F_thermal_overhead`.

3. **Effective System-on-Chip (SoC) Power Difference (`Diff_P_soc_eff`, in Watts - W):**
   The difference in processing platform active power consumption scaled by software and thermal overheads:
   `Diff_P_soc_eff = P_soc_eff_target - P_soc_eff_neighbor`
   - Where `P_soc_eff = P_soc * F_software_overhead * F_thermal_overhead`. Here, System-on-Chip (SoC) represents the integrated circuit that contains all the processing units, such as the Central Processing Unit (CPU) and Graphics Processing Unit (GPU), on a single silicon chip.

4. **Effective Connectivity Power Difference (`Diff_P_connectivity_eff`, in Watts - W):**
   The difference in wireless modem and Wireless Fidelity (Wi-Fi) active power consumption scaled by software and thermal overheads:
   `Diff_P_connectivity_eff = P_connectivity_eff_target - P_connectivity_eff_neighbor`
   - Where `P_connectivity_eff = P_connectivity * F_software_overhead * F_thermal_overhead`.

##### 8.1.2.2 Feature Distance Formula
The similarity between the target device and a candidate neighbor device is computed using the **Euclidean Distance** across the 4 physical components:
- **Formula:**
  `Distance = Sqrt( (Diff_P_battery_equiv)^2 + (Diff_P_display_eff)^2 + (Diff_P_soc_eff)^2 + (Diff_P_connectivity_eff)^2 )`
- We select the **3 distinct neighbor devices** (devices in the database that have canonical benchmark data) with the smallest `Distance` (excluding the target device itself).

##### 8.1.2.3 Interpolation and Correction
1. Calculate the average predicted score of the 3 neighbors (from Method C):
   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
2. Compute the Correction Ratio, which measures how the target device's profile structurally differs from its neighbors:
   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.
3. Compute the average real-world benchmark score of the 3 neighbors (normalized using Method A):
   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
4. Apply the Correction Ratio to calculate the final Interpolated Score:
   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`
- The resulting score is clamped between 0.0 and 10.0.

---

#### 8.1.3 Method C: Technical Predictor Model (Tertiary Path)
Evaluating a smartphone's battery life based solely on its charge capacity in milliampere-hours (mAh) is chemically and physically inaccurate. A phone with a large battery capacity and a high-draw display or an inefficient chipset can deplete its energy reserves much faster than a device with a smaller battery capacity but a highly optimized hardware and software stack.

To resolve this, Method C establishes the physical supply/demand equations for the smartphone. It characterizes a smartphone's battery endurance using the physical relationship between electrical energy storage and average power consumption under a standardized mixed-use workload. It calculates the theoretical active endurance hours (`T_predicted`) and converts them to a predicted score.

##### 8.1.3.1 The Fundamental Equation
The relationship between battery capacity (Supply) and average power consumption (Demand) is defined as:
`T_predicted = E_supply / P_demand`
- **Endurance Hours (T_predicted):** The predicted runtime in hours under active mixed-use conditions.
- **Supply (E_supply, in Watt-hours - Wh):** The total energy capacity of the battery.
- **Demand (P_demand, in Watts - W):** The average electrical power consumed by the device under active mixed-use conditions (web browsing, media streaming, voice calls, user interface interaction, and background synchronization).

##### 8.1.3.2 Supply Modeling (E_supply)
Battery capacity must be evaluated as energy capacity in Watt-hours (Wh) rather than charge capacity in milliampere-hours (mAh) because it accounts for operating voltage differences across single-cell and dual-cell battery configurations.
- **Formula:**
  `E_supply = (mAh * V_nominal) / 1000`
  - Where `mAh` is the battery charge capacity in milliampere-hours (mAh).
  - `V_nominal` is the nominal battery voltage in Volts (V).

**Nominal Voltage Detection Logic:**
To correctly identify `V_nominal`, we apply the following prioritized hierarchy:
1. **Explicit Voltage:** If the database contains a numeric value for `battery_voltage_v`, use that value.
2. **Dual-Cell configuration:** If the text field `battery_cell_configuration` contains "Dual-cell", "Dual cell", "2S", or "dual-cell" (case-insensitive), use **7.70 V** (two 3.85V cells in series).
3. **High-Power Charging Heuristic:** If the maximum wired charging speed is **120 Watts or higher**, use **7.70 V** (ultra-fast charging architectures require dual-cell configurations to halve current and prevent excessive thermal losses).
4. **Default Fallback:** Otherwise, use **3.85 V** (the industry-standard nominal voltage for a single-cell lithium-ion smartphone battery).

##### 8.1.3.3 Demand Modeling (P_demand)
Average power demand is modeled as the sum of hardware-governed display panel draw and software-scaled processing/connectivity active loads, scaled globally by the system's thermal efficiency factor:
`P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead`

*Rationale:* Software efficiency and background bloatware (`F_software_overhead`) affect processor cycle utilization and cellular/Wi-Fi radio sync duty cycles, but they do not physically alter the raw power consumed by the display panel's hardware to emit light. Restricting the software overhead multiplier to `P_soc + P_connectivity` ensures that display panel base power is not artificially scaled by software bloat, maintaining a physically accurate power model. Conversely, `F_thermal_overhead` remains a global multiplier because elevated temperature increases dynamic and static leakage across the entire circuit board and degrades the battery cell's internal discharge efficiency.

###### 8.1.3.3.1 Display Power Demand (P_display)
The display screen power demand is modeled as a function of physical surface area, panel technology, dynamic refresh rate, and resolution:
`P_display = display_surface_area_cm2 * C_panel * F_refresh * F_resolution`

- **Display Surface Area (display_surface_area_cm2):**
  Calculated using the physical screen diagonal and aspect ratio, as defined in Section 6.10:
  `display_surface_area_cm2 = (diagonal_inch * 2.54)^2 * (R / (R^2 + 1))`
  - Where `diagonal_inch` is the screen diagonal in inches, and `R` is the aspect ratio (height divided by width, e.g. 19.5/9 = 2.167).
- **Panel Efficiency Constant (C_panel, in Watts per square centimeter - W/cm2):**
  Represents the base power draw to illuminate 1 square centimeter of screen at a standardized reference brightness of 200 nits:
  - **0.0035 W/cm2:** Low-Temperature Polycrystalline Oxide (LTPO) Organic Light-Emitting Diode (OLED) or Tandem OLED panels (highly efficient backplanes).
  - **0.0045 W/cm2:** Standard OLED or Active-Matrix Organic Light-Emitting Diode (AMOLED) panels.
  - **0.0060 W/cm2:** Liquid Crystal Display (LCD) or In-Plane Switching (IPS) panels (requiring continuous, active Light-Emitting Diode (LED) backlights that cannot be turned off for individual pixels).
- **Refresh Rate Factor (F_refresh):**
  Adjusts power demand based on screen update frequency:
  `effective_hz = adaptive ? (0.65 * min_hz + 0.35 * max_hz) : max_hz`
  `F_refresh = 1.0 + 0.0025 * (effective_hz - 60.0)`
  - *Range of Variation:* Under typical configurations, the effective screen refresh rate in Hertz (Hz) ranges from 10 Hz (highly optimized adaptive screens under static displays) to 144 Hz (high-performance gaming screen rates). This yields a factor range of **0.875 to 1.210** (representing a -12.5% reduction to a +21.0% increase in display base power consumption).
  - *Justification:* Active screen redrawing incurs electrical power overhead in both the panel itself and the display driver integrated circuit (IC). Dynamic refresh rates (e.g. Low-Temperature Polycrystalline Oxide (LTPO) panels dropping to 1 Hertz (Hz) during static content) yield an effective average rate below 60 Hz, reducing power demand (`F_refresh < 1.0`). Conversely, high-refresh-rate gaming or scrolling at 120 Hz or 144 Hz increases dynamic draw.
- **Resolution Factor (F_resolution):**
  Adjusts power demand based on pixel density:
  `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0)`
  - *Range of Variation:* For screen resolutions ranging from a basic High Definition (HD) baseline of 1.0 Megapixel (MP) to extreme 4K Ultra High Definition (UHD) resolutions of 8.3 Megapixels (MP), this factor ranges from **0.975 to 1.1575** (representing a -2.5% reduction to a +15.75% increase in display base power consumption).
  - *Justification & Centering:* The resolution factor is centered around a standard baseline of 2.0 Megapixels (MP), which corresponds to modern 1080p displays (the primary reference at which the panel constant `C_panel` is calibrated). Lower-resolution screens receive a slight efficiency bonus (`F_resolution < 1.0`) due to wider subpixel aperture ratios (less light blocked by wiring). Higher-resolution QHD+ or 4K screens receive a penalty (`F_resolution > 1.0`) because they require higher driving currents to overcome the narrow aperture ratio and incur greater data bus and Graphics Processing Unit (GPU) rendering overhead.

###### 8.1.3.3.2 System-on-Chip (SoC) Power Demand (P_soc)
The System-on-Chip (SoC) power draw represents the processing platform's consumption. We directly anchor our model in the physical logic board parameters defined in Section 6.10:
`P_soc = (power_static_base + coefficient_soc_utilization * power_peak_soc) * F_node * F_cpu * F_gpu`

- **Static Base Power (power_static_base = 0.40 W):**
  The logic board baseline power consumption in Watts (W), representing static leakage currents, Power Management Integrated Circuit (PMIC) voltage conversion efficiency losses, and baseline memory interface active overhead under low-load mixed scenarios (as defined in Section 6.10).
- **SoC Mixed-Use Utilization Factor (coefficient_soc_utilization = 0.0075):**
  A unitless, dimensionless ratio representing the average active duty cycle or utilization fraction (0.75%) of the System-on-Chip (SoC) under standard mixed daily usage.
  - *Justification for the Scaling Factor:* Modern chipsets can draw up to 15 Watts (W) to 20 W under peak synthetic benchmarks, but standard daily activities (like web browsing, checking notifications, and messaging) consist mostly of idle states and very low processing loads. The coefficient `0.0075` models the average active processing workload as a fraction of peak capacity.
  - *Note on Modifier Application (Low-Load Efficiency Scaling):* While peak power (`power_peak_soc`) already includes the raw process node and microarchitectural efficiencies under 100% capacity (which is why multipliers are omitted in Section 6.10 to prevent double-counting), we must apply the efficiency multipliers (`F_node * F_cpu * F_gpu`) under low-load conditions because the efficiency gap between processors is **not scale-independent**. In fact, this gap is significantly wider at low utilization due to low-power operating physics:
    1. **The Voltage Floor Handicap:** Modern flagships on 3nm nodes scale voltage down to approximately 0.6 Volts (V) during light tasks. Legacy nodes are limited to a voltage floor of approximately 0.85 Volts (V) due to leakage instability. Since dynamic power scales with the square of voltage (V^2), legacy chips draw far more energy per cycle at low load than their peak power ratio would suggest.
    2. **Power-Gating & Core Scheduling:** Flagships aggressively power-gate unused cores or Neural Processing Units (NPUs) and schedule light tasks onto high-efficiency cores that complete tasks quickly and sleep (high dynamic "Race-to-Sleep" efficiency). Budget chips lack fine-grained power gating and have lower Instructions Per Cycle (IPC), forcing them to remain in active states longer.
    3. **Capacity Correction:** Without multipliers, the formula `0.0075 * power_peak_soc` would predict that a 19.5 W flagship draws 4x more power at low load than a 4.5 W budget chip, which is physically false. The multipliers act as low-load efficiency correction factors, adjusting the capacity-based term to prevent unfairly penalizing high-capacity, highly optimized processors.
- **Peak SoC Power (power_peak_soc):**
  The peak thermal design power of the chipset in Watts (W) sourced from the master database (referenced in Section 6.10).
- **Process Node Factor (F_node):**
  `F_node = 1.0 + 0.4855 * log(process_nm / 3.0)` where `process_nm` is the chipset's physical process node in nanometers (nm) (e.g., 3, 4, 5, 7, 12, etc.).
  - *Range of Variation:* With the physical process node size (`process_nm`) currently ranging from 3.0 nanometers (nm) (representing cutting-edge Gate-All-Around silicon) to 20.0 nanometers (nm) (representing legacy planar silicon), this factor ranges from **1.000 to 1.400** (representing a 0% baseline to a +40.0% increase in System-on-Chip (SoC) power consumption).
  - *Physical Significance of the 3.0 nm Reference Baseline:*
    The 3.0 nm reference baseline represents the peak of commercial silicon optimization for modern fabrication nodes. The logarithmic scaling natively supports future sub-3nm nodes (such as 2.0 nm or 1.8 nm), where `log(process_nm / 3.0)` becomes negative. In such cases, the formula yields a Process Node Factor (F_node) below 1.000 (representing additional power-saving gains).
  - *Justification for Logarithmic Scaling vs. Inverted Quadratic Scaling:*
    While transistor density (the number of transistors per unit area of silicon) scales quadratically relative to the linear dimension of the feature size (transistor density is proportional to 1 / s^2, where s is the process node size in nanometers (nm)), using an inverted quadratic scaling (linear scaling of density) to evaluate System-on-Chip (SoC) energy efficiency is physically inaccurate. The logarithmic scaling is utilized instead due to two core factors:
    1. **Dennard Scaling Limits and Geometric Scaling Physics:** In classical Dennard scaling, power density remained constant as transistors shrank because operating voltage scaled down proportionally. Below the 90nm threshold, Dennard scaling broke down due to leakage currents and physical voltage floors, forcing operating voltage to hit a physical floor (approximately 0.6 Volts (V) to 0.7 V for modern 3nm chips, compared to 0.75 V to 0.85 V for 7nm chips). Consequently, subsequent full-node transitions yield a constant percentage power savings (typically 20% to 30% savings per transition step) rather than scaling quadratically with transistor density.
       - **Physical Rationale for Logarithmic Scaling:**
         - Semiconductor gate sizes scale down geometrically (each full node transition multiplies the gate length in nanometers by approximately 0.7 to double transistor density). 
         - If each transition step yields a constant percentage of power savings, the total power efficiency scales geometrically with the number of steps.
         - Because both the node sizes and the efficiency gains scale geometrically, their relationship is naturally logarithmic. Expressing the Process Node Factor (F_node) as a logarithmic function of the gate length (process_nm) is therefore the mathematically correct way to represent constant percentage efficiency gains per full-node transition.
    2. **Low-Load Power Penalty Distribution:** Splicing the physical process node size directly into the System-on-Chip (SoC) Process Node Factor (F_node) determines the low-load power penalty. If we use an inverted quadratic scaling, mature nodes are severely over-penalized. For instance, with a 3nm baseline node and a 20nm legacy node:
       * Under inverted quadratic scaling, a cutting-edge 3nm node has `F_node = 1.000` (0% penalty), a mid-tier 7nm node has `F_node = 1.334` (+33.4% penalty), and a legacy 20nm planar node has `F_node = 1.400` (+40.0% penalty). This suggests that a 7nm chipset is only 6.6% more power-efficient under light daily workloads than a legacy 20nm planar chipset. This is physically incorrect: the 7nm node is vastly more efficient, reducing dynamic power and static leakage by a factor of 4x to 5x under low-load conditions.
       * Under logarithmic scaling, a cutting-edge 3nm node has `F_node = 1.000` (0% penalty), a mid-tier 7nm node has `F_node = 1.179` (+17.9% penalty), and a legacy 20nm planar node has `F_node = 1.400` (+40.0% penalty). This places the 7nm node near the physical midpoint of the efficiency curve between 20nm planar and 3nm Gate-All-Around (GAA) silicon, which is physically consistent with real-world low-power operating physics.
  - *Exclusion of Foundry-Based Process Node Bonuses:* Sourcing process node efficiency purely from the physical transistor gate length in nanometers (nm) on a logarithmic scale removes subjective foundry-based weightings (such as favoring Taiwan Semiconductor Manufacturing Company (TSMC) over Samsung or Intel) and data availability issues. This keeps the model strictly objective, neutral, and verifiable, avoiding speculative adjustments based on the manufacturing foundry.
    - To evaluate this exclusion, we analyze the impact of these parameters using simple orders of magnitude:
      1. **Real Impact of the Process Node Parameter:** The physical process node size in nanometers (nm) has a significant, mathematically verifiable impact on the final battery score. As already mentioned above, the Process Node Factor (F_node) introduces up to a **40%** variation in System-on-Chip (SoC) power demand (P_soc). Since the SoC itself represents **40% to 50%** of the device's total average power demand (P_demand), the entire process node parameter accounts for a **16% to 20%** shift in total power consumption. This translates to a shift in the predicted active endurance hours (T_predicted) of up to **~15%** (representing an intermediate value between a `1 - 1/1.20 = 16.7%` decrease and a `1 - 1/1.16 = 13.8%` decrease).
      2. **Negligible Impact of Foundry Variations:** The fabrication foundry (and its subtle differences in cell libraries or layout) has a much smaller impact, representing at most **10%** of the node's total efficiency influence.
      3. **Cascaded Impact:** Cascading this 10% foundry-specific variation through the model yields a final impact on predicted active endurance hours (T_predicted) of roughly **~1.5%** (10% of the ~15% node impact).
    - Consequently, while the physical process node size itself is a critical parameter with a substantial impact (~15% runtime shift) and is fully modeled, incorporating subjective foundry-specific adjustments adds significant database maintenance overhead for a minor shift (~1.5% runtime shift) that is generally lost in model rounding.
- **CPU Architecture Factor (F_cpu):**
  `F_cpu = 1.0 + 0.04 * (10 - CPU_AES_Score)`
  - *Range of Variation:* With the CPU Architecture Efficiency Score (CPU_AES_Score) ranging from a minimum of 0.0 (representing legacy core designs) to a theoretical maximum of 10.0 (representing cutting-edge high-efficiency core designs), this factor ranges from **1.400 to 1.000** (representing a +40.0% increase to a 0% baseline in System-on-Chip (SoC) power consumption).
  - *CPU Architecture Efficiency Score (CPU_AES_Score):* The CPU Architecture Efficiency Score represents the average structural efficiency of the CPU cores. It is the core-weighted average of the core-level architectural scores:
    `CPU_AES_Score = Sum(Core_Score_i * Core_Count_i) / Total_Core_Count`
    - Where `Core_Score_i` is the performance score of core architecture `i`, sourced directly from the **CPU Score** column of the Section 6.1.0 CPU Core Architecture Reference Table.
    - `Core_Count_i` is the number of cores of that specific architecture.
    - `Total_Core_Count` is the total number of CPU cores in the processor.
    - *Justification for Omission of Performance Scaling Factors (f, Alpha, Gamma):* Unlike Section 6.1 and 6.2 which calculate peak computational performance under full load, the low-load battery model omits clock frequency (`f`), frequency soft-saturation (`gamma`), and intra-cluster parallel scaling (`alpha`):
      1. **Frequency & Gamma Omission:** Dynamic energy per task is independent of frequency due to the "Race-to-Sleep" paradigm (running a task at double the frequency finishes it in half the time, canceling out frequency: `Energy = Power * Time = (C * V^2 * f) * (Instructions / (IPC * f)) = Instructions * C * V^2 / IPC`). Furthermore, low-load tasks run in the linear low-frequency regime, far below the voltage wall where soft-saturation (`gamma`) occurs.
      2. **Alpha (Parallel Scaling) Omission:** Mixed-use workloads are lightly threaded, running on only one or two active cores while the rest of the clusters are power-gated. Thus, cache contention and thread synchronization overheads modeled by `alpha` are physically negligible.
      3. **Soundness of Core-Weighted Average:** Although efficiency cores run background tasks most of the time, performance cores draw much higher dynamic power when active. The total energy consumed is a balanced function of both clusters, making the core-weighted average a physically sound proxy for the system's aggregate microarchitectural efficiency.
  - *Technical Justification for CPU Core Score as an Efficiency Proxy:* Integrating a separate efficiency column is redundant. The standard IPC-based **CPU Score** serves as an excellent proxy for low-load energy efficiency due to three microprocessor principles:
    1. **The "Race-to-Sleep" Paradigm:** Smartphone daily usage is characterized by short, bursty tasks. A processor with higher IPC completes these tasks in fewer clock cycles, returning the processor core to deep, low-power sleep states (C-states) faster, minimizing the duration of active electrical current draw.
    2. **Dynamic Voltage and Frequency Scaling (DVFS) Optimization (Cubic Scaling Control):** Dynamic power consumption in silicon is modeled as `P_dynamic = C * V^2 * f` (where `C` is capacitance, `V` is supply voltage, and `f` is frequency).
       * **The Voltage-Frequency Dependency:** To prevent logic timing failures, the supply voltage `V` must scale up roughly linearly with target clock frequency `f`. Substituting `V proportional to f` into the power equation reveals that active power scales cubically with frequency (`P_dynamic proportional to f^3`).
       * **IPC-Frequency Trade-off:** Computational performance (execution time) is dictated by `Time = Instructions / (IPC * f)`. A high Instructions Per Cycle (IPC) core can deliver the same processing throughput (same execution time for a given task) at a lower clock frequency (`f`).
       * **Power Reduction:** By running at a lower frequency, the processor allows the Power Management Integrated Circuit (PMIC) to supply a significantly lower operating voltage (`V`). Because of the cubic relationship, running at a lower frequency and voltage dramatically reduces active power consumption compared to a low-IPC core that must run at high frequencies and peak voltages to match the same performance.
    3. **Reduced Architectural Execution Overhead:** Advanced branch predictors and wider instruction execution windows in high-IPC cores prevent wasted operations on mispredicted paths and minimize execution pipeline stalls, meaning fewer physical gate-switching actions per task (lower Joules per instruction).
  - *Concrete Worked Example: Snapdragon 8 Gen 3 (Configured with 8 total cores):*
    - **Cluster 1 (Best):** 1 x Cortex-X4
      - Core Score (from §6.1.0 Table) = `7.95`
      - Core Count = `1`
      - Weighted Score = `7.95 * 1 = 7.95`
    - **Cluster 2 (Second Best):** 5 x Cortex-A720
      - Core Score (from §6.1.0 Table) = `5.00`
      - Core Count = `5`
      - Weighted Score = `5.00 * 5 = 25.00`
    - **Cluster 3 (Third Best):** 2 x Cortex-A520
      - Core Score (from §6.1.0 Table) = `1.00`
      - Core Count = `2`
      - Weighted Score = `1.00 * 2 = 2.00`
    - **Calculations:**
      - Sum of Weighted Scores = `7.95 + 25.00 + 2.00 = 34.95`
      - Total CPU Cores = `1 + 5 + 2 = 8`
      - `CPU_AES_Score = 34.95 / 8 = 4.36875`
- **GPU Architecture Factor (F_gpu):**
  `F_gpu = 1.0 + 0.01 * (10 - GPU_Efficiency_Score)`
  - *Range of Variation:* With the GPU Efficiency Score ranging from 0.0 (representing obsolete graphic engines) to 10.0 (representing cutting-edge efficient graphic engines), this factor ranges from **1.100 to 1.000** (representing a +10.0% increase to a 0% baseline in System-on-Chip (SoC) power consumption).
  - *GPU Efficiency Score:* Sourced from the architectural performance-per-watt efficiency score in Section 6.3.0.
  - *Justification for Separate Performance and Efficiency Scores (CPU vs. GPU):* Unlike the CPU model where the same IPC-based score serves as both the performance and efficiency proxy, the GPU model requires a separate, dedicated efficiency score:
    1. **Throughput-Oriented (SIMD) Architecture:** CPU performance is latency-oriented (IPC-driven), where higher IPC translates directly to lower frequency/voltage under a given thread load. GPU performance, however, is throughput-oriented and scaled simply by adding massive arrays of physical Arithmetic Logic Unit (ALU) shader cores (e.g., Immortalis-G925 MC12 vs. Mali-G715 MC7).
    2. **Low-Load Decoupling:** Under daily mixed-use (rendering 2D UI frames, basic scrolling), the GPU operates at near-idle states where it power-gates almost all of its execution units, running only a minimal section of the silicon at low frequencies. A massive, high-performance GPU with a high rasterization score is not necessarily more efficient under low loads; its efficiency is governed entirely by dynamic leakage control, low-voltage limits, and clock-grid gating efficiency.
    3. **Microarchitectural Variance:** Peak graphics performance is decoupled from average daily rendering efficiency, independent of the process node. To prevent double-counting, the Process Node Factor (F_node) already isolates silicon-level transistor leakage and voltage scaling limits of the fabrication node. The GPU Architecture Factor (F_gpu) isolates GPU-specific microarchitectural efficiency (such as global clock-tree distribution grids, execution unit power-gating granularity, and graphics memory bus overhead). For example, comparing two Graphics Processing Units (GPUs) manufactured on the **same 4-nanometer (nm) process node**:
       * A massive flagship GPU contains a very large Arithmetic Logic Unit (ALU) array that achieves elite peak performance. However, due to its physical size, its clock-tree distribution network, wide memory bus interfaces, and global routing logic draw substantial static and dynamic power even under low-load daily rendering tasks (User Interface (UI) scrolling or 2D display frames) where most shader cores are power-gated.
       * A compact entry-level GPU on the same node has a much smaller ALU array and lower peak performance. However, its small physical footprint, narrow memory bus, and simple clock grid ensure that its active overhead and leakage remain extremely low during light rendering tasks.
       * If peak graphics performance were used as the sole proxy for daily rendering efficiency, the model would incorrectly predict that the massive flagship GPU is more efficient under light workloads than the compact entry-level GPU on the same node. Using a separate GPU Efficiency Score ensures microarchitectural layout overhead is modeled independently of the fabrication node.

###### 8.1.3.3.3 Connectivity Power Demand (P_connectivity)
Models the average power drawn by cellular modems and Wi-Fi chips during active synchronization and data transfer:
`P_connectivity = P_cellular + P_wifi`

- **Cellular Modem Active Power (P_cellular):**
  The cellular modem power draw is determined by matching the cellular specification of the device directly to the corresponding technology row in **Section 7.1 (Cellular Capabilities)** without ambiguity. The predicted score of Section 7.1 must be used for mapping (rather than the final score) to avoid any potential scoring bias that could be introduced by dynamic booster adjustments:
  - **0.18 W:** `5G mmWave + Sub-6 (Global band coverage)` — 5th Generation (5G) networks supporting both high-frequency millimeter-Wave (mmWave) and Sub-6 Gigahertz (GHz) bands, requiring additional front-end hardware power.
  - **0.14 W:** `5G Sub-6 (Full Global Bands)` or `5G Sub-6 (Limited/regional bands)` — standard 5G networks operating on Sub-6 GHz frequencies.
  - **0.09 W:** `4G LTE-Advanced Pro` or `4G LTE (Basic)` — 4th Generation (4G) Long-Term Evolution (LTE) modems.
  - **0.05 W:** `3G fallback only` or `2G Only` — legacy 3rd Generation (3G) or 2nd Generation (2G) modems.
- **Wi-Fi Active Power (P_wifi):**
  The Wi-Fi chip power draw is determined by matching the Wi-Fi specification of the device directly to the corresponding standard row in **Section 7.3 (Wi-Fi Standard)** without ambiguity. The predicted score of Section 7.3 must be used for mapping (rather than the final score) to avoid any potential scoring bias that could be introduced by dynamic booster adjustments:
  - **0.05 W:** `Wi-Fi 7` — Wi-Fi 7 (802.11be) standard utilizing wide 320 Megahertz (MHz) channels and Multi-Link Operation (MLO).
  - **0.04 W:** `Wi-Fi 6E` or `Wi-Fi 6` — Wi-Fi 6 or 6E (802.11ax) standards utilizing 160 MHz channels.
  - **0.03 W:** `Wi-Fi 5`, `Wi-Fi 4`, or `Wi-Fi <=3` — Wi-Fi 5 (802.11ac), Wi-Fi 4 (802.11n), or older legacy Wi-Fi standards.

###### 8.1.3.3.4 Software Inefficiency Modifier (F_software_overhead)
Operating system (OS) execution efficiency and background application loads act as multipliers on hardware power demand:
`F_software_overhead = 1.0 + 0.10 * (10 - OS_Gen_Score)/10 + 0.10 * (10 - SCC_Score)/10`

- *Range of Variation:* Under typical configurations, this modifier ranges from **1.000** (optimal baseline: current Operating System (OS) version with zero third-party preinstalled bloatware, where OS_Gen_Score = 10.0 and SCC_Score = 10.0) to **1.200** (worst case: obsolete OS version with heavily bloated backgrounds, where OS_Gen_Score = 0.0 and SCC_Score = 0.0). This represents a 0% to +20.0% increase multiplier on overall power demand.

- **OS Generation Score (OS_Gen_Score):**
  Modern operating systems (OS) implement aggressive background process freezing and kernel scheduler optimizations that minimize idle wakeups. To ensure absolute precision and programmatic traceability, this score is fetched directly from the **OS Generation Score** column of the canonical [Operating System Version Reference](references/os_version_reference.md) file. This centralized lookup eliminates the parsing ambiguity of textual version ranges and integrates support for custom mobile operating systems.

  **Justification for Granular Year-by-Year Scoring:**
  To accurately reflect software power management evolution, the scoring system implements a granular, year-by-year rating. Every annual release of Android and iOS introduces incremental updates in background limits, wake-lock control, and process freezing. Because operating system (OS) power management optimizations have matured, these improvements follow an asymptotic curve: early transitions (e.g., introducing strict background limits in 2017–2018) yielded massive efficiency gains and larger score differences (e.g., from 0.0 to 2.5, then 3.5), whereas recent annual updates (e.g., 2023 to 2026+) deliver diminishing returns with smaller score adjustments (e.g., 8.5 to 9.0, 9.5, and 10.0) as efficiency gains flatten out. The exact score for each canonical OS version is documented in the [Operating System Version Reference](references/os_version_reference.md) lookup tables.

- **System Cleanliness & Control Score (SCC_Score):**
  Sourced from Section 5.2. The predicted score of Section 5.2 must be used (rather than the final score) to avoid any potential scoring bias that could be introduced by dynamic booster adjustments. A lower score indicates significant pre-installed manufacturer bloatware and background services, which prevent the processor from entering deep low-power sleep states.

###### 8.1.3.3.5 Thermal Efficiency Modifier (F_thermal_overhead)
Heat increases electrical current leakage in silicon transistors and raises the internal resistance of battery cells, degrading efficiency:
`F_thermal_overhead = 1.0 + 0.03 * (10 - TDSI_Score)/10`

- *Range of Variation:* Based on the Thermal Dissipation & Stability Index (TDSI) score, this modifier ranges from **1.000** (optimal baseline: elite thermal design, where TDSI_Score = 10.0) to **1.030** (worst case: poor heat-dissipation plastic body, where TDSI_Score = 0.0). This represents a 0% to +3.0% thermal leakage multiplier on overall power demand.
- **Thermal Dissipation & Stability Index Score (TDSI_Score):**
  Sourced from Section 6.10. The final score of Section 6.10 must be used (rather than the predicted score) because Section 6.10 is based primarily on empirical Benchmarks (such as 3DMark stability results) for its final value, which represents a verified performance ceiling and must have priority over prediction calculations.
  - *Justification:* The TDSI (Thermal Dissipation & Stability Index) score in Section 6.10 is derived from a sustained, 20-minute synthetic Graphics Processing Unit (GPU) stress test (such as 3DMark Wild Life Extreme) that saturates the device's hardware at maximum thermal limits. In contrast, Section 8.1 battery endurance modeling reflects moderate, low-load mixed daily activities (such as web browsing, video streaming, and messaging) where the system rarely reaches these peak thermal states. Because daily mixed-use tasks generate very little internal thermal stress compared to intensive 20-minute gaming workloads, the maximum possible heat-induced leakage penalty in this model is restricted to a moderate **3%** (applied when the TDSI score is 0.0, representing poor chassis heat dissipation). This calibration prevents extreme peak thermal behavior from disproportionately distorting or penalizing the device's standard, daily battery runtime calculations.

> [!NOTE]
> **Coherent Rationale for Baseline Calibration of Section 8.1 Modifiers:**
> Readers may observe a distinction in how the scaling factors and modifiers in Section 8.1 are anchored relative to their baseline configurations:
> 1. **Zero-Penalty / Efficiency Modifiers (F_node, F_cpu, F_gpu, F_software_overhead, F_thermal_overhead):**
>    These factors are anchored at a multiplier of **1.0** for the absolute best-case/ideal configurations (3.0 nanometers (nm) process node, and maximum scores of 10.0 for Central Processing Unit (CPU) microarchitecture, Graphics Processing Unit (GPU) efficiency, Operating System (OS) version, system cleanliness, and thermal chassis design). 
>    *Rationale:* These modifiers represent *power overhead penalties* that scale a base consumption. Under physical modeling, it is mathematically cleaner and more stable to define the base consumption (P_soc_base, representing System-on-Chip (SoC) base power) using an *ideal, zero-overhead state*. Any real-world inefficiencies (mature fabrication nodes, older core architectures, background software bloat, heat-induced leakage) act as one-directional scaling penalties (F >= 1.0) that inflate the base power. Anchoring these at the ideal limit prevents "moving-target" dependencies and ensures all deviations represent a mathematically positive overhead.
> 2. **Physical Parameter Scaling Factors (F_refresh, F_resolution):**
>    These factors are centered around a standard baseline configuration (60 Hertz (Hz) refresh rate and 2.0 Megapixels (MP) display resolution), where the multiplier equals **1.0**.
>    *Rationale for 60 Hz and 2.0 MP Baseline:* Unlike efficiency penalties, refresh rate and display resolution are direct, physical hardware specifications. 
>    - **60 Hz Alignment:** The panel constant C_panel (e.g., 0.0035 Watts per square centimeter (W/cm²) for Low-Temperature Polycrystalline Oxide (LTPO) Organic Light-Emitting Diode (OLED) panels) is calibrated to align with empirical display power measurements, which are standardly conducted at a reference refresh rate of 60 Hz in laboratory testing. Anchoring F_refresh at 1.0 at 60 Hz is therefore necessary to align base display power calculations with this empirical test data. Anchoring it at the best-case limit (such as 1 Hz) would require scaling C_panel to a non-standard state that cannot be verified from standard manufacturer specification sheets.
>    - **2.0 MP Alignment:** The 2.0 MP baseline corresponds to standard Full High Definition (FHD) resolution (1920 x 1080 pixels = ~2.07 MP), which has served as the global industry-standard reference resolution for mobile display driver Integrated Circuits (ICs) and panel power calibration for over a decade. It also acts as the physical median resolution across the mobile database (ranging from ~0.9 MP budget screens to ~4.5 MP premium screens), making it a stable baseline for scaling.
>
> **Model Refinement & Validation Studies:**
> In future updates of the model, statistical studies can be performed on the collected device database to compare the predictions of the Technical Predictor Model (Method C) with the empirical testing outcomes of the Canonical Benchmark Validation (Method A). These comparison studies will enable regression analyses and parameter tuning, allowing developers to systematically adjust the model's physical parameters (such as the scaling coefficients, baseline constants, and modifier weights) to match real-world battery endurance profiles with even greater precision.

##### 8.1.3.4 Predicted Endurance Hours and Score Calculation
Once both the battery energy supply (`E_supply`) and total power demand (`P_demand`) are computed under the physical model, the active endurance hours (`T_predicted`) and the corresponding predicted score are determined.

###### 8.1.3.4.1 Endurance Hours (T_predicted)
The predicted active runtime of the device in hours is calculated using the fundamental physical relationship:
`T_predicted = E_supply / P_demand`
- **Supply (E_supply):** Total stored energy in Watt-hours (Wh).
- **Demand (P_demand):** Average electrical power consumption in Watts (W).

###### 8.1.3.4.2 Predicted Score Normalization
To convert the physical active endurance hours (`T_predicted`) to the standardized 0.0 to 10.0 score, the value is normalized linearly relative to the database bounds defined in `scoring_constants.md` specifically for this physical modeling methodology.

`Predicted_Score = 10 * (T_predicted - Battery_Predictor_Hours_Min) / (Battery_Predictor_Hours_Max - Battery_Predictor_Hours_Min)` (Clamped 0.0-10.0)
- **Max Score (10.0):** Achieved when `T_predicted` >= `Battery_Predictor_Hours_Max` (18.0 hours).
- **Min Score (0.0):** Achieved when `T_predicted` <= `Battery_Predictor_Hours_Min` (5.0 hours).

- **Justification for Linear Normalization (Why not Logarithmic?):**
  Battery life utility scales strictly linearly for the user. Unlike human sensory perceptions (such as screen brightness or performance responsiveness, which follow logarithmic curves because the human brain perceives stimulus changes on a logarithmic scale), battery runtime represents a direct physical limit. A smartphone that provides 12 hours of active runtime delivers exactly twice the utility of a device providing 6 hours (allowing the user to operate the device for twice as long without searching for a power outlet). Therefore, a linear score scale is the only representation that preserves this proportional relationship of real-world endurance.

##### 8.1.3.5 Comparison of Battery Endurance (Section 8.1) and Thermal Dissipation (Section 6.10) Models

To ensure complete clarity and physical consistency across the scoring framework, the table below maps the Level 1 components and Level 2 parameters (including System-on-Chip (SoC) and display variables) used in both the average Battery Endurance model and the sustained Thermal Dissipation model, along with their engineering justifications:

| Level 1 Component      | Level 2 Parameter / Variable | In §8.1? | In §6.10? | Engineering Justification                                                                                                      |
| :--------------------- | :--------------------------- | :------: | :-------: | :----------------------------------------------------------------------------------------------------------------------------- |
| **SoC Power**          | `power_static_base` (0.40 W) |  **Yes** |  **Yes**  | Shared baseline logic board draw (including Power Management Integrated Circuit (PMIC) losses and RAM idle draw).              |
|                        | `power_peak_soc` (Watts)     |  **Yes** |  **Yes**  | Sourced from peak package power. Full in Section 6.10 (gaming peak); dampened by 0.0075 factor in Section 8.1 (mixed use).     |
|                        | `F_node` / `F_cpu` / `F_gpu` |  **Yes** |  **No**   | Section 8.1 uses low-load scaling multipliers. Omitted in Section 6.10 to prevent double-counting (see `power_peak_soc` line). |
| **Display Power**      | `display_surface_area` (cm²) |  **Yes** |  **Yes**  | Standard physical display footprint.                                                                                           |
|                        | `C_panel` (W/cm²)            |  **Yes** |  **Yes**  | Panel constant. Calibrated for 200 nits in Section 8.1 and scaled by 2.5 for 500 nits High Brightness Mode in Section 6.10.    |
|                        | `F_refresh` (Refresh Factor) |  **Yes** |  **Yes**  | Adaptive dynamic rate in Section 8.1. Fixed to peak max_hz rate in Section 6.10 (gaming locks to peak refresh).                |
|                        | `F_resolution` (Resolution)  |  **Yes** |  **Yes**  | Accounts for dynamic pixel density driving currents and Graphics Processing Unit (GPU) bus rendering overhead in both.         |
|                        | `k_heat_conversion` (0.95)   |  **No**  |  **Yes**  | Trapped heat factor in Section 6.10. Omitted in Section 8.1 because it tracks total energy, not just heat dissipation.         |
| **Connectivity Power** | `P_cellular` / `P_wifi`      |  **Yes** |  **No**   | Critical for daily use in Section 8.1. Offline in Section 6.10 (Airplane Mode; static leak covered in 0.40 Watt base).         |
| **Software Overhead**  | `F_software_overhead`        |  **Yes** |  **No**   | OS/bloatware factors in Section 8.1. Negligible in Section 6.10 under 100% sustained peak saturation.                          |
| **Thermal Overhead**   | `F_thermal_overhead`         |  **Yes** |  **No**   | Battery efficiency loss under heat in Section 8.1. Irrelevant for Section 6.10.                                                |

> [!NOTE]
> **Omission of Active Connectivity Power in the Thermal Model (Section 6.10):**
> While active connectivity draw (`P_connectivity = P_cellular + P_wifi`) ranges from ~ `0.08 W` to `0.23 W` during active daily data transfers, it is omitted from the sustained thermal model in Section 6.10 because:
> 1. **Offline Benchmark Execution:** Standardized graphics stress tests (such as 3DMark Wild Life Extreme) are executed locally with devices placed in Airplane Mode to eliminate testing variance. Dynamic data transfer power is therefore zero.
> 2. **Baseline Leakage Encapsulation:** The static, low-power leakage of inactive cellular and Wi-Fi silicon is already fully accounted for in the system's baseline logic board heat (`power_static_base = 0.40 W`), specifically within the baseline logic and baseband idle segment (~0.15 W).
> 3. **Thermal Scale Comparison:** Even under active online gaming conditions, the maximum dynamic modem draw (~0.23 W) represents less than 5% of the total thermal budget (e.g. 4.81 W for the Galaxy S24 Ultra), making it negligible compared to display heat (~1.18 W) and active SoC heat (~3.23 W).

> [!NOTE]
> **Omission of Software Overhead in the Thermal Model (Section 6.10):**
> Software efficiency and system cleanliness factors (`F_software_overhead`) are omitted from the sustained thermal dissipation model because:
> 1. **Hardware Power Envelope Limits:** During sustained peak benchmarks (such as 3DMark or GFXBench), the Central Processing Unit (CPU) and Graphics Processing Unit (GPU) are fully saturated at 100% utilization. The Power Management Integrated Circuit (PMIC) and system firmware enforce strict hardware power caps to prevent electrical overcurrent. Background software cannot cause the processor to draw more power than this physical maximum.
> 2. **Process Starvation and Scheduler Prioritization:** Operating System (OS) kernel schedulers prioritize the active foreground benchmark application over background services. Low-priority background bloatware is starved of execution cycles, meaning it does not contribute dynamic thermal load during the test.
> 3. **Bypassing of Power-Saving Sleep States:** Annual Operating System (OS) optimization upgrades (such as background process freezing, wake-lock pooling, and core parking) are designed to keep the processor in deep, low-power sleep states during idle periods. Because a sustained thermal benchmark forces the processor to remain continuously active in peak power states, these software optimization mechanisms are completely bypassed.

##### 8.1.3.6 Model Validation Worked Examples

###### 8.1.3.6.1 Ultra-Flagship Device
- **Specifications:**
  - **Chipset:** Snapdragon 8 Elite (Peak Package Power = `19.5 W`, TSMC 3nm Node, CPU_AES_Score = `7.50`, GPU_Efficiency_Score = `10.0`)
  - **Battery:** 5000 mAh at 3.85V (`E_supply = 19.25 Wh`)
  - **Display:** 115.0 cm² display area, LTPO OLED panel (`C_panel = 0.0035 W/cm²`), 90 Hz adaptive browsing (`effective_hz = 90 Hz`), QHD+ resolution (`megapixels_mp = 4.5`)
  - **Connectivity:** 5G Sub-6 modem (`P_cellular = 0.14 W`) + Wi-Fi 7 (`P_wifi = 0.05 W`)
  - **Modifiers:** OS_Gen_Score = `10.0`, SCC_Score = `10.0` (yields F_software_overhead = `1.00`), TDSI_Score = `10.0` (yields F_thermal_overhead = `1.00`)
- **Calculations:**
  - **System-on-Chip (SoC) Draw (P_soc):**
    - `P_soc_base = power_static_base + coefficient_soc_utilization * power_peak_soc = 0.40 + 0.0075 * 19.5 = 0.5463 W`
    - `F_node = 1.0 + 0.4855 * log(process_nm / 3.0) = 1.0 + 0.4855 * log(3.0 / 3.0) = 1.00`
    - `F_cpu = 1.0 + 0.04 * (10.0 - CPU_AES_Score) = 1.0 + 0.04 * (10.0 - 7.50) = 1.10`
    - `F_gpu = 1.0 + 0.01 * (10.0 - GPU_Efficiency_Score) = 1.0 + 0.01 * (10.0 - 10.0) = 1.00`
    - `P_soc = P_soc_base * F_node * F_cpu * F_gpu = 0.5463 * 1.00 * 1.10 * 1.00 = 0.6009 W`
  - **Display Draw (P_display):**
    - `F_refresh = 1.0 + 0.0025 * (effective_hz - 60.0) = 1.0 + 0.0025 * (90 - 60.0) = 1.075`
    - `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0) = 1.0 + 0.025 * (4.5 - 2.0) = 1.0625`
    - `P_display = display_surface_area_cm2 * C_panel * F_refresh * F_resolution = 115.0 * 0.0035 * 1.075 * 1.0625 = 0.4597 W`
  - **Connectivity Draw (P_connectivity):**
    - `P_connectivity = P_cellular + P_wifi = 0.14 + 0.05 = 0.1900 W`
  - **Total Demand (P_demand):**
    - `F_software_overhead = 1.0 + 0.10 * (10.0 - OS_Gen_Score)/10.0 + 0.10 * (10.0 - SCC_Score)/10.0 = 1.0 + 0.10 * (10.0 - 10.0)/10.0 + 0.10 * (10.0 - 10.0)/10.0 = 1.0000`
    - `F_thermal_overhead = 1.0 + 0.03 * (10.0 - TDSI_Score)/10.0 = 1.0 + 0.03 * (10.0 - 10.0)/10.0 = 1.0000`
    - `P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead = (0.4597 + (0.6009 + 0.1900) * 1.0000) * 1.0000 = 1.2506 W`
  - **Theoretical Endurance (T_predicted):**
    - `T_predicted = E_supply / P_demand = 19.25 Wh / 1.2506 W = 15.39 Hours`
  - **Predicted Score:**
    - `Predicted_Score = 10.0 * (T_predicted - Battery_Predictor_Hours_Min) / (Battery_Predictor_Hours_Max - Battery_Predictor_Hours_Min) = 10.0 * (15.39 - 5.0) / (18.0 - 5.0) = 7.99` (Out of 10.0)

###### 8.1.3.6.2 Budget Device
- **Specifications:**
  - **Chipset:** MediaTek Helio G99 (Peak Package Power = `4.5 W`, TSMC 6nm Node, CPU_AES_Score = `2.92`, GPU_Efficiency_Score = `5.0`)
  - **Battery:** 5000 mAh at 3.85V (`E_supply = 19.25 Wh`)
  - **Display:** 108.0 cm² display area, standard Liquid Crystal Display (LCD) panel (`C_panel = 0.0060 W/cm²`), 120 Hz static refresh rate (`effective_hz = 120 Hz`), Full High Definition Plus (FHD+) resolution (`megapixels_mp = 2.5`)
  - **Connectivity:** 4G Long-Term Evolution (LTE) Advanced (`P_cellular = 0.09 W`) + Wi-Fi 5 (`P_wifi = 0.03 W`)
  - **Modifiers:** OS_Gen_Score = `8.0` (Modern standard), SCC_Score = `4.0` (Significant background bloatware draw), TDSI_Score = `4.0` (Plastic build, basic chassis cooling)
- **Calculations:**
  - **SoC Draw (P_soc):**
    - `P_soc_base = power_static_base + coefficient_soc_utilization * power_peak_soc = 0.40 + 0.0075 * 4.5 = 0.4338 W`
    - `F_node = 1.0 + 0.4855 * log(process_nm / 3.0) = 1.0 + 0.4855 * log(6.0 / 3.0) = 1.1462`
    - `F_cpu = 1.0 + 0.04 * (10.0 - CPU_AES_Score) = 1.0 + 0.04 * (10.0 - 2.92) = 1.2832`
    - `F_gpu = 1.0 + 0.01 * (10.0 - GPU_Efficiency_Score) = 1.0 + 0.01 * (10.0 - 5.0) = 1.0500`
    - `P_soc = P_soc_base * F_node * F_cpu * F_gpu = 0.4338 * 1.1462 * 1.2832 * 1.0500 = 0.6700 W`
  - **Display Draw (P_display):**
    - `F_refresh = 1.0 + 0.0025 * (effective_hz - 60.0) = 1.0 + 0.0025 * (120 - 60.0) = 1.150`
    - `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0) = 1.0 + 0.025 * (2.5 - 2.0) = 1.0125`
    - `P_display = display_surface_area_cm2 * C_panel * F_refresh * F_resolution = 108.0 * 0.0060 * 1.150 * 1.0125 = 0.7545 W`
  - **Connectivity Draw (P_connectivity):**
    - `P_connectivity = P_cellular + P_wifi = 0.09 + 0.03 = 0.1200 W`
  - **Total Demand (P_demand):**
    - `F_software_overhead = 1.0 + 0.10 * (10.0 - OS_Gen_Score)/10.0 + 0.10 * (10.0 - SCC_Score)/10.0 = 1.0 + 0.10 * (10.0 - 8.0)/10.0 + 0.10 * (10.0 - 4.0)/10.0 = 1.0800`
    - `F_thermal_overhead = 1.0 + 0.03 * (10.0 - TDSI_Score)/10.0 = 1.0 + 0.03 * (10.0 - 4.0)/10.0 = 1.0180`
    - `P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead = (0.7545 + (0.6700 + 0.1200) * 1.0800) * 1.0180 = (0.7545 + 0.8532) * 1.0180 = 1.6366 W`
  - **Theoretical Endurance (T_predicted):**
    - `T_predicted = E_supply / P_demand = 19.25 Wh / 1.6366 W = 11.76 Hours`
  - **Predicted Score:**
    - `Predicted_Score = 10.0 * (T_predicted - Battery_Predictor_Hours_Min) / (Battery_Predictor_Hours_Max - Battery_Predictor_Hours_Min) = 10.0 * (11.76 - 5.0) / (18.0 - 5.0) = 5.20` (Out of 10.0)


### 🔹 8.2 Wired Charging Speed
*Description:* Charging speed with a cable. Higher wattage means you spend less time tethered to a wall outlet.
*   **Measurement:** Peak power input via wired connection.
*   **Unit:** Watts (W)
*   **Significance:** Reduces downtime when battery is low.
*Formula:* `Score = 10 * ((1/Battery_Wired_Charging_W_Min) - (1/Watts)) / ((1/Battery_Wired_Charging_W_Min) - (1/Battery_Wired_Charging_W_Max))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Battery_Wired_Charging_W_Max
*   **Min Score (0.0):** ≤ Battery_Wired_Charging_W_Min
> [!NOTE]
> **Why Inverse Proportional?** The actual charging time (T) rests precisely on an inverse hyperbola with wattage (W): T is proportional to C / W. Upgrading from 15W to 30W cuts charge time in half (saving ~45 minutes). Upgrading from 100W to 120W saves less than 2 minutes. Scoring the wattage via an exact Inverse formula perfectly plots the true user benefit: raw **Time Saved** waiting at the wall outlet.

### 🔹 8.3 Wireless Charging Speed
*Description:* Charging speed without cables. Convenient for topping up battery by simply placing the phone on a pad.
*   **Measurement:** Peak power input via wireless coil.
*   **Unit:** Watts (W)
*   **Significance:** Convenience and ease of topping up.
*Formula:* `Score = 10 * ((1/Battery_Wireless_Charging_W_Min) - (1/Watts)) / ((1/Battery_Wireless_Charging_W_Min) - (1/Battery_Wireless_Charging_W_Max))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Battery_Wireless_Charging_W_Max
*   **Min Score (0.0):** ≤ Battery_Wireless_Charging_W_Min
> [!NOTE]
> **Why Inverse Proportional?** Just like wired charging, the time it takes to charge wirelessly follows an inverse hyperbolic curve where the charging time (T) is proportional to 1 / W. Scoring the wattage inversely perfectly models the raw minutes of charging time saved, recognizing that jumping from 5W to 15W is a transformative time-saver, while jumping from 50W to 60W is nearly negligible.

### 🔹 8.4 Wired Reverse Charging
*Description:* Ability to use the phone as a power bank to charge other devices via a USB-C cable.
*   **Measurement:** Peak power output via USB-C port.
*   **Unit:** Watts (W)
*   **Significance:** Useful for sharing power with other phones or charging larger accessories.
*Formula:* `Score = 10 * (Watts / Battery_Reverse_Wired_W_Max)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_Reverse_Wired_W_Max
    *   **Min Score (0.0):** 0W (None)
> [!NOTE]
> **Why Linear?** Similar to wireless reverse, the output range is small (4.5W to ~10W). Linear scaling provides a fair and intuitive distribution of scores based on raw power output.

### 🔹 8.5 Wireless Reverse Charging
*Description:* Ability to charge other devices (like earbuds or watches) wirelessly by placing them on the back of the phone.
*   **Measurement:** Peak power output via wireless coil.
*   **Unit:** Watts (W)
*   **Significance:** Convenient for emergency top-ups of accessories on the go.
*Formula:* `Score = 10 * (Watts / Battery_Reverse_Wireless_W_Max)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_Reverse_Wireless_W_Max
    *   **Min Score (0.0):** 0W (None)
> [!NOTE]
> **Why Linear?** The range of reverse wireless charging is narrow (typically 4.5W to 10W). A linear scale accurately reflects that 10W is roughly twice as fast/useful as 4.5W for small accessory batteries.

### 🔹 8.6 Charger Adequacy (In-Box Performance Match)
*Description:* What comes in the package. A high-speed charger included saves you money and ensures you get the fastest charging speeds right away.
*   **Measurement:** Ratio of Included Charger Wattage to Maximum Supported Wired Charging Wattage.
*   **Unit:** Efficiency Ratio (0.0 - 1.0)
*   **Significance:** Determines if the user gets the device's full performance out of the box without extra purchases.
*Formula:* `Score = 10 * (Included_Watts / Max_Wired_Watts)` (Clamped 0-10)
    *   **Max Score (10.0):** Included Charger ≥ Max Device Speed (Ratio ≥ 1.0)
    *   **Min Score (0.0):** No Charger (0W)
> [!NOTE]
> **Why Ratio?** A "good" unboxing experience means not needing to buy accessories. If a phone supports 120W but comes with a 60W charger, the user is missing out on half the advertised performance, hence a lower score. If a 20W phone comes with a 20W charger, the experience is complete (10/10).


## 🟣 9. Financial & Economic Value

### 🔹 9.1 Price
*Description:* The current market price in USD. Lower prices mean better accessibility for more people.
*   **Measurement:** Manufacturer's Suggested Retail Price (MSRP) at launch or current average market price.
*   **Unit:** USD ($)
*   **Significance:** Primary barrier to entry and value determinant.
*Formula:* `Score = 10 - 10 * (log(Price) - log(Price_USD_Min)) / (log(Price_USD_Max) - log(Price_USD_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ Price_USD_Min
*   **Min Score (0.0):** ≥ Price_USD_Max
> [!NOTE]
> **Why Logarithmic?** Price sensitivity is relative. A $50 increase on a $150 phone is a massive 33% hike, whereas a $50 increase on a $1000 phone is a negligible 5%. The logarithmic scale reflects this relative impact on affordability.

### 🔹 9.2 Manufacturer Warranty Commitment
*Description:* The manufacturer's baseline global warranty period. This measures the manufacturer's confidence in their hardware quality, independent of regional legal requirements (e.g., EU consumer protection laws).
*   **Measurement:** Shortest manufacturer-provided warranty period applied globally.
*   **Unit:** Months
*   **Significance:** Reflects manufacturer confidence in build quality and long-term reliability.

IMPORTANT: The score is based on the **Limited Manufacturer Warranty** (the shortest period offered globally, typically 12 months). This measures the manufacturer's confidence in the hardware. A phone sold with a 12-month warranty in the US and a 24-month warranty in the EU will score based on the 12-month warranty, as the EU's 24-month period is a legal requirement, not a manufacturer commitment.

| Score    | Manufacturer Warranty Period  | Example Models                                                   |
| :------- | :---------------------------- | :--------------------------------------------------------------- |
| **10.0** |   **≥ 60 Months (5 Years)**   | Fairphone 5/6, Teracube (Often requires registration)            |
| **8.5**  |   **48 Months (4 Years)**     | Rugged/Enterprise models (e.g., Samsung Tactical).               |
| **7.0**  |   **36 Months (3 Years)**     | Newer EU baseline (Spain/Portugal) or Nokia X-series.            |
| **5.0**  |   **24 Months (2 Years)**     | EU Standard                                                      |
| **3.0**  |   **12 Months (1 Year)**      | US Standard. The bare minimum for Apple/Samsung/Google globally. |
| **0.0**  |   **0 Months**                | Grey Market / Used                                               |


### 🔹 9.3 Repairability
*Description:* How easy it is to fix. High scores mean you (or a shop) can easily replace a battery or screen, extending the phone's life.
*   **Measurement:** Official iFixit teardown score (0-10) and/or EU Repairability Index (0-5).
*   **Unit:** Composite Repairability Score (0-10)
*   **Significance:** Determines serviceability and long-term ownership viability.

**Scoring Logic:**
The final score is the average of the iFixit Score (0-10) and the converted EU Repairability Index (0-10).
*   **EU Conversion:** `EU_Converted_Score = EU_Index_Value * 2`
*   If both are available: `Score = (iFixit_Score + EU_Converted_Score) / 2`
*   If only one is available: `Score = Available_Score`
*   If neither is available: `Score = N/A` (Not Scored)

**Confidence Score:**
*   **Unknown:** Only one source available (iFixit OR EU).
*   **High:** Both sources available, difference ≤ 1.0 point.
*   **Medium:** Both sources available, difference ≤ 2.5 points.
*   **Low:** Both sources available, difference > 2.5 points.

*   **Max Score (10.0):** iFixit 10 / EU Index 5.0
*   **Min Score (0.0):** iFixit 0 / EU Index 0.0

## 🟣 10. Miscellaneous

### 🔹 10.1 Stylus Hardware & System Support (SHSS)
*Description:* Measures whether the phone supports active stylus input at the hardware and system level, including digitizer presence and latency class.
*   **Measurement:** Digitizer specifications, stylus protocol support (e.g., USI 2.0, MPP 2.0), manufacturer documentation.
*   **Unit:** Stylus Capability Index (0–10)
*   **Significance:** Determines whether precision input is natively supported or only simulated.

| Score    | Stylus Support Level                                                   | Example Models                          |
| :------- | :--------------------------------------------------------------------- | :-------------------------------------- |
| **10.0** | **Integrated active stylus + dedicated digitizer + Bluetooth features**| S24 Ultra                               |
| **8.0**  | **Integrated active stylus + dedicated digitizer**                     | Moto G Stylus                           |
| **6.0**  | **External active stylus support + dedicated digitizer**               | Z Fold 5, Xiaomi Mix Fold               |
| **3.0**  | **Universal Touchscreen Compatibility (Finger/Passive Stylus)**        | **Baseline for ALL modern smartphones** |
| **0.0**  | **No Touchscreen / Resistive Screen**                                  | Feature Phones / Legacy                 |

> [!NOTE]
> **Technical Definitions:**
> - **Dedicated Digitizer:** A specialized hardware layer under the screen (e.g., Wacom EMR) required for any "Active" stylus functions like pressure sensitivity and palm rejection. **An active stylus cannot function with pressure/tilt features without a digitizer.**
> - **Bluetooth Features:** Beyond writing, the stylus acts as a wireless remote control (e.g., camera shutter, media control, "Air Actions"). This requires an internal battery/capacitor in the stylus and a BLE radio.
> - **Integrated Active Stylus:** Physically built into the phone chassis (silo) for storage and charging.
> - **External Active Stylus Support:** The screen has the required digitizer, but the pen is sold separately or stored in a localized case (not inside the phone body).
> - **Universal Compatibility (Passive):** This is **NOT** a specific feature but rather the absence of a digitizer. It means the phone works with cheap "rubber tip" styluses that simply simulate a finger. Since all modern smartphones use capacitive screens, they all achieve this 3.0 baseline.


# 🟣 11. Reviews & Performance Boosters
*Description:* Adjustments based on real-world expert reviews. Technical specs don't always tell the whole story; reviews validate actual performance.
*   **Measurement:** Expert review consensus.
*   **Unit:** Multiplier (Booster)
*   **Significance:** Validates theoretical performance against real-world experience.
*   **Booster > 1.0:** Increases score (e.g., 1.05 = +5%). Used when a device outperforms its specs (e.g., great software optimization).
*   **Booster < 1.0:** Reduces score (e.g., 0.90 = -10%). Used when a device underperforms (e.g., overheating, bugs).

**Booster Methodology**
Boosters are applied strictly at the **subsection** level. This ensures that a review's specific findings impact only the relevant technical metric rather than the entire category.

### 11.A Core Principles
*   **Unaccounted Feature Requirement:** A booster is ONLY justified if it captures a characteristic or performance factor that is either entirely missing from the standard scoring system (Sections 1–10) or is significantly under-represented by the theoretical metrics.
*   **Real-World Test Exclusion:** Boosters are **FORBIDDEN** for subsections that are already scored using real-world benchmarks or tests. Since these scores already reflect actual performance, applying a booster would double-count the benefit.
    *   *Excluded Subsections:* **3.1** (SoC Performance), **3.2** (CPU Efficiency), **5.1** (Battery Capacity).
*   **No Overlap:** The justification MUST NOT overlap with any existing subsection evaluations. For example, if a camera's HDR capability is already scored in Subsection 4.16, "HDR performance" cannot be used as a justification for a booster on that same subsection or any other subsection.
*   **Complete Assessment:** Before applying a booster, verify that the feature is not already scored in another section (e.g., Video Codecs vs. ISP tuning). Double-counting features is strictly prohibited.
*   **Booster Clamping Rule:** The application of one or more boosters can never result in a `Final Score` higher than **10.0** or lower than **0.0**. If the mathematical calculation (`Predicted Score * Multiplier`) exceeds these boundaries, the result must be clamped to the 0–10 range. This ensures that expert adjustments remain within the same normalized scale as the standard technical metrics.

### 11.B Justification Logic
A valid booster requires a clear logical chain linking a hidden technical feature to an observed result.
Each booster section must provide the following elements:
1)  **Source Link:** The link of the review that must be publicly accesible 
2)  **Impacted Subsection:** The subsection number impacted by the booster value, for example 4.16
3)  **Booster:** The value of the booster, for example 1.05
4)  **Justification:**
    a)   **Unaccounted Feature (Cause):** The specific technical mechanism, hardware component, or software algorithm that is responsible for the anomaly. This is the "Why". IMPORTANT: The extract must be detailed and exhaustive enough to be understood by itself, without further explanation.
    b)   **Unaccounted Reason (Gap):** The explicit explanation of *why* this feature is not captured by the standard scoring rules of Sections 1-10.
         *   **Non-Technical Clarity Requirement:** This explanation MUST be understandable to a non-technical reader without prior background knowledge. If a highly technical mechanism (e.g., "pixel binning", "LTPO backplanes") is the root cause, you MUST append a plain-English `Context:` explanation detailing exactly what the mechanism is and why it represents an anomaly. Do not assume industry knowledge.
         *   **Context Source Support:** If a `Context:` explanation is provided, an additional supporting **URL LINKING** to a credible technical deep-dive MUST be provided inline within the same string to prove this context. See example 11.1 below.
         *   It is crucial for the **Unaccounted Reason (Gap)** to be closely related to the **Unaccounted Feature (Cause)**. Always use concepts actually stated in the source and never make your own interpretations.
    c)   **Observed Justification (Effect):** The tangible performance outcome observed in the review. This is the "What".
    The justification must be detailed and exhaustive enough to be understood by itself, without further explanation, and sufficient to justify the booster value.

**Extract Requirement:** Both **Unaccounted Feature** and **Observed Justification** must be **exact, verbatim extracts** from the review. These extracts must be exact, meaning that searching for any extract in the review source will find it as is. **NEVER** invent, paraphrase, or hallucinate content. If the exact text is not in the source, the booster is invalid.
**Technical Causality:** There must be a clear link between the technical mechanism (the **Unaccounted Feature**) and the performance outcome (the **Observed Justification**). Purely comparative statements (e.g., "best we have seen") are **INVALID** unless they explain *why*.

### 11.C Evidence Requirements 
*   **Proof & Precision:** The extracts must contain specific quantitative data (e.g., "Delta-E 0.14", "117 points") or precise technical descriptions. Vague praise is not evidence.
*   **Source Verification:** All source links must be active, accessible URLs from reputable publications. Placeholders (e.g., `example.com`) are **STRICTLY PROHIBITED**. If a specific text extract is used, the source must be verifiable.
*   **Specificity:** Justifications must be extremely specific to the findings of the review and the technical gap they fill.
*   **Disjointed Extracts:** Extracts may combine non-contiguous text from the same review, for example to link technical data with the resulting conclusion. Use `[...]` to indicate the separation. For more fluidity, parts that are less distant from each other than 3 sentences should not be separated.
*   **Decomposition:** A single review source may impact multiple subsections; in such cases, the booster must be decomposed into separate entries.
    *   *Example:* If a review finds a phone has exceptional telephoto zoom but poor video stabilization:
        *   **Booster A (1.10):** Targets Subsection 4.6 (Zoom Capability) for superior optics.
        *   **Booster B (0.90):** Targets Subsection 4.4 (Image Stabilization) for poor software compensation.

### 11.D Mandatory Pre-Commit Protocol
> [!CAUTION]
> **CRITICAL: STOP AND VERIFY**
> You are **FORBIDDEN** from writing or updating any booster in the document until you have explicitly executed the verification loop below.
> 1.  **Draft:** Prepare the content.
> 2.  **Verify:** Check rigidly against Rules 11.A, 11.B, and 11.C.
> 3.  **Log:** Prove the verification by filling in the mandatory log form.
> 4.  **Commit:** Only if **ALL** checks pass, you may update the file. **NEVER** publish without this strict verification.

*   **Verification Loop:** After drafting a booster, perform a mandatory self-check ensuring that **ALL** rules in sections 11.A, 11.B, and 11.C are strictly satisfied. If any rule is violated, discard and refine. Repeat this refinement process up to **3 times**. If the booster still fails to meet all criteria after the 3rd attempt, **discard the booster entirely** and log a "Verification Failed" error for that subsection.

*   **Mandatory Proof of Verification:**
    After the last verification loop iteration, the verification process must be proven by filling in the form `log_format.md` located in `docs/booster_logs`.
    
    **Storage Rules:**
    1.  **Location:** The filled log must be saved in `docs/booster_logs/logs/`.
    2.  **Folder Structure:** Save the log within a folder named after the phone's **Unique ID** (scan existing folders; if it doesn't exist, create it).
    3.  **Naming Convention:** The filename must include:
        *   First: The number of the subsection impacted by the booster.
        *   Second: A title that justifies the booster.
        *   *Format Example:* `4.17_Skin_Tone_Rendering.md`

> [!NOTE]
> The following items are **examples** of how expert reviews can be used to adjust theoretical scores. In practice, any reputable and verifiable expert review can be used as a booster source.

### 🔹 11.1 DXOMARK 24MP Texture Rendering
*   **Source Link:** [iPhone 15 Pro Max Camera Test](https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/)
*   **Impacted Subsection:** 4.16 Multi-Frame Computational Photography (MFCP)
*   **Booster:** **1.05**
*   **Justification:**
    *   **Unaccounted Feature:** "Other important updates compared to the previous generation iPhones include the jump from 12MP to 24MP images by default in most light conditions. In our tests, this made for significantly improved texture quality, especially in close-up portraits."
    *   **Unaccounted Reason:** Section 4.3 scores sensor resolution (48MP hardware), and Section 4.16 scores multi-frame processing presence (Always-on HDR + Night stacking). However, neither captures the quality impact of Apple's decision to bypass the industry standard and output 24MP images by default, which the review explicitly credits for improved texture preservation. Context: Modern smartphones group 4 small pixels together into 1 large pixel to capture more light (pixel binning), meaning even a 48MP camera normally outputs a 12MP image. Apple created unique software to simultaneously capture both a 12MP and 48MP image and merge them into a 24MP final image, yielding significantly higher detail without hardware changes (Source: https://www.apple.com/newsroom/2023/09/apple-unveils-iphone-15-pro-and-iphone-15-pro-max/).
    *   **Observed Justification:** "The camera in Apple's new flagship device comes with an entirely new texture rendering management, and in our tests the results were outstanding. With most lighting conditions resulting in 24MP images, finest details were preserved much better than on most competitors. [...] The Apple iPhone 15 Pro Max provided very natural skin rendering with subtle local contrast and pleasant rendering of the finest details like hair, lips, wrinkles, etc."

### 🔹 11.2 Tom's Guide Display Factory Calibration
*   **Source Link:** [iPhone 15 Pro Max Review](https://www.tomsguide.com/reviews/iphone-15-pro-max)
*   **Impacted Subsection:** 2.4 Color Gamut Coverage (CGC)
*   **Booster:** **1.05**
*   **Justification:**
    *   **Unaccounted Feature:** "it earned a Delta-E score of 0.14 (where zero is perfect)"
    *   **Unaccounted Reason:** Section 2.3 scores DCI-P3 coverage percentage, which measures what colors the display *can* show. It does not measure factory calibration accuracy (Delta-E), which determines how *correctly* those colors are rendered. A display with 100% DCI-P3 coverage but poor calibration will show inaccurate colors.
    *   **Observed Justification:** "The iPhone 15 Pro Max's display offers more accurate colors, as it earned a Delta-E score of 0.14 (where zero is perfect)"

### 🔹 11.3 DXOMARK Portrait Skin Tone Rendering
*   **Source Link:** [iPhone 15 Pro Max Camera Test](https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/)
*   **Impacted Subsection:** 4.17 Semantic / Scene AI Processing
*   **Booster:** **1.05**
*   **Justification:**
    *   **Unaccounted Feature:** "The smart HDR feature helped produce very natural and pleasant colors, even in very challenging light conditions."
    *   **Unaccounted Reason:** Section 4.17 scores the binary presence of semantic segmentation features (face detection, scene recognition). It does not score the specific quality of the tuning, such as the effectiveness of the Smart HDR algorithm in delivering strictly accurate and natural skin tones across diverse demographics, which requires qualitative validation beyond a checklist feature.
    *   **Observed Justification:** "Skin tones were improved compared to the already very good Apple iPhone 14 Pro, across all skin tone types." 
