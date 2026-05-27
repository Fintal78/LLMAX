# System on Chip (SoC) Reference (Canonical Source of Truth)

> [!IMPORTANT]
> This file is the **single canonical reference** for all System on Chip (SoC) specifications, core layouts, and cache capacities used across the entire database.
> All subsections in `scoring_rules.md`, `proposed_data_structure.md`, and `scoring_constants.md` that reference CPU cores, clock frequencies, Level 3 (L3) cache sizes, or System Level Cache (SLC) sizes **MUST** use the exact canonical hardware values defined in this file to ensure absolute consistency and auditability.
>
> **Consumers of this file:**
> - **§6.1 CPU Multi-Core Performance:** Raw CPU Throughput Score (RCTS) scaling and core yield calculations, and Cache & Fabric Efficiency Index (CFEI) shared cache scoring.
> - **§6.2 CPU Single-Core Performance:** CPU Architecture Score (CAS) architecture tables.
> - **§6.3 GPU Performance:** GPU hardware class normalization.
> - **§8.1 Battery Endurance:** Layer A (Hardware Efficiency Index) silicon node scaling and CPU cluster efficiency mapping.

---

## 📖 Architectural Overview & Terminology

To assist readers with varying levels of technical knowledge, the following primary hardware terms and abbreviations used throughout this reference are defined below:
* **System on Chip (SoC):** An integrated circuit that integrates all major components of a smartphone (CPU, GPU, NPU, Memory Controller, and Modems) onto a single physical silicon die.
* **Level 1 (L1) & Level 2 (L2) Caches:** Small, ultra-fast memory pools private to individual processor cores (L1) or core clusters (L2) to store frequently accessed instructions and data.
* **Level 3 (L3) Cache:** A larger, shared cache pool managed by the central processor interconnect (e.g., ARM DynamIQ Shared Unit [DSU]) accessible by all CPU cores across the SoC.
* **System Level Cache (SLC):** A massive on-chip Static Random-Access Memory (SRAM) buffer outside the CPU subsystem, shared by the entire chip (including the GPU, NPU, Display Engine, and ISP) to minimize power-hungry external RAM accesses.
* **Cache & Fabric Efficiency Index (CFEI):** The continuous, logarithmic scoring model (`[0.0, 10.0]`) evaluating a chip's total effective shared on-chip cache capacity (`L3 + SLC`) and physical routing layouts.
* **Random Access Memory (RAM) / Dynamic RAM (DRAM):** High-capacity external volatile memory used to store active application states and system data. 

---

## 1. Apple Silicon (A-Series)

Apple A-series SoCs bypass standard Level 3 (L3) caches entirely, utilizing massive cluster-private Level 2 (L2) caches (inherently captured in the CPU Architecture Score [CAS]) and a large system-wide System Level Cache (SLC). Since no Level 3 (L3) cache exists, their effective shared cache capacity is defined strictly as `SLC (MB)`.

| SoC Name             |    Year    | CPU Layout                 |  Max Freq  | L3 (MB) | SLC (MB) | Shared (MB) |   CFEI    |
| :------------------- | :--------: | :------------------------- | :--------: | :-----: | :------: | :---------: | :-------: |
| **Apple A19 Pro**    |    2025    | 2x Everest + 4x Sawtooth   |  4.26 GHz  |   `0`   |  `32.0`  |   `32.0`    | `10.0000` |
| **Apple A18 Pro**    |    2024    | 2x Everest + 4x Sawtooth   |  4.05 GHz  |   `0`   |  `32.0`  |   `32.0`    | `10.0000` |
| **Apple A18**        |    2024    | 2x Everest + 4x Sawtooth   |  4.05 GHz  |   `0`   |  `32.0`  |   `32.0`    | `10.0000` |
| **Apple A17 Pro**    |    2023    | 2x Coll + 4x Sawtooth      |  3.78 GHz  |   `0`   |  `24.0`  |   `24.0`    |  `9.3082` |
| **Apple A16 Bionic** |    2022    | 2x Everest + 4x Sawtooth   |  3.46 GHz  |   `0`   |  `24.0`  |   `24.0`    |  `9.3082` |
| **Apple A15 Bionic** |    2021    | 2x Avalanche + 4x Blizzard |  3.23 GHz  |   `0`   |  `32.0`  |   `32.0`    | `10.0000` |
| **Apple A14 Bionic** |    2020    | 2x Firestorm + 4x Icestorm |  3.10 GHz  |   `0`   |  `16.0`  |   `16.0`    |  `8.3333` |
| **Apple A13 Bionic** |    2019    | 2x Lightning + 4x Thunder  |  2.65 GHz  |   `0`   |  `16.0`  |   `16.0`    |  `8.3333` |
| **Apple A12 Bionic** |    2018    | 2x Vortex + 4x Tempest     |  2.49 GHz  |   `0`   |  `8.0`   |    `8.0`    |  `6.6667` |
| **Apple A11 Bionic** |    2017    | 2x Monsoon + 4x Mistral    |  2.39 GHz  |   `0`   |  `4.0`   |    `4.0`    |  `5.0000` |

