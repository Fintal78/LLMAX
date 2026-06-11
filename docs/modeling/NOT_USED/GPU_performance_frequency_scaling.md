> [!CAUTION]
> ⚠️⚠️⚠️ **THIS MODEL IS NO LONGER IN USE**
>
> This document describes a frequency scaling model (the **Computed Throughput Index — CTI**) that was developed for and initially integrated into the GPU Standard Graphics scoring pipeline (§ 6.3). It has since been **removed and replaced** by the simpler approach described in the active `scoring_rules.md`.
>
> **Why this model was removed:**
>
> The CTI model was applied directly to perceptual scores — that is, the GPU's architecture score (GAS, on the 0–10 scale which in that case was supposed to be a perceptual score and NOT a raw performance score) was used as the input to the scoring model. Because the model's diminishing-returns term `(1 − k·G)` grows weaker as the score `G` increases, high-performance GPU configurations were compressed more than low-performance ones relative to their true physical scaling.
>
> **Why the current model does not need it:**
>
> The active pipeline decouples the two concerns cleanly:
> 1. **Frequency scaling** is applied first, in the near-linear physics domain: `GPU_Yield = Standard_Graphics_Score × (R ^ γ)`. Here, `Standard_Graphics_Score` is a *linear* proxy for raw throughput (and NOT a perceptual score), and `R ^ γ` is a simple power-law frequency ratio. No perceptual component is introduced at this stage.
> 2. **Perceptual compression** (Weber-Fechner logarithmic normalization) is applied *afterwards*, in a single, uniform step: `GPU_Yield_norm = 10 × (log(GPU_Yield_Adjusted) − log(GPU_Yield_Adjusted_Min)) / (log(GPU_Yield_Adjusted_Max) − log(GPU_Yield_Adjusted_Min))`. Because the logarithm is applied to the *output* of the physics layer rather than to the input, it compresses all configurations on the same scale — naturally and uniformly squishing high-performance yields more than low-performance yields without any architecture-dependent term.

---

# GPU Performance Frequency Scaling Model: Complete Mathematical Analysis

## Executive Summary & Context

The goal of this document is to establish a mathematically rigorous, unified, and clamp-free GPU frequency scaling model that reconciles human perceptual limits with physical system constraints. Historically, dynamic performance adjustments (overclocking and underclocking) have been modeled using arbitrary exponents and empirical correction coefficients that often suffered from numerical clamping at hardware boundaries. 

To overcome these limitations, the scaling of the performance index with frequency is modeled using a two-phase analytical framework:
1. **Human Perceptual Scaling (Part 1):** We first solve a non-linear ordinary differential equation (ODE) based on the psychophysical principles of Weber's Law. This models the human eye's diminishing marginal sensitivity to frame rate increases as performance scales from budget tiers to flagships.
2. **Physical Headroom Modifier (Part 2):** We then overlay a system-wide support index to model physical reality. Modern SoCs share thermal budgets, memory bandwidth, and CPU cores. When the GPU is overclocked, it cannot scale in a vacuum; if the rest of the system (CPU, RAM speed, cooling stack) cannot support this throughput, a performance bottleneck is triggered. This is captured by the System Support Index (SSI).

The resulting Computed Throughput Index (CTI) scales dynamically relative to the baseline Graphics Architecture Score (GAS). This document provides the complete step-by-step mathematical derivation, empirical calibration, edge case safety checks, and exhaustive sweep verifications of this proposed framework.

---

## PART 1: Frequency Scaling Perceptual ODE — Derivation and Solution

### 1.1 The Differential Equation

The proposed frequency scaling behavior is defined by the following non-linear ordinary differential equation:

```
dG/G = (1 - k*G) * df/f
```

Where:
- **G** = GPU performance score as frequency scales (starts at the baseline Standard Graphics Architecture Score `GAS` under reference frequency, and scales to `CTI_raw` under target frequency ratio `R`)
- **f** = GPU core clock frequency (starts at `Reference_Frequency`, ends at `Actual_Frequency`)
- **k** = perceptual diminishing returns constant

**Physical interpretation:** The *relative* change in score (`dG/G`) is proportional to the *relative* change in frequency (`df/f`), but the proportionality factor `(1 - k*G)` decreases as the score `G` increases. This encodes the Weber-Fechner Law: at high frame rates (high scores), humans are less sensitive to further improvements.

### 1.2 Solving the ODE (Step-by-Step)

This is a separable ODE. We rearrange:

```
dG / [G * (1 - k*G)] = df / f
```

**Step 1: Partial fraction decomposition of the left side**

```
1 / [G * (1 - k*G)] = A/G + B/(1 - k*G)
```

Multiply both sides by `G * (1 - k*G)`:

```
1 = A * (1 - k*G) + B * G
```

- Set `G = 0`: `1 = A * 1` → **`A = 1`**
- Set `G = 1/k`: `1 = B * (1/k)` → **`B = k`**

So:

```
1 / [G * (1 - k*G)] = 1/G + k/(1 - k*G)
```

**Step 2: Integrate both sides**

```
Integral of [1/G + k/(1 - k*G)] dG = Integral of [1/f] df
```

Left side:
- `Integral of 1/G dG = ln|G|`
- `Integral of k/(1 - k*G) dG = -ln|1 - k*G|`  (substitution: `u = 1 - k*G`, `du = -k*dG`)

Right side:
- `Integral of 1/f df = ln|f| + C`

So:

```
ln|G| - ln|1 - k*G| = ln|f| + C
ln[G / (1 - k*G)] = ln(f) + C
```

**Step 3: Apply boundary condition**

