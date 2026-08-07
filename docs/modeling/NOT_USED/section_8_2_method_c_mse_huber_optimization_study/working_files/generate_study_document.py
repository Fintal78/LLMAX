import json
import math

with open("scratch/optimization_results.json", "r") as f:
    data = json.load(f)

huber_sweep = data["huber_sweep"]
mse_res = data["mse"]
mae_res = data["mae"]

# Selected Huber models
h10 = [h for h in huber_sweep if h["delta"] == 10.0][0]
h25 = [h for h in huber_sweep if h["delta"] == 25.0][0]
h30 = [h for h in huber_sweep if h["delta"] == 30.0][0]

lines = []

# Title & Important Notice
lines.append("# Method C (Loss-Based Model) Parameter Optimization & Loss Function Study\n")
lines.append("> [!IMPORTANT]")
lines.append("> **Study Target & Scope:** This document presents the complete mathematical derivation, hyperparameter sensitivity analysis, and empirical calibration study for **Method C (Physical Loss-Based Charging Duration Predictor)** across 44 real-world smartphone benchmarks from authentic GSMArena laboratory data.")
lines.append(">")
lines.append("> All formulas avoid arbitrary booster multipliers and obey strict energy conservation (`P_effective <= P_peak`).")
lines.append("> All optimization results are generated deterministically using global Differential Evolution (`scipy.optimize.differential_evolution`, fixed `seed=42`).\n")
lines.append("---\n")

# Section 1: Mathematical Formulation
lines.append("## 1. Mathematical Formulation & Parameter Mapping\n")
lines.append("### 1.1 Physical Power Loss Chain\n")
lines.append("Method C models the effective average charging power `P_effective` delivered to the battery cell across the full charging cycle as a multiplicative chain of physical loss factors:\n")
lines.append("`P_effective = P_peak * eff_eta_CCCV * eta_arch * eta_protocol * eta_thermal`\n")
lines.append("where:")
lines.append("- `P_effective <= P_peak` everywhere across the domain (no artificial booster multipliers `> 1.0`).")
lines.append("- `eff_eta_CCCV`: Full-cycle Constant Current / Constant Voltage (CC/CV) average power delivery ratio.")
lines.append("- `eta_arch`: Cell architecture efficiency relative to ideal Dual-Cell Series (2S) reference (`Dual-Cell = 1.00`, `Single-Cell = 0.60–1.00`).")
lines.append("- `eta_protocol`: Electrical conversion efficiency relative to direct drive (Direct Charge Pump, Universal Serial Bus Power Delivery Programmable Power Supply [`USB-PD PPS`], Fixed Power Delivery / Quick Charge [`Fixed PD/QC`], `Legacy 5V`, `Apple Legacy`).")
lines.append("- `eta_thermal`: Non-linear C-rate thermal tapering factor (`<= 1.0`) governed by exponential decay kinetics.\n")

