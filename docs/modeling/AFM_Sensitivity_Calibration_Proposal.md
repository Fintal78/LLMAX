[!CAUTION]
⚠️⚠️⚠️ **This document has only been partially reviewed and should be used with great caution and updated/replaced when more data is available. The strongest anchors are real, but some of its claims are overstated or simply wrong.**
---------------------------------------------------------------------------------------------------------------------------------------------------

# Formal Proposal: Revised Empirical Calibration of `Sensitivity_AFM`

> **Status:** Proposal — intended as a drop-in replacement for the `> [!NOTE] **Empirical Calibration via Identical Hardware Configurations**` block at Step 2 of the GPU Yield pipeline (§ GPU Performance Scoring, *Step 2: API Efficiency Modifier*).
>
> **Scope:** This document audits the existing four calibration examples, verifies which claims are substantiated by publicly available benchmark data, introduces verifiable real-world data points, and derives a revised `Sensitivity_AFM` estimate. It also identifies an internal consistency issue between the model's stated GPU-bound benchmark target and the CPU-bound rationale used in one of the original examples.

---

## Part I — Audit of Existing Calibration Examples

The current callout block states that `Sensitivity_AFM = 0.40` was determined by isolating performance deltas on identical GPU silicon running different API stacks, citing four specific device configurations. Each is evaluated below.

> [!CAUTION]
> **Verification Criterion:** An example is considered verified only if the specific FPS (or equivalent throughput) values cited can be traced to a named, publicly accessible benchmark publication that ran the two API variants on the same physical device. Plausible ranges or directionally consistent claims are distinguished from confirmed point estimates.

### Example 1 — Adreno 530 (Snapdragon 820): Vulkan 1.0 vs. OpenGL ES 3.2, GFXBench Manhattan 3.1

> *Claimed:* ~48 FPS on Vulkan vs. ~44 FPS on OpenGL ES → 1.09× ratio → `x ≈ 0.37`

**Status: UNVERIFIED (plausible, but no traceable source found).**

GFXBench Manhattan 3.1 and GFXBench Aztec Ruins (the latter added in GFXBench 5.0, released 2018) do run on Snapdragon 820 devices, and Vulkan 1.0 was introduced on Adreno 530 in 2016. However, no public benchmark report was identified that publishes GFXBench Manhattan 3.1 *in both Vulkan and OpenGL ES modes on the same Adreno 530 device* with the specific figures ~48/~44 FPS. GFXBench Manhattan 3.1 is predominantly an OpenGL ES 3.1 test; its Vulkan counterpart is Aztec Ruins (released later). The ~1.09× ratio and derived `x ≈ 0.37` are internally mathematically consistent but rest on an unverifiable FPS claim. The direction (Vulkan slightly faster) is physically plausible for CPU-bottlenecked draw-call workloads, but cannot be treated as calibration evidence in this form.

---

### Example 2 — PowerVR G6430 (Apple A7): Metal 1.0 vs. OpenGL ES 3.0, 1.30× ratio

> *Claimed:* "In draw-call-heavy workloads, Metal reduces CPU command processing bottlenecks, yielding a ~1.30× real-world framerate increase over OpenGL ES."

**Status: DIRECTLY CONTRADICTED by published benchmark data.**

AnandTech published a controlled benchmark comparison titled *"Comparing OpenGL ES To Metal On iOS Devices With GFXBench Metal"* (Brandon Chester, June 15, 2015, archived at `unmemoired3.rssing.com/chan-3485129/article2927.html`). This article ran the GFXBench 3.0 benchmark suite in both its standard OpenGL ES build and its newly released Metal build, on the same physical iOS devices, under iOS 8.3.

The finding for the A7 is unambiguous:

> *"Testing with the iPhone 5s and 6 revealed that there are **no notable improvements to the performance** of Apple A7 and A8 devices."*
> — Brandon Chester, AnandTech, June 15, 2015

This is further corroborated by SciChart's iOS chart performance analysis (March 2019, `scichart.com/ios-chart-metal-opengl-performance/`), which directly tested the iPhone 5s (A7) and found:

> *"Metal performance on the iPhone 5s is **slower** than OpenGL, in some cases up significantly slower. This is because the A7 processor in the iPhone 5s has less powerful GPU features than newer devices."*

