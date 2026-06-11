
[!CAUTION]
⚠️⚠️⚠️ **This document has only been partially reviewed and should be used with great caution and updated/replaced when more data is available.**
---------------------------------------------------------------------------------------------------------------------------------------------------

> [!NOTE]
> **Synthesis & Reviewer's Honest Take of the study below:**
> While this study is rigorous, mathematically consistent, and transparent about its limits, describing the recommended weights (**0.0900** for CPU [Central Processing Unit] Multi-Core and **0.1000** for GPU [Graphics Processing Unit] Standard Graphics) as "empirically calibrated" is an epistemic overreach. Due to the complete absence of a clean, same-SoC (System on Chip) mobile memory-isolation dataset, these values are **best-effort engineering judgment estimates** rather than measurement-derived empirical constants. 
> 
> Key flaws and limits of the current document include:
> 1. **Logical Inconsistency:** The document uses terms like "back-solved" and "derivation" while simultaneously admitting that no Tier-1 (Observation-driven) mobile isolation benchmark exists. The 24.6% implied performance drop is a modeling assumption, not an observed fact.
> 2. **Unquantified Scaling:** The GB5 (Geekbench 5) to GB6 (Geekbench 6) memory sensitivity increase is directionally plausible but entirely unquantified in mobile devices.
> 3. **Weak Empirical Bounds:** The Snapdragon 865 same-SoC device pair (Redmi K30 Pro vs Mi 10) only rules out very high weights (0.15–0.16) but cannot uniquely identify or empirically validate 0.0900.
> 4. **Provisional GPU Assignment:** The constraint Weight_GPU >= Weight_CPU is physically sound, but the exact value of 0.1000 is arbitrary and un-back-solved.
> 5. **Internal Table Discrepancy:** The unresolved shift in the base MTI (Memory Technology Index) tables (log-formula 5.17 vs. internal table 5.47 for LPDDR4X [Low Power Double Data Rate 4X]) propagates as a major ~10–20% uncertainty in the weight equations.
> 
> Therefore, these weights should be treated as **provisional operational constants** based on modeling constraints, not as empirically verified physical metrics.

---

# MTI Bottleneck Penalty Weight Calibration Study (Third-Iteration Revision)
## Empirical Calibration of the Memory Technology Index Penalty Weight for §6.1 CPU Multi-Core and §6.3 GPU Standard Graphics — Smartphones 2016–2026

---

## 1. Executive Summary

**Bottom line:** After a final, exhaustive search for mobile-only memory-isolation evidence, **no clean observation-driven datapoint exists** that quantifies the effect of LPDDR speed on smartphone Geekbench 6 multi-core or 3DMark scores with the SoC held constant. The single most-promising candidate — the AnandTech Snapdragon 865 (QRD865) deep dive — did **not** test LPDDR4X vs LPDDR5 on the same reference device; it tested LPDDR5 only. Therefore the calibration remains **model-driven with expert adjustment**, and the recommended weights are unchanged from the default.

**Recommended weights:**

| Section                    | Recommended Weight       | Range           | Confidence | Basis                                                |
|----------------------------|--------------------------|-----------------|------------|------------------------------------------------------|
| §6.1 CPU Multi-Core        | **0.0900**               | 0.0600 – 0.1200 | Medium-Low | Model-driven + expert adjustment (GB5→GB6 direction) |
| §6.3 GPU Standard Graphics | **0.1000** (provisional) | 0.0900 – 0.1400 | Low        | Direction-only; constrained ≥ §6.1                   |

**§6.1 rationale (one paragraph):** The 0.0900 weight is back-solved from the framework's own benchmark-calibrated machinery, not from a measured memory drop. At flagship demand 9.2084, this weight implies that downgrading LPDDR5X-8533 to LPDDR4X-4266 would cost ~24.6% of Geekbench 6 multi-core score. **No mobile benchmark demonstrating a ~25% GB6 multi-core loss purely from memory-speed reduction has ever been found.** The two cleanest mobile same-SoC pairs we located (RedMagic 10 Pro vs 10S Pro; iQOO 13 vs OnePlus 13) both show ~0% isolable memory effect — but they only probe the narrow LPDDR5X→LPDDR5T high-bandwidth band, where the model itself also predicts ~0%, so they neither confirm nor refute the large-deficit extrapolation. 0.0900 is therefore the honest midpoint of a model whose extrapolation is unvalidated; it is plausible but not observation-driven.