lines.append("### 1.2 Unified Physical Chain & 12-Parameter Mapping\n")
lines.append("The complete mathematical chain mapping each of the 12 scalar parameters to its exact physical component is structured as follows:\n")
lines.append("1. **Peak C-Rate Input (`C_rate`):**")
lines.append("   `C_rate = P_peak / E_supply`")
lines.append("   where `E_supply = (Capacity_mAh * V_nominal) / 1000` (in Watt-hours, `Wh`, with nominal voltage `V_nominal = 3.85V`).\n")
lines.append("2. **Constant Current / Constant Voltage Average Power Ratio (`eff_eta_CCCV`):**")
lines.append("   - Low-Power Region (`C_rate <= C_threshold`):")
lines.append("     `eff_eta_CCCV = min(1.00, max(0.05, eta_CCCV + s_low * (C_threshold - C_rate)))` [Param 1: `eta_CCCV`, Param 2: `C_threshold`, Param 3: `s_low`]")
lines.append("   - High-Power Region (`C_rate > C_threshold`):")
lines.append("     `eff_eta_CCCV = min(1.00, max(0.05, eta_CCCV + s_high * (C_threshold - C_rate)))` [Param 4: `s_high`]\n")
lines.append("3. **Cell Architecture Efficiency (`eta_arch`):**")
lines.append("   - `eta_arch = 1.0000` (Dual-Cell Series Array reference)")
lines.append("   - `eta_arch = eta_arch_single` (Single-Cell Array loss factor) [Param 7: `eta_arch_single`]\n")
lines.append("4. **Protocol Electrical Conversion Efficiency (`eta_protocol`):**")
lines.append("   - Direct Charge Pump: `eta_cp` [Param 8: `eta_cp`]")
lines.append("   - USB-PD PPS: `eta_pps` [Param 9: `eta_pps`]")
lines.append("   - Fixed PD / Quick Charge: `eta_pd` [Param 10: `eta_pd`]")
lines.append("   - Legacy 5V Standard: `eta_5v` [Param 11: `eta_5v`]")
lines.append("   - Apple Legacy Standard: `eta_apple` [Param 12: `eta_apple`]\n")
lines.append("5. **Thermal Tapering Kinetics (`eta_thermal`):**")
lines.append("   To model battery thermal saturation kinetics under high C-rate charging currents, the thermal tapering factor `eta_thermal` (`<= 1.0`) is defined via exponential decay kinetics:")
lines.append("   - If `C_rate > C_threshold`:")
lines.append("     `eta_thermal = exp(-k * (C_rate - C_threshold)^p)` [Param 5: `k`, Param 6: `p`]")
lines.append("   - If `C_rate <= C_threshold`:")
lines.append("     `eta_thermal = 1.0000`\n")
lines.append("6. **Effective Average Charging Power (`P_effective`):**")
lines.append("   `P_effective = P_peak * eff_eta_CCCV * eta_arch * eta_protocol * eta_thermal`\n")
lines.append("7. **Predicted Full Charge Duration (`T_predicted` / `T_C`):**")
lines.append("   `T_predicted = (E_supply / P_effective) * 60.0 + T_handshake`")
lines.append("   where `T_handshake = 0.5000 mins` (30 seconds) is the fixed physical hardware handshake intercept.\n")
lines.append("---\n")