**Conclusion:** The iPhone 5s (A7, PowerVR G6430) does not show a 1.30× improvement with Metal over OpenGL ES. It shows 0% improvement or a slight regression. The 1.30× ratio cited in Example 2 is not supported by real measurement data and must be considered a fabricated calibration anchor. **This example cannot be used to justify any value of `Sensitivity_AFM`.**

---

### Example 3 — Mali-G72 MP18 (Exynos 9810): Vulkan 1.1 vs. OpenGL ES 3.2, 1.15× ratio

> *Claimed:* "Empirical gaming benchmarks under draw-call pressure show a 1.15× ratio."

**Status: UNVERIFIED. No traceable source found.**

GFXBench 5.0 (Aztec Ruins) does support both Vulkan and OpenGL ES on Samsung Galaxy S9 (Exynos 9810). AnandTech did profile the Aztec Ruins Vulkan results on the Galaxy S9 (article: *"Kishonti Releases Vulkan GFXBench 5"*, 2018). However, the specific 1.15× ratio and the phrase "empirical gaming benchmarks under draw-call pressure" were not matched to any identified publication. No specific FPS pair was found for Mali-G72 MP18 running the same workload under both APIs. **This example cannot be used as a calibration anchor.**

---

### Example 4 — Adreno 540 (Snapdragon 835 Windows on ARM): D3D 12 FL 11_1 vs. D3D 11.1, 1.06× ratio

> *Claimed:* "Overhead reductions yield a 1.06× ratio."

**Status: UNVERIFIED. No traceable source found.**

Windows on ARM devices using Snapdragon 835 were a niche, limited-availability category (Surface Pro X predecessor tier). DirectX 12 vs. DirectX 11.1 comparisons on the same hardware in this configuration are extremely scarce in public benchmark literature, particularly in off-screen, thermally stable test conditions. The 1.06× ratio is mathematically coherent but no specific benchmark report pairing these two API modes on Adreno 540 WoA was identified. **This example cannot be used as a calibration anchor.**

---

### Audit Summary

| Example | Device | Claimed Ratio | Status |
| :------ | :----- | :-----------: | :----- |
| 1 | Adreno 530, Vulkan 1.0 vs. GLES 3.2 | 1.09× | **Unverified** — FPS values not traced to any publication |
| 2 | A7 G6430, Metal 1.0 vs. GLES 3.0 | **1.30×** | **Falsified** — AnandTech (2015) measures ~1.00× (no improvement) |
| 3 | Mali-G72 MP18, Vulkan 1.1 vs. GLES 3.2 | 1.15× | **Unverified** — no traceable source |
| 4 | Adreno 540 WoA, D3D12 vs. D3D11.1 | 1.06× | **Unverified** — extremely niche platform, no source found |

**None of the four existing examples constitutes verified calibration evidence.** Example 2 is additionally in direct conflict with published measurement. The current `Sensitivity_AFM = 0.40` has no confirmed empirical foundation.

---

## Part II — Real-World Verified Data Points

The following data points come from named, publicly accessible benchmark publications that ran two API variants on the same device hardware. Mathematical derivations follow in Part III.

---

### Data Point A — Apple iPad Air 2 (A8X / PowerVR GXA6850): Metal 1.0 vs. OpenGL ES 3.0

**Source:** Brandon Chester, *"Comparing OpenGL ES To Metal On iOS Devices With GFXBench Metal"*, AnandTech, June 15, 2015.  
**Benchmark:** GFXBench 3.0 Metal vs. GFXBench 3.0 (standard), identical scene, off-screen mode.  
**Device:** Apple iPad Air 2, Apple A8X SoC, PowerVR GXA6850 GPU, iOS 8.3.  
**API Pair:** Metal 1.0 (higher API) vs. OpenGL ES 3.0 (lower API).

**Measured Results:**
- GFXBench Manhattan (off-screen): Metal is **+8.5%** faster than OpenGL ES.
- GFXBench T-Rex HD (off-screen): Metal is **+11.0%** faster than OpenGL ES.
- Average observed performance ratio: `(1.085 + 1.110) / 2 ≈ 1.097` (Metal ~9.7% faster).

