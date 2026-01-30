# Comprehensive Smartphone Scoring Rules (v8.0) - Let's build the Golden Standard together

This document provides **exhaustive, unit-specific reference tables** for every technical criterion found in the v4.0 Data Structure.
*   **Principle:** Every single data point that differentiates a product must have a corresponding score.
*   **Normalization:** 0 = Worst/Obsolete, 10 = Best/State-of-the-Art.
*   **Units:** All criteria include specific units of measurement.


## 🟣 1. Design & Build Quality

### 🔹 1.1 Materials (Frame/Back)
*Description:* The physical materials used for the device chassis and rear panel. Affects how premium the phone feels, how well it resists drops, and how cool it stays during use.
*   **Measurement:** Manufacturer specifications and teardown confirmation.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Determines structural integrity, thermal dissipation, and tactile quality.

**Final Score Formula:**
`Materials Score = (0.6 × Frame Material Score) + (0.4 × Back Material Score)`

> [!NOTE]
> **Why this weighting is explicit:** The frame governs structural rigidity, torsional strength, and thermal conduction pathways more than the back panel, which mainly affects surface durability, radio transparency, and impact shatter behavior.

#### 1.1.A Frame Material (Structural Class)
*   **Measurement:** Manufacturer specifications and teardown confirmation.
*   **Unit:** Material Class
*   **Significance:** Determines chassis rigidity, bending resistance, and heat transfer from internal components to the outer shell.

| Score    | Frame Material Class       |
| :------- | :------------------------- | 
| **10.0** | **Titanium Alloy Frame**   |  
| **8.5**  | **Stainless Steel Frame**  |
| **7.0**  | **Aluminum Alloy Frame**   |  
| **4.0**  | **Polymer Composite Frame**| 
| **0.0**  | **Material Not Disclosed** | 

**Titanium Alloy Frame**: Titanium alloy structural frame; high strength-to-weight ratio, low thermal conductivity versus steel, high corrosion resistance
**Stainless Steel Frame**: Steel alloy structural frame; very high rigidity and mass, high thermal conductivity, strong impact resistance
**Aluminum Alloy Frame**: Aluminum structural frame; moderate rigidity, low mass, high thermal conductivity
**Polymer Composite Frame**: Structural frame made from plastic or fiber-reinforced polymer; low thermal conductivity, lower stiffness than metals
**Material Not Disclosed**: Frame material not specified in official documentation or teardown sources

#### 1.1.B Back Panel Material (Surface Class)
*   **Measurement:** Manufacturer specifications and teardown confirmation.
*   **Unit:** Material Class
*   **Significance:** Affects scratch resistance, shatter risk, radio signal transparency, and surface heat dissipation.

| Score    | Back Material Class        |                                                |
| :------- | :------------------------- | 
| **10.0** | **Ceramic Back**           |
| **8.0**  | **Strengthened Glass Back**|
| **6.0**  | **Standard Glass Back**    |
| **4.0**  | **Polymer Back**           |
| **0.0**  | **Material Not Disclosed** |

**Ceramic Back**: Back panel made from ceramic or ceramic composite; high surface hardness, low radio frequency interference, high brittleness
**Strengthened Glass Back**: Chemically strengthened aluminosilicate glass (e.g., Gorilla Glass, Victus); moderate hardness, brittle fracture behavior
**Standard Glass Back**: Glass back without strengthened certification; similar brittleness with lower surface hardness
**Polymer Back**: Plastic or polymer rear panel; low brittleness, low surface hardness, high radio frequency transparency
**Material Not Disclosed**: Back material not specified in official documentation or teardown sources   

### 🔹 1.2 Durability (Ingress Protection)
*Description:* Ingress Protection rating against dust and water. Dust and water resistance are tested separately under IEC 60529. A phone can be fully dust-sealed but weak against immersion, or vice versa. Treating them independently reflects the actual certification process and physical risks.
*   **Measurement:** Manufacturer IP certification (IEC 60529).
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for device longevity and accident protection.

**Final Score Formula:**
`IP Score = (0.5 × Dust Protection Score) + (0.5 × Water Protection Score)`

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

| Score    | Declared Glass Type                | Example Models                |
| :------- | :--------------------------------- | :---------------------------- |
| **10.0** | **Gorilla Glass Armor**            | Galaxy S24 Ultra              |
| **9.5**  | **Ceramic Shield (current gen)**   | iPhone 15 / 16 series         |
| **9.0**  | **Gorilla Glass Victus 2**         | OnePlus 12, S23 Ultra         |
| **8.0**  | **Gorilla Glass Victus / Victus+** | Pixel 7 Pro, Xiaomi 12S Ultra |
| **7.0**  | **Gorilla Glass 5 / 6**            | Galaxy A54, Nothing Phone (1) |
| **5.0**  | **Gorilla Glass 3 / Panda Glass**  | Budget mid-range              |
| **3.0**  | **Tempered Glass**                 | Low-end devices               |
| **2.0**  | **Glass (Unspecified)**            | Entry-level                   |
| **0.0**  | **Plastic / No Glass**             | Feature phones                |

**Gorilla Glass Armor**: Flagship reinforced glass with anti-reflective and ≥2.0m-class drop certification  
**Ceramic Shield (current gen)**: Ceramic-infused glass with ≥2.0m-class drop certification  
**Gorilla Glass Victus 2**: Advanced reinforced glass rated for drops on rough surfaces (~2.0m class)  
**Gorilla Glass Victus / Victus+**: Reinforced glass rated for ~2.0m drops  
**Gorilla Glass 5 / 6**: Mid-tier reinforced glass rated for ~1.6m drops  
**Gorilla Glass 3 / Panda Glass**: Entry-tier reinforced glass rated for ~1.2m drops  
**Tempered Glass**: Basic chemically strengthened glass (no certified drop class)  
**Glass (Unspecified)**: Manufacturer does not disclose protection class  
**Plastic / No Glass**: Polymer display cover

### 🔹 1.4 Dimensions (Thickness)
*Description:* Device thickness excluding camera bump. Thinner phones are easier to hold and fit better in pockets.
*   **Measurement:** Calipers at the thickest point of the body (excluding camera protrusion).
*   **Unit:** Millimeters (mm)
*   **Significance:** Affects pocketability and hand comfort.
*Formula:* `Score = 10 - 10 * ((Thickness - 7.0) / (10.0 - 7.0))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ 7.0 mm
*   **Min Score (0.0):** ≥ 10.0 mm
> [!NOTE]
> This is a continuous linear scoring metric. Thinner is better.

### 🔹 1.5 Weight
*Description:* Total device weight. Lighter phones are more comfortable to hold for long periods (e.g., reading, watching videos) without wrist strain.
*   **Measurement:** Digital scale weight including battery.
*   **Unit:** Grams (g)
*   **Significance:** Determines long-term holding comfort and fatigue.
*Formula:* `Score = 10 - 10 * ((Weight - 150) / (250 - 150))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ 150 g
*   **Min Score (0.0):** ≥ 250 g
> [!NOTE]
> This is a continuous linear scoring metric. Lighter is better.

### 🔹 1.6 Ergonomics (Width & Handling)
*Description:* Quantifies how easy the phone is to hold and operate with one hand. Width is the primary factor determining grip comfort and reachability.
*   **Measurement:** Device Width
*   **Unit:** Millimeters (mm)
*   **Significance:** Narrower phones are significantly easier to grip and use one-handed.
*Formula:* `Score = 10 - 10 * ((Width - 70.0) / (80.0 - 70.0))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ 70.0 mm (Compact / Easy Grip)
*   **Min Score (0.0):** ≥ 80.0 mm (Wide / Two-Handed Use)
> [!NOTE]
> This is a continuous linear scoring metric. Narrower is better for ergonomics. While curvature affects feel, width is the absolute limit for hand size.


## 🟣 2. Display

### A. Display Architecture (What it is)

### 🔹 2.1 Display Panel Architecture (DPA)
*Description:* Evaluates the physical display technology used to generate light and images. Focuses on panel construction and emission method — not brightness, color accuracy, refresh behavior, or power efficiency. OLED panels offer perfect blacks and vibrant colors due to self-emissive pixel control.
*   **Measurement:** Manufacturer specifications and teardown confirmations.
*   **Unit:** Panel Technology Tier (0–10)
*   **Significance:** Determines contrast capability, viewing angle stability, and pixel-level light control.

| Score    | Panel Type                 | Example Models              |
| :------- | :------------------------- | :-------------------------- |
| **10.0** | **Tandem OLED**            | iPad Pro M4 (Reference)     |
| **9.0**  | **OLED (LTPO/AMOLED)**     | S24 Ultra, iPhone 15 Pro    |
| **6.0**  | **IPS LCD**                | iPhone 11, Poco X4 GT       |
| **2.0**  | **TFT / PLS LCD**          | Budget devices              |
| **0.0**  | **TN LCD / Legacy**        | Galaxy J1 (Legacy)          |

**Tandem OLED**: Dual-stack emissive OLED panel (two light-emitting layers)  
**OLED (LTPO/AMOLED)**: Self-emissive OLED panel (AMOLED, P-OLED, Dynamic AMOLED, LTPO OLED, LTPS OLED)  
**IPS LCD**: LED-backlit LCD with in-plane switching  
**TFT / PLS LCD**: Thin-film transistor LCD (non-IPS), includes PLS (Plane-to-Line Switching)  
**TN LCD / Legacy**: Twisted nematic LCD and other legacy technologies

> [!IMPORTANT]
> **Single Source of Truth:** This table is the master reference for all display panel scores. Battery efficiency scoring (Section B.2.1) references this table.

### B. Visual Output Quality (What it looks like)

### 🔹 2.2 Resolution Density
*Description:* Pixel density (sharpness). Higher PPI means text and images look crisp, with no visible pixels.
*   **Measurement:** Pixels Per Inch (PPI)
*   **Unit:** PPI
*   **Significance:** Determines visual sharpness and clarity of text.
*   **Data Structure Mapping:** `2_2_resolution_density.ppi`

*Formula:* `Score = 10 * (log(PPI) - log(200)) / (log(600) - log(200))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 600 PPI
*   **Min Score (0.0):** ≤ 200 PPI
> [!NOTE]
> **Why Logarithmic?** Human visual acuity has diminishing returns. The difference in sharpness between 200 and 300 PPI is immediately obvious, while the difference between 500 and 600 PPI is barely perceptible to the naked eye.

### 🔹 2.3 Brightness (Peak)
*Description:* Maximum brightness in sunlight. Higher nits mean the screen is easily readable even under direct, bright sun.
*   **Measurement:** Peak brightness on a 1% window (APL) or High Brightness Mode (HBM).
*   **Unit:** Nits (cd/m²)
*   **Significance:** Critical for outdoor visibility and HDR content impact.
*Formula:* `Score = 10 * (log(Nits) - log(400)) / (log(4500) - log(400))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 4500 nits
*   **Min Score (0.0):** ≤ 400 nits
> [!NOTE]
> **Why Logarithmic?** Brightness perception follows the Weber-Fechner law. A jump from 500 to 1000 nits is perceived as a significant doubling in brightness, whereas a jump from 3000 to 3500 nits is perceived as a much smaller increase.

### 🔹 2.4 Color Gamut Coverage (CGC)
*Description:* Measures how much of standard color spaces the display can reproduce. This defines what the screen can physically display in terms of color richness and saturation.
*   **Measurement:** DCI-P3 coverage percentage from manufacturer specs or review databases.
*   **Unit:** Percentage (%)
*   **Significance:** Determines real-world color vibrancy and HDR reproduction capability.

*Formula:* `Score = 10 * (P3_percent - 85) / (100 - 85)` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 100% DCI-P3
*   **Min Score (0.0):** ≤ 85% DCI-P3

> [!NOTE]
> **Why this works:** DCI-P3 is the industry HDR content standard. The scale is continuous, fully quantitative, and automation-friendly.
> **sRGB Fallback:** If only sRGB data is available (typical for legacy or budget screens), the score is **0.0** because 100% sRGB corresponds to approximately 75-80% DCI-P3, which falls below the minimum threshold for modern wide-gamut scoring.

### 🔹 2.5 HDR Format Support (HFS)
*Description:* Measures which HDR video formats the display officially supports (decoding capability).
*   **Measurement:** Manufacturer specifications and DRM capability lists.
*   **Unit:** Supported Standards (Binary Features)
*   **Significance:** Ensures compatibility with premium content from streaming services (Netflix, Disney+, etc.).

| Score    | Supported Formats                 |
| :------- | :-------------------------------- |
| **10.0** | **Dolby Vision + HDR10+ + HDR10** |
| **8.0**  | **HDR10+ + HDR10**                |
| **6.0**  | **HDR10 only**                    |
| **0.0**  | **No HDR formats**                | 

### C. Interaction & Motion (How it behaves)

### 🔹 2.6 Motion Smoothness (Max Refresh Rate)
*Description:* How many times the screen updates per second. 120Hz+ makes scrolling and animations look incredibly smooth compared to standard 60Hz.
*   **Measurement:** High-speed camera analysis or system reporting.
*   **Unit:** Hertz (Hz)
*   **Significance:** Determines the smoothness of motion and animations.
*Formula:* `Score = 10 * (log(Hz) - log(45)) / (log(165) - log(45))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 165 Hz
*   **Min Score (0.0):** ≤ 45 Hz
> [!NOTE]
> **Why Logarithmic?** Motion smoothness perception follows Weber's Law. The upgrade from 60Hz to 120Hz is a massive leap in fluidity. The step from 120Hz to 144Hz or 165Hz is much harder to perceive for the average user.