---

## 2. Qualcomm Snapdragon Series

Qualcomm chipsets utilize standard ARM DynamIQ Shared Unit (DSU) interconnect architectures combining a central L3 cache and a system-wide System Level Cache (SLC) managed by the Qualcomm Network on Chip (NoC) system bus.

| SoC Name                     |    Year    | CPU Layout                          |  Max Freq  | L3 (MB) | SLC (MB) | Shared (MB) |    CFEI     |
| :--------------------------- | :--------: | :---------------------------------- | :--------: | :-----: | :------: | :---------: | :---------: |
| **Snapdragon 8 Elite**       |    2024    | 2x Oryon Gen 2 + 6x Oryon Gen 2     |  4.32 GHz  |   `0`   |  `8.0`   |    `32.0`   | `9.5000 (*)`|
| **Snapdragon 8 Gen 3**       |    2023    | 1x X4 + 5x A720 + 2x A520           |  3.30 GHz  |  `12.0` |  `6.0`   |    `18.0`   |  `8.6165`   |
| **Snapdragon 8 Gen 2**       |    2022    | 1x X3 + 2x A715 + 2x A710 + 3x A510 |  3.20 GHz  |  `8.0`  |  `6.0`   |    `14.0`   |  `8.0122`   |
| **Snapdragon 8+ Gen 1**      |    2022    | 1x X2 + 3x A710 + 4x A510           |  3.20 GHz  |  `6.0`  |  `4.0`   |    `10.0`   |  `7.2032`   |
| **Snapdragon 8 Gen 1**       |    2021    | 1x X2 + 3x A710 + 4x A510           |  3.00 GHz  |  `6.0`  |  `4.0`   |    `10.0`   |  `7.2032`   |
| **Snapdragon 888+**          |    2021    | 1x X1 + 3x A78 + 4x A55             |  3.00 GHz  |  `4.0`  |  `3.0`   |    `7.0`    |  `6.3456`   |
| **Snapdragon 888**           |    2020    | 1x X1 + 3x A78 + 4x A55             |  2.84 GHz  |  `4.0`  |  `3.0`   |    `7.0`    |  `6.3456`   |
| **Snapdragon 865+**          |    2020    | 1x A77 + 3x A77 + 4x A55            |  3.10 GHz  |  `4.0`  |  `3.0`   |    `7.0`    |  `6.3456`   |
| **Snapdragon 865**           |    2019    | 1x A77 + 3x A77 + 4x A55            |  2.84 GHz  |  `4.0`  |  `3.0`   |    `7.0`    |  `6.3456`   |
| **Snapdragon 855+**          |    2019    | 1x A76 + 3x A76 + 4x A55            |  2.96 GHz  |  `2.0`  |  `2.0`   |    `4.0`    |  `5.0000`   |
| **Snapdragon 855**           |    2018    | 1x A76 + 3x A76 + 4x A55            |  2.84 GHz  |  `2.0`  |  `2.0`   |    `4.0`    |  `5.0000`   |
| **Snapdragon 845**           |    2017    | 4x A75 + 4x A55                     |  2.80 GHz  |  `2.0`  |  `3.0`   |    `5.0`    |  `5.5367`   |
| **Snapdragon 7+ Gen 3**      |    2024    | 1x X4 + 4x A720 + 3x A520           |  2.80 GHz  |  `4.0`  |  `3.5`   |    `7.5`    |  `6.5115`   |
| **Snapdragon 7s Gen 3**      |    2024    | 1x A720 + 3x A720 + 4x A520         |  2.50 GHz  |  `2.0`  |  `1.5`   |    `3.5`    |  `4.6789`   |
| **Snapdragon 7+ Gen 2**      |    2023    | 1x X2 + 3x A710 + 4x A510           |  2.91 GHz  |  `4.0`  |  `3.0`   |    `7.0`    |  `6.3456`   |
| **Snapdragon 7 Gen 3**       |    2023    | 1x A715 + 3x A715 + 4x A510         |  2.63 GHz  |  `2.0`  |  `1.5`   |    `3.5`    |  `4.6789`   |
| **Snapdragon 7s Gen 2**      |    2023    | 4x A78 + 4x A55                     |  2.40 GHz  |  `2.0`  |  `1.5`   |    `3.5`    |  `4.6789`   |
| **Snapdragon 7 Gen 1**       |    2022    | 1x A710 + 3x A710 + 4x A510         |  2.40 GHz  |  `4.0`  |   `0`    |    `4.0`    |  `5.0000`   |
| **Snapdragon 778G+**         |    2021    | 4x A78 + 4x A55                     |  2.50 GHz  |  `2.0`  |  `2.0`   |    `4.0`    |  `5.0000`   |
| **Snapdragon 778G**          |    2021    | 4x A78 + 4x A55                     |  2.40 GHz  |  `2.0`  |  `2.0`   |    `4.0`    |  `5.0000`   |
| **Snapdragon 6 Gen 3**       |    2024    | 4x A78 + 4x A55                     |  2.40 GHz  |  `2.0`  |   `0`    |    `2.0`    |  `3.3333`   |
| **Snapdragon 695**           |    2021    | 2x A78 + 6x A55                     |  2.20 GHz  |  `1.0`  |   `0`    |    `1.0`    |  `1.6667`   |
| **Snapdragon 680**           |    2021    | 4x A73 + 4x A53                     |  2.40 GHz  |   `0`   |   `0`    |    `0.5`    |  `0.0000`   |
| **Qualcomm Legacy**          |  2016-20   | 4x A73/A57 + 4x A53 / pre-DSU       | 2.0-2.2GHz |   `0`   |   `0`    |    `0.5`    |  `0.0000`   |