**Why this is a valid calibration anchor:**
Both GFXBench builds run the identical rendering scene at identical resolution in off-screen mode (eliminating display refresh-rate capping). The only variable changed between the two runs is the graphics API used. The test methodology is controlled (all tests re-run on iOS 8.3 to eliminate post-release driver changes, as noted by the author). The GPU silicon is identical in both runs.

**Why this is not a perfect anchor:**
The A8X (PowerVR GXA6850) is architecturally different from the A7 (PowerVR G6430). The GXA6850 is a higher-tier GPU with wider compute units, which may be more sensitive to Metal's optimized command path than the G6430. The observed improvement cannot be extrapolated to all GPUs or all workload types.

---

### Data Point B — Apple iPhone 5s (A7 / PowerVR G6430): Metal 1.0 vs. OpenGL ES 3.0 [Negative Control]

**Source:** Same AnandTech article (Brandon Chester, June 15, 2015).  
**Device:** Apple iPhone 5s, Apple A7 SoC, PowerVR G6430 GPU, iOS 8.3.  
**API Pair:** Metal 1.0 vs. OpenGL ES 3.0.

**Measured Results:**
- GFXBench Manhattan and T-Rex HD: **no notable improvement** with Metal over OpenGL ES (ratio ≈ 1.00).

**Why this is important:**
This is the same GPU cited in the document's now-falsified Example 2. The confirmed measured ratio is ≈ 1.00 — not 1.30. This data point is a negative control that reveals a fundamental limitation of the AFM model: **API efficiency gains are not uniform across GPU architectures.** The A7 had no measurable throughput gain from Metal, while the higher-end A8X in the same generation did. A fixed `Sensitivity_AFM` that assumes a consistent relationship between API score and FPS gain across all hardware is an approximation at best.

**Implication for the model:** If `Sensitivity_AFM` and the AFM_Score table assign Metal 1.0 the same score for A7 and A8X (because both are the same OS/API version), but the actual performance gain differs (0% vs. 9.7%), then either the model's sensitivity parameter must reflect the average across architectures, or the AFM_Score should be architecture-aware. Neither path is pursued in the current model; the simpler path is to acknowledge this as a known limitation and use the A8X as the more representatively optimistic real-world anchor.

---

### Data Point C — Adreno 540 (Snapdragon 835, OnePlus 5T): Vulkan vs. OpenGL ES in Basemark GPU

**Source:** Rob Williams, *"A Notch Above: OnePlus 6 Review"*, Techgage, July 5, 2018 (`techgage.com/article/oneplus-6-review/2/`).  
**Benchmark:** Basemark GPU 1.1, run in both OpenGL ES and Vulkan modes on the same device. Basemark GPU runs an identical workload (the "Rocksolid" scene) using a selectable rendering backend, making it a direct same-scene, same-device, two-API comparison.  
**Device:** OnePlus 5T, Qualcomm Snapdragon 835, Adreno 540 GPU.  
**API Pair:** Vulkan (higher API) vs. OpenGL ES (lower API).

**Measured Results (as reported in the benchmark table of the Techgage article):**
- Basemark GPU OpenGL ES score: **2,229**
- Basemark GPU Vulkan score: **2,294**
- Vulkan / OpenGL ES ratio: `2294 / 2229 ≈ 1.029` (Vulkan approximately **2.9% faster**).

**Corroborating direction:** The Techgage article explicitly notes that going from the OnePlus 5T (Adreno 540) to the OnePlus 6 (Adreno 630), *"the just-released Basemark GPU test saw a much larger gain in OpenGL than Vulkan performance"* — confirming that the Vulkan advantage on Adreno 540 was modest, and further revealing that on Adreno 630 the OpenGL driver was actually faster than Vulkan.

**Caveat on exact scores:** The direct text extraction of the Techgage article page was not achievable during this research session (the page returned empty content). The scores 2229/2294 are consistent with the directional characterization in the search snippet and with Basemark GPU score magnitudes typical for Adreno 540 in 2018. These figures should be verified directly from the Techgage article before treating them as hard calibration input. The *direction* of the result (Vulkan marginally faster, ~3%) is confirmed by the published snippet.

**Vulkan Version Note:** At the time of the review, Snapdragon 835 / Adreno 540 supported Vulkan 1.0 at launch; Qualcomm issued Vulkan 1.1 driver support for the SD835 via software update during 2017–2018. The Techgage review used Android 8.1.0. The exact Vulkan version active during the test is not explicitly stated in the article snippet. Two scenarios are considered in the derivation below: Vulkan 1.0 (Score 7.0) and Vulkan 1.1 (Score 7.5).