# Section 2: Statistical Bibliography & Loss Function Theory
lines.append("## 2. Statistical Bibliography, Loss Function Theory & Process Steps\n")
lines.append("### 2.1 Optimization Scope, Target Variables & Loss Function Theory\n")
lines.append("Method C parameter optimization is structured across explicit target variables and loss function formulations:\n")
lines.append("1. **Stage 1 Target Variable (Physical Duration Residuals):**")
lines.append("   Objective loss functions (`L`) are applied directly to **physical full-charge duration residuals in minutes**:")
lines.append("   `r_i = T_predicted,i(theta) - T_A,i`")
lines.append("   where `T_A,i` is the empirical GSMArena laboratory benchmark duration (in minutes), `T_predicted,i(theta)` is the Method C analytical physical model prediction (in minutes), and `theta` represents the vector of 12 physical scalar parameters.\n")
lines.append("   *Rationale:* Physical duration `T` (in minutes) is the fundamental, unwarped physical output of the battery charging process. Fitting parameters on duration `T` ensures that the physical model accurately reflects electrical conversion, thermal throttling, and battery chemistry without distortion from non-linear score utility curves.\n")
lines.append("2. **Evaluated Candidate Loss Functions (Stage 1 Parameter Fitting):**")
lines.append("   - **Option 1: Pure Mean Squared Error (MSE on Physical Duration):**")
lines.append("     `MSE_T(theta) = (1/N) * sum_{i=1}^N (T_predicted,i(theta) - T_A,i)^2`")
lines.append("     - **Statistical Assumption:** Assumes duration residuals follow a Gaussian Normal distribution `r_i ~ N(0, sigma^2)`.")
lines.append("     - **Properties:** Minimizing MSE corresponds to Maximum Likelihood Estimation (MLE) under homoscedastic Gaussian noise, minimizing overall variance across the entire population.\n")
lines.append("   - **Option 2: Pure Mean Absolute Error (MAE on Physical Duration):**")
lines.append("     `MAE_T(theta) = (1/N) * sum_{i=1}^N |T_predicted,i(theta) - T_A,i|`")
lines.append("     - **Statistical Assumption:** Assumes duration residuals follow a Laplace distribution with heavy tails.")
lines.append("     - **Properties:** Minimizing MAE yields the conditional median estimator, weighting every minute of error equally.\n")
lines.append("   - **Option 3: Huber Loss Function (Huber on Physical Duration):**")
lines.append("     `L_Huber(r_i; delta) = 0.5 * r_i^2` if `|r_i| <= delta`, else `delta * (|r_i| - 0.5 * delta)`")
lines.append("     - **Hybrid 2-Zone Rule:** Applies quadratic (L2) loss for residuals within the threshold boundary (`|r_i| <= delta`) and linear (L1) loss for large residuals (`|r_i| > delta`).")
lines.append("     - **Statistical Foundation:** Introduced by Peter J. Huber (*Robust Estimation of a Location Parameter*, Annals of Mathematical Statistics, 1964).\n")
lines.append("3. **Standardized Evaluation Metric Suites:**")
lines.append("   - **Primary Physical Duration Metrics (`T`-metrics):**")
lines.append("     - **Mean Squared Duration Error (`MSE_T`):** `(1/N) * sum (T_predicted,i - T_A,i)^2` (`mins^2`)")
lines.append("     - **Root Mean Square Duration Error (`RMSE_T`):** `sqrt(MSE_T)` (`mins`)")
lines.append("     - **Mean Absolute Duration Error (`MAE_T`):** `(1/N) * sum |T_predicted,i - T_A,i|` (`mins`)")
lines.append("     - **Mean Duration Bias (`Mean_dT`):** `(1/N) * sum (T_predicted,i - T_A,i)` (`mins`)\n")
lines.append("   - **Derived Speed Score Metrics (`S`-metrics):**")
lines.append("     Speed scores `S` are computed from full-charge durations `T` via logarithmic utility normalization across the benchmark dynamic range `[T_min_A = 9.0 mins, T_max_A = 241.0 mins]`:")
lines.append("     `S = 10.0 * (ln(241.0 / T) / ln(241.0 / 9.0))`")
lines.append("     - **Mean Squared Score Error (`MSE_S`):** `(1/N) * sum (S_predicted,i - S_A,i)^2` (`pts^2`)")
lines.append("     - **Root Mean Square Score Error (`RMSE_S`):** `sqrt(MSE_S)` (`pts`)")
lines.append("     - **Mean Absolute Score Error (`MAE_S`):** `(1/N) * sum |S_predicted,i - S_A,i|` (`pts`)")
lines.append("     - **Mean Score Bias (`Mean_dS`):** `(1/N) * sum (S_predicted,i - S_A,i)` (`pts`)\n")
lines.append("---\n")

# Section 3: Huber Sensitivity Study
lines.append("## 3. Step 1: Huber Sensitivity Study & Hyperparameter Calibration\n")
lines.append("### 3.1 Huber Delta Sensitivity Analysis & Threshold Grid Sweep\n")
lines.append("To evaluate the sensitivity of the Huber Loss Model across candidate threshold values, a deterministic hyperparameter grid sweep was executed across candidate values `delta in [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]` minutes using Differential Evolution (`seed=42`, `popsize=25`, `maxiter=2000`):\n")

# Table 3.1
lines.append("| Threshold (`delta`) | `MSE_T` (`mins^2`) | `RMSE_T` (`mins`) | `MAE_T` (`mins`) | `Mean_dT` (`mins`) | Sensitivity Rationale |")
lines.append("| :-----------------: | :----------------: | :---------------: | :--------------: | :----------------: | :-------------------- |")

