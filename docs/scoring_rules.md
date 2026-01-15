# Comprehensive Smartphone Scoring Rules (v8.0) - Let's build the Golden Standard together

This document provides **exhaustive, unit-specific reference tables** for every technical criterion found in the v4.0 Data Structure.
*   **Principle:** Every single data point that differentiates a product must have a corresponding score.
*   **Normalization:** 0 = Worst/Obsolete, 10 = Best/State-of-the-Art.
*   **Units:** All criteria include specific units of measurement.


## 🟣 1. Design & Build Quality

### 🔹 1.1 Materials (Frame/Back)
*Description:* The physical materials used for the device chassis and rear panel. Affects how premium the phone feels, how well it resists drops, and how cool it stays during use.
*   **Measurement:** Manufacturer specifications and physical inspection.
*   **Unit:** Qualitative (Material Tier)
*   **Significance:** Determines structural integrity, thermal dissipation, and tactile quality.
| Score    | Combination                     | Example Models                  |
| :------- | :------------------------------ | :------------------------------ |
| **10.0** | **Titanium + Ceramic/Shield**   | iPhone 15 Pro Max, Xiaomi Mix 4 |
| **9.0**  | **Titanium + Glass**            | Samsung Galaxy S24 Ultra        |
| **8.5**  | **Stainless Steel + Glass**     | iPhone 14 Pro Max               |
| **8.0**  | **Aluminum + Glass (Victus)**   | Pixel 8 Pro, Galaxy S24+        |
| **7.0**  | **Aluminum + Glass (Standard)** | Nothing Phone (2), Xiaomi 13T   |
| **6.0**  | **Plastic Frame + Glass Back**  | Galaxy A55, Redmi Note 13 Pro+  |
| **5.0**  | **High-Quality Polycarbonate**  | Pixel 7a, Lumia 1020 (Legacy)   |
| **4.0**  | **Plastic + Plastic**           | Galaxy A15, Moto G Power        |
| **2.0**  | **Cheap Plastic / Removable**   | Entry-level / Feature Phones    |
| **0.0**  | **No Information**              | Unknown                         |

### 🔹 1.2 Durability (IP Rating)
*Description:* Ingress Protection rating against dust and water. Determines if your phone can survive a drop in the toilet, rain, or a dusty environment.
*   **Measurement:** Standardized ingress protection testing.
*   **Unit:** IP Rating (IEC 60529)
*   **Significance:** Critical for device longevity and accident protection.
| Score    | Rating (Unit) | Description                  | Example Models          |
| :------- | :------------ | :--------------------------- | :---------------------- |
| **10.0** | **IP69K**     | High Temp/Pressure Jets      | Ulefone Armor 23 Ultra  |
| **9.0**  | **IP68**      | Submersion >1.5m for 30 mins | S24 Ultra, iPhone 15    |
| **8.0**  | **IP67**      | Submersion 1m for 30 mins    | Pixel 7a, Galaxy A54    |
| **6.0**  | **IP54**      | Splash Proof                 | Moto G84, Redmi Note 13 |
| **4.0**  | **IP53**      | Light Spray                  | Poco X6 Pro             |
| **0.0**  | **None**      | No Rating                    | Entry-level devices     |

### 🔹 1.3 Glass Protection
*Description:* The generation of protective glass used on the display. Newer versions are much harder to crack or scratch when dropped.
*   **Measurement:** Manufacturer specifications (Mohs hardness scale correlation).
*   **Unit:** Generation / Brand
*   **Significance:** Reduces the likelihood of screen breakage from drops.
| Score    | Technology                   | Example Models                |
| :------- | :--------------------------- | :---------------------------- |
| **10.0** | **Gorilla Glass Armor**      | S24 Ultra                     |
| **9.5**  | **Ceramic Shield (Latest)**  | iPhone 15/16 Series           |
| **9.0**  | **Gorilla Glass Victus 2**   | S23 Ultra, OnePlus 12         |
| **8.0**  | **Gorilla Glass Victus / +** | Pixel 7 Pro, Xiaomi 12S Ultra |
| **7.0**  | **Gorilla Glass 5 / 6**      | Galaxy A54, Nothing Phone (1) |
| **5.0**  | **Gorilla Glass 3**          | Pixel 6a, Budget Phones       |
| **3.0**  | **Tempered Glass (Generic)** | Low-end Androids              |
| **0.0**  | **No Protection / Plastic**  | Entry-level / Feature Phones  |

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

