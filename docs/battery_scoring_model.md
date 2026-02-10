# Smartphone Battery Endurance Score Model v3.2
**Benchmark-First Approach with Predictive Interpolation**

> [!NOTE]
> This model provides the detailed methodology for **Subsection 5.1: Battery Endurance Score** of the [scoring_rules.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/scoring_rules.md).

## Overview
This model provides a comprehensive method to evaluate smartphone battery life by prioritizing **real-world performance data** over theoretical specifications.

The scoring philosophy is built on two pillars:
1.  **Primary Truth (Real-World Benchmarks):** When available, real-world benchmark results from trusted sources (GSMArena and PhoneArena) are used as the absolute truth. These tests capture the complex interplay of hardware, software, and usage patterns that raw specs cannot fully predict.
2.  **Secondary Truth (Predictive Interpolation):** When benchmark data is missing (e.g., for unreleased, niche, or older devices), we do not simply guess. Instead, we use a detailed **Technical Predictive Model** (based on Energy, Hardware Efficiency, and Software Optimization) to identify "Nearest Neighbor" devices—phones with very similar technical profiles that *do* have benchmark scores. We then interpolate the missing phone's score based on how these similar devices perform in the real world.

This approach ensures that widely tested phones have accurate, proven scores, while untested phones get highly educated estimates grounded in reality rather than just theoretical math.

---

## 🏗️ PART 1: THE PREDICTIVE MODEL (Internal Engine)
*This section defines the technical scoring logic used to characterize a device's hardware and software profile. It is used to calculate a "Predicted Score" which serves as the coordinate system for finding "Nearest Neighbors" in Part 3.*

### 🔋 Layer A: Battery Energy (45%)

#### A.1 Battery Energy Calculation
**Why this matters:** Battery life is fundamentally bounded by the total amount of energy stored. No matter how efficient a phone is, it cannot run without fuel. We calculate the total energy in Watt-hours (Wh) because it accounts for voltage differences, providing a more accurate measure of true capacity than milliamp-hours (mAh) alone.

**Data Structure Mapping:** `5_1_battery_endurance.layer_a_energy.wh`, `5_battery_and_charging.mah`, `5_battery_and_charging.battery_voltage_v`, and `5_battery_and_charging.battery_cell_configuration` (for dual-cell detection)

**Voltage Detection Logic:**

Modern smartphones use either single-cell or dual-cell battery configurations:

1. **Single-Cell (Standard):** One lithium-ion cell at **3.85V nominal**
   - Used in most phones with charging ≤ 100W
   - Lower current, simpler charging circuitry

2. **Dual-Cell (High-Power Charging):** Two cells in series at **7.7V nominal** (2 × 3.85V)
   - Required for ultra-fast charging (≥120W) to reduce current and heat
   - Example: iQOO phones with 120W charging use 3500mAh @ 7.7V (equivalent to 7000mAh @ 3.85V)
   - Manufacturers typically report PER-CELL capacity, not equivalent capacity

**Detection Priority:**

1. **Explicit Voltage:** If `battery_voltage_v` contains a numeric value → use that value
2. **Dual-Cell Indicators:** If battery_cell_configuration contains "Dual-cell", "Dual cell", "2S", or "dual-cell" (case-insensitive) → use **7.7V**
3. **High-Power Charging Heuristic:** If wired charging watts ≥ 120W → use **7.7V** (almost all ≥120W phones use dual-cell)
4. **Default Fallback:** Otherwise → use **3.85V** (single-cell standard)

**Formula:**
```
// Priority: Explicit Wh > Calculated Wh
IF wh_value is numeric:
    Wh = wh_value
ELSE:
    // Detect voltage
    IF battery_voltage_v is numeric:
        V = battery_voltage_v
    ELSE IF battery_cell_configuration contains "dual-cell" OR "2S" (case-insensitive):
        V = 7.7
    ELSE IF wired_charging_watts >= 120:
        V = 7.7
    ELSE:
        V = 3.85
    
    Wh = (mAh × V) / 1000

Energy_Score = 10 * (Wh − 8) / (25 − 8)
Energy_Score = clamp(Energy_Score, 0, 10)
```

