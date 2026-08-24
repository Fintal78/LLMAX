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


## 🟣 0. Model Hypotheses & Explanations

### 0.1 Logarithmic Normalization and Subsystem Penalties

In the processing performance pipelines of this framework—specifically **Section 6.1 (CPU Multi-Core Performance)**, **Section 6.2 (CPU Single-Core Performance)**, and **Section 6.3.A (GPU Standard Graphics)**—the system applies subsystem bottleneck penalties to the device's score. 

Rather than calculating these penalties in the raw physical domain first and performing normalization at the end, the framework utilizes a **Normalization-First approach**. The raw performance capacity is first mapped logarithmically to a 0–10 perceptual scale, and the penalties are subsequently subtracted directly from this normalized score.

#### The Mathematical Rationale of Logarithmic Subtraction
In real-world computer architecture, a hardware bottleneck (such as a cache capacity deficit or a memory bus bottleneck) acts as a percentage-based multiplier on raw performance rather than a fixed absolute reduction. 

For example, let a raw performance score be X, and let it be modified by a bottleneck multiplier A (where A is between 0.0 and 1.0, representing the fraction of performance retained after the bottleneck). This leads to a penalized raw performance of:
`Raw_Penalized = A * X`

When we apply logarithmic normalization (to compress raw performance to match human perception of speed, aligning with the Weber-Fechner Law), the multiplication turns mathematically into a simple subtraction:
`log(A * X) = log(A) + log(X)`

For example, for a bottleneck multiplier A of 0.8 (representing a 20% performance penalty), this would lead to:
`log(X) + log(0.8) = log(X) - 0.0969`

This proves that after perceptualisation (logarithmic normalization), the multiplier is transformed into a simple "subtractor". The penalties subtracted in Sections 6.1, 6.2 and 6.3.A are mathematically equivalent to these log-domain subtractors.

#### Why this is simpler and more robust
This approach is mathematically simpler because we only need to perform the perceptual normalization once at the beginning, rather than performing linear/performance normalizations and then a final perceptual normalization at the end. 


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
> **Why calculate using the Diagonal?** Sensor light-gathering capacity is determined by its **Area** (`Area ∝ Diagonal²`). Because of the power rule of logarithms, `log(x²) = 2 * log(x)`. When we put the squared diagonal into our normalization formula: `(log(Size²) - log(Min²)) / (log(Max²) - log(Min²))`, it expands to `(2 * log(Size) - 2 * log(Min)) / (2 * log(Max) - 2 * log(Min))`. The factor of `2` perfectly factors out of both the numerator and denominator and completely cancels out. Therefore, scoring the 1-dimensional diagonal logarithmically is mathematically identical to scoring the 2-dimensional area logarithmically, flawlessly simplifying the calculation.


### 🔹 4.2 Main Camera Aperture
*Description:* The size of the lens opening. Wider apertures (lower f-number) let in more light for brighter night shots and create natural bokeh.
*   **Measurement:** Focal length / Entrance pupil diameter.
*   **Unit:** f-stop (f/number)
*   **Significance:** Determines light gathering and depth of field.
*Formula:* `Score = 10 * (log(Camera_Main_Aperture_f_Max) - log(f_stop)) / (log(Camera_Main_Aperture_f_Max) - log(Camera_Main_Aperture_f_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ Camera_Main_Aperture_f_Min
*   **Min Score (0.0):** ≥ Camera_Main_Aperture_f_Max
> [!NOTE]
> **Why Logarithmic?** The quantity of light is proportional to the area of the camera's pupil, which is proportional to `1/f²`. 
> 
> If we wanted to score the raw *volume* of light, we would indeed calculate `1/f²` and score it linearly. However, just as we established in **Section 4.1 (Main Sensor Size)**, the real-world photographic benefits of gathering more light (expanding dynamic range, reducing noise) follow a diminishing return curve. To score the *photographic benefit* rather than the raw volume, we must apply a logarithmic curve: `log(1/f²)`.
> 
> Here is the mathematical magic. Because of the algebraic rules of logarithms, `log(1/f²)` simplifies perfectly to `-2 * log(f)`. 
> 
> When we place this into our standard normalization formula to calculate the score: 
> `(-2 * log(f_stop) - (-2 * log(f_max))) / (-2 * log(f_min) - (-2 * log(f_max)))`
> 
> The factor of `-2` completely factors out of both the top and bottom. The negative signs elegantly flip the subtraction direction, leaving us with: 
> `(log(f_max) - log(f_stop)) / (log(f_max) - log(f_min))`


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
> **Why Logarithmic?** Magnification scales inversely with distance (`M ≈ f/d`). Moving from 4cm to 2cm doubles the magnification capability (a massive gain in macro photography). Moving from 10cm to 8cm only increases magnification by ~25%. A logarithmic score flawlessly maps to this non-linear optical reality, heavily rewarding true microscopic lenses beneath 4cm.

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
> **Why 5.0 for 10-bit?** The raw number of color shades increases exponentially with bit depth (`2^n`), but human perception of these differences follows a **logarithmic scale** (Weber-Fechner law). Because `log_2(2^bits) = bits`, the resulting perceived improvement is perfectly linear relative to the bit depth itself. Therefore, the leap from 8 to 10 bits represents the same proportional visual gain as the leap from 10 to 12 bits, cleanly splitting the 10.0 score space in half.

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
> *   **Aperture (f-number):** In optics, the aperture is written as a fraction where the **f-number** is the denominator (`f/2.2`, `f/2.4`). **Because it's a fraction, a larger f-number actually means a smaller physical opening.**
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

| CPU Core Architecture        | CPU Score | Ref Freq (GHz) | Typical L2 (KB) |      ISA Gen     | ISA Gen Score | Idle Efficiency Score |
|:-----------------------------|:---------:|:--------------:|:---------------:|:-----------------|:-------------:|:---------------------:|
| **C1-Ultra (Lumex)**         |   10.00   |      4.21      |      2048       |      ARMv9.3     |     1.10      |         0.30          |
| **Apple Everest (A18/Pro)**  |   10.00   |      4.05      |     16384       |      ARMv9.2     |     1.08      |         1.30          |
| **Qualcomm Oryon Gen 2**     |   9.80    |      4.32      |     12288       |      ARMv8.7     |     1.05      |         1.00          |
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

When the target device lacks direct benchmark data, we use a technical predictive model to locate the **3 most physically similar reference devices** that *do* have benchmark data, and interpolate the target device's score.

To establish what makes two devices "physically similar," we leverage the core physics-based equations from **Method C: Technical Predictor Model** (detailed in Section 6.10.C). Under Method C, a device's thermal stability is governed by the available thermal headroom ratio, which is determined by the peak processor heat load, the parasitic system heat load, and the total admissible thermal power limit of the chassis.

##### 6.10.B.1 The 3-Component Physical Similarity Space
To map devices into a dimensionally homogeneous coordinate system where every dimension is expressed in **Watts (W)**, we measure how much the target device (the phone being scored) differs from a candidate neighbor device (a reference phone in our database). Specifically, we combine the differences in their three primary thermodynamic power components:
1.  **Peak System-on-Chip (SoC) Power (`P_soc_peak`, in Watts - W):**
    The peak thermal power generated by the processor silicon during high-performance workloads:
    `P_soc_peak = power_peak_soc`
2.  **Base System Power (`P_base`, in Watts - W):**
    The baseline heat generated by non-processor components (primarily display panel radiant heat and Power Management Integrated Circuit (PMIC) conversion losses):
    `P_base = power_base_needs`
3.  **Total Admissible Power (`P_admissible`, in Watts - W):**
    The maximum total power the chassis can safely manage at the end of the 1200-second evaluation window before its surface temperature surpasses the ergonomic safety limit (20°C temperature rise limit):
    `P_admissible = power_admissible`

Projecting devices into this 3-component physical similarity space ensures that similarity is based on actual thermal operating scales rather than arbitrary relative percentages. It weights the coordinates naturally 1-to-1 by physical impact in Watts, eliminating the need for artificial weights.

##### 6.10.B.2 Feature Distance Formula
The similarity between the target device and a candidate neighbor device is computed using the **Euclidean Distance** across the 3 physical components:
*   **Formula:**
    `Distance = Sqrt( (Diff_P_soc_peak)^2 + (Diff_P_base)^2 + (Diff_P_admissible)^2 )`
*   **Where the differences are defined as:**
    *   `Diff_P_soc_peak = P_soc_peak_target - P_soc_peak_neighbor`
    *   `Diff_P_base = P_base_target - P_base_neighbor`
    *   `Diff_P_admissible = P_admissible_target - P_admissible_neighbor`
    *   *Target:* The device currently being scored.
    *   *Neighbor:* Any device in the search space with a known benchmark score.
*   **Search Space:** All devices with known 3DMark Stability scores (Method A), **excluding the target device** itself.
*   **Selection:** Pick the 3 distinct neighbor devices with the smallest `Distance`.

> [!NOTE]
> **Why Homogeneous Euclidean Distance in Watts?**
> Thermal performance is an equilibrium between heat generation and heat dissipation. Projecting devices into a homogeneous coordinate system in Watts (W) ensures that similarity is measured using the exact physical scales of the thermal energy balance. 
> 
> Because the standard benchmark is evaluated at exactly 1200 seconds, the integrated admissible power limit (`P_admissible`) captures the combined resistance and transient capacitance of the chassis at that boundary. This eliminates the need for arbitrary weights and matches devices with similar physical heat-generation and heat-shedding characteristics to maintain interpolation accuracy.

##### 6.10.B.3 Interpolation and Correction
1.  Calculate the average predicted score of the 3 neighbors (from Method C):
    `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
    *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
2.  Compute the Correction Ratio, which measures how the target device's profile structurally differs from its neighbors:
    `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
    *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.
3.  Compute the average real-world benchmark score of the 3 neighbors (normalized using Method A):
    `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
4.  Apply the Correction Ratio to calculate the final Interpolated Score:
    `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`
    *Note:* The resulting score is clamped between 0.0 and 10.0.


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

**Table 1: Master SoC Peak Power Reference (Extract)**
*Values represent verified Package Power (Watts) measured under maximum peak synthetic load. For the full exhaustive database of all mobile silicon (2016–2026), refer to the Source of Truth.*

| SoC Model                           | Peak Power (power_peak_soc) [Watts]  | Node  |
| :---------------------------------- | :----------------------------------: | :---: |
| **Snapdragon 8 Elite**              | **19.5**                             | 3nm   |
| **Snapdragon 8 Gen 1**              | **16.5**                             | 4nm   |
| **Dimensity 9400**                  | **15.5**                             | 3nm   |
| **[...]**                           | **[...]**                            | [...] |

> [!IMPORTANT]
> **Source of Truth:** The full authoritative lookup table for all smartphone SoCs (2016–2026) is located in the [System on Chip (SoC) Reference (references/soc_reference.md)].

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

| Score    | Technology                                            | 
| :------- | :---------------------------------------------------- | 
| **10.0** | **Tier 1: 5G mmWave + Sub-6 (Global band coverage)**  | 
| **9.0**  | **Tier 2: 5G Sub-6 (Full Global Bands)**              |
| **8.0**  | **Tier 3: 5G Sub-6 (Limited/regional bands)**         |
| **6.0**  | **Tier 4: 4G LTE-Advanced Pro**                       |
| **4.0**  | **Tier 5: 4G LTE (Basic)**                            |
| **2.0**  | **Tier 6: 3G**                                        |
| **0.0**  | **Tier 7: 2G**                                        |

> [!NOTE]
> **Terminology & Abbreviations:**
> *   **5G (5th Generation):** The fifth generation of cellular networks, bringing higher speed and capacity.
> *   **mmWave (millimeter-Wave):** High-frequency 5G bands (typically above 24 GHz) providing ultra-fast speeds over short distances.
> *   **Sub-6 (Sub-6 Gigahertz):** Lower-frequency 5G bands (below 6 GHz) providing long-range coverage and penetration.
> *   **4G (4th Generation) / LTE (Long-Term Evolution):** The fourth generation of mobile networks.
> *   **LTE-Advanced Pro:** An enhanced 4G standard (sometimes called 4.5G) representing Category (Cat) 16 or higher modems with download speeds of 1.0 Gigabits per second (Gbps) or higher.
> *   **3G (3rd Generation):** Legacy third generation networks (such as Universal Mobile Telecommunications System / UMTS or High-Speed Downlink Packet Access / HSDPA).
> *   **2G (2nd Generation):** Legacy second generation networks (such as Global System for Mobile Communications / GSM).
>
> **Why is there no "5G mmWave Alone" category?**
> Millimeter-Wave frequencies suffer from severe path attenuation and signal blockages, making them incapable of acting as standalone coverage layers. In real-world networks, a device requires a Sub-6 GHz (or 4G LTE) connection anchor to maintain coverage. Therefore, all millimeter-Wave-capable devices are hybrid solutions supporting both millimeter-Wave and Sub-6 GHz bands; a device supporting millimeter-Wave alone is physically and operationally non-viable.
>
> **Ambiguity & Insufficient Data Fallback Rules:**
> To ensure absolute consistency and eliminate duplication of scoring logic, all step-by-step ambiguity resolution, System-on-Chip (SoC) lookup pathways, and generic generational fallback rules for cellular capability grading are defined exclusively in the schema guidelines of the database definition file [proposed_data_structure.md]. Automated agents must execute that multi-step logic hierarchy to resolve missing or incomplete specifications.


### 🔹 7.2 SIM Capabilities
*Description:* Evaluates the device's support for cellular subscriber identity modules (SIM), prioritizing network flexibility, digital convenience, and transceiver hardware concurrency. Dual SIM functionality allows users to maintain two active telephone numbers (e.g., work/personal lines) or utilize a local carrier network while traveling without disabling their primary card.

#### Terminology & Abbreviations
*   **SIM (Subscriber Identity Module):** The traditional physical card (currently Nano-SIM, the smallest physical form factor) that stores network authentication credentials to connect a device to a cellular network.
*   **eSIM (Embedded Subscriber Identity Module):** A programmable SIM chip soldered directly onto the device's motherboard. It allows users to download and store multiple carrier profiles digitally, enabling remote carrier activation and switching without physical card swaps.
*   **iSIM (Integrated Subscriber Identity Module):** The latest hardware standard where SIM functionality is integrated directly into the system secure processing unit (SPU) of the main processor (SoC), bypassing the need for a separate physical chip. It offers identical digital flexibility to eSIM but with enhanced space and power efficiency.
*   **DSDS (Dual SIM Dual Standby):** A dual-SIM operational mode where both SIMs (physical and/or digital) are registered on the network in standby. Because they share a single radio transceiver, if one SIM becomes actively engaged in a call or data session, the other SIM goes temporarily offline and cannot receive traffic.
*   **DSDA (Dual SIM Dual Active):** An advanced hardware configuration utilizing independent dual transceivers. Both SIMs remain fully active simultaneously, enabling voice calls and high-speed data transmission on both lines concurrently without interference.
*   **MEP (Multiple Enabled Profiles):** A software-hardware capability (standardized in Android 13 and iOS) that allows a single eSIM chip to maintain two concurrent active connections to different networks, enabling dual-eSIM functionality without requiring multiple physical eSIM chips.

*Measurement:* Analysis of physical slot and digital SIM specifications from manufacturer documentation and verified hardware reviews.
*Unit:* Configuration composite score.

#### Scoring Formula
The final SIM Capabilities score is calculated as the sum of two distinct technical components:

`SIM Capabilities Score = Slot & Digital Configuration Score + Concurrency Transceiver Premium`

The maximum achievable score is capped at 10.0, representing the physical and digital state-of-the-art.

#### Table 1: Slot & Digital Configuration Class (Base Score, Max 8.0)
Evaluates physical slots, programmable formats, profile management, and slot redundancy.

| Base Score | Configuration Name                     | Engineering Definition & Justification                                  |
|:----------:|:---------------------------------------|:------------------------------------------------------------------------|
|  **8.0**   | **Dual eSIM / iSIM + Physical Slot**   | Multiple active digital profiles (eSIM/iSIM) alongside a physical slot. |
|  **7.0**   | **Single eSIM / iSIM + Physical Slot** | One active digital profile (eSIM/iSIM) alongside a physical slot.       |
|  **5.50**  | **Dual Physical Nano-SIM Slots**       | Two physical Nano-SIM slots only; no electronic/integrated SIM support. |
|  **5.00**  | **Dual eSIM / iSIM Only**              | Multiple active digital profiles (eSIM/iSIM) but no physical slot.      |
|  **1.50**  | **Single eSIM / iSIM Only**            | One active digital profile (eSIM/iSIM) only; no physical slot.          |
|  **0.00**  | **Single Physical Nano-SIM Only**      | One physical Nano-SIM slot only; no dual-SIM or digital profile support.|

#### Table 2: Concurrency Transceiver Mode (Concurrency Premium, Max 2.0)
Measures the device's transceiver capability to maintain active concurrent connections.

| Concurrency Premium | Mode Name                        | Engineering Definition & Justification                                                           |
|:-------------------:|:---------------------------------|:-------------------------------------------------------------------------------------------------|
|       **2.0**       | **Dual SIM Dual Active (DSDA)**  | Dedicated dual radio transceivers. Allows simultaneous active voice/data sessions on both lines. |
|       **1.0**       | **Dual SIM Dual Standby (DSDS)** | Shared single transceiver. One line goes offline when the other is actively on a call.           |
|       **0.0**       | **Single Standby / None**        | No concurrent active standby capability (Single-SIM devices).                                    |

#### Justification for the 2-Table Decomposed Model
Table 2 is strictly required to complement Table 1 because SIM capabilities are defined by two independent hardware dimensions: the physical/electronic format interface (Table 1) and the transceiver radio frequency (RF) concurrency pathway (Table 2). Merging them or omitting Table 2 would fail to represent actual device designs:
1. **Transceiver Independence:** The slot configuration does not dictate transceiver concurrency. For example, a "Dual Physical Nano-SIM Slots" configuration (Table 1, Tier 3) can operate in Dual SIM Dual Standby (DSDS) mode on a budget device (Table 2, Tier 2, yielding 5.50 + 1.0 = 6.50) or in Dual SIM Dual Active (DSDA) mode on an older flagship featuring duplicate transceivers (Table 2, Tier 1, yielding 5.50 + 2.0 = 7.50).
2. **Flagship Concurrency Differentiation:** Modern flagships with "Dual eSIM / iSIM + Physical Slot" (Table 1, Tier 1) exhibit different architectures. An international iPhone 15 Pro uses a single transceiver (DSDS, yielding 8.0 + 1.0 = 9.0), while a OnePlus 12 features independent dual RF transceivers supporting full simultaneous data and voice concurrency (DSDA, yielding 8.0 + 2.0 = 10.0).
3. **Simplicity and Extensibility:** Decomposing the model avoids a combinatorial table of multiple merged rows, keeping data entry modular and easily auditable.

#### Configuration & Engineering Justification

*   **Asymmetry of Dual SIM vs. Single SIM (Physical vs. eSIM):**
    The scoring model applies an asymmetric valuation to physical vs. eSIM interfaces depending on whether the hardware supports single-line or multi-line (dual-SIM) configurations:
    
    1.  **Dual-SIM: Why Dual Physical (5.50) > Dual eSIM Only (5.00)**
        -   *Universal Compatibility:* A phone with dual physical SIM slots is usable anywhere in the world because physical plastic Nano-SIM cards are universally supported by all cellular operators (including legacy, prepaid, tourist, and discount carriers).
        -   *eSIM Restrictions:* A dual eSIM-only device is severely restricted in regions (such as parts of Africa, South America, and Asia) or with budget carriers that do not offer eSIM provisioning, rendering the second line (or the entire device) unusable. 
        -   *Operational Ease:* Physical SIMs can be swapped manually in seconds without internet connectivity or carrier web portals. Therefore, having a physical slot is a critical fallback, making Dual Physical (5.50) superior to Dual eSIM Only (5.00).

    2.  **Single-SIM: Why Single eSIM Only (1.50) > Single Physical Only (0.00)**
        -   *Digital Reconfigurability:* While both configurations restrict the user to a single active line, the single eSIM interface allows the user to store multiple digital profiles on the chip and swap them dynamically via software (e.g. download a roaming plan via a Quick Response - QR - code or carrier app).
        -   *Physical Rigidity:* A single physical SIM slot is completely rigid: to swap carriers, the user must physically acquire, handle, and insert a new plastic card. Thus, the software-configured eSIM offers slightly more convenience than a single physical slot, justifying the minor premium of 1.50 over 0.00.

*   **Physical Slot Fallback vs. eSIM-Only:**
    Although eSIM/iSIM represents superior digital convenience, it suffers from non-universal carrier adoption globally. In many developing regions or tourist destinations, cellular providers do not support eSIMs or restrict them to postpaid accounts. Devices lacking a physical tray restrict user choice in these regions, which is why eSIM-only configurations are penalized relative to hybrid slots.
*   **eSIM vs. iSIM Scoring Equivalency:**
    The integrated SIM (iSIM) represents a superior silicon-level engineering achievement over discrete eSIM chips. Its primary physical benefit (space savings of under 1 square millimeter) is captured indirectly in Section 1.4 (Ergonomics) through overall device thinness and volumetric packaging efficiency (permitting a larger battery). The power efficiency gain of iSIM (saving approximately 100 to 200 microwatts in standby) is not explicitly modeled as a distinct variable in Section 8.1 (Battery Endurance) because it is negligible (representing less than 0.02% of the standard active system power draw of at least 1 Watt, and less than 1% of deep-sleep standby power of 15 to 50 milliwatts). However, to avoid double-counting the indirect packaging advantages and because eSIM and iSIM offer identical cellular network capabilities, they are scored identically in Section 7.2.
*   **DSDA vs. DSDS Concurrency:**
    DSDA represents a significant hardware premium, requiring duplicate RF (Radio Frequency) front-end transceivers and antennas. This hardware duplication allows both SIMs to maintain active sessions simultaneously. DSDS is a software-switched single-transceiver compromise where one SIM is muted during active sessions on the other. DSDA is rewarded a 2.0 premium for this hardware superiority.
*   **Physical Tray Architecture Trade-offs:**
    To avoid double-counting, the trade-off of a hybrid SIM tray (where the user must choose between a second physical SIM card and a microSD storage card) is evaluated exclusively in Section 6.9 (Storage Expandability) and does not deduct from the cellular SIM capabilities score here.

> [!NOTE]
> **Regional Variant Scoring Constraint:**
> SIM configurations are heavily regionalized. For example, a single marketing model name (such as Apple iPhone 15 or Samsung Galaxy S24) may be sold as eSIM-only in the United States, dual physical SIM in China, and Nano-SIM + eSIM in Europe. SIM capabilities must be evaluated per specific regional SKU/variant to ensure database accuracy.
> 
> **Ambiguity & Insufficient Data Fallback Rules:**
> To ensure absolute consistency and eliminate duplication of scoring logic, all step-by-step ambiguity resolution and generic generational fallback rules for SIM capability grading are defined exclusively in the schema guidelines of the database definition file [proposed_data_structure.md]. Automated agents must execute that multi-step logic hierarchy to resolve missing or incomplete specifications.


### 🔹 7.3 Wi-Fi Standard
*Description:* Wi-Fi technology. Newer standards (Wi-Fi 7/6E) provide faster, more stable internet, especially in crowded homes.
*   **Measurement:** Supported Wi-Fi protocols.
*   **Unit:** Standard (Generation)
*   **Significance:** Local network speed and congestion management.
*   **Battery Model Mapping:** The exact standard string from this table is mapped directly in the battery endurance scoring of **Section 8.1** to determine Wi-Fi chip active power consumption (P_wifi).

| Score    | Standard             | 
| :------- | :------------------- | 
| **10.0** | **Tier 1: Wi-Fi 7**  | 
| **8.0**  | **Tier 2: Wi-Fi 6E** | 
| **7.0**  | **Tier 3: Wi-Fi 6**  | 
| **5.0**  | **Tier 4: Wi-Fi 5**  | 
| **3.0**  | **Tier 5: Wi-Fi 4**  | 
| **0.0**  | **Tier 6: Wi-Fi ≤3** |

> [!NOTE]
> **Understanding the score gaps:** Not all Wi-Fi upgrades are equal leaps, and the scoring reflects this:
>
> *   **Wi-Fi 4 → 5 (+2) and Wi-Fi 5 → 6 (+2):** Both brought significant new architectures. Wi-Fi 6 in particular introduced OFDMA (Orthogonal Frequency Division Multiple Access). Instead of the router communicating with only one smartphone at a time while forcing all other devices in the room to wait their turn to send or receive data, OFDMA splits a single frequency channel into multiple smaller sub-channels (called Resource Units / RUs). This allows the router to transmit data packets to, and receive data packets from, multiple different smartphones simultaneously — like switching from a single checkout lane to a supermarket with many lanes open at once — massively improving connection responsiveness in crowded homes or offices.
> *   **Wi-Fi 6 → 6E (+1):** This is **not a new protocol**. Wi-Fi 6E runs the exact same technology as Wi-Fi 6 (both are 802.11ax), simply extended to an additional frequency band (6GHz) for less congestion. Meaningful, but incremental — hence only a 1-point gap.
> *   **Wi-Fi 6E → 7 (+2):** Wi-Fi 7 is a **brand new protocol** (802.11be) with three fundamental advances: **Multi-Link Operation** (MLO, the phone uses 2.4GHz, 5GHz, and 6GHz simultaneously — like having three roads instead of one), **doubled channel width** (320MHz vs 160MHz for faster data bursts), and a new signal encoding that packs ~20% more data per transmission. Real-world speeds roughly double vs. Wi-Fi 6E. This earns its full 2-point gap.


### 🔹 7.4 Bluetooth & Audio Codecs

* **Description:** Evaluates the hardware capabilities of the device's Bluetooth wireless communication interface and high-fidelity wireless audio compression codecs. Newer Bluetooth standards provide faster data transmissions, larger ranges, better energy efficiency, and improved connection stability. Advanced audio codecs allow the device to transmit audio at higher bitrates (amount of data processed per second) over the air, delivering superior sound quality to compatible headphones or speakers.
* **Measurement:** Supported Bluetooth version and highest supported high-fidelity audio codec verified from official manufacturer documentation and technical product reviews.
* **Unit:** Composite score.