When `f = f_ref` (Reference Frequency), `G = GAS`:

```
ln[GAS / (1 - k*GAS)] = ln(f_ref) + C
C = ln[GAS / (1 - k*GAS)] - ln(f_ref)
```

**Step 4: Substitute back and simplify**

```
ln[G / (1 - k*G)] = ln(f) + ln[GAS / (1 - k*GAS)] - ln(f_ref)
ln[G / (1 - k*G)] = ln[(f / f_ref) * GAS / (1 - k*GAS)]
```

Exponentiating both sides:

```
G / (1 - k*G) = R * GAS / (1 - k*GAS)
```

Where **R = f / f_ref = Actual_Frequency / Reference_Frequency** (the frequency ratio).

**Step 5: Solve for G (the final CTI)**

Let `alpha = R * GAS / (1 - k*GAS)`:

```
G = alpha * (1 - k*G)
G = alpha - alpha*k*G
G * (1 + alpha*k) = alpha
G = alpha / (1 + alpha*k)
```

Substituting alpha back:

```
G = [R*GAS / (1 - k*GAS)] / [1 + k * R*GAS / (1 - k*GAS)]
G = [R*GAS / (1 - k*GAS)] / [(1 - k*GAS + k*R*GAS) / (1 - k*GAS)]
G = R*GAS / (1 - k*GAS + k*R*GAS)
G = R*GAS / (1 + k*GAS*(R - 1))
```

### 1.3 The Final Solution

> **CTI = R * GAS / (1 + k * GAS * (R - 1))**

**Verification:**
- **R = 1 (reference clock):** `CTI = 1*GAS / (1 + 0) = GAS` ✓
- **R > 1 (overclock):** Denominator `> 1`, so `CTI < R*GAS`. The overclock boost is dampened. ✓
- **R < 1 (underclock):** Denominator `< 1`, so `CTI > R*GAS`. The underclock penalty is cushioned. ✓
- **GAS = 0:** `CTI = 0` regardless of R. A GPU with zero base score produces nothing. ✓

This can also be expressed as an effective Frequency Scaling Factor (FSF):

```
FSF = CTI / GAS = R / (1 + k * GAS * (R - 1))
```

---

## PART 1b: Calibration of the Perceptual Scaling Constant k

### 1b.1 Establishing FPS Anchors

To calibrate k, we anchor the 0-10 score scale to real-world Frames Per Second (FPS) performance in demanding 3D games (e.g., Genshin Impact at High settings):

- **FPS_min = 30 FPS** → maps to **Score = 0** (minimum playable threshold)
- **FPS_max = 120 FPS** → maps to **Score = 10** (sustained peak fluidity)
- **FPS Ratio:** `FPS_max / FPS_min = 120 / 30 = 4`

**Justification for FPS_min = 30 FPS:**

1. **Representativeness:** 30 FPS is the universally accepted "minimum playable" threshold in gaming across the entire smartphone population. Below 30 FPS, games are considered non-functional (stuttering, unresponsive controls). Devices that cannot achieve 30 FPS in a benchmark workload are effectively unable to run that workload at all. Therefore, 30 FPS is the natural "Score = 0" floor — it represents the lowest performance level that is still meaningfully scorable, rather than anchoring to extreme outlier devices (e.g., 2016 ultra-budget phones at 10 FPS) that cannot even run modern benchmarks.

2. **Perceptual significance:** Frame rate perception research consistently identifies the **30 → 60 FPS transition** as the single most dramatic perceptual leap in gaming fluidity. By setting our floor at 30 FPS, the model's region of maximum sensitivity (scores near 0, where the elasticity `(1 - k*G)` is highest) is perfectly aligned with this most perceptually impactful zone. This ensures the model allocates the greatest scoring resolution precisely where humans notice the biggest differences.

### 1b.2 Applying Weber's Law to Derive k

The derivation proceeds in four explicit steps:

**Step A — Weber's Law (the empirical foundation)**

Weber's Law is one of the oldest and most robust findings in psychophysics (Ernst Weber, 1834). It states:

> *The just-noticeable difference (JND) in a stimulus is proportional to the magnitude of the stimulus itself.*

In mathematical form: `JND = c * S`, where `S` is the stimulus intensity and `c` is a constant (the "Weber fraction").

Applied to frame rate perception (with an empirically typical Weber fraction of `c ≈ 0.10` for visual motion fluidity), this means:

| FPS Level | JND (= c * FPS)         | Interpretation                                                    |
|:---------:|:-----------------------:|-------------------------------------------------------------------|
|  30 FPS   | 0.10 * 30 = **3 FPS**   | At the playability threshold, a 3 FPS change is noticeable        |
| 120 FPS   | 0.10 * 120 = **12 FPS** | At ultra-smooth rates, you need a 12 FPS swing to notice          |

The **perceptual impact** of a fixed absolute FPS change (say, +3 FPS) is therefore:
- At 30 FPS: **100%** of the JND (= 3/3) — hugely noticeable
- At 120 FPS: **25%** of the JND (= 3/12) — minor

This gives us the critical **ratio of perceptual impacts:**

```
Impact at 120 FPS     JND at 30 FPS      3      1
──────────────────  = ─────────────── = ──── = ────
Impact at 30 FPS      JND at 120 FPS     12     4
```

A user at 30 FPS is **4 times more sensitive** to a given FPS change than a user at 120 FPS.

**Step B — Identifying the sensitivity term in our ODE**

Returning to our differential equation:

```
dG / G = (1 - k*G) * df / f
```

