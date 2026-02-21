# Smartphone Battery Endurance Score Model v3.2
**Benchmark-First Approach with Predictive Interpolation**

> [!NOTE]
> This model provides the detailed methodology for **Subsection 5.1: Battery Endurance Score** of the [scoring_rules.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_rules.md).

## Overview
This model provides a comprehensive method to evaluate smartphone battery life by prioritizing **real-world performance data** over theoretical specifications.

The scoring philosophy is built on two pillars:
1.  **Primary Truth (Real-World Benchmarks):** When available, real-world benchmark results from trusted sources (GSMArena and PhoneArena) are used as the absolute truth. These tests capture the complex interplay of hardware, software, and usage patterns that raw specs cannot fully predict.
2.  **Secondary Truth (Predictive Interpolation):** When benchmark data is missing (e.g., for unreleased, niche, or older devices), we do not simply guess. Instead, we use a detailed **Technical Predictive Model** (based on Energy, Hardware Efficiency, and Software Optimization) to identify "Nearest Neighbor" devices—phones with very similar technical profiles that *do* have benchmark scores. We then interpolate the missing phone's score based on how these similar devices perform in the real world.

This approach ensures that widely tested phones have accurate, proven scores, while untested phones get highly educated estimates grounded in reality rather than just theoretical math.

---

## 🧮 5.1 Battery Endurance Score Calculations

#### Method A: Benchmark Validation (Primary)
*Description:* This is the preferred method when real-world benchmark data is available from trusted sources. Normalization translates hours into a 0-10 score.

**1. Benchmark Sources & Normalization**