**Scoring Range:**
- **Max Score (10) at:** ≥ 25 Wh (e.g., ~6500mAh @ 3.85V OR ~3250mAh @ 7.7V)
- **Min Score (0) at:** ≤ 8 Wh (e.g., ~2000mAh @ 3.85V OR ~1040mAh @ 7.7V)

> [!NOTE]
> **Why Linear?** Battery energy storage scales linearly with capacity. A 20 Wh battery stores exactly twice as much energy as a 10 Wh battery, providing proportionally longer runtime. There are no diminishing returns in energy storage - more Watt-hours directly translates to more battery life.

> [!NOTE]
> **Why 7.7V for dual-cell?** High-power charging (≥120W) generates significant heat. By using two cells in series (7.7V), the current is halved for the same power (P = V × I), dramatically reducing resistive heating (P_loss = I² × R). This enables faster, safer charging without overheating.


### ⚙️ Layer B: Hardware Efficiency Index (HEI) (35%)
*This layer evaluates how efficiently the phone's hardware converts stored energy into actual usage.*

#### B.1 SoC Efficiency (40% of HEI)

**B.1.1 Process Node (50% of SoC)**

**Why this matters:** The manufacturing process node (measured in nanometers) is the single biggest determinant of a chip's power efficiency. Smaller transistors require less voltage to switch, reducing dynamic power consumption. Foundry differences are also critical—TSMC nodes deliver 20-30% better power efficiency than Samsung at the same node label.

**Data Structure Mapping:** `3_4_efficiency_node.process_nm` and `3_4_efficiency_node.foundry`

**Formula:** **See Section 3.4 of scoring_rules.md** (Unified formula - single source of truth)

The process node scoring formula, including logarithmic calculation and foundry modifiers, is defined in Section 3.4 (Efficiency - Process Node) and is used identically here.

> [!NOTE]
> **Unified Formula Justification:** This formula is identical to Section 3.4 because process node efficiency affects both performance AND power consumption.

**B.1.2 CPU Architecture Class (30% of SoC)**

**Why this matters:** A smartphone's CPU is a heterogeneous mix of "Prime", "Performance", and "Efficiency" cores. Scrutinizing only the strongest core (as done in performance benchmarks) is misleading for battery life. Efficiency cores (like Cortex-A520/A55) handle 80% of daily tasks (background sync, audio playback, idling). A chip with modern efficiency cores will significantly outlast one with older efficiency cores, even if they share the same prime core. To accurately predict battery impact, we must evaluate the **weighted average efficiency** of the entire CPU cluster.

**Data Structure Mapping:** `5_1_battery_endurance.layer_b_hardware_efficiency.b_1_soc_efficiency.breakdown.cpu_architecture_score_aes` (calculated from `3_processing_power_and_performance.3_0_cpu_architecture_reference`)

**Scoring Method:**
**Architecture Efficiency Score (AES)**

*   *What is it?* The average quality of the cores, used as a key predictor for battery life.
*   **Formula:** `Sum(Core_Score * Core_Count) / Total_Core_Count`
    *   *Range is 0-10.*
    *   **Core Scores:** See [scoring_rules.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/scoring_rules.md) Section 3.0 for authoritative core scores.

> [!NOTE]
> **Why Weighted Average?** 
1.  **Work vs. Speed:** Benchmarks measure **Speed** (Clock Frequency), which scales power quadratically ($P \propto V^2 \times f$). High benchmark scores often mean high power drain, not efficiency. AES measures **Work-per-Clock** (IPC), which scales performance linearly without the voltage penalty.
2.  **The "Efficiency Core" Reality:** Battery life is dominated by the efficiency cores (e.g., Cortex-A520/A55) that handle 80% of daily background tasks (standby, audio, sync). Performance benchmarks test only the Prime Core. AES is the *only* metric that accounts for the generational quality of the efficiency cores, accurately predicting the device's idle/low-load power profile.