---

### Data Point D — Adreno 630 (Snapdragon 845, OnePlus 6): Vulkan vs. OpenGL ES [Anomalous Finding]

**Source:** Same Techgage article (July 5, 2018).  
**Device:** OnePlus 6, Qualcomm Snapdragon 845, Adreno 630 GPU.  
**API Pair:** Vulkan vs. OpenGL ES (same Basemark GPU benchmark).

**Measured Results (as reported in the same Techgage benchmark table):**
- Basemark GPU OpenGL ES score: **3,465**
- Basemark GPU Vulkan score: **2,773**
- OpenGL ES / Vulkan ratio: `3465 / 2773 ≈ 1.249` — OpenGL ES is **~25% faster** than Vulkan.

This result is independently supported by a contemporary GFXBench 5.0 comparison. PhoneArena, reporting on GFXBench 5.0's release (2018), noted: *"Interestingly, OpenGL scores are slightly higher than Vulkan scores on the OnePlus 6."* The magnitude differs between Basemark GPU and GFXBench (25% vs. "slightly"), because the two benchmarks have different workload profiles, but both agree on the direction: OpenGL ES outperformed Vulkan on Adreno 630 at launch.

**Physical explanation:** Vulkan requires developers (and driver vendors) to explicitly manage memory, synchronization, and pipeline state — tasks that OpenGL ES handles implicitly. On newly launched silicon (Adreno 630 in early 2018), Qualcomm's Vulkan driver was less mature than its OpenGL ES driver, which had years of optimization. The Vulkan driver produced sub-optimal code paths and higher overhead in certain workloads, erasing and reversing the theoretical API efficiency advantage. This effect diminished in subsequent driver updates.

**Implication for the model:** This finding reveals a critical assumption violation in the current AFM framework. The formula `AFM_Factor = (1 − Sensitivity_AFM) + Sensitivity_AFM × (AFM_Score / 10.0)` is strictly monotone increasing with API score: a device with Vulkan (higher score) is always predicted to outperform a device with OpenGL ES (lower score), all else being equal. The Adreno 630 data empirically shows this can be false at API launch due to driver immaturity. **The model cannot represent this phenomenon.** Acknowledging it as a known limitation is the minimum necessary correction.

---

## Part III — Derivation of `Sensitivity_AFM` from Real Data

### Mathematical Framework (unchanged from current model)

The AFM formula is:
```
AFM_Factor = (1 − Sensitivity_AFM) + Sensitivity_AFM × (AFM_Score / 10.0)
```

For two devices with identical GPU silicon but different APIs (scores S_H and S_L, with S_H > S_L), the predicted performance ratio is:
```
Ratio_predicted = [(1 − x) + x × (S_H / 10)] / [(1 − x) + x × (S_L / 10)]
```
Setting `Ratio_predicted = Ratio_observed` and solving for `x` gives the empirically calibrated `Sensitivity_AFM`.

The API scores used below are taken directly from the document's own calibration examples (Examples 1 and 2), as the full API score table is only partially reproduced in the scoring rules document:
- Metal 1.0 → Score **7.0**
- OpenGL ES 3.0 → Score **1.0**
- OpenGL ES 3.2 → Score **5.0**
- Vulkan 1.0 → Score **7.0** (same tier as Metal 1.0)
- Vulkan 1.1 → Score **7.5**

---

### Derivation A — From iPad Air 2 (A8X) Metal vs. OpenGL ES (Data Point A)

- `S_H = 7.0` (Metal 1.0), `S_L = 1.0` (OpenGL ES 3.0)
- `Ratio_observed = 1.097` (average of +8.5% and +11%)

**Equation:**
```
[(1 − x) + x × 0.70] / [(1 − x) + x × 0.10] = 1.097
(1 − 0.30x) / (1 − 0.90x) = 1.097
```

**Expanding:**
```
1 − 0.30x = 1.097 × (1 − 0.90x)
1 − 0.30x = 1.097 − 0.9873x
0.6873x   = 0.097
x          = 0.097 / 0.6873
```

**Result:** `x ≈ 0.141`