Since FPS is directly proportional to frequency at a fixed architecture (`FPS = Architecture_Constant * f`), a relative change in frequency equals a relative change in FPS:

```
df / f = dFPS / FPS
```

Therefore, the term **(1 - k*G)** controls how much a given relative FPS change translates into a relative score change. It is precisely the **perceptual sensitivity factor** at score level G:
- When `(1 - k*G)` is large (low scores / low FPS): the score is highly responsive to frequency changes
- When `(1 - k*G)` is small (high scores / high FPS): the score barely moves with frequency changes

**Step C — Mapping Score endpoints to FPS endpoints**

From our FPS anchors (Section 1b.1), we established:

- **Score G = 0** corresponds to **FPS_min = 30 FPS** → Our model's sensitivity: `(1 - k*0) = 1.00`
- **Score G = 10** corresponds to **FPS_max = 120 FPS** → Our model's sensitivity: `(1 - k*10) = ?`

**Step D — Calibrating k by equating the sensitivity ratios**

From Step A, Weber's Law gives us a concrete, empirically grounded ratio: the sensitivity at 120 FPS is exactly **1/4th** of the sensitivity at 30 FPS.

Our model must reproduce this same ratio:

```
Sensitivity at G=10      1
────────────────────  = ────
Sensitivity at G=0       4
```

Substituting our model's sensitivity expression:

```
(1 - k*10) / (1 - k*0) = 1/4

(1 - 10k) / 1 = 1/4

1 - 10k = 1/4

10k = 1 - 1/4 = 3/4

k = 3/40 = 0.075
```

### 1b.3 The Calibrated Constant

> **k = 3/40 = 0.075**

**Elasticity profile across the score range:**

| Score (G) | Elasticity (1 - k*G) | Physical Interpretation                                     |
|:---------:|:--------------------:|-------------------------------------------------------------|
|     0     |        1.000         | Maximum sensitivity: every Hz matters                       |
|     2     |        0.850         | Budget tier: high sensitivity                               |
|     5     |        0.625         | Mid-range: moderate sensitivity                             |
|     7     |        0.475         | Upper-mid: diminishing returns becoming noticeable          |
|    10     |        0.250         | Flagship peak: retains 25% of budget-level sensitivity      |
|   13.33   |        0.000         | Theoretical zero-sensitivity ceiling (= 1/k)                |

**Critical property:** The zero-elasticity point `1/k = 40/3 ≈ 13.33` is well above the maximum score of 10, ensuring the elasticity is always strictly positive within the 0-10 scale. This means frequency changes always have a meaningful perceptual impact — even for flagships, 25% of the sensitivity of a budget device remains.

### 1b.4 Denominator Positivity Check

The formula `CTI = R * GAS / (1 + k * GAS * (R - 1))` requires the denominator to be strictly positive:

```
1 + k * GAS * (R - 1) > 0
```

For underclocking (R < 1), the worst case is GAS = 10, R → 0:

```
1 + 0.075 * 10 * (0 - 1) = 1 - 0.75 = 0.25 > 0  ✓
```

Even at the theoretical extreme of R = 0 (GPU completely off), the denominator is `1 - k*GAS = 1 - 0.75 = 0.25 > 0`. The formula is mathematically safe for all physically plausible frequency ratios.

---

## PART 1c: Numerical Analysis of Perceptual Frequency Scaling (Before Headroom)

### Numerical Examples

| GAS | R    | CTI_raw | FSF_eff | Interpretation                                                    |
|:---:|:----:|:-------:|:-------:|-------------------------------------------------------------------|
|  0  | 0.8  |  0.000  | 0.8000  | Zero-score (extreme): perfect linear scaling, no dampening at all |
|  0  | 1.1  |  0.000  | 1.1000  | Zero-score (extreme): +10% freq → +10.0% boost (fully linear)     |
|  0  | 1.5  |  0.000  | 1.5000  | Zero-score (extreme): +50% freq → +50.0% boost (fully linear)     |
|  3  | 0.8  |  2.513  | 0.8377  | Budget: 20% underclock → 16.2% score drop (near-linear)           |
|  3  | 1.1  |  3.227  | 1.0758  | Budget: 10% overclock → 7.6% score boost (high reward)            |
|  3  | 1.5  |  4.045  | 1.3483  | Budget: 50% overclock → 34.8% score boost (large!)                |
|  7  | 0.8  |  6.257  | 0.8939  | High-end: 20% underclock → 10.6% score drop                       |
|  7  | 1.1  |  7.316  | 1.0451  | High-end: 10% overclock → 4.5% score boost                        |
|  7  | 1.5  |  8.317  | 1.1881  | High-end: 50% overclock → 18.8% score boost                       |
| 10  | 0.8  |  9.412  | 0.9412  | Flagship (extreme): 20% underclock → 5.9% score drop              |
| 10  | 1.1  | 10.233  | 1.0233  | Flagship (extreme): 10% overclock → 2.3% score boost              |
| 10  | 1.5  | 10.909  | 1.0909  | Flagship (extreme): 50% overclock → 9.1% score boost              |

The model captures:
- **GAS = 0 (extreme low):** Perfect linear scaling — the `(1 - k*G)` factor equals 1.0, so frequency maps 1:1 to score. 
  > [!IMPORTANT]
  > **Model Boundary Limit!** Since the base score is exactly 0.000, multiplying it by any frequency scaling factor still results in a final CTI of 0.000. In other words, frequency modifications (overclocking/underclocking) cannot materialize as a score change for an absolutely dead/non-functional base architecture (GAS = 0).
