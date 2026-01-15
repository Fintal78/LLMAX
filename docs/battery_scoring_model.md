# Smartphone Battery Performance Scoring Model v3.2
**Benchmark-First Approach with Predictive Interpolation**

> [!NOTE]
> This model provides the detailed methodology for **Subsection 5.1: Battery Capacity** of the [scoring_rules.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/scoring_rules.md).

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

**Data Structure Mapping:** `5_1_battery_capacity.mah` and `5_1_battery_capacity.battery_voltage_v`

**Voltage Handling:**
- If `battery_voltage_v` contains a numeric value: use that value.
- If `battery_voltage_v` = "Not available": use the industry standard default of **3.85V**.

**Formula:**
```
V = battery_voltage_v != "Not available" ? battery_voltage_v : 3.85
Wh = (mAh × Voltage) / 1000
Energy_Score = 10 * (Wh − 8) / (25 − 8)
Energy_Score = clamp(Energy_Score, 0, 10)
```
**Scoring Range:**
- **Max Score (10) at:** ≥ 25 Wh (e.g., ~6500mAh @ 3.85V)
- **Min Score (1) at:** ≤ 8 Wh (e.g., ~2000mAh @ 3.85V)


### ⚙️ Layer B: Hardware Efficiency Index (HEI) (35%)
*This layer evaluates how efficiently the phone's hardware converts stored energy into actual usage.*

#### B.1 SoC Efficiency (35% of HEI)

**B.1.1 Process Node (50% of SoC)**

**Why this matters:** The manufacturing process node (measured in nanometers) is the single biggest determinant of a chip's power efficiency. Smaller transistors require less voltage to switch, reducing dynamic power consumption.

**Data Structure Mapping:** `3_4_efficiency_node.process_nm`

**Scoring Range:**
- **Max Score (10) at:** 3nm (Latest TSMC nodes)
- **Min Score (0) at:** 20nm (Ancient nodes)

**Formula:**
```
Process_Score = 10 - 10 * (nm − 3) / (20 − 3)
Process_Score = clamp(Process_Score, 0, 10)
```

**B.1.2 CPU Architecture Class (30% of SoC)**

**Why this matters:** Newer CPU core designs (like ARM Cortex-X4 or A720) do more work per clock cycle than older ones (like Cortex-A53). This "instructions per clock" (IPC) advantage means they can finish tasks faster and return to sleep sooner, saving energy.

**Data Structure Mapping:** `3_2_cpu_structure.clusters[0].name`

**Scoring Range:**
- **Max Score (10) at:** Cortex-X4 / Apple A17
- **Min Score (0) at:** Cortex-A53

| CPU Core (Prime/Big) | Score |
|----------------------|-------|
| Cortex-X4 / A17 / A18| 10    |
| Cortex-X3            | 9     |
| Cortex-X2            | 8     |
| Cortex-A720 / A715   | 7     |
| Cortex-A78 / A77     | 6     |
| Cortex-A76 / A75     | 5     |
| Cortex-A55           | 2     |
| Cortex-A53 / A7      | 0     |

**B.1.3 GPU Architecture Class (20% of SoC)**

**Why this matters:** Similar to CPUs, newer GPU architectures deliver higher performance per watt.

**Data Structure Mapping:** `3_3_gpu_performance.model`

**Scoring Range:**
- **Max Score (10) at:** Apple GPU / Adreno 750
- **Min Score (0) at:** Mali-G52

| GPU Model            | Score |
|----------------------|-------|
| Apple GPU            | 10    |
| Adreno 750 / 740     | 9     |
| Adreno 730 / G715    | 8     |
| Adreno 660 / G610    | 6     |
| Mali-G57             | 2     |
| Mali-G52             | 0     |

**Formula:** `SoC_Efficiency = 0.5 × Process + 0.3 × CPU + 0.2 × GPU`

<br>

#### B.2 Display Efficiency (35% of HEI)

**B.2.1 Panel Technology (35% of Display)**

**Why this matters:** This metric captures the **intrinsic power efficiency** of the panel technology itself (pixel emission, backlight efficiency, black-level power draw), **independent of refresh rate**. It answers: *"How much energy does this panel consume to display a static image?"*

**Data Structure Mapping:** `2_1_technology.value`

**Difference from B.2.2:** This section does NOT reward adaptive refresh rates (like LTPO). That benefit is fully captured in B.2.2. Here, we focus purely on the material and structural efficiency of the screen.