### 🔹 2.1 Technology & Quality
*Description:* The screen technology. OLED panels offer perfect blacks and vibrant colors, while newer LTPO versions save significant battery life.
*   **Measurement:** Panel analysis (Microscope/Spec).
*   **Unit:** Technology Type
*   **Significance:** Defines contrast ratio, power efficiency, and viewing angles.
| Score    | Technology              | Description                    | Example Models              |
| :------- | :---------------------- | :----------------------------- | :-------------------------- |
| **10.0** | **Tandem OLED**         | Dual-stack, extreme brightness | iPad Pro M4 (Reference)     |
| **9.5**  | **LTPO 3.0 / Eco²**     | 1-120Hz, lowest power          | OnePlus 12, Xiaomi 14 Ultra |
| **9.0**  | **LTPO OLED**           | 1-120Hz Variable               | S24 Ultra, iPhone 15 Pro    |
| **8.0**  | **Dynamic AMOLED 2X**   | 120Hz, HDR10+                  | S21 Ultra, S22+             |
| **7.0**  | **Super AMOLED / OLED** | 60-90Hz, Infinite Contrast     | Galaxy A55, Pixel 7a        |
| **5.0**  | **IPS LCD (120Hz)**     | Fast LCD, Good Colors          | Poco X4 GT                  |
| **3.0**  | **IPS LCD (60Hz)**      | Standard LCD                   | iPhone 11, Galaxy A14       |
| **0.0**  | **TFT / TN**            | Poor Angles, Washout           | Galaxy J1 (Legacy)          |

### 🔹 2.2 Resolution Density
*Description:* Pixel density (sharpness). Higher PPI means text and images look crisp, with no visible pixels.
*   **Measurement:** Calculated from Resolution and Diagonal Size.
*   **Unit:** Pixels Per Inch (PPI)
*   **Significance:** Determines visual sharpness and clarity of text.
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

### 🔹 2.4 Eye Comfort (PWM Dimming)
*Description:* How the screen dims. Higher frequencies prevent eye strain, headaches, and fatigue for people sensitive to screen flicker.
*   **Measurement:** Oscilloscope or flicker meter at low brightness levels.
*   **Unit:** Hertz (Hz)
*   **Significance:** Reduces eye strain and headaches for sensitive users.
*Formula:* `Score = 10 * (log(Hz) - log(120)) / (log(3840) - log(120))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 3840 Hz
*   **Min Score (0.0):** ≤ 120 Hz
> [!NOTE]
> **Why Logarithmic?** The health benefits of higher PWM frequencies follow a diminishing return curve. The jump from 240Hz to 480Hz significantly reduces visible flicker for sensitive eyes, whereas the difference between 2000Hz and 3000Hz is marginal.

### 🔹 2.5 Touch Responsiveness
*Description:* How fast the screen reacts to your touch. Higher rates mean instant response in games and a "glued to your finger" feel.
*   **Measurement:** Touch latency testing (time from touch to signal).
*   **Unit:** Hertz (Hz)
*   **Significance:** Critical for competitive gaming and UI fluidity.
*Formula:* `Score = 10 * (log(Hz) - log(60)) / (log(960) - log(60))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 960 Hz
*   **Min Score (0.0):** ≤ 60 Hz
> [!NOTE]
> **Why Logarithmic?** Input latency perception is non-linear. Increasing sampling rate from 60Hz to 240Hz provides a noticeably "stickier" feel. Beyond 480Hz, the improvements in reaction time are smaller than the average human reaction variance.