- **GAS = 3 (budget):** High sensitivity to frequency (near-linear scaling).
- **GAS = 7 (high-end):** Moderate dampening — a 10% overclock yields +4.5% instead of +10%.
- **GAS = 10 (extreme high):** Strong dampening (retaining 25% sensitivity), yielding realistic +2.3% for a standard 10% overclock and +9.1% for an extreme 50% overclock.
  > [!NOTE]
  > **Normalization Cap:** While the raw ODE-based formula yields values above 10 (e.g., 10.233 and 10.909) for overclocked flagships, in practical database integration these scores will be capped at 10.0 due to the strict 0-10 normalization range of the final performance scaling index.
- **Symmetry:** Underclocking is cushioned at high GAS just like overclocking is dampened.

---

## PART 2: System Headroom and Bottleneck Frequency Scaling Modifier

### 2.1 Proposed Bottleneck Framework Formulation

In a real-world mobile System on a Chip (SoC), a GPU (Graphics Processing Unit) does not scale in a vacuum. Higher core frequencies require a proportional increase in system resources to sustain their performance:
1. **Memory Bandwidth:** Higher frame rates generate more data, which requires a fast system memory bus to prevent memory bottlenecking.
2. **CPU Support:** The central processor must execute game engine logic and draw call orchestration quickly enough to keep the GPU fed with instructions.
3. **Thermal Dissipation:** Overclocked silicon dissipates significantly more heat. If the device's cooling stack (such as a vapor chamber or graphite sheets) cannot handle this thermal load, the processor will rapidly throttle.

To reflect this physical reality, the model overlays a system-level bottleneck adjustment on top of the raw perceptual scaling score. This ensures that a GPU's score is scaled down if the surrounding hardware is insufficient to support its performance.

#### The Mathematical Formulation

```
If SSI >= CTI_raw:
    CTI_final = CTI_raw                                            (Sufficient Support / No Bottleneck)

If SSI < CTI_raw:
    Bottleneck_Ratio = (CTI_raw - SSI) / 10
    Transmission_Factor = 1 - Bottleneck_Ratio
    CTI_final = GAS + (CTI_raw - GAS) * Transmission_Factor        (Insufficient Support / Bottlenecked)
```

**Physical Justification (Operating-Point Fidelity):**
The bottleneck is evaluated directly against the GPU's actual target demand (`CTI_raw`), rather than the reference baseline design (`GAS`). This guarantees *operating-point fidelity*: if a GPU underclocks to a point where the smartphone's hardware (cooling stack, CPU, memory) can fully support its reduced throughput (`SSI >= CTI_raw`), there is no bottleneck. A system that has ample headroom for the underclocked GPU does not artificially cushion the underclock penalty. The GPU receives the full perceptual score drop, accurately reflecting the unhindered loss of frame rate.

#### Detailed Breakdown of Variables

To make this model intuitive and transparent, each variable is defined below:

*   **GAS (Graphics Architecture Score):** The baseline performance score of the GPU (on a standard 0.0 to 10.0 scale) when running at its nominal reference frequency on a fully supported reference platform.
*   **SSI (System Support Index):** An aggregate score (ranging from 0.0 to 10.0) representing the capabilities of the non-GPU system components. This includes thermal cooling stack efficiency, DRAM (Dynamic Random-Access Memory) bus bandwidth, and CPU (Central Processing Unit) headroom.
*   **CTI_raw (Raw Computed Throughput Index):** The theoretical, frequency-scaled graphics score computed in Part 1. This score represents pure perceptual scaling before any hardware bottlenecks are applied. It also acts as the **Peak System Demand**—the target throughput the GPU is demanding from the motherboard.
*   **CTI_final (Final Computed Throughput Index):** The final, system-constrained graphics score that represents the actual, physically realized performance of the GPU within the specific smartphone platform.
*   **Transmission_Factor (Bottleneck Transmission Factor):** A multiplier between `0.0` and `1.0` that dictates how much of the theoretical frequency scaling performance variation is allowed to pass through to the final score.

#### Step-by-Step Logical Walkthrough

The framework operates on a simple, physically sound decision tree:

##### Step 1: Establish the Operating-Point Demand
We evaluate the target demand the GPU places on the device's motherboard. Since frequency dynamically alters throughput, the peak system demand is exactly the theoretical scaled score: `CTI_raw`.

##### Step 2: Compare System Capabilities against Peak Demand
*   **Scenario A: Sufficient System Support (`SSI >= CTI_raw`)**
    If the phone's System Support Index (`SSI`) is greater than or equal to the target demand (`CTI_raw`), the hardware platform has perfect headroom. The vapor chamber can dissipate the heat, the memory bus is fast enough, and the CPU has ample cycles. There is zero bottlenecking. The final score is equal to the raw perceptual score:
    `CTI_final = CTI_raw`
*   **Scenario B: Insufficient System Support (`SSI < CTI_raw`)**
    If the phone's support capabilities fall short of the demand (`SSI < CTI_raw`), the system acts as a bottleneck. The performance scaling is adjusted downward:
    1.  **Calculate the Shortfall:** We determine the absolute gap between what the GPU requires and what the system can deliver: `CTI_raw - SSI`.
    2.  **Normalize the Shortfall:** Since all scores in our performance database are normalized to a `0.0` to `10.0` range, the maximum possible system shortfall is `10.0`. We convert the shortfall into a **Bottleneck Ratio** by dividing by `10`:
        `Bottleneck_Ratio = (CTI_raw - SSI) / 10`
    3.  **Compute the Transmission Factor:** We subtract the Bottleneck Ratio from `1.0` to calculate the percentage of the frequency variation that the system can successfully transmit:
        `Transmission_Factor = 1 - Bottleneck_Ratio`
        *If the system support index is very close to the peak demand, this factor will be near `1.0` (virtually all the frequency scaling variation—whether an overclock boost or an underclock penalty—is fully realized). If the system is heavily starved, the factor shrinks toward `0.0`.*
    4.  **Compute the Final Constrained Score:** The final score is determined by taking the baseline score (`GAS`) and adding only the successfully transmitted portion of the performance difference:
        `CTI_final = GAS + (CTI_raw - GAS) * Transmission_Factor`
        *This dynamic cushioning ensures that the performance gains from an overclock are attenuated by thermal/memory limits, while the performance drop from an underclock is cushioned only when the system's underlying bottlenecks remain restrictive at that specific operating point.*