### 🔹 2.7 Touch Responsiveness
*Description:* How fast the screen reacts to your touch. Higher rates mean instant response in games and a "glued to your finger" feel.
*   **Measurement:** Touch latency testing (time from touch to signal).
*   **Unit:** Hertz (Hz)
*   **Significance:** Critical for competitive gaming and UI fluidity.
*Formula:* `Score = 10 * (log(Hz) - log(60)) / (log(960) - log(60))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 960 Hz
*   **Min Score (0.0):** ≤ 60 Hz
> [!NOTE]
> **Why Logarithmic?** Input latency perception is non-linear. Increasing sampling rate from 60Hz to 240Hz provides a noticeably "stickier" feel. Beyond 480Hz, the improvements in reaction time are smaller than the average human reaction variance.

### 🔹 2.8 Eye Comfort (PWM Dimming)
*Description:* How the screen dims. Higher frequencies prevent eye strain, headaches, and fatigue for people sensitive to screen flicker.
*   **Measurement:** Oscilloscope or flicker meter at low brightness levels.
*   **Unit:** Hertz (Hz)
*   **Significance:** Reduces eye strain and headaches for sensitive users.
*Formula:* `Score = 10 * (log(Hz) - log(120)) / (log(3840) - log(120))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 3840 Hz
*   **Min Score (0.0):** ≤ 120 Hz
> [!NOTE]
> **Why Logarithmic?** The health benefits of higher PWM frequencies follow a diminishing return curve. The jump from 240Hz to 480Hz significantly reduces visible flicker for sensitive eyes, whereas the difference between 2000Hz and 3000Hz is marginal.

### D. Physical Immersion (How big it feels)