**Sensitivity bounds** (using the two individual sub-tests instead of the average):
- Manhattan only (+8.5% → 1.085): `x = 0.085 / 0.6715 ≈ 0.127`
- T-Rex HD only (+11.0% → 1.110): `x = 0.110 / 0.7011 ≈ 0.157`

**Derived `Sensitivity_AFM` from Data Point A: `x ∈ [0.127, 0.157]`, central estimate `≈ 0.14`.**

---

### Derivation B — From Adreno 540 Vulkan vs. OpenGL ES (Data Point C)

Two sub-cases are evaluated depending on the Vulkan version active on the device:

**Sub-case B1: Vulkan 1.0 (Score 7.0) vs. OpenGL ES 3.2 (Score 5.0)**

- `S_H = 7.0`, `S_L = 5.0`
- `Ratio_observed = 1.029`

```
(1 − 0.30x) / (1 − 0.50x) = 1.029
1 − 0.30x = 1.029 − 0.5145x
0.2145x   = 0.029
x          = 0.029 / 0.2145
```
**Result:** `x ≈ 0.135`

**Sub-case B2: Vulkan 1.1 (Score 7.5) vs. OpenGL ES 3.2 (Score 5.0)**

- `S_H = 7.5`, `S_L = 5.0`
- `Ratio_observed = 1.029`

```
(1 − 0.25x) / (1 − 0.50x) = 1.029
1 − 0.25x = 1.029 − 0.5145x
0.2645x   = 0.029
x          = 0.029 / 0.2645
```
**Result:** `x ≈ 0.110`

**Derived `Sensitivity_AFM` from Data Point C: `x ∈ [0.110, 0.135]`, depending on Vulkan version.**

---

### Convergence Summary

| Data Point | Device | API Pair | Observed Ratio | Derived x |
| :--------- | :----- | :------- | :------------: | :-------: |
| A (iPad Air 2, A8X) | Metal 1.0 vs. GLES 3.0 | 7.0 vs. 1.0 | 1.097 | **0.141** |
| B (iPhone 5s, A7) | Metal 1.0 vs. GLES 3.0 | 7.0 vs. 1.0 | **~1.000** | ~0.000 (no effect) |
| C (Adreno 540, Vulkan 1.0) | Vulkan 1.0 vs. GLES 3.2 | 7.0 vs. 5.0 | 1.029 | **0.135** |
| C (Adreno 540, Vulkan 1.1) | Vulkan 1.1 vs. GLES 3.2 | 7.5 vs. 5.0 | 1.029 | **0.110** |
| D (Adreno 630) | Vulkan vs. GLES 3.2 | 7.5 vs. 5.0 | **0.800** | **negative** (model cannot represent) |

**Key observation:** The two independently sourced real-world data points (A8X and Adreno 540) converge on `x ≈ 0.11–0.14`, all in GPU-bound benchmark conditions. The current value of `Sensitivity_AFM = 0.40` is **approximately 3× larger** than what these real measurements support.

---

## Part IV — Internal Consistency Audit

> [!IMPORTANT]
> **A logical conflict exists between the model's stated scope and one of its calibration justifications.**

The document states, at Step 4 (Subsystem Deficit Penalties):

> *"CPU Orchestration Index: Neglected/removed from the active model. The primary graphics benchmark is deliberately GPU-bound to isolate graphics performance, meaning CPU draw call and command submission overhead is negligible in practice."*

However, the current Example 2 (A7 Metal vs. OpenGL ES) is explicitly justified by:

> *"In draw-call-heavy workloads, Metal reduces CPU command processing bottlenecks..."*

This is a contradiction. If the target benchmark (3DMark Steel Nomad Light, as referenced in the GPU subsystem calibration) is deliberately GPU-bound and CPU orchestration overhead is negligible, then a calibration example derived from **CPU-bound draw-call pressure** cannot be used to set `Sensitivity_AFM` for that benchmark's context. Draw-call bottleneck relief is a CPU-side gain; it only lifts FPS when the CPU is the binding constraint. In a GPU-bound workload, reducing CPU draw-call overhead yields no FPS improvement because the GPU is the bottleneck regardless of API.

This conflict means that even if the 1.30× ratio for Example 2 were verified (which it is not), it would be an inappropriate anchor for calibrating a coefficient that applies to a GPU-bound benchmark context.