- **Max Score (10) at:** OLED (Any type, including LTPO/LTPS)
- **Min Score (1) at:** Legacy LCD

| Panel Type             | Score |
|------------------------|-------|
| OLED (incl. LTPO/LTPS) | 10    |
| AMOLED                 | 9     |
| IPS LCD                | 6     |
| TFT / PLS LCD          | 2     |
| Legacy LCD             | 0     |

**B.2.2 Refresh Efficiency (35% of Display)**

**Why this matters:** This metric captures the **dynamic power efficiency** related to screen updates. It answers: *"How often does the screen need to redraw, and how smart is it about not redrawing unnecessarily?"*

**Data Structure Mapping:** `2_6_refresh_rate.max_hz`, `2_6_refresh_rate.min_hz`, `2_6_refresh_rate.adaptive`

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

**B.2.3 Resolution Efficiency (30% of Display)**

**Why this matters:** Pushing more pixels requires more GPU power and a brighter backlight (or higher pixel drive) to achieve the same perceived brightness, increasing power consumption.

**Data Structure Mapping:** `2_2_resolution_density.width_px`, `2_2_resolution_density.height_px`

**Scoring Range:**
- **Max Score (10) at:** ≤ 1.0 MP (HD+)
- **Min Score (0) at:** ≥ 8.3 MP (4K)

**Formula:**
```
pixel_mp = (width × height) / 1,000,000
Resolution_Score = 10 - 10 * (pixel_mp − 1.0) / (8.3 − 1.0)
Resolution_Score = clamp(Resolution_Score, 0, 10)
```

**Formula:** `Display_Efficiency = 0.35 × Panel + 0.35 × Refresh + 0.30 × Resolution`

<br>

#### B.3 Connectivity Efficiency (15% of HEI)

**B.3.1 Cellular Generation (70%)**

**Why this matters:** Newer cellular standards like 5G provide faster speeds but require more complex modems and signal processing, leading to higher power drain compared to simpler 4G or 3G networks.

**Data Structure Mapping:** `7_1_cellular_capabilities.features`

**Scoring Range:**
- **Max Score (10) at:** 2G only (Most efficient)
- **Min Score (0) at:** 5G Sub-6 + mmWave (Least efficient)

**⚠️ INVERTED SCORING (newer = less efficient):**

| Tech      | Score |
|-----------|-------|
| 2G        | 10    |
| 3G        | 8     |
| 4G        | 6     |
| 5G Sub-6  | 4     |
| 5G mmWave | 0     |

**B.3.2 Wi-Fi Generation (30%)**

**Why this matters:** Similar to cellular, newer Wi-Fi standards (Wi-Fi 6E, 7) use wider channels (160MHz, 320MHz) and higher frequency bands (6GHz) which consume more power to maintain than older standards.

**Data Structure Mapping:** `7_3_wifi_standard.value`

**Scoring Range:**
- **Max Score (10) at:** Wi-Fi 4 or older
- **Min Score (0) at:** Wi-Fi 7

**⚠️ INVERTED SCORING (newer = less efficient):**

| Tech     | Score |
|----------|-------|
| Wi-Fi 4  | 10    |
| Wi-Fi 5  | 8     |
| Wi-Fi 6  | 6     |
| Wi-Fi 6E | 4     |
| Wi-Fi 7  | 0     |

**Formula:** `Connectivity_Efficiency = 0.7 × Cellular + 0.3 × WiFi`

<br>

#### B.4 Thermal Efficiency (10% of HEI)

**B.4.1 Cooling System (60%)**

**Why this matters:** Heat is the enemy of efficiency. A hot battery and processor suffer from increased internal resistance and leakage currents. Effective cooling keeps the device in its optimal thermal window.

**Data Structure Mapping:** `3_5_thermal_management.value`

**Scoring Range:**
- **Max Score (10) at:** Active fan
- **Min Score (0) at:** None

| Cooling       | Score |
|---------------|-------|
| Active fan    | 10    |
| Vapor chamber | 8     |
| Heat pipe     | 6     |
| Passive       | 4     |
| None          | 0     |

**B.4.2 Thickness (40%)**

**Why this matters:** Physically thicker phones have more internal volume for heat dissipation and airflow, allowing for better passive cooling than ultra-thin devices.

**Data Structure Mapping:** `1_4_dimensions.thickness_mm`

**Scoring Range:**
- **Max Score (10) at:** ≥ 10mm
- **Min Score (0) at:** ≤ 6mm