### 🔹 2.9 Screen Size
*Description:* The physical size of the display measured diagonally. Larger screens offer more immersive media and gaming experiences.
*   **Measurement:** Diagonal length of the active display area.
*   **Unit:** Inches (")
*   **Significance:** Determines immersion level and device footprint.
*Formula:* `Score = 10 * ((Size - 4.5) / (7.6 - 4.5))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 7.6"
*   **Min Score (0.0):** ≤ 4.5"
> [!NOTE]
> This is a continuous linear scoring metric. Larger screens provide more immersion.

### 🔹 2.10 Screen-to-Body Ratio (Bezels)
*Description:* How much of the front is screen vs. border. Higher percentage means thinner bezels and a more immersive, modern look.
*   **Measurement:** (Active Display Area / Total Frontal Area) * 100.
*   **Unit:** Percentage (%)
*   **Significance:** Aesthetic modernity and immersion.
*Formula:* `Score = 10 * ((Ratio - 60) / (93 - 60))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 93%
*   **Min Score (0.0):** ≤ 60%
> [!NOTE]
This is a continuous linear scoring metric. Higher ratio means thinner bezels.


## 🟣 3. Processing Power & Performance

### 🔹 3.1 SoC Performance (Sustained Outcome)
*Description:* Measures actual delivered performance in standardized workloads, regardless of architecture, clocks, or vendor optimizations. This represents the "heavy lifting" capability of the device.

*   **Measurement:** Geekbench 6 Multi-Core Score.
*   **Unit:** Points
*   **Significance:** Primary indicator of sustained workloads, gaming potential, and multitasking capability.

#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct Geekbench 6 score is available. It provides the most accurate representation of real-world performance.
`Score = 10 * (log(Score) - log(GB6_Multi_Worst_Phone)) / (log(GB6_Multi_Best_Phone) - log(GB6_Multi_Worst_Phone))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ GB6_Multi_Best_Phone
*   **Min Score (0.0):** ≤ GB6_Multi_Worst_Phone
> [!NOTE]
> **Why Logarithmic?** Performance utility follows diminishing returns. The difference between a laggy 500-point phone and a usable 1500-point phone is transformative. The difference between an 8500-point flagship and a 9500-point gaming beast is noticeable only in extreme niche scenarios.

#### 3.1.1 CPU Core Architecture Reference

**Master Scoring Table** (used across all CPU performance calculations)

This table provides the authoritative CPU core architecture scores used throughout the scoring system, including:
- Section 3.1 Method C: Multi-Thread Performance (CPS calculation)
- Section 3.2 Method C: Single-Thread Performance (CAS calculation)
- Battery Endurance Scoring (Battery efficiency - SoC component)

**Scoring Basis:** Based on IPC (Instructions Per Clock) performance and modern architecture capabilities.

| CPU Core Architecture        | Score  | Generation | Notes                          |
|------------------------------|--------|------------|--------------------------------|
| **Apple A18 / A17 Pro / A17**| **10** | 2023-2024  | Highest IPC, 3nm process       |
| **Cortex-X925**              | **10** | 2024       | ARMv9.2, latest flagship       |
| **Cortex-X4**                | **10** | 2023       | ARMv9, flagship performance    |
| **Cortex-X3**                | **9**  | 2022       | ARMv9 flagship                 |
| **Cortex-X2**                | **8**  | 2021       | ARMv9 early flagship           |
| **Cortex-A720 / A715**       | **7**  | 2023-2024  | ARMv9 modern performance       |
| **Cortex-A710**              | **6**  | 2021       | ARMv9 transitional             |
| **Cortex-A78 / A77**         | **6**  | 2019-2020  | ARMv8.2 legacy flagship        |
| **Cortex-A76 / A75**         | **5**  | 2017-2018  | ARMv8.2 older flagship         |
| **Cortex-A73**               | **4**  | 2016       | ARMv8 budget performance       |
| **Cortex-A55**               | **2**  | 2017       | ARMv8.2 modern efficiency      |
| **Cortex-A520 / A510**       | **2**  | 2021-2023  | ARMv9 efficiency cores         |
| **Cortex-A53 / A7**          | **0**  | 2012-2014  | ARMv8 ancient efficiency       |

> [!IMPORTANT]
> **Single Source of Truth:** This table is the master reference for all CPU core scores. All other sections reference this table. Do not duplicate or modify scores elsewhere.

#### Method B: Nearest Neighbor Interpolation (Secondary)
If the specific device has no benchmark, but we have data for other devices:
1.  **Identify Neighbors:** Find **3 Reference Phones** that have **BOTH** Geekbench scores and known specs. Select the ones with the closest **Theoretical Score** (calculated via Method C) to the target device.
2.  **Calculate Correction Ratio:**
    *   `Avg_Theoretical_Neighbors = (Theory_Neighbor1 + Theory_Neighbor2 + Theory_Neighbor3) / 3`
    *   `Ratio = Theoretical_Target / Avg_Theoretical_Neighbors`
3.  **Apply to Benchmark:**
    *   `Avg_Benchmark_Neighbors = (Bench_Neighbor1 + Bench_Neighbor2 + Bench_Neighbor3) / 3`
    *   `Estimated_Score = Ratio * Avg_Benchmark_Neighbors`

#### Method C: Theoretical Calculation (Tertiary)
Used as a standalone fallback if no neighbors exist, or as the **Predictor** for Method B.

**Step 1: Calculate Cluster Power Score (CPS)**
*   *What is it?* A sum of all CPU cores weighted by their strength.
*   **Formula:** `Sum(Core_Weight * Core_Count)`
*   **Core Weights:** See **Section 3.1.1 CPU Core Architecture Reference** for authoritative core scores.

**Step 2: Architecture Efficiency Score (AES)**
*   *What is it?* The average quality of the cores.
*   **Formula:** `Sum(Core_Weight * Core_Count) / Total_Core_Count`
    *   *Range is 0-10.
    *   **Why AES?** CPS measures total throughput (quantity), while AES measures architectural efficiency (quality). A high CPS with low AES implies many weak cores (server-like), while high AES implies strong individual cores (consumer flagship).

**Step 3: Frequency Scaling Factor (FSF)**
*   *What is it?* A multiplier for clock speed.
*   **Formula:** `1 + (Max_Freq_GHz - Max_Freq_GHz_Worst_Phone) / (Max_Freq_GHz_Best_Phone - Max_Freq_GHz_Worst_Phone)`
    *   *Range is 1-2.
    *   **Why FSF?** Two SoCs with identical cores (e.g., Cortex-A78) will perform differently if one is clocked at 2.0GHz and the other at 3.0GHz. FSF accounts for this linear performance gain from clock speed.

**Step 4: Calculate Final Score**
1.  **Raw Throughput (PTS - Predicted Throughput Score):** `CPS * AES * FSF`
2.  **Final Score:** `10 * (log(PTS) - log(PTS_Worst_Phone)) / (log(PTS_Best_Phone) - log(PTS_Worst_Phone))`
    *   **Parameters:** See `scoring_constants.md` for values.

> **Example: Snapdragon 8 Gen 3**
> *   **Specs:** 1x X4 (3.3GHz), 5x A720 (3.2GHz), 2x A520 (2.3GHz).
> *   **CPS:** `(1*9) + (5*6) + (2*3)` = **45**
> *   **AES:** `45 / 8` = **5.625**
> *   **FSF:** `1 + (3.3 - Max_Freq_GHz_Worst_Phone)/(Max_Freq_GHz_Best_Phone - Max_Freq_GHz_Worst_Phone)` = `1 + (3.3 - 1.8)/2.0` = **1.75**
> *   **Raw:** `45 * 5.625 * 1.75` = **442.97**
> *   **Score:** `10 * (log(442.97)-log(PTS_Worst_Phone)) / (log(PTS_Best_Phone)-log(PTS_Worst_Phone))`
> *   `10 * (log(442.97)-log(20)) / (log(600)-log(20))` = `10 * (2.646 - 1.301) / (2.778 - 1.301)` ≈ **9.1/10**

### 🔹 3.2 CPU Architecture & Single-Core Efficiency
*Description:* Measures the responsiveness of the CPU for immediate tasks like app launching and UI navigation. This isolates architectural efficiency and single-thread speed, independent of total core count.
*   **Measurement:** Geekbench 6 Single-Core Score.
*   **Unit:** Points
*   **Significance:** Determines the "snappiness" of the UI and speed of light tasks.

#### Method A: Benchmark (Primary)
**Direct Benchmark Score**
This is the preferred method when a direct Geekbench 6 score is available. It provides the most accurate representation of real-world performance.
`Score = 10 * (log(Score) - log(GB6_Single_Worst_Phone)) / (log(GB6_Single_Best_Phone) - log(GB6_Single_Worst_Phone))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ GB6_Single_Best_Phone
*   **Min Score (0.0):** ≤ GB6_Single_Worst_Phone
> [!NOTE]
> **Why Logarithmic?** Single-core speed has a direct but diminishing impact on UI fluidity. Moving from 300 to 1000 points dramatically reduces UI stutters. Moving from 2000 to 2500 points yields millisecond gains that are harder to perceive.

#### Method B: Nearest Neighbor Interpolation (Secondary)
If the specific device has no benchmark, but we have data for other devices:
1.  **Identify Neighbors:** Find **3 Reference Phones** that have **BOTH** Geekbench scores and known specs. Select the ones with the closest **Theoretical Score** (calculated via Method C) to the target device.
2.  **Calculate Correction Ratio:**
    *   `Avg_Theoretical_Neighbors = (Theory_Neighbor1 + Theory_Neighbor2 + Theory_Neighbor3) / 3`
    *   `Ratio = Theoretical_Target / Avg_Theoretical_Neighbors`
3.  **Apply to Benchmark:**
    *   `Avg_Benchmark_Neighbors = (Bench_Neighbor1 + Bench_Neighbor2 + Bench_Neighbor3) / 3`
    *   `Estimated_Score = Ratio * Avg_Benchmark_Neighbors`

#### Method C: Theoretical Calculation (Tertiary)
Used as a standalone fallback or as the **Predictor** for Method B.

**Step 1: Core Architecture Score (CAS)**
*   *What is it?* The weight of the *single strongest core* in the system.
*   **Weights:** See **Section 3.1.1 CPU Core Architecture Reference** for authoritative core scores.

**Step 2: Frequency Scaling Factor (FSF)**
*   *What is it?* A multiplier for clock speed.
*   **Formula:** `1 + (Max_Freq_GHz - Max_Freq_GHz_Worst_Phone) / (Max_Freq_GHz_Best_Phone - Max_Freq_GHz_Worst_Phone)`
    *   *Range is 1-2.
    *   **Why FSF?** Single-core performance scales almost linearly with frequency for the same architecture. A 3.0GHz core is roughly 50% faster than a 2.0GHz core of the same type. FSF normalizes this between the worst and best phones in the dataset.

**Step 3: Calculate Final Score**
1.  **Raw Single-Thread (STRS - Single Thread Raw Score):** `CAS * FSF`
2.  **Final Score:** `10 * (log(STRS) - log(STRS_Worst_Phone)) / (log(STRS_Best_Phone) - log(STRS_Worst_Phone))`
    *   **Parameters:** See `scoring_constants.md` for values.

> **Example: Snapdragon 8 Gen 3**
> *   **Specs:** Prime Core is Cortex-X4 at 3.3GHz.
> *   **CAS:** Cortex-X4 = **9**
> *   **FSF:** `1 + (3.3 - 1.8) / (3.8 - 1.8)` = `1 + 1.5/2.0` = **1.75**
> *   **Raw:** `9 * 1.75` = **15.75**
> *   **Score:** `10 * (log(15.75) - log(STRS_Worst_Phone)) / (log(STRS_Best_Phone) - log(STRS_Worst_Phone))`
> *   `10 * (log(15.75) - log(9)) / (log(20) - log(9))` = `10 * (1.197 - 0.954) / (1.301 - 0.954)` = `10 * 0.700` ≈ **7.0/10**


### 🔹 3.3 GPU Performance (Graphics & Gaming)
*Description:* Measures the graphical processing power for gaming, rendering, and compute tasks. This score is a composite of raw architecture power, modern API support, and advanced feature capabilities.
*   **Measurement:** Architecture Generation + API Support + Ray Tracing.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for high-fidelity gaming, UI smoothness, and future-proofing.

#### 3.3.1 GPU Architecture Reference

**Master Scoring Table** (used across all GPU-related calculations)

This table provides the authoritative GPU architecture scores used throughout the scoring system, including:
- Section 3.3 GPU Performance (Base Architecture Score - Part 1)
- Battery Endurance Scoring (Battery efficiency - SoC component)

**Scoring Basis:** Based on GPU generation, compute units, and real-world graphics performance.

| GPU Model                    | Score  | Generation | Notes                          |
|------------------------------|--------|------------|--------------------------------|
| **Apple GPU (A17/A18)**      | **10** | 2023-2024  | Highest mobile GPU performance |
| **Immortalis-G720**          | **10** | 2023       | ARM flagship with ray tracing  |
| **Adreno 750**               | **9**  | 2023       | Snapdragon 8 Gen 3             |
| **Adreno 740**               | **9**  | 2022       | Snapdragon 8 Gen 2             |
| **Adreno 730**               | **8**  | 2021       | Snapdragon 8 Gen 1             |
| **Mali-G715**                | **8**  | 2022       | Dimensity 9000 series          |
| **Mali-G710**                | **7**  | 2021       | Dimensity 8000 series          |
| **Adreno 660**               | **7**  | 2020       | Snapdragon 888                 |
| **Adreno 642L**              | **6**  | 2021       | Snapdragon 778G                |
| **Mali-G610**                | **6**  | 2021       | Dimensity 1080                 |
| **Adreno 619**               | **4**  | 2019       | Snapdragon 750G                |
| **Mali-G68**                 | **4**  | 2020       | Dimensity 900                  |
| **Mali-G57**                 | **2**  | 2018       | Budget Dimensity/Exynos        |
| **Adreno 610**               | **2**  | 2019       | Snapdragon 665/680             |
| **Mali-G52**                 | **0**  | 2018       | Entry-level budget             |

> [!IMPORTANT]
> **Single Source of Truth:** This table is the master reference for all GPU scores. All other sections reference this table. Do not duplicate or modify scores elsewhere.

**Part 1: Base GPU Architecture Score (70%)**
*   *What is it?* The core raw performance potential based on the GPU generation and tier.
*   **Measurement:** GPU Model & Generation.
*   **Scoring:** See **Section 3.3.1 GPU Architecture Reference** for authoritative GPU scores.

**Part 2: API & Feature Support Modifier (20%)**
*   *What is it?* Support for modern graphics APIs that enable advanced visual effects and efficiency.
*   **Measurement:** Vulkan / OpenGL ES Version.
*   **Why this matters:** Modern APIs like Vulkan 1.3 allow developers to squeeze significantly more performance out of the hardware.
| Score    | Feature Support                | Description                    |
| :------- | :----------------------------- | :----------------------------- |
| **10.0** | **Vulkan 1.3 + Adv. Compute**  | State-of-the-art API support   |
| **8.0**  | **Vulkan 1.2**                 | Modern standard                |
| **6.0**  | **Vulkan 1.1**                 | Previous generation standard   |
| **4.0**  | **OpenGL ES 3.2 Only**         | Legacy Android graphics        |
| **2.0**  | **OpenGL ES 3.0**              | Very old                       |
| **0.0**  | **OpenGL ES ≤ 2.0**            | Obsolete                       |

**Part 3: Ray Tracing Capability Modifier (10%)**
*   *What is it?* Hardware acceleration for realistic lighting and reflections.
*   **Measurement:** Hardware Ray Tracing Support (Yes/No).
*   **Why this matters:** Indicates architectural modernity and readiness for next-gen mobile gaming.
| Score    | HW Ray Tracing | Description                    |
| :------- | :------------- | :----------------------------- |
| **10.0** | **Yes**        | Hardware-accelerated RT        |
| **0.0**  | **No**         | Software fallback or none      |

**Final Formula:** `Score = (0.7 * Architecture) + (0.2 * API) + (0.1 * Ray_Tracing)`

### 🔹 3.4 Efficiency (Process Node)
*Description:* Chip manufacturing technology. Smaller numbers (e.g., 3nm) mean the chip is more advanced, using less battery and generating less heat.
*   **Measurement:** Semiconductor process node size + Foundry.
*   **Unit:** Nanometers (nm)
*   **Significance:** Major factor in power efficiency and thermal performance.
*Formula:*
1.  **Calculate Base Score:** `10 * (log(20) - log(Node)) / (log(20) - log(3)) - 0.3`
    *   *Note:* The `- 0.3` ensures that a perfect 10.0 is only achievable with the TSMC modifier.
2.  **Apply Modifier:** `Final_Score = Base_Score + Foundry_Modifier` (Clamped 0-10)

*   **Max Score (10.0):** ≤ 3nm (TSMC Only)
*   **Min Score (0.0):** ≥ 20nm

**Foundry Efficiency Modifier:**
| Foundry           | Modifier | Why?                                                                        |
| :---------------- | :------- | :-------------------------------------------------------------------------- |
| **TSMC**          | **+0.3** | 20-30% better power efficiency at same node label (empirically proven).     |
| **Samsung**       | **0.0**  | Standard efficiency baseline.                                               |
| **SMIC / Others** | **-0.3** | Generally lower yield/efficiency than leaders.                              |

> [!NOTE]
> **Why Logarithmic & 20nm Cap?** Transistor density and power efficiency scale non-linearly. A shrink from 10nm to 5nm is a massive leap compared to 20nm to 15nm. We cap the scale at 20nm (extended from 16nm) because almost all relevant modern devices are ≤20nm, ensuring the score resolution is focused where it matters most.

> [!NOTE]
> **Unified Formula for Battery Scoring:** This exact formula is also used in the Battery Endurance Score model (Section 5.1, see [battery_scoring_model.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/battery_scoring_model.md) B.1.1) because process node efficiency directly impacts battery life. Foundry differences (TSMC vs Samsung) affect power consumption by 20-30%, so the foundry modifier must be included in battery life predictions.

### 🔹 3.5 Thermal Dissipation & Stability Index (TDSI)
*Description:* A composite index measuring the device's ability to sustain performance and shed heat. It combines the physical thermal capacity of the chassis with the sophistication of the internal cooling solution.
*   **Measurement:** Frame Material + Weight + Dimensions + Cooling System Type.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Prevents throttling, ensures sustained gaming performance, and maintains device longevity.

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

*Formula:* `Score = 10 * (Weight_g - Weight_Lightest_Phone) / (Weight_Heaviest_Phone - Weight_Lightest_Phone)` (Clamped 0-10)
*   **Max Score (10.0):** obtained for Heaviest Phone (Weight_Heaviest_Phone)
*   **Min Score (0.0):** obtained for Lightest Phone (Weight_Lightest_Phone)

**A3 — Heat Dissipation Surface Area (20% of Part A)**
*   **Measurement:** Physical dimensions from spec sheet.
*   **Unit:** mm²
*   **Significance:** Bigger phones dissipate heat better through larger surface area.

*Formula:* `Surface = Height_mm × Width_mm`  
*Formula:* `Score = 10 * (Surface - 6000) / (9000 - 6000)` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 9000 mm²
*   **Min Score (0.0):** ≤ 6000 mm²

**A4 — Device Thickness (15% of Part A)**
*   **Measurement:** Device thickness from manufacturer specifications.
*   **Unit:** Millimeters (mm)
*   **Significance:** Thicker phones have more internal volume for heat dissipation and airflow, allowing for better passive cooling and thermal capacity.

*Formula:* `Score = 10 * (Thickness_mm - 6) / (10 - 6)` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 10 mm
*   **Min Score (0.0):** ≤ 6 mm

> [!NOTE]
> **Data Structure Mapping:** `1_4_dimensions.thickness_mm`

**Part A Final Score:**  
`Part_A = (0.40 × A1) + (0.25 × A2) + (0.20 × A3) + (0.15 × A4)`

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

**Part C: Thermal Demand Compensation (Additive Bonus)**
*   *What is it?* A fairness adjustment that rewards devices with lower power consumption (lower thermal load).
*   **Measurement:** Based on **Section 3.1 SoC Performance Score**.
*   **Significance:** A low-power chip generates less heat, so it remains stable even with simple cooling. A high-power chip generates massive heat, requiring advanced cooling to prevent throttling.
*   **Formula:** `Bonus = (10 - SoC_Performance_Score) * 0.5`
    *   **Max Bonus (+5.0):** Low-end SoC (Score ~0) -> Needs minimal cooling.
    *   **Min Bonus (+0.0):** Flagship SoC (Score 10) -> Needs maximum cooling.

> [!NOTE]
> **Why this formula?** We use an **Additive Bonus** approach. The physical hardware (Parts A & B) sets the baseline stability capability. Then, we add points if the "engine" is small and easy to cool.
> *   **Budget Phone:** Passive cooling (Score 3) + Low Load Bonus (4) = **7.0 (Stable)**.
> *   **Gaming Phone:** Active Fan (Score 10) + High Load Bonus (0) = **10.0 (Stable)**.
> *   **Hot Flagship:** Passive cooling (Score 3) + High Load Bonus (0) = **3.0 (Unstable)**.
> This correctly predicts that a passively cooled flagship will throttle, while a passively cooled budget phone will not.

**Final Formula:**
1.  **Calculate Physical Capability:** `Physical_Score = (0.5 × Part_A) + (0.5 × Part_B)`
2.  **Calculate Load Compensation:** `Load_Bonus = (10 - Section_3_1_Score) * 0.5`
3.  **Final TDSI:** `TDSI = Physical_Score + Load_Bonus` (Clamped 0-10)


### 🔹 3.6 RAM Technology - Memory Technology Efficiency Index (MTEI)
*Description:* The type of memory used. Newer technology (LPDDR5X) allows for faster app switching and saves battery compared to older types.
*   **Measurement:** JEDEC standard specification.
*   **Unit:** Memory Generation
*   **Significance:** Affects data transfer speeds and power consumption.
| Score    | Technology    | Example Models                 |
| :------- | :------------ | :----------------------------- |
| **10.0** | **LPDDR5X**   | S24 Ultra, OnePlus 12          |
| **9.0**  | **LPDDR5**    | S22 Ultra, Pixel 7 Pro         |
| **7.0**  | **LPDDR4X**   | Galaxy A54, Nothing Phone (2a) |
| **5.0**  | **LPDDR4**    | Older Mid-range                |
| **3.0**  | **LPDDR3**    | Legacy Budget                  |
| **1.0**  | **LPDDR2**    | Obsolete                       |
| **0.0**  | **DDR2/DDR3** | Ancient                        |

### 🔹 3.7 RAM Capacity - Memory Capacity Index (MCI)
*Description:* Measures the amount of physical memory available for applications and background processes. More RAM improves multitasking, reduces app reloads, and increases system stability under load.
*   **Measurement:** Total physical RAM.
*   **Unit:** Gigabytes (GB)
*   **Significance:** Determines multitasking capability and app retention.
*Formula:* `Score = 10 * (log(GB) - log(2)) / (log(24) - log(2))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 24 GB
*   **Min Score (0.0):** ≤ 2 GB
> [!NOTE]
> **Why Logarithmic?** The utility of RAM diminishes as it increases. Going from 4GB to 8GB dramatically improves multitasking and system stability. However, going from 16GB to 24GB offers minimal tangible benefit for current mobile applications.

### 🔹 3.8 Storage Technology
*Description:* The speed of the internal drive. Faster storage means the phone boots up instantly, apps install quickly, and files copy fast.
*   **Measurement:** Sequential Read/Write speed capacity.
*   **Unit:** Storage Generation, internal storage only.
*   **Significance:** Affects boot time, app load time, and file transfer speed.
| Score    | Technology   | Example Models             |
| :------- | :----------- | :------------------------- |
| **10.0** | **UFS 4.0**  | S24 Ultra, Xiaomi 14       |
| **8.0**  | **UFS 3.1**  | Pixel 7, S21 Ultra         |
| **7.0**  | **UFS 3.0**  | OnePlus 8 Pro              |
| **6.0**  | **UFS 2.2**  | Redmi Note 13, Galaxy A34  |
| **5.0**  | **UFS 2.1**  | Older Mid-range            |
| **3.0**  | **eMMC 5.1** | Galaxy A05, Budget Tablets |
| **1.0**  | **eMMC 4.5** | Very old                   |
| **0.0**  | **eMMC≤4.0** | Obsolete                   |

### 🔹 3.9 Storage Capacity
*Description:* Internal space for your data. More storage means you can save more photos, videos, and games without deleting old ones.
*   **Measurement:** Total internal non-volatile memory.
*   **Unit:** Gigabytes (GB)
*   **Significance:** Determines capacity for apps, media, and files.
*Formula:* `Score = 10 * (log(GB) - log(16)) / (log(1024) - log(16))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 1024 GB (1 TB)
*   **Min Score (0.0):** ≤ 16 GB
> [!NOTE]
> **Why Logarithmic?** Similar to RAM, storage utility is non-linear. 64GB to 128GB is a critical upgrade that prevents "storage full" anxiety. 512GB to 1TB is a luxury for power users, with less impact on daily basic functionality.

### 🔹 3.10 Storage Expandability
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


## 🟣 4. Camera Systems

### A. Rear Camera — Photography

### 🔹 4.1 Main Sensor Size
*Description:* The size of the camera sensor. Larger sensors capture more light, resulting in much better low-light photos and natural background blur.
*   **Measurement:** Diagonal sensor size (Type 1/x").
*   **Unit:** Optical Format (Inches)
*   **Significance:** The most critical hardware factor for image quality (noise, dynamic range).
*Formula:* `Score = 10 * (log(Size_Inch) - log(0.25)) / (log(1.0) - log(0.25))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 1.0 inch
*   **Min Score (0.0):** ≤ 0.25 inch (1/4")
> [!NOTE]
> **Why Logarithmic?** Sensor area grows quadratically with diagonal size, but photographic benefits (dynamic range, noise) follow a diminishing return curve in mobile form factors. A 1-inch sensor is a massive leap over 1/2-inch, but further increases face optical constraints.

### 🔹 4.2 Main Camera Aperture
*Description:* The size of the lens opening. Wider apertures (lower f-number) let in more light for brighter night shots and create natural bokeh.
*   **Measurement:** Focal length / Entrance pupil diameter.
*   **Unit:** f-stop (f/number)
*   **Significance:** Determines light gathering and depth of field.
*Formula:* `Score = 10 - 10 * ((f_stop - 1.4) / (2.4 - 1.4))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ f/1.4
*   **Min Score (0.0):** ≥ f/2.4
> [!NOTE]
> This is a continuous linear scoring metric. Lower f-number is better (wider aperture).

### 🔹 4.3 Main Camera Resolution
*Description:* The maximum pixel count of the primary sensor. Higher resolution allows for more detailed cropping and sharper images in good light.
*   **Measurement:** Total effective pixel count.
*   **Unit:** Megapixels (MP)
*   **Significance:** Allows for digital zooming and fine detail capture.
*Formula:* `Score = 10 * (log(MP) - log(12)) / (log(200) - log(12))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 200 MP
*   **Min Score (0.0):** ≤ 12 MP
> [!NOTE]
> **Why Logarithmic?** Moving from 12MP to 50MP provides a significant jump in detail for cropping. However, moving from 100MP to 200MP offers diminishing returns due to lens diffraction limits and file size management.

### 🔹 4.4 Image Stabilization
*Description:* Hardware and software systems used to compensate for hand movement during image capture and video recording. Essential for sharp low-light photos and smooth video recording.
*   **Measurement:** Manufacturer camera specifications and teardown confirmation (where available).
*   **Unit:** Stabilization Mechanism Class
*   **Significance:** Determines the camera's ability to maintain image sharpness at longer exposure times and reduce motion blur in video.

| Score    | Stabilization Mechanism                    |
| :------- | :----------------------------------------- |
| **10.0** | **Multi-Axis Gimbal / Multi-Sensor Shift** |
| **9.0**  | **Sensor-Shift OIS**                       |
| **8.0**  | **Lens-Based OIS**                         |
| **5.0**  | **EIS Only**                               |
| **0.0**  | **None**                                   |

**OIS (Optical Image Stabilization)**: Physical movement of lens elements or sensor to counteract camera shake  
**EIS (Electronic Image Stabilization)**: Software-based stabilization using frame cropping and motion compensation algorithms

**Multi-Axis Gimbal / Multi-Sensor Shift**: Mechanical stabilization system with ≥2-axis sensor or lens movement explicitly disclosed  
**Sensor-Shift OIS**: Image sensor physically moves to compensate for motion  
**Lens-Based OIS**: Optical lens group physically moves to compensate for motion  
**EIS Only**: Stabilization performed purely by digital frame cropping and motion estimation  
**None**: No stabilization mechanism disclosed

### 🔹 4.5 Zoom Capability
*Description:* Optical zoom power. Allows you to take sharp, detailed photos of distant objects (like at a concert) without losing quality. Only true optical zoom is considered. Digital/crop zoom are excluded. 
*   **Measurement:** Focal length ratio relative to the main camera.
*   **Unit:** Optical Magnification (x)
*   **Significance:** Enables capturing distant subjects without quality loss.
*Formula:* `Score = 10 * (log(Zoom) - log(1)) / (log(10) - log(1))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 10x Optical
*   **Min Score (0.0):** 1x (No Zoom)
> [!NOTE]
> **Why Logarithmic?** The difference in reach between 1x and 3x is transformative for composition. The difference between 10x and 12x is much less significant in terms of framing capability.

### 🔹 4.6 Ultrawide Camera Capability (UCC)
*Description:* How capable the ultrawide camera is for landscapes, architecture, and group shots. This measures hardware potential, not image aesthetics.
*   **Measurement:** Presence, Field of View (FOV), and Sensor Size.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Determines the quality and breadth of wide-perspective photography.

**4.6.1 Ultrawide Presence (Binary Gate)**
*   *Why it matters:* No ultrawide means no wide-perspective photography.
| Score    | Configuration         | Notes               |
| :------- | :-------------------- | :------------------ |
| **10.0** | **Ultrawide present** | Any ultrawide lens. |
| **0.0**  | **No ultrawide**      | Main camera only.   |

**4.6.2 Ultrawide Field of View**
*   *Why it matters:* Wider FOV captures more of the scene; this is the primary purpose of an ultrawide lens.
*   **Measurement:** Manufacturer FOV spec (degrees).
*   *Formula:* `Score = 10 * (FOV - 100) / (130 - 100)` (Clamped 0-10)
    *   **10.0:** ≥ 130°
    *   **0.0:** ≤ 100°
> [!NOTE]
> **Why Linear?** Field of View is a direct geometric measurement where each degree adds roughly equal value to the composition. The difference between 100° and 110° is perceptually similar to the difference between 110° and 120° in terms of "wideness".

**4.6.3 Ultrawide Sensor Size**
*   *Why it matters:* Larger sensors perform better in low light and have better dynamic range.
*   **Measurement:** Optical format (e.g., 1/2.0").
*   *Formula:* `Score = 10 * (log(Size) - log(0.25)) / (log(0.5) - log(0.25))` (Clamped 0-10)
    *   **10.0:** ≥ 1/2"
    *   **0.0:** ≤ 1/4"
> [!NOTE]
> **Why Logarithmic?** Sensor area grows quadratically with diagonal size, but photographic benefits (dynamic range, noise) follow a diminishing return curve. Moving from a tiny 1/4" sensor to a 1/2.5" sensor is a massive leap in quality, while moving from 1/2" to 1/1.5" offers smaller relative gains for an ultrawide module.

**Final Formula:**
*   If Presence = 1: `UCC = 0`
*   If Presence = 10: `UCC = (0.6 * FOV_Score) + (0.4 * Sensor_Score)`

### 🔹 4.7 Macro Capability & Close-Focus Performance (MCFP)
*Description:* The ability to focus on very close subjects. Prioritizes Autofocus-enabled ultrawides over cheap dedicated lenses.
*   **Measurement:** Focus type, Minimum Focus Distance, and Dedicated Lens specs.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for macro photography (flowers, insects, textures).

**4.7.1 Autofocus on Ultrawide**
*   *Why it matters:* Autofocus (AF) allows for close focus and subject tracking, enabling "real" macro mode.
| Score  | Focus Type                     |
| :----- | :----------------------------- |
| **10** | **Ultrawide Autofocus**        |
| **6**  | **Ultrawide with Fixed focus** |
| **0**  | **No macro-capable lens**      |

**4.7.2 Minimum Focus Distance**
*   *Why it matters:* The physical limit of how close you can get.
*   **Measurement:** Minimum focus distance (cm).
*   *Formula:* `Score = 10 - 10 * ((Distance - 1.5) / (10 - 1.5))` (Clamped 0-10)
    *   **10.0:** ≤ 1.5 cm
    *   **0.0:** ≥ 10 cm
> [!NOTE]
> **Why Linear?** In the macro range (1.5cm - 10cm), every centimeter closer allows for significantly more magnification. While magnification itself is non-linear, a linear scoring penalty for every centimeter lost is a fair and intuitive way to grade the "closeness" capability.

**4.7.3 Dedicated Macro Lens (Penalty-aware)**
*   *Why it matters:* Dedicated lenses can be useful but are often low-quality gimmicks. We cap the score at 6.0 to ensure they never outperform a high-quality Autofocus Ultrawide (Score 10).
*   **Measurement:** Sensor Resolution (MP).
*   *Formula:* `Score = clamp(MP, 0, 6)`
    *   **Max Score (6.0):** ≥ 6 MP (Decent utility)
    *   **Min Score (0.0):** 0 MP (None)
> [!NOTE]
> **Why Linear?** The useful range for dedicated macro lenses is narrow (typically 2MP to 5MP). A simple linear progression (`MP`) accurately maps the hardware capability: 0MP is useless (0), 2MP is weak (2), and 5MP is decent (5). This avoids overvaluing low-res "gimmick" sensors.

**Final Formula:**
*   `Ultrawide_Path = (0.4 * Score_4.7.1) + (0.6 * Score_4.7.2)`
*   `Dedicated_Path = Score_4.7.3`
*   `MCFP Score = Max(Ultrawide_Path, Dedicated_Path)`

### B. Rear Camera — Video Capture & Production

### 🔹 4.8 Rear Video Resolution
*Description:* Maximum spatial resolution supported for rear-camera video recording.
*   **Measurement:** Maximum supported rear video resolution.
*   **Unit:** Resolution Tier
*   **Significance:** Higher resolution allows greater detail, cropping flexibility, and higher-quality downscaling.
| Score  | Max Rear Video Resolution |
| :----- | :------------------------ |
| **10** | **≥ 4K**                  |
| **6**  | **1080p**                 |
| **3**  | **720p**                  |
| **0**  | **≤ 480p**                |

### 🔹 4.9 Rear Video Frame Rate
*Description:* Maximum frame rate supported at the highest commonly used resolution (≥1080p).
*   **Measurement:** Maximum FPS.
*   **Unit:** Frames per second (FPS)
*   **Significance:** Higher FPS (Frames Per Second) enables smoother motion and better motion clarity.
*Formula:* `Score = 10 * (log(FPS) - log(5)) / (log(120) - log(5))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 120 FPS
*   **Min Score (0.0):** ≤ 5 FPS
> [!NOTE]
> **Why Logarithmic?** The perception of smoothness is non-linear. The jump from 30fps to 60fps is dramatic (doubling smoothness), while 60fps to 120fps is noticeable but less transformative for standard video consumption.

### 🔹 4.10 Video Color & Dynamic Range
*Description:* Ability to capture wide dynamic range and rich color information in video.
*   **Measurement:** Supported HDR standards and bit depth.
*   **Unit:** HDR Capability Tier
*   **Significance:** HDR (High Dynamic Range) video preserves highlights and shadows and improves realism and grading headroom.

| Score    | Video HDR Capability                   |
| :------- | :------------------------------------- |
| **10.0** | **Dolby Vision or HDR10+ (10-bit)**    |
| **8.0**  | **HDR10 / HLG**                        |
| **6.0**  | **Extended SDR (flat / log-like SDR)** |
| **4.0**  | **Standard SDR**                       |
| **0.0**  | **No HDR support**                     |

**Definitions:**
*   **Dolby Vision:** A proprietary dynamic metadata format. It optimizes brightness, contrast, and color on a *scene-by-scene* or even *frame-by-frame* basis, ensuring the best possible picture quality for every moment of the video. It requires 10-bit or 12-bit color depth.
*   **HDR10+:** An open-standard dynamic metadata format similar to Dolby Vision. It also adjusts brightness and tone mapping scene-by-scene, offering a significant improvement over static HDR10.
*   **HDR10:** The baseline static metadata format. It sets a *single* brightness levels for the entire video file. If the movie has a very bright scene and a very dark scene, HDR10 must compromise between them, whereas dynamic formats optimize for both individually.
*   **HLG (Hybrid Log-Gamma):** A broadcast-friendly HDR standard designed to be backward compatible with SDR displays. slightly less capable than HDR10/Dolby Vision in absolute dynamic range but highly convenient.
*   **SDR (Standard Dynamic Range):** The traditional video standard (Rec.709 color space). It has limited brightness and color volume, leading to blown-out highlights (white skies) or crushed shadows in high-contrast scenes.

> [!NOTE]
> **Why is Dynamic Metadata (Score 10) better?**
> Dynamic formats (Dolby Vision, HDR10+) tell the display exactly how to render *each specific scene*. Static formats (HDR10) force the display to pick one average setting for the whole movie, which often makes dark scenes look too dark or bright scenes look washed out.

### 🔹 4.11 Video Encoding & Professional Recording
*Description:* Support for professional codecs and recording profiles enabling advanced post-production. This is a composite score evaluating codec quality, color profile support, and bit depth independently.
*   **Measurement:** Supported codecs, color profiles, and bit depth.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Professional codecs preserve detail, reduce compression artifacts, and allow color grading.

**Structure:** `Score = (0.40 × PCS) + (0.35 × LCPS) + (0.25 × CBD)`

#### 4.11.1 Professional Codec Support (PCS) — 40%
*What it measures:* Whether the phone can record in a mezzanine or RAW-class format designed for post-production, not delivery.
*   **Measurement:** Manufacturer specs, camera API codec list.
*   **Why it matters:** Mezzanine codecs (ProRes, CinemaDNG) preserve maximum image quality with minimal compression, enabling professional color grading and VFX work.

| Condition                                                                     | Score    |
| :---------------------------------------------------------------------------- | :------- |
| **Supports ProRes / CinemaDNG / ProRes RAW / equivalent mezzanine or RAW**    | **10.0** |
| **Does not**                                                                  | **0.0**  |

#### 4.11.2 Log Color Profile Support (LCPS) — 35%
*What it measures:* Whether the phone supports a logarithmic gamma curve, preserving dynamic range for color grading.
*   **Measurement:** Camera feature list, video mode specs.
*   **Why it matters:** Log profiles (e.g., S-Log, V-Log, HLG) flatten the image's contrast curve, capturing more highlight and shadow detail. This gives editors significantly more flexibility to adjust exposure and color in post-production without clipping or banding.

| Condition                         | Score    |
| :-------------------------------- | :------- |
| **Log profile available**         | **10.0** |
| **No log profile**                | **0.0**  |

#### 4.11.3 Color Bit Depth (CBD) — 25%
*What it measures:* How much color information is stored per channel in video recording.
*   **Measurement:** Codec specs, camera API output formats.
*   **Why it matters:** 10-bit color provides 1024 shades per channel (vs 256 in 8-bit), dramatically reducing banding in gradients (like skies) and enabling smoother color grading transitions.

| Bit Depth           | Score    |
| :------------------ | :------- |
| **10-bit or higher**| **10.0** |
| **8-bit only**      | **0.0**  |

**Final Formula:** `Score = (0.40 × PCS) + (0.35 × LCPS) + (0.25 × CBD)`

### 🔹 4.12 High Frame Rate (Slow Motion)
*Description:* Ability to capture video at very high frame rates for slow-motion playback.
*   **Measurement:** Maximum slow-motion FPS and resolution.
*   **Unit:** FPS @ Resolution (MP/s)
*   **Significance:** Enables creative effects and analysis of fast motion.
*Formula:* `Score = 10 * (log(MP_s) - log(32)) / (log(1000) - log(32))` (Clamped 0-10)
    *   `MP_s = Resolution_MP * FPS`
*   **Max Score (10.0):** ≥ 1000 MP/s (e.g., 4K @ 120fps)
*   **Min Score (0.0):** ≤ 32 MP/s (e.g., 720p @ 30fps)
> [!NOTE]
> **Why Logarithmic?** Slow motion quality depends on both resolution and speed. A logarithmic scale on total pixels-per-second (MP/s) fairly balances high-res/low-fps against low-res/high-fps modes, rewarding the total data throughput capability.

### C. Front Camera System (Selfie)

### 🔹 4.13 Front Camera Sensor Resolution
*Description:* Spatial resolution of the front-facing camera.
*   **Measurement:** Front camera megapixel count.
*   **Unit:** Megapixels (MP)
*   **Significance:** Determines selfie detail and cropping flexibility.
*Formula:* `Score = 10 * (log(MP) - log(5)) / (log(32) - log(5))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 32 MP
*   **Min Score (0.0):** ≤ 5 MP
> [!NOTE]
> **Why Logarithmic?** Selfie detail benefits diminish rapidly after a certain point. 32MP is sufficient for high-quality prints; beyond that, sensor size matters more than pixel count.

### 🔹 4.14 Front Camera Focus System
*Description:* Ability of the front-facing camera to maintain sharp focus across different subject distances.
*   **Measurement:** Focus mechanism and optical configuration.
*   **Unit:** Focus System Tier
*   **Significance:** Autofocus ensures sharp selfies and vlogs regardless of arm length or group distance.

| Score    | Focus System Tier                         | Objective Criteria                                   |
| :------- | :---------------------------------------- | :--------------------------------------------------- |
| **10.0** | **Autofocus (PDAF / Dual Pixel / Laser)** | Any active AF mechanism                              |
| **6.0**  | **Fixed Focus (Modern Wide-DOF)**         | Fixed focus AND (Aperture ≥ f/2.0 OR Sensor ≤ 1/3")  |
| **3.0**  | **Fixed Focus (Legacy Narrow-DOF)**       | Fixed focus AND (Aperture < f/2.0 AND Sensor > 1/3") |
| **0.0**  | **No Front Camera**                       | Feature phone                                        |

> [!NOTE]
> **Why this distinction?** Fixed-focus cameras rely on depth of field (DOF). Older or poorly designed selfie cameras with large sensors and fast apertures (low f-numbers) produce shallow DOF, causing frequent misfocus. Modern designs either add AF or intentionally limit DOF to maintain usability.

### 🔹 4.15 Front Camera Video Performance
*Description:* Maximum video capture capability of the front-facing camera, quantifying resolution, frame rate, and dynamic range.
*   **Measurement:** Max resolution, FPS, and HDR capability.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for vlogging, video calls, and content creation.
*Formula:* `Score = (0.4 * ResScore) + (0.35 * FPSScore) + (0.25 * DRScore)`

**4.15.1 Video Resolution Score**
*What it measures:* The maximum spatial resolution (pixel count) the front camera can record.
*   **Measurement:** Maximum supported front video resolution (long edge in pixels).
*   **Why it matters:** Higher resolution provides more detail for cropping, digital stabilization, and future-proofing. 4K allows for 1080p crops without quality loss, while 720p limits editing flexibility.
*   *Formula:* `ResScore = 10 * (log(px) - log(1280)) / (log(3840) - log(1280))` (Clamped 0-10)
    *   **Variables:**
        *   `px` = Long edge resolution in pixels (e.g., 3840 for 4K, 1920 for 1080p, 1280 for 720p)
    *   **Max Score (10.0):** 4K (3840px long edge)
    *   **Min Score (0.0):** 720p (1280px long edge)
> [!NOTE]
> **Why Logarithmic?** The perceptual benefit of resolution follows a diminishing return curve. The jump from 720p to 1080p is dramatic for clarity, but 1080p to 4K is less noticeable on small screens, though valuable for cropping and editing.

**4.15.2 Video Frame Rate Score**
*What it measures:* The maximum frame rate the front camera can sustain at its highest resolution.
*   **Measurement:** Maximum FPS at the highest supported resolution.
*   **Why it matters:** Higher frame rates (60fps) create smoother motion for vlogs and video calls, reducing motion blur and improving the perception of fluidity. 24fps is cinematic but can appear choppy for fast movement.
*   *Formula:* `FPSScore = 10 * (log(FPS) - log(24)) / (log(60) - log(24))` (Clamped 0-10)
    *   **Variables:**
        *   `FPS` = Maximum sustained frame rate (e.g., 60, 30, 24)
    *   **Max Score (10.0):** 60 FPS
    *   **Min Score (0.0):** 24 FPS
> [!NOTE]
> **Why Logarithmic?** Frame rate perception is non-linear. The difference between 24fps and 30fps is barely noticeable, but 30fps to 60fps is a significant smoothness upgrade for motion-heavy content.

**4.15.3 Dynamic Range & Codec Score (DRScore)**

*Description:* Measures the front camera’s support for high dynamic range and professional video recording profiles. Focuses on officially supported video standards, not subjective video quality.

**Measurement:** Manufacturer camera specs and system camera settings
**Unit:** Video Profile Tier (0–10)
**Significance:** Determines highlight retention, color grading potential, and post-processing flexibility for selfie video.

| Score    | Video Capability                                                                                  |
| :------- | :-------------------------------------------------------------------------------------------------|
| **10.0** | **Pro video format OR Log profile (Apple ProRes, Android LOG, or equivalent flat gamma profile)** |
| **9.0**  | **Dolby Vision HDR recording**                                                                    |
| **7.0**  | **HDR10 or HDR10+ recording**                                                                     |
| **4.0**  | **HLG HDR or manufacturer-labeled “HDR video”**                                                   |
| **1.0**  | **SDR only (8-bit, Rec.709)**                                                                     |
| **0.0**  | **No front camera**                                                                               |


### D. Computational Photography & AI

### 🔹 4.16 Multi-Frame Computational Photography (MFCP)
*Description:* Measures whether the camera system performs automatic multi-frame capture and stacking for still photos to improve noise, dynamic range, and sharpness.
*   **Measurement:** Official camera documentation and published feature lists.
*   **Unit:** Processing Tier (0–10)
*   **Significance:** Multi-frame pipelines significantly improve low-light performance and highlight retention in still images without relying on hardware changes.

**Why it matters:** Multi-frame processing captures multiple exposures in rapid succession and computationally merges them. This reduces noise (by averaging), expands dynamic range (by combining different exposures), and improves sharpness (by aligning and selecting the sharpest pixels). Always-on systems apply this benefit to every photo automatically, while conditional systems require manual mode activation.

| Score    | Publicly Documented Capability                                                                    |
| :------- | :------------------------------------------------------------------------------------------------ |
| **10.0** | **Always-on multi-frame HDR + Night stacking** (automatic frame fusion in daylight and low light) |
| **6.0**  | **Conditional multi-frame processing** (HDR or Night mode must be manually enabled)               |
| **0.0**  | **Single-frame capture only**                                                                     |

### 🔹 4.17 Semantic / Scene AI Processing
*Description:* Ability of the camera software to understand and segment scenes and subjects.
*   **Measurement:** Presence of semantic segmentation features.
*   **Unit:** AI Capability Tier
*   **Significance:** Enables better portraits, sky processing, skin tones, and subject isolation.
| Score    | Semantic AI                                          |
| :------- | :--------------------------------------------------- |
| **10.0** | **Full semantic segmentation (faces, sky, objects)** |
| **6.0**  | **Basic portrait / scene detection**                 |
| **0.0**  | **None**                                             |

### 🔹 4.18 Generative & Post-Capture AI Tools
*Description:* Ability to modify images after capture using AI.
*   **Measurement:** Presence of generative AI tools.
*   **Unit:** Feature Tier
*   **Significance:** Extends usability and creative flexibility beyond capture time.
| Score    | AI Editing Tools                        |
| :------- | :-------------------------------------- |
| **10.0** | **Generative erase / expand / relight** |
| **6.0**  | **Non-generative AI edits**             |
| **0.0**  | **None**                                |


## 🟣 5. Battery & Charging

### 🔹 5.1 Battery Endurance Score

> [!IMPORTANT]
> **Battery scoring uses a dedicated comprehensive model.**
> 
> See [battery_scoring_model.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/battery_scoring_model.md) for the complete methodology.

**Summary:** Battery endurance is scored using a sophisticated **Benchmark-First Approach with Predictive Interpolation** (Model v3.2) that:

1. **Prioritizes Real-World Data:** Uses actual battery test results from GSMArena and PhoneArena when available
2. **Technical Prediction:** Calculates a predicted score based on:
   - **Energy (45%):** Battery capacity in Watt-hours (accounting for voltage)
   - **Hardware Efficiency (35%):** SoC process node, display technology, connectivity, thermal management, charging stress
   - **Software Optimization (20%):** OS efficiency and bloatware impact
3. **Intelligent Interpolation:** For devices without benchmark data, finds "nearest neighbor" phones with similar specs and interpolates their real-world performance
*   **Measurement:** Standardized battery life tests (or predictive model).
*   **Unit:** Benchmark Score
*   **Significance:** Determines how long the phone lasts on a single charge under real-world usage.

### 🔹 5.2 Wired Charging Speed
*Description:* Charging speed with a cable. Higher wattage means you spend less time tethered to a wall outlet.
*   **Measurement:** Peak power input via wired connection.
*   **Unit:** Watts (W)
*   **Significance:** Reduces downtime when battery is low.
*Formula:* `Score = 10 * (log(Watts) - log(5)) / (log(120) - log(5))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 120W
*   **Min Score (0.0):** ≤ 5W
> [!NOTE]
> **Why Logarithmic?** Time-to-charge follows a diminishing return curve. Upgrading from 10W to 60W saves massive amounts of time (hours). Upgrading from 120W to 240W saves only minutes, as the battery chemistry limits sustained peak speeds.

### 🔹 5.3 Wireless Charging Speed
*Description:* Charging speed without cables. Convenient for topping up battery by simply placing the phone on a pad.
*   **Measurement:** Peak power input via wireless coil.
*   **Unit:** Watts (W)
*   **Significance:** Convenience and ease of topping up.
*Formula:* `Score = 10 * (log(Watts) - log(7.5)) / (log(50) - log(7.5))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 50W
*   **Min Score (0.0):** ≤ 7.5W
> [!NOTE]
> **Why Logarithmic?** Similar to wired charging, the convenience gain from 5W to 15W is significant (usable charging vs trickle). Beyond 50W, thermal limits often throttle speeds, reducing the real-world time savings.

### 🔹 5.4 Wireless Reverse Charging
*Description:* Ability to charge other devices (like earbuds or watches) wirelessly by placing them on the back of the phone.
*   **Measurement:** Peak power output via wireless coil.
*   **Unit:** Watts (W)
*   **Significance:** Convenient for emergency top-ups of accessories on the go.
*Formula:* `Score = 10 * (Watts / 10)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ 10W (Fast Reverse)
    *   **Min Score (0.0):** 0W (None)
> [!NOTE]
> **Why Linear?** The range of reverse wireless charging is narrow (typically 4.5W to 10W). A linear scale accurately reflects that 10W is roughly twice as fast/useful as 4.5W for small accessory batteries.

### 🔹 5.5 Wired Reverse Charging
*Description:* Ability to use the phone as a power bank to charge other devices via a USB-C cable.
*   **Measurement:** Peak power output via USB-C port.
*   **Unit:** Watts (W)
*   **Significance:** Useful for sharing power with other phones or charging larger accessories.
*Formula:* `Score = 10 * (Watts / 10)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ 10W
    *   **Min Score (0.0):** 0W (None)
> [!NOTE]
> **Why Linear?** Similar to wireless reverse, the output range is small (4.5W to ~10W). Linear scaling provides a fair and intuitive distribution of scores based on raw power output.

### 🔹 5.6 Charger Adequacy (In-Box Performance Match)
*Description:* What comes in the package. A high-speed charger included saves you money and ensures you get the fastest charging speeds right away.
*   **Measurement:** Ratio of Included Charger Wattage to Maximum Supported Wired Charging Wattage.
*   **Unit:** Efficiency Ratio (0.0 - 1.0)
*   **Significance:** Determines if the user gets the device's full performance out of the box without extra purchases.
*Formula:* `Score = 10 * (Included_Watts / Max_Wired_Watts)` (Clamped 0-10)
    *   **Max Score (10.0):** Included Charger ≥ Max Device Speed (Ratio ≥ 1.0)
    *   **Min Score (0.0):** No Charger (0W)
> [!NOTE]
> **Why Ratio?** A "good" unboxing experience means not needing to buy accessories. If a phone supports 120W but comes with a 60W charger, the user is missing out on half the advertised performance, hence a lower score. If a 20W phone comes with a 20W charger, the experience is complete (10/10).


## 🟣 6. Software & Longevity

### 🔹 6.1 Support Longevity
*Description:* How long the manufacturer promises updates. Longer support means your phone stays secure and gets new features for years.
*   **Measurement:** Manufacturer update policy commitment.
*   **Unit:** Years
*   **Significance:** Device longevity, security, and resale value.
*Formula:* `Score = 10 * (log(Years) - log(1)) / (log(7) - log(1))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 7 Years
*   **Min Score (0.0):** ≤ 1 Year
> [!NOTE]
> **Why Logarithmic?** The value of support diminishes over time as hardware ages. The difference between 1 and 3 years is critical for security. The difference between 5 and 7 years is less impactful as many users upgrade before then.

### 🔹 6.2 AI User Capability Index (AUCI)
*Description:* Evaluates how much practical AI capability a user actually gets on a smartphone today. Focuses strictly on user-visible outcomes, not marketing claims or internal architecture.
*   **Measurement:** Manufacturer feature lists, OS documentation, and verified reviews.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Determines the breadth and independence of AI features available to the user.

**Guiding Question:** *"What useful AI features does the user have access to, and how independently can the phone run them?"*

**Structure:** `AUCI = 0.45 × AFB + 0.55 × AEI`

#### 6.2.1 AI Feature Breadth (AFB)
*Description:* Measures how many distinct, meaningful user activity domains are enhanced by AI features. Each domain is counted once.
*   **AI Domains Considered:**
    1.  **Text & Writing:** Rewrite, summarize, proofread.
    2.  **Image Editing:** Object removal, generative fill.
    3.  **Voice & Translation:** Live translation, transcription.
    4.  **System Intelligence:** Contextual search, smart actions.
    5.  **Productivity / OS AI:** Notes, reminders, AI workflows.

*   **Scoring Formula:** `AFB = 10 × (AI_Domains_Enabled / 5)`

| Domains Present | AFB Score |
| :-------------- | :-------- |
| **5**           | **10.0**  |
| **4**           | **8.0**   |
| **3**           | **6.0**   |
| **2**           | **4.0**   |
| **1**           | **2.0**   |
| **0**           | **0.0**   |

#### 6.2.2 AI Execution Independence (AEI)
*Description:* Measures how independently AI features can run on the device, without relying on cloud services. This impacts latency, privacy, and offline usability.

| Score    | Execution Model                | Description                                         |
| :------- | :----------------------------- | :-------------------------------------------------- |
| **10.0** | **Fully On-Device**            | Core AI features run locally without internet.      |
| **8.0**  | **Hybrid (On-Device + Cloud)** | Local inference with cloud fallback.                |
| **5.0**  | **Cloud-First**                | AI requires internet connection.                    |
| **3.0**  | **Cloud + Account Required**   | Login and online dependency.                        |
| **0.0**  | **No Meaningful AI**           | Basic assistant only / no AI features.              |

**Final Formula:** `AUCI = (0.45 × AFB) + (0.55 × AEI)`


### 🔹 6.3 System Cleanliness & Control (SCC)
*Description:* Evaluates how much control the user has over their system environment, focusing on unwanted software, ads, and the ability to remove preinstalled content.
*   **Measurement:** Count of preinstalled apps, removability status, and presence of system ads.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Affects user experience, privacy, and storage.

**Structure:** `SCC = 0.4 × PAL + 0.35 × RDC + 0.25 × SAP`

#### 6.3.1 Preinstalled App Load (PAL)
*Description:* Quantifies the number of non-essential third-party apps preinstalled at first boot.

Third-party preinstalled app =
Any application not required for core OS functionality, including:
- partner apps (Facebook, TikTok, Booking, etc.)
- app stores other than the platform default
- OEM-branded commercial services (themes store, shopping, cloud upsells)

*   **Measurement:** Count of third-party apps (excluding core OS services and hardware utilities).
*   **Formula:** `PAL = clamp(10 - 2/3 × Third_Party_Apps, 0, 10)`

| Third-Party Apps | PAL Score |
| :--------------- | :-------- |
| **0**            | **10.0**  |
| **3**            | **8.0**   |
| **6**            | **6.0**   |
| **9**            | **4.0**   |
| **12**           | **2.0**   |
| **≥15**          | **0.0**   |

#### 6.3.2 Removability & Disable Control (RDC)
*Description:* Measures the user's ability to remove or disable the preinstalled apps counted in PAL.
*   **Formula:** `RDC = 10 × (Removable + 0.5 × Disableable) / Total_Preinstalled`
*   **Special Case:** If `Total_Preinstalled = 0`, then `RDC = 10`.

| Scenario                          | RDC Score |
| :-------------------------------- | :-------- |
| **All removable**                 | **10.0**  |
| **Half removable, half disable**  | **7.5**   |
| **Mostly disable-only**           | **~5.0**  |
| **Mostly locked**                 | **~2.0**  |
| **No control**                    | **0.0**   |

#### 6.3.3 System Ads & Promotions (SAP)
*Description:* Evaluates the presence of ads in system apps, notifications, and UI.

| Condition                                        | SAP Score |
| :----------------------------------------------- | :-------- |
| **No system ads, no promotions**                 | **10.0**  |
| **Ads present but all disabled by one toggle**   | **7.0**   |
| **Ads disabled only by multiple per-app toggles**| **4.0**   |
| **Ads present and cannot be fully disabled**     | **1.0**   |
| **Persistent / recurring ads**                   | **0.0**   |

**Final Formula:** `SCC = (0.4 × PAL) + (0.35 × RDC) + (0.25 × SAP)`


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
*Description:* SIM card options. Dual SIM lets you have two numbers (e.g., work/personal) or use a local SIM when traveling.
*   **Measurement:** Physical tray and eSIM support check.
*   **Unit:** Slot Configuration
*   **Significance:** Flexibility for multiple carriers and travel.
| Score    | Configuration                     | 
| :------- | :-------------------------------- | 
| **10.0** | **Dual eSIM + iSIM + Nano**       | 
| **9.0**  | **Dual SIM (Nano + eSIM)**        | 
| **8.0**  | **Dual Nano-SIM**                 | 
| **6.0**  | **Single Nano-SIM**               | 
| **4.0**  | **eSIM only (region-restricted)** | 
| **0.0**  | **No SIM (Wi-Fi Only)**           | 

### 🔹 7.3 Wi-Fi Standard
*Description:* Wi-Fi technology. Newer standards (Wi-Fi 7/6E) provide faster, more stable internet, especially in crowded homes.
*   **Measurement:** Supported Wi-Fi protocols.
*   **Unit:** Standard (Generation)
*   **Significance:** Local network speed and congestion management.
| Score    | Standard     | 
| :------- | :----------- | 
| **10.0** | **Wi-Fi 7**  | 
| **9.0**  | **Wi-Fi 6E** | 
| **8.0**  | **Wi-Fi 6**  | 
| **6.0**  | **Wi-Fi 5**  | 
| **3.0**  | **Wi-Fi 4**  | 
| **0.0**  | **Wi-Fi≤3**  |

### 🔹 7.4 Bluetooth & Audio Codecs
*Description:* Bluetooth quality. Newer versions offer more stable connections to headphones, and better codecs mean higher quality music.
*   **Measurement:** Supported Bluetooth profile and codecs.
*   **Unit:** Version / Codecs
*   **Significance:** Audio quality and connection stability with accessories.
| Score    | Version / Codecs                     | Example Models               |
| :------- | :----------------------------------- | :--------------------------- |
| **10.0** | **BT 5.4 + Lossless (aptX/LHDC)**    | Snapdragon 8 Gen 3 Flagships |
| **9.0**  | **BT 5.3 + High-res (LDAC/aptX HD)** | S23 Ultra, Pixel 7           |
| **8.0**  | **BT 5.3 + AAC/SBC only**            | iPhone 15 (No LDAC)          |
| **6.0**  | **BT 5.0-5.2**                       | Older Mid-range              |
| **4.0**  | **BT 4.2**                           | Budget / Legacy              |
| **0.0**  | **< BT 4.0**                         | Obsolete                     |

### 🔹 7.5 NFC & Ultra-Wideband (UWB)
*Description:* Contactless features. Near-Field Communication (NFC) allows for phone payments, while UWB lets you precisely find lost items (like trackers).
*   **Measurement:** Hardware check.
*   **Unit:** Feature Presence
*   **Significance:** Mobile payments and precision location finding.
| Score    | Features                  | Example Models            |
| :------- | :------------------------ | :------------------------ |
| **10.0** | **NFC + UWB (Precision)** | iPhone 15 Pro, S24 Ultra  |
| **6.0**  | **NFC Only**              | Pixel 8, Galaxy A55       |
| **0.0**  | **No NFC**                | Budget (Region dependent) |

### 🔹 7.6 Biometrics
*Description:* Unlocking methods. Secure face/fingerprint unlock is faster and safer than typing a PIN every time.
*   **Measurement:** Hardware check (Sensor type).
*   **Unit:** Technology Type
*   **Significance:** Security and convenience of unlocking.
| Score    | Technology                                   | Example Models          |
| :------- | :------------------------------------------- | :---------------------- |
| **10.0** | **3D Face ID + Ultrasonic Fingerprint (FP)** | (Hypothetical Ultimate) |
| **9.0**  | **Ultrasonic FP**                            | S24 Ultra               |
| **8.0**  | **3D Face Unlock (Secure)**                  | iPhone 15, Pixel 4      |
| **7.0**  | **Optical Under-Display FP**                 | Pixel 8, OnePlus 12     |
| **6.0**  | **Side-Mounted Capacitive FP**               | Z Fold 5, Galaxy A55    |
| **5.0**  | **Rear Capacitive FP**                       | Pixel 5, Older Androids |
| **3.0**  | **2D Face**                                  | Budget phones           |
| **0.0**  | **No Biometrics**                            | Entry Level / PIN only  |

### 🔹 7.7 Sensors
*Description:* The breadth of hardware sensors in the phone that enable accurate navigation, motion tracking, environmental awareness, and AR/VR features.
*   **Measurement:** Count of sensor categories present.
*   **Unit:** Normalized Score (0-10)
*   **Significance:** Critical for navigation, fitness tracking, AR apps, and basic phone functionality.

**Scoring Logic:**
Each phone can support up to 6 core sensor categories.
*Formula:* `Score = round(10 * (Detected_Categories / 6), 1)`

| Sensor Capability                | Points |
| :--------------------------------| :----- |
| **Advanced Depth / ToF / LiDAR** |    1   |
| **Barometer**                    |    1   |
| **Magnetometer / Compass**       |    1   |
| **Gyroscope**                    |    1   |
| **Accelerometer**                |    1   |
| **Proximity & Ambient Light**    |    1   |

**Sensor Descriptions:**
*   **Advanced Depth / ToF / LiDAR:** Dedicated depth sensor improves AR depth perception and enhances portrait effects.
*   **Barometer:** Measures barometric pressure; improves elevation data in maps and fitness apps.
*   **Magnetometer / Compass:** Detects magnetic fields so the phone knows heading relative to Earth’s magnetic north.
*   **Gyroscope:** Measures rotational motion; critical for AR/VR apps, stable navigation, and immersive motion tracking.
*   **Accelerometer:** Measures linear motion for step counting, tilt, and orientation changes.
*   **Proximity & Ambient Light:** Proximity stops accidental touches during calls; ambient light adjusts screen brightness.

**Scoring Table:**
| Completeness |  Score   | Example Interpretation       |
| :----------- | :------- | :--------------------------- |
|  **6 / 6**   | **10.0** | Full sensor suite (flagship) |
|  **5 / 6**   | **8.3**  | All but advanced depth       |
|  **4 / 6**   | **6.7**  | Standard modern sensors      |
|  **3 / 6**   | **5.0**  | Basic navigation + motion    |
|  **2 / 6**   | **3.3**  | Minimal motion tracking      |
|  **1 / 6**   | **1.7**  | Very limited sensors         |
|  **0 / 6**   | **0.0**  | No sensors detected          |

### 🔹 7.8 USB Port Speed
*Description:* Wired transfer speed. Fast USB means you can copy 4K videos to a PC in seconds, or connect to a monitor.
*   **Measurement:** Data transfer rate (Gbps).
*   **Unit:** Version / Speed
*   **Significance:** File transfer speed and video output capability.
| Score    | Version / Speed            | Example Models           |
| :------- | :--------------------------| :----------------------- |
| **10.0** | **USB 3.2 Gen 2 (10Gbps)** | S24 Ultra, iPhone 15 Pro |
| **8.0**  | **USB 3.1 / 3.0 (5Gbps)**  | Pixel 8                  |
| **6.0**  | **USB 2.0 (480Mbps)**      | iPhone 14, Galaxy A55    |
| **3.0**  | **Micro-USB**              | Legacy                   |
| **0.0**  | **Proprietary/none**       | Obsolete                 |

### 🔹 7.9 Ecosystem Connectivity & Cross-Device Features Index (ECI)
*Description:* Measures the availability of specific, verifiable connectivity & cross-device continuity features that improve workflow and device interaction — without subjective judgement.
*   **Measurement:** Count of supported features.
*   **Unit:** Index Score (0-10)
*   **Significance:** Workflow efficiency across multiple devices.

**Feature List (Scored Individually):**
Each feature is independent and publicly verifiable.

| Feature                                                 | Why it matters                        |
| :------------------------------------------------------ | :-------------------------------------|
| **Cross-device clipboard / drag & drop**                | Seamless text transfer across devices |
| **Auto switch / multipoint audio**                      | Earbuds/devices follow your activity  |
| **Native file transfer (e.g., Nearby Share / AirDrop)** | Quick local sharing                   |
| **Shared notifications across devices**                 | See alerts on all screens             |
| **Multi-device calling/SMS support**                    | Use phone comms on other devices      |

**Scoring Rules (0–10):**
Each feature presence counts as 1 point, up to a maximum of 5 points.
*Formula:* `ECI = (Count_of_Features / 5) * 10`

| Count | Score    |
| :---- | :------- |
| **5** | **10.0** |
| **4** | **8.0**  |
| **3** | **6.0**  |
| **2** | **4.0**  |
| **1** | **2.0**  |
| **0** | **0.0**  |


## 🟣 8. Audio

### 🔹 8.1 Speaker System Capability (SSC)
*Description:* Evaluates the physical speaker configuration of the device. Focuses on speaker count, placement, and channel symmetry. Acoustic tuning and subjective sound quality are intentionally excluded.
*   **Measurement:** Speaker count and placement (manufacturer specs, teardowns, reviews).
*   **Unit:** Hardware Configuration Score (0-10)
*   **Significance:** Determines baseline loudness, stereo separation, and immersion without headphones.

| Score    | Speaker Configuration                               |
| :------- | :-------------------------------------------------- |
| **10.0** | **Stereo, dual front-facing speakers**              | 
| **8.0**  | **Stereo, dual NON-front-facing speakers**          | 
| **6.0**  | **Stereo labeled but asymmetrical**                 | 
| **4.0**  | **Mono physical speaker**                           |                          
| **0.0**  | **No usable speaker**                               | 

Explanation:
**Stereo, dual front-facing speakers**: Two distinct speaker units both oriented toward the user (e.g., top/bottom or left/right front bezels)
**Stereo, dual NON-front-facing speakers**: The phone has two separate physical speaker units that output stereo sound, but at least one speaker does not face the user directly (e.g., bottom-firing or side-firing), which limits spatial accuracy.
**Stereo labeled but asymmetrical**: Two physical drivers present but one is not a true channel (e.g., both at bottom or unbalanced geometry)
**Mono physical speaker**: Only one physical speaker unit present, no stereo channel labeling
**No usable speaker**: No working built-in speaker (e.g., legacy device, accessory-only audio)

Note: This section evaluates only physical speaker hardware. Virtual surround, spatial audio, Dolby Atmos, and head tracking are software-level features and are evaluated separately in playback processing sections.

### 🔹 8.2 Playback Audio Processing & Immersion (PAPI)
*Description:* Evaluates the phone's ability to decode modern multichannel audio formats and to render spatialized sound during playback. This section focuses exclusively on playback-side processing, independent of speakers, microphones, or wired audio output.
*   **Measurement:** Supported playback formats, OS-level spatial audio feature support.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Determines compatibility with modern streaming content and immersion during media consumption.

**Structure:**
PAPI is a weighted composite of two subsections:
- **8.2.1 Audio Format Decode Support** — 50% weight
- **8.2.2 Spatial Audio Rendering** — 50% weight

*Formula:* `PAPI = (0.5 × Score_8.2.1) + (0.5 × Score_8.2.2)`

---

#### 8.2.1 Audio Format Decode Support
*What it measures:* Range of multichannel or object-based audio formats the device can natively decode.
*Why it matters:* Determines compatibility with modern streaming and video content.

| Score    | Supported Decode Formats             |
| :------- | :----------------------------------- |
| **10.0** | **Dolby Atmos and DTS:X**            |
| **8.0**  | **Dolby Atmos only**                 |
| **5.0**  | **Multichannel surround (DD / DD+)** |
| **0.0**  | **Stereo only**                      |

---

#### 8.2.2 Spatial Audio Rendering (Playback)
*What it measures:* Ability of the operating system to spatialize audio during playback, creating a 3D soundstage over headphones or speakers.
*Why it matters:* Determines immersion and realism during media consumption.

| Score    | Spatial Rendering Capability                |
| :------- | :------------------------------------------ |
| **10.0** | **Spatial audio with dynamic head tracking**|
| **7.0**  | **Spatial audio (static, no head tracking)**|
| **0.0**  | **No spatial rendering**                    |

---

### 🔹 8.3 Wired Audio Capability
*Description:* Evaluates native wired audio output options available without relying on external powered accessories.
*   **Measurement:** Presence of 3.5mm analog audio jack, presence of analog audio output via USB-C, digital-only USB-C audio fallback.
*   **Unit:** Wired Audio Capability Score (0-10)
*   **Significance:** Determines whether users can use wired headphones directly, with minimal friction and without extra hardware.

**Why 3.5mm is superior:**
The 3.5mm jack provides universal compatibility (works with all wired headphones), true zero-latency analog output, requires no adapters or dongles, and adds no points of failure. USB-C audio requires either rare analog support or digital conversion through a dongle, adding cost, fragility, and potential latency issues.

| Score    | Wired Audio Support                              | Example Models               |
| :------- | :----------------------------------------------- | :--------------------------- |
| **10.0** | **3.5mm headphone jack (native analog output)**  | Sony Xperia 1 V, Zenfone 10  |
| **6.0**  | **USB-C with documented analog audio output**    | Select Motorola/Sony models  |
| **3.0**  | **USB-C digital audio only (dongle required)**   | Most Flagships (S24, iPhone) |
| **0.0**  | **No wired audio support**                       | Rare/obsolete devices        |

### 🔹 8.4 Microphone & Audio Recording (MAR)
*Description:* Evaluates the audio capture capability of the device using only publicly verifiable data, without subjective quality judgments. This is a composite score based on hardware count, recording channels, and advanced features.
*   **Measurement:** Microphone count, recording channels/modes, documented audio features.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Determines audio capture quality for calls, videos, and content creation.

**Structure:**
MAR is a weighted composite of three subsections:
- **8.4.1 Microphone Hardware Count (MHC)** — 30% weight
- **8.4.2 Recording Channels & Modes (RCM)** — 30% weight
- **8.4.3 Advanced Capture Features (ACF)** — 40% weight

*Formula:* `MAR = (0.30 × MHC) + (0.30 × RCM) + (0.40 × ACF)`

---

#### 8.4.1 Microphone Hardware Count (MHC)
*What it measures:* Physical microphones available for capture (bottom, top, rear, front).
*Why it matters:* More microphones enable better noise separation, spatial capture, and redundancy.

| Score    | Microphone Count                      |
| :------- | :------------------------------------ |
| **10.0** | **≥ 4 microphones**                   |
| **8.0**  | **3 microphones**                     |
| **5.0**  | **2 microphones**                     |
| **2.0**  | **1 microphone**                      |
| **0.0**  | **Unknown / undocumented**            |

---

#### 8.4.2 Recording Channels & Modes (RCM)
*What it measures:* How many audio channels the phone can record and in which modes.
*Why it matters:* Stereo recording dramatically improves realism; multi-channel enables spatial audio and post-processing.

| Score    | Recording Capability                  |
| :------- | :------------------------------------ |
| **10.0** | **Multi-channel / spatial audio**     |
| **8.0**  | **Stereo audio recording**            |
| **5.0**  | **Mono recording**                    |
| **0.0**  | **Voice-only / unclear**              |

---

#### 8.4.3 Advanced Capture Features (ACF)
*What it measures:* Presence of clearly documented, named audio-processing features.
*Why it matters:* These features demonstrably improve intelligibility and subject isolation.

**Feature List (binary, additive):**
Each feature = +2.5 points, max 10.0.

| Feature (Publicly Documented)                                          | Points   |
| :--------------------------------------------------------------------- | :------- |
| **Directional / Audio Zoom**                                           | **+2.5** |
| **Wind noise reduction**                                               | **+2.5** |
| **Voice focus / subject isolation**                                    | **+2.5** |
| **High-quality external mic support (USB-C / 3.5mm with manual gain)** | **+2.5** |

*Formula:* `ACF = 2.5 × number_of_features` (Clamped 0-10)


## 🟣 9. Financial & Economic Value

### 🔹 9.1 Price
*Description:* The current market price in USD. Lower prices mean better accessibility for more people.
*   **Measurement:** Manufacturer's Suggested Retail Price (MSRP) at launch or current average market price.
*   **Unit:** USD ($)
*   **Significance:** Primary barrier to entry and value determinant.
*Formula:* `Score = 10 - 10 * (log(Price) - log(100)) / (log(1600) - log(100))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ $100
*   **Min Score (0.0):** ≥ $1600
> [!NOTE]
> **Why Logarithmic?** Price sensitivity is relative. A $50 increase on a $150 phone is a massive 33% hike, whereas a $50 increase on a $1000 phone is a negligible 5%. The logarithmic scale reflects this relative impact on affordability.

### 🔹 9.2 Repairability
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

### 🔹 9.3 Service Ecosystem Support
*Description:* Measures the practical ability to obtain official parts and documentation for the device.
*   **Measurement:** Manufacturer self-repair programs, parts store availability, public manuals, authorized network scope.
*   **Unit:** Support Level Score (0-10)
*   **Significance:** Determines if the device can actually be serviced in the real world over its lifetime.

| Score    | Support Level                             | Example Models                 |
| :------- | :-----------------------------------------| :----------------------------- |
| **10.0** | **Self-repair program + parts + manuals** | Fairphone, Apple, Samsung      |
| **8.0**  | **Official parts sold, no manuals**       | Google (via iFixit), Motorola  |
| **6.0**  | **Authorized repair only (global)**       | Most major global brands       |
| **3.0**  | **Limited regional service**              | Regional/Budget brands         |
| **0.0**  | **No official repair pathway**            | Niche/Import-only devices      |

### 🔹 9.4 Warranty Length
*Description:* Manufacturer's standard warranty period. Longer warranties indicate manufacturer confidence and provide financial protection.
*   **Measurement:** Manufacturer policy commitment.
*   **Unit:** Months
*   **Significance:** Financial protection against defects and accidents.

IMPORTANT: The score of a phone is based on its Limited Manufacturer Warranty (the one that applies globally, usually 12 months). This measures the manufacturer's confidence in the hardware. Hence, a phone sold in the US with a 12-month warranty and in the EU with a 24-month warranty will only get a 3.0 score corresponding to the 12-month warranty. In short, the shortest warranty applied worldwide is the one used for scoring.

| Score    | Manufacturer Warranty Period  | Example Models                                                   |
| :------- | :---------------------------- | :--------------------------------------------------------------- |
| **10.0** |   **≥ 60 Months (5 Years)**   | Fairphone 5/6, Teracube (Often requires registration)            |
| **8.5**  |   **48 Months (4 Years)**     | Rugged/Enterprise models (e.g., Samsung Tactical).               |
| **7.0**  |   **36 Months (3 Years)**     | Newer EU baseline (Spain/Portugal) or Nokia X-series.            |
| **5.0**  |   **24 Months (2 Years)**     | EU Standard                                                      |
| **3.0**  |   **12 Months (1 Year)**      | US Standard. The bare minimum for Apple/Samsung/Google globally. |
| **0.0**  |   **0 Months**                | Grey Market / Used                                               |


## 🟣 10. Miscellaneous

### 🔹 10.1 Haptics Quality
*Description:* Vibration quality. Good haptics feel like crisp clicks (premium), while bad ones feel like a buzzy rattle (cheap).
*   **Measurement:** Teardown / Tactile evaluation.
*   **Unit:** Motor Type
*   **Significance:** Affects typing experience and notification quality.

| Score    | Motor Type                                                      | Example Models              |
| :------- | :-------------------------------------------------------------- | :-------------------------- |
| **10.0** | **Large X-axis linear motor (≥ 20mm length or “Taptic-class”)** | iPhone (Taptic), OnePlus 12 |
| **8.0**  | **Standard X-axis linear motor**                                | S24, Pixel 8                |
| **6.0**  | **Z-axis linear motor**                                         | Galaxy A55                  |
| **3.0**  | **Eccentric rotating mass motor (coin or cylinder type)**       | Budget Phones               |
| **0.0**  | **No vibration motor**                                          | -                           |

### 🔹 10.2 Stylus Hardware & System Support (SHSS)
*Description:* Measures whether the phone supports active stylus input at the hardware and system level, including digitizer presence and latency class.
*   **Measurement:** Digitizer specifications, stylus protocol support, manufacturer documentation.
*   **Unit:** Stylus Capability Index (0–10)
*   **Significance:** Determines whether precision input is natively supported or only simulated.

| Score    | Stylus Support Level                                                   | Example Models                  |
| :------- | :--------------------------------------------------------------------- | :------------------------------ |
| **10.0** | **Integrated active stylus + dedicated digitizer + Bluetooth features**| S24 Ultra                       |
| **8.0**  | **Integrated active stylus + dedicated digitizer**                     | Moto G Stylus                   |
| **6.0**  | **External active stylus support (digitizer present)**                 | Z Fold 5, Xiaomi Mix Fold       |
| **3.0**  | **Passive capacitive stylus compatibility**                            | iPhone, Pixel, Standard Android |
| **0.0**  | **No stylus support**                                                  | -                               |

> [!NOTE]
> **Technical Definitions:**
> - **Digitizer:** A special layer under the screen that detects a stylus tip separately from your finger. This allows the phone to track very precise movements, detect pressure levels, and ignore your palm while writing. Phones without a digitizer can only use basic “dumb” styluses that act like a finger.
> - **Integrated active stylus:** Physically built into the phone and stored inside a dedicated slot in the device body.
> - **External active stylus:** A separate accessory you carry and attach magnetically or store in a case — it is not built into the phone.
> - **Passive capacitive stylus:** Essentially a finger substitute. It does not communicate electronically with the phone (no interaction with any digitizer layer).


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

### 11.B Justification Logic
A valid booster requires a clear logical chain linking a hidden technical feature to an observed result.
Each booster section must provide the following elements:
1)  **Source Link:** The link of the review that must be publicly accesible 
2)  **Impacted Subsection:** The subsection number impacted by the booster value, for example 4.16
3)  **Booster:** The value of the booster, for example 1.05
4)  **Justification:**
    a)   **Unaccounted Feature (Cause):** The specific technical mechanism, hardware component, or software algorithm that is responsible for the anomaly. This is the "Why".
    b)   **Unaccounted Reason (Gap):** The explicit explanation of *why* this feature is not captured by the standard scoring rules of Sections 1-10.
    c)   **Observed Justification (Effect):** The tangible performance outcome observed in the review. This is the "What".
    The justification must be detailed and exhaustive enough to be understood without further explanation, and sufficient to justify the booster value.