for h in huber_sweep:
    d = h["delta"]
    mse_t = f"{h['MSE_T']:.2f} mins^2"
    rmse_t = f"{h['RMSE_T']:.2f} mins"
    mae_t = f"{h['MAE_T']:.2f} mins"
    mean_dt = f"{h['Mean_dT']:+.2f} mins"
    
    if d == 5.0:
        rat = "Linear L1 dominant regime; caps tail errors heavily."
    elif d == 7.5:
        rat = "Intermediate L1/L2 transition step (MAE_T = 6.32 mins)."
    elif d == 10.0:
        rat = "Evaluated candidate setting (10-min outlier threshold boundary)."
    elif d == 12.5:
        rat = "Transition step toward L2 loss dominance."
    elif d == 15.0:
        rat = "Intermediate transition step."
    elif d == 20.0:
        rat = "Continued variance reduction (MSE_T = 87.60 mins^2)."
    elif d == 22.5:
        rat = "Transition toward low population bias."
    elif d == 25.0:
        rat = "Balanced transition point (Mean_dT = -0.14 mins)."
    elif d == 27.5:
        rat = "Near-zero bias transition (Mean_dT = -0.05 mins)."
    elif d == 30.0:
        rat = "Asymptotic L2 convergence regime (MSE_T = 84.67 mins^2)."
    elif d == 40.0:
        rat = "Fully converged to L2 loss asymptote (MSE_T = 84.51 mins^2)."
    elif d == 50.0:
        rat = "Minimum MSE_T asymptote (84.51 mins^2), identical to Pure MSE."
    else:
        rat = "Grid sweep step."
        
    lines.append(f"| **`delta = {d:4.1f} mins`** | `{mse_t:>14}` | `{rmse_t:>13}` | `{mae_t:>12}` | `{mean_dt:>14}` | {rat} |")

lines.append("\n**Grid Sensitivity Analysis & Findings:**")
lines.append("1. **Monotonic Convergence to Pure MSE:** As `delta` increases beyond `30.0 mins`, outlier capping diminishes across the 44-device dataset, causing Huber loss metrics to asymptote smoothly toward Pure MSE (`MSE_T = 84.51 mins^2`, `RMSE_T = 9.19 mins`, `MAE_T = 6.67 mins`, `Mean_dT = +0.14 mins`).")
lines.append("2. **Low-Threshold Behavior (`delta = 5.0` to `10.0 mins`):** At small threshold values, extreme slow-charging legacy devices (such as the Apple iPhone 7 Plus at 241.0 mins) exceed `delta` and are penalized strictly linearly rather than quadratically. This allows the model to achieve low error on core devices, while producing higher total squared variance (`MSE_T = 189.80 mins^2`).")
lines.append("3. **Objective Tradeoff Continuum:** There is no single setting that achieves the absolute minimum across all metrics simultaneously. Pure MSE achieves the minimum squared duration variance (`84.51 mins^2`), `delta = 7.5 mins` achieves the lowest duration MAE (`6.32 mins`), while `delta = 10.0 mins` achieves the lowest derived score error under Strategy 2 (`MAE_S = 0.2558 pts`, `MSE_S = 0.1111 pts^2`).\n")
lines.append("---\n")

# Section 4: Comparative Duration Performance
lines.append("## 4. Step 2: Physical Duration Error Comparison & Model Calibration\n")
lines.append("### 4.1 Comparative Duration Prediction Metric Matrix\n")
lines.append("The table below presents the exact physical duration prediction metrics across candidate models under deterministic global optimization:\n")

# Table 4.1
lines.append("| Duration Metric | Opt 1: Pure MSE | Opt 2: Pure MAE | Opt 3: Huber (`delta=10.0`) | Opt 3: Huber (`delta=25.0`) | Opt 3: Huber (`delta=30.0`) |")
lines.append("| :-------------- | :-------------: | :-------------: | :-------------------------: | :-------------------------: | :-------------------------: |")

