# Section 8.2 Method C Parameter Calibration & 44-Device Optimization Study

> [!IMPORTANT]

> **Study Target & Scope:** This document presents the complete mathematical derivation, hardware data audit, parameter domain boundary verification, statistical loss function theory, Huber loss threshold (`delta`) sensitivity sweep, normalization constant strategy evaluation, and complete 44-device prediction matrix (evaluating physical component parameters, duration in minutes, and normalized speed scores on a 0-to-10 point scale) for **Method C (Physical Loss-Based Charging Duration Predictor)** across authentic laboratory benchmarks from GSMArena data.

---

## 1. Statistical Concepts, Evaluation Metrics & Loss Function Theory

To evaluate and optimize charging prediction models accurately, both physical time predictions (in minutes) and normalized speed scores (on a 0-to-10 point scale) must be measured against empirical laboratory data. This section provides an accessible, non-technical explanation of the statistical metrics, loss functions, and optimization concepts used throughout this study.


### 1.1 Overview of Evaluation Metrics

When comparing predicted charging durations or speed scores against real-world benchmark measurements, four fundamental statistical metrics are used to quantify model accuracy:

1. **Mean Squared Error (`MSE`):**

   * **Definition:** Mean Squared Error (`MSE`) is the average of the squared differences between predicted values and actual measurements.

   * **Units:** Minutes squared (`mins^2` for `MSE_T`) or points squared (`pts^2` for `MSE_S`).

   * **Key Characteristic:** `MSE` is primarily used by optimization algorithms during mathematical parameter fitting because taking the derivative of a squared term yields a smooth, well-behaved mathematical slope (gradient).


2. **Root Mean Square Error (`RMSE`):**

   * **Definition:** Root Mean Square Error (`RMSE`) is the square root of `MSE` (`RMSE = sqrt(MSE)`). It represents the standard deviation of prediction errors and measures how spread out the prediction errors are around the true benchmark values.

   * **Units:** Physical duration in minutes (`RMSE_T`) or speed score points (`RMSE_S`).

   * **Key Characteristic:** Because errors are squared before being averaged, `RMSE` gives extra weight to larger prediction errors. A single large error (e.g. predicting a 30-minute error on one phone) increases `RMSE` significantly more than several small 2-minute errors.


3. **Mean Absolute Error (`MAE`):**

   * **Definition:** Mean Absolute Error (`MAE`) calculates the simple average gap between predicted values and actual benchmark measurements, ignoring whether the error is positive or negative.

   * **Units:** Physical duration in minutes (`MAE_T`) or speed score points (`MAE_S`).

   * **Key Characteristic:** `MAE` treats every minute of error equally. An error of 10 minutes on one phone is weighted exactly the same as two 5-minute errors on two other phones, making it a very direct and intuitive measure of average model accuracy for non-technical readers.


4. **Mean Directional Bias (`Mean_dT` & `Mean_dS`):**

   * **Definition:** Mean Directional Bias measures whether the model has a systematic tendency to over-predict or under-predict across the entire phone population.

     * `Mean_dT = Average(Predicted Duration - Actual Benchmark Duration)` in minutes.

     * `Mean_dS = Average(Predicted Score - Actual Benchmark Score)` in score points.

   * **Interpretation:** A positive duration bias (`Mean_dT > 0`) indicates the model systematically over-estimates charging duration (predicts slower charging than actual), whereas a negative bias (`Mean_dT < 0`) indicates under-estimation. An ideal model achieves a bias near zero (`Mean_dT ≈ 0.0 mins`).

---

### 1.2 Candidate Loss Functions & The Huber Loss 2-Zone Hybrid Method

During parameter optimization, an objective **loss function** measures total prediction error across the dataset. The residual error for each device `i` is defined as:

`e_i = T_A,i - T_C,i`

where `e_i` is the physical duration prediction residual in minutes (the difference between actual benchmark duration `T_A,i` and predicted duration `T_C,i`). The optimizer adjusts physical model parameters to minimize this loss across all devices. Three candidate loss functions are analyzed:

1. **Option 1: Pure Mean Squared Error (`MSE` - Quadratic Loss):**

   * `Loss_MSE = (1 / N) * Sum(e_i^2)`

   * *Properties:* Highly sensitive to extreme outlier errors. If a single device has a large duration error, `MSE` squares that error, creating a disproportionately massive penalty that forces the optimizer to distort global parameters to satisfy that single outlier.

2. **Option 2: Pure Mean Absolute Error (`MAE` - Linear Loss):**

   * `Loss_MAE = (1 / N) * Sum(|e_i|)`

   * *Properties:* Robust to extreme outlier errors because penalties increase linearly rather than quadratically. However, pure `MAE` lacks smooth mathematical derivatives at zero error (`|e_i| = 0`), which can cause numerical instability during gradient-based optimization.

3. **Option 3: Huber Loss Function (`L_Huber` - Robust 2-Zone Hybrid Method):**

   * `L_Huber(e_i; delta) = 0.5 * e_i^2` if `|e_i| <= delta`, else `delta * |e_i| - 0.5 * delta^2`

   * *The 2-Zone Hybrid Mechanism:* Huber Loss combines the best properties of both `MSE` and `MAE` by switching between two zones based on a threshold parameter `delta` (in minutes):

     * **Zone 1: Small Prediction Errors (`|e_i| <= delta`) → Uses Quadratic Error (`MSE`):** For prediction errors within threshold `delta` (`|e_i| <= delta`), the loss is squared (`0.5 * e_i^2`). This provides a smooth, continuous mathematical gradient that enables precise parameter fine-tuning.

     * **Zone 2: Large Outlier Errors (`|e_i| > delta`) → Uses Linear Error (`MAE`):** For large prediction errors exceeding threshold `delta` (`|e_i| > delta`), the loss function automatically transitions to a linear penalty (`delta * |e_i| - 0.5 * delta^2`). The penalty increases strictly linearly per minute of error, preventing extreme outlier residuals from dominating the gradient and pulling global parameter optimization out of alignment.

     * **Mathematical Continuity Offset (`- 0.5 * delta^2`):** The offset term `- 0.5 * delta^2` in Zone 2 ensures mathematical continuity at the boundary `|e_i| = delta`. At `|e_i| = delta`, Zone 1 yields `0.5 * delta^2` and Zone 2 yields `delta * delta - 0.5 * delta^2 = 0.5 * delta^2`. Subtracting `0.5 * delta^2` eliminates any abrupt jump in loss penalty, guaranteeing that both the loss function value and its slope (derivative) match seamlessly across both zones.

---

## 2. Physical Formulation & Parameter Definition

Method C predicts full 0% to 100% charging duration `T_predicted` (minutes) by calculating effective average power `P_effective` delivered across the charge cycle:

`T_predicted = (E_supply / P_effective) * 60`

`P_effective = P_peak * F_system(C_rate)`

`F_system = min(1, eta_low / (1 + k * max(0, C_rate - C0_effective)^p))`

`C0_effective = C0_base * f_thermal(power_ratio) * f_skin_headroom(T_limit)`


### 2.1 Physical Parameter Definitions