**Extract Requirement:** Both **Unaccounted Feature** and **Observed Justification** must be **exact, verbatim extracts** from the review. These extracts must be exact, meaning that searching for any extract in the review source will find it as is. **NEVER** invent, paraphrase, or hallucinate content. If the exact text is not in the source, the booster is invalid.
**Technical Causality:** There must be a clear link between the technical mechanism (the **Unaccounted Feature**) and the performance outcome (the **Observed Justification**). Purely comparative statements (e.g., "best we have seen") are **INVALID** unless they explain *why*.

### 11.C Evidence Requirements 
*   **Proof & Precision:** The extracts must contain specific quantitative data (e.g., "Delta-E 0.14", "117 points") or precise technical descriptions. Vague praise is not evidence.
*   **Source Verification:** All source links must be active, accessible URLs from reputable publications. Placeholders (e.g., `example.com`) are **STRICTLY PROHIBITED**. If a specific text extract is used, the source must be verifiable.
*   **Specificity:** Justifications must be extremely specific to the findings of the review and the technical gap they fill.
*   **Disjointed Extracts:** Extracts may combine non-contiguous text from the same review, for example to link technical data with the resulting conclusion. Use `[...]` to indicate the separation. For more fluidity, parts that are less distant from each other than 3 sentences should not be separated.
*   **Decomposition:** A single review source may impact multiple subsections; in such cases, the booster must be decomposed into separate entries.
    *   *Example:* If a review finds a phone has exceptional telephoto zoom but poor video stabilization:
        *   **Booster A (1.10):** Targets Subsection 4.5 (Zoom Capability) for superior optics.
        *   **Booster B (0.90):** Targets Subsection 4.4 (Image Stabilization) for poor software compensation.