### 🔹 2.6 Refresh Rate
*Description:* How many times the screen updates per second. 120Hz+ makes scrolling and animations look incredibly smooth compared to standard 60Hz.
*   **Measurement:** High-speed camera analysis or system reporting.
*   **Unit:** Hertz (Hz)
*   **Significance:** Determines the smoothness of motion and animations.
*Formula:* `Score = 10 * (log(Hz) - log(45)) / (log(165) - log(45))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 165 Hz
*   **Min Score (0.0):** ≤ 45 Hz
> [!NOTE]
> **Why Logarithmic?** Motion smoothness perception follows Weber's Law. The upgrade from 60Hz to 120Hz is a massive leap in fluidity. The step from 120Hz to 144Hz or 165Hz is much harder to perceive for the average user.

### 🔹 2.7 Color Accuracy & HDR
*Description:* Support for rich colors and contrast. Ensures movies and photos look realistic, vibrant, and exactly as the creator intended.
*   **Measurement:** Colorimeter (Delta E) and gamut coverage (DCI-P3 %).
*   **Unit:** Standards / Gamut Coverage
*   **Significance:** Ensures content is displayed as the creator intended.
| Score    | Features                       | Example Models                 |
| :------- | :----------------------------- | :----------------------------- |
| **10.0** | **Dolby Vision + 100% DCI-P3** | iPhone 15 Pro, Xiaomi 13 Ultra |
| **9.0**  | **HDR10+ + 100% DCI-P3**       | S24 Ultra, OnePlus 12          |
| **8.0**  | **HDR10 + High Gamut**         | Pixel 8, Nothing Phone (2)     |
| **6.0**  | **Basic HDR support**          | Galaxy A55                     |
| **3.0**  | **No HDR / sRGB only**         | Budget LCDs                    |
| **0.0**  | **No HDR, No sRGB**            | Entry Level / TN panels        |

### 🔹 2.8 Screen Size
*Description:* The physical size of the display measured diagonally. Larger screens offer more immersive media and gaming experiences.
*   **Measurement:** Diagonal length of the active display area.
*   **Unit:** Inches (")
*   **Significance:** Determines immersion level and device footprint.
*Formula:* `Score = 10 * ((Size - 4.5) / (7.6 - 4.5))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 7.6"
*   **Min Score (0.0):** ≤ 4.5"
> [!NOTE]
> This is a continuous linear scoring metric. Larger screens provide more immersion.

### 🔹 2.9 Screen-to-Body Ratio (Bezels)
*Description:* How much of the front is screen vs. border. Higher percentage means thinner bezels and a more immersive, modern look.
*   **Measurement:** (Active Display Area / Total Frontal Area) * 100.
*   **Unit:** Percentage (%)
*   **Significance:** Aesthetic modernity and immersion.
*Formula:* `Score = 10 * ((Ratio - 60) / (93 - 60))` (Clamped 0-10)
*   **Max Score (10.0):** ≥ 93%
*   **Min Score (0.0):** ≤ 60%
> [!NOTE]
> This is a continuous linear scoring metric. Higher ratio means thinner bezels.


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
*   **Core Weights:**
    *   **10:** Apple M3/A17 Pro
    *   **9:** Cortex-X4 (e.g., Snapdragon 8 Gen 3)
    *   **8:** Cortex-X3 (e.g., Snapdragon 8 Gen 2)
    *   **7:** Cortex-X2 (e.g., Snapdragon 8 Gen 1)
    *   **6:** Cortex-A720 / A715 / A710 (Modern Performance)
    *   **4:** Cortex-A76 / A55 Hybrids (Legacy Performance)
    *   **2:** Cortex-A520 / A510 (Modern Efficiency)
    *   **0:** Cortex-A55 / A53 (Legacy Efficiency)

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
*   **Weights:** Same as Section 3.1 (e.g., Cortex-X4 = 9, Cortex-A78 = 6).

**Step 2: Frequency Modifier (FM)**
*   *What is it?* A direct multiplier for clock speed.
*   **Formula:** `Max_Freq_GHz / Max_Freq_GHz_Best_Phone`
    *   *Range is 0-1.
    *   **Why FM?** Single-core performance scales almost linearly with frequency for the same architecture. A 3.0GHz core is roughly 50% faster than a 2.0GHz core of the same type.

**Step 3: Calculate Final Score**
1.  **Raw Single-Thread (STRS - Single Thread Raw Score):** `CAS * FM`
2.  **Final Score:** `10 * (log(STRS) - log(STRS_Worst_Phone)) / (log(STRS_Best_Phone) - log(STRS_Worst_Phone))`
    *   **Parameters:** See `scoring_parameters.md` for values.

> **Example: Snapdragon 8 Gen 3**
> *   **Specs:** Prime Core is Cortex-X4 at 3.3GHz.
> *   **CAS:** Cortex-X4 = **9**
> *   **FM:** `3.3 / Max_Freq_GHz_Best_Phone` = `3.3 / 3.8` = **0.87**
> *   **Raw:** `9 * 0.87` = **7.83**
> *   **Score:** `10 * (log(7.83) - log(STRS_Worst_Phone)) / (log(STRS_Best_Phone) - log(STRS_Worst_Phone))`
> *   `10 * (log(7.83) - log(1)) / (log(11) - log(1))` = `10 * (0.894 - 0) / (1.041 - 0)` = `10 * 0.859` ≈ **8.6/10**


### 🔹 3.3 GPU Performance (Graphics & Gaming)
*Description:* Measures the graphical processing power for gaming, rendering, and compute tasks. This score is a composite of raw architecture power, modern API support, and advanced feature capabilities.
*   **Measurement:** Architecture Generation + API Support + Ray Tracing.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for high-fidelity gaming, UI smoothness, and future-proofing.