* `P_peak` (Watts - W): Maximum physical input charging power accepted by the smartphone hardware during the bulk fast-charging phase (measured in Watts - W).

* `E_supply = (Capacity_mAh * V_nominal) / 1000` (Watt-hours - Wh): Total stored battery energy capacity.

* `C_rate = P_peak / E_supply` (reciprocal hours - `h^-1`): Continuous charging current rate normalized by stored energy.

* `eta_low`: Baseline low-power full-cycle utilization fraction.

* `C0_base`: Architecture-dependent baseline thermal saturation onset threshold. This parameter is where the fundamental difference between Single-Cell (1S) and Dual-Cell (2S) architectures is mathematically enforced:

  * **Single-Cell (1S):** Lower threshold (`C0_single`). The entire charging wattage is pushed at a standard nominal voltage (~3.85V), meaning current intensity (Amperes - `I`) is very high. High current creates severe Printed Circuit Board (`PCB`) trace heating (`P_loss = I^2 * R_trace`) and forces early thermal power tapering.

  * **Dual-Cell Series (2S):** A physically split 2S architecture doubles nominal system voltage (7.70V vs 3.85V). Because Power = Voltage * Current (`P = V * I`), doubling the voltage halves electrical current (`I_dual = 0.5 * I_single`) for identical charging power:

    * **At the Battery Cell Level:** For a given total battery capacity (Milliampere-hours - mAh), splitting the pack into two equal series cells halves the physical electrode surface area of each cell. Because internal resistance is inversely proportional to electrode surface area, each half-capacity cell has twice the internal resistance (`2R` per cell) of an equivalent single cell (`R`). Connecting these two cells in series sums their internal resistances to `4R` (`2R + 2R`). Cell Joule heating is `Heat_battery = (0.5 * I)^2 * (4R) = 0.25 * I^2 * 4R = I^2 * R`, yielding **0% reduction** (identical heat generation) in battery cell internal heat generation.

    * **At the Motherboard & PCB Trace Level:** PCB copper traces, connector ribbons, and Power Management Integrated Circuits (`PMIC`) have fixed resistance (`R_trace`). Halving the current reduces trace Joule heating to `Heat_trace = (0.5 * I)^2 * R_trace = 0.25 * (I^2 * R_trace)`, yielding an exact **75% reduction** (ratio of 1/4) in motherboard trace heat generation. Furthermore, it enables high-efficiency (~97%) 2:1 direct charge pumps. Because motherboard trace heating is the primary thermal bottleneck in high-power charging, this 75% trace heat reduction allows dual-cell devices to sustain much higher charge rates before reaching thermal saturation, as reflected in the higher `C0_base` threshold (`C0_dual` >> `C0_single`).

* `C0_effective`: Thermally scaled effective onset threshold.

* `k`: Non-linear thermal taper severity multiplier.

* `p`: Power saturation curvature exponent.


### 2.2 Integration of Section 6.10 Chassis Thermal Dissipation Factor `f_thermal(power_ratio)`

Method C couples directly to Section 6.10's physical chassis cooling metrics via the non-dimensional admissible power ratio `power_ratio = P_admissible_soc / P_peak_soc`:

`f_thermal(power_ratio) = power_ratio`

* **Direct Thermally Admissible Charge-Rate Ratio (Rough First-Order Estimate):**

  Section 6.10 defines `power_ratio` as the ratio of continuous admissible thermal power capacity (`P_admissible_soc`) relative to peak silicon heat load (`P_peak_soc`). Comparing the real device's maximum continuous admissible charge rate `C_admissible = P_admissible_soc / E_supply` to an unconstrained reference charge rate `C_ideal = P_peak_soc / E_supply` yields:

  `C_admissible / C_ideal = (P_admissible_soc / E_supply) / (P_peak_soc / E_supply) = P_admissible_soc / P_peak_soc = power_ratio`

  *Physical Assessment & Approximation Note:* This formulation serves as a **first-order, rough physical estimate**. It assumes that chassis thermal dissipation capacity for SoC silicon heat load maps linearly onto battery charging thermal headroom. In reality, SoC silicon heating (localized active compute) and battery charging heat (distributed PMIC conversion losses and internal cell impedance `I^2 * R`) have distinct thermal pathways, operating temperatures, and dissipation surfaces. This rough approximation explains why neutralizing `f_thermal = 1.0000` is empirically and physically evaluated below.


* **Linking with Benchmark Performance Stability & TDSI Score (Derivation from Section 6.10):**

  Section 6.10 relates physical `power_ratio` to empirical gaming benchmark performance stability percentage (`stability_%`) and the final `TDSI` score through two distinct physical and statistical transformations:

  1. **Silicon Dynamic Power Law (`P ∝ f^3`):** In Complementary Metal-Oxide-Semiconductor (`CMOS`) digital logic, dynamic power scales as `P = C * V^2 * f`. Because voltage scales linearly with operating frequency (`V ∝ f`), power scales cubically with clock frequency (`P ∝ f^3`).

  2. **Cube-Root Stability Relation:** Sustained gaming FPS (clock frequency `f`) is constrained by admissible chassis thermal power (`power_ratio`), yielding the Section 6.10 Cube-Root Law:

     `stability_% = 100 * (power_ratio)^0.333`

  3. **Inverting for Power Ratio:** Inverting the dynamic frequency relation yields:

     `power_ratio = (stability_% / 100)^3`

  4. **Section 6.10 Logarithmic Normalization to Final TDSI Score:** The final Thermal Dissipation & Stability Index (`TDSI`) on a 0-to-10 scale is **NOT** a simple linear fraction of `stability_%`. Instead, Section 6.10 applies a **Logarithmic Normalization** against empirical benchmark anchors:

     `TDSI = 10.0 * (log(stability_%) - log(S_min)) / (log(S_max) - log(S_min))`

     Inverting this logarithmic normalization gives `stability_% = S_min * (S_max / S_min)^(TDSI / 10.0)`. Consequently, calculating `power_ratio` directly from a final `TDSI` score requires converting `TDSI` back through the logarithmic inversion before cubing (`power_ratio = ((S_min / 100) * (S_max / S_min)^(TDSI / 10.0))^3`). An unconstrained reference device (`TDSI = 10.0`) sustains `f_thermal = 1.0`, while a throttled chassis (`TDSI < 10.0`) scales `f_thermal` accordingly.


* **Physical & Statistical Justification for Setting `f_thermal = 1.0000` Neutralized:**

  While `f_thermal(power_ratio)` provides an analytical link to 3DMark gaming thermal stability, empirical evaluation across the 44-device benchmark suite demonstrates that setting `f_thermal = 1.0000` universally is physically and statistically superior for charging modeling:

  1. **Statistical Insignificance of Partial Correlation:** Controlling for normalized charge rate `C_rate`, the partial correlation between `f_thermal` and empirical charge duration `T_A` is statistically insignificant (`r = -0.1467`, `p = 0.3419`), confirming that gaming stability adds no independent predictive signal beyond `C_rate`.

  2. **Workload Mechanism Disparity:** 3DMark Wild Life Extreme stress testing measures sustained 100% GPU/CPU active silicon power draw (5W–12W), whereas battery charging heat generation stems from internal cell impedance (`I^2 * R`) and PMIC conversion losses. Coupling charging kinetics directly to gaming benchmarks introduces cross-domain distortion.

  3. **Empirical Precision Gain:** Neutralizing `f_thermal = 1.0000` preserves overall predictive MAE (`9.23 mins` vs `9.28 mins`) while significantly reducing peak relative percentage errors on ultra-fast chargers from `+72.3%` down to `+54.0%`.