**Formula:**
```
Thickness_Score = 10 * (thickness_mm − 6) / (10 − 6)
Thickness_Score = clamp(Thickness_Score, 0, 10)
```

**Formula:** `Thermal_Efficiency = 0.6 × Cooling + 0.4 × Thickness`

<br>

#### B.5 Charging Stress (5% of HEI)

**B.5.1 Wired Charging (70%)**

**Why this matters:** High-wattage fast charging generates significant heat during the charging cycle. While the phone eventually cools down, this period of elevated temperature reduces the battery's chemical efficiency and increases internal resistance, leading to a transient period of higher power consumption and reduced effective capacity immediately after charging.

**Data Structure Mapping:** `5_2_wired_charging_speed.watts`

**Scoring Range:**
- **Max Score (10) at:** ≤ 10W (Slow charging, minimal heat)
- **Min Score (0) at:** ≥ 150W (Extreme fast charging, high heat)

**Formula (Inverted):**
```
Wired_Score = 10 - 10 * (Watts − 10) / (150 − 10)
Wired_Score = clamp(Wired_Score, 0, 10)
```

**B.5.2 Wireless Charging (30%)**

**Why this matters:** Wireless charging is inherently less efficient than wired charging, generating waste heat that warms up the entire device battery. This thermal stress, similar to fast wired charging, causes a temporary reduction in battery efficiency and effective capacity until the device returns to ambient temperature.

**Data Structure Mapping:** `5_3_wireless_charging_speed.watts`

**Scoring Range:**
- **Max Score (10) at:** 0W (No wireless charging)
- **Min Score (0) at:** ≥ 50W (Fast wireless charging)

**Formula (Continuous & Inverted):**
```
Wireless_Score = 10 - 10 * (Watts − 0) / (50 − 0)
Wireless_Score = clamp(Wireless_Score, 0, 10)
```

**Formula:** `Charging_Stress = 0.7 × Wired + 0.3 × Wireless`

**Final HEI Formula:**
```
HEI = 0.35 × SoC + 0.35 × Display + 0.15 × Connectivity + 0.10 × Thermal + 0.05 × Charging
```

---

### 📱 Layer C: Software & Optimization Index (SOI) (20%)
*This layer accounts for the efficiency of the operating system and the impact of pre-installed software.*

#### C.1 OS & Skin Efficiency (60%)

**Why this matters:** The OS scheduler determines when the CPU wakes up and how background tasks are handled. iOS and stock Android are generally more efficient at idle than heavy manufacturer skins.

**Data Structure Mapping:** `6_software_and_longevity.skin`

**Scoring Range:**
- **Max Score (10) at:** iOS
- **Min Score (0) at:** Legacy Android (<11)

| OS / Skin               | Score |
|-------------------------|-------|
| iOS                     | 10    |
| Stock Android / Pixel   | 9     |
| Light Skins (Moto/Sony) | 8     |
| Samsung One UI          | 7     |
| Heavy Skins (HyperOS)   | 6     |
| Budget Skins            | 2     |
| Legacy Android          | 0     |

#### C.2 Bloatware Overhead (40%)

**Why this matters:** Bloatware and adware often run hidden background processes that prevent the phone from entering deep sleep, causing "phantom" battery drain even when the phone is not in use.

**Data Structure Mapping:** Directly use SCC score of Section 6.3 System Cleanliness & Control from the file `scoring_rules.md`  



**Formula:** `SOI = 0.60 × OS_Skin + 0.40 × SCC`

---

### 📊 Predicted Score Calculation
*This score is used ONLY for finding "Nearest Neighbors" in Case 3.*
```
Predicted_Score = 0.45 × Energy_Score + 0.35 × HEI + 0.20 × SOI
```

---

## 🏆 PART 2: THE BENCHMARK LAYER
*Normalization of real-world test results into a 0-10 score.*