**§6.3 rationale (one paragraph):** Peer-reviewed mobile evidence (Mendis et al., 2018) establishes that graphics/display workloads demand higher average memory-bus bandwidth than CPU workloads, and 3DMark Steel Nomad Light is documented as markedly more bandwidth-intensive than prior tests. This justifies the ordering constraint **Weight_GPU ≥ Weight_CPU_multi** and a ratio of roughly 1.05–1.15, yielding a provisional 0.1000. This value is **not** independently back-solved from a GPU memory-isolation benchmark (none exists for mobile) and must be marked provisional. The legacy 0.08 GPU value in `scoring_rules.md` inverts the ordering and is rejected.

---

## 2. Scope & Epistemic Foundation

**Scope:** This study calibrates the MTI bottleneck penalty weight for smartphones released **2016–2026 only**. Desktop and laptop DDR4/DDR5 configurations (e.g., Core i5-12600K, i7-13700K) are **categorically excluded from the calibration basis** and appear only in the Excluded Evidence Appendix (§12). Mobile SoCs have large system-level caches (SLC), different memory controllers, and unified memory architectures; desktop memory-sensitivity figures cannot calibrate a smartphone MTI penalty.

**The framework is benchmark-calibrated by design.** Its CPU TDSI and GPU TDSI weights were back-solved from observed benchmark deltas. The agreed epistemic foundation of this revision is that the **MTI penalty weight must likewise be benchmark-anchored** — it is not a subjective "future-proofing" multiplier and must not be set by intuition about how much memory "should" matter.

**Evidence tiers (definitions used throughout):**

- **Tier 1 — Observation-driven:** A controlled measurement on real mobile hardware in which the SoC is held constant and only memory speed varies, producing a quantified benchmark delta. (Result of this study: **none found.**)
- **Tier 2 — Mobile directional:** Real mobile evidence that establishes the direction and rough magnitude of memory sensitivity but is confounded (clock/thermal/firmware differences) or is a simulation/architectural study rather than an end-to-end benchmark.
- **Tier 3 — Expert adjustment / engineering judgment:** A qualitative, documented mechanism (e.g., the Geekbench 6 shared-task model) whose *direction* is sourced but whose *magnitude* is not empirically quantified by any verifiable source.

---

## 3. Calibration Target & Mathematical Framework

**Penalty formula:**
> Penalty = W × Deficit^1.4

where Deficit = (demand − MTI), clamped at zero, and W is the weight being calibrated.

**MTI formula:**
> MTI = 10 × (log(MT/s) − log(1600)) / (log(10667) − log(1600))

The denominator is log(10667) − log(1600) = log(10667/1600) = **0.823925** (base-10).

**Recomputed MTI values (4 decimals, base-10 logarithms):**

| Memory  | MT/s | log₁₀(MT/s) | Numerator | MTI (computed) | Framework-stated |
|---------|------|-------------|-----------|----------------|------------------|
| LPDDR4X | 4266 | 3.630030    | 0.425910  | **5.1693**     | 5.17             |
| LPDDR5  | 5500 | 3.740363    | 0.536243  | **6.5084**     | 6.51             |
| LPDDR5  | 6400 | 3.806180    | 0.602060  | **7.3084**     | 7.31             |
| LPDDR5X | 8533 | 3.930951    | 0.726831  | **8.8216**     | 8.82             |
| LPDDR5T | 9600 | 3.982271    | 0.778151  | **9.4444**     | 9.41             |

All computed values match the framework-stated values to within rounding, **except LPDDR5T-9600**, where the log-formula yields **9.4444** versus the stated 9.41 (a 0.034 discrepancy, immaterial because LPDDR5T sits at the saturated top of the range where the penalty is ~0).

**Real-bandwidth anchor.** On the Snapdragon 865 — the framework's reference LPDDR4X-vs-LPDDR5 SoC — the published bus figures are LPDDR5-5500 at a maximum 44 GB/s versus LPDDR4X-4266 at a maximum 34.1 GB/s, across four 16-bit memory channels (cpu-monkey / Notebookcheck). The headline MT/s ratio (8533/4266 ≈ 2.0×) thus overstates the realized bandwidth gap, which is closer to ~1.3× at the LPDDR4X→LPDDR5 transition — a key reason the MTI scale is log-compressed rather than linear.