### 2.2 Boundary Case Analysis: Normalization Range and Clamping Limits

Since all performance scores in the smartphone database are rigorously mapped to a strict `0.0` to `10.0` range, the frequency-scaling model must define explicit boundaries and clamping guidelines to ensure mathematical soundness under all hardware configurations.

Without range constraints, a boundary case occurs when a flagship device with a perfect baseline score (`GAS = 10.0`) is overclocked (e.g., `R = 1.5`), yielding a raw performance index above the database limit:
*   `CTI_raw = 10.909`

If this raw score is passed unconstrained into the bottleneck framework under total system starvation (`SSI = 0`):
*   `Peak Demand = 10.909`
*   `Bottleneck_Ratio = (10.909 - 0) / 10 = 1.091`
*   `Transmission_Factor = 1 - 1.091 = -0.091`
*   `CTI_final = 10.0 + (10.909 - 10.0) * (-0.091) = 9.917`

**Resulting Anomaly:** Because the bottleneck ratio exceeds `1.000`, the bottleneck transmission factor becomes negative (`-0.091`). This results in `CTI_final = 9.917`, meaning an overclock physically *decreases* the performance score below the baseline reference score of `10.000`. Although an `SSI = 0` flagship is physically unrealistic, a mathematically sound model must maintain monotonicity and remain bounded under all conditions.

### 2.3 Resolution for Range Soundness: Two-Stage Clamping Guidelines

To maintain complete database consistency, protect range boundaries, and naturally resolve the sign inversion anomaly, the framework enforces a strict **Two-Stage Clamping Rule**:

#### Stage 1: Pre-Bottleneck Clamping of `CTI_raw`
Before passing the raw perceptual performance index into the system bottleneck logic, it is clamped to the standard database bounds:
```
CTI_raw = CLAMP(0.0, 10.0, CTI_raw)
```

##### How Stage 1 Solves the Sign Inversion Anomaly
Applying this constraint to the extreme boundary case (`GAS = 10.0`, `R = 1.5`, `SSI = 0`) yields the following elegant behavior:
1.  The raw index is clamped: `CTI_raw = CLAMP(0.0, 10.0, 10.909) = 10.0`
2.  The peak system demand is exactly the clamped score: `Peak Demand = 10.0`
3.  The bottleneck ratio is computed: `Bottleneck_Ratio = (10.0 - 0.0) / 10 = 1.000`
4.  The transmission factor is derived: `Transmission_Factor = 1 - 1.000 = 0.000`
5.  The final score is evaluated: `CTI_final = 10.0 + (10.0 - 10.0) * 0.000 = 10.0`

By enforcing pre-bottleneck clamping, the bottleneck ratio is mathematically capped at `1`, meaning the transmission factor `Transmission_Factor = 1 - Bottleneck_Ratio` is guaranteed to remain non-negative (`Transmission_Factor >= 0`) under all physically possible scenarios. The factor naturally reaches exactly `0` under complete system starvation, pinning the final score to baseline without requiring an arbitrary floor clamp.

#### Stage 2: Post-Bottleneck Clamping of `CTI_final`
As a final database-level safeguard, the final system-constrained graphics score is clamped to the nominal database bounds before it is committed:
```
CTI_final = CLAMP(0.0, 10.0, CTI_final)
```
This final stage ensures absolute structural safety, eliminating any risk of overflow or underflow in production data tables.

#### Stage 3: Input Validation and Boundary Exception Handling (Fail-Fast Rule)
Instead of using silent clamping (such as `GAS_safe = CLAMP(0.0, 10.0, GAS)`), which is a "false good idea" because it patches up and hides upstream pipeline anomalies or corrupted database records, the framework mandates strict validation and exception handling at the very beginning of the scoring process. If either parameter is out of bounds, the process must immediately halt and raise an explicit anomaly alert:
* **Check 1 (Graphics Architecture Score):** Assert `0.0 <= GAS <= 10.0`. If out of bounds, halt and raise a critical anomaly alert: `CRITICAL ANOMALY ALERT: Graphics Architecture Score (GAS = {GAS}) is outside standard database bounds [0.0, 10.0]. Halting scoring process.`
* **Check 2 (System Support Index):** Assert `0.0 <= SSI <= 10.0`. If out of bounds, halt and raise a critical anomaly alert: `CRITICAL ANOMALY ALERT: System Support Index (SSI = {SSI}) is outside standard database bounds [0.0, 10.0]. Halting scoring process.`

##### Why this is critical:
1. **Early Anomaly Detection:** Incorporating strict boundary checks ensures that data corruption or logic errors in upstream data sourcing are caught at the earliest possible stage, rather than being quietly masked by clamping.
2. **Division-by-Zero Safety:** Guaranteeing `GAS >= 0.0` mathematically ensures that the denominator in the perceptual scaling formula `1 + k * GAS * (R - 1)` is always strictly positive (at least `0.250`) for all physically possible clock frequency ratios (`R >= 0`), eliminating division-by-zero risk in production code.


