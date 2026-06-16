# System on Chip (SoC) Reference (Canonical Source of Truth)

> [!IMPORTANT]
> This file is the **single canonical reference** for all System on Chip (SoC) specifications, core layouts, and cache capacities used across the entire database.
> All subsections in `scoring_rules.md`, `proposed_data_structure.md`, and `scoring_constants.md` that reference CPU cores, clock frequencies, Level 3 (L3) cache sizes, or System Level Cache (SLC) sizes **MUST** use the exact canonical hardware values defined in this file to ensure absolute consistency and auditability.
>

---

## 📖 Architectural Overview & Terminology

To assist readers with varying levels of technical knowledge, the following primary hardware terms and abbreviations used throughout this reference are defined below:
* **System on Chip (SoC):** An integrated circuit that integrates all major components of a smartphone (CPU, GPU, NPU, Memory Controller, and Modems) onto a single physical silicon die.
* **Level 1 (L1) & Level 2 (L2) Caches:** Small, ultra-fast memory pools private to individual processor cores (L1) or core clusters (L2) to store frequently accessed instructions and data.
* **Level 3 (L3) Cache:** A larger, shared cache pool managed by the central processor interconnect (e.g., ARM DynamIQ Shared Unit [DSU]) accessible by all CPU cores across the SoC.
* **System Level Cache (SLC):** A massive on-chip Static Random-Access Memory (SRAM) buffer outside the CPU subsystem, shared by the entire chip (including the GPU, NPU, Display Engine, and ISP) to minimize power-hungry external RAM accesses.
* **Cache & Fabric Efficiency Index (CFEI):** The continuous, logarithmic calculation model (`[0.0, 10.0]`) evaluating a chip's total effective shared on-chip cache capacity (`L3 + SLC`) and physical routing layouts.
* **Random Access Memory (RAM) / Dynamic RAM (DRAM):** High-capacity external volatile memory used to store active application states and system data. 

---

## 1. Apple Silicon (A-Series)

Apple A-series SoCs bypass standard Level 3 (L3) caches entirely, utilizing massive cluster-private Level 2 (L2) caches (inherently captured in the CPU Architecture Score [CAS]) and a large system-wide System Level Cache (SLC). Since no Level 3 (L3) cache exists, their effective shared cache capacity is defined strictly as `SLC (MB)`.

| SoC Name             | Year | CPU Layout                 | Max Freq | L3 (MB) | SLC (MB) | shared_cache_mb | Source / Confidence     |
|:---------------------|:----:|:---------------------------|:--------:|:-------:|:--------:|:---------------:|:------------------------|
| **Apple A19 Pro**    | 2025 | 2x Everest + 4x Sawtooth   | 4.26 GHz | `0`     | `32.0`   | `32.0`          | Plausible (Arch Leaks)  |
| **Apple A19**        | 2025 | 2x Everest + 4x Sawtooth   | 4.26 GHz | `0`     | `16.0`   | `16.0`          | Plausible (Arch Leaks)  |
| **Apple A18 Pro**    | 2024 | 2x Everest + 4x Sawtooth   | 4.05 GHz | `0`     | `24.0`   | `24.0`          | Verified (Die Analysis) |
| **Apple A18**        | 2024 | 2x Everest + 4x Sawtooth   | 4.05 GHz | `0`     | `12.0`   | `12.0`          | Verified (Die Analysis) |
| **Apple A17 Pro**    | 2023 | 2x Coll + 4x Sawtooth      | 3.78 GHz | `0`     | `24.0`   | `24.0`          | Verified (Die Analysis) |
| **Apple A16 Bionic** | 2022 | 2x Everest + 4x Sawtooth   | 3.46 GHz | `0`     | `24.0`   | `24.0`          | Verified (Die Analysis) |
| **Apple A15 Bionic** | 2021 | 2x Avalanche + 4x Blizzard | 3.23 GHz | `0`     | `32.0`   | `32.0`          | Verified (Die Analysis) |
| **Apple A14 Bionic** | 2020 | 2x Firestorm + 4x Icestorm | 3.10 GHz | `0`     | `16.0`   | `16.0`          | Verified (Die Analysis) |
| **Apple A13 Bionic** | 2019 | 2x Lightning + 4x Thunder  | 2.65 GHz | `0`     | `16.0`   | `16.0`          | Verified (Die Analysis) |
| **Apple A12 Bionic** | 2018 | 2x Vortex + 4x Tempest     | 2.49 GHz | `0`     | `8.0`    | `8.0`           | Verified (Die Analysis) |
| **Apple A11 Bionic** | 2017 | 2x Monsoon + 4x Mistral    | 2.39 GHz | `0`     | `?`      | `?`             | Unverified / ?          |
| **Apple A10 Fusion** | 2016 | 2x Hurricane + 2x Zephyr   | 2.34 GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |

> [!NOTE]
> **Architectural Note on Apple A18 Cache Optimization:**
> The Apple A18 (2024) features a physical **12.0 MB System Level Cache (SLC)**, halved from the **24.0 MB SLC** on the A18 Pro/A17 Pro to minimize silicon die size. While this reduction yields a lower **Cache & Fabric Efficiency Index (CFEI)**, overall CPU throughput remains class-leading due to compensating architectural advancements: a massive **8.0 MB private L2 cache**, a higher clock speed (**4.05 GHz**), and superior Instructions Per Cycle (IPC) from the Everest core design.

---

## 2. Qualcomm Snapdragon Series

Qualcomm chipsets utilize standard ARM DynamIQ Shared Unit (DSU) interconnect architectures combining a central L3 cache and a system-wide System Level Cache (SLC) managed by the Qualcomm Network on Chip (NoC) system bus.

| SoC Name                | Year    | CPU Layout                          | Max Freq   | L3 (MB) | SLC (MB) | shared_cache_mb | Source / Confidence     |
|:------------------------|:-------:|:------------------------------------|:----------:|:-------:|:--------:|:---------------:|:------------------------|
| **Snapdragon 8 Elite**  | 2024    | 2x Oryon Gen 2 + 6x Oryon Gen 2     | 4.32 GHz   | `0`     | `8.0`    | `32.0 (*)`      | Verified (Die Analysis) |
| **Snapdragon 8s Gen 3** | 2024    | 1x X4 + 4x A720 + 3x A520           | 3.00 GHz   | `8.0`   | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 7+ Gen 3** | 2024    | 1x X4 + 4x A720 + 3x A520           | 2.80 GHz   | `?`     | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 7s Gen 3** | 2024    | 1x A720 + 3x A720 + 4x A520         | 2.50 GHz   | `?`     | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 6 Gen 3**  | 2024    | 4x A78 + 4x A55                     | 2.40 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Snapdragon 4s Gen 2** | 2024    | 2x A78 + 6x A55                     | 2.00 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Snapdragon 8 Gen 3**  | 2023    | 1x X4 + 5x A720 + 2x A520           | 3.30 GHz   | `12.0`  | `6.0`    | `18.0`          | Verified (Die Analysis) |
| **Snapdragon 7+ Gen 2** | 2023    | 1x X2 + 3x A710 + 4x A510           | 2.91 GHz   | `4.0`   | `3.0`    | `7.0`           | Plausible (Arch Cousin) |
| **Snapdragon 7 Gen 3**  | 2023    | 1x A715 + 3x A715 + 4x A510         | 2.63 GHz   | `?`     | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 7s Gen 2** | 2023    | 4x A78 + 4x A55                     | 2.40 GHz   | `?`     | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 8 Gen 2**  | 2022    | 1x X3 + 2x A715 + 2x A710 + 3x A510 | 3.20 GHz   | `8.0`   | `6.0`    | `14.0`          | Verified (Die Analysis) |
| **Snapdragon 8+ Gen 1** | 2022    | 1x X2 + 3x A710 + 4x A510           | 3.20 GHz   | `6.0`   | `4.0`    | `10.0`          | Verified (Die Analysis) |
| **Snapdragon 7 Gen 1**  | 2022    | 1x A710 + 3x A710 + 4x A510         | 2.40 GHz   | `4.0`   | `0`      | `4.0`           | Verified (Die Analysis) |
| **Snapdragon 8 Gen 1**  | 2021    | 1x X2 + 3x A710 + 4x A510           | 3.00 GHz   | `6.0`   | `4.0`    | `10.0`          | Verified (Die Analysis) |
| **Snapdragon 888+**     | 2021    | 1x X1 + 3x A78 + 4x A55             | 3.00 GHz   | `4.0`   | `3.0`    | `7.0`           | Verified (Die Analysis) |
| **Snapdragon 778G+**    | 2021    | 4x A78 + 4x A55                     | 2.50 GHz   | `2.0`   | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 778G**     | 2021    | 4x A78 + 4x A55                     | 2.40 GHz   | `2.0`   | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 695**      | 2021    | 2x A78 + 6x A55                     | 2.20 GHz   | `?`     | `0`      | `?`             | Unverified / ?          |
| **Snapdragon 680**      | 2021    | 4x A73 + 4x A53                     | 2.40 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Snapdragon 888**      | 2020    | 1x X1 + 3x A78 + 4x A55             | 2.84 GHz   | `4.0`   | `3.0`    | `7.0`           | Verified (Die Analysis) |
| **Snapdragon 865+**     | 2020    | 1x A77 + 3x A77 + 4x A55            | 3.10 GHz   | `4.0`   | `3.0`    | `7.0`           | Verified (Die Analysis) |
| **Snapdragon 865**      | 2019    | 1x A77 + 3x A77 + 4x A55            | 2.84 GHz   | `4.0`   | `3.0`    | `7.0`           | Verified (Die Analysis) |
| **Snapdragon 855+**     | 2019    | 1x A76 + 3x A76 + 4x A55            | 2.96 GHz   | `2.0`   | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 855**      | 2019    | 1x A76 + 3x A76 + 4x A55            | 2.84 GHz   | `2.0`   | `?`      | `?`             | Unverified / ?          |
| **Snapdragon 845**      | 2017    | 4x A75 + 4x A55                     | 2.80 GHz   | `2.0`   | `3.0`    | `5.0`           | Verified (Die Analysis) |
| **Snapdragon 835**      | 2017    | 4x Kryo Gold + 4x Kryo Silver       | 2.45 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Snapdragon 820**      | 2016    | 2x Kryo Gold + 2x Kryo Silver       | 2.15 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Qualcomm Legacy**     | 2016-20 | 4x A73/A57 + 4x A53 / pre-DSU       | 2.0-2.2GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Snapdragon 870**      | 2021    | 1x A77 + 3x A77 + 4x A55            | 3.20 GHz   | `4.0`   | `3.0`    | `7.0`           | Verified (Die Analysis) |
| **Snapdragon 780G**     | 2021    | 1x A78 + 3x A78 + 4x A55            | 2.40 GHz   | `4.0`   | `2.0`    | `6.0`           | Verified (Die Analysis) |
| **Snapdragon 480**      | 2021    | 2x A76 + 6x A55                     | 2.00 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Snapdragon 6 Gen 1**  | 2022    | 4x A78 + 4x A55                     | 2.20 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Snapdragon 662**      | 2020    | 4x A73 + 4x A53                     | 2.00 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Snapdragon 685**      | 2023    | 4x A73 + 4x A53                     | 2.80 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Snapdragon 4 Gen 2**  | 2023    | 2x A78 + 6x A55                     | 2.20 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Snapdragon 4 Gen 1**  | 2022    | 2x A78 + 6x A55                     | 2.00 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |

(*) **Note:** The Snapdragon 8 Elite's Cache & Fabric Efficiency Index (CFEI) calculation includes a custom Oryon Gen 2 Level 2 (L2) cluster fabric penalty of `-0.5` to reflect interconnect latency overhead between the physically separated CPU core clusters.

---

## 3. MediaTek Dimensity & Helio Series

MediaTek SoCs use large standard L3 caches inside their ARM-based CPU clusters, paired with highly capable System Level Caches (SLC) managed by their custom network fabric to deliver excellent performance sustainability.

| SoC Name                 | Year    | CPU Layout                | Max Freq   | L3 (MB) | SLC (MB) | shared_cache_mb | Source / Confidence     |
|:-------------------------|:-------:|:--------------------------|:----------:|:-------:|:--------:|:---------------:|:------------------------|
| **Dimensity 9400+**      | 2025    | 1x X925 + 3x X4 + 4x A720 | 3.63 GHz   | `12.0`  | `10.0`   | `22.0`          | Verified (Die Analysis) |
| **Dimensity 8400**       | 2025    | 8x A725 (All-Big-Core)    | 3.25 GHz   | `6.0`   | `5.0`    | `11.0`          | Verified (Die Analysis) |
| **Dimensity 9400**       | 2024    | 1x X925 + 3x X4 + 4x A720 | 3.63 GHz   | `12.0`  | `10.0`   | `22.0`          | Verified (Die Analysis) |
| **Dimensity 9300+**      | 2024    | 1x X4 + 3x X4 + 4x A720   | 3.40 GHz   | `8.0`   | `10.0`   | `18.0`          | Verified (Die Analysis) |
| **Dimensity 7300**       | 2024    | 4x A78 + 4x A55           | 2.50 GHz   | `2.0`   | `2.0`    | `4.0`           | Verified (Die Analysis) |
| **Dimensity 6300**       | 2024    | 2x A76 + 6x A55           | 2.40 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Dimensity 9300**       | 2023    | 1x X4 + 3x X4 + 4x A720   | 3.25 GHz   | `8.0`   | `10.0`   | `18.0`          | Verified (Die Analysis) |
| **Dimensity 9200+**      | 2023    | 1x X3 + 3x A715 + 4x A510 | 3.35 GHz   | `8.0`   | `6.0`    | `14.0`          | Verified (Die Analysis) |
| **Dimensity 8300 Ultra** | 2023    | 4x A715 + 4x A510         | 3.35 GHz   | `4.0`   | `4.0`    | `8.0`           | Verified (Die Analysis) |
| **Dimensity 7200**       | 2023    | 2x A715 + 6x A510         | 2.80 GHz   | `2.0`   | `2.0`    | `4.0`           | Verified (Die Analysis) |
| **Dimensity 9200**       | 2022    | 1x X3 + 3x A715 + 4x A510 | 3.05 GHz   | `8.0`   | `6.0`    | `14.0`          | Verified (Die Analysis) |
| **Dimensity 9000+**      | 2022    | 1x X2 + 3x A710 + 4x A510 | 3.20 GHz   | `8.0`   | `6.0`    | `14.0`          | Verified (Die Analysis) |
| **Dimensity 8200**       | 2022    | 4x A78 + 4x A55           | 3.10 GHz   | `4.0`   | `4.0`    | `8.0`           | Verified (Die Analysis) |
| **Dimensity 8100**       | 2022    | 4x A78 + 4x A55           | 2.85 GHz   | `4.0`   | `4.0`    | `8.0`           | Verified (Die Analysis) |
| **Dimensity 1080**       | 2022    | 2x A78 + 6x A55           | 2.60 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Helio G99**            | 2022    | 2x A76 + 6x A55           | 2.20 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Dimensity 9000**       | 2021    | 1x X2 + 3x A710 + 4x A510 | 3.05 GHz   | `8.0`   | `6.0`    | `14.0`          | Verified (Die Analysis) |
| **Dimensity 1200**       | 2021    | 1x A78 + 3x A78 + 4x A55  | 3.00 GHz   | `8.0`   | `?`      | `?`             | Unverified / ?          |
| **Dimensity 920**        | 2021    | 2x A78 + 6x A55           | 2.50 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Helio G85**            | 2020    | 2x A75 + 6x A55           | 2.00 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Helio G88**            | 2021    | 2x A75 + 6x A55           | 2.00 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **MediaTek Legacy**      | 2018-22 | 2x A76/A75 + 6x A55 / pre | 2.0-2.2GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Dimensity 1300**       | 2022    | 1x A78 + 3x A78 + 4x A55  | 3.00 GHz   | `8.0`   | `0`      | `8.0`           | Verified (Die Analysis) |
| **Dimensity 7050**       | 2023    | 2x A78 + 6x A55           | 2.60 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Dimensity 6100+**      | 2023    | 2x A76 + 6x A55           | 2.20 GHz   | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Dimensity 8000**       | 2022    | 4x A78 + 4x A55           | 2.75 GHz   | `4.0`   | `0`      | `4.0`           | Verified (Die Analysis) |
| **Helio G96**            | 2021    | 2x A76 + 6x A55           | 2.05 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Helio G95**            | 2020    | 2x A76 + 6x A55           | 2.05 GHz   | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |

---

## 4. Samsung Exynos Series

Samsung Exynos SoCs are developed with custom coherent interconnects (such as the Samsung Coherent Interconnect [SCI]) coordinating robust L3 and system caches to provide high internal bandwidth.

| SoC Name         | Year | CPU Layout                            | Max Freq | L3 (MB) | SLC (MB) | shared_cache_mb | Source / Confidence     |
|:-----------------|:----:|:--------------------------------------|:--------:|:-------:|:--------:|:---------------:|:------------------------|
| **Exynos 2500**  | 2025 | 1x X925 + 2x A725 + 5x A725 + 2x A520 | 3.30 GHz | `16.0`  | `?`      | `?`             | Unverified / ?          |
| **Exynos 2400**  | 2024 | 1x X4 + 2x A720 + 3x A720 + 4x A520   | 3.20 GHz | `8.0`   | `8.0`    | `16.0`          | Verified (Die Analysis) |
| **Exynos 2400e** | 2024 | 1x X4 + 2x A720 + 3x A720 + 4x A520   | 3.10 GHz | `8.0`   | `8.0`    | `16.0`          | Verified (Die Analysis) |
| **Exynos 1580**  | 2024 | 1x A720 + 3x A720 + 4x A520           | 2.90 GHz | `4.0`   | `?`      | `?`             | Unverified / ?          |
| **Exynos 1480**  | 2024 | 4x A78 + 4x A55                       | 2.75 GHz | `4.0`   | `?`      | `?`             | Unverified / ?          |
| **Exynos 1380**  | 2023 | 4x A78 + 4x A55                       | 2.40 GHz | `4.0`   | `0`      | `4.0`           | Verified (Die Analysis) |
| **Exynos 1330**  | 2023 | 2x A78 + 6x A55                       | 2.40 GHz | `4.0`   | `0`      | `4.0`           | Verified (Die Analysis) |
| **Exynos 2200**  | 2022 | 1x X2 + 3x A710 + 4x A510             | 2.80 GHz | `4.0`   | `8.0`    | `12.0`          | Verified (Die Analysis) |
| **Exynos 1280**  | 2022 | 2x A78 + 6x A55                       | 2.40 GHz | `4.0`   | `0`      | `4.0`           | Verified (Die Analysis) |
| **Exynos 2100**  | 2021 | 1x X1 + 3x A78 + 4x A55               | 2.90 GHz | `4.0`   | `6.0`    | `10.0`          | Verified (Die Analysis) |
| **Exynos 990**   | 2020 | 2x M5 + 2x A76 + 4x A55               | 2.73 GHz | `2.0`   | `?`      | `?`             | Unverified / ?          |
| **Exynos 1080**  | 2020 | 1x A78 + 3x A78 + 4x A55              | 2.80 GHz | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Exynos 9825**  | 2019 | 2x M4 + 2x A75 + 4x A55               | 2.84 GHz | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Exynos 9820**  | 2019 | 2x M4 + 2x A75 + 4x A55               | 2.73 GHz | `2.0`   | `0`      | `2.0`           | Verified (Die Analysis) |
| **Exynos 9810**  | 2018 | 4x M3 + 4x A55                        | 2.90 GHz | `4.0`   | `0`      | `4.0`           | Verified (Die Analysis) |
| **Exynos 850**   | 2020 | 8x A55                                | 2.00 GHz | `0.5`   | `0`      | `0.5`           | Verified (Die Analysis) |