**Internal-table discrepancy.** A second internal MTI table in the framework lists 5.47 (LPDDR4X) and 9.34 (LPDDR5T) rather than the log-formula's 5.17 / 9.44. This ~0.3-point shift at the low end (5.17 vs 5.47) changes the starved-deficit base and propagates to a **~10–20% swing in the back-solved weight**. This study uses the **log-formula values** as canonical and flags the internal table as a variant to be reconciled (sensitivity analysis in §9).

**Translation chain (empirical drop → weight):**
> Delta_score = 10 × log₁₀(ratio) / RCTS_normalizer
> Weight = Delta_score / (Deficit_starved^1.4 − Deficit_optimal^1.4)

with RCTS normalizer = **2.0060** and the deficit term, at flagship demand 9.2084:
- Deficit_starved = 9.2084 − 5.1693 = **4.0391**
- Deficit_optimal = 9.2084 − 8.8216 ≈ **0.3850** (framework value)
- Deficit term = 4.0391^1.4 − 0.3850^1.4 = 7.0588 − 0.2628 = **6.7960** (framework states 6.7968; matches to rounding)

---

## 4. Review-History Adjudication

This third-iteration revision formally implements the following six adjudicated points.

**4.1 — ACCEPTED: Desktop DDR4-vs-DDR5 data removed from calibration basis.** The Tom's Hardware i7-13700K result (Geekbench 5 multi 16542 → 19811, +19.8% from DDR4-3600 to DDR5-5600/6000) and the FPS Review i5-12600K (~9% GB5 multi) are **removed**. Desktop CPUs lack mobile SLC, use different memory controllers, and do not use unified memory; their memory-sensitivity cannot calibrate smartphone MTI. Relocated to Excluded Evidence (§12).

**4.2 — ACCEPTED: Snapdragon 865 device pair DOWNGRADED to directional sanity check only.** The Redmi K30 Pro 6GB (LPDDR4X) vs Mi 10 (LPDDR5) comparison is downgraded from "falsification evidence" to **directional sanity check only**. Confounders — cooling, firmware, scheduler, UFS 3.0 vs 3.1 storage, RAM amount, board design, silicon binning — mean the observed ≈0% net difference does **not** prove memory effect <5%. It shows only that the *net observed* effect ≈0%. **It cannot falsify a 15% memory sensitivity.** This is its exact epistemic status.

**4.3 — ACCEPTED: GB5→GB6 sensitivity argument labeled EXPERT ADJUSTMENT.** The claim that Geekbench 6's multi-core uses a cooperative shared-task model that stresses shared memory/SLC more than Geekbench 5's independent per-core model — and is therefore more memory-sensitive — is labeled **EXPERT ADJUSTMENT / engineering judgment**, not an empirical derivation. No verifiable source quantifies the GB5→GB6 memory-sensitivity gap. Primate Labs' own documentation (verified, §5 Tier 3) confirms the *qualitative direction only*.

**4.4 — ACCEPTED: Implied-drop transparency table included and scrutinized.** See §7. At flagship demand 9.2084, downgrading LPDDR5X-8533 (MTI 8.82) to LPDDR4X-4266 (MTI 5.17), with deficit term 6.7968 and RCTS normalizer 2.0060, the weights map to implied GB6-multi drops as shown. The document states plainly: **no real mobile benchmark demonstrating a ~25% GB6 multi-core loss purely from memory-speed reduction has been found; 0.09 is plausible but model-driven, not observation-driven.**

**4.5 — ACCEPTED: GPU ordering constraint Weight_GPU ≥ Weight_CPU.** Grounded in Mendis et al. (peer-reviewed, verified §5 Tier 2): graphics/display workloads require higher average memory-bus bandwidth than CPU workloads. The 0.08 GPU value in one framework document inverts this ordering and is **rejected**.

**4.6 — ACCEPTED: The framework is benchmark-calibrated by design.** Because the CPU TDSI and GPU TDSI weights were back-solved from benchmark deltas, the MTI weight must also be benchmark-anchored, not a subjective multiplier. Agreed epistemic foundation.

---

## 5. Evidence Base

### Tier 1 — Mobile Observation-Driven: NONE FOUND (honest evidence gap)

After targeted searches for (a) Geekerwan controlled RAM-frequency experiments, (b) same-SoC LPDDR4X-vs-LPDDR5 / LPDDR5X-vs-LPDDR5T device pairs with isolatable data, (c) the AnandTech QRD865 deep dive, (d) UL/3DMark technical quantifications, **no Tier 1 datapoint was found.**