*   **GSMArena Active Use Score (v2.0)**
    *   **Source:** [GSMArena Battery Tests v2.0](https://www.gsmarena.com/battery-test-v2.php3)
    *   **Metric:** Active Use Score (Hours)
    *   **Formula:** `GSM_Score = 10 * (Hours - Battery_GSMArena_Hours_Min) / (Battery_GSMArena_Hours_Max - Battery_GSMArena_Hours_Min)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_GSMArena_Hours_Max
    *   **Min Score (0.0):** ≤ Battery_GSMArena_Hours_Min
    *   *Constants: See [scoring_constants.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_constants.md) Section 5.1*

*   **PhoneArena Battery Life Estimate**
    *   **Source:** [PhoneArena Benchmarks](https://www.phonearena.com/phones/benchmarks/battery)
    *   **Metric:** "Battery Life Estimate" (Hours)
    *   **Formula:** `PA_Score = 10 * (Hours - Battery_PhoneArena_Hours_Min) / (Battery_PhoneArena_Hours_Max - Battery_PhoneArena_Hours_Min)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_PhoneArena_Hours_Max
    *   **Min Score (0.0):** ≤ Battery_PhoneArena_Hours_Min
    *   *Constants: See [scoring_constants.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_constants.md) Section 5.1*

**2. Scoring Logic (Data Availability)**

*   **Condition 1: Both Benchmarks Available**
    *   If the Target Phone has scores from **both** GSMArena and PhoneArena, take the average of the two normalized benchmark scores. The predictive model is ignored.
    *   **Formula:** `Final_Score = (GSM_Score + PA_Score) / 2`
    *   *Example:* Galaxy S24 Ultra. GSMArena: 16.75h -> GSM_Score = 5.84. PhoneArena: 10.5h -> PA_Score = 8.82. Final Score: `(5.84 + 8.82) / 2 = 7.33`

*   **Condition 2: Partial Data (One Benchmark Available)**
    *   If the Target Phone has a score from **only one** source (e.g., GSMArena), use the single available normalized benchmark score.
    *   **Formula:** `Final_Score = Available_Benchmark_Score`
    *   *Example:* Xiaomi 14 Pro. GSMArena: 14.17h -> GSM_Score = 4.16. PhoneArena: N/A. Final Score: `4.16`


#### Method B: Nearest Neighbor Interpolation (Secondary)
*Description:* Used if the specific device has no benchmark data (e.g., unreleased or niche phone), but we have data for other devices to inform a predicted score.

**1. Calculate Sub-Layer Scores**
Calculate the 3 sub-layer scores for the Target Phone via Method C:
*   `Layer A` (Energy Score)
*   `Layer B` (Hardware Efficiency Score - HEI)
*   `Layer C` (Software Optimization Score - SOI)

**2. Identify Neighbors via Feature Distance (Minimum Variance)**
Find **3 Reference Phones** that have **BOTH** GSMArena and PhoneArena scores (Condition 1 phones) and the smallest **Weighted Euclidean Distance** to the Target Phone:
*   **Distance Metric:** Weighted Euclidean Distance.
    *   `Distance = Sqrt( 0.45*(Diff_LayerA)^2 + 0.35*(Diff_LayerB)^2 + 0.20*(Diff_LayerC)^2 )`
    *   *Where Diff_LayerX = LayerX_Target - LayerX_Neighbor*
*   **Scientific Rationale:** Battery life is a complex trade-off between Capacity (Layer A), Efficiency (Layer B), and Optimization (Layer C). A "Huge Battery / Inefficient" phone (A=10, B=2) can have the same Overall Predicted Score as a "Small Battery / Efficient" phone (A=2, B=10). Weighting the sub-layers ensures we compare "apples to apples" by finding neighbors with similar *profiles*, which is scientifically superior for predicting nonlinear behavior (like thermal throttling or standby drain).
*   **Selection:** Pick the 3 neighbors with the smallest `Distance`.

**3. Calculate Correction Ratio:**
*   `Avg_Predicted_Neighbors = (Predicted_Neighbor1 + Predicted_Neighbor2 + Predicted_Neighbor3) / 3`
    *   *Note:* `Predicted_Neighbor1/2/3` refers to the **overall Predicted Score** (Method C) of each neighbor device.
*   `Correction_Ratio = Predicted_Target / Avg_Predicted_Neighbors`
    *   *Note:* `Predicted_Target` is the **overall Predicted Score** (Method C) of the target device.

**4. Apply to Benchmark:**
*   `Avg_Benchmark_Neighbors = (Benchmark_Neighbor1 + Benchmark_Neighbor2 + Benchmark_Neighbor3) / 3`
*   `Final_Score = Correction_Ratio * Avg_Benchmark_Neighbors`

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
>     *   `Final_Score = 0.9988 * 7.20 = 7.19`


#### Method C: Predicted Calculation (Tertiary)
*Description:* This section defines the technical scoring logic used to characterize a device's hardware and software profile. It is used to calculate a "Predicted Score" which serves as the coordinate system for finding "Nearest Neighbors" in Method B.

**Step 1: Calculate Layer A (Battery Energy - 45%)**

*Why it matters:* Battery life is fundamentally bounded by the total amount of energy stored. No matter how efficient a phone is, it cannot run without fuel. We calculate the total energy in Watt-hours (Wh) because it accounts for voltage differences, providing a more accurate measure of true capacity than milliamp-hours (mAh) alone.

*   **Data Structure Mapping:** `5_1_battery_endurance.layer_a_energy.wh`, `5_battery_and_charging.mah`, `5_battery_and_charging.battery_voltage_v`, and `5_battery_and_charging.battery_cell_configuration` (for dual-cell detection)

*Voltage Detection Logic:*
Modern smartphones use either single-cell or dual-cell battery configurations:
1. **Single-Cell (Standard):** One lithium-ion cell at **3.85V nominal**
   - Used in most phones with charging ≤ 100W
   - Lower current, simpler charging circuitry

2. **Dual-Cell (High-Power Charging):** Two cells in series at **7.7V nominal** (2 × 3.85V)
   - Required for ultra-fast charging (≥120W) to reduce current and heat
   - Example: iQOO phones with 120W charging use 3500mAh @ 7.7V (equivalent to 7000mAh @ 3.85V)
   - Manufacturers typically report PER-CELL capacity, not equivalent capacity

*Detection Priority:*
1. **Explicit Voltage:** If `battery_voltage_v` contains a numeric value → use that value
2. **Dual-Cell Indicators:** If `battery_cell_configuration` contains "Dual-cell", "Dual cell", "2S", or "dual-cell" (case-insensitive) → use **7.7V**
3. **High-Power Charging Heuristic:** If wired charging watts ≥ 120W → use **7.7V** (almost all ≥120W phones use dual-cell)
4. **Default Fallback:** Otherwise → use **3.85V** (single-cell standard)

*   **Formula:** `Wh = (mAh × V) / 1000` (Use explicit Wh if provided, otherwise calculate)
*   **Formula:** `Energy_Score = 10 * (Wh - Battery_Energy_Wh_Min) / (Battery_Energy_Wh_Max - Battery_Energy_Wh_Min)` (Clamped 0-10)
    *   **Max Score (10.0):** ≥ Battery_Energy_Wh_Max
    *   **Min Score (0.0):** ≤ Battery_Energy_Wh_Min
    *   *Constants: See [scoring_constants.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_constants.md) Section 5.1*

> [!NOTE]
> **Why Linear?** Battery energy storage scales linearly with capacity. A 20 Wh battery stores exactly twice as much energy as a 10 Wh battery, providing proportionally longer runtime. There are no diminishing returns in energy storage - more Watt-hours directly translates to more battery life.
> **Why 7.7V for dual-cell?** High-power charging generates significant heat. By using two cells in series, current is halved for the same power, reducing resistive heating and enabling safer fast charging without overheating.

**Step 2: Calculate Layer B (Baseline Energy Demand - 35%)**
*Description:* This layer evaluates how efficiently the phone's hardware converts stored energy into baseline usage (Baseline Energy Demand).

> [!NOTE]
> **The Peak vs. Baseline Demand Paradox:** 
> Why does a flagship CPU (like Snapdragon 8 Gen 3) receive a low Cooling Bonus in the **Thermal Dissipation Model (Section 3.4)**, but a high Efficiency Bonus here in the **Battery Model**? 
> *   **Thermals (Peak Demand):** Section 3.4 measures *Peak Thermal Demand*. Under maximum load in a benchmark, a flagship CPU draws massive wattage (~15W) and generates intense heat, demanding heavy cooling compensation. 
> *   **Battery (Baseline Demand):** Battery life is dominated by *Baseline Energy Demand* (mixed use, standby, video playback). The same flagship CPU's advanced architecture (high IPC) completes these light tasks instantly and "races-to-sleep," drawing significantly less power than an older, inefficient CPU. 
> Therefore, high-end architecture is a *penalty* for peak thermals, but a *massive bonus* for baseline battery efficiency.

*   **B.1 SoC Efficiency (40% of Layer B)**
    *   **B.1.1 Process Node (50% of SoC)**
        *   *Why it matters:* Process node (nm) is the biggest determinant of a chip's power efficiency. Smaller transistors require less voltage to switch. Foundry differences are also critical (e.g., TSMC vs Samsung).
        *   *Data Mapping:* `3_4_efficiency_node.process_nm` and `3_4_efficiency_node.foundry`
        *   *Formula:* Score calculated via **[scoring_rules.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_rules.md) Section 3.4** (Unified formula).

    *   **B.1.2 CPU Architecture Class (30% of SoC)**
        *   *Why it matters:* Efficiency cores (e.g., A520) handle 80% of daily tasks. We use the Architecture Efficiency Score (AES) to evaluate the weighted average efficiency of the entire CPU cluster, accurately predicting idle/low-load power.
        *   *Formula:* `Sum(Core_Score * Core_Count) / Total_Core_Count`
            *   *Range is 0-10.*
        *   *Reference:* Standard Core Scores from **Section 3.1.0**.

        > [!NOTE]
        > **Why Linear and Unadjusted for Frequency?** 
        > 1. **Why Linear? (Work vs. Speed):** Benchmarks measure **Speed** (Clock Frequency), which scales power quadratically ($P \propto V^2 \times f$). High benchmark scores often mean high power drain, not efficiency. AES measures **Work-per-Clock** (IPC), which scales performance linearly without the voltage penalty. The architectural baseline quality of the cores across generations scales approximately linearly in its ability to offer proportionately better work-per-watt efficiency at baseline loads.
        > 2. **Why No Frequency Adjustment? (The "Efficiency Core" Reality):** While peak clock frequency dramatically increases maximum power draw (which hurts performance/watt at peak load), battery endurance tests primarily simulate mixed-use, video playback, and standby scenarios. In these scenarios, the CPU spends the vast majority of its time in deep sleep or running at low-power clock domains. Battery life is dominated by the efficiency cores (e.g., Cortex-A520/A55) that handle 80% of daily background tasks. Therefore, the *intrinsic architectural efficiency* (IPC) of the cluster matters far more for predicting whole-day endurance than the chip's theoretical maximum speed limit. AES is the *only* metric that accounts for the generational quality of the efficiency cores, accurately predicting the device's idle/low-load power profile. Peak power penalties are handled naturally during active high-load benchmarking (Method A) or indirectly through thermal bleeding, not at the baseline calculation step.

    *   **B.1.3 GPU Architecture Class (20% of SoC)**
        *   *Why it matters:* Similar to CPUs, newer GPU architectures deliver higher performance per watt.
        *   *Reference:* **Efficiency Score** column from **Section 3.3.0**.
            *   *Note:* The scoring table is defined in Section 3.3.0. For battery calculations, we use the specific **Efficiency Score** which decouples raw performance from power draw (e.g., penalizing hot chips like Snapdragon 888). This score measures performance-per-watt rather than peak capability.
        
        > [!NOTE]
        > **Avoid Double Counting:** Process node benefits (e.g., 5nm vs 3nm) are handled in the **SoC Efficiency Score (Section 3.4)**, which is used in **Section B.1.1**. This GPU Efficiency Score focuses on the **architectural efficiency** and thermal stability of the GPU implementation itself, regardless of the node. Ideally, an efficient architecture on an efficient node gets high scores in both. A "hot" architecture on an efficient node would get a lower GPU score despite the good node score.
    *   `SoC_Efficiency = (0.50 × Node) + (0.30 × CPU) + (0.20 × GPU)`

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

    *   `Display_Efficiency = (0.35 × Panel_Tech) + (0.35 × Refresh) + (0.30 × Resolution)`

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
        > **Why Inverted Scoring?** Newer cellular generations (5G) require more complex modems with higher power consumption than older standards (4G, 3G). While 5G provides faster speeds, it comes at a battery efficiency cost. This inverted scoring reflects the bare power penalty. See Section 7.1 of scoring_rules.md for feature-based scoring (where newer = better).

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
        > **Why Inverted Scoring?** Newer WiFi standards (WiFi 6E, 7) use wider channels (160MHz, 320MHz) and higher frequency bands (6GHz) which require more power to maintain. While they provide better performance, they reduce battery efficiency. See Section 7.3 of scoring_rules.md for feature-based scoring.

    *   `Connectivity_Efficiency = (0.70 × Cellular) + (0.30 × WiFi)`

*   **B.4 Thermal Efficiency (10% of Layer B)**
    *   *Why it matters:* Heat increases internal resistance and leakage currents. Good cooling preserves battery efficiency.
    *   *Formula:* `Thermal_Efficiency = TDSI_Score` (From **Section 3.5**)

    > [!NOTE]
    > The **same TDSI score** is used in both contexts because thermal management capability is an objective hardware characteristic. The different impact on performance vs. battery efficiency is handled through **weighting**.

*   **Final Layer B Formula:** `HEI = (0.40 × SoC) + (0.40 × Display) + (0.10 × Connectivity) + (0.10 × Thermal)`

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
    *   *Reference:* Use the System Cleanliness & Control (SCC) score from **Section 6.3**.

*   **Final Layer C Formula:** `SOI = (0.60 × OS_Age) + (0.40 × SCC)`

**Step 4: Calculate Predicted Score**
*   **Formula:** `Predicted_Score = (0.45 × Energy_Score) + (0.35 × HEI) + (0.20 × SOI)`