**B.1.3 GPU Architecture Class (20% of SoC)**

**Why this matters:** Similar to CPUs, newer GPU architectures deliver higher performance per watt.

**Data Structure Mapping:** `3_3_0_gpu_architecture_reference.efficiency_score`

**GPU Scores:** **See Section 3.3.0 of scoring_rules.md** for the authoritative GPU Architecture Reference table (Use the **Efficiency Score** column).

The scoring table is defined in Section 3.3.0. For battery calculations, we use the specific **Efficiency Score** which decouples raw performance from power draw (e.g., penalizing hot chips like Snapdragon 888). This score measures performance-per-watt rather than peak capability.

> [!NOTE]
> **Avoid Double Counting:** Process node benefits (e.g., 5nm vs 3nm) are handled in the **SoC Efficiency Score (Section 3.4)**, which is used in **Section B.1.1**. This GPU Efficiency Score focuses on the **architectural efficiency** and thermal stability of the GPU implementation itself, regardless of the node. Ideally, an efficient architecture on an efficient node gets high scores in both. A "hot" architecture on an efficient node would get a lower GPU score despite the good node score.

**Formula:** `SoC_Efficiency = 0.5 × Process + 0.3 × CPU + 0.2 × GPU`


#### B.2 Display Efficiency (40% of HEI)

**B.2.1 Panel Technology (35% of Display)**

**Why this matters:** This metric captures the **intrinsic power efficiency** of the panel technology itself (pixel emission, backlight efficiency, black-level power draw), **independent of refresh rate**. It answers: *"How much energy does this panel consume to display a static image?"*

**Data Structure Mapping:** `2_1_panel_architecture.value`

**Panel Scores:** **See Section 2.1 of scoring_rules.md** for the authoritative Display Panel Architecture table.

The scoring table is defined in Section 2.1 and is used identically here for battery efficiency calculations. OLED panels are inherently more power-efficient than LCDs because they don't require a backlight and can turn off individual pixels for true black.

**Difference from B.2.2:** This section does NOT reward adaptive refresh rates (like LTPO). That benefit is fully captured in B.2.2. Here, we focus purely on the material and structural efficiency of the screen.


**B.2.2 Refresh Efficiency (35% of Display)**

**Why this matters:** This metric captures the **dynamic power efficiency** related to screen updates. It answers: *"How often does the screen need to redraw, and how smart is it about not redrawing unnecessarily?"*

**Data Structure Mapping:** `2_6_refresh_rate_max_hz`, `2_display.refresh_rate_min_hz`, `2_display.refresh_rate_adaptive`

**Difference from B.2.1:** This is where LTPO panels shine. Their ability to drop to 1Hz is rewarded here via the `effective_refresh` calculation.

**Scoring Range:**
- **Max Score (10) at:** Effective Refresh ≤ 30Hz (e.g., LTPO idling)
- **Min Score (0) at:** Effective Refresh ≥ 165Hz

**Formula:**
```
effective_refresh = adaptive ? (min_hz + max_hz) / 2 : max_hz
Refresh_Score = 10 - 10 * (effective_refresh − 30) / (165 − 30)
Refresh_Score = clamp(Refresh_Score, 0, 10)
```

> [!NOTE]
> **Why Linear?** Display power consumption scales linearly with refresh rate. A 120Hz display uses approximately 2x the power of 60Hz because it updates the screen twice as often. Unlike visual quality (where higher refresh rates have diminishing perceptual returns), power draw is strictly proportional to refresh frequency.

**B.2.3 Resolution Efficiency (30% of Display)**

**Why this matters:** Pushing more pixels requires more GPU power and a brighter backlight (or higher pixel drive) to achieve the same perceived brightness, increasing power consumption.

**Data Structure Mapping:** `2_display.megapixels_mp`

**Scoring Range:**
- **Max Score (10) at:** ≤ 1.0 MP (HD+)
- **Min Score (0) at:** ≥ 8.3 MP (4K)