### 11.D Process
*   **Verification Loop:** After drafting a booster, perform a mandatory self-check ensuring that **ALL** rules in sections 11.A, 11.B, and 11.C are strictly satisfied. If any rule is violated, discard and refine. Repeat this refinement process up to **3 times**. If the booster still fails to meet all criteria after the 3rd attempt, **discard the booster entirely** and log a "Verification Failed" error for that subsection.

> [!NOTE]
> The following items are **examples** of how expert reviews can be used to adjust theoretical scores. In practice, any reputable and verifiable expert review can be used as a booster source.

### 🔹 11.1 DXOMARK 24MP Texture Optimization
*   **Source Link:** [iPhone 15 Pro Max Camera Test](https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/)
*   **Impacted Subsection:** 4.16 Computational Photography & AI
*   **Booster:** **1.05**
*   **Justification:**
    *   **Unaccounted Feature:** "the jump from 12MP to 24MP images by default"
    *   **Unaccounted Reason:** Section 4.3 scores the sensor's max resolution (48MP) and Section 4.16 scores HDR presence, but neither captures the computational fusion that enables a 24MP default output with superior texture rendering.
    *   **Observed Justification:** "made for significantly improved texture quality"

### 🔹 11.2 Tom's Guide Display Color Accuracy
*   **Source Link:** [iPhone 15 Pro Max Review](https://www.tomsguide.com/reviews/iphone-15-pro-max)
*   **Impacted Subsection:** 2.7 Color Accuracy & HDR
*   **Booster:** **1.05**
*   **Justification:**
    *   **Unaccounted Feature:** "earned a Delta-E score of 0.14"
    *   **Unaccounted Reason:** Section 2.7 scores theoretical support (DCI-P3, Dolby Vision) but does not measure the specific factory calibration accuracy (Delta-E).
    *   **Observed Justification:** "offers more accurate colors"

### 🔹 11.3 NotebookCheck PWM Flickering
*   **Source Link:** [iPhone 15 Pro Max Review](https://www.notebookcheck.net/Apple-iPhone-15-Pro-Max-review-More-camera-power-and-titanium-for-Apple-s-biggest-smartphone.756855.0.html)
*   **Impacted Subsection:** 2.1 Display Technology
*   **Booster:** **0.95**
*   **Justification:**
    *   **Unaccounted Feature:** "The frequency of 240 Hz is relatively low"
    *   **Unaccounted Reason:** Section 2.1 scores the OLED technology type but does not penalize low-frequency PWM dimming which can cause eyestrain for sensitive users.
    *   **Observed Justification:** "sensitive users will likely notice flickering" 