#### Terminology & Abbreviations
*   **Bluetooth (BT):** A short-range wireless technology standard used for exchanging data between fixed and mobile devices over short distances.
*   **LE (Low Energy) / BLE (Bluetooth Low Energy):** A power-conserving variant of Bluetooth designed for low-bandwidth applications (such as sensors, fitness trackers, and smartwatches) to run for long periods on small batteries.
*   **LC3 (Low Complexity Communication Codec):** The modern, high-efficiency default audio codec introduced with Bluetooth Low Energy (LE) Audio. It provides significantly better sound quality than legacy standards at much lower bitrates, reducing latency and battery consumption.
*   **SBC (Subband Codec):** The mandatory, universal baseline audio codec supported by all Bluetooth audio devices. It is a lossy standard that uses substantial compression, yielding basic audio quality.
*   **AAC (Advanced Audio Coding):** A highly efficient, standard lossy audio codec widely used by Apple iOS devices and popular music streaming services. It offers better sound quality than SBC at equivalent bitrates.
*   **LDAC:** Sony's proprietary High-Resolution Bluetooth audio codec (certified by the Japan Audio Society for "Hi-Res Audio Wireless"). It transmits audio at high bitrates up to 990 Kilobits per second (kbps), maintaining more audio detail than standard codecs.
*   **LHDC (Low Latency High-Definition Audio Codec):** A high-resolution Bluetooth audio codec developed by Savitech. It supports bitrates up to 900 kbps and offers low-latency transmission for gaming and media consumption.
*   **SSC (Samsung Seamless Codec):** Samsung's proprietary high-resolution audio codec. It dynamically scales its transmission bitrate to prevent audio dropouts in busy wireless environments and supports high-fidelity 24-bit audio when paired with compatible Samsung Galaxy Buds.
*   **UHQ-BT (Ultra High Quality Bluetooth):** Samsung's legacy proprietary high-resolution audio codec, which served as a precursor to their Scalable and Seamless codecs.
*   **L2HC (Huawei's proprietary codec):** Huawei's high-resolution and lossless audio codec. It adjusts bitrates dynamically up to 1.9 Megabits per second (Mbps) in its latest versions to maintain high quality and connection stability.

#### Scoring Formula
The Bluetooth & Audio Codecs score is calculated as the sum of the physical Bluetooth version subscore, the codec capability subscore, and any applicable perceived quality / ecosystem optimization bonuses:

`Bluetooth & Audio Codecs Score = Clamp(Bluetooth Version Subscore + Codec Capability Subscore + Perceived Quality Bonus, 0.00, 10.00)`

The final score is clamped between a minimum of **0.00** (worst/obsolete configuration) and a maximum of **10.00** (best/state-of-the-art configuration).

#### Part 1: Bluetooth Version Score (Weighted, Max 5.00)
Evaluates the physical Bluetooth transceiver version built into the phone. The subscore is assigned based on the highest standard supported by the hardware:

| Bluetooth Version             | Subscore | Engineering Definition & Justification                                                      |
| :---------------------------- | :------: | :------------------------------------------------------------------------------------------ |
| **Bluetooth 5.4**             | **5.00** | Supports Periodic Advertising (PAwR) and Encrypted Advertising (EAD).                       |
| **Bluetooth 5.3**             | **4.50** | Introduces Connection Subrating for instant power/performance scaling.                      |
| **Bluetooth 5.2**             | **4.00** | **MAJOR LEAP:** Introduces Low Energy (LE) Audio, Low Complexity Codec (LC3), and Auracast. |
| **Bluetooth 5.1**             | **2.50** | Introduces Direction Finding for precise centimeter-level positioning.                      |
| **Bluetooth 5.0**             | **2.00** | **MAJOR LEAP:** Major capacity update: 2x speed, 4x range, 8x broadcast capacity.           |
| **Bluetooth 4.2 / 4.1 / 4.0** | **1.00** | Legacy low-power Bluetooth Low Energy (BLE) connectivity baseline.                          |
| **Bluetooth < 4.0**           | **0.00** | Obsolete Classic Bluetooth standards without low-energy profiles.                           |

##### Engineering Significance of Bluetooth Standards
*   **Bluetooth 5.4 Key Technologies:**
    *   *Periodic Advertising with Responses (PAwR):* Enables energy-efficient bidirectional communication between a central device (such as a smartphone or hub) and thousands of ultra-low-power nodes (such as smart tags, sensors, or electronic shelf labels) in a synchronized manner, without needing dedicated connection pairings.
    *   *Encrypted Advertising Data (EAD):* Standardizes how broadcast payloads are securely encrypted. Only authorized receivers can decrypt the broadcast data, preventing unauthorized eavesdropping and tracking of device locations or sensor readouts.
*   **Bluetooth 5.3 Key Technologies:**
    *   *Connection Subrating:* Allows the connection to instantly transition between a low-power, slow-cycling standby state and a high-performance active transmission state. This reduces communication delay (latency) and extends battery life during variable-activity tasks like audio calls or fitness tracking.
*   **Bluetooth 5.2 Key Technologies:**
    *   *Low Energy (LE) Audio & Low Complexity Communication Codec (LC3):* Implements high-quality audio streaming over power-saving low-energy channels. The LC3 compression standard delivers equal or better sound quality than the legacy SBC baseline at half the transmission bitrate, significantly lowering energy draw and latency.
    *   *Auracast Broadcast Audio:* Enables a transmitter to broadcast one or more audio streams to an unlimited number of nearby compatible receivers (such as headphones, earbuds, or hearing aids) simultaneously.
*   **Bluetooth 5.1 Key Technologies:**
    *   *Direction Finding:* Supports Angle of Arrival (AoA) and Angle of Departure (AoD) measurements using multi-antenna arrays. This allows the receiver to calculate the exact direction of a signal source, enabling precise indoor navigation and tracking accurate to a few centimeters.
*   **Bluetooth 5.0 Key Technologies:**
    *   *2x Speed & 4x Range:* Increases the maximum transmission bitrate to 2 Megabits per second (Mbps) (double the speed of older standards) or extends the range up to four times, allowing for more stable whole-home connectivity and faster data transfers for wearables.

#### Part 2: Codec Capability Score (Tiered, Max 5.00)
Evaluates the highest quality wireless audio compression protocol supported by the device's operating system and hardware licensing. Scored by the highest tier codec protocol supported:

| Codec Tier   | Subscore  | Qualifying Codecs                                                   | Engineering Definition & Justification                               |
| :----------- | :-------: | :------------------------------------------------------------------ | :------------------------------------------------------------------- |
| **Lossless** |  **5.00** | aptX Lossless, LHDC V5 Lossless, L2HC 3.0                           | Mathematically bit-for-bit lossless CD audio up to 1.2 Mbps.         |
| **High-Res** |  **3.50** | LDAC, LHDC v1-v4, aptX Adaptive, aptX HD, SSC, UHQ-BT, L2HC 1.0/2.0 | High-bitrate lossy audio up to 24-bit/96 kHz (500 to 990 kbps).      |
| **Standard** |  **0.00** | AAC, SBC, LC3, aptX Classic, aptX LL                                | Standard baseline lossy audio at standard bitrates (128 to 352 kbps).|

#### Part 3: Perceived Quality & Ecosystem Optimization Bonus (Additive, Max +1.50)
Real-world listening quality, connection stability, and latency management are enhanced on certain devices through custom software/hardware integration and proprietary audio pipelines:
*   **Apple iOS AAC Optimization (+1.50):** Applied to Apple devices. Due to Apple's highly optimized hardware-accelerated AAC (Advanced Audio Coding) encoder/decoder integration and proprietary custom audio processing pipeline, these devices deliver perceived audio quality, latency management, and connection stability that are significantly superior to standard SBC (Subband Codec) or AAC implementations, bridging the gap toward the High-Res (High-Resolution) tier under standard bitrates (128-256 kbps).
*   **Samsung Seamless Codec (SSC) Optimization (+0.50):** Applied to Samsung devices. SSC dynamically scales its transmission bitrate to prevent audio dropouts in busy wireless environments and supports high-fidelity 24-bit audio when paired with compatible Samsung Galaxy Buds.
*   **None (+0.00):** Standard generic Bluetooth audio implementation without custom system-level optimization or dynamic scaling.

#### Common Configuration Reference (overall BT + Codec Score)
The following reference scenarios demonstrate how the subscores and perceived quality bonuses compile into the final score:

| Score    | Combo Example                              | Typical Devices                  |
| :------- | :----------------------------------------- | :------------------------------- |
| **10.0** | **5.4 + Lossless** (5.0 + 5.0 + 0.0)       | OnePlus 12, Asus ROG Phone 8     |
| **8.5**  | **5.3 + High-Res + SSC** (4.5 + 3.5 + 0.5) | Samsung Galaxy S24/S25 Series    |
| **7.5**  | **5.2 + High-Res** (4.0 + 3.5 + 0.0)       | Google Pixel 8, Xiaomi 13 Pro    |
| **6.0**  | **5.3 + Standard + AAC** (4.5 + 0.0 + 1.5) | Apple iPhone 15/16 Series        |
| **2.0**  | **5.0 + Standard** (2.0 + 0.0 + 0.0)       | Entry-level/Older Budget Android |


### 🔹 7.5 Biometrics

*Description:* Unlocking methods. Secure face or fingerprint unlock is faster and safer than typing a PIN (Personal Identification Number) every time.
*   **Measurement:** Verification of physical biometric hardware presence and operating system (OS) security class integration.
*   **Unit:** Composite Score (0.00 to 10.00)
*   **Significance:** Determines device access convenience and payment-grade transaction authorization security.

#### 7.5.0 Technical Definitions & Security Hierarchy
To ensure objective, consistent, and transparent grading for all devices, biometric technologies are classified by their security strength, authentication latency (speed), and environmental reliability (such as performance under direct sunlight or with wet hands).

##### 1. Fingerprint (FP) Recognition Technologies
*   **Ultrasonic Under-Display (UD) Fingerprint (FP) Sensors:** Modalities that emit high-frequency acoustic waves to map a three-dimensional (3D) replica of the physical ridges and pores of the finger.
    *   *Security & Usability:* Certified as Android Class 3 (Strong) security. It operates through display panels, works reliably even with wet or dirty fingers, does not require bright display flashes, and is highly resistant to two-dimensional (2D) spoof attacks.
*   **Capacitive Physical Fingerprint (FP) Sensors:** Traditional sensors integrated into the device chassis (such as a side-mounted power button, rear-mounted circular pad, or a front-mounted Home button) that utilize miniature capacitor arrays to measure electrical charge variances. (Also includes rare under-glass capacitive sensors, which are categorized here for simplicity.)
    *   *Security & Usability:* Certified as Android Class 3 (Strong) or Apple Touch ID equivalent. They offer exceptionally low authentication latency (typically under 150 milliseconds) and high consistency, but occupy external frame area and fail to read if the sensor surface or skin is wet.
*   **Optical Under-Display (UD) Fingerprint (FP) Sensors:** Modalities that project light from the display screen to capture a high-contrast 2D photographic image of the fingerprint ridges via an under-glass camera sensor.
    *   *Security & Usability:* Certified as Android Class 3 (Strong) on modern devices. They are sensitive to skin moisture variations, can be blinded by intense outdoor sunlight, and emit a bright flash that can cause eye discomfort in dark environments.
*   **Legacy Swipe Fingerprint (FP) Sensors:** Obsolete scanners requiring the user to physically drag their finger across a narrow capacitive sensor strip (e.g., Samsung Galaxy S5, Galaxy Note 4).
    *   *Security & Usability:* Classified as Android Class 2 (Weak) or Class 1 (Convenience). They suffer from a high rate of read failures, slow throughput, and low spoof resistance.

##### 2. Face and Iris Recognition Technologies
*   **Three-Dimensional (3D) Face Unlock (Hardware-Based):** Dedicated hardware arrays that project thousands of invisible infrared (IR) light dots (Structured Light) or emit timed IR pulses (Time-of-Flight / ToF) to map a 3D facial coordinate mesh.
    *   *Security & Usability:* Certified as Class 3 (Strong) equivalent (e.g., Apple Face ID). It has a False Acceptance Rate (FAR) of 1 in 1,000,000, operates in total darkness, and cannot be spoofed by flat photos or video screens.
*   **Secure Two-Dimensional (2D) Face Unlock (Software + Secure Silicon):** Systems utilizing a standard front camera coupled with machine learning (ML) depth-estimation algorithms, where facial templates are processed within a dedicated physical security chip (e.g., Google Pixel 8/9 using the Tensor G3/G4 and Titan M2 security processors).
    *   *Security & Usability:* Certified as Android Class 3 (Strong). This category requires official Class 3 (Strong) certification or equivalent verified manufacturer documentation demonstrating it is authorized for payments. Otherwise, ordinary camera-based face unlock is scored under standard 2D software face unlock (0.00). It degrades in low-light environments and does not function in complete darkness.
*   **Iris Scanner (Dedicated IR Hardware):** Modalities mapping the unique patterns of the human iris using a dedicated IR Light-Emitting Diode (LED) and an IR-wavelength camera sensor (e.g., Samsung Galaxy S8/S9/Note 8/Note 9).
    *   *Security & Usability:* Certified as Class 3 (Strong) equivalent. It is secure and works in the dark, but suffers from a narrow positioning angle, slow registration speed, and outdoor sunlight interference.
*   **Standard Two-Dimensional (2D) Face Unlock (Software-Only):** Basic camera-based facial matching without dedicated secure hardware processors or dynamic depth-checking liveness algorithms.
    *   *Security & Usability:* Classified as Android Class 2 (Weak) or Class 1 (Convenience). It is insecure, easily bypassed with static photos or digital displays, and restricted from payment or banking authentication.

#### Composite Scoring Formula
The final Biometrics Score is calculated as a composite sum of two distinct technical dimensions:

`Biometrics Score = Primary Biometric Subscore + Redundancy Premium`

The overall score is clamped strictly between **0.00** (no secure biometrics) and **10.00** (state-of-the-art secure biometrics).

#### 7.5.1 Primary Biometric Subscore (Max 8.00 points)
Assesses the highest-tier biometric modality available on the device that meets the Class 3 (Strong) standard or Apple equivalent:

| Primary Technology                            |  Subscore  | Key Technical Attributes & Security Level                                            |
| :-------------------------------------------- | :--------: | :----------------------------------------------------------------------------------- |
| **Ultrasonic Under-Display FP**               |  **8.00**  | 3D acoustic scan; wet-finger tolerant; no display flash; payment-grade.              |
| **3D Face Unlock (Structured Light/ToF)**     |  **8.00**  | 3D mesh projection; hands-free; works in darkness; payment-grade.                    |
| **Capacitive Physical FP (Side/Rear/Front)**  |  **7.00**  | Physical button sensor; sub-150ms latency; fails with wet hands; payment-grade.      |
| **Optical Under-Display FP**                  |  **6.00**  | Under-glass 2D capture; bright display flash required; payment-grade.                |
| **Secure 2D Face Unlock (Class 3 Certified)** |  **5.50**  | Standard camera + ML depth mapping; payment-grade; fails in darkness.                |
| **Iris Scanner (Dedicated IR Hardware)**      |  **4.50**  | Iris detail mapping; works in darkness; narrow angle alignment; payment-grade.       |
| **Legacy Swipe Fingerprint Sensor**           |  **1.50**  | Swipe capacitive bar; high False Rejection Rate (FRR); lockscreen-only.              |
| **No Secure Biometrics (PIN/Pattern Only)**   |  **0.00**  | No secure hardware; includes standard 2D software face unlock (Class 2/1).           |

#### 7.5.2 Redundancy & Concurrency Premium (Max 2.00 points)
Rewards the presence of a secondary secure unlock method. Dual-modality combinations ensure convenience in situations where one method is blocked (e.g., wearing gloves vs. wearing a mask or sunglasses). If the device lacks a second secure biometric sensor (meaning the secondary method is either absent or is an insecure software-only 2D face unlock), it receives no redundancy premium (+0.00 points).

*   **Dual Strong Biometrics (Dual-Sensor Redundancy) (+2.00 points):** The device features both a secure fingerprint sensor (defined as Ultrasonic, Capacitive Physical, or Optical Under-Display FP; subscore >= 6.00) AND a secure face/iris scanner (defined as 3D Face Unlock, Secure 2D Face Unlock, or Iris Scanner; subscore >= 4.50).
    *   *Examples:* Google Pixel 9 Pro (Ultrasonic UD FP + Secure 2D Face), Huawei Mate 60 Pro (3D Face ID + Under-Display Optical FP), Samsung Galaxy Note 9 (Capacitive Rear FP + Dedicated Iris Scanner).

#### Common Configuration Reference (Sample Models)
The following matrix demonstrates how subscores and redundancy premiums compile into final biometrics scores for key device profiles:

| Device Model                 | Primary (Max 8.0) |  Redundancy (Max 2.0)  |    Final Score    | Hardware & Security Profile                    |
| :--------------------------- | :---------------: | :--------------------: | :---------------: | :--------------------------------------------- |
| **Google Pixel 9 Pro**       |       8.00        |   2.00 (Dual Strong)   | **10.00 / 10.0**  | Ultrasonic FP + Secure 2D Face                 |
| **Huawei Mate 60 Pro**       |       8.00        |   2.00 (Dual Strong)   | **10.00 / 10.0**  | 3D Face ID + Optical UD FP                     |
| **Samsung Galaxy Note 9**    |       7.00        |   2.00 (Dual Strong)   |  **9.00 / 10.0**  | Capacitive FP + Dedicated Iris Scanner         |
| **Samsung Galaxy S24 Ultra** |       8.00        |     0.00 (Single)      |  **8.00 / 10.0**  | Gen 2 Ultrasonic FP + Class 2 Face             |
| **Vivo X100 Ultra**          |       8.00        |     0.00 (Single)      |  **8.00 / 10.0**  | 3D Sonic Max FP + Class 2 Face                 |
| **Apple iPhone 16 Pro Max**  |       8.00        |     0.00 (Single)      |  **8.00 / 10.0**  | 3D Face ID only                                |
| **Google Pixel 8 Pro**       |       6.00        |   2.00 (Dual Strong)   |  **8.00 / 10.0**  | Optical UD FP + Secure 2D Face                 |
| **Xiaomi Redmi Note 13 Pro** |       7.00        |     0.00 (Single)      |  **7.00 / 10.0**  | Side Capacitive FP + Class 2 Face              |
| **Apple iPhone 8**           |       7.00        |     0.00 (Single)      |  **7.00 / 10.0**  | Front Capacitive Touch ID                      |
| **OnePlus 12**               |       6.00        |     0.00 (Single)      |  **6.00 / 10.0**  | Optical UD FP + Class 2 Face                   |
| **Samsung Galaxy A55**       |       6.00        |     0.00 (Single)      |  **6.00 / 10.0**  | Optical UD FP + Class 2 Face                   |
| **Samsung Galaxy S5**        |       1.50        |     0.00 (Single)      |  **1.50 / 10.0**  | Swipe physical fingerprint reader only         |
| **Standard budget phone**    |       0.00        |      0.00 (None)       |  **0.00 / 10.0**  | Standard 2D Face only (no fingerprint sensor)  |

> [!NOTE]
> **Regional Variant Scoring Constraint & Verification:**
> Biometric hardware configurations do not typically differ by region for standard models, unlike SIM capabilities. However, regional software differences may affect the availability of payment-grade Class 3 certification for software-based facial recognition (such as Google's Secure 2D Face).
> 
> **How to Verify and Action Regional Software Blocks:**
> The AI agent must verify regional software blocks by checking the manufacturer's official specifications or user documentation for the specific target region SKU:
> 1. If the manufacturer's regional product documentation indicates that face unlock cannot be used for Google Wallet / payment authentication in that specific market, the Face Unlock capability MUST be downgraded to standard 2D Face (0.00 points subscore).
> 2. For models targeted at regions where payment API integration is absent by default (e.g., Google Mobile Services (GMS) APIs are absent in mainland China), software-based secure Face Unlock (e.g., Pixel's secure 2D Face) MUST be downgraded to standard 2D Face (0.00 points subscore).


### 🔹 7.6 Sensors

*Description:* Evaluates the physical hardware sensor suite built into the smartphone. Sensors serve as the physical interface between device software and the real world, enabling motion tracking, spatial 3D mapping, environmental context awareness, photography assistance, and specialized health/industrial utility.
*   **Measurement:** Hardware sensor presence verified via manufacturer technical specifications, official product datasheets, and credibility-checked public spec repositories (e.g. GSMArena, PhoneArena, DeviceSpecifications, NotebookCheck).
*   **Unit:** Composite Score (0.00 to 10.00)
*   **Significance:** Critical for navigation accuracy, motion stability, High Dynamic Range (HDR) camera assist, Augmented Reality (AR) spatial tracking, indoor elevation tracking, display eye comfort, and specialized industrial/health utility.
*   **Scope:** Measures the complete publicly documented consumer smartphone hardware sensor suite.
*   **Cross-Section Non-Double-Scoring Boundaries:** To preserve strict modularity and prevent double-counting across the database architecture:
    *   *Section 4 (Camera System):* Primary, ultrawide, and telephoto image capture sensors, resolution (Megapixels), optical format sizes, lens aperture, Optical Image Stabilization (OIS), and video recording are evaluated exclusively in **Section 4**. Section 7.6 scores strictly the presence of auxiliary stand-alone hardware sensor ICs (Laser AF rangefinder diode, RGBCIR spectral sensor, LiDAR 3D scanner module), NOT camera image capture quality or lens optics.
    *   *Section 7.5 (Biometrics):* Biometric authentication hardware (fingerprint scanners, 3D Face ID structured-light emitters, Iris scanners) is evaluated exclusively in **Section 7.5**.
    *   *Section 7.7 (NFC & UWB):* Short-range wireless radios (Near-Field Communication / NFC, Ultra-Wideband / UWB) are evaluated exclusively in **Section 7.7**.
    *   *Sections 7.1–7.4 (Cellular & Wireless Connectivity):* Cellular RF transceivers, SIM slot configurations, Wi-Fi, and Bluetooth radios are evaluated exclusively in **Sections 7.1–7.4** (Barometer pressure hardware is scored in Section 7.6 strictly as a physical MEMS pressure sensor IC).

#### Terminology & Abbreviations
*   **MEMS (Micro-Electro-Mechanical Systems):** Microscopic mechanical and electro-mechanical devices fabricated on silicon chips to measure physical forces such as motion, gravity, and pressure.
*   **IMU (Inertial Measurement Unit):** A combined electronic module that measures device body motion, force, and angular rate using accelerometers, gyroscopes, and magnetometers.
*   **ALS (Ambient Light Sensor):** An optical sensor that measures surrounding illumination level to adjust screen brightness automatically.
*   **RGBCIR (Red-Green-Blue-Clear-Infrared):** Multi-channel ambient light sensors that measure visible light color spectrum and infrared radiation to assist display white balance.
*   **IR (Infrared):** Electromagnetic radiation with wavelengths longer than visible light, used in optical proximity, depth rangefinding, and non-contact thermometry.
*   **ToF (Time-of-Flight):** A depth-mapping camera technology that calculates distance by measuring the travel time of emitted light pulses to construct 3D depth maps.
*   **LiDAR (Light Detection and Ranging):** A high-resolution 3D spatial scanner using laser light pulses to generate real-time 3D point-cloud meshes.
*   **SpO2 (Peripheral Oxygen Saturation):** The percentage of oxygenated hemoglobin in blood, measured by optical pulse oximetry sensors.
*   **HRM (Heart Rate Monitor):** Optical photoplethysmography sensors that shine light into skin capillaries to measure pulse rate.
*   **VOC (Volatile Organic Compounds):** Chemical sensors measuring airborne organic pollutants and indoor air quality.
*   **FLIR (Forward-Looking Infrared):** Microbolometer thermal imaging camera technology that captures long-wave infrared (LWIR) radiation to measure temperature heatmaps.

#### Composite Scoring Formula
The final Sensors score is calculated as the sum of three distinct hardware subscore suites:

`Sensors Score = Clamp(IMU Subscore + Environmental Subscore + Advanced Subscore, 0.00, 10.00)`

The total available subscores sum to exactly **10.00 points**, matching state-of-the-art consumer flagship sensor suites, clamped strictly between **0.00** (no basic sensors) and **10.00** (complete flagship/specialized sensor array).

#### Weight Allocation Rationale & Real-World Utility Analysis
The weighting distribution across the three sensor sub-suites is calibrated against empirical user feedback, engineering analysis, and technology publication benchmarks:

*   **IMU Suite (4.50 Points / 45% Weight) — Highest Usability Impact:**
    *   *Real-World Application:* Motion tracking and angular rate sensing directly govern daily core interactions, providing high-rate physical motion telemetry for 3D mobile gaming aiming accuracy, Augmented Reality (AR) spatial placement, screen auto-rotation, and map directional heading cones (Section 7.6 scores strictly the physical MEMS sensor IC, preserving non-double-scoring separation from Section 4 camera stabilization performance).
    *   *User Pain Point:* Public reviews and technical teardowns demonstrate that devices using virtual software gyroscope emulation suffer from 50–200ms rotational latency, severe motion drift, and incompatibility with AR applications, justifying the 2.00 point valuation for physical MEMS gyroscopes.
*   **Environmental & Ambient Suite (3.50 Points / 35% Weight) — Core Display & Call Ergonomics:**
    *   *Real-World Application:* Automates display power, eye comfort, and call ergonomics through physical hardware detection of ambient light, proximity distance, atmospheric pressure, and magnetic flip covers.
    *   *User Pain Point:* User reviews highlight severe frustration with software/ultrasonic proximity emulation (e.g. Elliptic Labs audio algorithms), which cause frequent accidental cheek-muting and screen touch during calls. This validates the 1.25 point valuation for dedicated physical IR proximity hardware.
*   **Advanced Spatial, Optical & Specialized Suite (~2.00 Points / ~20% Weight) — Balanced Bonus Utility:**
    *   *Real-World Application:* Enables advanced 3D room/object scanning, low-light autofocus lock, flicker-free lighting color matching, thermal inspection diagnostics, and direct health/temperature monitoring.
    *   *Empirical Balance:* Capping this suite at ~2.00 points ensures specialized niche sensors boost flagship scores appropriately without double-scoring against Section 4 camera image capture quality or unfairly penalizing mainstream consumer flagships that omit industrial thermal or specialized health modules.

---

#### 7.6.1 Part 1: Inertial & Motion Sensing Suite (IMU) Subscore (Max 4.50 points)
Evaluates core physical motion, rotation, and direction hardware sensors. Inertial Measurement Units (IMU) provide high-rate motion data necessary for interface rotation, gaming, camera stabilization, and navigation orientation.

| Subscore  | Hardware Component & Feature Tier          | Engineering Definition & Verification Rule                                                              |
| :-------: | :----------------------------------------- | :-----------------------------------------------------------------------------------------------------= |
| **---**   | **[Sensor 1: 3-Axis Gyroscope]**           | **Rotational Motion & Angular Velocity Sensing (Max 2.00 pts)**                                         |
|  **2.00** | *Hardware 3-Axis MEMS Gyroscope*           | Dedicated physical MEMS gyro. Provides sub-ms angular velocity data for motion tracking, 3D gaming, AR. |
|  **0.00** | *Virtual Gyroscope (Software Emulation)*   | Software rotation using accelerometer + compass. High latency (50-200ms), drift, and AR incompatibility.|
| **---**   | **[Sensor 2: 3-Axis Magnetometer]**        | **Earth's Magnetic Field & Cardinal Compass Direction (Max 1.50 pts)**                                  |
|  **1.50** | *Hardware 3-Axis Magnetometer / Compass*   | Dedicated Hall-effect/magnetoresistive sensor measuring Earth's magnetic field for map cone direction.  |
|  **0.00** | *No Hardware Magnetometer / Compass Absent*| No magnetic sensor. Map apps show static location dot without heading direction cone.                   |
| **---**   | **[Sensor 3: 3-Axis Accelerometer]**       | **Linear Acceleration & Orientation Sensing (Max 1.00 pt)**                                             |
|  **1.00** | *Hardware 3-Axis MEMS Accelerometer*       | Dedicated physical MEMS accelerometer for linear acceleration, step pedometer, and screen orientation.  |
|  **0.00** | *No Accelerometer / Absent*                | Lacks basic physical acceleration sensing hardware.                                                     |

*Sub-formula:* `IMU Subscore = Gyroscope (Max 2.00) + Magnetometer (Max 1.50) + Accelerometer (Max 1.00)` (Max 4.50 pts)

##### Sensor Utility Breakdown (IMU Suite)
*   **3-Axis MEMS Gyroscope:** Measures body rotational speed and angular velocity. Useful for 3D mobile gaming motion aiming, head tracking in Augmented Reality (AR) apps, and high-frequency motion telemetry.
*   **3-Axis Magnetometer (Compass):** Measures Earth's geomagnetic field vectors. Useful for real-time cardinal directional heading (North/South/East/West) and orienting direction cones in map navigation applications.
*   **3-Axis MEMS Accelerometer:** Measures linear g-force acceleration and gravity vectors. Useful for display auto-rotation (portrait/landscape), step counting (pedometer), shake gesture shortcuts, and fall detection.

---

#### 7.6.2 Part 2: Environmental & Ambient Sensing Suite Subscore (Max 3.50 points)
Evaluates hardware sensors that detect surrounding environmental conditions (light, object distance, atmospheric pressure, magnetic covers) to automate display behavior, protect call state, and measure altitude.

| Subscore  | Hardware Component & Feature Tier          | Engineering Definition & Verification Rule                                                              |
| :-------: | :----------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **---**   | **[Sensor 1: Proximity Sensor]**           | **Display Call State & Face Distance Sensing (Max 1.25 pts)**                                           |
|  **1.25** | *Physical Hardware IR/Optical Proximity*   | Physical IR LED + photodiode under glass (<5cm). Guarantees 100% reliable call screen turn-off.         |
|  **0.00** | *Virtual Software / Ultrasonic Proximity*  | Software/ultrasonic audio algorithm (Elliptic Labs). High false call-touch rates.                       |
| **---**   | **[Sensor 2: Ambient Light & Color]**      | **Display Auto-Brightness & Color Temperature (Max 1.25 pts)**                                          |
|  **1.25** | *Hardware ALS + Hardware Color Sensor*     | Physical ALS + dedicated multi-channel ambient color sensor (Apple True Tone, RGBCIR).                  |
|  **1.00** | *Standard Hardware Ambient Light (ALS)*    | Single physical RGB/monochrome light sensor for standard auto-brightness.                               |
|  **0.00** | *Virtual / Camera-Based Light Sensing*     | Selfie camera periodic sampling or no auto-brightness capability.                                       |
| **---**   | **[Sensor 3: Atmospheric Barometer]**      | **Barometric Pressure & Elevation Lock Sensing (Max 0.75 pt)**                                          |
|  **0.75** | *Hardware Barometric Pressure Sensor*      | Physical MEMS pressure sensor (0.1 hPa). Enables stair elevation tracking and fast GNSS altitude locks. |
|  **0.00** | *No Barometer / Absent*                    | Lacks barometric pressure hardware.                                                                     |
| **---**   | **[Sensor 4: Hall Effect Sensor]**         | **Magnetic Cover & Foldable Closure Sensing (Max 0.25 pt)**                                             |
|  **0.25** | *Hardware Hall Effect Sensor*              | Physical magnetic sensor for flip covers, Moto Mods, and foldable closure state.                        |
|  **0.00** | *No Hall Sensor / Absent*                  | Lacks magnetic cover proximity hardware.                                                                |

*Sub-formula:* `Environmental Subscore = Proximity (Max 1.25) + Ambient Light (Max 1.25) + Barometer (Max 0.75) + Hall Sensor (Max 0.25)` (Max 3.50 pts)

##### Sensor Utility Breakdown (Environmental Suite)
*   **Physical IR Proximity Sensor:** Detects physical objects within <5cm of the earpiece. Useful for turning off display and touch sensing during phone calls to prevent accidental cheek muting.
*   **Ambient Light & Color Sensor (ALS):** Measures front-facing ambient room illumination lux and light spectrum color temperature. Useful for smooth automatic display brightness adaptation and screen color tint matching (e.g. Apple True Tone, RGBCIR). Strictly dedicated to display visual adaptation, separate from rear camera photo spectral sensors.
*   **Barometric Pressure Sensor (Barometer):** Measures atmospheric pressure in hectopascals (hPa). Useful for tracking flights of stairs in fitness apps and accelerating satellite GNSS 3D altitude locks.
*   **Hall Effect Sensor:** Detects magnetic field proximity. Useful for activating cover screens on foldables, Moto Mods, and magnetic flip case sleep/wake states.

---

#### 7.6.3 Part 3: Advanced Spatial, Optical & Specialized Sensing Suite Subscore (Max 2.00 points to reach total max score of 10.00 for Section 7.6)
Evaluates optional, photography-assist, 3D scanning, and specialized physiological/industrial hardware sensors.

| Subscore  | Hardware Component & Feature Tier                      | Engineering Definition & Verification Rule                                                       |
| :-------: | :----------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **---**   | **[Category A: Spatial Depth & Laser AF]**             | **3D Mesh Scanning, ToF & Camera Laser Rangefinder (Max 1.00 pt)**                               |
|  **1.00** | *Tier 1: LiDAR Scanner / 3D Spatial*                   | 3D spatial laser scanner (iPhone 12–16 Pro). 3D point-cloud mesh for instant low-light AF and AR.|
|  **0.60** | *Tier 2: 3D ToF Camera / DepthVision*                  | 3D Time-of-Flight IR depth sensor (Galaxy S10 5G/S20U, Note 10+, P30 Pro) for portrait bokeh.    |
|  **0.35** | *Tier 3: Laser Autofocus Rangefinder*                  | Dedicated IR laser rangefinder for fast low-light/macro autofocus (Pixel 2–9, S21–25U, LG G3–G8).|
|  **0.00** | *Tier 4: Standard Dual Camera / None*                  | Standard dual-camera software parallax or no optical depth hardware.                             |
| **---**   | **[Category B: Spectral & Color Assist]**              | **Multi-Channel Photography Spectral & Flicker Sensing (Max 0.50 pt)**                           |
|  **0.50** | *Dedicated Multi-Spectral Color Sensor*                | Multi-channel spectral sensor or flicker photodiode (Hasselblad, Xiaomi Ultra, Galaxy Ultra).    |
|  **0.00** | *None / Standard Camera White Balance*                 | Standard camera auto white balance without spectral or flicker hardware.                         |
| **---**   | **[Category C: Industrial & Health Suite]**            | **Active Microbolometer, Physiological & Infrared Environmental Sensors**                        |
|  **0.50** | *Tier 1: Active Microbolometer Thermal*                | FLIR/Infiray LWIR microbolometer thermal camera (CAT S60/S62 Pro, Blackview, Ulefone).           |
|  **0.35** | *Tier 2: Dedicated Physiological Suite*                | Optical Heart Rate (HRM) + Blood Oxygen (SpO2) photodiode array (Galaxy S5–S10, Note 4–9).       |
|  **0.20** | *Tier 3: Standalone Infrared Temperature Sensor*       | Non-contact infrared temperature sensor (Google Pixel 8 Pro / 9 Pro).                            |
|  **0.20** | *Tier 4: Volatile Organic Compounds Air Quality Sensor*| Dedicated VOC air quality gas sensor IC (CAT S61).                                               |
|  **0.20** | *Tier 5: Ultraviolet Sensor*                           | Dedicated UV index photodiode sensor IC (Galaxy Note 4, Galaxy S5).                              |
|  **0.00** | *Tier 6: Standard Consumer Suite / None*               | No specialized thermal, physiological, or environmental hardware sensors.                        |

*Sub-formula:* `Advanced Subscore = Spatial Depth + Spectral Assist + Industrial & Health Sensors`

##### Sensor Utility Breakdown (Advanced Suite)
*   **3D Spatial Depth & Laser AF (LiDAR / ToF / Laser Rangefinder):** Measures laser round-trip time. Useful for instant 3D room/object mesh scanning (Polycam/Canvas), low-light autofocus lock, and AR depth mapping.
*   **Multi-Spectral & Color Assist Sensor:** Measures scene light spectrum channels and AC artificial lighting flicker frequency at the rear camera array. Useful for eliminating artificial LED/fluorescent light flicker banding in photos/videos and calibrating rear camera white balance (e.g. Hasselblad, Xiaomi Ultra). Strictly dedicated to camera photo/video capture quality, separate from display ambient light sensors.
*   **Industrial & Health Suite (Thermal / Physiological / Environmental Sensors):** Measures long-wave infrared heatmaps, biological vitals, non-contact temperature, air quality, and UV levels. Useful for trade/electrical hot-spot thermal diagnostics (FLIR), pulse oximetry (SpO2/HRM), non-contact skin/surface temperature reading, VOC air quality monitoring, and UV radiation sensing. Multi-sensor feature stacking is fully supported and bounded by Section 7.6's global 10.00 pt clamp.

*Feature Stacking Rule:*
When a device incorporates multiple distinct specialized sensors (e.g. CAT S61 featuring both an Active Microbolometer Thermal Camera at 0.50 pt and a Volatile Organic Compounds Air Quality Sensor at 0.20 pt), the subscores of all detected features are additive (0.50 + 0.20 = 0.70 pts). This additive model accurately rewards multi-sensor hardware utility, with overall Section 7.6 points bounded by the master 10.00-point ceiling.

##### Architectural Analysis: Clamping Rules & Part 3 Evaluation Logic
A dedicated local clamping step to 2.00 points is intentionally **NOT required or implemented for Part 3**, based on the following two core engineering grounds:

1. **Empirical Hardware Boundary (Real-World Benchmark Limits):**
   Across the entire history of commercial mobile hardware manufacturing, real-world Part 3 subscores naturally remain far below the 2.00 pt allocation budget across all device categories:
   *   **Rugged Industrial Champion (CAT S61):** Laser Autofocus Rangefinder (0.35 pt) + FLIR Microbolometer Thermal Camera (0.50 pt) + VOC Air Quality Gas Sensor (0.20 pt) = **1.05 pts total**.
   *   **Apple iPhone Pro Series (iPhone 12 Pro through 16 Pro Max):** LiDAR Scanner (1.00 pt) + Standard White Balance (0.00 pt) + Standard Health Suite (0.00 pt) = **1.00 pt total**.
   *   **Android Ultra Flagships (Xiaomi 14 Ultra / Vivo X100 Ultra / OnePlus 12):** Laser Autofocus Rangefinder (0.35 pt) + Dedicated Multi-Spectral Color Sensor (0.50 pt) + Standard Health Suite (0.00 pt) = **0.85 pt total**.
   *   **Legacy Depth Flagships (Samsung Galaxy S20 Ultra / Note 10+):** 3D ToF DepthVision Camera (0.60 pt) + Standard White Balance (0.00 pt) + Standard Health Suite (0.00 pt) = **0.60 pt total**.
   Because commercial production devices top out at **1.05 pts** in real life, no real-world smartphone ever reaches or exceeds 2.00 points in Part 3. Applying an intermediate local clamp at 2.00 points would add zero mathematical value for any existing device.

2. **Mathematical Guarantee via Global Section 7.6 Clamping:**
   To maintain a lean schema without redundant formula overhead, overall score boundaries are strictly enforced by Section 7.6's master calculation formula:
   `Section 7.6 Score = Clamp(Part 1 Subscore + Part 2 Subscore + Part 3 Subscore, 0.00, 10.00)`
   This single global clamp mathematically guarantees that the total sensors score can **NEVER exceed 10.00 points** under any circumstances, while allowing multi-sensor industrial devices (such as CAT S61 stacking Thermal + VOC gas sensors) to be fully rewarded for their specialized hardware without artificial local suppression.


### 🔹 7.7 NFC & Ultra-Wideband (UWB)

*Description:* Evaluates short-range wireless communication and precision spatial positioning hardware. Near-Field Communication (NFC) enables touchless mobile wallet payments, public transit ticketing, smart tag scanning, and device pairing. Ultra-Wideband (UWB) pulse radio provides centimeter-accurate spatial positioning, directional item finding, and secure hands-free automotive access.
*   **Measurement:** Verification of physical NFC controller presence, UWB transceiver presence, and off-state power reserve card emulation from official manufacturer documentation and public specification sheets.
*   **Unit:** Composite Score (0.00 to 10.00)
*   **Significance:** Governs contactless payment authorization, transit pass-through speed, keyless vehicle access security against relay attacks, and directional tracking of lost items.
*   **Cross-Section Non-Double-Scoring Boundaries:**
    *   *Section 7.4 (Bluetooth & Audio Codecs):* Bluetooth Low Energy (BLE) transceivers and audio codecs are evaluated exclusively in **Section 7.4**. UWB is evaluated here strictly as a high-frequency pulse radio spatial positioning interface.
    *   *Section 7.5 (Biometrics):* Biometric transaction authorization (Fingerprint / 3D Face ID payment authorization) is evaluated exclusively in **Section 7.5**. Section 7.7 evaluates strictly the short-range radio chip and secure credential hardware presence.
    *   *Digital Wallet Software & Bank Support:* Operating system payment apps (Apple Wallet, Google Wallet, Samsung Wallet) and bank card issuer availability are software/financial services that are NOT scored here. Section 7.7 scores strictly physical hardware radio capability.

#### Terminology & Abbreviations
*   **NFC (Near-Field Communication):** A short-range wireless technology operating at 13.56 Megahertz (MHz) over distances under 4 centimeters, enabling contactless payments and tag scanning.
*   **UWB (Ultra-Wideband):** A high-frequency pulse radio technology operating between 3.1 and 10.6 Gigahertz (GHz) that measures signal Time-of-Flight (ToF) for centimeter-level spatial positioning.
*   **ToF (Time-of-Flight):** A distance measurement method calculating the exact travel time of radio pulses moving at the speed of light between devices.
*   **BLE (Bluetooth Low Energy):** A low-power Bluetooth standard used to initiate peer discovery and handshake before UWB high-precision ranging begins.
*   **RSSI (Received Signal Strength Indicator):** An estimated measure of signal power level used by Bluetooth devices to approximate relative distance without directional heading.
*   **SKU (Stock Keeping Unit):** A specific regional hardware configuration of a smartphone model.

#### Scoring Formula
The final NFC & Ultra-Wideband score is calculated as the sum of the NFC capability subscore, the UWB spatial ranging subscore, and any applicable hardware feature premiums:

`NFC & UWB Score = Clamp(NFC Capability Subscore + UWB Spatial Ranging Subscore + Depleted-Battery Power Reserve Premium, 0.00, 10.00)`

The total score is bounded strictly between a minimum of **0.00** (no NFC and no UWB hardware) and a maximum of **10.00** (full NFC + UWB + off-state power reserve card emulation).

#### 7.7.1 Part 1: NFC Hardware Capability Subscore (Max 6.00 points)
Evaluates physical Near-Field Communication (NFC) hardware controller presence for touchless payments, transit cards, tag scanning, and device pairing.

##### Why NFC Matters
Near-Field Communication operates at 13.56 Megahertz (MHz) over distances under 4 centimeters, serving as a primary daily connectivity interface that enables:
*   **Touchless Mobile Wallet Payments:** Tapping the phone at retail point-of-sale terminals via Apple Pay, Google Wallet, Samsung Wallet, or local banking apps.
*   **Public Transit Pass-Through:** Instant contact-free turnstile access on subway and bus networks using digital transit passes.
*   **Smart Tag Scanning & Device Pairing:** Reading physical RFID/NFC tags and initiating instant Bluetooth/Wi-Fi accessory pairing with a single tap.

| Subscore | NFC Hardware Configuration | Engineering Verification & Public Spec Rule                                 |
| :------: | :------------------------- | :-------------------------------------------------------------------------- |
| **6.00** | **NFC Hardware Present**   | Official specs list NFC support ("Yes"). Enables mobile payments & transit. |
| **0.00** | **No NFC Hardware**        | Official specs state NFC absent ("No" / omitted). Tap-to-pay unavailable.   |

---

#### 7.7.2 Part 2: UWB Spatial Ranging Subscore (Max 3.50 points)
Evaluates Ultra-Wideband (UWB) pulse radio presence for high-precision spatial distance ranging, directional tag finding, and hands-free keyless access.

##### Why UWB Matters
Ultra-Wideband uses Time-of-Flight (ToF) radio pulses to achieve ~10cm positioning accuracy, approximately 100× more precise than Bluetooth Low Energy (BLE). This enables:
*   **Precision Item Finding:** Directional compass guidance to lost item trackers (e.g., Apple AirTag, Samsung SmartTag+) with exact distance and 3D bearing vectors.
*   **Digital Car & Smart Lock Keys:** Secure hands-free keyless entry with spatial distance awareness to prevent signal relay theft attacks.
*   **Enhanced Point-to-Share File Transfer:** Directional device-pointing orientation for wireless peer-to-peer file sharing.
*   **Indoor Navigation:** Centimeter-accurate positioning in indoor venues where satellite GPS signals are unavailable.

| Subscore | UWB Hardware Configuration            | Engineering Verification & Public Spec Rule                                              |
| :------: | :------------------------------------ | :--------------------------------------------------------------------------------------- |
| **3.50** | **Dedicated UWB Transceiver Present** | Official specs confirm UWB presence. Enables ~10cm directional finding & keyless access. |
| **0.00** | **No UWB Hardware**                   | Official specs omit UWB. Ranging limited to BLE RSSI (~1–3m approximation).              |

---

#### 7.7.3 Part 3: Depleted-Battery Power Reserve Premium (Additive, Max +0.50 point)
Rewards hardware power routing that maintains micro-power to card emulation functions when the device battery is exhausted.

##### Why Depleted-Battery Power Reserve Matters
Solves a critical emergency pain point by allowing users to tap transit turnstile gates or unlock digital vehicle and home keys for up to 5 hours after the smartphone battery reaches 0% and shuts down the main operating system. Explicitly documented by manufacturers (e.g. Apple "Express Cards with Power Reserve", Samsung/Google offline digital key support).

| Premium   | Hardware Feature Premium                   | Engineering Verification & Public Spec Rule                                          |
| :-------: | :----------------------------------------- | :----------------------------------------------------------------------------------- |
| **+0.50** | **Off-State Power Reserve Card Emulation** | Official docs confirm transit/key taps remain functional for 5 hrs after 0% battery. |

---

> [!IMPORTANT]
> **Core Regional Hardware Rule:**
> NFC presence MUST be evaluated per specific regional Stock Keeping Unit (SKU). Many mid-range and budget smartphones (e.g. Xiaomi Redmi Note series, Samsung Galaxy A series, Motorola Moto G series, Poco series) include NFC on European, North American, and East Asian SKUs, but omit NFC on Indian, Latin American, or Southeast Asian SKUs of the exact same model name. Database entries must reflect the physical spec of the target regional SKU being evaluated. If regional SKU documentation is incomplete, automated agents must execute the fallback hierarchy defined in [proposed_data_structure.md].


### 🔹 7.8 USB Port Speed & External Display Capabilities

*Description:* Evaluates the smartphone's physical Universal Serial Bus (USB) interface, maximum wired data transfer protocol bandwidth, native external display output capability (DisplayPort Alternate Mode / DP Alt Mode), and native desktop operating system environment.
*   **Hardware vs. Cable Scope:** This section evaluates the maximum hardware capability officially supported by the smartphone device itself, NOT the data transfer bandwidth or video output capability of the bundled inbox charging cable.
*   **Measurement:** Verification of physical port connector type, USB protocol generation / transfer speed, DisplayPort Alternate Mode hardware support, and desktop software environment presence from official manufacturer technical specifications, developer documentation, hardware teardowns, and credibility-checked public spec repositories (e.g. GSMArena, PhoneArena, DeviceSpecifications, NotebookCheck).
*   **Unit:** Composite Score (0.00 to 10.00)
*   **Significance:** Governs local high-speed file transfer rates (backing up 4K/8K videos, RAW photo dumps, local system backups), direct high-bitrate video capture logging to external Solid-State Drives (SSDs), native external display output to monitors/TVs/projectors, and desktop windowed multitasking (Samsung DeX, Motorola Ready For).
*   **Cross-Section Non-Double-Scoring Boundaries:** To preserve strict modularity and prevent double-counting across the database architecture:
    *   *Section 8.2 (Wired Charging Speed & USB Power Delivery / USB-PD):* Charging wattage (e.g. 15W, 25W, 45W, 65W, 120W), charging protocol standards (USB Power Delivery / USB-PD 3.0/3.1, Programmable Power Supply / PPS, Qualcomm Quick Charge / QC, proprietary Dart/VOOC/HyperCharge), battery thermal limits, and charging times are evaluated strictly and exclusively in **Section 8.2**. Section 7.8 evaluates strictly **Wired Data Protocol Speed, Bus Bandwidth, Video Output (DisplayPort Alt Mode), and Desktop Mode Software**.
    *   *Section 6.9 (Storage Speed - UFS / eMMC / NVMe):* The internal read/write performance of the smartphone's internal storage chip (e.g. Universal Flash Storage / UFS 4.0 vs Embedded MultiMediaCard / eMMC 5.1) is evaluated exclusively in **Section 6.9**. Section 7.8 evaluates strictly the **throughput capacity of the external USB port controller and interface bus protocol**.
    *   *Section 2 (Display):* The internal smartphone display specifications (resolution, nits, panel technology, refresh rate) are evaluated exclusively in **Section 2**. Section 7.8 evaluates strictly the **external display output pipeline (DisplayPort Alternate Mode & Desktop Environment software integration)**.

#### Terminology & Abbreviations

##### 1. USB Protocols & Physical Interface Standards
*   **USB (Universal Serial Bus):** An industry standard for cables, connectors, and protocols used for physical connection, communication, and power supply between computers and mobile devices.
*   **USB-C / Type-C (Universal Serial Bus Type-C):** A 24-pin reversible physical plug connector standard supporting high-speed data, power delivery, and alternate video modes.
*   **Micro-USB (Micro Universal Serial Bus):** A legacy physical connector (5-pin Micro-B or 10-pin Micro-B) used on older and budget mobile devices.
*   **USB4:** The modern open USB protocol standard incorporating Thunderbolt specifications, supporting dynamic bandwidth sharing up to 40 Gbps.
*   **TB (Thunderbolt):** High-bandwidth hardware interface technology developed by Intel and Apple (Thunderbolt 3/4 operating at 40 Gbps) supporting PCIe tunneling and dual 4K display output.

##### 2. Display Output & Desktop Software Modes
*   **DP Alt Mode (DisplayPort Alternate Mode):** A functional extension of USB Type-C that enables dedicated physical pins inside the cable and connector to carry native DisplayPort audio and video signals directly to external displays.
*   **MHL (Mobile High-Definition Link):** A legacy High Definition video and audio interface over Micro-USB or early Type-C connectors requiring powered external active converter dongles.
*   **DeX (Desktop eXperience):** Samsung's proprietary software interface that converts a smartphone's operating system into a desktop windowed workstation environment when connected to an external screen.

##### 3. System Hardware & Storage Bus Standards
*   **SSD (Solid-State Drive):** High-speed external flash storage media using Non-Volatile Memory Express (NVMe) or Serial Advanced Technology Attachment (SATA) interfaces.
*   **PCIe (Peripheral Component Interconnect Express):** A high-speed interface standard for connecting computer peripherals directly to the processor bus.

#### Composite Scoring Formula
The final USB Port Speed & External Display Capabilities score is calculated as the sum of three independent technical subscores:

`USB Port Speed & Display Score = Clamp(Part 1 Subscore + Part 2 Subscore + Part 3 Subscore, 0.00, 10.00)`

Where:
- **Part 1: USB Protocol & Interface Speed Subscore (Max 8.00 points / 80% Weight)**
- **Part 2: Wired Display Output Subscore (Max 1.50 points / 15% Weight)**
- **Part 3: Desktop Mode Software Environment Subscore (Max 0.50 points / 5% Weight)**

The total available subscores sum to exactly **10.00 points**, bounded strictly between **0.00** (obsolete / charge-only port) and **10.00** (state-of-the-art 40 Gbps USB4/TB4 + DP Alt Mode + Native Windowed Desktop OS).

#### Weight Allocation Rationale & Real-World Utility Analysis
The weighting distribution among data transfer protocol bandwidth (Max 8.00 points), wired display output hardware (Max 1.50 points), and desktop software environments (Max 0.50 points) is calibrated against empirical user feedback, professional workflow demands, tech review emphasis, and forum discussions:

*   **USB Protocol & Bus Bandwidth (Max 8.00 Points / 80% Weight) — Primary Daily Utility:**
    *   *Real-World Application:* Directly dictates file transfer speeds for 4K/8K video backups, RAW photo libraries, and device backups to external storage or Personal Computers (PCs). For creative professionals, 10 Gbps (USB 3.2 Gen 2) throughput enables direct real-time 4K 60fps ProRes / RAW video logging to external NVMe SSDs without frame drops.
    *   *Reviewer & User Consensus:* Tech publications (GSMArena, NotebookCheck, Android Authority, The Verge) and user forums overwhelmingly highlight USB port speed as a major daily pain point. Flagship devices locked internally to legacy USB 2.0 speeds (480 Mbps), such as the base Apple iPhone 15/16 or Samsung Galaxy A series, receive heavy criticism because transferring a 50 Gigabyte (GB) 4K video project over USB 2.0 takes over 22 minutes (throttled to ~38 MB/s), compared to under 50 seconds on a 10 Gbps USB 3.2 Gen 2 port (~1000 MB/s). This validates the 8.00 point allocation for data bus bandwidth.
*   **Wired Display Output Hardware (Max 1.50 Points / 15% Weight) — Core Display Pipeline:**
    *   *Real-World Application:* Hardware DisplayPort Alternate Mode allows users to connect their smartphone directly to external monitors, TVs, or projectors via a single USB-C cable for native wired video output, presentation projection, and lag-free media viewing.
    *   *User Value:* Tech reviews and user feedback place primary emphasis on the fundamental presence of hardware video output capability (connecting a phone directly to a monitor or TV via USB-C). Whether the OS launches a specialized desktop interface is a secondary software feature. Awarding 1.50 points to native DP Alt Mode hardware reflects this core video output utility, evaluated independently of UI software implementation.
*   **Desktop Mode Software Environment (Max 0.50 Points / 5% Weight) — Specialized Workstation Bonus:**
    *   *Real-World Application:* Windowed desktop environments (Samsung DeX, Motorola Ready For, Huawei Desktop Mode, LG Screen+) transform the smartphone UI into a desktop PC layout with multi-window multitasking, desktop browser rendering, and taskbar navigation when connected to external displays.
    *   *User Value:* While highly praised by power users, desktop UI modes represent a niche feature that rarely drives primary smartphone purchasing decisions. Allocating 0.50 points rewards this software engineering achievement without distorting the core hardware ranking of devices that feature native DP Alt Mode output (e.g. Apple iPhone Pro or Google Pixel).

---

#### 7.8.1 Part 1: USB Protocol & Interface Speed Subscore (Max 8.00 points)
Evaluates physical port connector standards and hardware bus protocol data throughput ceilings across all smartphone generations.

*   **Tier 1 — 8.00 pts (USB4 / USB 3.2 Gen 2x2 / Thunderbolt-compatible | 20–40 Gbps):** **State-of-the-Art USB Tier.** Supports the highest currently available USB bandwidth for smartphones (20–40 Gbps), enabling maximum speed external storage and display connectivity.
*   **Tier 2 — 7.00 pts (USB 3.2 Gen 2 / USB 3.1 Gen 2 | 10 Gbps SuperSpeed+):** **Reference Flagship Standard.** Examples include selected flagship models (e.g. Apple iPhone 15 Pro / 16 Pro Max, Samsung Galaxy S24 Ultra, Asus ROG Phone 8 Pro, Sony Xperia 1 VI, Vivo X100 Ultra, Xiaomi 14 Ultra). Enables direct 4K 60fps ProRes / RAW SSD recording.
*   **Tier 3 — 5.50 pts (USB 3.2 Gen 1 / USB 3.1 Gen 1 / USB 3.0 | 5 Gbps SuperSpeed):** **Standard Flagships & Mid-Range.** Examples include selected flagships and upper mid-range models (e.g. Google Pixel 8 Pro / 9 Pro, Samsung Galaxy S24 base, OnePlus 12, Motorola Edge 50 Pro) supporting USB 3.2 Gen 1 (5 Gbps). Fast media transfer without severe bus throttling.
*   **Tier 4 — 4.50 pts (USB 3.0 10-pin Micro-B | 5 Gbps SuperSpeed):** **Legacy USB 3.0 Micro-B Devices.** Examples include legacy dual-plug models (e.g. Samsung Galaxy Note 3, Samsung Galaxy S5). High-speed USB 3.0 bus via 10-pin Micro-B connector (reduced score due to fragile 10-pin plug design and lack of cable ecosystem).
*   **Tier 5 — 2.50 pts (USB 2.0 High Speed over USB Type-C | 480 Mbps):** **Mainstream Mid-Range & Base iPhones.** Examples include mainstream models (e.g. Apple iPhone 15 base / 16 base, Samsung Galaxy A55, Xiaomi Redmi Note 13 Pro, Poco X6 Pro). Reversible Type-C convenience for charging/syncing.
*   **Tier 6 — 2.25 pts (USB 2.0 High Speed over Apple Lightning | 480 Mbps):** **Legacy Apple iPhones (2012–2022).** Examples include 8-pin Lightning models (e.g. Apple iPhone 14 Pro Max, iPhone 13, iPhone 12). Reversible 8-pin connector locked to USB 2.0 speed (minor penalty vs Type-C reflects connector ecosystem isolation rather than protocol bandwidth).
*   **Tier 7 — 1.50 pts (USB 2.0 High Speed over 5-pin Micro-USB | 480 Mbps):** **Legacy Budget Androids (2016–2022).** Examples include legacy budget models (e.g. Samsung Galaxy J7, Xiaomi Redmi 9A, Motorola Moto G6 Play). Non-reversible plug, reduced connector durability, obsolete cable ecosystem (protocol speed is standard 480 Mbps).
*   **Tier 8 — 0.00 pts (Micro-USB 1.1 / Charge-only pinout / Legacy 30-pin | < 12 Mbps / None):** **Obsolete Feature Phones & Legacy Devices.** Devices lacking standard USB data controller implementation or locked to charge-only lines.

*Sub-formula:* `Part 1 Subscore = Assigned Protocol Tier Subscore` (Max 8.00 pts)

---

#### 7.8.2 Part 2: Wired Display Output Subscore (Max 1.50 points)
Evaluates physical video output pipeline hardware over the USB port. Part 2 evaluates hardware presence of native video output capability only, independent of UI implementation or supported display resolution.

*   **Tier 1 — 1.50 pts (Native DisplayPort Alternate Mode / Direct USB-C Video Output):** Native DisplayPort Alternate Mode (DP Alt Mode) over USB Type-C for direct native video output to external monitors, TVs, and projectors.
*   **Tier 2 — 0.75 pts (Legacy Wired Display Output / MHL / SlimPort):** Legacy wired display technologies (Mobile High-Definition Link / SlimPort) over Micro-USB or early Type-C requiring dedicated active converter adapters and offering lower compatibility than DisplayPort Alt Mode (1080p limit).
*   **Tier 3 — 0.00 pts (No Wired Video Output / Audio / Data / Charge Only):** Lacks DisplayPort multiplexing hardware. Video output unsupported over native USB cable. Requires wireless casting (Miracast/Chromecast) or DisplayLink active adapters.

*Sub-formula:* `Part 2 Subscore = Assigned Display Tier Subscore` (Max 1.50 pts)

---

#### 7.8.3 Part 3: Desktop Mode Software Environment Subscore (Max 0.50 point)
Evaluates native operating system software support for windowed desktop workstation environments when connected to external displays.

*   **Tier 1 — 0.50 pt (Native Windowed Desktop OS Environment):** Native operating system desktop interface (Samsung DeX, Motorola Ready For, Huawei Desktop Mode, LG Screen+) featuring windowed multitasking, taskbar, desktop browser rendering, and desktop mouse/keyboard interface.
*   **Tier 2 — 0.00 pt (No Native Desktop OS Mode):** Lacks native windowed desktop operating system mode (standard screen mirroring, casting interfaces, PC companion utilities like PC Connect, or media playback UI only).

*Sub-formula:* `Part 3 Subscore = Assigned Desktop Tier Subscore` (Max 0.50 pt)


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
   - *Reason for Removal:* DXOMARK (a commercial technology testing laboratory) publishes a composite battery score. However, this score is heavily weighted toward charging speeds and charging efficiency. Since charging speeds are already evaluated in Section 8.2 (Wired Charging) and Section 8.3 (Wireless Charging), including DXOMARK here would double-count charging capabilities and distort the endurance-only metric. Additionally, its database has limited coverage and relies on proprietary testing parameters that are not open or reproducible.
3. **Establishment of GSMArena as the Canonical Source:**
   - *Reason:* GSMArena (a global mobile technology publication) features the most comprehensive, standardized, and publicly available smartphone battery testing database in the world, covering major, minor, and regional brands. This provides a single, clean, and highly reliable target for real-world validation.

##### 8.1.1.2 Unified Active-Equivalent Hours (T_unified)
GSMArena (Global System for Mobile Communications Arena) updated its battery testing protocol in November 2023 from Version 1.0 (v1.0), which reported an "Endurance Rating" (ER) in hours, to Version 2.0 (v2.0), which reports a standardized "Active Use Score" (AUS) in hours.

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
To map devices into a dimensionally homogeneous coordinate system where every dimension is expressed in Watts (W), we measure how much the target device (the phone being scored) differs from a candidate neighbor device (a reference phone in our database). Specifically, we combine the differences in their three effective power demand components—display (`Diff_P_display_eff`), processing platform (`Diff_P_soc_eff`), and connectivity module (`Diff_P_connectivity_eff`)—with a fourth component representing the equivalent battery power difference (`Diff_P_battery_equiv`). This fourth component converts the difference in nominal battery energy capacity (`E_supply_target - E_supply_neighbor`) between the target and the neighbor into an equivalent power draw delta.

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
   The difference in sequential time-weighted connectivity power consumption (Cellular and Wireless Fidelity, or Wi-Fi) scaled by software and thermal overheads:
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
Evaluating a smartphone's battery life based solely on its charge capacity in milliampere-hours (mAh) is incomplete because it ignores operating voltage variations and the device's actual power consumption. A phone with a large battery capacity and a high-draw display or an inefficient chipset can deplete its energy reserves much faster than a device with a smaller battery capacity but a highly optimized hardware and software stack.

To resolve this, Method C establishes the physical supply/demand equations for the smartphone. It characterizes a smartphone's battery endurance using the physical relationship between electrical energy storage and average power consumption under a standardized mixed-use workload. It calculates the theoretical active endurance hours (`T_predicted`) and converts them to a predicted score.

##### 8.1.3.1 The Fundamental Equation
The relationship between battery capacity (Supply) and average power consumption (Demand) is defined as:
`T_predicted = E_supply / P_demand`
- **Endurance Hours (T_predicted):** The predicted runtime in hours under active mixed-use conditions.
- **Supply (E_supply, in Watt-hours - Wh):** The total energy capacity of the battery.
- **Demand (P_demand, in Watts - W):** The average electrical power consumed by the device under active mixed-use conditions (web browsing, media streaming, voice calls, user interface interaction, and background synchronization).

##### 8.1.3.2 Supply Modeling (E_supply)
The total nominal stored energy capacity `E_supply` (in Watt-hours - Wh) is derived as:
`E_supply = (Capacity_mAh * V_nominal) / 1000`

> [!NOTE]
> For the complete, authoritative determination logic governing nominal battery voltage (`V_nominal`), battery cell architecture classification (1S, 2S, 3S+, 1S2P), effective voltage overrides, and multi-tier evidence fallbacks, refer to [proposed_data_structure.md Section 8.1].

##### 8.1.3.3 Demand Modeling (P_demand)
Average power demand is modeled as the sum of hardware-governed display panel draw and software-scaled processing/connectivity active loads, scaled globally by the system's thermal efficiency factor:
`P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead`

*Rationale:* Software efficiency and background bloatware (`F_software_overhead`) affect processor cycle utilization and cellular/Wi-Fi radio sync duty cycles, but they do not physically alter the raw power consumed by the display panel's hardware to emit light. Restricting the software overhead multiplier to `P_soc + P_connectivity` ensures that display panel base power is not artificially scaled by software bloat, maintaining a physically accurate power model.

Conversely, the thermal overhead is composed of two separate physical phenomena that are accounted for independently:
1. **Joule Heating and Battery Resistance Losses:** As total current drawn from the battery increases, the voltage drops across the cell's internal resistance, causing power loss inside the battery itself (Joule heating). Since all components draw current from the same battery, this physical loss scales with the entire power draw. It is therefore modeled as a global multiplier (`F_thermal_overhead`) applied to the overall system-level `P_demand`.
2. **Semiconductor Static Leakage:** Elevated temperatures exponentially increase subthreshold static leakage currents within the active silicon dies (predominantly the SoC CPU and GPU blocks). This is a component-specific leakage that does not affect the display panel or connectivity modules. It is modeled locally inside `P_soc` via the `F_node_static` multiplier on the CPU background/idle baseline, rather than as a global factor.

###### 8.1.3.3.1 Display Power Demand (P_display)
The display screen power demand is modeled as a function of physical surface area, panel technology, dynamic refresh rate, and resolution:
`P_display = display_surface_area_cm2 * C_panel * F_refresh * F_resolution`

- **Display Surface Area (display_surface_area_cm2):**
  Calculated using the physical screen diagonal and aspect ratio:
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
  - *Weight Rationale:* The 65/35 weighting represents the average duty cycle of an adaptive display, where the screen operates in its static or lowest refresh state (`min_hz`) approximately 65% of the time (e.g., reading text, viewing static images) and ramps up to its peak rate (`max_hz`) during the remaining 35% of active motion or touch interaction (e.g., scrolling, transitions, gaming).
  `F_refresh = 1.0 + 0.0025 * (effective_hz - 60.0)`
  - *Range of Variation:* Under typical configurations, the effective screen refresh rate in Hertz (Hz) ranges from 10 Hz (highly optimized adaptive screens under static displays) to 144 Hz (high-performance gaming screen rates). This yields a factor range of **0.875 to 1.210** (representing a -12.5% reduction to a +21.0% increase in display base power consumption).
  - *Justification:* Active screen redrawing incurs electrical power overhead in both the panel itself and the display driver integrated circuit (IC). Dynamic refresh rates (e.g. Low-Temperature Polycrystalline Oxide (LTPO) panels dropping to 1 Hertz (Hz) during static content) yield an effective average rate below 60 Hz, reducing power demand (`F_refresh < 1.0`). Conversely, high-refresh-rate gaming or scrolling at 120 Hz or 144 Hz increases dynamic draw.
- **Resolution Factor (F_resolution):**
  Adjusts power demand based on pixel density:
  `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0)`
  - *Range of Variation:* For screen resolutions ranging from a basic High Definition (HD) baseline of 1.0 Megapixel (MP) to extreme 4K Ultra High Definition (UHD) resolutions of 8.3 Megapixels (MP), this factor ranges from **0.975 to 1.1575** (representing a -2.5% reduction to a +15.75% increase in display base power consumption).
  - *Justification & Centering:* The resolution factor is centered around a standard baseline of 2.0 Megapixels (MP), which corresponds to standard Full High Definition (FHD) resolution (the global industry-standard reference for mobile display driver Integrated Circuits (ICs) and panel power calibration). Lower-resolution screens receive a slight efficiency bonus (`F_resolution < 1.0`) due to wider subpixel aperture ratios (where a larger percentage of the subpixel's physical area emits light rather than being blocked by control wiring). Higher-resolution QHD+ or 4K screens receive a penalty (`F_resolution > 1.0`) because they have narrower aperture ratios (where more of the screen area is occupied by dense, light-blocking control wiring), requiring higher driving currents to achieve the same screen brightness, while also incurring greater data bus and Graphics Processing Unit (GPU) rendering overhead.

###### 8.1.3.3.2 System-on-Chip (SoC) Power Demand (P_soc)
The System-on-Chip (SoC) power draw represents the processing platform's consumption. We directly anchor our model in the physical logic board parameters defined in Section 6.10:
`P_soc = power_static_base * F_static_cpu * F_node_static + coefficient_soc_utilization * power_peak_soc * F_active_cpu * F_gpu * F_node_active`

- **Static Base Power (power_static_base = 0.40 W):**
  The logic board baseline power consumption in Watts (W), representing static leakage currents, Power Management Integrated Circuit (PMIC) voltage conversion efficiency losses, and baseline memory interface active overhead under low-load mixed scenarios (as defined in Section 6.10).
- **SoC Mixed-Use Utilization Factor (coefficient_soc_utilization = 0.0150):**
  A unitless, dimensionless ratio representing the average active duty cycle or utilization fraction (1.50%) of the System-on-Chip (SoC) under standard mixed daily usage.
  - *Justification for the 1.50% Scaling Factor (Empirical Calibration):* To ensure our predictive formula (Method C) aligns with physical reality and empirical benchmark testing (Method A, specifically the GSMArena Active Use Score), we conducted a comparative cross-device analysis:
    1. **Flagship Benchmark Calibration (Galaxy S24 Ultra):** Under Method A, the S24 Ultra (Snapdragon 8 Gen 3, 5000 mAh, 14.0 W Peak SoC) achieves an active endurance of ~13.8 hours, implying an average total system power draw of ~1.39 W. Deducting the physical power drawn by the display, baseboard, and modem yields an empirical average SoC power of ~0.55 W to 0.70 W. A coefficient of `0.0150` (1.50%) predicts an active dynamic SoC penalty of ~0.18 W (yielding a total SoC draw of ~ 0.40 + 0.18 = 0.58 W), which aligns well with this empirical data. A lower coefficient (e.g., under 1.00%) would predict an active dynamic SoC penalty of under 0.10 W, severely underestimating the actual energy consumed during active workloads.
    2. **Workload Discrepancy Physics:** A 1.50% utilization factor is physically necessary because real-world workloads are *not* constant across different device tiers. While a flagship processor completes basic tasks quickly and idles ("Race-to-Sleep"), standard benchmarks (and real users) push flagship hardware harder: games render at 120 frames per second (fps) with high graphics settings (compared to 60 fps on budget phones), and websites render with smoother scrolling and higher asset limits. Consequently, the flagship's active duty cycle sits at approximately 1.50% of its massive peak capacity under mixed-use testing, rather than a deep-idle state.
    3. **Budget Benchmark Calibration (Galaxy A15 4G):** For budget phones like the A15 4G (Helio G99, 4.5 W Peak SoC), the physical active penalty is naturally smaller. A 1.50% coefficient adds only ~0.10 W of active penalty, keeping the total SoC estimate safely anchored by the static baseline leakage (power_static_base). This accurately maintains the efficiency scaling between flagship and budget classes without over-penalizing simpler hardware.
  - *Note on Modifier Application (Low-Load Efficiency Scaling):* While peak power (`power_peak_soc`) already includes the raw process node and microarchitectural efficiencies under 100% capacity (which is why multipliers are omitted in Section 6.10 to prevent double-counting), we must apply the respective efficiency multipliers (specifically `F_static_cpu * F_node_static` to the static base and `F_active_cpu * F_gpu * F_node_active` to the active dynamic segment) under low-load conditions because the efficiency gap between processors is **not scale-independent**. In fact, this gap is significantly wider at low utilization due to low-power operating physics:
    1. **The Voltage Floor Handicap:** Modern flagships on 3nm nodes scale voltage down to approximately 0.6 Volts (V) during light tasks. Legacy nodes are limited to a voltage floor of approximately 0.85 Volts (V) due to leakage instability. Since dynamic power scales with the square of voltage (V^2), legacy chips draw far more energy per cycle at low load than their peak power ratio would suggest.
    2. **Power-Gating & Core Scheduling:** Flagships aggressively power-gate unused cores or Neural Processing Units (NPUs) and schedule light tasks onto high-efficiency cores that complete tasks quickly and sleep (high dynamic "Race-to-Sleep" efficiency). Budget chips lack fine-grained power gating and have lower Instructions Per Cycle (IPC), forcing them to remain in active states longer.
    *Conclusion (Capacity Correction):* As a consequence of these low-load physics, simply scaling peak power linearly (`0.0150 * power_peak_soc`) would predict that a 19.5 W flagship draws 4x more power at low load than a 4.5 W budget chip, which is physically false. The efficiency multipliers therefore act as low-load capacity correction factors, adjusting the capacity-based term to prevent unfairly penalizing high-capacity, highly optimized processors.
- **Peak SoC Power (power_peak_soc):**
  The peak thermal design power of the chipset in Watts (W) sourced from the canonical reference (references/soc_reference.md).
- **Decoupled Process Node Factors (F_node_static and F_node_active):**
  Rather than applying a single global factor to the entire SoC power draw, the physical model applies decoupled process node multipliers to the static (idle) and active (dynamic) components separately to account for how different silicon domains scale.
  Here, `process_nm` represents the chipset's physical fabrication node size in nanometers (nm) (e.g., 3, 4, 5, 7, 12, etc.), and 3.0 nm represents the baseline reference.

  - *Mathematical Derivation of the Linear Scaling Exponent (alpha_silicon = 1.0):*
    1. **Power Consumption per Generation Step:**
       We model the active silicon (chip-level) power consumption P of the chip changing by a constant percentage per generation. Moving forward (scaling down) by one generation step reduces active silicon power draw by a constant fraction delta (the active chip-level efficiency gain per step), so the power at generation n+1 is:
       `P_n+1 = P_n * (1 - delta)`
       After k generations of scaling, the power becomes:
       `P = P_0 * (1 - delta)^k`
    2. **Geometric Node Size Scaling:**
       Historically, semiconductor gate feature sizes scale down geometrically by a constant shrinkage factor r per generation step. Therefore, the process node size s after k generations is:
       `s = s_0 * r^k`
       To express the generation count k in terms of the node sizes, we divide by s_0 and take the natural logarithm of both sides:
       `s / s_0 = r^k`
       `ln(s / s_0) = k * ln(r)`
       `k = ln(s / s_0) / ln(r)`
    3. **Derivation of the Power-Law Relationship:**
       Substituting the expression for the generation count k back into the power equation:
       `P = P_0 * (1 - delta)^(ln(s / s_0) / ln(r))`
       Since `e^ln(x) = x`, we can rewrite the term using base e:
       `P = P_0 * e^(ln(s / s_0) * (ln(1 - delta) / ln(r)))`
       `P = P_0 * (e^ln(s / s_0))^(ln(1 - delta) / ln(r))`
       `P = P_0 * (s / s_0)^(ln(1 - delta) / ln(r))`
       This mathematically proves that a constant percentage efficiency gain per generation implies a power-law relationship:
       `P / P_0 = (s / s_0)^alpha_silicon`
       where the scaling exponent alpha_silicon is:
       `alpha_silicon = ln(1 - delta) / ln(r)`
    4. **Numerical Verification:**
       Silicon foundries typically disclose that each major process generation transition achieves an average active silicon power reduction of **30%** (delta = 0.30) under constant performance, alongside a geometric gate shrinkage factor of **r = 0.70**. Substituting these values:
       `alpha_silicon = ln(1 - 0.30) / ln(0.70) = ln(0.70) / ln(0.70) = 1.0`
       This proves that the active silicon power scaling exponent is ~ **1.0**, which physically anchors the linear scaling term `(process_nm / 3.0)^1.0` (or simply `(process_nm / 3.0)`) used for the process-dependent logic paths.

  - *Linear Partitioning Formulations:*
    Using the derived active silicon scaling exponent of 1.0, the total system-level SoC power is partitioned into process-independent and process-dependent logic components in both the idle and active regimes:
    `F_node_static = 0.80 + 0.20 * (process_nm / 3.0)`
    `F_node_active = 0.65 + 0.35 * (process_nm / 3.0)`

  - *Justification for Static (Idle) Scaling (80% Independent / 20% Dependent):*
    Under low-load or idle conditions, the high-performance CPU and GPU logic execution blocks are completely power-gated (shut down using sleep transistors). The static leakage power is dominated by Static Random Access Memory (SRAM) cache data retention arrays, always-on peripheral clock grids, and baseline power management conversion overhead. These components are largely independent of process node size. Based on typical mobile System-on-Chip (SoC) power breakdowns under low-load operation, approximately **20%** of idle power is assumed to originate from process-sensitive leakage (subthreshold leakage of active wake-up control logic and refresh circuitry), while the remaining **80%** is treated as process-independent. These splits are calibrated engineering approximations informed by empirical SoC power characterization data, and cross-validated against real-device battery endurance measurements spanning the full 3–20 nm node range — not quantities derivable directly from semiconductor physics.
  - *Justification for Active (Non-Idle) Scaling (65% Independent / 35% Dependent):*
    Under active processing load, approximately **35%** of the total System-on-Chip (SoC) active power is assumed to scale with the fabrication node (active dynamic switching capacitance of the compute logic gates), while the remaining **65%** arises from node-insensitive subsystems: high-speed I/O pads driving external memory buses, clock distribution buffers, analog phase-locked loops (PLLs), power management circuitry, and board interconnect capacitances. These interface and clock structures are constrained by physical wire geometry and layout rules and do not significantly improve with process shrink. As with the static split, these percentages are calibrated parameters rather than first-principles results; they have been tuned to produce agreement with empirical battery endurance benchmarks across a representative cross-section of flagship, budget, midrange, and legacy devices.
  - *Range of Variation:*
    - For `F_node_static`: Ranges from **1.000** (at 3nm) to **2.133** (at 20nm, representing a +113.3% static leakage penalty).
    - For `F_node_active`: Ranges from **1.000** (at 3nm) to **2.983** (at 20nm, representing a +198.3% active dynamic power penalty).
  - *Physical Significance of the 3.0 nm Reference Baseline:*
    The 3.0 nm reference baseline represents the peak of commercial silicon optimization for modern fabrication nodes. The linear scaling natively supports future sub-3nm nodes (such as 2.0 nm or 1.8 nm), where the ratio `(process_nm / 3.0)` is less than 1. In such cases, both multipliers fall below 1, representing additional power-saving gains.
  - *Exclusion of Foundry-Based Process Node Bonuses:* Sourcing process node efficiency purely from the physical transistor gate length in nanometers (nm) via decoupled static and active factors removes subjective foundry-based weightings (such as favoring Taiwan Semiconductor Manufacturing Company (TSMC) over Samsung or Intel) and data availability issues. This keeps the model strictly objective, neutral, and verifiable, avoiding speculative adjustments based on the manufacturing foundry. This is justified by the fact that the fabrication foundry (and its subtle differences in cell libraries or layout) is estimated to represent only about **10%** of the node's total efficiency influence.

- **CPU Static and Active Architecture Factors (F_static_cpu and F_active_cpu):**
  Rather than applying a single global multiplier to the combined base and active SoC power, the physical model decouples the static board leakage and active dynamic draw, scaling them independently:
  `F_static_cpu = 1.0 + 0.04 * (10.0 - CPU_Background_Score)`
  `F_active_cpu = 1.0 + 0.04 * (10.0 - CPU_Active_Score)`
  
  - *Range of Variation:* With both efficiency scores ranging from 0.00 (representing minimum microarchitectural efficiency) to 10.00 (representing peak efficiency), both multipliers range from **1.000 to 1.400** (representing a 0% baseline penalty to a +40.0% increase in their respective System-on-Chip (SoC) power components).
  - *Unified Rationale for Linear (Performance) Scores:*
    Section 8.1 is a **quantitative physical model** simulating real power demand (in Watts) and battery capacity (in Watt-hours) to predict battery life (in hours) before linearly normalizing the resulting runtime. In physics, electrical power scales linearly with physical attributes (e.g., dynamic power P ≈ C * V^2 * f, and static leakage scales linearly with transistor width and cache area). Incorporating logarithmically compressed (perceptual) scores into a physical power model breaks linear scaling. **Therefore, all CPU score inputs in the Section 8.1 physical model must be strictly normalized linear performance/architectural scores, NOT logarithmically compressed perceptual scores.** Both component scores are clamped strictly to `[0.00, 10.00]` to guarantee mathematical safety.
  - **`CPU Background Score` (CPU_Background_Score):**
    `CPU_Background_Score = clamp(idle_efficiency_score, 0.00, 10.00)`
    - Sourced directly from the **Idle Efficiency Score** column of the §6.1.0 CPU Core Architecture Reference Table for the lowest-performing (smallest) active core cluster on the SoC.
    - *Physical Justification:* Cores optimized for standby and lightweight operations (Cortex-A520/A525, Apple Sawtooth) feature ultra-narrow pipelines, tiny caches, and advanced power-gating, yielding a score close to `10.00` (zero leakage penalty). Large cores (Qualcomm Oryon Gen 2, Cortex-X4, Apple Everest) have wider pipelines, massive L2 caches, and higher transistor counts, yielding a score close to `0.00` (maximum leakage penalty). Older efficiency cores (Cortex-A55, Cortex-A53) lack advanced voltage scaling floors and power gating, receiving intermediate scores (`8.00` and `7.00`) to reflect their higher standby leakage.
  - **`CPU Active Score` (CPU_Active_Score):**
    `CPU_Active_Score = clamp(0.35 * CPU_Burst_Score + 0.65 * CPU_Sustained_Score, 0.00, 10.00)`
    - **`CPU_Burst_Score`**: Sourced from Section 6.2 (CPU Single-Core Performance), normalized linearly to preserve physical power scaling:
      `CPU_Burst_Score = 10.0 * (CY - CPU_STRS_Score_Min) / (CPU_STRS_Score_Max - CPU_STRS_Score_Min) clamped 0-10.`
      - Where `CY` is the Core Yield from Section 6.2, representing the single-core burst capability including frequency scaling and microarchitectural Instructions Per Cycle (IPC).
      - **Physical Modeling of Frequency and Race-to-Sleep:** Including clock frequency scaling (f) directly in the burst score is physically necessary to capture "Race-to-Sleep" efficiency. A higher burst frequency allows the CPU to execute tasks much faster, returning the core to low-power static idle states sooner and minimizing the integration time of static leakage power. This frequency-aware performance benefit is balanced by `power_peak_soc`, which captures the cubic dynamic power penalty (P ∝ f^3) of higher clock speeds.
    - **`CPU_Sustained_Score`**: Sourced from Section 6.1, normalized linearly to preserve physical power scaling:
      `CPU_Sustained_Score = 10.0 * (RCTS - CPU_RCTS_Min) / (CPU_RCTS_Max - CPU_RCTS_Min) clamped 0-10.`
      - Where `RCTS` is the Raw CPU Throughput Score from Section 6.1, representing the aggregate throughput efficiency of all active cores under multi-threaded saturation.
    - **Justification for Using Calculated Method C Scores Across All Devices:** To maintain database integrity and physical consistency, the battery model uses the calculated/predicted performance scores from Method C (the analytical Core Yield (CY) and Raw CPU Throughput Score (RCTS)) for all devices, rather than sourcing from the final database score columns (which may contain empirical Method A benchmark scores or interpolated Method B scores). If Method A benchmark scores were used for benchmarked devices, then unbenchmarked devices would have to use either Method B or Method C. However, Method B (Nearest Neighbor Interpolation) operates on logarithmically compressed perceptual scores rather than linear physical performance scores. Adapting the interpolation model of Method B to also calculate and output raw linear performance scores would significantly increase the complexity of the framework. Conversely, falling back directly to Method C for unbenchmarked devices (bypassing Method B) would introduce systematic biases and variance between devices scored via empirical benchmarks and those scored via analytical predictions. Sourcing the linear performance inputs (`CPU_Burst_Score` and `CPU_Sustained_Score`) strictly from the Method C calculation equations for all devices ensures a neutral, consistent, and unbiased physical power model that scales uniformly across the entire database.
    - **Justification for Neglecting Cache and Memory Subsystem Penalties in Section 8.1:**
      In this physical model, `CPU_Burst_Score` and `CPU_Sustained_Score` are calculated from the raw, unpenalized performance variables (`CY` and `RCTS`). Subsystem penalties from Section 6.1 (such as `Penalty_CFEI` and `Penalty_MTI`) and Section 6.2 (such as `Penalty_L2CS` and `Penalty_MTI`) are neglected. Note that the multi-core thermal throttling penalty (`Penalty_TDSI`) is also excluded here, but for a different reason: Section 8.1 already has its own dedicated `F_thermal_overhead` multiplier that globally models thermal inefficiency on power demand, so including `Penalty_TDSI` would double-count the same physical effect.
      This is a mathematically and physically sound approximation because the impact of these performance penalties on average active power demand is negligible, which is verified by analyzing the worst-case scenario:
      1. **Worst-Case Core Penalty Hypothesis (0.8 point):** For the reference Samsung Galaxy S24 Ultra (Snapdragon 8 Gen 3, LPDDR5X, 18 MB shared cache), the actual cache and memory penalties are: Section 6.2 single-core: `Penalty_L2CS` = 0.34 points + `Penalty_MTI` = 0.01 points = **0.35 points total**; Section 6.1 multi-core (excluding `Penalty_TDSI`): `Penalty_MTI` ≈ 0.00 points + `Penalty_CFEI` ≈ 0.00 points = **< 0.01 points total**. We deliberately assume a **worst-case penalty of 0.8 point** applied uniformly to both single-core burst and multi-core sustained scores. This represents an extremely conservative upper bound that covers all devices in the database, including low-end and legacy chipsets which suffer from severe memory bandwidth bottlenecks and minimal cache allocations.
      2. **Active Score Impact:** A 0.8-point reduction in both scores translates directly to a 0.8-point drop in `CPU_Active_Score` (since it is a linear combination: `0.35 * 0.8 + 0.65 * 0.8 = 0.8`).
      3. **CPU Active Multiplier (F_active_cpu) Impact:** The CPU Active Architecture Factor is calculated as:
         `F_active_cpu = 1.0 + 0.04 * (10.0 - CPU_Active_Score)`
         An offset of 0.8 point in `CPU_Active_Score` shifts `F_active_cpu` by an absolute delta of:
         `ΔF_active_cpu = 0.04 * 0.8 = 0.032`.
         Since `F_active_cpu` is always >= 1.0, this absolute shift of `0.032` translates to a conservative relative dynamic active workload power increase of at most **3.2%** (which occurs in the worst case when `F_active_cpu` is at its minimum of `1.0`).
      4. **P_soc Dynamic Power Impact:** Critically, `F_active_cpu` only scales the **dynamic active workload** portion of `P_soc`, not the entire SoC power draw. The `P_soc` formula decomposes into two physically distinct terms:
         - **Static baseboard leakage** = `0.40 * F_static_cpu * F_node_static` ≈ 0.43 W (for the reference Samsung Galaxy S24 Ultra) — this represents always-on silicon leakage and is **completely unaffected** by CPU performance penalties.
         - **Dynamic active workload** = `0.0150 * Power_Peak_SoC * F_active_cpu * F_gpu * F_node_active` ≈ 0.27 W (for the reference Samsung Galaxy S24 Ultra) — only this term is scaled by `F_active_cpu` and is therefore the only portion affected by the neglected penalties.
         Applying the conservative 3.2% increase shifts only this dynamic portion by: `3.2% * 0.27 W ≈ 0.009 W (9 milliwatts)`.
      5. **Total Power Demand (P_demand) Impact:** Under typical mixed use, the total power draw `P_demand` is calculated as:
         `P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead`
         `P_demand = (0.4037 W + (0.6981 W + 0.0710 W) * 1.0730) * 1.0246 ≈ 1.26 W`.
         The 9 mW SoC power increase propagates through the software and thermal modifiers to shift `P_demand` by:
         `0.009 W * 1.0730 * 1.0246 ≈ 0.010 W` (10 mW), representing a negligible relative increase of under **0.8%** on the total power draw.
      6. **Endurance Time (T_predicted) Impact:** For a typical 5000 mAh battery (≈ 19.25 Wh of energy capacity), a < 0.8% shift in power demand translates to a runtime difference of less than **8 minutes** (shifting predicted runtime from 15.29 hours to 15.17 hours) and a battery score shift of less than **0.1 points** on the 10-point scale. This is well below the standard 2% to 5% experimental margins of real-world battery endurance tests, proving that the neglect hypothesis is completely sound for both Section 6.1 and 6.2 inputs.
      7. **Implementation Complexity Trade-Off:** While incorporating cache/memory penalties would offer minor precision gains, doing so would require adding significant layers of mathematical complexity:
         - The system would have to perform complex "reverse-logarithmic" equations inside Section 8.1 to mathematically "undo" the logarithmic compression of the final 6.1 and 6.2 scores to extract penalized raw capacity scores.
         - The system would also need to isolate and strip out the multi-core thermal throttling penalty (`Penalty_TDSI`) from the multi-core score to prevent double-counting with Section 8.1's dedicated global `F_thermal_overhead` multiplier.
         At this stage, the induced mathematical complexity is not worth the trade-off for the negligible performance impact of under 0.8% on predicted runtimes. However, implementing these penalty terms directly into the linear power formulas remains a potential area for future model improvement.
  - *Derivation of Dynamic Active CPU Weights (35% Burst / 65% Sustained):*
    The active use score composites four equal tests: calls over 4G/VoLTE (20% time share), web browsing (30%), video streaming (30%), and 3D gaming (20%).
    1. *Calls and Video (50% combined time):* CPU operates in a low-intensity scheduling state where dynamic active power is negligible compared to modem and display draw.
       - *Physical Modeling Justification:* Although this 50% time share has negligible dynamic active CPU power (and thus receives a 0% weight in the active dynamic CPU weight derivation), it is fully accounted for in the global battery model:
         - **Leakage (Static) Component:** During this low-intensity state, the CPU's static leakage power remains fully active and is scaled by the `CPU_Background_Score` (`F_static_cpu` multiplier on the static baseboard power `power_static_base`).
         - **Dynamic Active Component:** The negligible dynamic draw during this phase mathematically reduces the time-weighted average dynamic active CPU consumption. This is directly reflected in the low overall SoC utilization coefficient (`coefficient_soc_utilization = 0.0150`), which averages the active dynamic power of all phases (including the 0 W active dynamic draw of the Calls and Video phases) over the entire test duration.
    2. *Web Browsing (30% time):* Browser rendering triggers brief, high-performance CPU bursts. Sourced from empirical profiling, average active dynamic CPU power = `0.15 W`.
        `E_burst = 0.30 (time share) * 0.15 W = 0.045 Wh-equivalent`
    3. *3D Gaming (20% time):* CPU sustains multi-core load feeding the GPU. Average dynamic active CPU power = `0.40 W`.
        `E_sustained = 0.20 (time share) * 0.40 W = 0.080 Wh-equivalent`
    4. *Relative Dynamic Active Energy Shares:*
        `Burst Weight = 0.045 / (0.045 + 0.080) = 36%` (rounded to `0.35`)
        `Sustained Weight = 0.080 / (0.045 + 0.080) = 64%` (rounded to `0.65`)

- **GPU Architecture Factor (F_gpu):**
  `F_gpu = 1.0 + 0.01 * (10.0 - GPU_Efficiency_Score)`
  - *Range of Variation:* With the GPU Efficiency Score ranging from 0.00 to 10.00, this factor ranges from **1.100 to 1.000** (representing a +10.0% increase to a 0% baseline in the **active dynamic power component** of the System-on-Chip (SoC)).
  - *Justification for Active-Only Application (Decoupled from Static Leakage):*
    Under low-load and idle conditions, the Graphics Processing Unit (GPU) is **power-gated** (disconnected from the power supply at the transistor level), meaning it draws zero static leakage current. The static leakage floor (`power_static_base`) is dominated by the idle CPU cores, logic board, and Power Management Integrated Circuit (PMIC) losses. The GPU is active only during three-dimensional (3D) gaming and User Interface (UI) rendering transitions, where it consumes dynamic active power. Therefore, `F_gpu` is decoupled from the static base power (`power_static_base`) and applied strictly as a multiplier on the active dynamic segment (`coefficient_soc_utilization * power_peak_soc * F_active_cpu * F_gpu * F_node_active`), preventing an inefficient GPU design from incorrectly penalizing the device's standby battery life.
  - *GPU Efficiency Score:* Sourced from the architectural performance-per-watt efficiency score in Section 6.3.0.
  - *Justification for Separate Performance and Efficiency Scores (CPU vs. GPU):* Unlike the CPU active model, where linear performance scores (burst and sustained) serve directly as proxies for active-state architectural efficiency (while a separate idle efficiency score is used strictly for the background leakage regime), the GPU model requires a separate, dedicated active-state efficiency score completely decoupled from its peak throughput capabilities:
    1. **Throughput-Oriented Single Instruction, Multiple Data (SIMD) Architecture:** CPU performance is latency-oriented (IPC-driven), where higher IPC translates directly to lower frequency/voltage under a given thread load. GPU performance, however, is throughput-oriented and scaled simply by adding massive arrays of physical Arithmetic Logic Unit (ALU) shader cores (e.g., Immortalis-G925 MC12 vs. Mali-G715 MC7).
    2. **Low-Load Decoupling:** Under daily mixed-use (rendering 2D UI frames, basic scrolling), the GPU operates at near-idle states where it power-gates almost all of its execution units, running only a minimal section of the silicon at low frequencies. A massive, high-performance GPU with a high rasterization score is not necessarily more efficient under low loads; its efficiency is governed entirely by dynamic leakage control, low-voltage limits, and clock-grid gating efficiency.
    3. **Microarchitectural Variance:** Peak graphics performance is decoupled from average daily rendering efficiency, independent of the process node. To prevent double-counting, the Process Node Factor (F_node) already isolates silicon-level transistor leakage and voltage scaling limits of the fabrication node. The GPU Architecture Factor (F_gpu) isolates GPU-specific microarchitectural efficiency (such as global clock-tree distribution grids, execution unit power-gating granularity, and graphics memory bus overhead). For example, comparing two Graphics Processing Units (GPUs) manufactured on the **same 4-nanometer (nm) process node**:
       * A massive flagship GPU contains a very large Arithmetic Logic Unit (ALU) array that achieves elite peak performance. However, due to its physical size, its clock-tree distribution network, wide memory bus interfaces, and global routing logic draw substantial static and dynamic power even under low-load daily rendering tasks (User Interface (UI) scrolling or 2D display frames) where most shader cores are power-gated.
       * A compact entry-level GPU on the same node has a much smaller ALU array and lower peak performance. However, its small physical footprint, narrow memory bus, and simple clock grid ensure that its active overhead remains extremely low during light rendering tasks.
       * If peak graphics performance were used as the sole proxy for daily rendering efficiency, the model would incorrectly predict that the massive flagship GPU is more efficient under light workloads than the compact entry-level GPU on the same node. Using a separate GPU Efficiency Score ensures microarchitectural layout overhead is modeled independently of the fabrication node.

###### 8.1.3.3.3 Connectivity Power Demand (P_connectivity)
Models the average power drawn by the cellular modem and Wireless Fidelity (Wi-Fi) chip under active mixed-use daily scenarios. In real-world operation, modern phones can have both radios active simultaneously for tasks such as Wi-Fi calling, assisted Global Positioning System (GPS), push notifications, background synchronization, or multi-link connectivity. However, under the empirical test sequences of the canonical benchmark (Method A), sustained user data transmission is treated as sequential rather than concurrent within the benchmark workload.

To align the theoretical model with the sequential, non-concurrent nature of the benchmark tests, we apply a time-weighted sequential power model:
`P_connectivity = 0.20 * P_cellular + 0.70 * P_wifi`

- **Sequential Weighting Justification:**
  - **Decomposition of Benchmark A (GSMArena Active Use Score) Phases:** The benchmark allocates approximately the following weight shares to its four active test phases:
    1. *Voice Calls Phase (20% share):* Sourced over a Fourth Generation (4G) Voice over Long-Term Evolution (VoLTE) cellular connection. Only the cellular modem is actively transmitting (`P_cellular`), while the Wi-Fi radio is idle.
    2. *Web Browsing Phase (30% share):* Sourced over Wi-Fi, involving dynamic scrolling page loads. Only the Wi-Fi radio is actively transmitting (`P_wifi`), while the cellular modem is in standby.
    3. *YouTube Video Streaming Phase (30% share):* Sourced over Wi-Fi, involving continuous video playback. Only the Wi-Fi radio is actively transmitting (`P_wifi`), while the cellular modem is in standby.
    4. *Three-Dimensional (3D) Gaming Phase (20% share):* Sourced local-offline on the device, requiring heavy CPU/GPU processing but zero active data transmission. Both modems remain in standby.
  - **Derivation of Connectivity Multipliers:**
    - **20% Cellular Active Duty Cycle (`0.20` multiplier):** Maps directly to the Voice Calls Phase where cellular transmission is active (`0.20 * P_cellular`).
    - **70% Wi-Fi Active Duty Cycle (`0.70` multiplier):** Combines the active data transmission during the Web Browsing Phase (30%) and Video Streaming Phase (30%). During the remaining 40% of the active use cycle (Voice Calls and 3D Gaming), the Wi-Fi radio is not actively transmitting but remains in a connected standby state. The connected standby state is approximated as consuming 25% of the active transmission power, representing periodic beacon reception, Delivery Traffic Indication Message (DTIM) wakeups, and link maintenance. This is an engineering approximation intended to capture background Wi-Fi activity during non-data phases, adding an equivalent duty cycle of `40% * 25% = 10%` and yielding a total weighted multiplier of `30% (Web) + 30% (Video) + 10% (Standby Overhead) = 70%` (`0.70 * P_wifi`).
    - **10% Idle Standby Duty Cycle (Omitted from active summation):** Represents the remaining portion of the offline 3D Gaming Phase where the cellular modem operates at its baseline idle/standby power floor with zero active transmission. Unlike Wi-Fi, whose connected standby remains associated with an access point and periodically exchanges management frames, the cellular modem's baseline idle registration and paging activity is treated as part of the device's static platform power and is therefore absorbed into `power_static_base`.

- **Cellular Modem Active Power (P_cellular):**
  To represent modem draw, the device's cellular hardware solution is mapped to one of the technology categories in **Section 7.1 (Cellular Capabilities)**. Because in-use cellular modem power is highly dynamic and depends on external factors (such as received signal strength indicator (RSSI), transmit power, uplink duty cycle, modulation and coding scheme (MCS), network congestion, and carrier aggregation), these values are **representative average active powers** under the standardized benchmark workload rather than universal hardware constants:
  - **0.18 W:** `5G mmWave + Sub-6 (Global band coverage)` — 5th Generation (5G) networks supporting both high-frequency millimeter-Wave (mmWave) and Sub-6 Gigahertz (GHz) bands, requiring additional front-end hardware power.
  - **0.14 W:** `5G Sub-6 (Full Global Bands)` or `5G Sub-6 (Limited/regional bands)` — standard 5G networks operating on Sub-6 GHz frequencies.
  - **0.09 W:** `4G LTE-Advanced Pro` or `4G LTE (Basic)` — 4th Generation (4G) Long-Term Evolution (LTE) modems.
  - **0.05 W:** `3G` or `2G` — legacy 3rd Generation (3G) or 2nd Generation (2G) modems.
- **Wi-Fi Active Power (P_wifi):**
  The device's Wi-Fi hardware solution is mapped to one of the standard categories in **Section 7.3 (Wi-Fi Standard)**. Similar to the cellular modem, the values are **representative average active powers** consumed during the dynamic test sequences rather than instantaneous peak power or energy-per-bit efficiency:
  - **0.05 W:** `Wi-Fi 7` — Wi-Fi 7 (802.11be) standard utilizing wide 320 Megahertz (MHz) channels and Multi-Link Operation (MLO).
  - **0.04 W:** `Wi-Fi 6E` or `Wi-Fi 6` — Wi-Fi 6 or 6E (802.11ax) standards utilizing 160 MHz channels.
  - **0.03 W:** `Wi-Fi 5`, `Wi-Fi 4`, or `Wi-Fi ≤3` — Wi-Fi 5 (802.11ac), Wi-Fi 4 (802.11n), or older legacy Wi-Fi standards.
  - *Note on Wi-Fi Power and Efficiency:* While newer standards (like Wi-Fi 7) are significantly more efficient on an *energy-per-bit* basis (completing data transfers faster and returning to standby), their dynamic average active power draw is higher during the active benchmark phases due to the activation of wider channel bandwidths (up to 320 MHz), additional Radio Frequency (RF) front-end chains, and Multi-Link Operation (MLO) active radios.

###### 8.1.3.3.4 Software Inefficiency Modifier (F_software_overhead)
Operating system (OS) execution efficiency and background application loads act as multipliers on hardware power demand:
`F_software_overhead = 1.0 + 0.01 * (10 - OS_Gen_Score) + 0.01 * (10 - SCC_Score)`

- *Range of Variation:* Under typical configurations, this modifier ranges from **1.000** (optimal baseline: current Operating System (OS) version with zero third-party preinstalled bloatware, where OS_Gen_Score = 10.0 and SCC_Score = 10.0) to **1.200** (worst case: obsolete OS version with heavily bloated backgrounds, where OS_Gen_Score = 0.0 and SCC_Score = 0.0). This represents a 0% to +20.0% increase multiplier on overall power demand.

- **OS Generation Score (OS_Gen_Score):**
  Modern operating systems (OS) implement aggressive background process freezing and kernel scheduler optimizations that minimize idle wakeups. To ensure absolute precision and programmatic traceability, this score is fetched directly from the **OS Generation Score** column of the canonical [Operating System Version Reference](references/os_version_reference.md) file. This centralized lookup eliminates the parsing ambiguity of textual version ranges and integrates support for custom mobile operating systems.

  **Justification for Granular Year-by-Year Scoring:**
  To accurately reflect software power management evolution, the scoring system implements a granular, year-by-year rating. Every annual release of Android and iOS introduces incremental updates in background limits, wake-lock control, and process freezing. Because operating system (OS) power management optimizations have matured, these improvements follow an asymptotic curve: early transitions (e.g., introducing strict background limits in 2017–2018) yielded massive efficiency gains and larger score differences (e.g., from 0.0 to 2.5, then 3.5), whereas recent annual updates (e.g., 2023 to 2026+) deliver diminishing returns with smaller score adjustments (e.g., 8.5 to 9.0, 9.5, and 10.0) as efficiency gains flatten out.

- **System Cleanliness & Control Score (SCC_Score):**
  Sourced from Section 5.2. The predicted score of Section 5.2 must be used (rather than the final score) to avoid any potential scoring bias that could be introduced by dynamic booster adjustments. A lower score indicates significant pre-installed manufacturer bloatware and background services, which prevent the processor from entering deep low-power sleep states.

###### 8.1.3.3.5 Thermal Efficiency Modifier (F_thermal_overhead)
Heat increases electrical current leakage in silicon transistors and raises the internal resistance of battery cells, degrading efficiency:
`F_thermal_overhead = 1.0 + 0.03 * (Power_Ratio_Max - power_ratio) / (Power_Ratio_Max - Power_Ratio_Min) clamped 1.000 to 1.030`

- *Range of Variation:* Based on the device's raw thermal headroom, this modifier ranges from **1.000** (optimal baseline: elite thermal design capable of sustaining peak SoC power, where power_ratio >= Power_Ratio_Max) to **1.030** (worst case: poor heat-dissipation plastic body matching the standardized performance floor, where power_ratio <= Power_Ratio_Min). This represents a 0% to +3.0% thermal leakage multiplier on overall power demand.
- **Parameters and Canonical Limits:**
  - `power_ratio` is the raw physical power ratio calculated analytically in Section 6.10.C (`power_ratio = power_admissible_soc / power_peak_soc`).
  - `Power_Ratio_Min = (Thermal_Stability_Min / 100) ^ 3` is the power ratio limit corresponding to the thermal performance floor.
  - `Power_Ratio_Max = (Thermal_Stability_Max / 100) ^ 3` is the power ratio limit corresponding to full thermal sustainability.
  - `Thermal_Stability_Min` and `Thermal_Stability_Max` are the canonical limits defined in `scoring_constants.md`.
- **Justification for Sourcing the Power Ratio Over the Stability Score:**
  - *Thermodynamic vs. Visual Scaling:* Semiconductor dynamic power scales cubically with frequency (`Power proportional to frequency^3`), meaning visual performance (FPS) stability is a cube-root function of the power ratio (`Stability_% = power_ratio ^ 0.333`). While this cube-root compression is appropriate for modeling human visual perception of frame-rate stuttering during gaming, the battery model is a physical energy-balance model. Silicon transistor leakage and battery internal resistance degrade directly as a function of temperature limits and physical wattage mismatches, not visual frame rates.
  - *Linking Admissible Power to Operating Temperature Rise:*
    The `power_ratio` (`power_admissible_soc / power_peak_soc`) serves as a direct physical proxy for the device's thermal headroom. A lower `power_ratio` indicates a severe thermal budget deficit under load. Under physical laws, this deficit translates directly into a higher operating temperature rise as the chassis struggles to dissipate the peak heat generated. This increased operating temperature is the critical driver of efficiency loss, directly causing higher silicon transistor leakage current and elevated internal battery cell resistance.
- **Justification for Using Calculated Method C Stability Across All Devices:** Sourcing the `power_ratio` strictly from the Method C calculation equations for all devices ensures a neutral, consistent, and unbiased physical power model that scales uniformly across the entire database, following the exact same rationale defined for the CPU performance inputs (see the justification under the CPU performance section above).
- *Calibration:* The maximum possible heat-induced leakage penalty is restricted to **3.0%** (applied when `power_ratio <= Power_Ratio_Min`). Because daily mixed-use tasks (such as web browsing and video streaming) generate very little thermal stress compared to a sustained 20-minute gaming workload, this moderate penalty prevents extreme peak thermal throttling behavior from disproportionately distorting standard, daily battery runtime calculations.

> [!NOTE]
> **Baseline Calibration & Future Refinements:**
> Only the **60 Hz alignment** (`F_refresh = 1.0` at 60 Hz) possesses a solid physical rationale, as display panel constants (`C_panel`) are empirically measured and calibrated at a standard 60 Hz refresh rate in laboratory environments. The remaining baselines (2.0 MP for resolution, 3.0 nm for process node, and a score of 10.0 for efficiency modifiers) are mathematical conventions. Consequently, these coefficients and arbitrary offsets should be fine-tuned and adjusted in future model versions using empirical regression analysis on the device database.
> Indeed, in future updates of the model, statistical studies can be performed on the collected device database to compare the predictions of the Technical Predictor Model (Method C) with the empirical testing outcomes of the Canonical Benchmark Validation (Method A). These comparison studies will enable regression analyses and parameter tuning, allowing developers to systematically adjust the model's physical parameters (such as the scaling coefficients, baseline constants, and modifier weights) to match real-world battery endurance profiles with even greater precision.

##### 8.1.3.4 Predicted Endurance Hours and Score Calculation
Once both the battery energy supply (`E_supply`) and total power demand (`P_demand`) are computed under the physical model, the active endurance hours (`T_predicted`) and the corresponding predicted score are determined.

###### 8.1.3.4.1 Endurance Hours (T_predicted)
The predicted active runtime of the device in hours is calculated using the fundamental physical relationship:
`T_predicted = E_supply / P_demand`
- **Supply (E_supply):** Total stored energy in Watt-hours (Wh).
- **Demand (P_demand):** Average electrical power consumption in Watts (W).

###### 8.1.3.4.2 Predicted Score Normalization
To convert the physical active endurance hours (`T_predicted`) to the standardized 0.0 to 10.0 score, the value is normalized linearly relative to the database bounds defined in `scoring_constants.md`.
- **Formula:**
  `Predicted_Score = 10 * (T_predicted - Battery_Predictor_Hours_Min) / (Battery_Predictor_Hours_Max - Battery_Predictor_Hours_Min)` (Clamped 0.0-10.0)
    *   **Max Score (10.0):** Achieved when `T_predicted` >= `Battery_Predictor_Hours_Max`.
    *   **Min Score (0.0):** Achieved when `T_predicted` <= `Battery_Predictor_Hours_Min`.

- **Justification for Linear Normalization (Why not Logarithmic?):**
  Battery life utility scales strictly linearly for the user. Unlike human sensory perceptions (such as screen brightness or performance responsiveness, which follow logarithmic curves because the human brain perceives stimulus changes on a logarithmic scale), battery runtime represents a direct physical limit. A smartphone that provides 12 hours of active runtime delivers exactly twice the utility of a device providing 6 hours (allowing the user to operate the device for twice as long without searching for a power outlet). Therefore, a linear score scale is the only representation that preserves this proportional relationship of real-world endurance.

##### 8.1.3.5 Comparison of Battery Endurance (Section 8.1) and Thermal Dissipation (Section 6.10) Models

To ensure complete clarity and physical consistency across the scoring framework, the table below maps the Level 1 components and Level 2 parameters (including System-on-Chip (SoC) and display variables) used in both the average Battery Endurance model and the sustained Thermal Dissipation model, along with their engineering justifications:

| Level 1 Component      | Level 2 Parameter / Variable | In §8.1? | In §6.10? | Engineering Justification                                                                                                      |
| :--------------------- | :--------------------------- | :------: | :-------: | :----------------------------------------------------------------------------------------------------------------------------- |
| **SoC Power**          | `power_static_base` (0.40 W) |  **Yes** |  **Yes**  | Shared baseline logic board draw (including Power Management Integrated Circuit (PMIC) losses and RAM idle draw).              |
|                        | `power_peak_soc` (Watts)     |  **Yes** |  **Yes**  | Sourced from peak package power. Full in Section 6.10 (gaming peak); dampened by 0.015 factor in Section 8.1 (mixed use).      |
|                        | `F_node` / `F_cpu` / `F_gpu` |  **Yes** |  **No**   | Section 8.1 uses low-load scaling multipliers. Omitted in Section 6.10 to prevent double-counting (see previous line).         |
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
> While sequential time-weighted connectivity draw (`P_connectivity = 0.20 * P_cellular + 0.70 * P_wifi`) ranges from ~ `0.03 W` to `0.07 W` during active daily mixed usage (with a maximum peak of `0.18 W` representing the maximum single-interface transmission power, since cellular and Wi-Fi do not operate concurrently), it is omitted from the sustained thermal model in Section 6.10 because:
> 1. **Offline Benchmark Execution:** Standardized graphics stress tests (such as 3DMark Wild Life Extreme) are executed locally with devices placed in Airplane Mode to eliminate testing variance. Dynamic data transfer power is therefore zero.
> 2. **Baseline Leakage Encapsulation:** The static, low-power leakage of inactive cellular and Wi-Fi silicon is already fully accounted for in the system's baseline logic board heat (`power_static_base = 0.40 W`), specifically within the baseline logic and baseband idle segment (~0.15 W).
> 3. **Thermal Scale Comparison:** Even under active online gaming conditions, the peak dynamic connectivity draw (~0.18 W) represents only about 3% to 6% of a device's total sustained thermal budget (typically 3.0 W to 6.0 W), making it negligible compared to primary thermal drivers like the active display and System-on-Chip (SoC).

> [!NOTE]
> **Omission of Software Overhead in the Thermal Model (Section 6.10):**
> Software efficiency and system cleanliness factors (`F_software_overhead`) are omitted from the sustained thermal dissipation model because:
> 1. **Hardware Power Envelope Limits:** During sustained peak benchmarks (such as 3DMark or GFXBench), the Central Processing Unit (CPU) and Graphics Processing Unit (GPU) are fully saturated at 100% utilization. The Power Management Integrated Circuit (PMIC) and system firmware enforce strict hardware power caps to prevent electrical overcurrent. Background software cannot cause the processor to draw more power than this physical maximum.
> 2. **Process Starvation and Scheduler Prioritization:** Operating System (OS) kernel schedulers prioritize the active foreground benchmark application over background services. Low-priority background bloatware is starved of execution cycles, meaning it does not contribute dynamic thermal load during the test.
> 3. **Bypassing of Power-Saving Sleep States:** Annual Operating System (OS) optimization upgrades (such as background process freezing, wake-lock pooling, and core parking) are designed to keep the processor in deep, low-power sleep states during idle periods. Because a sustained thermal benchmark forces the processor to remain continuously active in peak power states, these software optimization mechanisms are completely bypassed.

##### 8.1.3.6 Model Validation Worked Examples

###### 8.1.3.6.1 Ultra-Flagship Device
- **Specifications:**
  - **Chipset:** Snapdragon 8 Elite (Peak Package Power = `19.5 W`, TSMC 3nm Node, smallest core = Oryon Gen 2 with `CPU_Background_Score = 0.00` and `CPU_Burst_Score = 9.1343`, `CPU_Sustained_Score = 9.7723`, `GPU_Efficiency_Score = 10.0`)
  - **Battery:** 5000 mAh at 3.85V (`E_supply = 19.25 Wh`)
  - **Display:** 115.0 cm² display area, LTPO OLED panel (`C_panel = 0.0035 W/cm²`), 90 Hz adaptive browsing (`effective_hz = 90 Hz`), QHD+ resolution (`megapixels_mp = 4.5`)
  - **Connectivity:** 5G Sub-6 modem (`P_cellular = 0.14 W`) + Wi-Fi 7 (`P_wifi = 0.05 W`)
  - **Modifiers:** OS_Gen_Score = `10.0`, SCC_Score = `10.0`, power_ratio = `1.0000`
- **Calculations:**
  - **System-on-Chip (SoC) Draw (P_soc):**
    - *CPU Active Score:* Calculated as the weighted average of the Burst and Sustained scores (`CPU_Active_Score = 0.35 * CPU_Burst_Score + 0.65 * CPU_Sustained_Score`):
      `CPU_Active_Score = clamp(0.35 * 9.1343 + 0.65 * 9.7723, 0.00, 10.00) = 9.5490`
    - *CPU Static Efficiency Factor:* Adjusts static base power based on background efficiency:
      `F_static_cpu = 1.0 + 0.04 * (10.0 - CPU_Background_Score) = 1.0 + 0.04 * (10.0 - 0.00) = 1.4000`
    - *CPU Active Efficiency Factor:* Adjusts active dynamic power based on active core efficiency:
      `F_active_cpu = 1.0 + 0.04 * (10.0 - CPU_Active_Score) = 1.0 + 0.04 * (10.0 - 9.5490) = 1.0180`
    - *Static Process Node Factor:* Adjusts static leakage based on fabrication node geometry:
      `F_node_static = 0.80 + 0.20 * (process_nm / 3.0) = 0.80 + 0.20 * (3.0 / 3.0) = 1.0000`
    - *Active Process Node Factor:* Adjusts active dynamic power based on fabrication node geometry:
      `F_node_active = 0.65 + 0.35 * (process_nm / 3.0) = 0.65 + 0.35 * (3.0 / 3.0) = 1.0000`
    - *GPU Architecture Factor:* Adjusts active dynamic power based on GPU layout efficiency:
      `F_gpu = 1.0 + 0.01 * (10.0 - GPU_Efficiency_Score) = 1.0 + 0.01 * (10.0 - 10.0) = 1.0000`
    - *Total SoC Power Draw:* Sum of the process-scaled static board leakage and active dynamic SoC power (`P_soc = power_static_base * F_static_cpu * F_node_static + coefficient_soc_utilization * power_peak_soc * F_active_cpu * F_gpu * F_node_active`):
      `P_soc = 0.40 * 1.4000 * 1.0000 + 0.0150 * 19.5 * 1.0180 * 1.0000 * 1.0000 = 0.5600 W + 0.2978 W = 0.8578 W`
  - **Display Draw (P_display):**
    - *Refresh Rate Factor:* Adjusts display power based on screen update frequency:
      `F_refresh = 1.0 + 0.0025 * (effective_hz - 60.0) = 1.0 + 0.0025 * (90 - 60.0) = 1.0750`
    - *Resolution Factor:* Adjusts display power based on pixel density:
      `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0) = 1.0 + 0.025 * (4.5 - 2.0) = 1.0625`
    - *Total Display Power Draw:* Product of surface area, panel constant, refresh rate, and resolution factors:
      `P_display = display_surface_area_cm2 * C_panel * F_refresh * F_resolution = 115.0 * 0.0035 * 1.0750 * 1.0625 = 0.4597 W`
  - **Connectivity Draw (P_connectivity):**
    - *Weighted Active/Standby Connectivity Power:* Average power drawn by Wi-Fi and cellular modems under benchmark sequences:
      `P_connectivity = 0.20 * P_cellular + 0.70 * P_wifi = 0.20 * 0.14 + 0.70 * 0.05 = 0.0280 + 0.0350 = 0.0630 W`
  - **Total Demand (P_demand):**
    - *Software Inefficiency Modifier:* Accounts for OS optimization generation and pre-installed software bloat:
      `F_software_overhead = 1.0 + 0.01 * (10.0 - OS_Gen_Score) + 0.01 * (10.0 - SCC_Score) = 1.0 + 0.01 * (10.0 - 10.0) + 0.01 * (10.0 - 10.0) = 1.0000`
    - *Thermal Efficiency Modifier:* Accounts for transistor leakage and cell internal resistance rise using raw physical power ratio:
      `F_thermal_overhead = 1.0 + 0.03 * (Power_Ratio_Max - power_ratio) / (Power_Ratio_Max - Power_Ratio_Min) = 1.0 + 0.03 * (1.0000 - 1.0000) / (1.0000 - 0.0640) = 1.0000`
    - *Total Power Demand:* Combined display, processing, and connectivity scaled by software and thermal modifiers:
      `P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead = (0.4597 + (0.8578 + 0.0630) * 1.0000) * 1.0000 = 1.3805 W`
  - **Theoretical Endurance (T_predicted):**
    - *Active Endurance Hours:* Predicted runtime calculated as the ratio of total battery energy to average power demand:
      `T_predicted = E_supply / P_demand = 19.25 Wh / 1.3805 W = 13.94 Hours`
  - **Predicted Score:**
    - *Standardized Battery Score:* Predictor active endurance hours normalized linearly between canonical limits:
      `Predicted_Score = 10.0 * (T_predicted - Battery_Predictor_Hours_Min) / (Battery_Predictor_Hours_Max - Battery_Predictor_Hours_Min) = 10.0 * (13.94 - 3.95) / (26.67 - 3.95) = 4.40`

###### 8.1.3.6.2 Budget Device
- **Specifications:**
  - **Chipset:** MediaTek Helio G99 (Peak Package Power = `4.5 W`, TSMC 6nm Node, smallest core = Cortex-A55 with `CPU_Background_Score = 8.00` and `CPU_Burst_Score = 1.7313`, `CPU_Sustained_Score = 1.4449`, `GPU_Efficiency_Score = 5.0`)
  - **Battery:** 5000 mAh at 3.85V (`E_supply = 19.25 Wh`)
  - **Display:** 108.0 cm² display area, standard Liquid Crystal Display (LCD) panel (`C_panel = 0.0060 W/cm²`), 120 Hz static refresh rate (`effective_hz = 120 Hz`), Full High Definition Plus (FHD+) resolution (`megapixels_mp = 2.5`)
  - **Connectivity:** 4G Long-Term Evolution (LTE) Advanced (`P_cellular = 0.09 W`) + Wi-Fi 5 (`P_wifi = 0.03 W`)
  - **Modifiers:** OS_Gen_Score = `8.0`, SCC_Score = `4.0`, power_ratio = `0.4384`
- **Calculations:**
  - **System-on-Chip (SoC) Draw (P_soc):**
    - *CPU Active Score:* Calculated as the weighted average of the Burst and Sustained scores (`CPU_Active_Score = 0.35 * CPU_Burst_Score + 0.65 * CPU_Sustained_Score`):
      `CPU_Active_Score = clamp(0.35 * 1.7313 + 0.65 * 1.4449, 0.00, 10.00) = 1.5451`
    - *CPU Static Efficiency Factor:* Adjusts static base power based on background efficiency:
      `F_static_cpu = 1.0 + 0.04 * (10.0 - CPU_Background_Score) = 1.0 + 0.04 * (10.0 - 8.00) = 1.0800`
    - *CPU Active Efficiency Factor:* Adjusts active dynamic power based on active core efficiency:
      `F_active_cpu = 1.0 + 0.04 * (10.0 - CPU_Active_Score) = 1.0 + 0.04 * (10.0 - 1.5451) = 1.3382`
    - *Static Process Node Factor:* Adjusts static leakage based on fabrication node geometry:
      `F_node_static = 0.80 + 0.20 * (process_nm / 3.0) = 0.80 + 0.20 * (6.0 / 3.0) = 1.2000`
    - *Active Process Node Factor:* Adjusts active dynamic power based on fabrication node geometry:
      `F_node_active = 0.65 + 0.35 * (process_nm / 3.0) = 0.65 + 0.35 * (6.0 / 3.0) = 1.3500`
    - *GPU Architecture Factor:* Adjusts active dynamic power based on GPU layout efficiency:
      `F_gpu = 1.0 + 0.01 * (10.0 - GPU_Efficiency_Score) = 1.0 + 0.01 * (10.0 - 5.0) = 1.0500`
    - *Total SoC Power Draw:* Sum of the process-scaled static board leakage and active dynamic SoC power (`P_soc = power_static_base * F_static_cpu * F_node_static + coefficient_soc_utilization * power_peak_soc * F_active_cpu * F_gpu * F_node_active`):
      `P_soc = 0.40 * 1.0800 * 1.2000 + 0.0150 * 4.5 * 1.3382 * 1.0500 * 1.3500 = 0.5184 W + 0.1280 W = 0.6464 W`
  - **Display Draw (P_display):**
    - *Refresh Rate Factor:* Adjusts display power based on screen update frequency:
      `F_refresh = 1.0 + 0.0025 * (effective_hz - 60.0) = 1.0 + 0.0025 * (120 - 60.0) = 1.1500`
    - *Resolution Factor:* Adjusts display power based on pixel density:
      `F_resolution = 1.0 + 0.025 * (megapixels_mp - 2.0) = 1.0 + 0.025 * (2.5 - 2.0) = 1.0125`
    - *Total Display Power Draw:* Product of surface area, panel constant, refresh rate, and resolution factors:
      `P_display = display_surface_area_cm2 * C_panel * F_refresh * F_resolution = 108.0 * 0.0060 * 1.1500 * 1.0125 = 0.7545 W`
  - **Connectivity Draw (P_connectivity):**
    - *Weighted Active/Standby Connectivity Power:* Average power drawn by Wi-Fi and cellular modems under benchmark sequences:
      `P_connectivity = 0.20 * P_cellular + 0.70 * P_wifi = 0.20 * 0.09 + 0.70 * 0.03 = 0.0180 + 0.0210 = 0.0390 W`
  - **Total Demand (P_demand):**
    - *Software Inefficiency Modifier:* Accounts for OS optimization generation and pre-installed software bloat:
      `F_software_overhead = 1.0 + 0.01 * (10.0 - OS_Gen_Score) + 0.01 * (10.0 - SCC_Score) = 1.0 + 0.01 * (10.0 - 8.0) + 0.01 * (10.0 - 4.0) = 1.0800`
    - *Thermal Efficiency Modifier:* Accounts for transistor leakage and cell internal resistance rise using raw physical power ratio:
      `F_thermal_overhead = 1.0 + 0.03 * (Power_Ratio_Max - power_ratio) / (Power_Ratio_Max - Power_Ratio_Min) = 1.0 + 0.03 * (1.0000 - 0.4384) / (1.0000 - 0.0640) = 1.0180`
    - *Total Power Demand:* Combined display, processing, and connectivity scaled by software and thermal modifiers:
      `P_demand = (P_display + (P_soc + P_connectivity) * F_software_overhead) * F_thermal_overhead = (0.7545 + (0.6464 + 0.0390) * 1.0800) * 1.0180 = 1.5216 W`
  - **Theoretical Endurance (T_predicted):**
    - *Active Endurance Hours:* Predicted runtime calculated as the ratio of total battery energy to average power demand:
      `T_predicted = E_supply / P_demand = 19.25 Wh / 1.5216 W = 12.65 Hours`
  - **Predicted Score:**
    - *Standardized Battery Score:* Predictor active endurance hours normalized linearly between canonical limits:
      `Predicted_Score = 10.0 * (T_predicted - Battery_Predictor_Hours_Min) / (Battery_Predictor_Hours_Max - Battery_Predictor_Hours_Min) = 10.0 * (12.65 - 3.95) / (26.67 - 3.95) = 3.83`


### 🔹 8.2 Wired Charging System
*Description:* Comprehensive evaluation of the wired charging system, comprising pure full-charge duration performance, open universal USB Power Delivery ecosystem interoperability, and hardware bypass power delivery capability.
*   **Measurement:** Canonical full charge duration in minutes (`T_final`) evaluated via Method A (Empirical Benchmark), Method B (Nearest-Neighbor Interpolation), or Method C (Analytical Physics Predictor) to yield `S_speed`, combined with continuous open USB-PD speed ratio (`S_interoperability`) and hardware battery-bypass direct drive (`S_bypass`).
*   **Unit:** Minutes (mins) for speed duration; Composite Score (0.0 to 10.0) for overall section score.
*   **Significance:** Minimizes wall-tethered downtime when battery power is depleted, guarantees fast charging across non-proprietary third-party chargers, and prevents overheating during plugged-in heavy use (gaming, GPS navigation, mobile hotspot tethering).

#### 8.2.0 Executive Framework Overview & Core Component Definitions
To provide a complete and transparent evaluation of a smartphone's wired charging system, the overall Section 8.2 score is derived from **three distinct, non-overlapping hardware components**:

1. **Pure Charging Speed Score (`S_speed` — 88% Weight):**
   * **What it measures:** The real-world physical duration in minutes required to charge a completely depleted smartphone battery from 0% to 100% State of Charge using its fastest official wall charger.
   * **Why & Weight Rationale (88%):** Primary utility impacting 100% of users on 100% of charge cycles. Minimizing wall-tethered downtime is the dominant physical driver of charging satisfaction.

2. **Universal Protocol Interoperability Score (`S_interoperability` — 9% Weight):**
   * **What it measures:** The percentage of maximum charging performance accessible when using open, non-proprietary third-party chargers (such as USB Power Delivery — USB-PD, an open universal fast-charging standard defined by the USB Implementers Forum, and Programmable Power Supply — PPS, an advanced extension allowing real-time voltage and current micro-adjustments), rather than vendor-locked proprietary wall adapters.
   * **Why & Weight Rationale (9%):** Secondary utility impacting users when charging away from home (office, travel, laptop chargers). Creates a meaningful penalty for vendor lock-in without allowing a slow universal phone to outscore an ultra-fast proprietary phone (`S_interoperability << S_speed`).

3. **Hardware Bypass Charging / Direct Drive Score (`S_bypass` — 3% Weight):**
   * **What it measures:** A Power Management Integrated Circuit (PMIC, an on-board silicon chip regulating internal power conversion and bus rails) feature that routes wall electricity **directly to the logic board and processor**, bypassing the battery cell entirely during plugged-in use.
   * **Why & Weight Rationale (3%):** Niche utility for heavy plugged-in workloads (3D gaming, GPS navigation in sunlight, hotspot tethering). Normal plugged-in use forces current into the battery while pulling heavy current out, generating extreme heat; direct drive powers the processor directly to keep the battery cool. Weighted at 3% to reward hardware capability without distorting everyday smartphone scores (`S_bypass << S_interoperability`).

##### Section 8.2 Overall Composite Formula
`Final Score 8.2 = 0.88 * S_speed + 0.09 * S_interoperability + 0.03 * S_bypass` (Clamped 0.0 to 10.0)

#### 8.2.1 Pure Wired Charging Speed
Evaluates the physical time required to restore a depleted smartphone battery from 0% to 100% State of Charge under standard laboratory conditions.

##### 8.2.1.A Method A: Benchmark (Primary)
Method A is the primary empirical benchmark calculation used when a verified laboratory test log from GSMArena is available in the database.

###### 8.2.1.A.1 Canonical Benchmark Source Selection & Justification
To guarantee 100% empirical rigor, eliminate inter-benchmark protocol offsets, and avoid data bias, **Method A strictly utilizes the GSMArena Wired Charging Speed Benchmark as its single canonical data source**.

**Engineering Justification for Excluding Multi-Source Blending:**
1. **Strict Protocol Standardization:** GSMArena executes a fully controlled laboratory protocol: the phone is discharged to 0% State of Charge, allowed to rest until reaching a stable ambient temperature (22°C to 25°C), and charged with the screen turned off using the manufacturer's maximum supported official fast-charging brick and original high-current cable.
2. **Database Uniformity & Historical Depth:** GSMArena maintains a continuous, uninterrupted benchmark database covering over 1,500 smartphones from 2016 through 2026, ensuring consistent measurement criteria across a decade of mobile hardware.
3. **Elimination of Inter-Benchmark Bias:** Secondary review outlets (such as PhoneArena or NotebookCheck) utilize differing criteria—such as testing with bundled in-box chargers (which may be lower wattage than the phone's maximum capability) or defining "100%" at initial UI prompt rather than true mains wall-power termination. Blending data from multiple outlets introduces systemic offsets of 5 to 15 minutes for identical devices. Standardizing strictly on GSMArena eliminates this variance completely.

###### 8.2.1.A.2 Metric Extraction & Duration (`T_final`)
When a GSMArena test result is present in the database:
`T_final = GSMArena_charging_time_100_mins`
*Score Source Tag:* Logged as `"Method A (GSMArena Empirical Benchmark)"`.

###### 8.2.1.A.3 Charging Speed Component Score (`S_speed`)
The charging speed score (`S_speed`) is computed directly from the extracted duration `T_final` using a **Logarithmic Utility Normalization Formula**:

`S_speed = 10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(T_final)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins))` (Clamped 0.0 to 10.0)

*   `Battery_Wired_Charge_Time_Min_Mins` and `Battery_Wired_Charge_Time_Max_Mins`: Normalization constants defined in `scoring_constants.md`.

> [!NOTE]
> **Why Logarithmic Utility Normalization (`log(T)`)?**
> Human perception of waiting time exhibits diminishing marginal utility and is broadly consistent with logarithmic psychophysical models such as the Weber-Fechner Law. Linear normalization treats identical reductions in charging time as equally valuable regardless of the starting point, while inverse normalization (`1 / T`) disproportionately rewards improvements among already ultra-fast devices. Logarithmic normalization provides a realistic approximation of perceived user benefit by emphasizing the elimination of long charging times, while preserving meaningful rewards for substantial reductions in typical fast-charging ranges. An additional advantage is scale invariance: equal proportional improvements in charging time (for example, halving the full-charge duration) receive equal score gains, matching how users and reviewers commonly describe charging performance as "twice as fast" or "50% faster" rather than in absolute minutes saved.


##### 8.2.1.B Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** devices (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A, and serves as the primary fallback for unbenchmarked devices when 3 or more reference devices exist in the database.

When the target device lacks direct benchmark data, we use a technical predictive model to locate the **3 most physically similar reference devices** that *do* have benchmark data, and interpolate the target device's score.

###### 8.2.1.B.1 The 3-Component Physical Similarity Space
To map devices into a dimensionally homogeneous coordinate system, we measure how much the target device differs from a candidate neighbor device across its primary physical charging parameters derived from **Method C: Technical Predictor Model** (detailed in Section 8.2.1.C):
1. **Stored Battery Energy (`E_supply`, in Watt-hours - Wh):** Total nominal battery energy.
2. **Peak Rated Power (`P_peak`, in Watts - W):** Maximum supported continuous wired wattage.
3. **Predicted Charge Duration (`T_predicted`, in minutes - mins):** Analytical baseline charging duration calculated by Method C.

> [!NOTE]
> **Logarithmic System Identity & Implicit Architecture Alignment:**
> Taking the logarithm of Method C's fundamental equation yields the exact physical identity:
> `log(T_predicted) = log(E_supply) - log(P_peak) - log(F_system) + log(60)`
> If two devices have near-identical `log(E_supply)`, `log(P_peak)`, and `log(T_predicted)`, then `log(F_system)` and `C_rate` (`P_peak / E_supply`) are also mathematically guaranteed to be near-identical. Because Single-Cell (1S) and Dual-Cell Series (2S) architectures differ by a factor of 6.6x in baseline onset threshold (`C0_single = 0.4051 h^-1` vs. `C0_dual = 2.6813 h^-1`), similarity across these three logarithmic dimensions naturally forces neighbor devices to share the **exact same cell architecture** without requiring artificial penalty offsets.

###### 8.2.1.B.2 Feature Distance Formula
The similarity between the target device and a candidate neighbor device is computed using a **Log-Standardized Euclidean Distance** across all continuous physical dimensions:

`Distance = Sqrt( (Delta_log_E_supply)^2 + (Delta_log_P_peak)^2 + (Delta_log_T_predicted)^2 )`

*   `Delta_log_E_supply = log(E_supply_target) - log(E_supply_neighbor)`
*   `Delta_log_P_peak = log(P_peak_target) - log(P_peak_neighbor)`
*   `Delta_log_T_predicted = log(T_predicted_target) - log(T_predicted_neighbor)`
*   **Search Space:** All devices with known GSMArena full charge benchmarks (Method A), **excluding the target device** itself.
*   **Selection:** Pick the 3 distinct neighbor devices with the smallest `Distance`.

###### 8.2.1.B.3 Interpolation, Calibration & Speed Component Score (`S_speed`)
1. **Compute Neighbor Predicted Average:** Calculate the average predicted charge duration of the 3 nearest neighbors (from Method C):
   `Avg_Predicted_Neighbors = (T_predicted_Neighbor1 + T_predicted_Neighbor2 + T_predicted_Neighbor3) / 3`
2. **Compute Correction Ratio:** Measures how the target device's physical profile structurally differs from its neighbors (where `T_predicted_Target` is the target device's predicted charge duration calculated via Method C):
   `Correction_Ratio = T_predicted_Target / Avg_Predicted_Neighbors`
3. **Compute Neighbor Empirical Average:** Calculate the average real-world benchmark charge duration of the 3 nearest neighbors (from Method A):
   `Avg_Benchmark_Neighbors = (T_GSMArena_Neighbor1 + T_GSMArena_Neighbor2 + T_GSMArena_Neighbor3) / 3`
4. **Calculate Interpolated Full Charge Duration (`T_interpolated`):**
   `T_final = T_interpolated = Correction_Ratio * Avg_Benchmark_Neighbors`
   *Score Source Tag:* Logged as `"Method B (Nearest Neighbor Interpolation)"`.
5. **Compute Speed Component Score (`S_speed_MethodB`):**
   `S_speed_MethodB = 10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(T_final)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins))` (Clamped 0.0 to 10.0)

   *   `Battery_Wired_Charge_Time_Min_Mins` and `Battery_Wired_Charge_Time_Max_Mins`: Shared normalization constants defined in `scoring_constants.md`.

> [!NOTE]
> **Unified Benchmark-Aligned Normalization Rationale:**
> Method B uses the unified normalization constants (`Battery_Wired_Charge_Time_Min_Mins` and `Battery_Wired_Charge_Time_Max_Mins`) defined in `scoring_constants.md`, which are shared across all three evaluation paths (`Method A`, `Method B`, `Method C`) to guarantee complete scale invariance (see [section_8_2_method_c_huber_optimization_study.md] for detailed mathematical justification and strategy evaluation).


##### 8.2.1.C Method C: Technical Predictor Model (Tertiary, Analytical Method)
Method C is the standalone analytical physics model. Its parameter values are calibrated and justified across 40+ empirical laboratory benchmarks in [section_8_2_method_c_huber_optimization_study.md]. It is used as a fallback when physical benchmark logs and neighbor reference pools are unavailable, and serves as the **Predictor** input (`T_predicted`) for Method B interpolation.

###### 8.2.1.C.1 Conceptual Physics & The Fundamental Equations
In mobile battery engineering, evaluating charging speed solely by **Peak Rated Wattage** (Watts) is fundamentally misleading. A 45 Watt (W) charger powering a small 2,500 Milliampere-hour (mAh) battery replenishes energy far faster than an identical 45 Watt (W) charger powering a massive 6,000 Milliampere-hour (mAh) battery. 

Furthermore, Lithium-Ion and Lithium-Polymer battery cells cannot accept constant power throughout a charge cycle. Charging occurs in two non-linear phases:
1. **Constant Current (CC) Phase (0% to ~50–80% State of Charge):** The Battery Management System (BMS) delivers high current. Power input reaches or approaches peak wattage (`P_peak`).
2. **Constant Voltage (CV) / Trickle Phase (~80% to 100% State of Charge):** Internal cell resistance rises and lithium ions saturate the graphite anode. To prevent metallic lithium plating, internal cell swelling, and thermal runaway, the Battery Management System (BMS) forces voltage to cap and exponentially decays current toward zero.

The true metric of user utility is **Full Charge Duration (`T_predicted` in minutes)**—the exact time needed to restore a depleted phone (0% State of Charge) to complete capacity (100% State of Charge) under standard operating temperatures.

The model estimates the physical consequences of publicly observable characteristics, answering one fundamental question: *Given only publicly observable characteristics of a phone, how long should a 0–100% charge take?*

The fundamental equations representing this physical process are:

`T_predicted = (E_supply / P_effective) * 60`

`P_effective = P_peak * F_system(C_rate)`

`F_system = min(1, eta_low / (1 + k * max(0, C_rate - C0_effective)^p))`

`C0_effective = C0_base * f_thermal(power_ratio) * f_skin_headroom(T_limit)`

Where:
*   `T_predicted`: Full 0% to 100% charging duration expressed in minutes (min) (hence the factor of 60 converting hours to minutes).
*   `E_supply`: Stored battery energy capacity in Watt-hours (Wh).
*   `P_effective`: Average effective power delivered over the entire charge cycle in Watts (W).
*   `P_peak`: Maximum physical input charging power accepted by the smartphone hardware in Watts (W).
*   `C_rate`: Continuous charging current rate normalized by stored energy (`C_rate = P_peak / E_supply` in reciprocal hours, `h^-1`).
*   `F_system(C_rate)`: Continuous full-cycle power retention factor.
*   `eta_low = 0.9679`: Baseline low-power full-cycle utilization fraction.
*   `C0_effective`: Thermally scaled effective onset threshold (`C0_effective = C0_base` since `f_thermal` and `f_skin_headroom` are neutralized to 1.0).
*   `C0_base`: Architecture-dependent baseline thermal saturation onset threshold.
*   `k = 1.1265`: Non-linear thermal taper severity multiplier.
*   `p = 0.1344`: Power saturation curvature exponent.

> [!NOTE]
> **Parameter Justification & Calibration Study:**
> The numerical values for the 5 physical parameters above (`eta_low`, `C0_single`, `C0_dual`, `k`, `p`) are derived and justified in detail via global deterministic optimization on empirical benchmarks in [section_8_2_method_c_huber_optimization_study.md].


###### 8.2.1.C.2 Step-by-Step Mathematical Derivation
Method C is populated for **all** devices to serve as the baseline physical predictor model. It serves as the ultimate fallback score for unbenchmarked devices when fewer than 3 nearest neighbors exist in the database.

**Step 1: Stored Battery Energy (`E_supply`)**
Evaluates total stored nominal battery energy capacity `E_supply` in Watt-hours (Wh):
`E_supply = (Capacity_mAh * V_nominal) / 1000`

*   *Note: Sourced directly from [Section 8.1]. Refer to Section 8.1 for the complete determination logic governing nominal voltage (`V_nominal`) and battery cell architecture.*

**Step 2: Maximum Charging Input Power (`P_peak`)**
`P_peak` is the maximum open wired charging power input accepted by the device in Watts (W), representing phone hardware capacity rather than charger output rating.

*   *Note: Refer to [proposed_data_structure.md] for the complete evidence sourcing hierarchy.*

*Data Integrity Rationale:* A bundled wall charger may be rated for 67W, while the phone hardware may be internally capped at 33W. Using the charger's maximum output instead of the phone's actual accepted input power causes massive prediction errors.

**Step 3: Continuous C-Rate (`C_rate`)**
Calculates the peak continuous charge rate relative to battery capacity (in reciprocal hours, `h^-1`):
`C_rate = P_peak / E_supply`
*   *Example:* A 240 W charger on a 17.71 Wh battery produces a peak C-rate of `240 / 17.71 = 13.55 h^-1`.

*Electrochemical Kinetics Rationale:* C-Rate normalizes the charging speed relative to the battery's size. A 1.0 C-rate implies the battery would theoretically charge in one hour if power remained constant. High C-rates drive faster lithium-ion intercalation at the anode but generate exponentially more heat, which dictates when and how severely the system must engage thermal throttling in subsequent steps.

**Step 4: Continuous Full-Cycle Power Retention Factor (`F_system`)**
Calculates the continuous peak-to-average charging power retention factor `F_system`:

`F_system = min(1, eta_low / (1 + k * max(0, C_rate - C0_effective)^p))`

`C0_effective = C0_base * f_thermal(power_ratio) * f_skin_headroom(T_limit)`

*   **Architecture-Dependent Onset Thresholds (`C0_base`):**
    *   **Single-Cell (1S) Array (`C0_single = 0.4051 h^-1`):** Single-cell batteries operate at ~3.85 Volts (V) nominal, requiring high current to accept peak charging power. Higher current increases Printed Circuit Board (PCB) trace Joule heating (`I^2 * R`), triggering power tapering at a lower onset charge rate threshold (`C0 ≈ 0.41 h^-1`).
    *   **Dual-Cell Series (2S) Array (`C0_dual = 2.6813 h^-1`):** Dual-cell series arrays double system voltage to ~7.70 Volts (V) nominal, halving per-cell current for equivalent wattages and reducing Printed Circuit Board (PCB) Joule heat by 75%. This enables 2S architectures to sustain unthrottled charging up to a significantly higher onset threshold (`C0 ≈ 2.68 h^-1`).
    *   **Impact on Charging Duration (`T_predicted`):** The onset threshold `C0_base` dictates when power tapering begins. Devices with high onset thresholds (such as 2S arrays) maintain peak power utilization over a larger fraction of the Constant Current (CC, the first phase of lithium-ion battery charging where maximum current is delivered) phase, resulting in higher average effective power (`P_effective`) and substantially shorter predicted full charge durations (`T_predicted`).

*   **Neutralization of Operational Multipliers (`f_thermal = 1.0`, `f_skin_headroom = 1.0`):**
    In the 44-device calibration, System-on-Chip (SoC, the main semiconductor package containing CPU and GPU) thermal load (`f_thermal`) and skin temperature headroom (`f_skin_headroom`) are fixed to `1.0` (neutralized) because observable hardware specifications (peak wattage `P_peak` and cell architecture 1S vs. 2S) already capture the dominant thermal constraints. Adding additional empirical thermal multipliers introduced model over-parameterization without improving prediction accuracy. For full mathematical derivations, sensitivity sweeps, and optimization matrices, see [section_8_2_method_c_huber_optimization_study.md].

**Step 5: Average Effective Full-Cycle Power (`P_effective`)**
Calculates actual sustained average charging power delivered over the entire 0% to 100% cycle:
`P_effective = P_peak * F_system`

**Step 6: Predicted Duration (`T_predicted`) & Speed Component (`S_speed`)**
1. **Predicted Full Charge Duration (`T_predicted`):**
   `T_final = T_predicted = (E_supply / P_effective) * 60`

2. **Compute Method C Speed Component Score (`S_speed_MethodC`):**
   `S_speed_MethodC = 10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(T_predicted)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins))` (Clamped 0.0 to 10.0)

   *   `Battery_Wired_Charge_Time_Min_Mins` and `Battery_Wired_Charge_Time_Max_Mins`: Shared normalization constants defined in `scoring_constants.md`.

> [!NOTE]
> **Unified Benchmark-Aligned Normalization Rationale:**
> Method C uses the unified normalization constants (`Battery_Wired_Charge_Time_Min_Mins` and `Battery_Wired_Charge_Time_Max_Mins`) defined in `scoring_constants.md`, which are shared across all three evaluation paths (`Method A`, `Method B`, `Method C`) to guarantee complete scale invariance (see [section_8_2_method_c_huber_optimization_study.md] for detailed mathematical justification and strategy evaluation).
> 

##### Empirical Calibration & Optimization Study Reference

The physical parameters of Method C (`eta_low`, `C0_single`, `C0_dual`, `k`, `p`) were calibrated across 44 authentic smartphone laboratory benchmarks from GSMArena data using a robust Huber loss optimization framework (`delta = 0.0 mins / Pure MAE Primary`).

The complete mathematical derivation, statistical loss function theory, sensitivity sweeps, boundary interior checks, normalization constant strategy evaluations, and master 44-device prediction dataset are documented in [section_8_2_method_c_huber_optimization_study.md].

> [!NOTE]
> **Summary of Optimization Calibration Results:**
> * **Duration Precision (`T`-metrics):** Across all 44 benchmark devices, the calibrated Method C model achieves an overall Mean Absolute Error (`MAE_T`) of **9.91 minutes** and Root Mean Square Error (`RMSE_T`) of **15.26 minutes**.
> * **Standard Android Sub-Dataset:** Modern fast-charging smartphones (Samsung S-series, OnePlus, Xiaomi, Vivo, ROG Phone, Nothing, Pixel) achieve an average duration residual (`MAE_T`) of **5.97 minutes** (`RMSE_T = 10.34 mins`).
> * **Extreme Outliers & Vendor Firmware Tuning:** The largest duration residuals are concentrated in Apple iPhones and the LG G7 ThinQ (`MAE_T = 23.57 mins`, `RMSE_T = 25.73 mins`, likely driven by conservative vendor Battery Management System BMS thermal management policies and extended Constant Voltage CV trickle charging profiles) as well as specific Samsung mid-range hardware (Samsung Galaxy A55 and A54 exhibiting a `+37.7 minute` / `+59.8%` outlier residual compared to the Galaxy A34 baseline due to Exynos PMIC charging controller tuning differences).
> * **Normalized Speed Score Accuracy (`S`-metrics under Strategy 2):** Converting physical duration predictions into speed scores via Benchmark-Aligned Normalization Constants (`T_min = 9.0 mins`, `T_max = 241.0 mins`) achieves a Mean Absolute Score Error (`MAE_S`) of **0.453 points** (on a 0.0 to 10.0 scale) and near-zero overall score bias (`Mean_dS = -0.024 points`) with zero clipping.
> 
> For historical traceability, an earlier exploratory 12-parameter calibration study is preserved in [section_8_2_method_c_mse_huber_optimization_study.md]. That early model was discarded because its unconstrained 12-parameter optimization suffered from severe over-parameterization, parameter instability, and physically unviable parameter values (such as inverted protocol efficiency hierarchies), whereas the active 5-parameter model delivers stronger physical grounding through a significantly simpler architecture while achieving comparable accuracy against empirical benchmark data.


#### 8.2.2 Ecosystem Interoperability & Advanced Hardware Features
Evaluates hardware features and charging ecosystem openness that are not reflected in single-charger laboratory speed benchmarks.

##### 8.2.2.A Universal Protocol Interoperability Score (`S_interoperability`, 9% Weight)
Evaluates charging ecosystem freedom by calculating the continuous ratio of maximum power accessible via open, non-proprietary USB Power Delivery (USB-PD 3.0/3.1 Programmable Power Supply — PPS or fixed PD) relative to the device's peak rated wattage (`P_peak`):

`S_interoperability = 10 * (P_universal_USB_PD / P_peak)` (Clamped 0.0 to 10.0)

*   `P_universal_USB_PD`: Maximum power input (in Watts) achieved when connected to a standard, open USB Power Delivery charger.
*   `P_peak`: Maximum peak rated wired charging power input (in Watts) accepted by the smartphone hardware using official proprietary adapters (identical to `P_peak` in Section 8.2.1).

###### Sourcing Hierarchy & Evidence Verification Rules
To guarantee maximum data reproducibility, resolve unannounced USB-PD fallback wattages, and eliminate brand bias (as highlighted by industry analyses from AndroidAuthority and ChargerLAB), `P_universal_USB_PD` MUST be extracted using the following **6-Tier Evidence Hierarchy**:

1. **Tier 1 — Official Manufacturer Datasheet / Technical Specification Manual:** Published explicit USB-PD / PPS wattage limits.
2. **Tier 2 — USB-IF (USB Implementers Forum) Official Certified Product Database:** Verified USB-PD 3.0 / 3.1 PPS compliance profiles.
3. **Tier 3 — ChargerLAB (POWER-Z Hardware Protocol Analyzer Logs):** Empirical VBUS/CC line power negotiation measurements.
4. **Tier 4 — GSMArena Laboratory Reviews:** Verified third-party charger compatibility logs.
5. **Tier 5 — Notebookcheck Hardware Reviews:** Oscilloscope and power meter charging protocol tests.
6. **Tier 6 — AndroidAuthority Charging Deep-Dives:** Empirical USB-PD vs. proprietary brick comparative measurements.

###### Deterministic Multi-Tier Fallback Rules for Universal Charging Wattage
When explicit empirical or manufacturer documentation (Tiers 1–6) is not yet available for a device, `P_universal_USB_PD` is resolved deterministically using a conservative multi-tier physical decision tree:

1. **Explicit Measured / Documented Power (`P_measured` / `P_documented`):**
   If verified data exists in Tiers 1–6 (datasheets, USB-IF certified profiles, POWER-Z logs, or laboratory reviews), set `P_universal_USB_PD = P_measured`. Explicit empirical evidence MUST NEVER be overridden by fallback rules.

2. **USB-PD Supported, but Maximum Wattage Unspecified:**
   If official specifications confirm USB Power Delivery (USB-PD / PPS) support but omit the numerical wattage limit:
   `P_universal_USB_PD = min(P_peak, P_era)`

   *Where `P_era` is a conservative, year-dependent ceiling representing the evolution of the USB-PD ecosystem:*
   *   **2016–2017:** `P_era = 10.0 W` (Legacy 5V/2A early USB-PD 2.0 adoption; e.g. Google Pixel 1st gen)
   *   **2018–2019:** `P_era = 15.0 W` (Standard 5V/3A baseline USB-PD profile; e.g. Pixel 3, early Samsung PD)
   *   **2020–2021:** `P_era = 20.0 W` (USB-PD 3.0 / early PPS adoption; e.g. Pixel 5 at 18W, Samsung S20 at 25W PD PPS)
   *   **2022–2023:** `P_era = 25.0 W` (Mainstream PD 3.0 PPS; e.g. Samsung S22/S23 at 25W, Pixel 7/8 at 21W–27W)
   *   **2024–2026:** `P_era = 30.0 W` (Mature PD 3.1 PPS ecosystem; e.g. Pixel 9 Pro at 27W–37W, Samsung S24 Ultra at 45W)

3. **USB Type-C Present, but No Evidence of USB-PD Support:**
   If the device features a USB Type-C port but lacks documented USB-PD protocol support (e.g., proprietary legacy fast-charging only):
   `P_universal_USB_PD = min(P_peak, 15.0 W)` (USB Type-C specification maximum without PD: 5V/3A via CC pin current advertisement).

4. **Legacy Micro-USB / Proprietary Connector without Universal Fast Charging:**
   If the device uses a Micro-USB port without universal fast-charging support:
   `P_universal_USB_PD = min(P_peak, 5.0 W)` (Standard 5V/1A USB BC 1.2 trickle charging).

5. **No Open/Universal USB Charging Compatibility:**
   If the device lacks any open USB charging compatibility:
   `P_universal_USB_PD = 0.0 W`.

> [!NOTE]
> **Industry Prevalence of Unspecified USB-PD Fallback Wattages:**
> Official OEM datasheets frequently state that a device supports open USB Power Delivery (USB-PD / PPS) while deliberately omitting the exact numerical wattage limit. This occurs because manufacturers prioritize highlighting headline proprietary fast-charging speeds (e.g., OnePlus 100W SUPERVOOC, Xiaomi 120W HyperCharge, Vivo 120W FlashCharge) to drive proprietary wall-charger accessory sales, or omit peak limits entirely to avoid regulatory over-promising (e.g., Apple iPhone spec sheets list *"Fast-charge capable"* without publishing maximum numerical PD wattages). 
> **Data Availability & Structural Monotonicity Rationale:**
> All required inputs for this decision tree—launch release year, USB port type, USB-PD claim status, and peak rated wattage (`P_peak`)—are 100% public data fields available across standard smartphone specification databases (such as GSMArena). Formulating all fallback rules with the physical minimum cap `min(P_peak, P_fallback)` guarantees complete structural coherence and strict monotonicity across capability tiers: `Explicit Logged PD >= Unspecified PD >= Basic Type-C >= Micro-USB >= Proprietary Only`. The `P_era` progression (10 → 15 → 20 → 25 → 30 W) tracks the real-world evolution of the USB-PD ecosystem validated against ChargerLAB and AndroidAuthority empirical data, while high-power proprietary flagships (120W–240W) default to conservative physical ceilings until Tiers 1–6 logs verify higher negotiated power levels.


##### 8.2.2.B Hardware Bypass Charging / Direct Drive Feature Score (`S_bypass`, 3% Weight)
Evaluates hardware capability to route electrical current directly from the wall charger to system components (PMIC/logic board), completely bypassing the battery cell during plugged-in high-load use (gaming, GPS navigation, mobile hotspot tethering):

| Score    | Bypass Charging Class                  | Support Status                             |
| :------: | :------------------------------------- | :----------------------------------------- |
| **10.0** | **Hardware Bypass Charging Supported** | Supported natively in firmware/hardware    |
| **0.0**  | **No Bypass Charging**                 | Always routes current through battery cell |

*Detailed Bypass Class Definitions & Examples:*
*   **10.0 — Hardware Bypass Charging Supported:** Supported natively in firmware/hardware (e.g. Samsung Game Booster "Pause USB Power Delivery", ASUS ROG "Bypass Charging", Sony Xperia "H.S. Power Control", Black Shark, RedMagic, Infinix Bypass Charge). Power flows directly from wall brick to logic board, skipping battery to eliminate heat during gaming, GPS navigation, or hotspot tethering.
*   **0.0 — No Bypass Charging:** Device always routes electrical current through the battery cell, causing thermal buildup and accelerated battery degradation during concurrent heavy use and charging.


#### 8.2.3 Composite Section Score Calculation
The final Section 8.2 score combines pure wired charging speed (`S_speed`), universal protocol interoperability (`S_interoperability`), and hardware bypass charging (`S_bypass`):

`Final Score 8.2 = 0.88 * S_speed + 0.09 * S_interoperability + 0.03 * S_bypass` (Clamped 0.0 to 10.0)


#### 8.2.4 Model Validation Worked Examples
Below are 2 detailed, verified worked examples evaluating real-world flagship devices across Method A (Empirical GSMArena Benchmark) and Method C (Analytical Physics Predictor), calculating the final composite section score.

##### Example 1: Samsung Galaxy S24 Ultra (45W Universal Fast Charging)
*   **Empirical Source:** [GSMArena Samsung Galaxy S24 Ultra Review — Charging Test](https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2670p3.php)
*   **Verified Benchmark Data (`T_GSMArena`):** `65.0 minutes` (0% to 100% full charge time using official 45W USB-PD PPS charger; 69% reached in 30 minutes).
*   **Hardware Specifications:**
    *   `P_peak`: `45.0 W`
    *   `Capacity_mAh`: 5,000 mAh at 3.85V (`E_supply = 19.25 Wh`)
    *   `Cell Architecture`: Single-Cell (`C0_single = 0.4051 h^-1`)
    *   `P_universal_USB_PD`: `45.0 W` -> `S_interoperability = 10.0 * (45.0 / 45.0) = 10.00`
    *   `S_bypass`: `10.00` (Supports Game Booster "Pause USB Power Delivery" direct drive)
*   **Step-by-Step Method C Speed Calculations:**
    1. *Continuous C-Rate:* `C_rate = 45.0 / 19.25 = 2.3377 h^-1`
    2. *Continuous Full-Cycle Power Retention Factor (`F_system`):*
       `F_system = min(1.0, 0.9679 / (1.0 + 1.1265 * max(0, 2.3377 - 0.4051)^0.1344)) = 0.9679 / (1.0 + 1.1265 * 1.0918) = 0.4339`
    3. *Average Effective Full-Cycle Power:*
       `P_effective = 45.0 * 0.4339 = 19.52 W`
    4. *Method C Predicted Duration (`T_predicted`):*
       `T_predicted = (19.25 / 19.52) * 60 = 59.2 minutes`
*   **Method A vs. Method C Alignment Comparison:**
    *   *Method A Pure Speed Score (Empirical `T_GSMArena = 65.0 min`):* `S_speed_MethodA = 10 * (log(241.0) - log(65.0)) / (log(241.0) - log(9.00)) = 3.99`
    *   *Method C Pure Speed Score (Analytical Physics `T_predicted = 59.2 min`):* `S_speed_MethodC = 10 * (log(241.0) - log(59.2)) / (log(241.0) - log(9.00)) = 4.27`
    *   *Method A Final Composite Score:*
        `Final Score 8.2 = 0.88 * 3.99 + 0.09 * 10.00 + 0.03 * 10.00 = 3.51 + 0.90 + 0.30 = 4.71`
    *   *Method C Final Composite Score (Fallback):*
        `Final Score 8.2 = 0.88 * 4.27 + 0.09 * 10.00 + 0.03 * 10.00 = 3.76 + 0.90 + 0.30 = 4.96`

##### Example 2: Xiaomi 13 Pro (120W Dual-Cell Proprietary Direct Charge)
*   **Empirical Source:** [GSMArena Xiaomi 13 Review — Charging Test](https://www.gsmarena.com/xiaomi_13-review-2531p3.php)
*   **Verified Benchmark Data (`T_GSMArena`):** `19.0 minutes` (0% to 100% full charge time in 120W Boost Mode).
*   **Hardware Specifications:**
    *   `P_peak`: `120.0 W`
    *   `Capacity_mAh`: 4,820 mAh at 3.85V (`E_supply = 18.56 Wh`)
    *   `Cell Architecture`: Dual-Cell (`C0_dual = 2.6813 h^-1`)
    *   `P_universal_USB_PD`: `65.0 W` -> `S_interoperability = 10.0 * (65.0 / 120.0) = 5.42`
    *   `S_bypass`: `0.00` (No native hardware bypass charging)
*   **Step-by-Step Method C Speed Calculations:**
    1. *Continuous C-Rate:* `C_rate = 120.0 / 18.56 = 6.4655 h^-1`
    2. *Continuous Full-Cycle Power Retention Factor (`F_system`):*
       `F_system = min(1.0, 0.9679 / (1.0 + 1.1265 * max(0, 6.4655 - 2.6813)^0.1344)) = 0.9679 / (1.0 + 1.1265 * 1.1979) = 0.4124`
    3. *Average Effective Full-Cycle Power:*
       `P_effective = 120.0 * 0.4124 = 49.49 W`
    4. *Method C Predicted Duration (`T_predicted`):*
       `T_predicted = (18.56 / 49.49) * 60 = 22.5 minutes`
*   **Method A vs. Method C Alignment Comparison:**
    *   *Method C Pure Speed Score:* `22.5 minutes` -> `S_speed_MethodC = 10 * (log(241.0) - log(22.5)) / (log(241.0) - log(9.00)) = 7.21`
    *   *Method A Pure Speed Score:* `19.00 minutes` -> `S_speed_MethodA = 10 * (log(241.0) - log(19.00)) / (log(241.0) - log(9.00)) = 7.73`
    *   *Method A Final Composite Score:*
        `Final Score 8.2 = 0.88 * 7.73 + 0.09 * 5.42 + 0.03 * 0.00 = 6.80 + 0.49 + 0.00 = 7.29`
    *   *Method C Final Composite Score (Fallback):*
        `Final Score 8.2 = 0.88 * 7.21 + 0.09 * 5.42 + 0.03 * 0.00 = 6.34 + 0.49 + 0.00 = 6.83`


### 🔹 8.3 Wireless Charging System
*Description:* Comprehensive evaluation of the wireless charging system, prioritizing real-world convenience and compatibility. Scores are derived from a theoretical speed prediction, universal interoperability with public standards (Qi/Qi2), and the physical convenience and efficiency of magnetic alignment.
*   **Measurement:** Technical predicted charge duration in minutes (`T_predicted_wireless`), open universal charging power (`P_universal_wireless`), and magnetic hardware support tiers.
*   **Unit:** Composite Score (0.0 to 10.0)
*   **Significance:** Ensures rapid wireless top-ups using proprietary gear, guarantees compatibility with public/automotive wireless pads, and drastically improves convenience through reliable magnetic alignment.

#### 8.3.0 Executive Framework Overview & Weights
Because there is no widespread, standardized 0-100% empirical benchmark database for wireless charging, a hybrid approach combining measured times (for some phones) and theoretical predictions (for others) would introduce unacceptable bias (due to unmeasured real-world thermal throttling). Therefore, the overall Section 8.3 score uses a **100% Analytical Predictive Model** combined with hardware feature tiers:

1. **Pure Wireless Charging Speed (`S_speed` — 40% Weight):**
   * **What it measures:** The theoretical minimum physical duration required to charge the battery using the device's maximum supported wireless wattage, governed by a dedicated wireless thermal calibration curve and technology-specific transfer efficiencies.
   * **Why & Weight Rationale (40%):** Represents the fastest possible wireless charging speed. While important, empirical user sentiment data shows users prioritize reliable universal compatibility over raw proprietary speed for wireless charging, hence its de-prioritization relative to wired charging speed.

2. **Universal Open Standard Interoperability (`S_universal` — 40% Weight):**
   * **What it measures:** How well the phone charges on common, third-party chargers—like the ones built into cars, coffee shop tables, or affordable nightstand docks—that aren't made by the phone's manufacturer. It scores the phone's charging speed on these public "open standard" (Qi/Qi2) pads against a 25W gold standard. The stakes are high for consumers: a phone might advertise an incredible "80W" charging speed on the box, but if it requires an expensive, proprietary dock to achieve that, it might drop to a painfully slow 5W on your car's built-in pad. This metric rewards phones that charge quickly on *any* standard charger, protecting users from being locked into a single expensive accessory ecosystem.
   * **Why & Weight Rationale (40%):** Wireless charging is valued primarily for convenience and compatibility (cars, furniture, airports). A device that charges at 80W on a proprietary dock but drops to 5W on a generic pad provides a degraded real-world experience and is penalized here.

3. **Magnetic Alignment Capability (`S_alignment` — 20% Weight):**
   * **What it measures:** Whether the phone has built-in magnets around its wireless charging receiver (like Apple's MagSafe or the new Qi2 standard) that allow it to snap perfectly into place on a charger. It evaluates if the phone supports this effortlessly out of the box, or if it requires you to buy a specific manufacturer case to get the magnetic effect.
   * **Why & Weight Rationale (20%):** The biggest frustration with older wireless charging is waking up to a dead phone because it was bumped slightly off-center during the night. Misalignment causes the charging pads to struggle, generating massive amounts of waste heat that slows down the charge and degrades battery health. Magnets solve this problem entirely by guaranteeing perfect alignment every single time. Beyond charging, they also unlock a highly convenient ecosystem of snap-on accessories, like floating car dash mounts, magnetic wallets, and attachable power banks.

##### Section 8.3 Overall Composite Formula
*   If the device does not support wireless charging, the score is mathematically zeroed:
    `Final Score 8.3 = 0.00`
*   If the device supports wireless charging:
    `Final Score 8.3 = 0.40 * S_speed + 0.40 * S_universal + 0.20 * S_alignment` (Clamped 0.0 to 10.0)

#### 8.3.1 Pure Wireless Charging Speed (`S_speed`)
Wireless speed relies exclusively on an **Analytical Physics Predictor (Method C)** calibrated specifically for wireless inductive and thermal losses.

1. **Continuous C-Rate:** 
   First, evaluate the total stored nominal battery energy capacity (`E_supply`) in Watt-hours (Wh):
   `E_supply = (Capacity_mAh * V_nominal) / 1000`
   
   *(Note: Sourced directly from Section 8.1. Refer to Section 8.1 for the complete determination logic governing nominal voltage `V_nominal` and battery cell architecture).*
   
   Then, calculate the continuous wireless C-Rate (in reciprocal hours, `h^-1`):
   `C_rate_wireless = P_wireless_max / E_supply`
   
2. **Dedicated Wireless Thermal Factor (`F_thermal_wireless`):** 
   Wireless charging generates distinct thermal penalties compared to wired charging, with heat from induction coils causing earlier and steeper thermal throttling. We apply a dedicated phenomenological thermal curve optimized to real-world datasets using the following wireless-specific calibration constants:
   *   Threshold `C0_w` = 0.7778
   *   Penalty scaling `k_w` = 1.1232
   *   Exponent `p_w` = 0.2194
   
   `F_thermal_wireless = 1 / (1 + k_w * max(0, C_rate_wireless - C0_w)^p_w)`

3. **Transfer Efficiency (`F_transfer`):** 
   This coefficient models the baseline energy lost to electromagnetic flux leakage and hardware-level inductive coupling inefficiencies. While the separate `F_thermal_wireless` factor models the phone battery's dynamic thermal throttling when receiving high wattage, `F_transfer` acts as a static hardware modifier representing how well the charger's physical design (e.g., magnetic alignment or active cooling fans) preserves efficiency before the power even enters the phone.
   
   The framework defines 4 physical efficiency tiers. The fundamental physical reasons for these efficiency differences are as follows:

   *   **Tier 1: Active Cooling (0.83):** Highest efficiency. The charging base contains a physical fan. By actively forcing ambient air over the transmitting induction coils, the system lowers the baseline electrical resistance of the copper, offering the highest static transfer efficiency before the power even reaches the phone.
   *   **Tier 2: Magnetic Alignment (0.82):** Hardware-enforced magnetic alignment guarantees that the transmitter and receiver coils are 100% concentric. In standard wireless charging, being off-center by even a few millimeters causes massive magnetic flux leakage. Magnets mathematically eliminate this misalignment variance, ensuring near-perfect static coupling. *(Note: Modeling this 0.82 efficiency gain is not double-counting with the `Magnetic Alignment Capability` (`S_alignment`) score; `F_transfer` strictly models the **electrical physics** required to accurately predict real-world charging speed, while the `S_alignment` metric independently scores the **convenience of the magnetic accessory ecosystem** (e.g., snap-on car mounts and wallets). Additionally, the dynamic thermal penalty of high wattage is handled by `F_thermal_wireless`).*
   *   **Tier 3: Advanced Passive (0.78):** Uses advanced 2-way communication profiles (like Qi EPP or Proprietary optimized protocols) for efficient power negotiation, but lacks fans or magnets. The average real-world placement by a user is always slightly off-center, leading to unavoidable moderate flux leakage. This tier covers all modern passive chargers (from standard 15W Qi up to proprietary 50W passive stands). *Note: Their static coupling efficiencies are identical; the thermal consequence of pushing higher peak power is handled entirely by the `F_thermal_wireless` equation to prevent double-counting.*
   *   **Tier 4: Basic Qi BPP (0.72):** Lowest efficiency. Uses the legacy Qi Baseline Power Profile (BPP) limited to 5W. Unlike modern profiles, BPP relies on primitive one-way communication (the receiver can only send basic "power up/down" pulses to the transmitter) and older coil standards. This lack of precise power negotiation results in the highest proportion of baseline energy being lost to poor inductive coupling.

   *(Note: For the exact categorization rules and edge-case precedence, refer to the `proposed_data_structure.md` file.)*

4. **Average Effective Power (`P_effective_wireless`):** 
   `P_effective_wireless = P_wireless_max * F_transfer * F_thermal_wireless`

5. **Predicted Duration (`T_predicted_wireless`):** 
   `T_predicted_wireless = 60 * (E_supply / P_effective_wireless)`

*   **Speed Component Score (`S_speed`):**
    The predicted time is then normalized using a **Logarithmic Utility** curve *(refer to Section 8.2.1.A.3 "Charging Speed Component Score" for the justification of applying logarithmic utility normalization to charging times)*:
    `S_speed = 10 * (log(Battery_Wireless_Charge_Time_Max_Mins) - log(T_predicted_wireless)) / (log(Battery_Wireless_Charge_Time_Max_Mins) - log(Battery_Wireless_Charge_Time_Min_Mins))` (Clamped 0.0 to 10.0)

**Huber Optimization Study & Validation Cases:**
These parameters were determined via a Huber loss optimization study against real-world 0-100% wireless charging tests. The full Python optimization script, dataset, and generated thermal curve plots are maintained in the repository at `docs/modeling/section_8_3_method_c_huber_optimization_study/optimizer.py`. We selected a Huber loss `delta` of `10.0` (errors under 10 minutes are penalized quadratically, while larger errors are penalized linearly to prevent extreme outliers from skewing the curve).

**Huber Delta Sensitivity Analysis:**

| Huber Delta | `k`    | `p`    | `c0`   | Bias (mins) | MAE (mins) | RMSE (mins) | Max Err (mins) |
| :---------- | :----- | :----- | :----- | :---------- | :--------- | :---------- | :------------- |
| 0.0 (L1)    | 0.9769 | 0.4084 | 0.5761 | +0.89       | 13.77      | 18.18       | 30.21          |
| 2.5         | 1.1567 | 0.2627 | 0.7755 | -1.63       | 7.97       | 12.22       | 23.06          |
| 5.0         | 1.1446 | 0.2471 | 0.7765 | -1.67       | 8.20       | 12.05       | 22.90          |
| 7.5         | 1.1334 | 0.2327 | 0.7773 | -1.69       | 8.42       | 11.92       | 22.75          |
| 10.0        | 1.1232 | 0.2194 | 0.7778 | -1.68       | 8.62       | 11.85       | 22.60          |
| 12.5        | 1.1197 | 0.2090 | 0.7782 | -1.53       | 8.80       | 11.78       | 22.25          |
| 15.0        | 1.1527 | 0.2115 | 0.7783 | -0.56       | 8.83       | 11.57       | 20.72          |
| 17.5        | 1.1855 | 0.2137 | 0.7783 | +0.41       | 8.87       | 11.47       | 19.18          |
| 20.0        | 1.1992 | 0.2146 | 0.7783 | +0.81       | 8.88       | 11.46       | 18.54          |
| 22.5        | 1.1992 | 0.2146 | 0.7783 | +0.81       | 8.88       | 11.46       | 18.54          |
| 25.0        | 1.1992 | 0.2146 | 0.7783 | +0.81       | 8.88       | 11.46       | 18.54          |

> [!NOTE]
> **Observation on L1 vs. Huber Convergence:** While optimizing for pure L1 loss (`delta=0.0`) should theoretically produce the lowest MAE, the sharp, non-differentiable bottom of the L1 curve causes the gradient-descent solver to fail and get stuck in a poor local minimum (`MAE=13.77`). By slightly rounding the bottom of the curve (`delta=2.5`), the solver gains the smooth gradients needed to mathematically converge, achieving the true lowest error (`MAE=7.97`). We ultimately adopt `delta=10.0` as our baseline to maintain generalized stability and prevent overfitting to our sample data.

These `delta=10.0` parameters yield a predictive MAE of 8.62 minutes across diverse brands and power levels:

| Device                   | Cap (mAh) | V_nom (V) | E_wh    | P_max (W) | C_rate | F_trans | F_therm | P_eff (W) | T_act (m) | T_pred (m) | Err (m) | Err (%) |
| :----------------------- | :-------- | :-------- | :------ | :-------- | :----- | :------ | :------ | :-------- | :-------- | :--------- | :------ | :------ |
| Xiaomi 14 Ultra          | 5000      | 3.85      | 19.2500 | 80        | 4.1558 | 0.83    | 0.4053  | 26.9119   | 46        | 42.9       | -3.1    | -6.7%   |
| OnePlus 12               | 5400      | 3.85      | 20.7900 | 50        | 2.4050 | 0.83    | 0.4445  | 18.4468   | 55        | 67.6       | +12.6   | +22.9%  |
| Samsung Galaxy S24 Ultra | 5000      | 3.85      | 19.2500 | 15        | 0.7792 | 0.78    | 0.7901  | 9.2442    | 125       | 124.9      | -0.1    | -0.1%   |
| iPhone 15 Pro Max        | 4422      | 3.85      | 17.0247 | 15        | 0.8811 | 0.82    | 0.5943  | 7.3099    | 135       | 139.7      | +4.7    | +3.5%   |
| Google Pixel 8 Pro       | 5050      | 3.85      | 19.4425 | 23        | 1.1830 | 0.83    | 0.5205  | 9.9363    | 140       | 117.4      | -22.6   | -16.1%  |

**Input Sources & Categorization for Validation Cases:**
*   **Xiaomi 14 Ultra:** 5000 mAh, 80W max. Uses the official Xiaomi 80W cooling-fan stand (fan built into the base) -> `F_trans` = 0.83.
*   **OnePlus 12:** 5400 mAh, 50W max. Uses the official OnePlus 50W AirVOOC cooling-fan stand (fan built into the base) -> `F_trans` = 0.83.
*   **Samsung Galaxy S24 Ultra:** 5000 mAh, 15W max. Uses standard 15W wireless chargers (no active fan) -> `F_trans` = 0.78.
*   **iPhone 15 Pro Max:** 4422 mAh, 15W max. Uses the Apple MagSafe puck (perfect magnetic alignment) -> `F_trans` = 0.82.
*   **Google Pixel 8 Pro:** 5050 mAh, 23W max. Uses the official Google Pixel Stand 2nd Gen (which features a built-in cooling fan in its base) -> `F_trans` = 0.83.

#### 8.3.2 Universal Open Standard Interoperability (`S_universal`)
Measures the highest charging power the phone itself accepts using an open Qi-family standard *without* a manufacturer-specific wireless protocol.
*   **Formula:** `S_universal = 10 * P_universal_wireless / P_universal_wireless_max` (Clamped 0.0 to 10.0)
*   **Parameters:**
    *   `P_universal_wireless`: The highest supported wattage on open Qi/Qi2 standards (typically 5W, 7.5W, 10W, 15W, or 25W).
    *   `P_universal_wireless_max` (Constant): The gold standard universal open Qi2 wattage benchmark, set to `25.0` W.

> [!NOTE]
> **Crucial Parameter Distinction:**
> *   `P_wireless_max` represents the absolute maximum wireless charging power (including proprietary systems, e.g., 80W) that the phone is capable of accepting. It is used in 8.3.1 (`S_speed`) to calculate raw speed.
> *   `P_universal_wireless` represents the highest charging power the phone accepts specifically on open, non-proprietary standards (Qi/Qi2). It is compared to the universal benchmark constant `P_universal_wireless_max` (25.0 W) in 8.3.2 (`S_universal`).
> This distinction ensures that a phone with a massive proprietary charging speed does not artificially inflate its universal compatibility score.

#### 8.3.3 Magnetic Alignment Capability (`S_alignment`)
Measures the device's official magnetic alignment capability, evaluating how reliably the charging system maintains optimal coil alignment and supports magnetic mounting/accessories.
*   **Formula:** Tiered assignment based on verified official capability.
    *   **10.0 (Tier 1: Native Qi2 (MPP) / MagSafe):** Requires native Magnetic Power Profile (MPP) hardware built into the phone. Includes Apple MagSafe on iPhone 12-17 and Qi2 MPP certified Androids.
    *   **8.0 (Tier 2: Native Proprietary Magnetic):** Requires built-in magnets intended for charging alignment, but relies on a proprietary ecosystem rather than Qi2 MPP (e.g., Realme MagDart).
    *   **5.0 (Tier 3: OEM Magnetic Case Required):** The phone lacks built-in charging magnets but officially supports a first-party/OEM-certified magnetic case to achieve alignment. Generic third-party aftermarket rings/cases do NOT qualify.
    *   **0.0 (Tier 4: No official magnetic alignment):** Standard induction coil only. Device supports wireless charging but lacks any qualifying native or OEM magnetic alignment.

> [!NOTE]
> **Methodological Justification for Tiers & Ambiguity Limits:**
> A strict conceptual boundary separates "native hardware" from "official capability". By evaluating *capability*, Tier 3 correctly rewards manufacturers who explicitly engineer a case-based magnetic ecosystem (e.g., Huawei, OnePlus), while explicitly punishing reliance on generic third-party aftermarket stickers/cases. Additionally, stringent ambiguity rules (detailed in the data schema) mandate that "Qi2 Ready" marketing or the mere physical presence of magnets (e.g., for speakers or cameras) do NOT automatically grant Tier 1 or Tier 2 scores without explicit documentation of charging alignment intent.


### 🔹 8.4 Wired Reverse Charging System
*Description:* Comprehensive evaluation of the wired reverse charging system, measuring the smartphone's ability to act as a physical power bank to charge external devices (such as wireless earbuds, other smartphones, or tablets) via a Universal Serial Bus Type-C (USB-C) cable.
*   **Measurement:** Peak continuous power output via USB-C port (`P_reverse_wired`) combined with verified source-mode protocol capability (`S_protocol`).
*   **Unit:** Composite Score (0.0 to 10.0) derived from Watts (W) and categorical source protocol tiers.
*   **Significance:** Enables asynchronous emergency top-ups for secondary devices. High-power output allows for charging larger devices (tablets, laptops), while verified open source protocols (like Universal Serial Bus Power Delivery — USB-PD) ensure safe, standardized power negotiation between host and recipient.

#### 8.4.0 Executive Framework Overview & Core Component Definitions
To provide a complete and transparent evaluation, the overall Section 8.4 score is derived from **two distinct, non-overlapping hardware components**:

1. **Pure Power Output Score (`S_power` — 80% Weight):**
   * **What it measures:** The highest verified continuous electrical power output in Watts (`P_reverse_wired`) the smartphone can deliver from its physical port to an externally connected device in a reverse-power / source configuration under documented operating conditions.
   * **Why & Weight Rationale (80%):** The raw amount of energy transferred per minute is the dominant physical driver of user utility. A 30W output can viably charge a tablet or rapidly rescue a depleted smartphone, whereas a 2.5W output is strictly limited to slow trickle-charging low-capacity wearables.

2. **Protocol Interoperability Score (`S_protocol` — 20% Weight):**
   * **What it measures:** The highest verified USB power-source capability supported by the host device during reverse power transfer (`S_protocol`), evaluating host-side communication standards (open USB-PD Source versus Type-C CC pin current advertisement versus legacy USB On-The-Go — OTG 5V current dumping).
   * **Why & Weight Rationale (20%):** High wattage without standardized protocol handshaking creates thermal strain and compatibility risks. Smart source-side protocols guarantee open interoperability across third-party accessories and enable safe power negotiation.

##### Section 8.4 Overall Composite Formula
`Final Score 8.4 = 0.80 * S_power + 0.20 * S_protocol` (Clamped 0.0 to 10.0)

> [!IMPORTANT]
> **Strict Source-Side Evaluation & Boundary Rules:**
> 1. **Source vs. Sink Separation:** Inbound charging capability (e.g. accepting 45W USB-PD from a wall charger) MUST NEVER be used to infer outbound reverse charging capability. Dual-Role Power (DRP) controllers can support high-wattage inbound charging while capping outbound reverse charging to basic 5V rails.
> 2. **Inclusions (Count):** Phone acting as a power source via a physical cable to external devices (phone to earbuds, phone to phone, phone to smartwatch, phone to tablet, or phone to active USB peripheral).
> 3. **Exclusions (Do Not Count):** Inbound wall charging, wireless reverse charging (scored separately in Section 8.5), proprietary dock outputs where the phone is not sourcing through its physical port, and passive USB peripherals that do not establish the phone as an active power source.

#### 8.4.1 Component 1: Pure Power Output (`S_power`)
Evaluates the continuous energy transfer capability during reverse charging using a **Logarithmic Benchmark Normalization Formula**:

`S_power = 10 * (log(P_reverse_wired + 1) - log(Battery_Reverse_Wired_W_Min + 1)) / (log(Battery_Reverse_Wired_W_Max + 1) - log(Battery_Reverse_Wired_W_Min + 1))` (Clamped 0.0 to 10.0)

*   `P_reverse_wired`: The highest explicitly documented or lab-tested continuous source power output available from the physical port in Watts (W).
*   `Battery_Reverse_Wired_W_Min` and `Battery_Reverse_Wired_W_Max`: Normalization constants defined in `scoring_constants.md`.

> [!NOTE]
> **Why Logarithmic Utility Normalization for Reverse Charging?**
> The primary real-world use case for reverse wired charging is performing emergency top-ups for small wearables (such as TWS earbuds or smartwatches) or giving a dead phone just enough battery to make an emergency call.
> 
> Most wearables physically bottleneck inbound charging at 2W–5W. Because of this hardware limitation, a 30W source provides virtually zero additional utility over a 5W source when charging these devices. The jump from 0W (no capability) to 4.5W (basic Type-C) yields massive "zero-to-one" utility, whereas the jump from 15W to 30W yields steeply diminishing returns (only benefiting the rare edge-case of fast-charging another full-sized smartphone). Logarithmic normalization perfectly captures this reality, heavily rewarding baseline support while properly tapering off at excessive wattages.
> 
> *(Mathematical Note: The `+ 1` offset inside the `log()` functions prevents a mathematical undefined error (negative infinity) when wattage is 0.0 W, safely anchoring the baseline to exactly `log(1) = 0.0` points).*

#### 8.4.2 Component 2: Standard Protocol Interoperability (`S_protocol`)

Evaluates the verified source-side negotiation standards of the reverse charging connection. The score rewards the safety and universal compatibility of the underlying power transfer protocol.

| Score    | Protocol Class                                       | Scoring Justification                                                       |
| :------: | :--------------------------------------------------- | :-------------------------------------------------------------------------- |
| **10.0** | **USB Power Delivery (PD) Source**                   | Maximum interoperability and dynamic power scaling via digital negotiation. |
| **7.5**  | **USB Type-C Current Advertisement (Rp) Source**     | Safe, standardized analog current regulation, but lacks dynamic scaling.    |
| **3.0**  | **Legacy USB On-The-Go (OTG) Source**                | Basic 5V output; lacks modern safety handshakes and wide compatibility.     |
| **0.0**  | **No Wired Reverse Source**                          | Device provides zero power sourcing utility.                                |

*Detailed Engineering Justifications & Protocol Analysis:*
*   **10.0 — USB Power Delivery (PD) Source:** Represents the pinnacle of universal compatibility. The host device contains Dual-Role Power (DRP) controllers capable of broadcasting active USB-PD Power Data Objects (PDOs) over the Configuration Channel (CC) line using Biphase Mark Coding (BMC). This earns the maximum score because it allows two devices to digitally negotiate voltage and current in real-time, ensuring maximum charging speed for the sink device while guaranteeing absolute thermal and electrical safety for the source device.
*   **7.5 — USB Type-C Current Advertisement (Rp) Source:** A robust and safe modern standard that earns a high score for utilizing standardized Type-C Configuration Channel (CC) pin pull-up resistors (`Rp`) to advertise source current levels (such as 1.5A or 3.0A). It is scored lower than USB-PD because it relies on static analog advertisement rather than dynamic digital negotiation, meaning it cannot adjust voltages on the fly or communicate advanced power profiles, but it still guarantees safe and reliable power delivery across all modern Type-C hardware.
*   **3.0 — Legacy USB On-The-Go (OTG) Source:** Represents legacy host power output originally designed for low-drain computer peripherals (such as computer mice or flash drives) via 5V VBUS rails (e.g., 500mA USB 2.0 standard). It receives a low baseline score because it lacks modern Type-C CC current advertisement or USB-PD source handshaking, resulting in very slow charge speeds and a lack of intelligent safety negotiation when connected to modern smartphones or wearables.
*   **0.0 — No Wired Reverse Source:** The device hardware or firmware does not support power sourcing via its physical port, yielding zero utility.


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
