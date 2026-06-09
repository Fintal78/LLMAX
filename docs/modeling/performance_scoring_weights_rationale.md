# Performance Scoring Weights and Exponents: Mathematical and Physical Rationale

This document establishes the physical, architectural, and mathematical rationales for the subsystem performance weights and exponents applied across CPU Multi-Core (§6.1), CPU Single-Core (§6.2), and GPU Standard Graphics (§6.3) in the smartphone performance database. 
To isolate and calibrate these factors accurately, each database section utilizes a specific, standardized industry-standard benchmark:

*   **CPU Multi-Core (§6.1):** Evaluates multi-threaded Central Processing Unit (CPU) performance using the **Geekbench 6 (GB6) Multi-Core** benchmark. Geekbench 6 is a processor utility that runs a series of short, bursty, real-world tasks (e.g. photo processing, database compilation, ray tracing, machine learning inference) lasting 2 to 5 seconds per sub-test.
*   **CPU Single-Core (§6.2):** Evaluates single-threaded Central Processing Unit (CPU) performance using the **Geekbench 6 (GB6) Single-Core** benchmark, measuring the execution speed and instruction throughput of a single active core under short-burst tasks.
*   **GPU Standard Graphics (§6.3):** Evaluates Graphics Processing Unit (GPU) graphics throughput using the **3DMark Steel Nomad Light Unlimited** benchmark. This is a heavy, cross-platform 3D rendering test simulating modern mobile gaming workloads. It runs a sustained, continuous 60-second rendering workload at 100% graphics processor utilization to stress both the silicon and the chassis cooling capacity.

---

## 1. Unified Subsystem Weights & Exponents Calibration

The following table presents the target calibration values for all supporting subsystem weights and exponents. Every metric represents a potential bottleneck that subtracts performance from the raw, unthrottled processor yield.

| Section        | Subsystem Metric           | Weight | Exponent | Bottleneck Nature      | Within-Section Priority | Cross-Section Priority     |
| :------------- | :------------------------- | :----: | :------: | :--------------------- | :---------------------- | :------------------------- |
| **§6.1 CPU Multi-Core**                     |        |          |                        |                         |                            |
| §6.1 Multi-CPU | Memory (MTI)               | 0.1500 |   1.4    | Hard (bus congestion)  | Primary (bandwidth)     | Multi-Core > Single-Core   |
| §6.1 Multi-CPU | Cache (CFEI)               | 0.0200 |   1.3    | Soft (latency delay)   | Secondary (latency)     | Multi-Core < Single-Core   |
| §6.1 Multi-CPU | Thermal (TDSI)             | 0.0150 |   1.4    | Hard (thermal DVFS)    | Tertiary (burst)        | Multi-Core ~ GPU           |
| **§6.2 CPU Single-Core**                    |        |          |                        |                         |                            |
| §6.2 Mono-CPU  | Cache (L2CS)               | 0.0600 |   1.4    | Hard (pipeline stall)  | Primary (latency)       | Single-Core > Multi-Core   |
| §6.2 Mono-CPU  | Memory (MTI)               | 0.0300 |   1.3    | Soft (latency delay)   | Secondary (bandwidth)   | Single-Core < Multi-Core   |
| §6.2 Mono-CPU  | Thermal (TDSI)             | 0.0000 |    —     | Negligible             | Negligible              | Single-Core negligible     |
| **§6.3 GPU Standard Graphics**              |        |          |                        |                         |                            |
| §6.3 GPU (SGS) | Memory (MTI)               | 0.1600 |   1.4    | Hard (bus congestion)  | Primary (bandwidth)     | GPU ~ Multi-Core           |
| §6.3 GPU (SGS) | Thermal (TDSI)             | 0.0180 |   1.4    | Hard (thermal DVFS)    | Secondary (thermal)     | GPU ~ Multi-Core           |
| §6.3 GPU (SGS) | CPU Orchestration          | 0.0000 |    —     | Negligible             | Negligible              | GPU negligible             |

### Abbreviations Legend
*   **CPU:** Central Processing Unit (the main processor).
*   **GPU:** Graphics Processing Unit (the graphics processor).
*   **SGS:** Standard Graphics Score (the normalized GPU performance score).
*   **MTI:** Memory Throughput Index (evaluates memory bus bandwidth capacity).
*   **CFEI:** Cache & Fabric Efficiency Index (evaluates shared Level 3 and system-level caches).
*   **L2CS:** Level 2 Cache Score (evaluates private core-level Level 2 caches).
*   **TDSI:** Thermal Dissipation Stability Index (evaluates sustained thermal stability).
*   **DVFS:** Dynamic Voltage and Frequency Scaling (hardware-level frequency throttling).