**Part 1: Base GPU Architecture Score (70%)**
*   *What is it?* The core raw performance potential based on the GPU generation and tier.
*   **Measurement:** GPU Model & Generation.
| Score    | GPU Class                                | Example Models                 |
| :------- | :--------------------------------------- | :----------------------------- |
| **10.0** | **Apple GPU (Latest) / Immortalis-G720** | iPhone 15 Pro, Dimensity 9300  |
| **9.0**  | **Adreno 750 / 740**                     | S24 Ultra, S23 Ultra           |
| **8.0**  | **Adreno 730 / Mali-G715**               | S22 Ultra, Pixel 8 Pro         |
| **7.0**  | **Adreno 660 / Mali-G710**               | S21 Ultra, Pixel 7 Pro         |
| **6.0**  | **Adreno 642L / Mali-G610**              | Nothing Phone (1), Galaxy A55  |
| **4.0**  | **Adreno 619 / Mali-G68**                | Galaxy A54, Moto G84           |
| **2.0**  | **Adreno 610 / Mali-G52**                | Budget Phones (Snapdragon 680) |
| **0.0**  | **Legacy / Unknown**                     | Entry Level                    |

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
1.  **Calculate Base Score:** `10 * (log(16) - log(Node)) / (log(16) - log(3)) - 0.3`
    *   *Note:* The `- 0.3` ensures that a perfect 10.0 is only achievable with the TSMC modifier.
2.  **Apply Modifier:** `Final_Score = Base_Score + Foundry_Modifier` (Clamped 0-10)

*   **Max Score (10.0):** ≤ 3nm (TSMC Only)
*   **Min Score (0.0):** ≥ 16nm

**Foundry Efficiency Modifier:**
| Foundry           | Modifier | Why?                                               |
| :---------------- | :------- | :------------------------------------------------- |
| **TSMC**          | **+0.3** | Consistently higher efficiency at same node label. |
| **Samsung**       | **0.0**  | Standard efficiency baseline.                      |
| **SMIC / Others** | **-0.3** | Generally lower yield/efficiency than leaders.     |

> [!NOTE]
> **Why Logarithmic & 16nm Cap?** Transistor density scales non-linearly. A shrink from 10nm to 5nm is a massive leap compared to 16nm to 11nm. We cap the scale at 16nm because almost all relevant modern devices (post-2018) are ≤16nm, ensuring the score resolution is focused where it matters most.

### 🔹 3.5 Thermal Dissipation & Stability Index (TDSI)
*Description:* A composite index measuring the device's ability to sustain performance and shed heat. It combines the physical thermal capacity of the chassis with the sophistication of the internal cooling solution.
*   **Measurement:** Materials + Weight + Cooling System Type.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Prevents throttling, ensures sustained gaming performance, and maintains device longevity.

**Part A: Passive Thermal Capacity (60%)**
*   *What is it?* The hardware's physical ability to absorb and dissipate heat into the environment.
*   **Measurement:** Frame/Back Material + Device Mass.
*   **Step 1: Material Score**
| Material Configuration               | Score  | Why?                                    |
| :----------------------------------- | :----- | :-------------------------------------- |
| **Metal Frame + Glass/Ceramic Back** | **10** | Best passive dissipation combo.         |
| **Metal Frame + Plastic Back**       | **8**  | Plastic back traps some heat.           |
| **Plastic Frame + Glass Back**       | **6**  | Plastic frame hinders edge dissipation. |
| **Plastic Frame + Composite**        | **4**  | Low thermal conductivity.               |
| **All Plastic**                      | **0**  | Insulator, poor dissipation.            |

*   **Step 2: Mass Modifier (Thermal Inertia)**
    *   *Formula:* `Mass_Modifier = clamp(Weight_g / Weight_Heaviest_Phone, 0.7, 1.0)`
    *   *Logic:* Heavier phones have more thermal mass. We use `Weight_Heaviest_Phone` as the reference. Lighter phones get a reduction factor (<1.0), while the heaviest phone gets no penalty (1.0).
*   **Score A:** `clamp(Material_Score * Mass_Modifier, 0, 10)`