**Formula:**
```
Resolution_Score = 10 - 10 * (megapixels_mp − 1.0) / (8.3 − 1.0)
Resolution_Score = clamp(Resolution_Score, 0, 10)
```

> [!NOTE]
> **Why Linear?** Power consumption scales roughly linearly with pixel count in the practical phone display range (1MP to 8.3MP). While GPU and display power don't increase perfectly proportionally with megapixels due to modern optimizations (efficient controllers, adaptive backlight scaling), the relationship is close enough to linear that a simple linear formula provides an accurate approximation for battery efficiency scoring.

**Formula:** `Display_Efficiency = 0.35 × Panel + 0.35 × Refresh + 0.30 × Resolution`


#### B.3 Connectivity Efficiency (10% of HEI)

**B.3.1 Cellular Generation (70%)**

**Why this matters:** Newer cellular standards like 5G provide faster speeds but require more complex modems and signal processing, leading to higher power drain compared to simpler 4G or 3G networks.

**Data Structure Mapping:** `7_1_cellular_capabilities.features`

**Scoring Range:**
- **Max Score (10) at:** 2G only (Most efficient)
- **Min Score (0) at:** 5G Sub-6 + mmWave (Least efficient)

**⚠️ INVERTED SCORING (newer = less efficient):**

| Technology                                   | Battery Score |
|----------------------------------------------|---------------|
| **2G Only**                                  | **10**        |
| **3G fallback only**                         | **8**         |
| **4G LTE (Basic)**                           | **6**         |
| **4G LTE-Advanced Pro**                      | **4**         |
| **5G Sub-6 (Limited/regional bands)**        | **2**         |
| **5G Sub-6 (Full Global Bands)**             | **1**         |
| **5G mmWave + Sub-6 (Global band coverage)** | **0**         |

> [!NOTE]
> **Why Inverted Scoring?** Newer cellular generations (5G) require more complex modems with higher power consumption than older standards (4G, 3G). While 5G provides faster speeds, it comes at a battery efficiency cost. This inverted scoring reflects the power penalty of newer cellular technology. See Section 7.1 of scoring_rules.md for feature-based scoring (where newer = better).

**B.3.2 Wi-Fi Generation (30%)**

**Why this matters:** Similar to cellular, newer Wi-Fi standards (Wi-Fi 6E, 7) use wider channels (160MHz, 320MHz) and higher frequency bands (6GHz) which consume more power to maintain than older standards.

**Data Structure Mapping:** `7_3_wifi_standard.value`

**Scoring Range:**
- **Max Score (10) at:** Wi-Fi 3 or older
- **Min Score (0) at:** Wi-Fi 7

**⚠️ INVERTED SCORING (newer = less efficient):**

| Standard     | Battery Score |
|--------------|---------------|
| **Wi-Fi≤3**  | **10**        |
| **Wi-Fi 4**  | **7**         |
| **Wi-Fi 5**  | **5**         |
| **Wi-Fi 6**  | **3**         |
| **Wi-Fi 6E** | **2**         |
| **Wi-Fi 7**  | **0**         |

> [!NOTE]
> **Why Inverted Scoring?** Newer WiFi standards (WiFi 6E, 7) use wider channels (160MHz, 320MHz) and higher frequency bands (6GHz) which require more power to maintain than older standards. While they provide better performance, they reduce battery efficiency. See Section 7.3 of scoring_rules.md for feature-based scoring (where newer = better).

**Formula:** `Connectivity_Efficiency = 0.7 × Cellular + 0.3 × WiFi`


#### B.4 Thermal Efficiency (10% of HEI)

**Why this matters:** Heat is the enemy of efficiency. A hot battery and processor suffer from increased internal resistance and leakage currents. Effective thermal management keeps the device in its optimal thermal window, preserving battery efficiency.