(*) **Note:** The Snapdragon 8 Elite's Cache & Fabric Efficiency Index (CFEI) includes a custom Oryon Gen 2 Level 2 (L2) cluster fabric penalty of `-0.5000` to reflect interconnect latency overhead between the physically separated CPU core clusters.

---

## 3. MediaTek Dimensity & Helio Series

MediaTek SoCs use large standard L3 caches inside their ARM-based CPU clusters, paired with highly capable System Level Caches (SLC) managed by their custom network fabric to deliver excellent performance sustainability.

| SoC Name                     |    Year    | CPU Layout                  |  Max Freq  | L3 (MB) | SLC (MB) | Shared (MB) |   CFEI    |
| :--------------------------- | :--------: | :-------------------------- | :--------: | :-----: | :------: | :---------: | :-------: |
| **Dimensity 9400+**          |    2025    | 1x X925 + 3x X4 + 4x A720   |  3.63 GHz  |  `12.0` |  `10.0`  |    `22.0`   |  `9.0990` |
| **Dimensity 9400**           |    2024    | 1x X925 + 3x X4 + 4x A720   |  3.63 GHz  |  `12.0` |  `10.0`  |    `22.0`   |  `9.0990` |
| **Dimensity 9300+**          |    2024    | 1x X4 + 3x X4 + 4x A720     |  3.40 GHz  |  `8.0`  |  `10.0`  |    `18.0`   |  `8.6165` |
| **Dimensity 9300**           |    2023    | 1x X4 + 3x X4 + 4x A720     |  3.25 GHz  |  `8.0`  |  `10.0`  |    `18.0`   |  `8.6165` |
| **Dimensity 9200+**          |    2023    | 1x X3 + 3x A715 + 4x A510   |  3.35 GHz  |  `8.0`  |  `6.0`   |    `14.0`   |  `8.0122` |
| **Dimensity 9200**           |    2022    | 1x X3 + 3x A715 + 4x A510   |  3.05 GHz  |  `8.0`  |  `6.0`   |    `14.0`   |  `8.0122` |
| **Dimensity 9000+**          |    2022    | 1x X2 + 3x A710 + 4x A510   |  3.20 GHz  |  `8.0`  |  `6.0`   |    `14.0`   |  `8.0122` |
| **Dimensity 9000**           |    2021    | 1x X2 + 3x A710 + 4x A510   |  3.05 GHz  |  `8.0`  |  `6.0`   |    `14.0`   |  `8.0122` |
| **Dimensity 8300 Ultra**     |    2023    | 4x A715 + 4x A510           |  3.35 GHz  |  `4.0`  |  `4.0`   |    `8.0`    |  `6.6667` |
| **Dimensity 8200**           |    2022    | 4x A78 + 4x A55             |  3.10 GHz  |  `4.0`  |  `4.0`   |    `8.0`    |  `6.6667` |
| **Dimensity 8100**           |    2022    | 4x A78 + 4x A55             |  2.85 GHz  |  `4.0`  |  `4.0`   |    `8.0`    |  `6.6667` |
| **Dimensity 7300**           |    2024    | 4x A78 + 4x A55             |  2.50 GHz  |  `2.0`  |  `2.0`   |    `4.0`    |  `5.0000` |
| **Dimensity 7200**           |    2023    | 2x A715 + 6x A510           |  2.80 GHz  |  `2.0`  |  `2.0`   |    `4.0`    |  `5.0000` |
| **Dimensity 6300**           |    2024    | 2x A76 + 6x A55             |  2.40 GHz  |  `2.0`  |   `0`    |    `2.0`    |  `3.3333` |
| **Dimensity 1080**           |    2022    | 2x A78 + 6x A55             |  2.60 GHz  |  `2.0`  |   `0`    |    `2.0`    |  `3.3333` |
| **Dimensity 920**            |    2021    | 2x A78 + 6x A55             |  2.50 GHz  |  `2.0`  |   `0`    |    `2.0`    |  `3.3333` |
| **Helio G99**                |    2022    | 2x A76 + 6x A55             |  2.20 GHz  |   `0`   |   `0`    |    `0.5`    |  `0.0000` |
| **Helio G85**                |    2020    | 2x A75 + 6x A55             |  2.00 GHz  |   `0`   |   `0`    |    `0.5`    |  `0.0000` |
| **MediaTek Legacy**          |  2018-22   | 2x A76/A75 + 6x A55 / pre   | 2.0-2.2GHz |   `0`   |   `0`    |    `0.5`    |  `0.0000` |