**The AnandTech QRD865 myth, corrected.** The AnandTech article "The Snapdragon 865 Performance Preview" (Andrei Frumusanu, December 2019) is frequently cited as a same-device LPDDR4X-vs-LPDDR5 test. It is **not**. The article states verbatim: *"On the QRD865 device we've tested the chip was naturally equipped with the new LP5 standard."* It tested **LPDDR5 only**. It contains no controlled LPDDR4X comparison. Crucially, the article reports Qualcomm itself **downplaying** LPDDR5's performance importance: *"Qualcomm was actually downplaying the importance of LP5 itself: the new standard does bring higher memory speeds providing better bandwidth, however latency should be the same, and power efficiency benefits, while there, shouldn't be overplayed."* AnandTech further cites Arm's rule of thumb that there is roughly *"a 1% performance difference for each 5ns of latency to DRAM"* — and since LPDDR5 leaves latency essentially unchanged, the implied CPU-score effect of the LPDDR4X→LPDDR5 move is small. This is a useful qualitative signal (Tier 2), but **not** a quantified isolation datapoint.

**Geekerwan controlled memory experiment: not found.** No verifiable Geekerwan (极客湾) experiment holding a mobile SoC constant while varying only LPDDR frequency, with a quoted %-per-step delta, could be located. (A Chinese-language reference to a Geekerwan "locked memory frequency" video concerns a desktop Loongson 3A6000 test and is unusable.)

**Conclusion:** The calibration cannot be upgraded to observation-driven. This is a required honest output, not a failure.

### Tier 2 — Mobile Directional

**(a) Mendis et al. (2018), peer-reviewed — GPU > CPU bandwidth demand (basis for §6.3 ordering).** "Impact of Memory Frequency Scaling on User-centric Smartphone Workloads," Proc. 33rd ACM/SIGAPP SAC 2018. Platform: Samsung Galaxy S4 (i9500), Exynos 5410, 2GB dual-channel 800 MHz LPDDR3 (12.8 GB/s), PowerVR SGX544 MP3 GPU, measured with a Monsoon power monitor. Key verified statements: *"As smartphones are increasingly used for media-rich, high-memory throughput applications, memory bus related power consumption can outweigh the CPU and GPU,"* and *"Decreasing the memory frequency essentially increases the amount of time the CPU has to wait for memory fetches and thereby increases the CPU utilisation and decreases the GPU utilisation."* This establishes that graphics workloads are bound by memory-bus bandwidth, supporting Weight_GPU ≥ Weight_CPU.

**(b) Steiner et al. (2022), arXiv:2209.14756 — LPDDR5 bandwidth saturation (simulation).** "Unveiling the Real Performance of LPDDR5 Memories" (TU Kaiserslautern, Fraunhofer IESE, Mercedes-Benz). Cycle-accurate DRAMSys simulation. Key verified findings: for sequential traffic both LPDDR4 and LPDDR5 reach near the theoretical maximum, with — per the ACM published version — *"only for the highest data rates and traffic with mixed reads and writes the bandwidth slightly drops up to a maximum loss of around 8.5 % (LPDDR5 with BL16), which is still a very reasonable result for a single-rank memory channel"*; and critically, *"for target data rates below 4266 MT/s an upgrade from LPDDR4 to LPDDR5 does not bring any advantage at all from a bandwidth perspective."* For random traffic, LPDDR4 (BL16) *"already starts to saturate at data rates of 1600 MT/s, which is only around one third of the maximum,"* and *"at the highest data rate 4266 MT/s the device only achieves 33 % of the maximum theoretical bandwidth for mixed traffic and 35.5 % for pure read traffic."* **Implication for calibration:** real achievable bandwidth saturates and does not scale linearly with headline MT/s, so a log-compressed MTI scale is well-justified, and the marginal value of memory above ~LPDDR5 is small.