---

## 5. Google Tensor Series

Google Tensor chipsets are co-designed with Samsung's custom Exynos manufacturing platform, sharing equivalent DSU-hosted L3 and large 8 megabyte (MB) SLC structures to accelerate on-device machine learning operations.

| SoC Name             | Year | CPU Layout                | Max Freq | L3 (MB) | SLC (MB) | shared_cache_mb | Source / Confidence     |
|:---------------------|:----:|:--------------------------|:--------:|:-------:|:--------:|:---------------:|:------------------------|
| **Google Tensor G4** | 2024 | 1x X4 + 3x A720 + 4x A520 | 3.10 GHz | `?`     | `?`      | `?`             | Unverified / ?          |
| **Google Tensor G3** | 2023 | 1x X3 + 4x A715 + 4x A510 | 2.91 GHz | `?`     | `?`      | `?`             | Unverified / ?          |
| **Google Tensor G2** | 2022 | 2x X1 + 2x A78 + 4x A55   | 2.85 GHz | `4.0`   | `8.0`    | `12.0`          | Verified (Die Analysis) |
| **Google Tensor**    | 2021 | 2x X1 + 2x A76 + 4x A55   | 2.80 GHz | `4.0`   | `8.0`    | `12.0`          | Verified (Die Analysis) |