---

## 4. Samsung Exynos Series

Samsung Exynos SoCs are developed with custom coherent interconnects (such as the Samsung Coherent Interconnect [SCI]) coordinating robust L3 and system caches to provide high internal bandwidth.

| SoC Name             |    Year    | CPU Layout                          |  Max Freq  | L3 (MB) | SLC (MB) | Shared (MB) |   CFEI    |
| :------------------- | :--------: | :---------------------------------- | :--------: | :-----: | :------: | :---------: | :-------: |
| **Exynos 2500**      |    2025    | 1x X5 + 2x A725 + 5x A725 + 2x A520 |  3.30 GHz  |  `8.0`  |  `8.0`   |    `16.0`   |  `8.3333` |
| **Exynos 2400**      |    2024    | 1x X4 + 2x A720 + 3x A720 + 4x A520 |  3.20 GHz  |  `8.0`  |  `8.0`   |    `16.0`   |  `8.3333` |
| **Exynos 2400e**     |    2024    | 1x X4 + 2x A720 + 3x A720 + 4x A520 |  3.10 GHz  |  `8.0`  |  `8.0`   |    `16.0`   |  `8.3333` |
| **Exynos 2200**      |    2022    | 1x X2 + 3x A710 + 4x A510           |  2.80 GHz  |  `4.0`  |  `4.0`   |    `8.0`    |  `6.6667` |
| **Exynos 2100**      |    2021    | 1x X1 + 3x A78 + 4x A55             |  2.90 GHz  |  `4.0`  |  `6.0`   |    `10.0`   |  `7.2032` |
| **Exynos 990**       |    2020    | 2x M5 + 2x A76 + 4x A55             |  2.73 GHz  |  `4.0`  |  `4.0`   |    `8.0`    |  `6.6667` |
| **Exynos 9825**      |    2019    | 2x M4 + 2x A75 + 4x A55             |  2.84 GHz  |  `4.0`  |  `2.0`   |    `6.0`    |  `5.9749` |
| **Exynos 9820**      |    2019    | 2x M4 + 2x A75 + 4x A55             |  2.73 GHz  |  `4.0`  |  `2.0`   |    `6.0`    |  `5.9749` |
| **Exynos 1580**      |    2024    | 1x A720 + 3x A720 + 4x A520         |  2.90 GHz  |  `4.0`  |  `2.0`   |    `6.0`    |  `5.9749` |
| **Exynos 1480**      |    2024    | 4x A78 + 4x A55                     |  2.75 GHz  |  `2.0`  |  `2.0`   |    `4.0`    |  `5.0000` |
| **Exynos 1380**      |    2023    | 4x A78 + 4x A55                     |  2.40 GHz  |  `1.5`  |   `0`    |    `1.5`    |  `2.6416` |
| **Exynos 1280**      |    2022    | 2x A78 + 6x A55                     |  2.40 GHz  |  `1.5`  |   `0`    |    `1.5`    |  `2.6416` |
| **Exynos 1330**      |    2023    | 2x A78 + 6x A55                     |  2.40 GHz  |  `1.5`  |   `0`    |    `1.5`    |  `2.6416` |