**Part B: Cooling System Class (40%)**
*   *What is it?* The engineering sophistication of the internal heat management.
*   **Measurement:** Cooling solution type (from specs/marketing).
| Cooling Solution                | Score  | Description                                |
| :------------------------------ | :----- | :----------------------------------------- |
| **Active Cooling (Fan)**        | **10** | Physical fan (e.g., RedMagic).             |
| **Large Vapor Chamber**         | **8**  | Explicitly marketed large area (>4000mm²). |
| **Vapor Chamber (Standard)**    | **7**  | Standard flagship cooling.                 |
| **Multi-layer Graphite/Copper** | **5**  | Basic passive spreading.                   |
| **Basic Heat Spreader**         | **3**  | Minimal cooling (budget).                  |
| **None Disclosed**              | **0**  | Likely no specific cooling.                |

**Final Formula:** `TDSI = (0.6 * Score_A) + (0.4 * Score_B)`

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
*Description:* Technology to reduce blur from handshakes. Essential for sharp low-light photos and smooth video recording.
*   **Measurement:** Hardware analysis (OIS, Sensor-Shift).
*   **Unit:** Stabilization Type
*   **Significance:** Critical for low-light sharpness and video stability.
| Score    | Technology                      | Example Models                |
| :------- | :------------------------------ | :---------------------------- |
| **10.0** | **Gimbal / Sensor-Shift Gen 2** | iPhone 15 Pro Max, Zenfone 10 |
| **9.0**  | **Sensor-Shift OIS**            | iPhone 15, Pixel 8 Pro        |
| **8.0**  | **Standard OIS**                | S24 Ultra, Galaxy A55         |
| **5.0**  | **EIS Only (Electronic)**       | Budget Phones                 |
| **2.0**  | **Poor EIS**                    | Low-end chipsets              |
| **0.0**  | **None**                        | Entry Level                   |

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
| Score  | Focus Type                |
| :----- | :------------------------ |
| **10** | **Ultrawide with AF**     |
| **6**  | **Fixed focus ultrawide** |
| **0**  | **No macro-capable lens** |

**4.7.2 Minimum Focus Distance**
*   *Why it matters:* The physical limit of how close you can get.
*   **Measurement:** Minimum focus distance (cm).
*   *Formula:* `Score = 10 - 10 * ((Distance - 2) / (10 - 2))` (Clamped 0-10)
    *   **10.0:** ≤ 2 cm
    *   **0.0:** ≥ 10 cm
> [!NOTE]
> **Why Linear?** In the macro range (2cm - 10cm), every centimeter closer allows for significantly more magnification. While magnification itself is non-linear, a linear scoring penalty for every centimeter lost is a fair and intuitive way to grade the "closeness" capability.

**4.7.3 Dedicated Macro Lens (Penalty-aware)**
*   *Why it matters:* Dedicated lenses can be useful but are often low-quality gimmicks. We cap the score at 6.0 to ensure they never outperform a high-quality AF Ultrawide (Score 10).
*   **Measurement:** Sensor Resolution (MP).
*   *Formula:* `Score = clamp(MP, 0, 6)`
    *   **Max Score (6.0):** ≥ 6 MP (Decent utility)
    *   **Mid Score (2.0):** 2 MP (Basic/Gimmick)
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
*   **Measurement:** Maximum FPS at ≥1080p.
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
| Score  | Video HDR Capability                   |
| :----- | :------------------------------------- |
| **10** | **Dolby Vision or HDR10+ (10-bit)**    |
| **8**  | **HDR10 / HLG**                        |
| **6**  | **Extended SDR (flat / log-like SDR)** |
| **4**  | **Standard SDR**                       |
| **0**  | **No HDR support**                     |

### 🔹 4.11 Video Encoding & Professional Profiles
*Description:* Support for professional codecs and recording profiles enabling advanced post-production.
*   **Measurement:** Supported codecs and profiles.
*   **Unit:** Codec / Profile Tier
*   **Significance:** Professional codecs preserve detail, reduce compression artifacts, and allow color grading.
| Score    | Encoding Capability                                     |
| :------- | :------------------------------------------------------ |
| **10.0** | **Log profile + Pro codec (ProRes / RAW / equivalent)** |
| **8.0**  | **Log profile (10-bit HEVC / H.265)**                   |
| **6.0**  | **High-bitrate standard codec**                         |
| **4.0**  | **Standard consumer codec**                             |
| **2.0**  | **Legacy codec**                                        |
| **0**    | **Highly compressed**                                   |

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
> **Why this distinction?** Fixed-focus cameras rely on depth of field (DOF). Older or poorly designed selfie cameras with large sensors and fast apertures produce shallow DOF, causing frequent misfocus. Modern designs either add AF or intentionally limit DOF to maintain usability.