---

### 2.3 Physical Derivation of the Skin Temperature Headroom Factor `f_skin_headroom(T_limit)`

The physical scaling relationship between allowable skin temperature limits (`T_limit`) and sustainable charging onset threshold is defined as:

`f_skin_headroom(T_limit) = ((T_limit - T_ambient_ref) / (T_limit_ref - T_ambient_ref))^0.5`

* **Thermodynamic Derivation:**

  1. **Joule Heat Generation Rate (`P_heat ∝ C_rate^2`):**

     From Joule's Law, internal heat generation is `P_heat = I^2 * R_effective`. Continuous charge rate `C_rate` (reciprocal hours, `h^-1`) is defined as continuous input power `P_input` divided by stored battery energy `E_supply` (Watt-hours - Wh):

     `C_rate = P_input / E_supply = (I * V_nominal) / (Capacity_Ah * V_nominal) = I / Capacity_Ah  =>  I = C_rate * Capacity_Ah`

     Substituting `I = C_rate * Capacity_Ah` into Joule's Law yields `P_heat = C_rate^2 * (Capacity_Ah^2 * R_effective)`. Since nominal battery capacity `Capacity_Ah` and internal resistance `R_effective` are constant for a given device, internal heat generation scales directly with the square of the charge rate:

     `P_heat ∝ C_rate^2`

  2. **Allowable Thermal Rise & Equilibrium:** Permissible temperature rise above reference ambient temperature `T_ambient_ref` is bounded by vendor thermal skin threshold `T_limit`: `Delta_T_max = T_limit - T_ambient_ref`. Equating steady-state heat generation to dissipation (`P_heat ∝ Delta_T_max`) gives `C_max^2 ∝ Delta_T_max  =>  C_max ∝ sqrt(T_limit - T_ambient_ref)`. Normalizing `C_max(T_limit)` against baseline reference skin limit `T_limit_ref`:

     `f_skin_headroom(T_limit) = C_max(T_limit) / C_max(T_limit_ref) = ((T_limit - T_ambient_ref) / (T_limit_ref - T_ambient_ref))^0.5`

     Plugging in reference baseline values (`T_ambient_ref = 25.0°C`, `T_limit_ref = 40.0°C`  =>  `Delta_T_ref = 15.0°C`):

     `f_skin_headroom(T_limit) = ((T_limit - 25.0) / 15.0)^0.5`

     **Mathematical Analysis & Assessment of Negligible Impact:**

     Detailed empirical analysis across the 44-device benchmark suite demonstrates that the actual predictive impact of `f_skin_headroom` on full charging duration `T_predicted` is negligible (<< 1 minute per device). This negligible sensitivity is governed by sub-linear exponent damping (`p << 1`):

     * **Sub-Linear Exponent Damping (`p << 1`):** In the continuous system power retention factor `F_system = eta_low / (1 + k * max(0, C_rate - C0_effective)^p)`, the effective onset threshold `C0_effective` is subtracted from continuous charge rate `C_rate` before being raised to the power exponent `p`. While `C_rate` exceeds `C0_effective` by varying margins across active fast-charging devices, reducing `f_skin_headroom` from `1.0000` down to `0.8165` shifts `C0_effective` by only a small absolute delta (`Delta C0 = 0.07 h^-1` for 1S single-cell and `0.48 h^-1` for 2S dual-cell). Raising the modified term `max(0, C_rate - C0_effective)` to the highly sub-linear exponent `p ≈ 0.1341` (which acts like a ~7.5th root) heavily dampens this shift. Combined with the additive unit baseline (`1 + ...`) in the denominator, variations in `f_skin_headroom` produce negligible changes in `F_system` (< 0.005) and alter full predicted charging duration `T_predicted` by less than 1 minute across the dataset.

     Furthermore, enforcing vendor-specific skin temperature thresholds (`T_limit`) relies on arbitrary, brand-dependent firmware throttling policies (specifically Apple's conservative skin thermal limits and extended CV trickle charging) that introduce subjective vendor biases into an otherwise objective physical loss model. Consequently, we completely eliminate these biases by setting `f_skin_headroom` to 1.0 (`f_skin_headroom = 1.0000`) universally across all devices.

---

## 3. Huber Loss Threshold (`delta`) Sensitivity Sweep & Boundary Interior Verification

Using deterministic global optimization (`Differential Evolution`, `seed=42`, `popsize=20`, `maxiter=800`), we evaluated model performance across 12 candidate Huber loss thresholds (`delta = 0.0` to `100.0` mins) to analyze parameter sensitivity across the defined search domain bounds (`eta_low ∈ [0.50, 1.00]`, `C0_single and C0_dual ∈ [0.00, 15.00] h^-1`, `k ∈ [0.00, 10.00]`, `p ∈ [0.01, 5.00]`):

* **Threshold Sensitivity Analysis:** Selecting `delta = 0.0 mins (Pure MAE Primary)` comes extremely close to minimizing overall dataset mean absolute error (`MAE_T = 8.64 mins` vs minimum `8.63 mins`) while compressing peak relative percentage error (`Max Error % = +37.3%`) and offering maximum mathematical simplicity (L1 Pure MAE loss).

* **Parameter Convergence & Search Domain Margin Verification:** Every optimized parameter value across all 12 Huber loss thresholds converges with substantial, comfortable safety margins away from the search domain boundaries. These wide safety margins confirm that global optimization achieved genuine, unconstrained physical stationary optima rather than being truncated or artificially limited by search domain boundary constraints (`Boundary Status: OK (Interior)`).


| Huber Threshold (`delta`) | eta_low    | C0_single (h^-1) | C0_dual (h^-1) | `k`        | `p`        | `Mean_dT` (mins) | `MAE_T` (mins) | `RMSE_T` (mins) | Max Error (mins) | Max Error (%) | Boundary Status |
| :-----------------------: | :--------: | :--------------: | :------------: | :--------: | :--------: | :--------------: | :------------: | :-------------: | :--------------: | :-----------: | :-------------: |
| **`0.0` (Pure MAE)**      | ` 0.9670 ` | `0.4051`         | `2.6087`       | ` 1.1191 ` | ` 0.1341 ` | `-3.00`          | **`8.64`**     | `13.49`         | `36.63`          | `+37.3%`      | OK (Interior)   |
| **`0.5`**                 | ` 0.9675 ` | `0.4051`         | `2.6343`       | ` 1.1223 ` | ` 0.1323 ` | `-2.95`          | **`8.63`**     | `13.48`         | `36.57`          | `+37.1%`      | OK (Interior)   |
| **`1.0`**                 | ` 0.9673 ` | `0.4051`         | `2.6400`       | ` 1.1236 ` | ` 0.1331 ` | `-2.90`          | **`8.63`**     | `13.46`         | `36.49`          | `+37.4%`      | OK (Interior)   |
| **`2.5`**                 | ` 0.9673 ` | `0.4050`         | `2.6404`       | ` 1.1316 ` | ` 0.1365 ` | `-2.67`          | **`8.66`**     | `13.39`         | `36.15`          | `+38.6%`      | OK (Interior)   |
| **`5.0`**                 | ` 0.9671 ` | `0.4050`         | `2.6841`       | ` 1.1560 ` | ` 0.1465 ` | `-1.94`          | **`8.81`**     | `13.17`         | `35.09`          | `+42.4%`      | OK (Interior)   |
| **`7.5`**                 | ` 0.9670 ` | `0.4049`         | `2.6882`       | ` 1.1654 ` | ` 0.1520 ` | `-1.65`          | **`8.88`**     | `13.09`         | `34.66`          | `+44.3%`      | OK (Interior)   |
| **`10.0`**                | ` 0.9668 ` | `0.4048`         | `2.6901`       | ` 1.1761 ` | ` 0.1574 ` | `-1.32`          | **`8.95`**     | `13.02`         | `34.18`          | `+46.2%`      | OK (Interior)   |
| **`15.0`**                | ` 0.9663 ` | `0.4046`         | `2.6886`       | ` 1.1933 ` | ` 0.1689 ` | `-0.76`          | **`9.09`**     | `12.92`         | `33.34`          | `+50.2%`      | OK (Interior)   |
| **`20.0`**                | ` 0.9662 ` | `0.4043`         | `2.6919`       | ` 1.2097 ` | ` 0.1801 ` | `-0.25`          | **`9.23`**     | `12.86`         | `32.57`          | `+54.0%`      | OK (Interior)   |
| **`30.0`**                | ` 0.9659 ` | `0.4040`         | `2.6961`       | ` 1.2312 ` | ` 0.1922 ` | `+0.43`          | **`9.40`**     | `12.83`         | `31.57`          | `+58.7%`      | OK (Interior)   |
| **`50.0`**                | ` 0.9659 ` | `0.4040`         | `2.6952`       | ` 1.2325 ` | ` 0.1927 ` | `+0.47`          | **`9.41`**     | `12.83`         | `31.52`          | `+58.9%`      | OK (Interior)   |
| **`100.0` (MSE-like)**    | ` 0.9659 ` | `0.4040`         | `2.6952`       | ` 1.2325 ` | ` 0.1927 ` | `+0.47`          | **`9.41`**     | `12.83`         | `31.52`          | `+58.9%`      | OK (Interior)   |

---

## 4. Speed Score Conversion & Normalization Strategy Assessment

While predicting full charging duration `T_predicted` (in minutes) provides an unwarped physical output, benchmark evaluations require converting duration into an intuitive, human-readable **Speed Score (`S_speed_MethodC` points on a 0-to-10 scale)**.


### 4.1 Logarithmic Speed Score Mapping Formula

Predicted physical charging duration `T_predicted` (minutes) is converted into Speed Score `S_speed_MethodC` (points on a 0-to-10 scale) using the canonical Logarithmic Utility Normalization formula:

`S_speed_MethodC = 10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(T_predicted)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins))` (Clamped 0.0 to 10.0)

---

### 4.2 Choice of Normalization Constants: Dedicated Bounds vs. Common Aligned Bounds

Converting physical duration predictions `T_predicted` into normalized speed scores `S_speed_MethodC` requires defining lower (`Battery_Wired_Charge_Time_Min_Mins`) and upper (`Battery_Wired_Charge_Time_Max_Mins`) normalization bounds. Two distinct normalization strategies were analyzed:

1. **Strategy 1: Method-Specific Dedicated / Dynamic Normalization Constants (`Battery_Wired_Charge_Time_Predicted_Min_Mins` & `Battery_Wired_Charge_Time_Predicted_Max_Mins`):**

   * **Concept:** Uses the model's own predicted minimum (`Battery_Wired_Charge_Time_Predicted_Min_Mins = 11.6 mins` for Realme GT3) and maximum (`Battery_Wired_Charge_Time_Predicted_Max_Mins = 240.2 mins` for iPhone 7 Plus) charging durations as dedicated normalization endpoints:

     `S_speed_MethodC = 10 * (log(240.2) - log(T_predicted)) / (log(240.2) - log(11.6))` (Clamped 0.0 to 10.0)

   * **Mathematical Assessment of Strategy 1 (Score Deformation):** Because Method C's predicted duration range (`[11.6 mins, 240.2 mins]`) is strictly contained within Method A's benchmark interval (`[9.00 mins, 241.0 mins]`), forcing Method C's narrower bounds to span the full `0.00` to `10.00` point scale shrinks the logarithmic denominator from `3.2876` down to `3.0305`. This creates an artificial upward score deformation across the entire dataset, shifting the average score bias to `Mean_dS = +0.380 pts` and inflating overall score errors (`MAE_S = 0.461 pts`, `RMSE_S = 0.605 pts`).

2. **Strategy 2: Common / Benchmark-Aligned Global Normalization Constants (`Battery_Wired_Charge_Time_Min_Mins = 9.00 mins`, `Battery_Wired_Charge_Time_Max_Mins = 241.0 mins` - Recommended Master Strategy):**

   * **Concept:** Uses fixed, common empirical benchmark bounds (`Battery_Wired_Charge_Time_Min_Mins = 9.00 mins` for Redmi Note 12 Explorer and `Battery_Wired_Charge_Time_Max_Mins = 241.0 mins` for iPhone 7 Plus) across all modeling methods (predicted and Benchmark):

     `S_speed_MethodC = 10 * (log(Battery_Wired_Charge_Time_Max_Mins) - log(T_predicted)) / (log(Battery_Wired_Charge_Time_Max_Mins) - log(Battery_Wired_Charge_Time_Min_Mins))` (Clamped 0.0 to 10.0)

   * **In-Depth Assessment & Why Strategy 2 is Superior:**

     * **Absence of Clipping:** Because Method C's predicted durations (`11.6 mins <= T_predicted <= 240.2 mins`) fall entirely inside Method A's empirical interval (`[9.00 mins, 241.0 mins]`), **no score clipping occurs at either boundary** (no device is capped at 0.00 or 10.00 pts).

     * **Preservation of Scale Invariance:** Strategy 2 maintains exact mathematical scale invariance across Method A, Method B, and Method C. Every minute of physical charging duration corresponds to the exact same score point value regardless of which predictor generated it.

     * **Superior Empirical Precision:** Eliminates artificial score deformation, significantly reducing score prediction errors (`MAE_S` drops from `0.461 pts` down to `0.392 pts`, `RMSE_S` drops from `0.605 pts` down to `0.507 pts`) and achieving near-zero directional score bias (`Mean_dS = +0.023 pts`).

---

### 4.3 Strategy Comparison

The table below summarizes the quantitative performance metrics (`MAE_S`, `RMSE_S`, `Mean_dS`) and physical trade-offs under Strategy 1 (Dedicated Model Bounds) vs. Strategy 2 (Common Aligned Bounds) across the primary calibrated Huber model configuration (`delta = 0.0 mins`):


| Normalization Strategy                 | `T_min` (mins) | `T_max` (mins) | `MAE_S` (pts) | `RMSE_S` (pts) | `Mean_dS` (pts) | Mathematical Assessment & Recommendation                                                                                      |
| :------------------------------------- | :------------: | :------------: | :-----------: | :------------: | :-------------: | :---------------------------------------------------------------------------------------------------------------------------- |
| **Strategy 1: Dedicated Model Bounds** | `11.6 m`       | `240.2 m`      | ` 0.461 pts ` | ` 0.605 pts `  | ` +0.380 pts `  | **Clean 0-10 spread (guaranteed zero clipping for Method C) but worse statistical metrics.**                                  |
| **Strategy 2: Common Aligned Bounds**  | ` 9.0 m`       | `241.0 m`      | ` 0.392 pts ` | ` 0.507 pts `  | ` +0.023 pts `  | **(Recommended) Preserves global scale invariance and achieves near-zero score bias, still with zero clipping for Method C.** |

---

## 5. Residual Analysis & Sub-Dataset Validation

Across the 44-device laboratory benchmark dataset, residual analysis reveals a clear structural bifurcation between standard smartphones and hardware exhibiting vendor-specific thermal throttling:

* **Standard Android Devices (34 devices):** Model duration predictions for modern fast-chargers (Samsung, OnePlus, Xiaomi, Vivo, ROG Phone, Nothing, Pixel) display an average residual error `MAE_T` of **3.5 to 5.0 minutes**, confirming good predictive accuracy under unthrottled physical loss kinetics.

* **Apple iPhones & LG G7 ThinQ (10 devices):** Display an elevated average error `MAE_T` of **22.64 minutes**. Large negative duration residuals (Delta = -20 to -35 minutes) are concentrated exclusively in Apple and LG hardware, likely due to conservative vendor Battery Management System (`BMS`) firmware throttling policies and extended Constant Voltage (`CV`) trickle charging curves.

---

## 6. Master Device Prediction Matrix

Below is the complete 44-device prediction dataset under the primary calibrated configuration (`delta = 0.0 mins (Pure MAE Primary)`, `eta_low = 0.9670`, `C0_single_base = 0.4051 h^-1`, `C0_dual_base = 2.6087 h^-1`, `k = 1.1191`, `p = 0.1341`). Note that because `f_thermal = 1.0000` and `f_skin_headroom = 1.0000` across all devices in the baseline physical model, the effective thermal onset threshold `C0_effective` is identical to `C0_base` (`2.6087 h^-1` for 2S dual-cell and `0.4051 h^-1` for 1S single-cell).

To ensure maximum visual clarity and prevent horizontal table overflow, the dataset is presented in two structured tables:

1. **Table 6.1 (Physical Component Evaluation):** Details hardware specifications, charge rates, intermediate system power retention factors, effective charging wattage, thermal onset thresholds, and clickable GSMArena laboratory review links.

2. **Table 6.2 (Master Duration & Speed Score Prediction Matrix):** Reports physical charging durations (`T_A` actual vs `T_C` predicted in minutes) alongside speed scores (`S_A` empirical score vs `S_C` predicted scores under both Strategy 1 Dedicated Bounds and Strategy 2 Common Bounds on a 0-to-10 point scale).


### 6.1 Physical Component Evaluation Across all 44 Benchmark Devices


| Smartphone Device Model      | Arch   | P_peak  | E_supply | C_rate | P_eff  | F_system | C0_effective | GSMArena Review Link                                                                            |
| :--------------------------- | :----: | :-----: | :------: | :----: | :----: | :------: | :----------: | :---------------------------------------------------------------------------------------------: |
| **Realme GT3**               | Dual   | 240.0 W | 17.71 Wh | 13.55  | 91.3 W | 0.3803   | 2.6087       | [Realme GT3](https://www.gsmarena.com/realme_gt3-review-2542p3.php)                             |
| **iQOO 11 Pro**              | Dual   | 200.0 W | 18.10 Wh | 11.05  | 77.7 W | 0.3884   | 2.6087       | [iQOO 11 Pro](https://www.gsmarena.com/vivo_iqoo_11_pro-12002.php)                              |
| **Motorola Edge 50 Pro**     | Dual   | 125.0 W | 17.33 Wh | 7.21   | 50.9 W | 0.4074   | 2.6087       | [Motorola Edge 50 Pro](https://www.gsmarena.com/motorola_edge_50_pro-review-2686p3.php)         |
| **Xiaomi 13 Pro**            | Dual   | 120.0 W | 18.56 Wh | 6.47   | 49.6 W | 0.4130   | 2.6087       | [Xiaomi 13 Pro](https://www.gsmarena.com/xiaomi_13_pro-review-2537p3.php)                       |
| **Xiaomi 12T Pro**           | Dual   | 120.0 W | 19.25 Wh | 6.23   | 49.8 W | 0.4150   | 2.6087       | [Xiaomi 12T Pro](https://www.gsmarena.com/xiaomi_12t_pro-review-2495p3.php)                     |
| **Poco F4 GT**               | Dual   | 120.0 W | 18.10 Wh | 6.63   | 49.4 W | 0.4117   | 2.6087       | [Poco F4 GT](https://www.gsmarena.com/poco_f4_gt-review-2418p3.php)                             |
| **Vivo X100 Pro**            | Dual   | 100.0 W | 20.79 Wh | 4.81   | 43.1 W | 0.4309   | 2.6087       | [Vivo X100 Pro](https://www.gsmarena.com/vivo_x100_pro-review-2647p3.php)                       |
| **OnePlus 12**               | Dual   | 100.0 W | 20.79 Wh | 4.81   | 43.1 W | 0.4309   | 2.6087       | [OnePlus 12](https://www.gsmarena.com/oneplus_12-review-2661p3.php)                             |
| **OnePlus 11**               | Dual   | 100.0 W | 19.25 Wh | 5.19   | 42.6 W | 0.4258   | 2.6087       | [OnePlus 11](https://www.gsmarena.com/oneplus_11-review-2533p3.php)                             |
| **OnePlus 12R**              | Dual   | 80.0 W  | 21.17 Wh | 3.78   | 36.1 W | 0.4512   | 2.6087       | [OnePlus 12R](https://www.gsmarena.com/oneplus_12r-review-2665p3.php)                           |
| **Asus ROG Phone 7**         | Dual   | 65.0 W  | 23.10 Wh | 2.81   | 33.0 W | 0.5076   | 2.6087       | [Asus ROG Phone 7](https://www.gsmarena.com/asus_rog_phone_7-review-2572p3.php)                 |
| **Xiaomi 14**                | Single | 90.0 W  | 17.71 Wh | 5.08   | 36.6 W | 0.4069   | 0.4051       | [Xiaomi 14](https://www.gsmarena.com/xiaomi_14-review-2665p3.php)                               |
| **Honor Magic 6 Pro**        | Single | 80.0 W  | 21.56 Wh | 3.71   | 33.4 W | 0.4179   | 0.4051       | [Honor Magic 6 Pro](https://www.gsmarena.com/honor_magic6_pro-review-2664p3.php)                |
| **Motorola Edge 40**         | Single | 68.0 W  | 17.33 Wh | 3.92   | 28.3 W | 0.4160   | 0.4051       | [Motorola Edge 40](https://www.gsmarena.com/motorola_edge_40-review-2565p3.php)                 |
| **Xiaomi 13**                | Single | 67.0 W  | 17.33 Wh | 3.87   | 27.9 W | 0.4165   | 0.4051       | [Xiaomi 13](https://www.gsmarena.com/xiaomi_13-review-2545p3.php)                               |
| **Honor Magic 5 Pro**        | Single | 66.0 W  | 19.64 Wh | 3.36   | 27.8 W | 0.4215   | 0.4051       | [Honor Magic 5 Pro](https://www.gsmarena.com/honor_magic5_pro-review-2545p3.php)                |
| **Samsung Galaxy S24 Ultra** | Single | 45.0 W  | 19.25 Wh | 2.34   | 19.6 W | 0.4351   | 0.4051       | [Samsung Galaxy S24 Ultra](https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2651p3.php) |
| **Samsung Galaxy S23 Ultra** | Single | 45.0 W  | 19.25 Wh | 2.34   | 19.6 W | 0.4351   | 0.4051       | [Samsung Galaxy S23 Ultra](https://www.gsmarena.com/samsung_galaxy_s23_ultra-review-2525p3.php) |
| **Samsung Galaxy S22 Ultra** | Single | 45.0 W  | 19.25 Wh | 2.34   | 19.6 W | 0.4351   | 0.4051       | [Samsung Galaxy S22 Ultra](https://www.gsmarena.com/samsung_galaxy_s22_ultra-review-2384p3.php) |
| **Nothing Phone (2)**        | Single | 45.0 W  | 18.10 Wh | 2.49   | 19.5 W | 0.4327   | 0.4051       | [Nothing Phone (2)](https://www.gsmarena.com/nothing_phone_2-review-2592p3.php)                 |
| **Google Pixel 9 Pro XL**    | Single | 37.0 W  | 19.48 Wh | 1.90   | 16.4 W | 0.4434   | 0.4051       | [Google Pixel 9 Pro XL](https://www.gsmarena.com/google_pixel_9_pro_xl-review-2722p3.php)       |
| **Google Pixel 8 Pro**       | Single | 30.0 W  | 19.44 Wh | 1.54   | 13.6 W | 0.4521   | 0.4051       | [Google Pixel 8 Pro](https://www.gsmarena.com/google_pixel_8_pro-review-2618p3.php)             |
| **Samsung Galaxy S24**       | Single | 25.0 W  | 15.40 Wh | 1.62   | 11.2 W | 0.4500   | 0.4051       | [Samsung Galaxy S24](https://www.gsmarena.com/samsung_galaxy_s24-review-2652p3.php)             |
| **Samsung Galaxy S23**       | Single | 25.0 W  | 15.02 Wh | 1.66   | 11.2 W | 0.4489   | 0.4051       | [Samsung Galaxy S23](https://www.gsmarena.com/samsung_galaxy_s23-review-2536p3.php)             |
| **Samsung Galaxy A55**       | Single | 25.0 W  | 19.25 Wh | 1.30   | 11.5 W | 0.4600   | 0.4051       | [Samsung Galaxy A55](https://www.gsmarena.com/samsung_galaxy_a55-review-2663p3.php)             |
| **Samsung Galaxy A54**       | Single | 25.0 W  | 19.25 Wh | 1.30   | 11.5 W | 0.4600   | 0.4051       | [Samsung Galaxy A54](https://www.gsmarena.com/samsung_galaxy_a54-review-2550p3.php)             |
| **Samsung Galaxy A34**       | Single | 25.0 W  | 19.25 Wh | 1.30   | 11.5 W | 0.4600   | 0.4051       | [Samsung Galaxy A34](https://www.gsmarena.com/samsung_galaxy_a34-review-2544p3.php)             |
| **Google Pixel 7 Pro**       | Single | 23.0 W  | 19.25 Wh | 1.19   | 10.7 W | 0.4640   | 0.4051       | [Google Pixel 7 Pro](https://www.gsmarena.com/google_pixel_7_pro-review-2500p3.php)             |
| **Samsung Galaxy S10**       | Single | 15.0 W  | 13.09 Wh | 1.15   | 7.0 W  | 0.4660   | 0.4051       | [Samsung Galaxy S10](https://www.gsmarena.com/samsung_galaxy_s10-review-1902p3.php)             |
| **Samsung Galaxy S9**        | Single | 15.0 W  | 11.55 Wh | 1.30   | 6.9 W  | 0.4600   | 0.4051       | [Samsung Galaxy S9](https://www.gsmarena.com/samsung_galaxy_s9-review-1741p3.php)               |
| **Samsung Galaxy S8**        | Single | 15.0 W  | 11.55 Wh | 1.30   | 6.9 W  | 0.4600   | 0.4051       | [Samsung Galaxy S8](https://www.gsmarena.com/samsung_galaxy_s8-review-1599p3.php)               |
| **Nokia 2.4**                | Single | 5.0 W   | 17.33 Wh | 0.29   | 4.8 W  | 0.9670   | 0.4051       | [Nokia 2.4](https://www.gsmarena.com/nokia_2_4_hands_on-news-46452.php)                         |
| **Samsung Galaxy A03 Core**  | Single | 7.8 W   | 19.25 Wh | 0.41   | 5.7 W  | 0.7308   | 0.4051       | [Samsung Galaxy A03 Core](https://www.gsmarena.com/samsung_galaxy_a03_core-11210.php)           |
| **Apple iPhone 16 Pro Max**  | Single | 30.0 W  | 18.04 Wh | 1.66   | 13.5 W | 0.4489   | 0.4051       | [Apple iPhone 16 Pro Max](https://www.gsmarena.com/apple_iphone_16_pro_max-review-2751p3.php)   |
| **Apple iPhone 14 Pro Max**  | Single | 29.0 W  | 16.64 Wh | 1.74   | 13.0 W | 0.4469   | 0.4051       | [Apple iPhone 14 Pro Max](https://www.gsmarena.com/apple_iphone_14_pro_max-review-2486p3.php)   |
| **Apple iPhone 15 Pro Max**  | Single | 27.0 W  | 17.02 Wh | 1.59   | 12.2 W | 0.4509   | 0.4051       | [Apple iPhone 15 Pro Max](https://www.gsmarena.com/apple_iphone_15_pro_max-review-2604p3.php)   |
| **Apple iPhone 13 Pro Max**  | Single | 27.0 W  | 16.75 Wh | 1.61   | 12.2 W | 0.4503   | 0.4051       | [Apple iPhone 13 Pro Max](https://www.gsmarena.com/apple_iphone_13_pro_max-review-2332p3.php)   |
| **Apple iPhone 11 Pro Max**  | Single | 18.0 W  | 15.04 Wh | 1.20   | 8.3 W  | 0.4639   | 0.4051       | [Apple iPhone 11 Pro Max](https://www.gsmarena.com/apple_iphone_11_pro_max-review-1991p3.php)   |
| **LG G7 ThinQ**              | Single | 18.0 W  | 11.55 Wh | 1.56   | 8.1 W  | 0.4517   | 0.4051       | [LG G7 ThinQ](https://www.gsmarena.com/lg_g7_thinq-review-1786p3.php)                           |
| **Apple iPhone XS Max**      | Single | 15.0 W  | 12.08 Wh | 1.24   | 6.9 W  | 0.4621   | 0.4051       | [Apple iPhone XS Max](https://www.gsmarena.com/apple_iphone_xs_max-review-1830p3.php)           |
| **Apple iPhone X**           | Single | 15.0 W  | 10.43 Wh | 1.44   | 6.8 W  | 0.4553   | 0.4051       | [Apple iPhone X](https://www.gsmarena.com/apple_iphone_x-review-1681p3.php)                     |
| **Apple iPhone 8**           | Single | 5.0 W   | 7.01 Wh  | 0.71   | 2.5 W  | 0.4945   | 0.4051       | [Apple iPhone 8](https://www.gsmarena.com/apple_iphone_8-review-1673p3.php)                     |
| **Apple iPhone 7 Plus**      | Single | 5.0 W   | 11.17 Wh | 0.45   | 2.8 W  | 0.5581   | 0.4051       | [Apple iPhone 7 Plus](https://www.gsmarena.com/apple_iphone_7_plus-review-1508p3.php)           |


### 6.2 Master 44-Device Duration & Speed Score Prediction Matrix


| Smartphone Device Model      | Benchmark T_A | Predicted T_C | Duration Error dT | Error % | Benchmark S_A | Dedicated S_C(S1) | Score Error dS(S1) | Common S_C(S2) | Score Error dS(S2) |
| :--------------------------- | :-----------: | :-----------: | :---------------: | :-----: | :-----------: | :---------------: | :----------------: | :------------: | :----------------: |
| **Realme GT3**               | 9.6 m         | 11.6 m        | +2.0 m            | +20.8%  | 9.80 pts      | 10.00 pts         | +0.20 pts          | 9.23 pts       | -0.58 pts          |
| **Redmi Note 12 Explorer**   | 9.0 m         | 12.4 m        | +3.4 m            | +37.8%  | 10.00 pts     | 9.78 pts          | -0.22 pts          | 9.03 pts       | -0.97 pts          |
| **iQOO 11 Pro**              | 12.0 m        | 14.0 m        | +2.0 m            | +16.7%  | 9.12 pts      | 9.38 pts          | +0.25 pts          | 8.66 pts       | -0.47 pts          |
| **Motorola Edge 50 Pro**     | 18.0 m        | 20.4 m        | +2.4 m            | +13.3%  | 7.89 pts      | 8.14 pts          | +0.25 pts          | 7.51 pts       | -0.38 pts          |
| **Xiaomi 13 Pro**            | 19.0 m        | 22.5 m        | +3.5 m            | +18.4%  | 7.73 pts      | 7.81 pts          | +0.09 pts          | 7.21 pts       | -0.51 pts          |
| **Xiaomi 12T Pro**           | 19.0 m        | 23.2 m        | +4.2 m            | +22.1%  | 7.73 pts      | 7.71 pts          | -0.01 pts          | 7.12 pts       | -0.61 pts          |
| **Poco F4 GT**               | 17.0 m        | 22.0 m        | +5.0 m            | +29.4%  | 8.07 pts      | 7.89 pts          | -0.18 pts          | 7.28 pts       | -0.78 pts          |
| **Vivo X100 Pro**            | 31.0 m        | 28.9 m        | -2.1 m            | -6.8%   | 6.24 pts      | 6.99 pts          | +0.75 pts          | 6.45 pts       | +0.21 pts          |
| **OnePlus 12**               | 26.0 m        | 28.9 m        | +2.9 m            | +11.2%  | 6.77 pts      | 6.99 pts          | +0.21 pts          | 6.45 pts       | -0.32 pts          |
| **OnePlus 11**               | 25.0 m        | 27.1 m        | +2.1 m            | +8.4%   | 6.89 pts      | 7.20 pts          | +0.31 pts          | 6.65 pts       | -0.25 pts          |
| **OnePlus 12R**              | 32.0 m        | 35.2 m        | +3.2 m            | +10.0%  | 6.14 pts      | 6.34 pts          | +0.20 pts          | 5.85 pts       | -0.29 pts          |
| **Asus ROG Phone 7**         | 42.0 m        | 42.0 m        | +0.0 m            | +0.0%   | 5.31 pts      | 5.75 pts          | +0.44 pts          | 5.31 pts       | +0.00 pts          |
| **Xiaomi 14**                | 35.0 m        | 29.0 m        | -6.0 m            | -17.1%  | 5.87 pts      | 6.98 pts          | +1.11 pts          | 6.44 pts       | +0.57 pts          |
| **Honor Magic 6 Pro**        | 36.0 m        | 38.7 m        | +2.7 m            | +7.5%   | 5.78 pts      | 6.02 pts          | +0.24 pts          | 5.56 pts       | -0.22 pts          |
| **Motorola Edge 40**         | 44.0 m        | 36.8 m        | -7.2 m            | -16.4%  | 5.17 pts      | 6.19 pts          | +1.02 pts          | 5.72 pts       | +0.54 pts          |
| **Xiaomi 13**                | 42.0 m        | 37.3 m        | -4.7 m            | -11.2%  | 5.31 pts      | 6.15 pts          | +0.83 pts          | 5.68 pts       | +0.36 pts          |
| **Honor Magic 5 Pro**        | 48.0 m        | 42.4 m        | -5.6 m            | -11.7%  | 4.91 pts      | 5.72 pts          | +0.81 pts          | 5.29 pts       | +0.38 pts          |
| **Samsung Galaxy S24 Ultra** | 59.0 m        | 59.0 m        | +0.0 m            | +0.0%   | 4.28 pts      | 4.63 pts          | +0.35 pts          | 4.28 pts       | +0.00 pts          |
| **Samsung Galaxy S23 Ultra** | 59.0 m        | 59.0 m        | +0.0 m            | +0.0%   | 4.28 pts      | 4.63 pts          | +0.35 pts          | 4.28 pts       | +0.00 pts          |
| **Samsung Galaxy S22 Ultra** | 59.0 m        | 59.0 m        | +0.0 m            | +0.0%   | 4.28 pts      | 4.63 pts          | +0.35 pts          | 4.28 pts       | +0.00 pts          |
| **Nothing Phone (2)**        | 55.0 m        | 55.8 m        | +0.8 m            | +1.5%   | 4.49 pts      | 4.82 pts          | +0.32 pts          | 4.45 pts       | -0.04 pts          |
| **Google Pixel 9 Pro XL**    | 79.0 m        | 71.2 m        | -7.8 m            | -9.9%   | 3.39 pts      | 4.01 pts          | +0.62 pts          | 3.71 pts       | +0.32 pts          |
| **Google Pixel 8 Pro**       | 81.0 m        | 86.0 m        | +5.0 m            | +6.2%   | 3.32 pts      | 3.39 pts          | +0.07 pts          | 3.13 pts       | -0.18 pts          |
| **Samsung Galaxy S24**       | 75.0 m        | 82.1 m        | +7.1 m            | +9.5%   | 3.55 pts      | 3.54 pts          | -0.01 pts          | 3.28 pts       | -0.28 pts          |
| **Samsung Galaxy S23**       | 80.0 m        | 80.3 m        | +0.3 m            | +0.4%   | 3.35 pts      | 3.62 pts          | +0.26 pts          | 3.34 pts       | -0.01 pts          |
| **Samsung Galaxy A55**       | 85.0 m        | 100.4 m       | +15.4 m           | +18.1%  | 3.17 pts      | 2.88 pts          | -0.29 pts          | 2.66 pts       | -0.51 pts          |
| **Samsung Galaxy A54**       | 82.0 m        | 100.4 m       | +18.4 m           | +22.4%  | 3.28 pts      | 2.88 pts          | -0.40 pts          | 2.66 pts       | -0.62 pts          |
| **Samsung Galaxy A34**       | 84.0 m        | 100.4 m       | +16.4 m           | +19.5%  | 3.21 pts      | 2.88 pts          | -0.33 pts          | 2.66 pts       | -0.54 pts          |
| **Google Pixel 7 Pro**       | 109.0 m       | 108.2 m       | -0.8 m            | -0.7%   | 2.41 pts      | 2.63 pts          | +0.22 pts          | 2.44 pts       | +0.02 pts          |
| **Samsung Galaxy S10**       | 108.0 m       | 112.4 m       | +4.4 m            | +4.1%   | 2.44 pts      | 2.51 pts          | +0.06 pts          | 2.32 pts       | -0.12 pts          |
| **Samsung Galaxy S9**        | 107.0 m       | 100.4 m       | -6.6 m            | -6.2%   | 2.47 pts      | 2.88 pts          | +0.41 pts          | 2.66 pts       | +0.19 pts          |
| **Samsung Galaxy S8**        | 100.0 m       | 100.4 m       | +0.4 m            | +0.4%   | 2.68 pts      | 2.88 pts          | +0.20 pts          | 2.66 pts       | -0.01 pts          |
| **Nokia 2.4**                | 215.0 m       | 215.1 m       | +0.1 m            | +0.0%   | 0.35 pts      | 0.36 pts          | +0.02 pts          | 0.35 pts       | -0.00 pts          |
| **Samsung Galaxy A03 Core**  | 205.0 m       | 202.6 m       | -2.4 m            | -1.2%   | 0.49 pts      | 0.56 pts          | +0.07 pts          | 0.53 pts       | +0.04 pts          |
| **Apple iPhone 16 Pro Max**  | 117.0 m       | 80.4 m        | -36.6 m           | -31.3%  | 2.20 pts      | 3.61 pts          | +1.41 pts          | 3.34 pts       | +1.14 pts          |
| **Apple iPhone 14 Pro Max**  | 112.0 m       | 77.0 m        | -35.0 m           | -31.2%  | 2.33 pts      | 3.75 pts          | +1.42 pts          | 3.47 pts       | +1.14 pts          |
| **Apple iPhone 15 Pro Max**  | 109.0 m       | 83.9 m        | -25.1 m           | -23.0%  | 2.41 pts      | 3.47 pts          | +1.06 pts          | 3.21 pts       | +0.80 pts          |
| **Apple iPhone 13 Pro Max**  | 106.0 m       | 82.7 m        | -23.3 m           | -22.0%  | 2.50 pts      | 3.52 pts          | +1.02 pts          | 3.25 pts       | +0.76 pts          |
| **Apple iPhone 11 Pro Max**  | 120.0 m       | 108.1 m       | -11.9 m           | -9.9%   | 2.12 pts      | 2.63 pts          | +0.51 pts          | 2.44 pts       | +0.32 pts          |
| **LG G7 ThinQ**              | 108.0 m       | 85.2 m        | -22.8 m           | -21.1%  | 2.44 pts      | 3.42 pts          | +0.98 pts          | 3.16 pts       | +0.72 pts          |
| **Apple iPhone XS Max**      | 131.0 m       | 104.6 m       | -26.4 m           | -20.2%  | 1.85 pts      | 2.74 pts          | +0.89 pts          | 2.54 pts       | +0.68 pts          |
| **Apple iPhone X**           | 125.0 m       | 91.6 m        | -33.4 m           | -26.7%  | 2.00 pts      | 3.18 pts          | +1.18 pts          | 2.94 pts       | +0.95 pts          |
| **Apple iPhone 8**           | 148.0 m       | 170.1 m       | +22.1 m           | +14.9%  | 1.48 pts      | 1.14 pts          | -0.34 pts          | 1.06 pts       | -0.42 pts          |
| **Apple iPhone 7 Plus**      | 241.0 m       | 240.2 m       | -0.8 m            | -0.3%   | 0.00 pts      | 0.00 pts          | +0.00 pts          | 0.01 pts       | +0.01 pts          |

---

## 7. Data Integrity & Hardware Verification Guidelines

To ensure future iterations of the charging model maintain physical validity and eliminate data corruption risks, the following mandatory data integrity rules MUST be enforced across all input dataset updates:


1. **Strict 4-Tier Evidence Hierarchy for Maximum Charging Input Power (`P_peak`):**

   * `P_peak` represents the phone's actual accepted physical input power in Watts (W), NOT the wall charger output rating.

   * *Hierarchy:* (1) Measured Direct Current (`DC`) / Alternating Current (`AC`) input power from laboratory meters (e.g., ChargerLAB or Notebookcheck); (2) Official manufacturer accepted input wattage; (3) Documented charging mode capabilities; (4) Inferred from charger (strictly forbidden if phone input differs).


2. **Cell Architecture Verification Protocol (Single-Cell 1S vs Dual-Cell Series 2S):**

   * Cell architecture MUST NOT be inferred from marketing claims or wattage thresholds alone.

   * Dual-Cell Series Configuration (2S) operating at 7.70V nominal halves electrical current for a given wattage. While internal cell heating remains identical, this reduces motherboard trace and connector resistive heating (`P_loss = I^2 * R_trace`) by 75%. All high-power series implementations (125W TurboPower, 80W–100W SuperVOOC, 65W–120W HyperCharge) MUST be verified via official teardowns and correctly assigned `C0_dual`.


3. **Exact Stored Battery Energy (`E_supply`) & Nominal Voltage (`V_nominal`):**

   * Exact Watt-hour (Wh) energy ratings printed on official battery cell labels MUST be used where published.

   * When calculating energy from Milliampere-hours (mAh), single-cell nominal voltage `V_nominal = 3.85V` applies unless explicit cell specs (e.g., Apple 3.79V–3.84V) or 2S series configurations (7.70V) dictate otherwise.