**Scoring:** Use the complete **[Thermal Dissipation & Stability Index (TDSI)](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_rules.md#L540-L602)** from Section 3.5.

> [!NOTE]
> The **same TDSI score** is used in both contexts because thermal management capability is an objective hardware characteristic. The different impact on performance vs. battery efficiency is handled through **weighting**.

**Formula:** `Thermal_Efficiency = TDSI_Score` (from Section 3.5)


**Final HEI Formula:**
```
HEI = 0.40 × SoC + 0.40 × Display + 0.10 × Connectivity + 0.10 × Thermal
```

### 📱 Layer C: Software & Optimization Index (SOI) (20%)
*This layer accounts for the efficiency of the operating system and the impact of pre-installed software.*

#### 🔹 C.1 OS Power Management Architecture (60%)
**Why this matters:** The operating system's kernel and power management framework determine how effectively hardware resources are utilized. Modern OS versions (Android 12+, iOS 15+) act as a neutral baseline for efficiency, introducing standardized features like aggressive background process freezing, precise alarm management, and improved scheduler awareness (e.g., Android's "Performance Class" standards).

**Neutrality Principle:**
This score is determined **strictly by the OS Generation**, not the brand.
*   **Modern Architecture (Score 10):** Features standardized "phantom process" killing, strict background execution limits, and deep hardware integration (e.g., Android 12+, iOS 15+).
*   **Legacy Architecture:** Lacks modern power-saving APIs, leading to higher standby drain.

**Data Structure Mapping:** `6_software_and_longevity.os_version`

**Scoring Table:**

| Score    | OS Generation (Android) | OS Generation (iOS) | Status                |
| :------- | :---------------------- | :------------------ | :-------------------- |
| **10.0** | **Android 14+**         | **iOS 17+**         | Current/Cutting Edge  |
| **9.0**  | **Android 13**          | **iOS 16**          | Recent Modern         |
| **8.0**  | **Android 12**          | **iOS 15**          | Modern Standard       |
| **6.0**  | **Android 10-11**       | **iOS 13-14**       | Legacy Support        |
| **4.0**  | **Android 8-9**         | **iOS 11-12**       | Aging                 |
| **0.0**  | **Android < 8**         | **iOS < 11**        | Obsolete              |


#### C.2 Bloatware Overhead (40%)

**Why this matters:** Bloatware and adware often run hidden background processes that prevent the phone from entering deep sleep, causing "phantom" battery drain even when the phone is not in use.

**Data Structure Mapping:** Directly use SCC score of `6_3_system_cleanliness_control` from the file `scoring_rules.md`  

**Formula:** `SOI = 0.60 × OS_Skin + 0.40 × SCC`


### 📊 Predicted Score Calculation
*This score is used ONLY for finding "Nearest Neighbors" in Case 3.*
```
Predicted_Score = 0.45 × Energy_Score + 0.35 × HEI + 0.20 × SOI
```

## 🏆 PART 2: THE BENCHMARK LAYER
*Normalization of real-world test results into a 0-10 score.*