### 🔹 4.15 Front Camera Video Performance
*Description:* Maximum video capture capability of the front-facing camera, quantifying resolution, frame rate, and dynamic range.
*   **Measurement:** Max resolution, FPS, and HDR capability.
*   **Unit:** Composite Score (0-10)
*   **Significance:** Critical for vlogging, video calls, and content creation.
*Formula:* `Score = (0.4 * ResScore) + (0.35 * FPSScore) + (0.25 * DRScore)`

**4.15.1 Video Resolution Score**
*   *Formula:* `ResScore = 10 * (log(px) - log(1280)) / (log(3840) - log(1280))` (Clamped 0-10)
    *   **Max Score (10.0):** 4K (3840px long edge)
    *   **Min Score (0.0):** 720p (1280px long edge)
    *   **Anchors:** 1080p ≈ 3.3

**4.15.2 Video Frame Rate Score**
*   *Formula:* `FPSScore = 10 * (log(FPS) - log(24)) / (log(60) - log(24))` (Clamped 0-10)
    *   **Max Score (10.0):** 60 FPS
    *   **Min Score (0.0):** 24 FPS
    *   **Anchors:** 30 FPS ≈ 2.6

**4.15.3 Dynamic Range & Codec Score**
| Score    | Video Capability                         |
| :------- | :----------------------------------------|
| **10.0** | **Log profile or Dolby Vision / ProRes** |
| **9.0**  | **Log profile or Dolby Vision**          |
| **7.0**  | **HDR10 / HDR10+**                       |
| **4.0**  | **Basic HDR (HLG / vendor HDR)**         |
| **1.0**  | **SDR only (8-bit, Rec.709)**            |
| **0.0**  | **No front camera**                      |


### D. Computational Photography & AI

### 🔹 4.16 Computational Photography & AI
*Description:* Use of multiple frames to improve image quality (noise reduction, HDR).
*   **Measurement:** Presence of HDR and Night multi-frame processing.
*   **Unit:** Feature Tier
*   **Significance:** Multi-frame stacking significantly improves low-light and dynamic range.
| Score    | Multi-Frame Capability            |
| :------- | :-------------------------------- |
| **10.0** | **Advanced HDR + Night stacking** |
| **6.0**  | **Basic HDR**                     |
| **0.0**  | **None**                          |

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

### 🔹 5.1 Battery Capacity

> [!IMPORTANT]
> **Battery scoring uses a dedicated comprehensive model.**
> 
> See [battery_scoring_model.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/battery_scoring_model.md) for the complete methodology.

**Summary:** Battery performance is scored using a sophisticated **Benchmark-First Approach with Predictive Interpolation** (Model v3.2) that:

1. **Prioritizes Real-World Data:** Uses actual battery test results from GSMArena and PhoneArena when available
2. **Technical Prediction:** Calculates a predicted score based on:
   - **Energy (45%):** Battery capacity in Watt-hours (accounting for voltage)
   - **Hardware Efficiency (35%):** SoC process node, display technology, connectivity, thermal management, charging stress
   - **Software Optimization (20%):** OS efficiency and bloatware impact
3. **Intelligent Interpolation:** For devices without benchmark data, finds "nearest neighbor" phones with similar specs and interpolates their real-world performance
*   **Measurement:** Standardized battery life tests (or predictive model).
*   **Unit:** Watt-hours (Wh) / Benchmark Score
*   **Significance:** Determines how long the phone lasts on a single charge.

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
*   **Min Score (0.0):** ≤ 7.5W (Standard Qi)
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
*Description:* Evaluates the hardware design and acoustic potential of the built-in speakers. Focuses on speaker count, channel balance, and enclosure design — not subjective "sound taste".
*   **Measurement:** Speaker count & placement, channel symmetry, presence of dedicated bass chamber, peak loudness measurements (when available).
*   **Unit:** Hardware Configuration Index (0-10)
*   **Significance:** Directly impacts media consumption, gaming immersion, and call loudness without headphones.

| Score    | Speaker Configuration                                  | Example Models                 |
| :------- | :----------------------------------------------------- | :----------------------------- |
| **10.0** | **Dual front-facing speakers + dedicated bass chamber**| ROG Phone 8, Black Shark 5 Pro |
| **8.5**  | **Symmetrical stereo (top + bottom), tuned enclosure** | iPhone 15 Pro Max, S24 Ultra   |
| **7.0**  | **Stereo using earpiece + bottom speaker**             | Pixel 8, Galaxy A55            |
| **5.0**  | **Asymmetrical stereo (weak earpiece channel)**        | Budget Mid-range               |
| **3.0**  | **Single bottom-firing speaker**                       | Entry Level                    |
| **1.0**  | **Single low-power speaker (muffled / low SPL)**       | Feature phones                 |
| **0.0**  | **No usable external speaker**                         | Obsolete/damaged devices       |