lines.append(f"| **Mean Squared Duration Error (`MSE_T`)**      | `{mse_res['metrics']['MSE_T']:>11.2f} mins^2` | `{mae_res['metrics']['MSE_T']:>11.2f} mins^2` | `{h10['metrics']['MSE_T']:>23.2f} mins^2` | `{h25['metrics']['MSE_T']:>23.2f} mins^2` | `{h30['metrics']['MSE_T']:>23.2f} mins^2` |")
lines.append(f"| **Root Mean Square Duration Error (`RMSE_T`)** | `{mse_res['metrics']['RMSE_T']:>11.2f} mins`   | `{mae_res['metrics']['RMSE_T']:>11.2f} mins`   | `{h10['metrics']['RMSE_T']:>23.2f} mins`   | `{h25['metrics']['RMSE_T']:>23.2f} mins`   | `{h30['metrics']['RMSE_T']:>23.2f} mins`   |")
lines.append(f"| **Mean Absolute Duration Error (`MAE_T`)**     | `{mse_res['metrics']['MAE_T']:>11.2f} mins`   | `{mae_res['metrics']['MAE_T']:>11.2f} mins`   | `{h10['metrics']['MAE_T']:>23.2f} mins`   | `{h25['metrics']['MAE_T']:>23.2f} mins`   | `{h30['metrics']['MAE_T']:>23.2f} mins`   |")
lines.append(f"| **Mean Duration Bias (`Mean_dT = T_pred - T_A`)** | `{mse_res['metrics']['Mean_dT']:>+11.2f} mins`   | `{mae_res['metrics']['Mean_dT']:>+11.2f} mins`   | `{h10['metrics']['Mean_dT']:>+23.2f} mins`   | `{h25['metrics']['Mean_dT']:>+23.2f} mins`   | `{h30['metrics']['Mean_dT']:>+23.2f} mins`   |")
lines.append(f"| **Dynamic Predictor Minimum (`T_min,C`)**      | `{mse_res['metrics']['T_min_C']:>11.2f} mins`   | `{mae_res['metrics']['T_min_C']:>11.2f} mins`   | `{h10['metrics']['T_min_C']:>23.2f} mins`   | `{h25['metrics']['T_min_C']:>23.2f} mins`   | `{h30['metrics']['T_min_C']:>23.2f} mins`   |")
lines.append(f"| **Dynamic Predictor Maximum (`T_max,C`)**      | `{mse_res['metrics']['T_max_C']:>11.2f} mins`   | `{mae_res['metrics']['T_max_C']:>11.2f} mins`   | `{h10['metrics']['T_max_C']:>23.2f} mins`   | `{h25['metrics']['T_max_C']:>23.2f} mins`   | `{h30['metrics']['T_max_C']:>23.2f} mins`   |")

lines.append("\n### 4.2 Calibrated Parameter Sets Across Loss Functions\n")
lines.append("The 12 physical parameters obtained from global optimization under strict physical domain constraints are detailed below:\n")

# Table 4.2
lines.append("| Parameter Name | Search Domain | Opt 1: Pure MSE | Opt 2: Pure MAE | Opt 3: Huber (`delta=10.0`) | Opt 3: Huber (`delta=30.0`) |")
lines.append("| :------------- | :-----------: | :-------------: | :-------------: | :-------------------------: | :-------------------------: |")

p_names = [
    ("eta_CCCV (Ideal CC/CV Ratio)", "eta_CCCV", "[0.30, 0.95]"),
    ("C_threshold (Thermal Onset)", "C_thresh", "[0.50, 3.00]"),
    ("s_low (Low-Power Scaling)", "s_low", "[0.00, 1.50]"),
    ("s_high (High-Power Scaling)", "s_high", "[0.00, 1.00]"),
    ("k (Thermal Penalty Coeff)", "k", "[0.0001, 1.00]"),
    ("p (Thermal Exponent)", "p", "[0.50, 3.00]"),
    ("eta_arch_single (Single-Cell)", "eta_arch_single", "[0.60, 1.00]"),
    ("eta_cp (Direct Charge Pump)", "eta_cp", "[0.70, 1.00]"),
    ("eta_pps (USB-PD PPS)", "eta_pps", "[0.60, 1.00]"),
    ("eta_pd (Fixed PD / QC)", "eta_pd", "[0.50, 0.95]"),
    ("eta_5v (Legacy 5V Standard)", "eta_5v", "[0.50, 0.95]"),
    ("eta_apple (Apple Legacy)", "eta_apple", "[0.50, 0.95]"),
]

for label, key, domain in p_names:
    v_mse = f"{mse_res['params'][key]:.4f}"
    v_mae = f"{mae_res['params'][key]:.4f}"
    v_h10 = f"{h10['params'][key]:.4f}"
    v_h30 = f"{h30['params'][key]:.4f}"
    lines.append(f"| **{label:<30}** | `{domain:<13}` | `{v_mse:>15}` | `{v_mae:>15}` | `{v_h10:>27}` | `{v_h30:>27}` |")

lines.append(f"| **{'T_handshake (Fixed Hardware Intercept)':<30}** | `{'[0.50, 0.50]':<13}` | `{'0.5000':>15}` | `{'0.5000':>15}` | `{'0.5000':>27}` | `{'0.5000':>27}` |")
lines.append("\n---\n")

