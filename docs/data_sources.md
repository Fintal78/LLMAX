# 📚 Scoring Data Sources & References

This document lists all the authoritative sources, databases, and standards used to calculate the **Smartphone Scoring Rules (v8.0)** and **Battery Endurance Model (v3.2)**.

## 1. Primary Benchmark Databases
These sources provide the quantitative performance data used for "Truth" values.

**Geekbench Browser**
*   **Used In:** Section 3.1 (SoC Performance), 3.2 (Single-Core)
*   **Metric:** Geekbench 6 Multi-Core & Single-Core Scores
*   **Link:** [browser.geekbench.com](https://browser.geekbench.com)

**3DMark Wild Life Extreme (UL Benchmarks)**
*   **Used In:** Section 3.3 (GPU Performance - Benchmark 1)
*   **Metric:** Wild Life Extreme Score (Points)
*   **Link:** [benchmarks.ul.com/compare/best-smartphones](https://benchmarks.ul.com/compare/best-smartphones) (Leaderboard with scores)

**GFXBench Manhattan 3.1 (Kishonti)**
*   **Used In:** Section 3.3 (GPU Performance - Benchmark 2)
*   **Metric:** Manhattan 3.1 Offscreen (FPS)
*   **Link:** [gfxbench.com](https://gfxbench.com) (Cross-platform GPU benchmark database)

**GSMArena**
*   **Used In:** Section 5.1 (Battery Model), General Specifications
*   **Metric:** Active Use Score (v2.0), Hardware Specs
*   **Link:** [gsmarena.com/battery-test-v2.php3](https://www.gsmarena.com/battery-test-v2.php3)

**PhoneArena**
*   **Used In:** Section 5.1 (Battery Model)
*   **Metric:** Battery Life Estimate
*   **Link:** [phonearena.com/phones/benchmarks/battery](https://www.phonearena.com/phones/benchmarks/battery)

## 2. Repairability & Longevity
Sources used to determine device lifespan, serviceability, and environmental impact.

**iFixit**
*   **Used In:** Section 9.2 (Repairability), 1.1 (Materials)
*   **Metric:** Repairability Score (0-10), Teardown Analysis
*   **Link:** [ifixit.com/smartphone-repairability-scores](https://www.ifixit.com/smartphone-repairability-scores)

**EU EPREL Database (Official)**
*   **Used In:** Section 9.2 (Repairability), Section 5.1 (Battery Verification)
*   **Metric:** EU Repairability Index (0-5), Battery Endurance & Durability Ratings
*   **Link:** [eprel.ec.europa.eu/screen/product/smartphonestablets20231669](https://eprel.ec.europa.eu/screen/product/smartphonestablets20231669)

## 3. Architecture & Reference Frequencies
Sources used to determine the "Reference Frequency" and "Architecture Score" in Sections 3.0 and 3.3.0.

**Arm / Apple / Qualcomm Official Specifications**
*   **Used In:** Section 3.0 (CPU Ref Freq), Section 3.3.0 (GPU Ref Freq)
*   **Metric:** Base/Boost Clocks, Core Counts, IPC Claims
*   **Sources:**
    *   [Arm Developer Documentation](https://developer.arm.com/Processors)
    *   [Apple Platform Architecture (WWDC Sessions)](https://developer.apple.com/videos/)
    *   [Qualcomm Snapdragon Product Briefs](https://www.qualcomm.com/products/snapdragon)
    *   [AnandTech Architecture Deep Dives](https://www.anandtech.com/) (Historical Reference)