### 1. GSMArena Active Use Score (v2.0)
**Source:** [GSMArena Battery Tests v2.0](https://www.gsmarena.com/battery-test-v2.php3)

**Metric:** Active Use Score (Hours:Minutes)

**Normalization:**
**Scoring Range:**
- **Max Score (10) at:** ≥ 23:07 hours (23.12h)
- **Min Score (0) at:** ≤ 7:48 hours (7.8h)
- **Formula:**
```
GSM_Score = 10 * (Hours - 7.8) / (23.12 - 7.8)
GSM_Score = clamp(GSM_Score, 0, 10)
```

### 2. PhoneArena Battery Life Estimate
**Source:** [PhoneArena Benchmarks](https://www.phonearena.com/phones/benchmarks/battery)

**Metric:** "Battery Life Estimate" (Composite score)

**Normalization:**
**Scoring Range:**
- **Max Score (10) at:** ≥ 11:25 hours (11.42h)
- **Min Score (0) at:** ≤ 3:36 hours (3.6h)
- **Formula:**
```
PA_Score = 10 * (Hours - 3.6) / (11.42 - 3.6)
PA_Score = clamp(PA_Score, 0, 10)
```

## 🧮 PART 3: SCORING LOGIC (The 3 Cases)

### ✅ CASE 1: Both Benchmarks Available
**Condition:** Target Phone has scores from **both** GSMArena and PhoneArena.

**Method:**
Simply take the average of the two normalized benchmark scores. The predictive model is ignored.

**Formula:**
```
Final_Score = (GSM_Score + PA_Score) / 2
```

**Example:**
- **Target Phone:** Galaxy S24 Ultra
- GSMArena: 16h 45m (16.75h) → `GSM_Score = 10 * (16.75 - 7.8) / (23.12 - 7.8) = 5.84`
- PhoneArena: 10h 30m (10.5h) → `PA_Score = 10 * (10.5 - 3.6) / (11.42 - 3.6) = 8.82`
- **Final Score:** `(5.84 + 8.82) / 2 = 7.33`


### ⚠️ CASE 2: Partial Data (One Benchmark Available)
**Condition:** Target Phone has a score from **only one** source (e.g., GSMArena).

**Method:**
Use the single available normalized benchmark score.

**Formula:**
```
Final_Score = Available_Benchmark_Score
```

**Example:**
- **Target Phone:** Xiaomi 14 Pro (China exclusive)
- GSMArena: 14h 10m (14.17h) → `GSM_Score = 10 * (14.17 - 7.8) / (23.12 - 7.8) = 4.16`
- PhoneArena: N/A
- **Final Score:** `4.16`


### 🔮 CASE 3: Interpolation (No Benchmarks Available)
**Condition:** Target Phone has **NO** benchmark data (e.g., unreleased or niche phone).

**Method:** "Nearest Neighbor" Interpolation
1.  Calculate `Predicted_Target` using the technical model (Part 1).
2.  Find **3 Reference Phones (Neighbor1, Neighbor2, Neighbor3)** that:
    *   Have **BOTH** GSMArena and PhoneArena scores (Case 1 phones).
    *   Have the closest `Predicted_Score` to the Target Phone.
3.  Calculate the **Correction Ratio** between Target's prediction and the neighbors' average prediction.
4.  Apply this ratio to the neighbors' average **Benchmark Score**.

**Step-by-Step Formula:**

1.  **Find Neighbors:** Select Neighbor1, Neighbor2, Neighbor3 having:
    *   a) Scores from **BOTH** GSMArena and PhoneArena benchmarks.
    *   b) Minimizing `|Predicted_Target - Predicted_Neighbor_X|`.
2.  **Calculate Average Prediction of Neighbors:**
    `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
3.  **Calculate Correction Ratio:**
    `Ratio = Predicted_Target / Avg_Predicted_Neighbors`
4.  **Calculate Average Benchmark of Neighbors:**
    `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
5.  **Calculate Final Score:**
    `Final_Score = Ratio * Avg_Benchmark_Neighbors`

**Example:**
- **Target Phone:** "FuturePhone 5" (No benchmarks)
    - `Predicted_Target = 8.5` (High specs, large battery)
- **Neighbors Found (Similar Specs, with Benchmarks):**
    - **Neighbor1:** `Predicted = 8.0`, `Benchmark = 7.2`
    - **Neighbor2:** `Predicted = 8.2`, `Benchmark = 7.4`
    - **Neighbor3:** `Predicted = 7.8`, `Benchmark = 7.0`
- **Calculations:**
    - `Avg_Predicted_Neighbors = (8.0 + 8.2 + 7.8) / 3 = 8.0`
    - `Avg_Benchmark_Neighbors = (7.2 + 7.4 + 7.0) / 3 = 7.2`
    - `Ratio = 8.5 / 8.0 = 1.0625` (Target Phone is predicted to be ~6.25% better than neighbors)
    - `Final_Score = 1.0625 * 7.2 = 7.65`

**Why this works:**
The neighbors generally perform worse in the real world than their raw specs suggest (Avg Bench 7.2 vs Avg Pred 8.0). Even though the Target Phone has a high predicted score of 8.5, we adjust it down to 7.65 to reflect the reality of similar devices, while still rewarding it for having better specs than the neighbors.