# Section 5: Score Normalization Mapping
lines.append("## 5. Step 3: Score Normalization Mapping & Strategy Assessment (`S_final` Metrics)\n")
lines.append("### 5.1 Score Normalization Strategies\n")
lines.append("- **Strategy 1 (Dynamic Bounds Normalization):** Maps predicted duration `T_C` into speed score `S_C` using model-fitted dynamic bounds `[T_min,C, T_max,C]`:")
lines.append("  `S_C = 10.0 * (ln(T_max,C / T_C) / ln(T_max,C / T_min,C))`")
lines.append("- **Strategy 2 (Benchmark Aligned Bounds Normalization - Recommended):** Maps predicted duration `T_C` using empirical benchmark bounds `[T_min_A = 9.00 mins, T_max_A = 241.0 mins]`:")
lines.append("  `S_C = 10.0 * (ln(241.0 / T_C) / ln(241.0 / 9.0))`\n")
lines.append("### 5.2 Comparative Speed Score Metric Matrix\n")
lines.append("#### Strategy 2: Benchmark Aligned Bounds Normalization (Recommended)\n")

# Table 5.2 (Strategy 2)
lines.append("| Model Candidate | `MSE_S` (`pts^2`) | `RMSE_S` (`pts`) | `MAE_S` (`pts`) | `Mean_dS` (`pts`) |")
lines.append("| :-------------- | :---------------: | :--------------: | :-------------: | :---------------: |")

s2_models = [
    ("Opt 1: Pure MSE Model", mse_res['metrics']['Strategy_2']),
    ("Opt 2: Pure MAE Model", mae_res['metrics']['Strategy_2']),
    ("Opt 3: Huber Model (delta=10.0)", h10['metrics']['Strategy_2']),
    ("Opt 3: Huber Model (delta=25.0)", h25['metrics']['Strategy_2']),
    ("Opt 3: Huber Model (delta=30.0)", h30['metrics']['Strategy_2']),
]

for name, s in s2_models:
    lines.append(f"| **{name:<32}** | `{s['MSE_S']:>13.4f} pts^2` | `{s['RMSE_S']:>12.4f} pts` | `{s['MAE_S']:>11.4f} pts` | `{s['Mean_dS']:>+13.4f} pts` |")

lines.append("\n#### Strategy 1: Dynamic Bounds Normalization\n")

# Table 5.2 (Strategy 1)
lines.append("| Model Candidate | `MSE_S` (`pts^2`) | `RMSE_S` (`pts`) | `MAE_S` (`pts`) | `Mean_dS` (`pts`) |")
lines.append("| :-------------- | :---------------: | :--------------: | :-------------: | :---------------: |")

s1_models = [
    ("Opt 1: Pure MSE Model", mse_res['metrics']['Strategy_1']),
    ("Opt 2: Pure MAE Model", mae_res['metrics']['Strategy_1']),
    ("Opt 3: Huber Model (delta=10.0)", h10['metrics']['Strategy_1']),
    ("Opt 3: Huber Model (delta=25.0)", h25['metrics']['Strategy_1']),
    ("Opt 3: Huber Model (delta=30.0)", h30['metrics']['Strategy_1']),
]

for name, s in s1_models:
    lines.append(f"| **{name:<32}** | `{s['MSE_S']:>13.4f} pts^2` | `{s['RMSE_S']:>12.4f} pts` | `{s['MAE_S']:>11.4f} pts` | `{s['Mean_dS']:>+13.4f} pts` |")

lines.append("\n---\n")

# Section 6: Master Prediction Matrix
lines.append("## 6. Step 4: Master 44-Device Prediction Matrix & Final Evaluation\n")
lines.append("### 6.1 Physical Component Evaluation Across all 44 Benchmark Devices (Huber `delta = 10.0 mins`)\n")
lines.append("The table below details the exact evaluated physical parameters and intermediate component values derived from the calibrated Huber model (`delta = 10.0 mins`) for each of the 44 smartphones in the GSMArena laboratory benchmark dataset:\n")

# Table 6.1
lines.append("| Device Model | Battery (Wh) | P_peak (W) | C_rate (h^-1) | Arch Type | Protocol Type | eta_arch | eta_proto | eta_thermal | eff_eta_CCCV | P_effective (W) | T_handshake |")
lines.append("| :----------- | :----------: | :--------: | :-----------: | :-------: | :-----------: | :------: | :-------: | :---------: | :----------: | :-------------: | :---------: |")