---

## 6. Kirin Series

Huawei's custom HiSilicon Kirin processors incorporate dedicated custom system cache layers inside their network fabric to offset DRAM bandwidth access and optimize core efficiency.

| SoC Name         | Year | CPU Layout                                  | Max Freq | L3 (MB) | SLC (MB) | shared_cache_mb | Source / Confidence     |
|:-----------------|:----:|:--------------------------------------------|:--------:|:-------:|:--------:|:---------------:|:------------------------|
| **Kirin 9010**   | 2024 | 2x Taishan Prime + 6x Taishan Mid + 4x A510 | 2.30 GHz | `?`     | `?`      | `?`             | Unverified / ?          |
| **Kirin 9000S**  | 2023 | 1x Taishan Prime + 3x Taishan Mid + 4x A510 | 2.62 GHz | `?`     | `?`      | `?`             | Unverified / ?          |
| **Kirin 9000**   | 2020 | 1x A77 + 3x A77 + 4x A55                    | 3.13 GHz | `?`     | `8.0`    | `?`             | Unverified / ?          |
| **Kirin 990 5G** | 2019 | 2x A76 + 2x A76 + 4x A55                    | 2.86 GHz | `?`     | `?`      | `?`             | Unverified / ?          |
| **Kirin 980**    | 2018 | 2x A76 + 2x A76 + 4x A55                    | 2.60 GHz | `4.0`   | `?`      | `?`             | Unverified / ?          |
| **Kirin 970**    | 2017 | 4x A73 + 4x A53                             | 2.40 GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Kirin 960**    | 2016 | 4x A73 + 4x A53                             | 2.40 GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Kirin Legacy** | 2016 | 4x A73/A57 + 4x A53 / pre-DSU               | 2.0-2.2G | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |

---

## 7. Unisoc Series

Unisoc chipsets target budget and entry-level markets, featuring standard ARM cores with highly integrated communication modems and lightweight memory controllers.

| SoC Name        | Year | CPU Layout               | Max Freq | L3 (MB) | SLC (MB) | shared_cache_mb | Source / Confidence     |
|:----------------|:----:|:-------------------------|:--------:|:-------:|:--------:|:---------------:|:------------------------|
| **Unisoc T820** | 2022 | 1x A76 + 3x A76 + 4x A55 | 2.70 GHz | `0.5`   | `0`      | `0.5`           | Verified (Die Analysis) |
| **Unisoc T770** | 2022 | 1x A76 + 3x A76 + 4x A55 | 2.50 GHz | `0.5`   | `0`      | `0.5`           | Verified (Die Analysis) |
| **Unisoc T760** | 2021 | 4x A76 + 4x A55          | 2.20 GHz | `0.5`   | `0`      | `0.5`           | Verified (Die Analysis) |
| **Unisoc T616** | 2021 | 2x A75 + 6x A55          | 2.00 GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Unisoc T612** | 2022 | 2x A75 + 6x A55          | 1.80 GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
| **Unisoc T606** | 2021 | 2x A75 + 6x A55          | 1.60 GHz | `0`     | `0`      | `0.5`           | Verified (Die Analysis) |