### 1. GSMArena Active Use Score (v2.0)
**Source:** [GSMArena Battery Tests v2.0](https://www.gsmarena.com/battery-test-v2.php3)

**Metric:** Active Use Score (Hours:Minutes)

**Normalization:**
**Scoring Range:**
- **Max Score (10) at:** ≥ 23:07 hours (23.12h)
- **Min Score (1) at:** ≤ 7:48 hours (7.8h)
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
- **Min Score (1) at:** ≤ 3:36 hours (3.6h)
- **Formula:**
```
PA_Score = 10 * (Hours - 3.6) / (11.42 - 3.6)
PA_Score = clamp(PA_Score, 0, 10)
```

---

## 🧮 PART 3: SCORING LOGIC (The 3 Cases)

### ✅ CASE 1: Both Benchmarks Available
**Condition:** Target Phone A has scores from **both** GSMArena and PhoneArena.

**Method:**
Simply take the average of the two normalized benchmark scores. The predictive model is ignored.

**Formula:**
```
Final_Score_A = (GSM_Score_A + PA_Score_A) / 2
```

**Example:**
- **Phone A:** Galaxy S24 Ultra
- GSMArena: 16h 45m (16.75h) → `GSM_Score = 10 * (16.75 - 7.8) / (23.12 - 7.8) = 5.84`
- PhoneArena: 10h 30m (10.5h) → `PA_Score = 10 * (10.5 - 3.6) / (11.42 - 3.6) = 8.82`
- **Final Score:** `(5.84 + 8.82) / 2 = 7.33`

---

### ⚠️ CASE 2: Partial Data (One Benchmark Available)
**Condition:** Target Phone A has a score from **only one** source (e.g., GSMArena).

**Method:**
Use the single available normalized benchmark score.

**Formula:**
```
Final_Score_A = Available_Benchmark_Score_A
```

**Example:**
- **Phone A:** Xiaomi 14 Pro (China exclusive)
- GSMArena: 14h 10m (14.17h) → `GSM_Score = 10 * (14.17 - 7.8) / (23.12 - 7.8) = 4.16`
- PhoneArena: N/A
- **Final Score:** `4.16`

---

### 🔮 CASE 3: Interpolation (No Benchmarks Available)
**Condition:** Target Phone A has **NO** benchmark data (e.g., unreleased or niche phone).

**Method:** "Nearest Neighbor" Interpolation
1.  Calculate `Predicted_Score_A` using the technical model (Part 1).
2.  Find **3 Reference Phones (Neighbor1, Neighbor2, Neighbor3)** that:
    *   Have **BOTH** GSMArena and PhoneArena scores (Case 1 phones).
    *   Have the closest `Predicted_Score` to Phone A.
3.  Calculate the **Correction Ratio** between A's prediction and the neighbors' average prediction.
4.  Apply this ratio to the neighbors' average **Benchmark Score**.

**Step-by-Step Formula:**

1.  **Find Neighbors:** Select Neighbor1, Neighbor2, Neighbor3 having:
    *   a) Scores from **BOTH** GSMArena and PhoneArena benchmarks.
    *   b) Minimizing `|Predicted_Score_A - Predicted_Score_X|`.
2.  **Calculate Average Prediction of Neighbors:**
    `Avg_Pred_Neighbors = (Predicted_Score_Neighbor1 + Predicted_Score_Neighbor2 + Predicted_Score_Neighbor3) / 3`
3.  **Calculate Correction Ratio:**
    `Ratio = Predicted_Score_A / Avg_Pred_Neighbors`
4.  **Calculate Average Benchmark of Neighbors:**
    `Avg_Bench_Neighbors = (Final_Score_Neighbor1 + Final_Score_Neighbor2 + Final_Score_Neighbor3) / 3`
5.  **Calculate Final Score:**
    `Final_Score_A = Ratio * Avg_Bench_Neighbors`

**Example:**
- **Target Phone A:** "FuturePhone 5" (No benchmarks)
    - `Predicted_Score_A = 8.5` (High specs, large battery)
- **Neighbors Found (Similar Specs, with Benchmarks):**
    - **Neighbor1:** `Predicted = 8.0`, `Benchmark = 7.2`
    - **Neighbor2:** `Predicted = 8.2`, `Benchmark = 7.4`
    - **Neighbor3:** `Predicted = 7.8`, `Benchmark = 7.0`
- **Calculations:**
    - `Avg_Pred_Neighbors = (8.0 + 8.2 + 7.8) / 3 = 8.0`
    - `Avg_Bench_Neighbors = (7.2 + 7.4 + 7.0) / 3 = 7.2`
    - `Ratio = 8.5 / 8.0 = 1.0625` (Phone A is predicted to be ~6.25% better than neighbors)
    - `Final_Score_A = 1.0625 * 7.2 = 7.65`

**Why this works:**
The neighbors generally perform worse in the real world than their raw specs suggest (Avg Bench 7.2 vs Avg Pred 8.0). Even though Phone A has a high predicted score of 8.5, we adjust it down to 7.65 to reflect the reality of similar devices, while still rewarding it for having better specs than the neighbors.