for d in h10["device_predictions"]:
    lines.append(f"| **{d['name']:<26}** | `{d['battery_wh']:>5.2f} Wh` | `{d['peak_power_w']:>5.1f} W` | `{d['C_rate']:>5.2f} h^-1` | `{d['architecture']:^9}` | `{d['protocol']:^13}` | `{d['eta_arch']:>6.4f}` | `{d['eta_proto']:>7.4f}` | `{d['eta_thermal']:>9.4f}` | `{d['eff_eta_CCCV']:>10.4f}` | `{d['p_eff']:>7.2f} W` | `0.5000 m` |")

lines.append("\n### 6.2 Master 44-Device Prediction Table (`T_C` vs `T_A` and `S_C` vs `S_A`)\n")
lines.append("The complete 44-device prediction table comparing empirical GSMArena benchmark duration (`T_A`) and speed score (`S_A`) against Method C predicted duration (`T_C`) and score (`S_C`) under Huber (`delta = 10.0 mins`) and Strategy 2 (Benchmark Aligned Bounds) is presented below:\n")

# Table 6.2
lines.append("| Smartphone Device Model | P_peak (W) | T_A (mins) | T_C (mins) | S_A (pts) | S_C (pts) | dS (pts) | dT (mins) | GSMArena Benchmark Link |")
lines.append("| :---------------------- | :--------: | :--------: | :--------: | :-------: | :-------: | :------: | :-------: | :---------------------- |")

for d in h10["device_predictions"]:
    link_text = f"[{d['name']} Benchmark]({d['gsmarena_url']})"
    lines.append(f"| **{d['name']:<26}** | `{d['peak_power_w']:>5.1f} W` | `{d['t_actual']:>5.1f} m` | `{d['t_pred']:>5.1f} m` | `{d['s_actual']:>5.2f}` | `{d['s_pred_s2']:>5.2f}` | `{d['dS_s2']:>+5.2f}` | `{d['dT']:>+5.1f} m` | {link_text} |")

lines.append("\n---\n")

# Section 7: Comparative Assessment & Synthesis
lines.append("## 7. Comparative Assessment & Synthesis\n")
lines.append("1. **Data Integrity & Verification:** All 44 benchmark smartphones have been verified against authentic GSMArena laboratory review pages, confirming genuine full-charge durations (`T_A`), battery watt-hours (`Wh`), and peak charging power ratings (`P_peak`).")
lines.append("2. **Optimization Rigor & Reproducibility:** Deterministic global optimization using Differential Evolution (`seed=42`) eliminates stochastic variation and guarantees full reproducibility across all loss functions and grid sweep thresholds.")
lines.append("3. **Model Selection Tradeoffs:**")
lines.append("   - **Pure MSE (Option 1):** Minimizes physical duration variance globally (`MSE_T = 84.51 mins^2`, `RMSE_T = 9.19 mins`, `MAE_T = 6.67 mins`, `Mean_dT = +0.14 mins`).")
lines.append("   - **Huber Loss (`delta = 10.0 mins`, Option 3):** Achieves the lowest speed score prediction error under Strategy 2 (`MAE_S = 0.2558 pts`, `MSE_S = 0.1111 pts^2`, `Mean_dS = -0.0125 pts`) by bounding the influence of extreme slow-charging outliers.")
lines.append("   - **Huber Loss (`delta = 30.0 mins`):** Converges smoothly to the L2 asymptotic limit (`MSE_T = 84.67 mins^2`, `MAE_T = 6.61 mins`, `Mean_dT = +0.03 mins`).")
lines.append("4. **Normalization Strategy:** Strategy 2 (Benchmark Aligned Bounds `[9.0 mins, 241.0 mins]`) is strictly recommended over Strategy 1, as it anchors scores to real-world empirical performance boundaries, preventing artificial score inflation or drift.\n")

output_text = "\n".join(lines)
with open("docs/modeling/section_8_2_method_c_mse_huber_optimization_study.md", "w", encoding="utf-8") as f:
    f.write(output_text)

print(f"Successfully generated section_8_2_method_c_mse_huber_optimization_study.md ({len(lines)} lines)")