### 2.4 Dynamic Behavior Analysis under Underclocking

> [!IMPORTANT]
> **Underclock Cushioning Direction:** When underclocking with `SSI < GAS`, the modifier cushions the underclock penalty, reducing the drop.

**Physical Justification:** When `SSI < GAS`, the system is already bottlenecking the GPU at reference frequency. Underclocking the GPU reduces its power and bandwidth demands, making the system's underlying bottleneck less severe. Therefore, the actual drop in realized system performance is smaller than the theoretical drop in raw GPU throughput.

**Mathematical Verification and Physical Reality:**

To verify how the bottleneck framework cushions performance degradation during underclocking, let us evaluate a realistic scenario where a device with high graphics capabilities (`GAS = 7.0`) is underclocked to `R = 0.8` on a moderately constrained system (`SSI = 5.0`):

1. **Calculate the raw perceptual underclock score:**
   * `CTI_raw = 6.257`
2. **Compare target demand against system support:**
   * Since `SSI = 5.0 < CTI_raw = 6.257`, the system's background resources are insufficient to fully transmit the GPU's potential, meaning a bottleneck is active.
3. **Determine the Bottleneck Ratio and Transmission Factor:**
   * `Bottleneck_Ratio = (6.257 - 5.0) / 10.0 = 0.1257`
   * `Transmission_Factor = 1.0 - 0.1257 = 0.8743`
4. **Evaluate the final constrained underclock score:**
   * `CTI_final = 7.0 + (6.257 - 7.0) * 0.8743 = 7.0 + (-0.743) * 0.8743 = 6.350`

**Physical Result:**
Under pure perceptual scaling, underclocking the GPU by 20% would normally penalize the performance score by `-0.743` points (`7.0 -> 6.257`). However, because the motherboard was already bottlenecking the GPU at this operating point, reducing the core frequency eases the demand on shared system resources (lowering thermal footprint and memory bandwidth contention). The model correctly cushions the loss, permitting a realized drop of only `-0.650` points (`7.0 -> 6.350`).

---

## PART 3: Integrated System Frequency Scaling Sensitivity Sweep

To verify the dynamic behavior and mathematical stability of the frequency scaling framework, this section presents comprehensive sensitivity sweeps across four representative hardware tiers:
1. **Zero-Score Device (`GAS = 0.0`):** Extreme low baseline architecture.
2. **Budget Device (`GAS = 3.0`):** Entry-level architecture.
3. **High-End Device (`GAS = 7.0`):** Upper-mid performance architecture.
4. **Flagship Device (`GAS = 10.0`):** State-of-the-art peak performance architecture.

### What is presented in the tables:
The values inside the cells of the following tables represent the **`CTI_final` (Final Computed Throughput Index) score** on our standard `[0.0, 10.0]` database scale, calculated as a function of:
*   **Columns:** The target clock frequency scaling ratio (`R` from `0.6` to `1.5`).
*   **Rows:** The motherboard's System Support Index (`SSI` from `0.0` to `10.0`), representing background hardware capacity.

These grids serve as the definitive benchmark to validate database compiling and scoring runs.

### Key Observations from the Sweep

**Extreme low — Zero-score device (GAS = 0):**

| SSI | R=0.6   | R=0.8   | R=0.9   | R=1.0  | R=1.1   | R=1.2   | R=1.5   |
|:---:|:-------:|:-------:|:-------:|:------:|:-------:|:-------:|:-------:|
| Any |  0.000  |  0.000  |  0.000  |  0.000 |  0.000  |  0.000  |  0.000  |

*A GPU with GAS = 0 produces CTI = 0 regardless of frequency ratio or system support. This is correct: the formula CTI = R * 0 / (...) = 0 always. No performance exists to scale.*

**Budget device (GAS = 3):**

| SSI | R=0.6   | R=0.8   | R=0.9   | R=1.0  | R=1.1   | R=1.2   | R=1.5   |
|:---:|:-------:|:-------:|:-------:|:------:|:-------:|:-------:|:-------:|
|  0  |  2.180  |  2.635  |  2.828  |  3.000 |  3.154  |  3.292  |  3.622  |
|  3  |  1.978  |  2.513  |  2.762  |  3.000 |  3.222  |  3.425  |  3.936  |
|  5  |  1.978  |  2.513  |  2.762  |  3.000 |  3.227  |  3.445  |  4.045  |
|  7  |  1.978  |  2.513  |  2.762  |  3.000 |  3.227  |  3.445  |  4.045  |
| 10  |  1.978  |  2.513  |  2.762  |  3.000 |  3.227  |  3.445  |  4.045  |

*No bottleneck occurs when the background system capacity matches or exceeds the GPU's target operating demand (SSI >= CTI_raw). Because underclocking reduces the GPU's demand (CTI_raw < 3.0), any background system capacity with SSI >= 3.0 is guaranteed to have zero bottlenecking under all underclock ratios.*
*Budget devices are rarely bottlenecked because their overall throughput demand remains low.*

**High-end device (GAS = 7):**

| SSI | R=0.6   | R=0.8   | R=0.9   | R=1.0  | R=1.1   | R=1.2   | R=1.5   |
|:---:|:-------:|:-------:|:-------:|:------:|:-------:|:-------:|:-------:|
|  0  |  6.212  |  6.722  |  6.882  |  7.000 |  7.085  |  7.144  |  7.222  |
|  3  |  5.706  |  6.499  |  6.777  |  7.000 |  7.180  |  7.325  |  7.617  |
|  5  |  5.370  |  6.350  |  6.707  |  7.000 |  7.243  |  7.445  |  7.880  |
|  7  |  5.316  |  6.257  |  6.649  |  7.000 |  7.306  |  7.566  |  8.143  |
| 10  |  5.316  |  6.257  |  6.649  |  7.000 |  7.316  |  7.602  |  8.317  |

