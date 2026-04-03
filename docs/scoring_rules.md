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
> **Why this weighting is explicit:** The frame governs structural rigidity, torsional strength, and thermal conduction pathways more than the back panel, which mainly affects surface durability, radio transparency, and impact shatter behavior.

#### 1.1.A Frame Material (Structural Class)
*   **Measurement:** Manufacturer specifications and teardown confirmation.
*   **Unit:** Material Class
*   **Significance:** Determines chassis rigidity and bending resistance.

| Score    | Frame Material Class       |
| :------- | :------------------------- | 
| **10.0** | **Titanium Alloy**         |  
| **8.5**  | **Stainless Steel**        |
| **7.0**  | **Aluminum Alloy**         |  
| **4.0**  | **Polymer Composite**      | 
| **0.0**  | **Material Not Disclosed** | 

**Titanium Alloy**: Titanium alloy structural frame; high strength-to-weight ratio, low thermal conductivity versus steel, high corrosion resistance
**Stainless Steel**: Steel alloy structural frame; very high rigidity and mass, high thermal conductivity, strong impact resistance
**Aluminum Alloy**: Aluminum structural frame; moderate rigidity, low mass, high thermal conductivity
**Polymer Composite**: Structural frame made from plastic or fiber-reinforced polymer; low thermal conductivity, lower stiffness than metals
**Material Not Disclosed**: Frame material not specified in official documentation or teardown sources

#### 1.1.B Back Panel Material (Surface Class)
*   **Measurement:** Manufacturer specifications and teardown confirmation.
*   **Unit:** Material Class
*   **Significance:** Affects scratch resistance, shatter risk, and radio signal transparency.

| Score    | Back Material Class        |
| :------- | :------------------------- | 
| **10.0** | **Ceramic**                |
| **8.0**  | **Strengthened Glass**     |
| **6.0**  | **Standard Glass**         |
| **4.0**  | **Polymer**                |
| **0.0**  | **Material Not Disclosed** |

**Ceramic**: Back panel made from ceramic or ceramic composite; high surface hardness, low radio frequency interference, high brittleness
**Strengthened Glass**: Chemically strengthened aluminosilicate glass (e.g., Gorilla Glass, Victus); moderate hardness, brittle fracture behavior
**Standard Glass**: Glass back without strengthened certification; similar brittleness with lower surface hardness
**Polymer**: Plastic or polymer rear panel; low brittleness, low surface hardness, high radio frequency transparency
**Material Not Disclosed**: Back material not specified in official documentation or teardown sources   

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