**(c) RedMagic 10 Pro (LPDDR5X-8533) vs 10S Pro (LPDDR5T-9600) — same Snapdragon 8 Elite, single-source.** GSMArena tested both (same reviewer, 16GB/512GB each). Geekbench 6 multi: 10S Pro 9802 (fan off) / 9864 (fan on) vs 10 Pro 9833 — a delta of roughly +0.3% or even slightly negative. Single-core: 3204 vs 3128 (+2.4%) against a prime-clock increase of 4.47/4.32 = +3.5%; 3DMark Wild Life Extreme 7121 vs 6728 (+5.8%) against a GPU-clock increase of 1200/1100 = +9.1%. GSMArena attributes the gains to **clocks, not memory**: *"With the Prime CPU cores clocked higher, the 10S Pro edges out ahead of the 10 Pro in the Geekbench single-threaded test… However, once the two Prime cores have to share the power budget with the six Performance cores, things even out with the original model."* **Epistemic status: directional sanity check only** (clock AND memory both changed). Note the deltas are all ≤ the clock-only expectation, providing an upper bound: LPDDR5X→LPDDR5T added ≈0% isolable benefit. **Importantly, the model itself predicts ≈0% here** — at demand 9.2084, both 8533 (deficit 0.385) and 9600 (deficit clamped to 0) sit at the saturated top of the MTI scale, so this pair cannot probe the large-deficit region and neither confirms nor refutes the 0.09 weight.

**(d) iQOO 13 (LPDDR5T) vs OnePlus 13 (LPDDR5X) — same Snapdragon 8 Elite.** Per NanoReview (citing NotebookCheck/Geekbench/3DMark): GB6 multi 9297 vs 8945 (+4%), single 3008 vs 2899 (+4%); but on the GPU side Wild Life Extreme is ≈0% (6250 vs 6241) and OpenCL compute is essentially tied (OnePlus marginally ahead). The ~4% CPU lead is commonly attributed to iQOO's more aggressive tuning/thermals, not memory. **Epistemic status: directional sanity check only**, same caveats as (c).

### Tier 3 — Expert Adjustment

**Geekbench 6 shared-task multi-core model (direction only).** Primate Labs' official "Geekbench 6 Benchmark Internals" (March 2023) confirms the methodology change verbatim: *"Geekbench 6 uses a 'shared task' model for multi-threading, rather than the 'separate task' model used in earlier versions of Geekbench… The 'shared task' approach parallelizes workloads by having each thread processes part of a larger shared task. Given the increased inter-thread communication required to coordinate the work between threads, this approach may not scale as well as the 'separate task' approach."* Separately, Primate Labs staff on the official support forum note that *"Given the larger datasets used in Geekbench 6 several workloads are now memory-constrained, rather than CPU-constrained, on most systems."* This documents the **qualitative direction** (GB6 multi is more memory-sensitive than GB5) but **no source quantifies the magnitude** of the GB5→GB6 gap. Hence any upward nudge to the weight on this basis is expert adjustment, not derivation.

---

## 6. Confounder Analysis for Every Retained Comparison

- **Comparison: Redmi K30 Pro vs Mi 10 (S865)**
  - **Memory variable:** LPDDR4X vs LPDDR5
  - **Confounders present:** Cooling, firmware, scheduler, UFS 3.0 vs 3.1, RAM amount, board, binning
  - **Net usable conclusion:** Net observed ≈0%; cannot isolate memory; cannot falsify 15%

- **Comparison: RedMagic 10 Pro vs 10S Pro (8 Elite)**
  - **Memory variable:** LPDDR5X-8533 vs LPDDR5T-9600
  - **Confounders present:** CPU clock +3.5%, GPU clock +9.1%, cooling/fan, firmware revision
  - **Net usable conclusion:** Memory adds ≤0% beyond clock; but only probes saturated high-MTI band

- **Comparison: iQOO 13 vs OnePlus 13 (8 Elite)**
  - **Memory variable:** LPDDR5X vs LPDDR5T
  - **Confounders present:** OEM tuning, thermal envelope, scheduler, storage
  - **Net usable conclusion:** ~4% CPU / ~0% GPU; attributable to tuning, not isolatable to memory

- **Comparison: Mendis et al. (Exynos 5410)**
  - **Memory variable:** LPDDR3 frequency steps
  - **Confounders present:** Single old SoC (2013), non-Geekbench workloads, power-focused
  - **Net usable conclusion:** Direction only: GPU more bandwidth-bound than CPU
  
- **Comparison: Steiner et al. (simulation)**
  - **Memory variable:** LPDDR4 vs LPDDR5 data rates
  - **Confounders present:** Simulation, not silicon; bandwidth not benchmark score
  - **Net usable conclusion:** Bandwidth saturates; log scale justified

Every retained comparison is confounded. **No retained comparison isolates memory speed cleanly.**

---

## 7. Step-by-Step Numerical Derivation for §6.1 (4 decimals)