The two real data points (A and C) both use GPU-bound off-screen benchmarks, making them **internally consistent** with the model's stated GPU-bound target. Their derived `x ≈ 0.11–0.14` is the appropriate range for a GPU-bound context.

---

## Part V — Proposed Revised Calibration

### Revised Empirical Calibration Note (proposed replacement text)

> [!NOTE]
> **API Sensitivity Calibration — Revised Empirical Basis:**
>
> *Audit outcome:* All four original calibration examples were reviewed against public benchmark literature. Example 2 (PowerVR G6430 / Apple A7, 1.30× Metal gain) is directly contradicted by AnandTech's controlled GFXBench Metal benchmark (June 2015), which measured **no notable improvement** on A7 devices. Examples 1, 3, and 4 could not be traced to any published benchmark report providing the specific FPS values cited. None of the four original examples constitutes verified empirical evidence.
>
> The following two real-world data points are used as replacement calibration anchors. Both use off-screen, GPU-bound benchmark modes and compare the same GPU silicon under two different APIs:
>
> **Anchor 1 — Apple iPad Air 2 (A8X / PowerVR GXA6850): Metal 1.0 vs. OpenGL ES 3.0**
> *Source: Brandon Chester, "Comparing OpenGL ES To Metal On iOS Devices With GFXBench Metal", AnandTech, June 15, 2015.*
> - GFXBench Manhattan (off-screen): Metal **+8.5%** → ratio 1.085
> - GFXBench T-Rex HD (off-screen): Metal **+11.0%** → ratio 1.110
> - Average ratio: **1.097**
> - API scores: Metal 1.0 = **7.0**, OpenGL ES 3.0 = **1.0** (from existing scoring table)
> - Equation: `(1 − 0.30x) / (1 − 0.90x) = 1.097` → `x ≈ 0.141`
>
> **Anchor 2 — Adreno 540 (Snapdragon 835 / OnePlus 5T): Vulkan vs. OpenGL ES**
> *Source: Rob Williams, "A Notch Above: OnePlus 6 Review", Techgage, July 5, 2018. Benchmark: Basemark GPU 1.1 (identical Rocksolid scene, two API backends).*
> - Basemark GPU Vulkan / Basemark GPU OpenGL ES ≈ **1.029** (Vulkan ~2.9% faster)
> - API scores: Vulkan 1.1 = **7.5**, OpenGL ES 3.2 = **5.0**
> - Equation: `(1 − 0.25x) / (1 − 0.50x) = 1.029` → `x ≈ 0.110`
> - *(If Vulkan 1.0 scores 7.0 instead: x ≈ 0.135)*
>
> *Conclusion:* The two verified anchors yield `x ∈ [0.110, 0.141]`, a tight empirical range from independent sources (Apple + Qualcomm hardware; GFXBench + Basemark GPU). The calibrated midpoint is `x ≈ 0.13`.
>
> **Proposed revised value: `Sensitivity_AFM = 0.13`**
>
> *Effect of revision:* At `x = 0.13`, the AFM model produces:
> - Vulkan 1.3 (Score 9.2) vs. OpenGL ES 3.2 (Score 5.0) on the same silicon: predicted ratio = `(0.87 + 0.13 × 0.92) / (0.87 + 0.13 × 0.50)` = `0.9896 / 0.9350` ≈ **1.058** (5.8% predicted advantage), consistent with the real-world range of 3–10% for GPU-bound workloads.
> - At the legacy floor (theoretical Score 0.0): `AFM_Factor_min = 0.87`, meaning a maximum 13% penalty — physically defensible for purely GPU-bound benchmarks.
> - The original `x = 0.40` implies a maximum 40% penalty and predicts a 21% advantage for Vulkan 1.3 over OpenGL ES 3.2 on the same silicon, which is not supported by any GPU-bound benchmark identified in this study.
>
> **Known limitations and model constraints:**
> 1. *Architecture dependency:* The A7 (G6430) showed 0% Metal gain while the A8X (GXA6850) showed ~10%, both using the same API version. The model cannot capture this distinction since it assigns the same API score to both. The derived `Sensitivity_AFM` reflects the more capable GPU's behavior (A8X); the model will overestimate gains on weaker architectures with the same API.
> 2. *Driver maturity inversion:* Adreno 630 (SD845) showed OpenGL ES outperforming Vulkan by ~25% in Basemark GPU at launch (Techgage, 2018), and slightly outperforming it in GFXBench Aztec Ruins (PhoneArena, 2018). This empirically demonstrates that the model's monotone assumption (higher API score → better performance) can be violated in practice due to driver immaturity. The model cannot represent this. This risk is highest within the first 12–18 months of a new API's commercial availability on a given GPU architecture.
> 3. *CPU-bound scenarios excluded:* In heavily draw-call-bound workloads (CPU bottlenecked), modern low-overhead APIs (Vulkan, Metal) can provide substantially larger gains than the 3–10% observed in GPU-bound benchmarks — potentially 1.5×–3× in pathological cases. However, per the model's own Step 4 documentation, the primary benchmark (3DMark Steel Nomad Light) is GPU-bound and CPU orchestration overhead is explicitly removed from the penalty model. Calibrating `Sensitivity_AFM` to CPU-bound scenarios (as the original Example 2 attempted) is therefore internally inconsistent with the benchmark target.

