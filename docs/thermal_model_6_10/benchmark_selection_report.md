# REPORT: BENCHMARK SELECTION MATRIX (SECTION 6.10 AGENT)

## 1. Objective
To select the authoritative empirical benchmark for validating the Physics-Based Thermodynamic RC Model. The chosen benchmark must be transparent, widely available, and scientifically aligned with our Power (Wattage) modeling.

## 2. Selection Criteria & Weights

| Criteria               | Description                                                             | Weight  |
| :-------------------- -| :---------------------------------------------------------------------- | :------ |
| **Breadth (B)**        | Number of brands, models, and platforms (iOS/Android/Windows) covered.  | **30%** |
| **Model Alignment (A)**| Ability to measure **Watts** or thermal power directly vs. just FPS.    | **25%** |
| **Transparency (T)**   | Disclosure of measurement methods (Queries vs. Timers) and raw logs.    | **20%** |
| **Reputation (R)**     | Industry adoption and status as a "standard" in tech reviews.           | **15%** |
| **Accessibility (C)**  | Ease of use for typical users/evaluators to verify scores.              | **10%** |

## 3. Candidate Scoring (1-10 Scale)

| Benchmark                     | B (30%) | A (25%) | T (20%) | R (15%) | C (10%) | Weighted Total |
| :---------------------------- | :-----: | :-----: | :-----: | :-----: | :-----: | :------------: |
| **3DMark (Wild Life Extreme)**|    10   |    6    |    9    |    10   |    9    |     **8.7**    |
| **Burnout Benchmark**         |    5    |    10   |    8    |    7    |    7    |     **7.4**    |
| **GFXBench (Manhattan)**      |    9    |    6    |    7    |    8    |    8    |     **7.6**    |
| **Geekbench 6 (GPU)**         |    10   |    4    |    6    |    10   |    10   |     **7.7**    |

---

## 4. Deep-Dive Analysis

### 🏆 1st Place: 3DMark Wild Life Extreme (UL Solutions)
*   **Why it wins:** Its **Breadth** is unmatched. For a database that aims to score "all phones," 3DMark provides the only consistent data point across Apple, Samsung, Xiaomi, and obscure brands.
*   **Transparency:** Uses **Vulkan/Metal GPU Timestamps**, making it highly credible.
*   **The Alignment Gap:** While it measures FPS, our **0.40 Gamma Factor** provides a mathematically rigorous bridge to our internal Power (Watt) model.

### 🥈 2nd Place: Burnout Benchmark (Andrey Belyaev)
*   **The "Scientific Choice":** This is the only tool that allows **direct model-to-wattage comparison**. If we were only scoring Android flagships, this would be #1.
*   **The Bottleneck:** It lacks iOS support and a comprehensive public database for older/budget devices, failing our "Breadth" requirement.

---

## 5. Final Selection: THE DUAL-STANDARD RULE

To ensure maximum accuracy without sacrificing database breadth, the scoring framework will adopt a **Dual-Standard approach**:

1.  **Primary Standard (3DMark Wild Life Extreme Stability %):** Used for **Final Scoring** and cross-brand comparisons. Validates the end-user experience (FPS).
2.  **Calibration standard (Burnout Benchmark):** Used for **Model Tuning** and validating the 3.57W steady-state physics on new flagship releases. Validates the raw electricity (Watts).

> [!IMPORTANT]
> By using 3DMark as the primary anchor and Burnout as the calibration tool, we ensure the framework is both **empirically universal** and **physically accurate**.