**Inputs:** demand = 9.2084; MTI_starved (LPDDR4X-4266) = 5.1693; MTI_optimal (LPDDR5X-8533) = 8.8216; exponent = 1.4; RCTS normalizer = 2.0060.

**Step 1 — Deficits:**
- Deficit_starved = 9.2084 − 5.1693 = 4.0391
- Deficit_optimal = 9.2084 − 8.8216 = 0.3868 (framework uses 0.3850; difference immaterial)

**Step 2 — Deficit term:**
- 4.0391^1.4 = exp(1.4 × ln 4.0391) = exp(1.4 × 1.39590) = exp(1.95426) = 7.0588
- 0.3850^1.4 = exp(1.4 × ln 0.3850) = exp(1.4 × −0.95444) = exp(−1.33622) = 0.2628
- Deficit term = 7.0588 − 0.2628 = **6.7960** (framework: 6.7968 ✓)

**Step 3 — Weight → implied drop conversion.** Penalty (score points) = W × 6.7968; Delta_score = 10 × log₁₀(ratio) / 2.0060. Setting Penalty = Delta_score:
- log₁₀(ratio) = W × 6.7968 × 2.0060 / 10 = W × 1.36344
- Implied % drop = 1 − 10^(−W × 1.36344)

**Step 4 — Implied-drop transparency table:**

| Weight W | Implied GB6 multi-core drop (LPDDR5X-8533 → LPDDR4X-4266) |
|----------|-----------------------------------------------------------|
| 0.06     | ~17.2%                                                    |
| **0.09** | **~24.6%**                                                |
| 0.12     | ~30.7%                                                    |
| 0.15     | ~37.6%                                                    |
| 0.16     | ~39.7%                                                    |