---


## 2. Relative Weight Comparisons & Physical Justifications

### 2.1 Memory Throughput Index (MTI) Weight Rationale
The Memory Throughput Index (MTI) represents the system's ability to feed data to the processor's execution units. Its weight varies significantly based on execution parallelism:
*   **CPU Multi-Core (§6.1) vs. CPU Single-Core (§6.2):** 
    In multi-core CPU workloads, all active cores compete simultaneously for the shared system memory bus. This concurrent demand triggers memory bus contention, queue delays, and cache thrashing, turning RAM speed into a hard performance limit (Weight = **0.1500**). Conversely, a single active CPU core generates very light memory bus traffic that is easily accommodated by modern LPDDR5X (Low Power Double Data Rate 5X) memory channels, making memory bandwidth a secondary latency factor (Weight = **0.0300**).
*   **GPU Standard Graphics (§6.3) vs. CPU Multi-Core (§6.1):** 
    Modern mobile Graphics Processing Units (GPUs) are massively parallel throughput engines executing thousands of threads simultaneously. They process massive volumes of texture coordinates, vertex buffers, and framebuffer operations, making them extremely hungry for memory bandwidth under peak workloads. While mobile GPUs utilize Tile-Based Deferred Rendering (TBDR) architectures to reduce external memory transactions, high-resolution rendering at high frame rates (such as 3DMark Steel Nomad Light) saturates the system bus, making memory throughput a slightly harder bottleneck (Weight = **0.1600**) than multi-core CPUs performing general-purpose random memory access (Weight = **0.1500**).

### 2.2 Thermal Dissipation Stability Index (TDSI) Weight Rationale
The Thermal Dissipation Stability Index (TDSI) models the chassis' thermal management capability. The calibrated weights directly reflect the duration and intensity of the corresponding benchmark workloads:
*   **CPU Single-Core (§6.2) is Negligible:** 
    A single active CPU core generates very little heat (typically less than 2 to 3 Watts). The passive thermal dissipation capacity of a standard smartphone chassis is more than sufficient to keep the temperature below throttling limits indefinitely, rendering thermal stability irrelevant (Weight = **0.0000**).
*   **CPU Multi-Core (§6.1) vs. GPU Standard Graphics (§6.3):** 
    - The CPU multi-core benchmark, Geekbench 6 (GB6), consists of a series of short, bursty workloads (e.g. PDF rendering, file compression) lasting 2 to 5 seconds each with pauses in between. The chassis thermal mass acts as a buffer, preventing full thermal saturation. The observed performance drop of a passively cooled device (e.g. Samsung Galaxy S24 Ultra) compared to an actively cooled device (e.g. ASUS ROG Phone 8 Pro) is only about **5.5%** under looped runs, justifying a low TDSI weight of **0.0150**. For the exhaustive step-by-step mathematical derivation and multi-device verification of this 0.0150 TDSI weight, refer to the dedicated [CPU_tdsi_calibration_details.md] document.
    - The GPU benchmark, 3DMark Steel Nomad Light, is a continuous, sustained 60-second rendering test that runs the GPU at 100% load. This sustained loading quickly heats the passive cooling chassis of standard smartphones, initiating thermal throttling. Because this 60-second run is brief compared to long-loop stress tests, the device does not reach full thermal saturation. Therefore, the GPU TDSI weight is conservatively calibrated to **0.018** by assuming that thermal constraints explain half of the observed short-term performance gap between passive and active chassis. For a detailed breakdown of the empirical verification, assumptions, and physical limits of this weight, see the calibration analysis in **Section 4.2 (Verification of GPU TDSI Weight (0.018))**.

### 2.3 Cache Weight Rationale