*At SSI = 7.0: Since system support is greater than or equal to the actual target demand (SSI >= CTI_raw) for all underclock points, no underclock bottleneck occurs. Overclock bottlenecks only materialize at frequency ratios where the GPU's target throughput demand exceeds the system support (CTI_raw > 7.0).*
*At SSI = 0.0: Extreme starvation creates a heavy bottleneck, compressing all dynamic performance variations back toward the baseline GAS of 7.0.*

**Extreme high — Flagship device (GAS = 10):**

| SSI | R=0.6   | R=0.8   | R=0.9   | R=1.0  | R=1.1   | R=1.2   | R=1.5   |
|:---:|:-------:|:-------:|:-------:|:------:|:-------:|:-------:|:-------:|
|  0  |  9.796  |  9.965  |  9.993  | 10.000 | 10.000  | 10.000  | 10.000  |
|  3  |  9.367  |  9.789  |  9.912  | 10.000 | 10.000  | 10.000  | 10.000  |
|  5  |  9.082  |  9.671  |  9.858  | 10.000 | 10.000  | 10.000  | 10.000  |
|  7  |  8.796  |  9.554  |  9.804  | 10.000 | 10.000  | 10.000  | 10.000  |
| 10  |  8.571  |  9.412  |  9.730  | 10.000 | 10.000  | 10.000  | 10.000  |

*Observations:*
* **Flagship Overclock Clamping:** For a flagship device that is already at the absolute structural ceiling of our scoring system (GAS = 10.0), any overclocking ratio (`R > 1.0`) yields a theoretical raw index `CTI_raw` above 10.0. Applying Stage 1 pre-bottleneck clamping limits `CTI_raw` strictly to 10.0. This guarantees that `CTI_final` is pinned exactly to 10.0 across all SSI tiers, preventing any overflow beyond the standardized 0.0 to 10.0 database scale.
* **Realistic Cushioned Underclocks:** Unlike legacy MAX-based calculations which locked underclock scores to a flat 10.0 under heavy starvation, the new demand-based model allows underclocking to register a slight, cushioned drop even at `SSI = 0` (e.g., dropping to `9.796` at `R = 0.6`). This is physically highly accurate, representing that severely starved hardware experiences a minor performance loss from underclocking, but the drop is largely cushioned because the underlying system bottlenecks are already dominant.
* **Ample Support Scaling (`SSI = 10`):** In a perfectly supported system with zero bottlenecks, underclocking a flagship to `R = 0.6` registers a drop of exactly `-14.3%` (`10.0 -> 8.571`), which matches pure human perceptual scaling without any hardware limitations.

---

## PART 4: Model Synthesis & Transfer Specifications

To maintain complete mathematical rigor and consistency across the database, this section synthesizes the exact formulas, variable mappings, and clamping guidelines that must be transferred to the primary scoring documentation:
1. [proposed_data_structure.md]
2. [scoring_rules.md]

### 4.1 Primary Scaling Formulas & Parameters

*   **Perceptual scaling constant:** `k = 0.075` (calibrated from Weber-Fechner anchors: `FPS_min = 30` and `FPS_max = 120`)
*   **Target frequency ratio:** `R = Actual_Frequency / Reference_Frequency`

#### Stage 1: Perceptual Dynamic Scaling (Range-Clamped)
Calculate the theoretical human perceptual score and immediately clamp it to the standardized `[0.0, 10.0]` database scale:
`CTI_raw = CLAMP(0.0, 10.0, R * GAS / (1 + k * GAS * (R - 1)))`

#### Stage 2: System Bottleneck Headroom Adjustment
Compare the System Support Index (`SSI`) against `CTI_raw`.

*   **Sufficient System Support Case (`SSI >= CTI_raw`):**
    `CTI_final = CTI_raw`
*   **Starved System Support Case (`SSI < CTI_raw`):**
    `Transmission_Factor = 1.0 - (CTI_raw - SSI) / 10`
    `CTI_final = GAS + (CTI_raw - GAS) * Transmission_Factor`

---

### 4.2 Mathematical Soundness and Bounds

The new framework achieves complete mathematical soundness and scale-bounds safety through its early-clamping architecture:
1. **Early Clamping on `CTI_raw`:** Clamping the perceptual score to `[0.0, 10.0]` immediately after Stage 1 prevents any out-of-bounds demand from propagating into the bottleneck logic.
2. **Natural Non-Negativity:** Since `SSI < CTI_raw` and both variables are strictly in `[0.0, 10.0]`, the shortfall `(CTI_raw - SSI) / 10` is mathematically guaranteed to reside within `[0.0, 1.0]`. Consequently, the transmission factor `Transmission_Factor = 1.0 - (CTI_raw - SSI)/10` is naturally bounded in `[0.0, 1.0]`.
3. **Guaranteed Scale Parity:** Because `CTI_final` is computed via a linear interpolation between two values in the `[0.0, 10.0]` range (`GAS` and `CTI_raw`) using a factor strictly within `[0.0, 1.0]`, the final score `CTI_final` is mathematically guaranteed to reside within the standard database range `[0.0, 10.0]`, eliminating the need for post-bottleneck clamping logic.
4. **Input Validation Safety:** Enforcing strict validation checks on inputs (`GAS` and `SSI` in `[0.0, 10.0]`) at the very beginning of the process eliminates division-by-zero risk by ensuring the perceptual denominator `1 + k * GAS * (R - 1)` is always strictly positive (at least `0.250`) for all physically possible frequency ratios (`R >= 0`).