---

## 5. Google Tensor Series

Google Tensor chipsets are co-designed with Samsung's custom Exynos manufacturing platform, sharing equivalent DSU-hosted L3 and large 8 megabyte (MB) SLC structures to accelerate on-device machine learning operations.

| SoC Name             |    Year    | CPU Layout                 |  Max Freq  | L3 (MB) | SLC (MB) | Shared (MB) |   CFEI    |
| :------------------- | :--------: | :------------------------- | :--------: | :-----: | :------: | :---------: | :-------: |
| **Google Tensor G4** |    2024    | 1x X4 + 3x A720 + 4x A520  |  3.10 GHz  |  `4.0`  |  `8.0`   |    `12.0`   |  `7.6416` |
| **Google Tensor G3** |    2023    | 1x X3 + 4x A715 + 4x A510  |  2.91 GHz  |  `4.0`  |  `8.0`   |    `12.0`   |  `7.6416` |
| **Google Tensor G2** |    2022    | 2x X1 + 2x A78 + 4x A55    |  2.85 GHz  |  `4.0`  |  `8.0`   |    `12.0`   |  `7.6416` |
| **Google Tensor G1** |    2021    | 2x X1 + 2x A76 + 4x A55    |  2.80 GHz  |  `4.0`  |  `8.0`   |    `12.0`   |  `7.6416` |

---

## 6. HiSilicon Kirin Series

Huawei's custom HiSilicon Kirin processors incorporate dedicated custom system cache layers inside their network fabric to offset DRAM bandwidth access and optimize core efficiency.

| SoC Name                                   |    Year    | CPU Layout                                  |  Max Freq  | L3 (MB) | SLC (MB) | Shared (MB) |   CFEI    |
| :----------------------------------------- | :--------: | :------------------------------------------ | :--------: | :-----: | :------: | :---------: | :-------: |
| **HiSilicon Kirin 9010**                   |    2024    | 2x Taishan Prime + 6x Taishan Mid + 4x A510 |  2.30 GHz  |  `4.0`  |  `8.0`   |    `12.0`   |  `7.6416` |
| **HiSilicon Kirin 9000S**                  |    2023    | 1x Taishan Prime + 3x Taishan Mid + 4x A510 |  2.62 GHz  |  `4.0`  |  `8.0`   |    `12.0`   |  `7.6416` |
| **HiSilicon Kirin 9000**                   |    2020    | 1x A77 + 3x A77 + 4x A55                    |  3.13 GHz  |  `4.0`  |  `8.0`   |    `12.0`   |  `7.6416` |
| **HiSilicon Kirin 990 5G**                 |    2019    | 2x A76 + 2x A76 + 4x A55                    |  2.86 GHz  |  `4.0`  |  `4.0`   |    `8.0`    |  `6.6667` |
| **HiSilicon Kirin 980**                    |    2018    | 2x A76 + 2x A76 + 4x A55                    |  2.60 GHz  |  `4.0`  |  `2.0`   |    `6.0`    |  `5.9749` |
| **HiSilicon Kirin 970**                    |    2017    | 4x A73 + 4x A53                             |  2.40 GHz  |   `0`   |   `0`    |    `0.5`    |  `0.0000` |
| **HiSilicon Legacy**                       |    2016    | 4x A73/A57 + 4x A53 / pre-DSU               |  2.0-2.2G  |   `0`   |   `0`    |    `0.5`    |  `0.0000` |