### 🔹 1.4 Thickness
*Description:* Device thickness excluding camera bump. Thinner phones are easier to hold and fit better in pockets.
*   **Measurement:** Calipers at the thickest point of the body (excluding camera protrusion).
*   **Unit:** Millimeters (mm)
*   **Significance:** Affects pocketability and hand comfort.
*Formula:* `Score = 10 - 10 * ((Thickness - Thickness_mm_Min) / (Thickness_mm_Max - Thickness_mm_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ Thickness_mm_Min
*   **Min Score (0.0):** ≥ Thickness_mm_Max
> [!NOTE]
> **Why Linear?** The discomfort of carrying a thick phone (in a pocket or in the hand) increases by the same amount with each extra millimeter. Think of it like a book: a 9mm hardcover is noticeably thicker than an 8mm one, and a 12mm brick is noticeably thicker than an 11mm one — the penalty is constant. There are no diminishing returns in the practical 6–12mm smartphone range, so a straight linear scale is the most honest model.

### 🔹 1.5 Weight
*Description:* Total device weight. Lighter phones are more comfortable to hold for long periods (e.g., reading, watching videos) without wrist strain.
*   **Measurement:** Digital scale weight including battery.
*   **Unit:** Grams (g)
*   **Significance:** Determines long-term holding comfort and fatigue.
*Formula:* `Score = 10 - 10 * ((Weight - Weight_g_Min) / (Weight_g_Max - Weight_g_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ Weight_g_Min
*   **Min Score (0.0):** ≥ Weight_g_Max
> [!NOTE]
> **Why Linear?** Wrist and arm fatigue from holding a phone scales approximately proportionally with weight — the same way a 200g book feels twice as heavy as a 100g booklet after an extended reading session. Within the practical 130–250g range that covers all modern smartphones, each additional gram adds a constant ergonomic cost. No diminishing returns apply here.

### 🔹 1.6 Ergonomics (Width & Handling)
*Description:* Quantifies the ergonomic handling cost of phone width for one-handed use. Wider phones are harder to grip and operate single-handedly, with the discomfort accelerating beyond a critical threshold tied to human hand anatomy. Note: the positive benefit of a wider phone (bigger screen) is already captured in Section 2.9 (Screen Size) and Section 2.8 (Screen-to-Body Ratio).
*   **Measurement:** Device Width
*   **Unit:** Millimeters (mm)
*   **Significance:** Beyond a critical threshold (~75–77mm), one-handed operation becomes difficult for a large share of users.
*Formula:* `Score = 10 * (1 - ((Width_mm - Width_mm_Min) / (Width_mm_Max - Width_mm_Min))^2)` (Clamped 0-10)
*   **Max Score (10.0):** ≤ Width_mm_Min
*   **Min Score (0.0):** ≥ Width_mm_Max
> [!NOTE]
> **Why Quadratic (not Linear)?** Research into hand anthropometry shows that phone width comfort is **not a constant penalty per millimeter** — it has a real physical threshold.
>
> **The data:** Average female hand width is 79–83mm; average male is 88–97mm. Modern phones range from 67.3mm (iPhone SE 4th gen) to 79.0mm (Galaxy S24 Ultra). This means:
> *   A phone under ~71mm is comfortable for almost every user — a linear scale would unfairly apply the same per-mm penalty here as in the uncomfortable range.
> *   A phone crossing 75–77mm starts causing grip adjustments for roughly 30% of users (most women and smaller-handed men).
> *   Beyond 78mm, the majority of users rely on two hands for basic navigation — a steep penalty applies.
>
> **The math:** A quadratic formula `(1 - x²)` stays near 10 in the comfortable narrow range and drops steeply as width approaches the maximum, mirroring this threshold-based reality. A linear scale would naively assign the same cost to going from 68mm to 69mm as to going from 77mm to 78mm, which is factually wrong.
>
> **Real-phone reference scores** (Min = 67.3mm, Max = 79.0mm):
>
> | Phone              | Width  | Score    |
> | :----------------- | :----- | -------: |
> | iPhone SE 4th gen  | 67.3mm | **10.0** |
> | Galaxy S24         | 70.6mm |  **9.2** |
> | iPhone 16          | 71.5mm |  **8.7** |
> | Galaxy S24+        | 75.9mm |  **5.3** |
> | Galaxy S24 Ultra   | 79.0mm |  **0.0** |
>
> *Note: The S24 Ultra scoring 0 on this specific metric is correct. Its large screen is already fully rewarded by Section 2.9 and Section 2.8. This metric scores solely the ergonomic handling cost.*


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
> **Why Quadratic?** The usable screen real estate scales as the *Area* of the display, which is proportional to the square of the diagonal ($Area \propto Diagonal^2$). While a linear penalty treats a 0.5" increase at the bottom of the scale exactly the same as at the top, a true geometric (Quadratic) curve exponentially rewards the massive manufacturing difficulty and user-experience gain of producing massive 6.8"+ "Ultra" screens.

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

#### Design Rationale & Methodology
Traditional SCC metrics require subjective hands-on testing that cannot be automated from public data. However, since bloatware and ad policies are defined universally at the **platform/skin level** (e.g., all Samsung One UI phones share the identical core app bundle and ad policy), we evaluate the **three distinct cleanliness dimensions** natively for each known skin. 

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
*   **Significance:** Directly impacts the perceived value and premium nature of the device by preventing intrusive monetization.

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

| CPU Core Architecture        | CPU Score | Ref Freq (GHz) | Generation | Notes                                      |
|------------------------------|:---------:|:--------------:|:----------:|--------------------------------------------|
| **Apple Everest (A18/Pro)**  | **10**    | **4.05**       | 2024-2025  | Highest mobile IPC, 3nm (N3E)              |
| **Oryon Gen 2 (SD 8 Elite)** | **10**    | **4.32**       | 2024-2025  | Qualcomm custom, massive IPC/Freq leap     |
| **Cortex-X925 / Lumex Ultra**| **9**     | **3.60**       | 2024-2025  | ARM Blackhawk, desktop-class IPC           |
| **Apple A17 Pro Cores**      | **9**     | **3.78**       | 2023       | 3nm (N3B), predecessor to Everest          |
- [...] *(See full list in [proposed_data_structure.md])*


### 🔹 6.1 CPU Multi-Core Performance (Sustained Outcome)
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
> [!NOTE]
> **Why Logarithmic?** Performance utility follows diminishing returns. A 1000-point jump between a baseline 1500-point phone and a capable 2500-point mid-ranger is transformative for daily usability. In contrast, a 1000-point jump between a 10000-point flagship and an 11000-point gaming beast is a marginal improvement noticeable only in extreme multitasking or specialized competitive gaming.

#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.
1.  **Identify Neighbors:** Find **3 distinct Reference Phones** that have **BOTH** Geekbench scores and known specs. Select the ones with the smallest **Distance** to the target device, **excluding the target device** itself:
    *   `Distance = abs(Diff_Predicted)`
    *   *Where Diff_Predicted = Predicted_Target - Predicted_Neighbor*
    *   *Note:* Based on **Predicted Score** calculated via Method C.
2.  **Calculate Correction Ratio:**
    *   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
        *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
    *   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
        *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.
3.  **Apply to Benchmark:**
    *   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
    *   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

> [!NOTE]
> **Why Simple Proximity vs Euclidean Distance?**
> Euclidean distance calculation would be particularly tricky here as it requires to have the same amount of dimensions, which is very often not the case as the core count varies significantly per architecture (e.g., Apple 6-core vs Android 8-core configurations).
> Since Geekbench Multi-Core is a total throughput metric and the Predicted Score itself models total throughput (Sum of all clusters), the scalar difference between Predicted Scores correctly identifies performance neighbors without the complexity of mapping mismatched cluster topologies.

#### Method C: Predicted Calculation (Tertiary)
Used as a standalone fallback if no neighbors exist, or as the **Predictor** for Method B.

> [!NOTE]
> **Understanding Core Clusters (The "Prime, Performance, Efficiency" Split)**
> Modern smartphone processors (like Snapdragon or Dimensity) do not use identical cores. Instead, they group different types of cores into **Clusters** to balance speed and battery life:
> *   **Prime Cores:** The most powerful cores (e.g., Cortex-X series). Usually appearing as a single core (1x) dedicated to extreme bursts of speed, like launching a heavy app.
> *   **Performance Cores (P-Cores):** High-speed "workhorse" cores (e.g., Cortex-A700 series). These handle the daily heavy lifting like web browsing, gaming, and multitasking.
> *   **Efficiency Cores (E-Cores):** Low-power cores (e.g., Cortex-A500 series). These stay active during background tasks (syncing, standby) to ensure the phone uses as little battery as possible when not in active heavy use.
>
> **Method C** calculates performance by scoring every identified cluster found in the device's SOC reference (§6.1.0) individually before summing them up. This structure works for all phones: a single-core phone has one cluster, while a modern flagship has three or more.

**Step 1: Frequency-Adjusted Core Score (FACS)**
Instead of calculating a raw score and then scaling it globally, we calculate the throughput for **each cluster** individually.

*   **Frequency Scaling Factor (FSF) Formula:** `Actual_Freq / Ref_Freq`
    *   *Significance:* Scales the base architecture score based on whether the specific cluster is overclocked or underclocked.
    *   **Reference:** See **Section 6.1.0** for Reference Frequencies.
*   **Frequency-Adjusted Core Score (FACS) Formula:** `Core_Architecture_Score * Core_Count * FSF`
    *   *Significance:* Represents the total throughput contribution of a specific core cluster, accounting for its architecture, count, and clock speed.
    *   **Core_Architecture_Score (CAS):** The baseline performance score for the specific core architecture as defined in the **Master Scoring Table (§6.1.0)**.
    *   **Core_Count:** The number of identical physical cores within the specific processing cluster (e.g., 1 prime, 5 performance).

**Step 2: Calculate Predicted Score**
1.  **Raw Performance Throughput Score (PTS):** Sum of `FACS` from all clusters in the SoC configuration.
2.  **Predicted Score:** `10 * (log(PTS) - log(CPU_PTS_Score_Min)) / (log(CPU_PTS_Score_Max) - log(CPU_PTS_Score_Min))`
*   **Max Score (10.0):** ≥ CPU_PTS_Score_Max
*   **Min Score (0.0):** ≤ CPU_PTS_Score_Min

> **Example: Snapdragon 8 Gen 3**
> *   **Ref Freqs:** X4=3.3GHz, A720=2.8GHz, A520=2.0GHz (from Section 6.1.0)
> *   **Actual Specs:** 1x X4 @ 3.3GHz, 5x A720 @ 3.2GHz, 2x A520 @ 2.3GHz
>
> 1.  **Prime Cluster (Cortex-X4):**
>     *   FSF: `3.3 / 3.3` = 1.0
>     *   FACS: `8 (CAS) * 1 (Count) * 1.0 (FSF)` = **8.0**
> 2.  **Performance Cluster (Cortex-A720):**
>     *   FSF: `3.2 / 2.8` = 1.14
>     *   FACS: `5 (CAS) * 5 (Count) * 1.14 (FSF)` = **28.5**
> 3.  **Efficiency Cluster (Cortex-A520):**
>     *   FSF: `2.3 / 2.0` = 1.15
>     *   FACS: `1 (CAS) * 2 (Count) * 1.15 (FSF)` = **2.3**
>
> *   **Raw Performance Throughput Score (PTS):** `8.0 + 28.5 + 2.3` = **38.8**
> *   **Predicted Score:** `10 * (log(38.8) - log(5)) / (log(80) - log(5))` ≈ **7.4/10**

### 🔹 6.2 CPU Architecture & Single-Core Efficiency
*Description:* Measures the responsiveness of the CPU for immediate tasks like app launching, web browsing, and UI navigation. This isolates architectural efficiency and single-thread speed.
*   **Measurement:** Geekbench 6 Single-Core Score.
*   **Unit:** Points (0–10)
*   **Significance:** Determines the "snappiness" of the UI and speed of light tasks.

> [!TIP]
> **Why do we need this separate from Section 3.1?**
> *   **Section 6.1 (Multi-Core) measures CAPACITY (The Truck):** Determines if the phone *can* run heavy tasks (rendering, gaming) without bottling up.
> *   **Section 6.2 (Single-Core) measures RESPONSIVENESS (The Sports Car):** Determines how *fast* a single task (like opening an app or scrolling a webpage) happens. 
> A phone with many weak cores (high 3.1) can still feel "laggy" in UI interactions if individual cores are slow (low 3.2). Single-core speed is the primary driver of perceived fluidity in daily use.

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
    *   `Distance = abs(Diff_Predicted)`
    *   *Where Diff_Predicted = Predicted_Target - Predicted_Neighbor*
    *   *Note:* Based on **Predicted Score** calculated via Method C.
2.  **Calculate Correction Ratio:**
    *   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
        *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
    *   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
        *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.
3.  **Apply to Benchmark:**
    *   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
    *   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

> [!NOTE]
> **Why Simple Proximity vs Euclidean Distance?**
> Single-core performance is inherently 1-dimensional, dominated by the Prime Core's architecture and frequency. There are no sub-dimensions to trade off (unlike Display or Battery). Therefore, the scalar difference in Predicted Score is the mathematically correct proxy for neighbor selection.

#### Method C: Predicted Calculation (Tertiary)
Used as a standalone fallback or as the **Predictor** for Method B.

**Step 1: Core Architecture Score (CAS)**
*   *What is it?* The score of the *single strongest core* in the system.
*   **Scores:** See **Section 6.1.0 CPU Core Architecture Reference** for authoritative core scores.

**Step 2: Frequency Scaling Factor (FSF)**
*   *What is it?* A multiplier for clock speed variations.
*   **Formula:** `Actual_Frequency_GHz / Reference_Frequency_GHz`
    *   *Range:* Typically 0.8 - 1.3 (underclocked vs overclocked).
    *   **Why FSF?** Single-core performance scales almost linearly with frequency for the same architecture. FSF normalizes this relative to the reference design.
    *   **Reference:** See **Section 6.1.0** for Reference Frequencies.

**Step 3: Calculate Predicted Score**
1.  **Raw Single-Thread (STRS - Single Thread Raw Score):** `CAS * FSF`
2.  **Predicted Score:** `10 * (log(STRS) - log(CPU_STRS_Score_Min)) / (log(CPU_STRS_Score_Max) - log(CPU_STRS_Score_Min))`
*   **Max Score (10.0):** ≥ CPU_STRS_Score_Max
*   **Min Score (0.0):** ≤ CPU_STRS_Score_Min

> **Example: Snapdragon 8 Gen 3 for Galaxy (Overclocked)**
> *   **Specs:** Prime Core is Cortex-X4 at **3.4GHz**. Reference Frequency for X4 is **3.30GHz**.
> *   **CAS:** Cortex-X4 = **8**
> *   **FSF:** `3.4 / 3.3` ≈ **1.03**
> *   **Raw Single-Thread (STRS):** `8 * 1.03` = **8.24**
> *   **Predicted Score:** `10 * (log(8.24) - log(0.4)) / (log(10) - log(0.4))` ≈ **9.4/10**

#### 6.3.0 GPU Architecture Reference

**Master Scoring Table** (used across all GPU-related calculations)

This table provides the authoritative GPU architecture scores used throughout the scoring system, including:
- Section 6.3 GPU Performance (Base Architecture Score)
- Section 8.1 for Battery Endurance Scoring (Battery efficiency - SoC component)

**Scoring Basis:** Based on GPU generation, compute units, and real-world graphics performance.

> [!NOTE]
> **Understanding the GPU Performance Table**
> 
> This table scores GPUs across three dimensions:
> 
> **1. Standard Graphics (0-10):** Traditional 3D gaming performance
> *   **Used in:** Section 6.3 (GPU Performance scoring)
> *   Measures polygon rendering, texture processing, and shader execution
> *   The foundation of all mobile games (Genshin Impact, PUBG, etc.)
> *   Higher scores = smoother gameplay at higher settings
> 
> **2. Ray Tracing (0-10):** Advanced realistic lighting, shadows, and reflections
> *   **Used in:** Section 6.3 (GPU Performance scoring)
> *   Ray tracing simulates how light bounces in the real world, creating photorealistic reflections (mirrors, water), accurate shadows, and global illumination
> *   **Score 0:** No hardware support - GPU cannot accelerate ray tracing at all
> *   **Score 1-5:** Basic hardware support - can run simple Ray Tracing (RT) effects but with significant performance cost
> *   **Score 6-8:** Capable hardware - handles RT effects in modern games (e.g., Resident Evil Village Mobile) with acceptable framerates
> *   **Score 9-10:** Flagship-tier - delivers smooth RT performance even in demanding scenarios
> *   *Why the variation?* Ray tracing requires dedicated hardware units (RT cores). More cores + newer architecture = higher score. For example, Adreno 750 has more RT cores than Adreno 740, hence 10 vs 8.
> 
> **3. Efficiency (0-10):** Performance-per-watt (battery impact)
> *   **Used in:** Section 8.1 (Battery Endurance calculations)
> *   Measures how much performance you get per unit of power consumed
> *   *Why separate from performance?* Some GPUs (e.g., Snapdragon 888's Adreno 660) have high Standard Graphics scores but terrible efficiency (overheats, drains battery). Others (e.g., Snapdragon 778G's Adreno 642L) have moderate performance but excellent efficiency.
> *   **Process node benefits** (3nm vs 5nm) are scored separately in Section 6.10. This Efficiency score focuses on architectural design and thermal management.
> 
| GPU Model                 | Standard Graphics | Ray Tracing | Ref Freq (MHz) | Efficiency | Notes                                   |
| :------------------------ | :---------------: | :---------: | :------------: | :--------: | :-------------------------------------- |
| **Adreno 830**            |      **10.0**     |    **10.0** |    **1100**    |   **10.0** | Snapdragon 8 Elite                      |
| **Immortalis-G925 MC12**  |      **10.0**     |    **10.0** |    **1626**    |   **10.0** | Dimensity 9400                          |
| **Adreno 750**            |      **10.0**     |    **10.0** |    **903**     |    **9.0** | Snapdragon 8 Gen 3                      |
| [...]                     | [...]             | [...]       | [...]          | [...]      | [...]                                   |

> [!IMPORTANT]
> **Source of Truth:** For the full list of all 40+ supported GPU architectures and their authoritative scores, refer to the **GPU ARCHITECTURE SCORING TABLE** in [proposed_data_structure.md].

> [!NOTE]
> **Understanding Mali/Immortalis "MC" Notation:** ARM Mali and Immortalis GPUs use Multi-Core (MC) configurations. The number after "MC" indicates the shader core count. For example:
> - **Immortalis-G715 MC11** = 11 shader cores (flagship config)
> - **Mali-G715 MC9** = 9 shader cores (high-end config)
> - **Mali-G715 MC7** = 7 shader cores (mid-range config)
> More cores = higher performance. Always match the exact MC count from device specifications (found on GSMArena under "Chipset" details).


### 🔹 6.3 GPU Performance (Graphics & Gaming)
*Description:* Measures the graphical processing power for gaming, rendering, and compute tasks. This score reflects the device's ability to drive high-fidelity visuals at high frame rates.
*   **Measurement:** Composite of Standard Graphics (90%) and Ray Tracing (10%).
*   **Unit:** Points (0-10)
*   **Significance:** Critical for AAA gaming, ray tracing, and UI smoothness on high-refresh-rate displays.

#### Part 1: Standard Graphics Score (SGS)
*Focus:* Traditional rasterization performance (Geometry, Textures, Shaders) and API efficiency.
*   **Primary Source:** 3DMark Steel Nomad Light.

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
> **Why Logarithmic?** Graphics performance scales exponentially in user experience. The difference between 500 points (entry-level, struggles with basic games) and 900 points (smooth gameplay in most titles) is transformative. However, the difference between 1400 points (flagship) and 1800 points (top-tier flagship) shows diminishing returns - both deliver excellent performance, and the improvement is barely noticeable in real-world use.

**Scoring Logic:**
*   **Data Available:** `SGS = SGS_Bench`
*   **No Data Available:** Proceed to Method B.

#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.

1.  **Identify Neighbors:** Find **3 distinct Reference Phones** that have benchmark scores (from 3DMark) and known specs. Select the ones with the smallest **Distance** to the target device, **excluding the target device** itself:
    *   `Distance = abs(Diff_Predicted_SGS)`
    *   *Where Diff_Predicted_SGS = Predicted_SGS_Target - Predicted_SGS_Neighbor*
    *   *Note:* Based on **Predicted SGS** calculated via Method C.
2.  **Calculate Correction Ratio:**
    *   `Avg_Predicted_SGS_Neighbors = (Predicted_SGS_Neighbor1 + Predicted_SGS_Neighbor2 + Predicted_SGS_Neighbor3) / 3`
        *   *Note:* `Predicted_SGS_Neighbor1/2/3` refers to the **Predicted SGS** (Method C) of each neighbor device.
    *   `Correction_Ratio = Predicted_SGS_Target / Avg_Predicted_SGS_Neighbors`
        *   *Note:* `Predicted_SGS_Target` is the **Predicted SGS** (Method C) of the target device.
3.  **Apply to Benchmark:**
    *   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
    *   `SGS = Correction_Ratio * Avg_Benchmark_Neighbors`

> [!NOTE]
> **Why Simple Proximity vs Euclidean Distance?**
> Unlike Display or Battery where multiple independent factors (Brightness, Color, Refresh Rate) contribute equally to the score, GPU performance is dominated by a single factor: **Base Architecture Score (GAS)** (75% weight). Devices with similar Predicted SGS scores almost certainly share the same or immediate-neighbor GPU architecture. Therefore, selecting neighbors based on **Closest Predicted Score** is computationally efficient and effectively groups devices by hardware generation without needing complex multi-dimensional distance calculations.

#### Method C: Predicted Standard Graphics (Tertiary)
Used as a standalone fallback or as the **Predictor** for Method B.

**Step 1: Get Base Scores (GAS)**
*   **What is it?** The base capability of the GPU architecture.
*   **Lookup:** Find the exact GPU Model in **Section 6.3.0 table** above. Use the **Standard Graphics** value.
*   **Source:** GSMArena lists full GPU name under "Chipset" section.

**Step 2: Frequency Scaling Factor (FSF)**
*   **What is it?** A multiplier for clock speed variations.
*   **Formula:** `Actual_Frequency_MHz / Reference_Frequency_MHz`
    *   *Significance:* Scales the base architecture score (GAS) based on whether the GPU is overclocked or underclocked relative to the reference design.
    *   **Reference:** See **Section 6.3.0** for Reference Frequencies.
    *   *Example:* Adreno 750 @ 903 MHz (reference) → `903 / 903 = 1.0`
    *   *Example:* Adreno 750 @ 1000 MHz (overclocked) → `1000 / 903 = 1.11`

**Step 3: API & Feature Support Modifier (AFM - SGS Component)**
*   **What is it?** A modifier focusing **exclusively on API Efficiency for Rasterization**.
*   **Formula:** `0.75 + (0.25 * API_Score / 10)`
    *   *Max Value:* 1.0 (Vulkan 1.3)
    *   *Min Value:* 0.75 (Legacy OpenGL only)
    *   *Why this formula?* Ranges from 0.75 (25% penalty relative to baseline) to 1.0 (0% penalty). The +0.75 ensures the API modifier doesn't overly crush the score of older capable hardware, while still rewarding modern efficiency.

**API Support Score Table (Detailed)**
*   **Measurement:** Highest supported Vulkan / OpenGL ES Version.
*   **Unit:** Score (0-10)
*   **Significance:** Modern APIs like Vulkan 1.3 allow developers to squeeze significantly more performance from the same hardware through advanced features like dynamic rendering and compute shader capabilities.

**API Support Score Table (Detailed)**
*   **Measurement:** Highest supported Vulkan / Metal / OpenGL ES / DirectX Version.
*   **Unit:** Score (0-10)
*   **Significance:** Modern APIs allow developers to squeeze significantly more performance through advanced features like dynamic rendering and compute shaders.

| Vulkan (Android)  | Metal (iOS)    | OpenGL ES (Leg)    | DirectX (Win Mob)       | Score     |
| :---------------- | :------------- | :----------------- | :---------------------- | :-------: |
| **Vulkan 1.4**    | **Metal 4.0**  | —                  | **D3D 12 (FL 12_2)**    | **10.0**  |
| **Vulkan 1.3**    | **Metal 3.0**  | —                  | **D3D 12 (FL 12_0)**    | **9.2**   |
| [...]             | [...]          | [...]              | [...]                   | [...]     |

> [!IMPORTANT]
> **Source of Truth:** For the full list of all supported Graphics APIs and their authoritative scores, refer to the **GPU API Support Scoring Table** in [proposed_data_structure.md].

**AMBIGUOUS API RESOLUTION (MANDATORY FALLBACK CENSUS)**
If the explicit API version is NOT disclosed on the primary spec sheet, use the following fallback matrices based on the device's OS generation and chipset era.

**MATRIX 1: APPLE / iOS (Extract)**
| Apple SoC Generation | Min iOS Version | Inferred API Version |
| :------------------- | :-------------- | :------------------- |
| **A18, M4, M5**      | iOS 18+         | Metal 4.0            | 
| **A17 Pro**          | iOS 17.5+       | Metal 3.3            |
| [...]                | [...]           | [...]                |

> [!IMPORTANT]
> **Source of Truth:** For the full OS/Architecture fallback matrices (Matrix 1, 2, and 3), refer to the **Ambiguous API Resolution** section in [proposed_data_structure.md].

**MATRIX 2: ANDROID (Extract)**
| Android Launch OS    | GPU Architecture Baseline      | Inferred API  |
| :------------------- | :----------------------------- | :------------ |
| **Android 15+**      | Adreno 8xx+, Immortalis G92x+  | Vulkan 1.4    |
| **Android 13 - 14**  | Adreno 7xx, Mali-G71x          | Vulkan 1.3    |
| [...]                | [...]                          | [...]         |

**MATRIX 3: WINDOWS MOBILE (Extract)**
| Windows OS Version   | Era / Reference Hardware      | Inferred API  |
| :------------------- | :---------------------------- | :------------ |
| **Windows 11 (24H2)**| Snapdragon X Elite (Adreno X1)| D3D 12 (12_2) |
| **Windows Phone 8.0**| Lumia 920 / 1020 (Baseline)   | D3D 9.3       |
| [...]                | [...]                         | [...]         |

> [!IMPORTANT]
> **Multi-API Support & Scoring Logic:**
>
> Mobile devices support **BOTH Vulkan and OpenGL ES simultaneously**. Android supports all versions of both APIs, with approximately 85% of active devices supporting Vulkan.
>
> **ANGLE Translation Layer:** Some modern devices (e.g., certain Exynos chipsets) run OpenGL ES on top of Vulkan using the ANGLE translation layer. This **does not** make OpenGL ES better - ANGLE adds translation overhead, making it slower than native Vulkan. It simply means the device doesn't need separate OpenGL ES drivers.
>
> **Scoring Rule:** When a device supports multiple graphics APIs, **use the highest-scoring API** for the predicted score.
>
> *Example:*
> *   Device supports: Vulkan 1.3 (score 10.0) + OpenGL ES 3.2 (score 5.0)
> *   API Score: 10.0 (Vulkan takes priority as the better API)
> *   *Rationale:* Developers will always use the most advanced API available to maximize graphics quality and efficiency. A device with Vulkan 1.3 will run games using Vulkan, not OpenGL ES, regardless of whether OpenGL ES is available.

**Step 4: Calculate Predicted SGS**
1.  **Raw Capability Score (RC):** `GAS * FSF * API_Modifier`
2.  **Predicted SGS:** `10 * (log(RC) - log(GPU_RC_Score_Min)) / (log(GPU_RC_Score_Max) - log(GPU_RC_Score_Min))`
    *   **Max Score (10.0):** ≥ GPU_RC_Score_Max
    *   **Min Score (0.0):** ≤ GPU_RC_Score_Min

#### Part 2: Ray Tracing Score (RTS)
*Focus:* Advanced lighting physics (Reflection, Refraction, Shadows).
*   **Measurement:** Direct Hardware Capability.
*   **Logic:** Retrieve **Ray Tracing** (0-10) score directly from **Section 6.3.0 Table** above.
*   **Why no benchmark?** Ray Tracing is a specific hardware feature. Using the architectural capability score is the most accurate predictor of support and performance tier for this specific feature subset.

#### Final Section 6.3 Score Calculation
Weighted combination of Standard Graphics (Raster) and Ray Tracing.

**Formula:** `Predicted_Score = (SGS * 0.9) + (RTS * 0.1)`

> [!NOTE]
> **Why 10% for Ray Tracing?** Ray Tracing (RT) is a technique where the phone's graphics chip simulates how light bounces off real surfaces — creating realistic reflections in mirrors and water, and accurate shadows. While only ~5–10% of current mobile games use it, this **10% weight is intentionally forward-looking**: manufacturers are investing heavily in RT hardware, just as they invested in 5G before streaming services caught up. Phones built today will use RT heavily within 2–3 years. The 90% on classic rendering keeps scores grounded in today's reality.

> [!TIP]
> **Example 1: Top-Tier Flagship (Snapdragon 8 Gen 3 / Adreno 750)**
> *   **Step 1: Determine Standard Graphics Score (SGS)**
>     *   **Method A (Benchmark):** Available. Score = 1800+ → **SGS = 10.0**
>     *   *(For reference only: Method C Predictor would give ~9.3)*
> *   **Step 2: Determine Ray Tracing Score (RTS)**
>     *   **Table Lookup:** Adreno 750 → **RTS = 10.0**
> *   **Step 3: Calculate Final Score**
>     *   `Final = (SGS * 0.9) + (RTS * 0.1)`
>     *   `Final = (10.0 * 0.9) + (10.0 * 0.1) = 9.0 + 1.0 = 10.0`
>
> **Example 2: Mid-Range Device (Snapdragon 778G / Adreno 642L)**
> *   **Step 1: Determine Standard Graphics Score (SGS)**
>     *   **Method A (Benchmark):** Not Available in Database.
>     *   **Method B (Neighbors):** Found 3 similar devices (Galaxy A52s, Xiaomi 11 Lite, Moto Edge 20).
>         *   Avg Neighbor Benchmark: 750 points (Steel Nomad Light).
>         *   Correction Ratio: ~1.02 (Target has slightly higher clock).
>         *   Estimated Benchmark: `750 * 1.02 = 765`.
>         *   **SGS:** `10 * (log(765) - log(500)) / (log(1800) - log(500)) = 3.3`
> *   **Step 2: Determine Ray Tracing Score (RTS)**
>     *   **Table Lookup:** Adreno 642L → **RTS = 0.0**
> *   **Step 3: Calculate Final Score**
>     *   `Final = (3.3 * 0.9) + (0.0 * 0.1) = 2.97`


### 🔹 6.4 AI Hardware Performance (Neural Processor)
*Description:* Measures the raw hardware acceleration for AI/ML tasks. The Neural Processing Unit (NPU) or AI Processing Unit (APU) is a dedicated chip that handles AI workloads. This score reflects the device's ability to run on-device generative AI, real-time translation, and advanced image processing *quickly*.
*   **Measurement:** Geekbench AI (Quantized INT8 Score).
*   **Unit:** Points
*   **Significance:** Critical for future-proofing and enabling smooth operation of modern "AI Phone" features.

> [!IMPORTANT]
> **Hardware vs. Software:** This section measures **Hardware Capability** (The Engine). It is distinct from **Section 5.3 (AI Feature Suite)** which measures the *features* the software actually provides (The Destination). A powerful Neural Processing Unit (NPU) (high 6.4 score) is required to run advanced features smoothly, but doesn't guarantee they are installed.

**SoC Neural Processing Unit (NPU) / AI Accelerator Reference Table**

This table provides the authoritative AI scores for major SoCs, reflecting their Neural Processing Unit (NPU) hardware acceleration capabilities (INT8/FP16) for machine learning.

| SoC Model                             | NPU / Neural Engine            | AI Score (0-10) |
| :------------------------------------ | :----------------------------- | :-------------- |
| **Snapdragon 8 Elite Gen 5**          | Hexagon (2026 Model)           | **10.0**        |
| **Snapdragon 8 Elite**                | Hexagon (Oryon v1)             | **9.5**         |
| [...]                                 | [...]                          | [...]           |

> [!IMPORTANT]
> **Source of Truth:** For the full list of all supported SoC AI accelerators and their authoritative scores, refer to the **SOC_NEURAL_PROCESSING_UNIT_(NPU)_/_AI_ACCELERATOR_LOOKUP_TABLE** in [proposed_data_structure.md].

> [!IMPORTANT]
> **SoC not listed in the table?** Do **not** guess a score. Add a new row to this table first:
> 1. Find the SoC's Geekbench AI (Quantized INT8) score on the [Geekbench AI Leaderboard](https://browser.geekbench.com/ai-benchmarks).
> 2. Normalise it against the Min/Max constants (Method A formula below) to get an authoritative score.
> 3. Insert the new row in descending score order, then use it for scoring.

#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct Geekbench AI score is available. It provides the most accurate representation of real-world AI/NPU performance.
*   **Source:** [Geekbench AI Leaderboard](https://browser.geekbench.com/ai-benchmarks)
*   **Metric:** Quantized Score (INT8)
    *   *Why Quantized?* Mobile NPUs are optimized for integer math (INT8) for efficiency. Evaluating FLOAT32 often falls back to the CPU/GPU, missing the NPU's true potential.
*   **Normalization:**
    *   **Formula:** `Score = 10 * (log(Geekbench_AI_Score) - log(AI_GB_Quant_Score_Min)) / (log(AI_GB_Quant_Score_Max) - log(AI_GB_Quant_Score_Min))` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ AI_GB_Quant_Score_Max
    *   **Min Score (0.0):** ≤ AI_GB_Quant_Score_Min

> [!NOTE]
> **Why Logarithmic?** AI performance utility follows a curve of diminishing returns relative to real-world experience. A **+5,000 point** jump from a legacy 1,000-point NPU to 6,000 points is transformative, enabling the shift from basic cloud-assisted tasks to capable local voice processing and real-time photo object removal. In contrast, an identical **+5,000 point** jump from 75,000 to 80,000 points represents a marginal improvement in the inference speed of extremely large local LLMs that is imperceptible for 99% of daily smartphone AI features. Logarithmic scaling correctly assigns more value to these early, usability-defining gains.

#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.

**1. Identify Neighbors via Feature Distance (Minimum Variance)**
Instead of just matching the overall predicted score, we find the 3 devices that are statistically closest across **all** AI-relevant hardware components.
*   **Search Space:** All phones with known Geekbench AI scores (Method A), **excluding the target device** itself.
*   **Distance Metric:** Weighted Euclidean Distance.
    *   `Distance = Sqrt( 0.40*(AI_Diff)^2 + 0.25*(RAM_Tech_Diff)^2 + 0.15*(GPU_Diff)^2 + 0.10*(RAM_Cap_Diff)^2 + 0.10*(Process_Diff)^2 )`
    *   *Where "Diff" is the difference between Target and Neighbor scores for each component:*
        *   `AI` (table above, Sec 6.4), `RAM_Tech` (Sec 6.5), `GPU` (Sec 6.3), `RAM_Cap` (Sec 6.6), `Process` (Sec 6.10 Part C).
    *   **Scientific Rationale:** We weight the distance calculation to ensure that neighbors are selected based on the most critical performance factors (NPU, Bandwidth) rather than less impactful specs. 
    *   **Important:** Calculation uses **Predicted Scores** (Specs only) for all components to ensure neutrality, not Final Scores (Specs + Boosters). This ensures we compare devices based on intrinsic hardware similarity.
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
*   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

#### Method C: Predicted Calculation (Tertiary)
Used as a standalone fallback if no neighbors exist, or as the **Predictor** for Method B.

**Step 1: Gather Components**
The predicted score is a weighted sum of 5 hardware factors, based on research into mobile AI bottlenecks (Geekbench AI, MLPerf).

1.  **SoC AI Score (40%) – The Engine**
    *   **Source:** Retrieve `AI Score` from **the Section 6.4 table**.
    *   **Rationale:** The Neural Processing Unit (NPU) is the specialized processor designed to do the heavy lifting for AI. Just as a powerful engine drives a car, the NPU is built to run AI math (quantized INT8) efficiently. It is the single most important factor for raw performance.

2.  **RAM Technology Score (25%) – The Highway**
    *   **Source:** Retrieve Score from **Section 6.5**.
    *   **Rationale:** An engine is useless without fuel. AI models require massive amounts of data to be fed to the NPU instantly. If the "highway" (Memory Bandwidth) is too narrow, the NPU sits idle waiting for data. Faster RAM (e.g., LPDDR5X) directly translates to faster AI response times.

3.  **GPU Performance Score (15%) – The Backup Engine**
    *   **Source:** Retrieve Score from **Section 6.3**.
    *   **Rationale:** While the NPU handles most tasks, some complex AI instructions (floating point math) are too specific for it. In these cases, the system falls back to the Graphics Unit (GPU). A strong GPU ensures the phone doesn't choke on these complex tasks.

4.  **RAM Capacity Score (10%) – The Warehouse**
    *   **Source:** Retrieve Score from **Section 6.6**.
    *   **Rationale:** This measures *how big* of a model you can run. 8GB is the bare minimum for modern "On-Device AI". If the warehouse is too small, the phone has to constantly swap data in and out, drastically slowing down performance. *Note: having excess RAM (e.g., 24GB) doesn't make a small task faster, which is why this weight is limited to 10%.*

5.  **Process Node Score (10%) – Efficiency**
    *   **Source:** Retrieve Score from **Section 6.10 Part C**.
    *   **Rationale:** AI calculations generate significant heat. A more efficient chip (e.g., 3nm vs 5nm) determines whether the device can run at top speed for sustained periods or if it will slow down (throttle) to cool off.

**Step 2: Calculate Predicted Score**
`Predicted_Score = (0.40 * AI) + (0.25 * RAM_Tech) + (0.15 * GPU) + (0.10 * RAM_Cap) + (0.10 * Process_Node)`


### 🔹 6.5 RAM Technology - Memory Technology Efficiency Index (MTEI)
*Description:* The type of memory used. Newer technology (LPDDR5X) allows for faster app switching and saves battery compared to older types.
*   **Measurement:** JEDEC standard specification.
*   **Unit:** Memory Generation
*   **Significance:** Affects data transfer speeds and power consumption.

| Score    | Technology    | Representative Examples        |
| :------- | :------------ | :----------------------------- |
| **10.0** | **LPDDR5X**   | S24 Ultra, OnePlus 12          |
| **9.0**  | **LPDDR5**    | S22 Ultra, Pixel 7 Pro         |
| **7.0**  | **LPDDR4X**   | Galaxy A54, Nothing Phone (2a) |
| **5.0**  | **LPDDR4**    | Older Mid-range                |
| **3.0**  | **LPDDR3**    | Legacy Budget                  |
| **1.0**  | **LPDDR2**    | Obsolete                       |
| **0.0**  | **DDR2/DDR3** | Ancient                        |

### 🔹 6.6 RAM Capacity - Memory Capacity Index (MCI)
*Description:* Measures the amount of physical memory available for applications and background processes. More RAM improves multitasking, reduces app reloads, and increases system stability under load.
*   **Measurement:** Total physical RAM.
*   **Unit:** Gigabytes (GB)
*   **Significance:** Determines multitasking capability and app retention.
*Formula:* `Score = 10 * (log(GB) - log(RAM_GB_Min)) / (log(RAM_GB_Max) - log(RAM_GB_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ RAM_GB_Max
*   **Min Score (0.0):** ≤ RAM_GB_Min
> [!NOTE]
> **Why Logarithmic?** The utility of RAM diminishes as it increases. Going from 4GB to 8GB (+4GB) dramatically improves multitasking and system stability. However, an identical +4GB upgrade from 20GB to 24GB offers almost zero tangible benefit for current mobile applications.

### 🔹 6.7 Storage Technology
*Description:* The speed of the internal drive. Faster storage means the phone boots up instantly, apps install quickly, and files copy fast.
*   **Measurement:** Sequential Read/Write speed capacity.
*   **Unit:** Storage Generation, internal storage only.
*   **Significance:** Affects boot time, app load time, and file transfer speed.

| Score    | Technology   | Representative Examples    |
| :------- | :----------- | :------------------------- |
| **10.0** | **UFS 4.0**  | S24 Ultra, Xiaomi 14       |
| **8.0**  | **UFS 3.1**  | Pixel 7, S21 Ultra         |
| **7.0**  | **UFS 3.0**  | OnePlus 8 Pro              |
| **6.0**  | **UFS 2.2**  | Redmi Note 13, Galaxy A34  |
| **5.0**  | **UFS 2.1**  | Older Mid-range            |
| **3.0**  | **eMMC 5.1** | Galaxy A05, Budget Tablets |
| **1.0**  | **eMMC 4.5** | Very old                   |
| **0.0**  | **eMMC≤4.0** | Obsolete                   |

### 🔹 6.8 Storage Capacity
*Description:* Internal space for your data. More storage means you can save more photos, videos, and games without deleting old ones.
*   **Measurement:** Total internal non-volatile memory.
*   **Unit:** Gigabytes (GB)
*   **Significance:** Determines capacity for apps, media, and files.
*Formula:* `Score = 10 * (log(GB) - log(Storage_GB_Min)) / (log(Storage_GB_Max) - log(Storage_GB_Min))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Storage_GB_Max
*   **Min Score (0.0):** ≤ Storage_GB_Min
> [!NOTE]
> **Why Logarithmic?** Similar to RAM, storage utility is non-linear. The +64GB upgrade from 64GB to 128GB is a critical jump that prevents "storage full" anxiety. However, an identical +64GB addition from 512GB to 576GB provides almost zero perceptible change to a user's daily experience.

### 🔹 6.9 Storage Expandability
*Description:* Ability to add a memory card. A dedicated slot lets you cheaply add massive storage for photos and media.
*   **Measurement:** Physical expansion slot.
*   **Unit:** Slot Type
*   **Significance:** Cost-effective storage expansion option.

| Score    | Feature                     | Example Models                |
| :------- | :-------------------------- | :---------------------------- |
| **10.0** | **Dedicated MicroSD Slot**  | Galaxy A15, Poco M6 Pro       |
| **8.0**  | **Hybrid SIM/MicroSD Slot** | Galaxy A54, Redmi Note 13     |
| **5.0**  | **Proprietary Expansion**   | Huawei (NM Card)              |
| **0.0**  | **No Expansion Slot**       | S24 Ultra, iPhone 15, Pixel 8 |


### 🔹 6.10 Thermal Dissipation & Stability Index (TDSI)
*Description:* A composite index measuring the device's ability to sustain performance and shed heat. It combines the physical thermal capacity of the chassis, the internal cooling solution, and the thermal efficiency of the processor node.
*   **Measurement:** Frame Material + Weight + Dimensions + Cooling System Type + Process Node.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Prevents throttling, ensures sustained gaming performance, and maintains device longevity.

> [!IMPORTANT]
> **Why is TDSI not double-scoring physical materials or process nodes?**
> Standard benchmarks (like Geekbench 3.1) measure instantaneous, burst performance. They do not penalize a device that melts your hand or heavily throttles after 5 minutes of intensive load. The TDSI uniquely scores the hardware's physical capacity to sustain that peak load over time. A phone can score 10/10 in burst speed, but if it has a plastic frame and no cooling, it will throttle to 5/10. TDSI corrects this blind spot in standard benchmarking.

**Part A: Chassis Thermal Capacity (50%)**
*   *What is it?* How much heat the phone body can absorb and spread passively.
*   **Measurement:** Frame material, device weight, and physical dimensions.

**A1 — Frame Thermal Conductivity Class (40% of Part A)**
*   **Measurement:** Frame material from manufacturer specifications.
*   **Unit:** Material Class (Discrete)
*   **Significance:** Primary heat path from SoC to edges.

| Score    | Frame Material                 | Thermal Conductivity Basis    |
| :------- | :----------------------------- | :---------------------------- |
| **10.0** | **Titanium / Stainless Steel** | High conductivity metals      |
| **8.0**  | **Aluminum / Magnesium Alloy** | Very high conductivity        |
| **4.0**  | **Plastic Composite**          | Low conductivity              |
| **0.0**  | **Polymer / Rubberized**       | Very low conductivity         |

> [!NOTE]
> **Why frame only?** Frame material is always published in specs, forms the primary heat path from SoC to edges, and is more consistent than back panel materials.

**A2 — Device Thermal Mass (25% of Part A)**
*   **Measurement:** Device weight.
*   **Unit:** Grams (g)
*   **Significance:** Heavier phones have more thermal mass to absorb heat spikes.

*Formula:* `Score = 10 * (Weight_g - Thermal_Weight_g_Min) / (Thermal_Weight_g_Max - Thermal_Weight_g_Min)` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Thermal_Weight_g_Max
*   **Min Score (0.0):** ≤ Thermal_Weight_g_Min

**A3 — Heat Dissipation Surface Area (20% of Part A)**
*   **Measurement:** Physical dimensions from spec sheet.
*   **Unit:** mm²
*   **Significance:** Bigger phones dissipate heat better through larger surface area.

*Formula:* `Surface = Height_mm * Width_mm`  
*Formula:* `Score = 10 * (Surface - Thermal_Surface_Area_mm2_Min) / (Thermal_Surface_Area_mm2_Max - Thermal_Surface_Area_mm2_Min)` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Thermal_Surface_Area_mm2_Max
*   **Min Score (0.0):** ≤ Thermal_Surface_Area_mm2_Min

**A4 — Device Thickness (15% of Part A)**
*   **Measurement:** Device thickness from manufacturer specifications.
*   **Unit:** Millimeters (mm)
*   **Significance:** Thicker phones have more internal volume for heat dissipation and airflow, allowing for better passive cooling and thermal capacity.

*Formula:* `Score = 10 * (Thickness_mm - Thermal_Thickness_mm_Min) / (Thermal_Thickness_mm_Max - Thermal_Thickness_mm_Min)` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Thermal_Thickness_mm_Max
*   **Min Score (0.0):** ≤ Thermal_Thickness_mm_Min

> [!NOTE]
> **Data Structure Mapping:** `1_4_thickness.thickness_mm`

**Part A Score:**  
`Part_A = (0.40 * A1) + (0.25 * A2) + (0.20 * A3) + (0.15 * A4)`

**Part B: Internal Cooling System Class (50%)**
*   *What is it?* The engineering sophistication of the internal heat management.
*   **Measurement:** Manufacturer thermal system disclosure.
*   **Unit:** System Class (Discrete)
*   **Significance:** Advanced cooling systems enable sustained peak performance by actively removing heat from critical components.

| Score    | Cooling System                      | 
| :------- | :---------------------------------- |
| **10.0** | **Active Cooling (Fan)**            |
| **8.0**  | **Large Vapor Chamber (≥4000 mm²)** |
| **7.0**  | **Vapor Chamber (Standard)**        |
| **5.0**  | **Multi-layer Graphite/Copper**     |
| **3.0**  | **Single Heat Spreader**            |
| **0.0**  | **No Thermal System Disclosed**     |

**Part C: Process Node Efficiency Reference**
*   *What is it?* Chip manufacturing technology. Smaller numbers (e.g., 3nm) mean the chip is more advanced, wasting less energy as heat.
*   **Measurement:** Semiconductor process node size + Foundry.
*   **Unit:** Nanometers (nm)
*   **Significance:** Determines the baseline thermal inefficiency of the chip that the cooling system must overcome.

**Formula:**
1.  **Node Score:** `10 * (log(SoC_Process_Node_nm_Max) - log(Node)) / (log(SoC_Process_Node_nm_Max) - log(SoC_Process_Node_nm_Min))`
2.  **Foundry Score:** See Foundry Efficiency table below.
3.  **Process Node Score:** `(0.9 * Node_Score) + (0.1 * Foundry_Score)` (Clamped 0-10)

*   **Max Score (10.0):** ≤ SoC_Process_Node_nm_Min + TSMC Foundry
*   **Min Score (0.0):** ≥ SoC_Process_Node_nm_Max + SMIC/Other Foundry

> **Why Logarithmic?** Transistor density and power efficiency scale non-linearly. A shrink from a mid-range node to a cutting-edge node is a massive leap, while equivalent absolute reductions at larger nodes yield diminishing returns.

**Foundry Efficiency Score:**
| Foundry           | Foundry Score | Why?                                                                        |
| :---------------- | :-----------: | :-------------------------------------------------------------------------- |
| **TSMC**          | **10**        | 20-30% better power efficiency at same node label (empirically proven).     |
| **Samsung**       | **5**         | Standard efficiency baseline.                                               |
| **SMIC / Others** | **0**         | Generally lower yield/efficiency than leaders.                              |

> [!NOTE]
>
> **Global Reference:** This calculated Process Node Score is the authoritative value used by both the **Battery Endurance Model (Section 8.1)** and the **AI Hardware Performance Model (Section 6.4)**.

**Final Formula: Peak Thermal Demand Compensation**
*   *What is it?* A fairness adjustment based on the **Peak Thermal Demand** generated by the processing engine, rewarding devices that are inherently easier to cool.
*   **Significance (The Peak vs. Baseline Demand Paradox):** Peak performance draws extreme wattage, generating massive heat. A flagship chip doing maximum computing (Section 6.1 Peak Score = 10) draws 15+ watts, requiring heavy cooling. A budget chip (Peak Score = 2) might only physically draw 4 watts. However, a flagship chip built on an efficient 3nm node generates *less* waste heat per watt than an inefficient 5nm node.
*   **Calculate Thermal Mitigation:**
    *   We combine two sources of thermal relief: having a less powerful chip (which restricts maximum power draw) and having a highly efficient manufacturing node (which wastes far less drawn power as heat).
    *   `Peak_Thermal_Demand = Section_6_1_Score`
    *   `Node_Efficiency_Relief = Process_Node_Score`
    *   `Thermal_Mitigation = (10 - Peak_Thermal_Demand) + Node_Efficiency_Relief`
*   **Calculate Load Compensation Bonus:**
    *   `Load_Bonus = Thermal_Mitigation / 5`
    *   **Max Bonus (+4.0):** Low-power peak demand, highly efficient node -> Needs minimal cooling to remain stable.
    *   **Min Bonus (+0.0):** Extreme peak power demand, highly inefficient node -> Requires massive cooling to survive.

1.  **Calculate Baseline Physical Capability:** `Physical_Score = (0.5 * Part_A) + (0.5 * Part_B)`
2.  **Calculate TDSI Score:** `TDSI = (0.8 * Physical_Score) + Load_Bonus` (Clamped 0-10)

> [!NOTE]
> **Why these weights?** By multiplying the `Physical_Score` by 0.8 (max 8.0 points) and adding a `Load_Bonus` (max 4.0 points, but typically 2.0 for flagships), an ultra-gaming flagship with perfect physical cooling (8.0) and top-tier chip efficiency (2.0) will score a perfect 10.0 without exceeding the clamp limit. This ensures that no premium thermal hardware is "wasted" mathematically when combined with efficient chips.
> **Why this formula?** We use an **Additive Bonus** approach. The physical hardware (Parts A & B) sets the baseline cooling capability. Then, we add bonus points if the "engine" is small or highly efficient. This correctly predicts that a passively cooled flagship will throttle, while a passively cooled budget phone will remain perfectly stable.

## 🟣 7. Connectivity & Sensors

### 🔹 7.1 Cellular Capabilities
*Description:* Network speed and compatibility. Better support means faster downloads and reliable signal in more countries.
*   **Measurement:** Modem specification analysis.
*   **Unit:** Bands / Technology
*   **Significance:** Connectivity speed and global roaming capability.

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
> **Avoid Double Scoring:** The benefits of iSIM (integrated directly into the SoC) are strictly related to **Space Savings** (<1mm² vs ~2mm²) and **Power Efficiency**. These physical engineering advantages are already captured and rewarded in **Section 1.4 (Thickness)** and **Section 8.1 (Battery Endurance)**.
> 
> **Approximation Note:** This is currently an approximation. While **Section 8.1** rewards overall battery life, the theoretical model does not yet strictly quantify the specific µW savings of iSIM vs eSIM, nor do general benchmarks (like GSMArena) typically isolate this specific variable. However, treating them as functionally equivalent in this section prevents double-counting the engineering benefits that don't directly alter the user's *connectivity* options. 

### 🔹 7.3 Wi-Fi Standard
*Description:* Wi-Fi technology. Newer standards (Wi-Fi 7/6E) provide faster, more stable internet, especially in crowded homes.
*   **Measurement:** Supported Wi-Fi protocols.
*   **Unit:** Standard (Generation)
*   **Significance:** Local network speed and congestion management.

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

### 🔹 8.1 Battery Endurance Score (Model v3.2)
*Description:* Evaluates smartphone battery life by prioritizing **real-world performance data** over theoretical specifications via a **Benchmark-First Approach with Predictive Interpolation**.
*   **Measurement:** Standardized battery life tests (or predictive model).
*   **Unit:** Benchmark Score (0-10)
*   **Significance:** Determines how long the phone lasts on a single charge under real-world usage.

**Scoring Philosophy:**
1.  **Primary Truth (Real-World Benchmarks):** When available, real-world benchmark results from trusted sources (GSMArena and PhoneArena) are used as the absolute truth.
2.  **Secondary Truth (Predictive Interpolation):** When benchmark data is missing, we use a detailed **Technical Predictive Model** (based on Energy, Hardware Efficiency, and Software Optimization) to identify "Nearest Neighbor" devices—phones with very similar technical profiles that *do* have benchmark scores. We then interpolate the missing phone's score based on how these similar devices perform in the real world. Ensure widely tested phones have accurate, proven scores, while untested phones get highly educated estimates grounded in reality.

#### Method A: Benchmark Validation (Primary)
*Description:* This is the preferred method when real-world benchmark data is available from trusted sources. Normalization translates hours into a 0-10 score.

**1. Benchmark Sources & Normalization**

*   **GSMArena Active Use Score (v2.0)**
    *   **Source:** [GSMArena Battery Tests v2.0](https://www.gsmarena.com/battery-test-v2.php3)
    *   **Metric:** Active Use Score (Hours)
    *   **Formula:** `GSM_Score = 10 * (Hours - Battery_GSMArena_Hours_Min) / (Battery_GSMArena_Hours_Max - Battery_GSMArena_Hours_Min)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_GSMArena_Hours_Max
    *   **Min Score (0.0):** ≤ Battery_GSMArena_Hours_Min

*   **PhoneArena Battery Life Estimate**
    *   **Source:** [PhoneArena Benchmarks](https://www.phonearena.com/phones/benchmarks/battery)
    *   **Metric:** "Battery Life Estimate" (Hours)
    *   **Formula:** `PA_Score = 10 * (Hours - Battery_PhoneArena_Hours_Min) / (Battery_PhoneArena_Hours_Max - Battery_PhoneArena_Hours_Min)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_PhoneArena_Hours_Max
    *   **Min Score (0.0):** ≤ Battery_PhoneArena_Hours_Min

**2. Scoring Logic (Data Availability)**

*   **Condition 1: Both Benchmarks Available**
    *   If the Target Phone has scores from **both** GSMArena and PhoneArena, take the average of the two normalized benchmark scores. The predictive model is ignored.
    *   **Formula:** `Score = (GSM_Score + PA_Score) / 2`

*   **Condition 2: Partial Data (One Benchmark Available)**
    *   If the Target Phone has a score from **only one** source (e.g., GSMArena), use the single available normalized benchmark score.
    *   **Formula:** `Score = Available_Benchmark_Score`


#### Method B: Nearest Neighbor Interpolation (Secondary / Validation)
Method B is populated for **all** phones (even if Method A is available) to evaluate the precision of the interpolation model by comparing its result with Method A.

**1. Calculate Sub-Layer Scores**
Calculate the 3 sub-layer scores for the Target Phone via Method C:
*   `Layer A` (Energy Score)
*   `Layer B` (Hardware Efficiency Score - HEI)
*   `Layer C` (Software Optimization Score - SOI)

**2. Identify Neighbors via Feature Distance (Minimum Variance)**
Find **3 distinct Reference Phones** that have **BOTH** GSMArena and PhoneArena scores (Condition 1 phones) and the smallest **Weighted Euclidean Distance** to the Target Phone, **excluding the target device** itself:
*   **Distance Metric:** Weighted Euclidean Distance.
    *   `Distance = Sqrt( 0.45*(Diff_LayerA)^2 + 0.35*(Diff_LayerB)^2 + 0.20*(Diff_LayerC)^2 )`
    *   *Where Diff_LayerX = LayerX_Target - LayerX_Neighbor*
*   **Scientific Rationale:** Battery life is a complex trade-off between Capacity (Layer A), Efficiency (Layer B), and Optimization (Layer C). A "Huge Battery / Inefficient" phone (A=10, B=2) can have the same Overall Predicted Score as a "Small Battery / Efficient" phone (A=2, B=10). Weighting the sub-layers ensures we compare "apples to apples" by finding neighbors with similar *profiles*, which is scientifically superior for predicting nonlinear behavior (like thermal throttling or standby drain).
*   **Selection:** Pick the 3 distinct neighbors with the smallest `Distance`.

**3. Calculate Correction Ratio:**
*   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
    *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
*   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
    *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.

**4. Apply to Benchmark:**
*   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
*   `Interpolated_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

> **Example: "FuturePhone 5" (No benchmarks)**
> *   `Predicted_Target = 8.50` (High capacity, high efficiency). *Profile (Layers A/B/C):* 8.5 / 8.5 / 8.5
> *   **Neighbors Found (Via Weighted Euclidean Similarity):**
>     *   Neighbor1: Profile = 8.4/8.6/8.5, predicted score = `(0.45*8.4 + 0.35*8.6 + 0.20*8.5)` = **8.49**, Benchmark = 7.20
>     *   Neighbor2: Profile = 8.6/8.4/8.5, predicted score = `(0.45*8.6 + 0.35*8.4 + 0.20*8.5)` = **8.51**, Benchmark = 7.40
>     *   Neighbor3: Profile = 8.5/8.5/8.6, predicted score = `(0.45*8.5 + 0.35*8.5 + 0.20*8.6)` = **8.52**, Benchmark = 7.00
> *   **Calculations:**
>     *   `Avg_Predicted_Neighbors = (8.49 + 8.51 + 8.52) / 3 = 8.51`
>     *   `Avg_Benchmark_Neighbors = (7.20 + 7.40 + 7.00) / 3 = 7.20`
>     *   `Correction_Ratio = 8.50 / 8.51 = 0.9988` (Target profile is almost identical to neighbors)
>     *   `Interpolated_Score = 0.9988 * 7.20 = 7.19`


#### Method C: Predicted Calculation (Tertiary)
*Description:* This section defines the technical scoring logic used to characterize a device's hardware and software profile. It is used to calculate a "Predicted Score" which serves as the coordinate system for finding "Nearest Neighbors" in Method B.

**Step 1: Calculate Layer A (Battery Energy - 45%)**

*Why it matters:* Battery life is fundamentally bounded by the total amount of energy stored. No matter how efficient a phone is, it cannot run without fuel. We calculate the total energy in Watt-hours (Wh) because it accounts for voltage differences, providing a more accurate measure of true capacity than milliamp-hours (mAh) alone.

*Voltage Detection Logic:*
Modern smartphones use either single-cell or dual-cell battery configurations:
1. **Single-Cell (Standard):** One lithium-ion cell at **3.85V nominal**
   - Used in most phones with charging ≤ 100W
   - Lower current, simpler charging circuitry

2. **Dual-Cell (High-Power Charging):** Two cells in series at **7.7V nominal** (2 * 3.85V)
   - Required for ultra-fast charging (≥120W) to reduce current and heat
   - Example: iQOO phones with 120W charging use 3500mAh @ 7.7V (equivalent to 7000mAh @ 3.85V)
   - Manufacturers typically report PER-CELL capacity, not equivalent capacity

*Detection Priority:*
1. **Explicit Voltage:** If `battery_voltage_v` contains a numeric value → use that value
2. **Dual-Cell Indicators:** If `battery_cell_configuration` contains "Dual-cell", "Dual cell", "2S", or "dual-cell" (case-insensitive) → use **7.7V**
3. **High-Power Charging Heuristic:** If wired charging watts ≥ 120W → use **7.7V** (almost all ≥120W phones use dual-cell)
4. **Default Fallback:** Otherwise → use **3.85V** (single-cell standard)

*   **Formula:** `Wh = (mAh * V) / 1000` (Use explicit Wh if provided, otherwise calculate)
*   **Formula:** `Energy_Score = 10 * (Wh - Battery_Energy_Wh_Min) / (Battery_Energy_Wh_Max - Battery_Energy_Wh_Min)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_Energy_Wh_Max
    *   **Min Score (0.0):** ≤ Battery_Energy_Wh_Min

> [!NOTE]
> **Why Linear?** Battery energy storage scales linearly with capacity. A 20 Wh battery stores exactly twice as much energy as a 10 Wh battery, providing proportionally longer runtime. There are no diminishing returns in energy storage - more Watt-hours directly translates to more battery life.
> **Why 7.7V for dual-cell?** High-power charging generates significant heat. By using two cells in series, current is halved for the same power, reducing resistive heating and enabling safer fast charging without overheating.

**Step 2: Calculate Layer B (Baseline Energy Demand - 35%)**
*Description:* This layer evaluates how efficiently the phone's hardware converts stored energy into baseline usage (Baseline Energy Demand).

> [!NOTE]
> **The Peak vs. Baseline Demand Paradox:** 
> Why does a flagship CPU (like Snapdragon 8 Gen 3) receive a low Cooling Bonus in the **Thermal Dissipation Model (Section 6.10)**, but a high Efficiency Bonus here in the **Battery Model**? 
> *   **Thermals (Peak Demand):** Section 6.10 measures *Peak Thermal Demand*. Under maximum load in a benchmark, a flagship CPU draws massive wattage (~15W) and generates intense heat, demanding heavy cooling compensation. 
> *   **Battery (Baseline Demand):** Battery life is dominated by *Baseline Energy Demand* (mixed use, standby, video playback). The same flagship CPU's advanced architecture (high IPC) completes these light tasks instantly and "races-to-sleep," drawing significantly less power than an older, inefficient CPU. 
> Therefore, high-end architecture is a *penalty* for peak thermals, but a *massive bonus* for baseline battery efficiency.

*   **B.1 SoC Efficiency (40% of Layer B)**
    *   **B.1.1 Process Node (50% of SoC)**
        *   *Why it matters:* Process node (nm) is the biggest determinant of a chip's power efficiency. Smaller transistors require less voltage to switch. Foundry differences are also critical (e.g., TSMC vs Samsung).
        *   *Formula:* Use the **Process Node Score** from **Section 6.10 Part C** exclusively (i.e., `(0.9 * Node_Score) + (0.1 * Foundry_Score)`). Do **not** use the full TDSI score (which additionally includes the physical body Parts A & B and the Load Bonus).

    *   **B.1.2 CPU Architecture Class (30% of SoC)**
        *   *Why it matters:* Efficiency cores (e.g., A520) handle 80% of daily tasks. We use the Architecture Efficiency Score (AES) to evaluate the weighted average efficiency of the entire CPU cluster, accurately predicting idle/low-load power.
        *   *Formula:* `Sum(Core_Score * Core_Count) / Total_Core_Count`
            *   *Range is 0-10.*
        *   *Reference:* Standard Core Scores from **Section 6.1.0**.

        > [!NOTE]
        > **Why Linear and Unadjusted for Frequency?** 
        > 1. **Why Linear? (Work vs. Speed):** Benchmarks measure **Speed** (Clock Frequency), which scales power quadratically ($P \propto V^2 \times f$). High benchmark scores often mean high power drain, not efficiency. AES measures **Work-per-Clock** (IPC), which scales performance linearly without the voltage penalty. The architectural baseline quality of the cores across generations scales approximately linearly in its ability to offer proportionately better work-per-watt efficiency at baseline loads.
        > 2. **Why No Frequency Adjustment? (The "Efficiency Core" Reality):** While peak clock frequency dramatically increases maximum power draw (which hurts performance/watt at peak load), battery endurance tests primarily simulate mixed-use, video playback, and standby scenarios. In these scenarios, the CPU spends the vast majority of its time in deep sleep or running at low-power clock domains. Battery life is dominated by the efficiency cores (e.g., Cortex-A520/A55) that handle 80% of daily background tasks. Therefore, the *intrinsic architectural efficiency* (IPC) of the cluster matters far more for predicting whole-day endurance than the chip's theoretical maximum speed limit. AES is the *only* metric that accounts for the generational quality of the efficiency cores, accurately predicting the device's idle/low-load power profile. Peak power penalties are handled naturally during active high-load benchmarking (Method A) or indirectly through thermal bleeding, not at the baseline calculation step.

    *   **B.1.3 GPU Architecture Class (20% of SoC)**
        *   *Why it matters:* Similar to CPUs, newer GPU architectures deliver higher performance per watt.
        *   *Reference:* **Efficiency Score** column from **Section 6.3.0**.
            *   *Note:* The scoring table is defined in Section 6.3.0. For battery calculations, we use the specific **Efficiency Score** which decouples raw performance from power draw (e.g., penalizing hot chips like Snapdragon 888). This score measures performance-per-watt rather than peak capability.
        
        > [!NOTE]
        > **Avoid Double Counting:** Process node benefits (e.g., 5nm vs 3nm) are handled in the **SoC Efficiency Score (Section 6.10)**, which is used in **Section B.1.1**. This GPU Efficiency Score focuses on the **architectural efficiency** and thermal stability of the GPU implementation itself, regardless of the node. Ideally, an efficient architecture on an efficient node gets high scores in both. A "hot" architecture on an efficient node would get a lower GPU score despite the good node score.
    *   `SoC_Efficiency = (0.50 * Node) + (0.30 * CPU) + (0.20 * GPU)`

*   **B.2 Display Efficiency (40% of Layer B)**
    *   **B.2.1 Panel Technology (35% of Display)**
        *   *Why it matters:* This metric captures the **intrinsic power efficiency** of the panel technology itself (pixel emission, backlight efficiency, black-level power draw), **independent of refresh rate**. It answers: *"How much energy does this panel consume to display a static image?"*
        *   *Reference:* Panel Technology score from **Section 2.1**.
            *   *Note:* OLED panels are inherently more power-efficient than LCDs because they don't require a backlight and can turn off individual pixels for true black.
            *   *Difference from B.2.2:* This section does NOT reward adaptive refresh rates (like LTPO). That benefit is fully captured in B.2.2. Here, we focus purely on the material and structural efficiency of the screen.
    *   **B.2.2 Refresh Efficiency (35% of Display)**
        *   *Why it matters:* This metric captures the **dynamic power efficiency** related to screen updates. It answers: *"How often does the screen need to redraw, and how smart is it about not redrawing unnecessarily?"*
            *   *Difference from B.2.1:* This is where LTPO panels shine. Their ability to drop to 1Hz is rewarded here via the `effective_hz` calculation.
        *   *Formula:* `effective_hz = adaptive ? (min_hz + max_hz) / 2 : max_hz`
        *   *Formula:* `Refresh_Score = 10 - 10 * (effective_hz - Battery_Refresh_Effective_Hz_Min) / (Battery_Refresh_Effective_Hz_Max - Battery_Refresh_Effective_Hz_Min)` (Clamped 0-10)

        > [!NOTE]
        > **Why Linear?** Display power consumption scales linearly with refresh rate. A 120Hz display uses approximately 2x the power of 60Hz because it updates the screen twice as often. Unlike visual quality (where higher refresh rates have diminishing perceptual returns), power draw is strictly proportional to refresh frequency.

    *   **B.2.3 Resolution Efficiency (30% of Display)**
        *   *Why it matters:* Pushing more pixels requires more GPU power and backlight brightness.
        *   *Formula:* `Resolution_Score = 10 - 10 * (megapixels_mp - Battery_Resolution_MP_Min) / (Battery_Resolution_MP_Max - Battery_Resolution_MP_Min)` (Clamped 0-10)

        > [!NOTE]
        > **Why Linear?** Power consumption scales roughly linearly with pixel count in the practical phone display range. While GPU and display power don't increase perfectly proportionally with megapixels due to modern optimizations, the relationship is close enough to linear that a simple linear formula provides an accurate approximation for battery efficiency scoring.

    *   `Display_Efficiency = (0.35 * Panel_Tech) + (0.35 * Refresh) + (0.30 * Resolution)`

*   **B.3 Connectivity Efficiency (10% of Layer B)**
    *   **B.3.1 Cellular Generation (70%)**
        *   *Why it matters:* Newer cellular standards provide faster speeds but require complex, power-hungry modems. This is an **inverted** scale (older = better battery).
        *   *Scoring Table:*

        | Technology                                   | Score    |
        | :------------------------------------------- | :------- |
        | **2G Only**                                  | **10.0** |
        | **3G fallback only**                         | **8.0**  |
        | **4G LTE (Basic)**                           | **6.0**  |
        | **4G LTE-Advanced Pro**                      | **4.0**  |
        | **5G Sub-6 (Limited/regional bands)**        | **2.0**  |
        | **5G Sub-6 (Full Global Bands)**             | **1.0**  |
        | **5G mmWave + Sub-6 (Global band coverage)** | **0.0**  |

        > [!NOTE]
        > **Why Inverted Scoring?** Newer cellular generations (5G) require more complex modems with higher power consumption than older standards (4G, 3G). While 5G provides faster speeds, it comes at a battery efficiency cost. This inverted scoring reflects the bare power penalty. See **Section 7.1** for feature-based scoring (where newer = better).

    *   **B.3.2 Wi-Fi Generation (30%)**
        *   *Why it matters:* Newer Wi-Fi standards use wider channels which consume more power. Also an **inverted** scale.
        *   *Scoring Table:*

        | Standard     | Score    |
        | :----------- | :------- |
        | **Wi-Fi ≤ 3**| **10.0** |
        | **Wi-Fi 4**  | **7.0**  |
        | **Wi-Fi 5**  | **5.0**  |
        | **Wi-Fi 6**  | **3.0**  |
        | **Wi-Fi 6E** | **2.0**  |
        | **Wi-Fi 7**  | **0.0**  |

        > [!NOTE]
        > **Why Inverted Scoring?** Newer WiFi standards (WiFi 6E, 7) use wider channels (160MHz, 320MHz) and higher frequency bands (6GHz) which require more power to maintain. While they provide better performance, they reduce battery efficiency. See **Section 7.3** for feature-based scoring.

    *   `Connectivity_Efficiency = (0.70 * Cellular) + (0.30 * WiFi)`

*   **B.4 Thermal Efficiency (10% of Layer B)**
    *   *Why it matters:* Heat increases internal resistance and leakage currents. Good cooling preserves battery efficiency.
    *   *Formula:* `Thermal_Efficiency = TDSI_Score` (From **Section 6.10**)

    > [!NOTE]
    > The **same TDSI score** is used in both contexts because thermal management capability is an objective hardware characteristic. The different impact on performance vs. battery efficiency is handled through **weighting**.

*   **Final Layer B Formula:** `HEI = (0.40 * SoC) + (0.40 * Display) + (0.10 * Connectivity) + (0.10 * Thermal)`

**Step 3: Calculate Layer C (Software Optimization Index - 20%)**
*Description:* This layer accounts for the efficiency of the operating system and the impact of pre-installed background bloatware.

*   **C.1 OS Power Management Architecture (60%)**
    *   *Why it matters:* The operating system's kernel and power management framework determine how effectively hardware resources are utilized. Modern OS versions (Android 12+, iOS 15+) act as a neutral baseline for efficiency, introducing standardized features like aggressive background process freezing, precise alarm management, and improved scheduler awareness (e.g., Android's "Performance Class" standards).

    > [!NOTE]
    > **Neutrality Principle:** This score is determined **strictly by the OS Generation**, not the brand.
    > *   **Modern Architecture (Score 10.0-8.0):** Features standardized "phantom process" killing, strict background execution limits, and deep hardware integration.
    > *   **Legacy Architecture:** Lacks modern power-saving APIs, leading to higher standby drain.

    | OS Gen (Android) | OS Gen (iOS) | Score    | Status               |
    | :--------------- | :----------- | :------- | :------------------- |
    | **Android 14+**  | **iOS 17+**  | **10.0** | Current/Cutting Edge |
    | **Android 13**   | **iOS 16**   | **9.0**  | Recent Modern        |
    | **Android 12**   | **iOS 15**   | **8.0**  | Modern Standard      |
    | **Android 10-11**| **iOS 13-14**| **6.0**  | Legacy Support       |
    | **Android 8-9**  | **iOS 11-12**| **4.0**  | Aging                |
    | **Android < 8**  | **iOS < 11** | **0.0**  | Obsolete             |

*   **C.2 Bloatware Overhead (40%)**
    *   *Why it matters:* Bloatware often runs hidden background processes causing "phantom" standby drain.
    *   *Reference:* Use the System Cleanliness & Control (SCC) score from **Section 5.2**.

*   **Final Layer C Formula:** `SOI = (0.60 * OS_Age) + (0.40 * SCC)`

**Step 4: Calculate Predicted Score**
*   **Formula:** `Predicted_Score = (0.45 * Energy_Score) + (0.35 * HEI) + (0.20 * SOI)`


### 🔹 8.2 Wired Charging Speed
*Description:* Charging speed with a cable. Higher wattage means you spend less time tethered to a wall outlet.
*   **Measurement:** Peak power input via wired connection.
*   **Unit:** Watts (W)
*   **Significance:** Reduces downtime when battery is low.
*Formula:* `Score = 10 * ((1/Battery_Wired_Charging_W_Min) - (1/Watts)) / ((1/Battery_Wired_Charging_W_Min) - (1/Battery_Wired_Charging_W_Max))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Battery_Wired_Charging_W_Max
*   **Min Score (0.0):** ≤ Battery_Wired_Charging_W_Min
> [!NOTE]
> **Why Inverse Proportional?** The actual charging time ($T$) rests precisely on an inverse hyperbola with wattage ($W$): $T \propto C / W$. Upgrading from 15W to 30W cuts charge time in half (saving ~45 minutes). Upgrading from 100W to 120W saves less than 2 minutes. Scoring the wattage via an exact Inverse formula perfectly plots the true user benefit: raw **Time Saved** waiting at the wall outlet.

### 🔹 8.3 Wireless Charging Speed
*Description:* Charging speed without cables. Convenient for topping up battery by simply placing the phone on a pad.
*   **Measurement:** Peak power input via wireless coil.
*   **Unit:** Watts (W)
*   **Significance:** Convenience and ease of topping up.
*Formula:* `Score = 10 * ((1/Battery_Wireless_Charging_W_Min) - (1/Watts)) / ((1/Battery_Wireless_Charging_W_Min) - (1/Battery_Wireless_Charging_W_Max))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ Battery_Wireless_Charging_W_Max
*   **Min Score (0.0):** ≤ Battery_Wireless_Charging_W_Min
> [!NOTE]
> **Why Inverse Proportional?** Just like wired charging, the time it takes to charge wirelessly follows an inverse hyperbolic curve ($T \propto 1/W$). Scoring the wattage inversely perfectly models the raw minutes of charging time saved, recognizing that jumping from 5W to 15W is a transformative time-saver, while jumping from 50W to 60W is nearly negligible.

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