*   **CPU Multi-Core (§6.1) vs. CPU Single-Core (§6.2) – Cache Effects:**  
    Cache performance influences CPU workloads differently depending on the degree of execution parallelism.

    In single-core workloads, execution latency is often dominated by the ability of the active core to retrieve instructions and data rapidly from its private cache hierarchy. Because only one execution thread is active, memory bandwidth demand remains low and rarely saturates the external memory subsystem. As a result, the processor becomes highly sensitive to cache latency and cache hit rate. A cache miss forces the core to wait for data from higher cache levels or system memory, directly reducing instruction throughput. This makes cache efficiency a primary determinant of single-core performance, justifying the higher cache weight (0.0600).

    In multi-core workloads, multiple cores execute simultaneously and generate substantial demand on the shared memory subsystem. Performance increasingly becomes constrained by aggregate memory throughput, memory-controller contention, interconnect traffic, and synchronization overheads rather than by the latency experienced by any individual core. While shared L3 cache efficiency remains beneficial, its influence is partially diluted because many workload stalls originate from memory-bandwidth limitations rather than cache-access latency alone. Consequently, cache performance remains a secondary contributor in the multi-core model, justifying the lower cache weight (0.0200).

    This distinction reflects the different dominant bottlenecks of each workload type: single-core performance is primarily latency-sensitive, whereas multi-core performance is primarily throughput-sensitive.

### 2.4 GPU Subsystem Exclusions (Cache & CPU Orchestration)
*   **Absence of GPU Cache Score:** 
    GPUs are throughput-oriented architectures designed to hide memory latency through massive thread parallelism. When one group of threads stalls waiting for data from memory, the GPU instantly context-switches to another thread group. Unlike latency-sensitive CPUs, GPUs do not depend on large, low-latency L2 (Level 2) caches for performance. Furthermore, mobile GPU cache configurations are rarely disclosed by manufacturers (like Qualcomm or Apple), making any cache metric unverifiable.
*   **Omission of CPU Orchestration Index (Weight = 0.0000):** 
    Modern graphics APIs (Application Programming Interfaces) like Vulkan 1.3 and Metal are designed to have extremely low CPU driver overhead. During standard graphics benchmarks like 3DMark Steel Nomad Light, the workload is completely GPU-bound. The CPU only needs to submit draw calls, which takes less than 5% of its capacity. Including a CPU performance weight would introduce unnecessary cross-contamination into the GPU score, justifying its omission.

---

## 3. Exponent (beta) Calibration & Rationale

Exponents model the non-linear compounding nature of physical bottlenecks. We utilize exactly two distinct exponents based on the mathematical characteristics of the constraints:

### 3.1 Exponent (beta) = 1.4 for Hard Physical Bottlenecks
*   **Physical Rationale:** Memory bus bandwidth and chassis thermal dissipation are hard physical boundaries. When parallel threads exceed the physical capacity of the memory bus, access queues stall catastrophically. Similarly, when cumulative heat dissipation exceeds the chassis limit, the device triggers aggressive hardware-level Dynamic Voltage and Frequency Scaling (DVFS) to prevent damage. This sudden, non-linear performance drop is modeled by the higher exponent of **1.4**.

### 3.2 Exponent (beta) = 1.3 for Latency-Driven Soft Constraints
*   **Physical Rationale:** Cache misses and single-core memory requests do not saturate physical channels or trigger emergency thermal throttling. Instead, they increase the average memory access latency. The CPU's execution pipeline remains active but runs slower due to data wait times. This gentler, latency-driven performance degradation is modeled by the lower exponent of **1.3**.

---

## 4. Empirical Data Sources & Calibrations

> [!NOTE]
> **Methodological Scope & Limitations:**
> Currently, only two formal empirical calibration studies have been conducted to derive and verify the subsystem weights:
> 1. The Graphics Processing Unit (GPU) Thermal Dissipation Stability Index (TDSI) calibration presented below in Sections 4.1 and 4.2.
> 2. The Central Processing Unit (CPU) Multi-Core TDSI calibration, which is documented in detail in [CPU_tdsi_calibration_details.md].
> 
> Ideally, comprehensive empirical studies should be performed to mathematically isolate and establish every single weight and exponent pair across the database. This would require evaluating multiple hardware configurations for each (weight, exponent) pair under test. However, isolating a single variable in consumer mobile devices is exceptionally difficult: it is nearly impossible to find device pairs that are completely identical in silicon architecture, clock speeds, software stacks, and operating conditions, differing *only* in the single subsystem being measured (such as cache size or memory bandwidth).
> 
> Consequently, both completed studies are inherently imperfect in isolating pure variables and provide estimated weight ranges rather than absolute physical constants.