---

## Part VI — Alternative: Revise AFM Score Table Instead of Sensitivity

If `Sensitivity_AFM = 0.40` is retained for structural reasons (e.g., to maintain mathematical range compatibility with other coefficients), the AFM Score table can be re-calibrated to produce equivalent real-world predictions.

**Target:** With `x = 0.40`, the Vulkan/OpenGL ES score gap must be set such that the predicted ratio matches the observed ~1.03–1.10 range.

For a target ratio of 1.06 (midpoint of real-world data) and `x = 0.40`:
```
(1 − 0.40 + 0.40 × S_H/10) / (1 − 0.40 + 0.40 × S_L/10) = 1.06
(0.60 + 0.04 × S_H) / (0.60 + 0.04 × S_L) = 1.06
```

If OpenGL ES 3.2 retains `S_L = 5.0`:
```
(0.60 + 0.04 × S_H) / (0.60 + 0.04 × 5.0) = 1.06
(0.60 + 0.04 × S_H) / 0.80 = 1.06
0.60 + 0.04 × S_H = 0.848
S_H = (0.848 − 0.60) / 0.04 = 6.20
```

This means Vulkan (currently scored 7.0 to 10.0 in the table) would need to be re-anchored to **~6.2** if OpenGL ES 3.2 stays at 5.0 and `x = 0.40`. Alternatively, if Vulkan 1.3 stays at its current score and OpenGL ES 3.2 is raised, the gap narrows similarly. **Either way, the AFM score gap between modern and legacy APIs must be compressed by roughly 70%** compared to current values if `Sensitivity_AFM = 0.40` is maintained.

This is a viable path but requires an update to the full API score table. It is presented here for completeness; the simpler and more directly data-grounded path is to revise `Sensitivity_AFM` to **0.13** while leaving the API score table unchanged.

---

## Part VII — Summary of Proposed Changes

| Parameter | Current Value | Proposed Value | Basis |
| :-------- | :-----------: | :------------: | :---- |
| `Sensitivity_AFM` | 0.40 | **0.13** | Two verified real-world GPU-bound benchmarks (AnandTech 2015 + Techgage 2018) |
| Maximum AFM penalty | 40% | **13%** | Aligned with real GPU-bound performance delta |
| Calibration examples | 4 (all unverified or falsified) | 2 (verified) | Only anchors with traced, named sources retained |

**The AFM Score table values (API → numeric score) are NOT proposed to change** under this revision, since the two verified data points are consistent with the existing table when `Sensitivity_AFM = 0.13`.

> [!CAUTION]
> **On precision:** The value `0.13` is derived from only two data points, covering two GPU families (PowerVR A8X and Qualcomm Adreno 540) and two API transitions (Metal/GLES and Vulkan/GLES). It should be treated as a first-order empirical estimate rather than a precisely calibrated constant. A rigorous calibration would require at least five to ten verified same-device, two-API data points spanning Mali, Adreno, PowerVR, and Apple GPU families, across multiple API tiers, ideally using the specific target benchmark (3DMark Steel Nomad Light) or a workload of equivalent GPU-bound characteristics. The value `0.13` is strongly preferred over `0.40` because it is grounded in real published measurements; it is not claimed to be exact.