---

### 4.3 Complete Production-Ready Algorithm

For clear cross-team reference, the GPU Performance Frequency Scaling Framework is detailed below in both **plain English step-by-step logic** and **executable code**. 

In this unified framework, the algorithm produces two primary outputs:
1. **`CTI_final` (Final Computed Throughput Index):** The system-constrained graphics performance score.
2. **`FSF` (Frequency Scaling Factor):** The realized overall frequency scaling multiplier (where `CTI_final = GAS * FSF`). Monitoring `FSF` provides a direct and precious indicator of how efficiently a given motherboard and cooling solution are transmitting raw GPU frequency changes into realized graphics performance.

#### 4.3.1 Plain English Step-by-Step Logic

##### Step 1: Input Validation and Anomaly Detection (Fail-Fast)
We verify that the baseline hardware score and system support metrics are strictly within standard database limits to prevent downstream calculations from encountering corrupt or out-of-bounds numbers:
1.  **Graphics Architecture Score (`GAS`):** Assert `0.0 <= GAS <= 10.0`. If false, raise a high-priority alert and halt the scoring process.
2.  **System Support Index (`SSI`):** Assert `0.0 <= SSI <= 10.0`. If false, raise a high-priority alert and halt the scoring process.
*This fail-fast safeguard ensures any upstream pipeline anomaly is detected at the earliest possible stage rather than being silently patched.*

##### Step 2: Calculate Range-Clamped Perceptual Scaling
Using the psychophysical constant `k = 0.075` (calibrated from 30 FPS to 120 FPS game test anchors), we calculate the theoretical graphics score and immediately clamp the result to standard `[0.0, 10.0]` bounds:
`CTI_raw = CLAMP(0.0, 10.0, (R * GAS) / (1 + 0.075 * GAS * (R - 1)))`
*Early clamping prevents out-of-bounds scores from propagating downstream.*

##### Step 3: Evaluate Hardware Bottlenecks
We compare the motherboard's support capacity (`SSI`) against the range-clamped GPU demand (`CTI_raw`):

*   **Scenario A: Sufficient System Support (`SSI >= CTI_raw`)**
    The phone's cooling stack, CPU, and DRAM bus speed are fully capable of handling the GPU throughput. No throttling occurs:
    `CTI_final = CTI_raw`

*   **Scenario B: Insufficient System Support (`SSI < CTI_raw`)**
    The phone's hardware environment is insufficient to support peak performance, throttling performance variation through a naturally bounded transmission factor:
    1.  **Determine Transmission Factor:** `Transmission_Factor = 1.0 - (CTI_raw - SSI) / 10.0`
    2.  **Evaluate Bottlenecked Score:** `CTI_final = GAS + (CTI_raw - GAS) * Transmission_Factor`

##### Step 4: Derive Realized Frequency Scaling Factor (FSF)
We calculate the realized **Frequency Scaling Factor (FSF)** for database monitoring:
`FSF = CTI_final / GAS` (if `GAS > 0.0`, else `1.0`)
*The FSF represents the overall, system-constrained performance multiplier achieved by the GPU relative to its baseline reference potential.*

---

#### 4.3.2 Production Executable Pseudocode

```python
# =====================================================================
# GPU PERFORMANCE FREQUENCY SCALING FRAMEWORK (CTI)
# =====================================================================
# Input Parameters:
#   GAS : Graphics Architecture Score (baseline GPU score at nominal frequency)
#   SSI : System Support Index (weighted aggregate of non-GPU capabilities)
#   R   : Frequency Ratio (Actual_Frequency / Reference_Frequency)
# Output Parameters:
#   CTI_final : Final Computed Throughput Index (system-constrained score)
#   FSF       : Realized Frequency Scaling Factor (multiplier for monitoring)
# =====================================================================

# Step 1: Input Validation and Fail-Fast Check
if not (0.0 <= GAS <= 10.0):
    raise ValueError(
        f"CRITICAL ANOMALY ALERT: Graphics Architecture Score (GAS = {GAS}) "
        f"is outside standard database bounds [0.0, 10.0]. Halting scoring process."
    )
if not (0.0 <= SSI <= 10.0):
    raise ValueError(
        f"CRITICAL ANOMALY ALERT: System Support Index (SSI = {SSI}) "
        f"is outside standard database bounds [0.0, 10.0]. Halting scoring process."
    )

# Step 2: Calculate Range-Clamped Perceptual Scaling (Weber-Fechner Law)
k = 0.075
CTI_raw = CLAMP(0.0, 10.0, R * GAS / (1.0 + k * GAS * (R - 1.0)))

# Step 3: Evaluate Hardware Bottlenecks
if SSI >= CTI_raw:
    # Scenario A: Ample system headroom (no bottlenecking)
    CTI_final = CTI_raw
else:
    # Scenario B: System starvation bottleneck detected
    # Transmission factor is naturally and mathematically bounded in [0.0, 1.0]
    Transmission_Factor = 1.0 - (CTI_raw - SSI) / 10.0
    
    # Scale down the performance variation
    CTI_final = GAS + (CTI_raw - GAS) * Transmission_Factor

# Step 4: Derive Realized Frequency Scaling Factor (FSF) for Monitoring
FSF = CTI_final / GAS if GAS > 0.0 else 1.0
```