### 4.1 3DMark Steel Nomad Light Benchmark References
To ground the GPU calibrations in real-world performance, we use verified scores from the official UL (Underwriters Laboratories) Solutions benchmark database:
*   **Samsung Galaxy S24 Ultra (Passive cooling, Snapdragon 8 Gen 3 for Galaxy):**
    *   **Source Link:** [UL Solutions - Samsung Galaxy S24 Ultra Review](https://benchmarks.ul.com/hardware/phone/Samsung+Galaxy+S24+Ultra+review)
    *   **Verified Score:** 3DMark Steel Nomad Light Unlimited = **1,430**
*   **ASUS ROG Phone 8 Pro (Active cooling/gaming design, Snapdragon 8 Gen 3):**
    *   **Source Link:** [UL Solutions - Asus ROG Phone 8 Pro Review](https://benchmarks.ul.com/hardware/phone/Asus+ROG+Phone+8+Pro+review)
    *   **Verified Score:** 3DMark Steel Nomad Light Unlimited = **1,708**

### 4.2 Derivation of GPU TDSI Weight (0.018)

*   **Observed Performance Gap:**
    `Performance Drop = (1708 - 1430) / 1708 = 16.28%`
    *(Note: This total gap reflects the combined effect of all differences between the two devices: thermal throttling, power management software, and driver/API stack differences.)*

*   **Step 0 — Partitioning the Gap (Qualitative Justification for the 50/50 Split):**
    Before computing any weight, we must decide what fraction of the 16.28% gap is attributable to thermal constraints specifically. Two broad categories of causes are at play:
    -   **Thermal throttling:** The S24 Ultra uses a passive chassis. After a few seconds at 100% Graphics Processing Unit (GPU) load, chip junction temperatures rise. The hardware Dynamic Voltage and Frequency Scaling (DVFS) governor steps down the GPU clock to protect the silicon, reducing throughput.
    -   **Non-thermal causes:** Samsung's Game Optimization Service (GOS) applies power-limit caps independently of temperature. Additionally, driver scheduling policies and GPU power state hysteresis differ between devices, resulting in measurable throughput differences even before thermal limits are reached.

    The 3DMark Steel Nomad Light test is exactly **60 seconds** long. This is long enough for thermal throttling to begin (particularly on a passively cooled chassis), but far too short for the chassis to reach full thermal saturation — which only occurs after roughly 10 to 20 minutes of sustained load. Under a 20-minute continuous stress test, the net thermal stability gap between the passive S24 Ultra (59.00% stability) and the active ROG Phone 8 Pro (71.00% stability) is 12.00%. For a 60-second burst, the actual thermal penalty must be substantially smaller than this long-term ceiling.

    Without any additional empirical measurement splitting the two causes in isolation, the most defensible and conservative assumption is an **equal 50/50 split**: half of the observed 16.28% gap is attributed to thermal throttling, and the other half to non-thermal causes. This yields a target thermal-only drop of:
    `Target_Drop_Thermal = 16.28% / 2 = 8.14%`

*   **Step-by-Step Weight Derivation:**

    The following steps first establish the thermal deficit of the S24 Ultra independently of any weight (Steps 1–4), then invert the penalty formula to solve for the weight that exactly produces the 8.14% target thermal drop (Steps 5–6).

    1.  **Step 1 — Core GPU Yield Calculation:**
        The raw throughput potential of the Graphics Processing Unit (GPU) silicon is calculated by adjusting the baseline architectural score for frequency:
        `GPU_Yield = Standard_Graphics_Score * (R ^ gamma)`
        - `Standard_Graphics_Score` for Adreno 750 = `8.9000` (sourced from the `GPU_ARCHITECTURE_LOOKUP_TABLE` in `proposed_data_structure.md`).
        - `Actual Frequency` = `1000 MHz` (the maximum clock frequency of the processor).
        - `Reference Frequency` = `903 MHz` (sourced from the `GPU_ARCHITECTURE_LOOKUP_TABLE`).
        - `R` (Frequency Ratio) = `1000 / 903 = 1.1074`
        - `gamma` = `0.9300` (the frequency soft-saturation exponent representing the voltage wall).
        - `GPU_Yield = 8.9000 * (1.1074 ^ 0.9300) = 9.7856`

    2.  **Step 2 — API Efficiency Modifier Application:**
        The software Application Programming Interface (API) overhead modifies the intrinsic throughput capability:
        `GPU_Yield_Adjusted = GPU_Yield * AFM_Factor`
        - `AFM_Factor` (API Feature Modifier Factor) = `0.8000 + 0.2000 * (AFM_Score / 10.0)`
        - For Vulkan 1.3 support, the `AFM_Score` = `9.2000` (sourced from the `GPU_API_SUPPORT_LOOKUP_TABLE`).
        - `AFM_Factor = 0.8000 + 0.2000 * (9.2000 / 10.0) = 0.9840`
        - `GPU_Yield_Adjusted = 9.7856 * 0.9840 = 9.6290`

    3.  **Step 3 — Logarithmic Normalization:**
        To convert raw throughput to a human-perceptual score on a 0–10 scale:
        `GPU_Yield_norm = 10.0 * (log10(GPU_Yield_Adjusted) - log10(GPU_Yield_Adjusted_Min)) / (log10(GPU_Yield_Adjusted_Max) - log10(GPU_Yield_Adjusted_Min))`
        - Sourcing constants: `GPU_Yield_Adjusted_Min = 0.3000` and `GPU_Yield_Adjusted_Max = 10.3007`.
        - Substituting: `10.0 * (log10(9.6290) - log10(0.3000)) / (log10(10.3007) - log10(0.3000)) = 10.0 * (0.9836 - (-0.5229)) / (1.0129 - (-0.5229)) = 10.0 * (1.5065 / 1.5358) = 9.8092` (rounded to 4 decimal places).

    4.  **Step 4 — Thermal Deficit Calculation:**
        The S24 Ultra's passive chassis thermal capacity is represented by a TDSI score of `4.2400`, derived from its verified 3DMark Wild Life Extreme Stress Test stability rating of **59.00%** (https://benchmarks.ul.com/hardware/phone/Samsung+Galaxy+S24+Ultra+review), where a 40.00% stability floor maps to 0.0, and 100.00% maps to 10.0:
        `TDSI_S24 = 10.0 * (log10(59.0000) - log10(40.0000)) / (log10(100.0000) - log10(40.0000)) = 4.2416` (rounded to `4.2400` for database alignment).
        This gives a thermal deficit of:
        `Deficit_TDSI = 9.8092 - 4.2400 = 5.5692`

    5.  **Step 5 — Back-Calculating the Required Penalty from the Target Drop:**
        From Step 0, the target thermal-only drop is **8.14%**. We need to convert this physical percentage drop into the equivalent normalized score penalty, so that we can solve for the weight in Step 6. The penalty is derived directly from the Step 3 normalization formula:

        - **Define the drop:** a physical performance drop of `Drop` means the throttled benchmark score is a fraction of the unthrottled one:
          `Benchmark_Throttled = Benchmark_Unthrottled * (1 - Drop)`
        - **Apply the Step 3 normalization** to both the unthrottled and throttled scores using the 3DMark Steel Nomad Light bounds (Min = 40, Max = 3120):
          `Score_Unthrottled = 10.0 * (log10(Benchmark_Unthrottled) - log10(40)) / (log10(3120) - log10(40))`
          `Score_Throttled   = 10.0 * (log10(Benchmark_Throttled)   - log10(40)) / (log10(3120) - log10(40))`
        - **The penalty is their difference** (the `log10(40)` terms cancel):
          `Penalty_TDSI = Score_Unthrottled - Score_Throttled = 10.0 * (log10(Benchmark_Unthrottled) - log10(Benchmark_Throttled)) / (log10(3120) - log10(40))`
        - **Substitute** `Benchmark_Throttled = Benchmark_Unthrottled * (1 - Drop)` and apply the logarithm quotient rule:
          `log10(Benchmark_Unthrottled) - log10(Benchmark_Unthrottled * (1 - Drop)) = log10(Benchmark_Unthrottled / (Benchmark_Unthrottled * (1 - Drop))) = log10(1 / (1 - Drop))`
        - **Result:** the `Benchmark_Unthrottled` cancels completely, leaving a formula that depends only on the drop percentage:
          `Penalty_TDSI = 10.0 * log10(1 / (1 - Drop)) / (log10(3120) - log10(40))`
        - **Numerical application** for a target drop of **8.14%**:
          - Log term: `log10(1 / (1 - 0.0814)) = log10(1 / 0.9186) = log10(1.08862) = 0.03687`
          - Normalizer range: `log10(3120) - log10(40) = 3.4942 - 1.6021 = 1.8921`
          - `Penalty_TDSI_target = 0.03687 * 10.0 / 1.8921 = 0.3688 / 1.8921 = 0.1949 points`

    6.  **Step 6 — Back-Calculating the Weight:**
        The penalty formula is `Penalty_TDSI = Weight * (Deficit_TDSI ^ 1.4)`. Solving for the weight:
        `Weight = Penalty_TDSI_target / (Deficit_TDSI ^ 1.4) = 0.1949 / (5.5692 ^ 1.4) = 0.1949 / 11.0858 = 0.0176 ~ 0.018`
        This is the calibrated GPU Thermal Dissipation Stability Index (TDSI) weight.