(Independent recomputation confirms 0.06→17.2%, 0.09→24.6%, 0.15→37.6%, 0.16→39.5%; the 0.12 entry computes to ~31.4% by my arithmetic vs the framework's 30.7% — a minor rounding divergence.)

**Honest statement:** **No real mobile benchmark demonstrating a ~25% GB6 multi-core loss purely from a memory-speed reduction has been found.** The 0.0900 weight is therefore plausible but **model-driven**, not observation-driven. The only mobile same-SoC pairs available (RedMagic, iQOO/OnePlus) sit in the saturated high-MTI band and cannot test the 4266↔8533 extrapolation that produces the 24.6% figure.

---

## 8. §6.3 GPU Derivation

**Ordering constraint:** Weight_GPU ≥ Weight_CPU_multi, grounded in Mendis et al. (graphics/display demand higher average memory-bus bandwidth than CPU) and corroborated by the documented bandwidth-intensity of 3DMark Steel Nomad Light. As Osvaldo Pinali Doederlein (opinali) writes in the Medium analysis "3DMark's Steel Nomad": *"This shows that Steel Nomad, even the Light variant that fits in the 6GB VRAM, is a lot more bandwidth-intensive than older tests."*

**Ratio estimate:** 1.05–1.15 (GPU memory sensitivity modestly above CPU).

**Provisional value:** 0.1000 = 0.0900 × ~1.11.

**Un-back-solved status (explicit):** This value is **not** independently derived from a GPU memory-isolation benchmark — none exists for mobile. The available GPU evidence (RedMagic Wild Life Extreme +5.8% vs +9.1% GPU clock; iQOO/OnePlus Wild Life Extreme ≈0%) shows no isolable memory uplift in the saturated band, consistent with but not confirming the value. 0.1000 is provisional and direction-only.

---

## 9. Sensitivity Analysis

**(a) Demand baseline 8.8–9.5.** Lowering demand toward 8.8 shrinks both deficits (LPDDR5X approaches zero deficit), reducing the deficit term and *raising* the back-solved weight for a fixed target drop; raising demand to 9.5 enlarges deficits and lowers the implied weight. Across 8.8–9.5 the 0.09 weight's implied drop spans roughly 22–27%, so the central conclusion (no observed ~25% drop) is robust to demand choice.

**(b) MTI table variant (log-formula 5.17 vs internal-table 5.47).** Using 5.47 instead of 5.17 reduces Deficit_starved from 4.0391 to 3.7384, cutting the deficit term from ~6.80 to ~5.97 (−12%) and thus *raising* the back-solved weight by ~10–14% for the same target drop. This is the ~10–20% effect flagged in §3 and is the single largest internal source of weight uncertainty.

**(c) Empirical drop band 15–30%.** If a future Tier 1 experiment measured a 15% drop, the back-solved weight ≈ 0.052; a 20% drop → ≈ 0.071; a 25% drop → ≈ 0.092; a 30% drop → ≈ 0.114. This band (0.052–0.114) is why the recommended range is 0.06–0.12 and the point estimate 0.09.

---

## 10. Final Recommendation & Consolidation Instructions

**Recommended consolidated values:**
- **§6.1 CPU Multi-Core: 0.0900** (range 0.0600–0.1200; Medium-Low confidence; model-driven + expert adjustment).
- **§6.3 GPU Standard Graphics: 0.1000** (range 0.0900–0.1400; Low confidence; direction-only; constrained ≥ §6.1).

**Specific document edits:**
1. `scoring_rules.md` §6.1: change current **0.16 → 0.0900**.
2. Rationale doc §6.1: change current **0.15 → 0.0900** (consolidate the two documents to a single value).
3. `scoring_rules.md` §6.3: change current **0.08 → 0.1000** (the 0.08 inverts the GPU≥CPU ordering and is rejected).
4. Rationale doc §6.3: change current **0.16 → 0.1000**.
5. **Delete or flag** the unsourced "35–42% SPEC CPU2017" memory-sensitivity claim (no verifiable source; see §12).
6. **Add ordering-constraint note:** Weight_GPU ≥ Weight_CPU_multi, with the Mendis et al. citation.

---

## 11. Confidence Statement & The Single Decisive Future Experiment

**Confidence:** §6.1 Medium-Low; §6.3 Low. Both weights are model-driven; the evidence base contains zero Tier 1 mobile isolation datapoints.

**The single decisive experiment that would upgrade both weights to observation-driven Tier 1:** A rooted flagship device (e.g., a Snapdragon 8 Elite or Dimensity 9400 handset) with **locked CPU/GPU clocks and locked thermals**, run across **≥3 LPDDR frequency steps** (e.g., LPDDR5X-8533, a downclocked intermediate, and a low step approximating LPDDR4X-4266 effective bandwidth), recording **Geekbench 6 Multi-Core and 3DMark Steel Nomad Light** at each step. The measured score-vs-bandwidth curve would directly back-solve both W_CPU and W_GPU, replacing the model-driven 0.09/0.10 with observation-driven values and collapsing the uncertainty range.

---

## 12. Excluded Evidence Appendix

- **Excluded item: Tom's Hardware i7-13700K (GB5 multi 16542→19811, +19.8%, DDR4→DDR5)**
  - **Reason for exclusion:** Desktop CPU; no mobile SLC; different memory controller; non-unified memory. Cannot calibrate smartphone MTI.
- **Excluded item: The FPS Review i5-12600K (~9% GB5 multi DDR4→DDR5)**
  - **Reason for exclusion:** Same as above — desktop.
- **Excluded item: "35–42% SPEC CPU2017" memory-sensitivity claim**
  - **Reason for exclusion:** **Unsourced.** No verifiable origin found; likely conflates desktop/server SPEC data. Delete or flag.
- **Excluded item: Snapdragon 8 Gen 2 "for Galaxy" vs standard 8 Gen 2**
  - **Reason for exclusion:** CPU/GPU clocks differ (overclocked bin), not a memory-only pair. Rejected.
- **Excluded item: Geekerwan desktop Loongson 3A6000 "locked memory" video**
  - **Reason for exclusion:** Desktop, not mobile LPDDR. Rejected.
- **Excluded item: Vendor marketing (RedMagic "30% boost", MediaTek "40% bandwidth savings")**
  - **Reason for exclusion:** Marketing spin, contradicted by independent measurement. Rejected.

---

## 13. Full Source Register

- **Source #1: AnandTech, "Snapdragon 865 Performance Preview" (Frumusanu, 2019), anandtech.com/show/15207**
  - **Verification status:** Fetched (article body via mirror + search corroboration)
  - **Data extracted:** QRD865 tested **LPDDR5 only**; Qualcomm downplayed LP5 performance importance; latency unchanged; Arm rule "~1% per 5ns DRAM latency"; SPEC2006 +25% int / +29% fp (vs S855, not memory-isolated). **No LPDDR4X-vs-LPDDR5 same-device test exists.**
- **Source #2: Mendis et al. (2018), eprints.whiterose.ac.uk/id/eprint/125334**
  - **Verification status:** Fetched; quotes re-extracted
  - **Data extracted:** Exynos 5410, LPDDR3 12.8 GB/s; lowering memory freq raises CPU wait/utilisation and lowers GPU utilisation; graphics bound by memory bus → GPU≥CPU ordering.
- **Source #3: Steiner et al. (2022), arxiv.org/pdf/2209.14756 (+ ACM dl.acm.org/doi/fullHtml/10.1145/3565053.3565062)**
  - **Verification status:** Fetched; findings re-extracted
  - **Data extracted:** LPDDR5 vs LPDDR4 bandwidth; max ~8.5% loss (LP5 BL16 sequential mixed); below 4266 MT/s LP4→LP5 gives no advantage; LP4 random saturates at 1600 MT/s, only 33% of max at 4266 → log scale justified.
- **Source #4: Primate Labs, "Geekbench 6 Benchmark Internals" (March 2023), geekbench.com/doc/geekbench6-benchmark-internals.pdf**
  - **Verification status:** Fetched
  - **Data extracted:** Confirms shared-task multi-core model; "may not scale as well" due to inter-thread communication. Direction only.
- **Source #5: Primate Labs support forum**
  - **Verification status:** Search-verified
  - **Data extracted:** "Given the larger datasets used in Geekbench 6 several workloads are now memory-constrained, rather than CPU-constrained, on most systems." Direction only.
- **Source #6: GSMArena RedMagic 10S Pro benchmarks, gsmarena.com/redmagic_10s_pro_benchmarks_and_throttling_tests_-news-68118.php**
  - **Verification status:** Fetched (via subagent)
  - **Data extracted:** 10S Pro (LPDDR5T) vs 10 Pro (LPDDR5X): GB6 multi 9802/9864 vs 9833 (~0%); single-core 3204 vs 3128; WLE 7121 vs 6728. Gains attributed to clocks.
- **Source #7: NanoReview iQOO 13 vs OnePlus 13, nanoreview.net/en/phone-compare/vivo-iqoo-13-vs-oneplus-13**
  - **Verification status:** Search/subagent-verified
  - **Data extracted:** GB6 multi 9297 vs 8945; WLE ≈0% (6250 vs 6241); attributed to tuning.
- **Source #8: Beebom, Snapdragon 8 Gen 3 benchmarks, beebom.com/snapdragon-8-gen-3-benchmark-results**
  - **Verification status:** Fetched
  - **Data extracted:** QRD GB6 multi = 7501 (flagship demand anchor 9.2084 derivation).
- **Source #9: Gizmochina, Redmi K30 Pro vs Mi 10, gizmochina.com/2020/04/10/...**
  - **Verification status:** Search-verified
  - **Data extracted:** K30 Pro (LPDDR4X) "performed a bit better" than Mi 10 (LPDDR5) in GB5 — net ≈0%/slightly better; confounded. Sanity check only.
- **Source #10: NotebookCheck Redmi K30 Pro Geekbench, notebookcheck.net/...451068**
  - **Verification status:** Search-verified
  - **Data extracted:** K30 Pro 6GB = LPDDR4X variant confirmed; GB5 903/3362 (cited).
- **Source #11: cpu-monkey / Notebookcheck Snapdragon 865 spec, cpu-monkey.com/en/cpu-qualcomm_snapdragon_865**
  - **Verification status:** Fetched
  - **Data extracted:** LPDDR5-5500 = 44 GB/s max; LPDDR4X-4266 = 34.1 GB/s max; four 16-bit memory channels. Real bandwidth gap ≈1.3×, not 2×.
- **Source #12: Medium "3DMark's Steel Nomad" (Osvaldo Pinali Doederlein / opinali), medium.com/@opinali/3dmarks-steel-nomad-cd4d34f955d2**
  - **Verification status:** Fetched
  - **Data extracted:** "Steel Nomad, even the Light variant… is a lot more bandwidth-intensive than older tests." Supports GPU bandwidth sensitivity.
- **Source #13: Tom's Hardware / The FPS Review desktop DDR4-vs-DDR5**
  - **Verification status:** Excluded (not re-fetched)
  - **Data extracted:** Desktop; excluded per §4.1.

---

*End of calibration study. This document is a standalone reference file for the framework repository. All numerical claims are sourced to the Source Register (§13); where clean mobile isolation data does not exist, this is stated explicitly as a required honest output rather than concealed.*