### 🔹 8.2 Wired Audio Capability
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

### 🔹 8.3 Microphone & Audio Recording (MAR)
*Description:* Evaluates the audio capture capability of the device using only publicly verifiable data, without subjective quality judgments. This is a composite score based on hardware count, recording channels, and advanced features.
*   **Measurement:** Microphone count, recording channels/modes, documented audio features.
*   **Unit:** Composite Index (0-10)
*   **Significance:** Determines audio capture quality for calls, videos, and content creation.

**Structure:**
MAR is a weighted composite of three subsections:
- **8.3.1 Microphone Hardware Count (MHC)** — 30% weight
- **8.3.2 Recording Channels & Modes (RCM)** — 30% weight
- **8.3.3 Advanced Capture Features (ACF)** — 40% weight

*Formula:* `MAR = (0.30 × MHC) + (0.30 × RCM) + (0.40 × ACF)`

---

#### 8.3.1 Microphone Hardware Count (MHC)
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

#### 8.3.2 Recording Channels & Modes (RCM)
*What it measures:* How many audio channels the phone can record and in which modes.
*Why it matters:* Stereo recording dramatically improves realism; multi-channel enables spatial audio and post-processing.

| Score    | Recording Capability                  |
| :------- | :------------------------------------ |
| **10.0** | **Multi-channel / spatial audio**     |
| **8.0**  | **Stereo audio recording**            |
| **5.0**  | **Mono recording**                    |
| **0.0**  | **Voice-only / unclear**              |

---

#### 8.3.3 Advanced Capture Features (ACF)
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

---


### 🔹 8.4 Advanced Audio Features
*Description:* Software enhancements for playback. Spatial Audio and Dolby Atmos create a 3D soundstage from supported content.
*   **Measurement:** Software support check.
*   **Unit:** Feature Suite
*   **Significance:** Enhances immersion in movies and games.
| Score    | Features                       | Example Models         |
| :------- | :----------------------------- | :--------------------- |
| **10.0** | **Spatial Audio + Head Track** | iPhone 15, Pixel 8 Pro |
| **8.0**  | **Dolby Atmos / DTS:X**        | S24 Ultra, Xiaomi 13T  |
| **5.0**  | **Basic EQ / Presets**         | Budget Androids        |
| **2.0**  | **None**                       | Basic Phones           |


## 🟣 9. Financial & Economic Value

### 🔹 9.1 Price
*Description:* The current market price in USD. Lower prices mean better accessibility for more people.
*   **Measurement:** MSRP at launch or current average market price.
*   **Unit:** USD ($)
*   **Significance:** Primary barrier to entry and value determinant.
*Formula:* `Score = 10 - 10 * (log(Price) - log(100)) / (log(1600) - log(100))` (Clamped 0-10)
*   **Max Score (10.0):** ≤ $100
*   **Min Score (0.0):** ≥ $1600
> [!NOTE]
> **Why Logarithmic?** Price sensitivity is relative. A $50 increase on a $150 phone is a massive 33% hike, whereas a $50 increase on a $1000 phone is a negligible 5%. The logarithmic scale reflects this relative impact on affordability.

### 🔹 9.2 Repairability
*Description:* How easy it is to fix. High scores mean you (or a shop) can easily replace a battery or screen, extending the phone's life.
*   **Measurement:** Official iFixit teardown score (or equivalent).
*   **Unit:** iFixit Score (0-10)
*   **Significance:** Determines serviceability and long-term ownership viability.
*Formula:* `Score = iFixit_Score` (Direct mapping)
*   **Max Score (10.0):** iFixit 10
*   **Min Score (0.0):** iFixit 0
> [!NOTE]
> This is a continuous linear scoring metric directly mapped to the industry-standard iFixit score.

### 🔹 9.3 Warranty Length
*Description:* Manufacturer's standard warranty period. Longer warranties indicate manufacturer confidence and provide financial protection.
*   **Measurement:** Manufacturer policy commitment.
*   **Unit:** Months
*   **Significance:** Financial protection against defects and accidents.
| Score    | Warranty Period                  | Example Models            |
| :------- | :------------------------------- | :------------------------ |
| **10.0** | **≥ 60 Months (5 Years)**        | Fairphone 5               |
| **8.0**  | **36 Months (3 Years)**          | Enterprise Editions       |
| **6.0**  | **24 Months (2 Years)**          | EU Standard               |
| **4.0**  | **12 Months (1 Year)**           | US Standard               |
| **0.0**  | **0 Months**                     | Grey Market / Used        |

## 🟣 10. Reviews & Performance Boosters
*Description:* Adjustments based on real-world expert reviews. Technical specs don't always tell the whole story; reviews validate actual performance.
*   **Measurement:** Expert review consensus.
*   **Unit:** Multiplier (Booster)
*   **Significance:** Validates theoretical performance against real-world experience.
*   **Booster > 1.0:** Increases score (e.g., 1.05 = +5%). Used when a device outperforms its specs (e.g., great software optimization).
*   **Booster < 1.0:** Reduces score (e.g., 0.90 = -10%). Used when a device underperforms (e.g., overheating, bugs).

### 🔹 10.1 DXOMARK Camera
*   **Url:** https://www.dxomark.com/
*   **Description:** Top-tier camera score
*   **Impacted Section:** 4.1 - 4.9 Camera
*   **Booster:** **1.05**
*   **Justification:** Validates real-world image quality beyond just sensor size.

### � 10.2 GSM Arena Battery
*   **Url:** https://www.gsmarena.com/battery-test.php3
*   **Description:** Exceptional endurance rating
*   **Impacted Section:** 5.1 Battery
*   **Booster:** **1.10**
*   **Justification:** Confirms software optimization beats raw mAh capacity.

### � 10.3 JerryRigEverything
*   **Url:** https://www.youtube.com/@JerryRigEverything
*   **Description:** Failed durability test
*   **Impacted Section:** 1.2 Durability
*   **Booster:** **0.50**
*   **Justification:** Structural failure (snapping) overrides theoretical IP rating.

### � 10.4 User Reports
*   **Url:** https://www.reddit.com/r/Android/
*   **Description:** Widespread overheating
*   **Impacted Section:** 3.5 Thermal
*   **Booster:** **0.80**
*   **Justification:** Real-world throttling issues not caught in short benchmarks.


## 🟣 11. Miscellaneous

### 🔹 11.1 Haptics Quality
*Description:* Vibration quality. Good haptics feel like crisp clicks (premium), while bad ones feel like a buzzy rattle (cheap).
*   **Measurement:** Teardown / Tactile evaluation.
*   **Unit:** Motor Type
*   **Significance:** Affects typing experience and notification quality.
| Score    | Motor Type                | Example Models              |
| :------- | :------------------------ | :-------------------------- |
| **10.0** | **X-Axis Linear (Large)** | iPhone (Taptic), OnePlus 12 |
| **8.0**  | **X-Axis Linear (Std)**   | S24, Pixel 8                |
| **6.0**  | **Z-Axis Linear**         | Galaxy A55                  |
| **4.0**  | **Coin/ERM Motor**        | Budget Phones               |
| **1.0**  | **None / Broken**         | -                           |

### 🔹 11.2 Sustainability
*Description:* Eco-friendliness. Using recycled materials and plastic-free packaging reduces the device's environmental footprint.
*   **Measurement:** Materials analysis and packaging audit.
*   **Unit:** Qualitative (Eco-Score)
*   **Significance:** Reduces environmental impact.
| Score    | Effort                           | Example Models           |
| :------- | :------------------------------- | :----------------------- |
| **10.0** | **Fairphone Level (Modular)**    | Fairphone 5              |
| **9.0**  | **High Recycled % + No Plastic** | Apple, Samsung Flagships |
| **5.0**  | **Standard Packaging**           | Most Chinese OEMs        |
| **2.0**  | **No Effort**                    | -                        |

### 🔹 11.3 Stylus Support
*Description:* Precision input method. Integrated styluses offer the best experience for note-taking and drawing, while external support is a good bonus.
*   **Measurement:** Hardware check.
*   **Unit:** Feature Presence / Latency
*   **Significance:** Enhances productivity and creativity.
| Score    | Support Level                     | Example Models                  |
| :------- | :-------------------------------- | :------------------------------ |
| **10.0** | **Integrated (BT + Low Latency)** | S24 Ultra                       |
| **8.0**  | **Integrated (Standard)**         | Moto G Stylus                   |
| **5.0**  | **External Support (Active)**     | Z Fold 5, Xiaomi Mix Fold       |
| **2.0**  | **No Dedicated Support**          | iPhone, Pixel, Standard Android |
