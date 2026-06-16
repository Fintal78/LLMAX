# AI Software Stack Scoring Simulations & Verification Matrix

This document lists the simulated chipset/OS pairings used to verify and battletest the AI Software Stack classification algorithm in Section 6.4. It maps the criteria specified in `scoring_rules.md` and `proposed_data_structure.md` to deterministic scoring results for all unique devices in the database.

### Tier Legend
* **Tier 1 (T1) - Native Synergistic (Score: 10.00):** Manufacturer-designed native OS framework & silicon compiler (e.g., Apple Core ML, Google Android AICore/Edge TPU, Huawei MindSpore).
* **Tier 2 (T2) - SDK Co-Optimized (Score: 8.00):** 3rd-party SoC with vendor optimization SDK (e.g., Qualcomm QNN, MediaTek NeuroPilot, Samsung ENN) or dedicated custom co-processors.
* **Tier 3 (T3) - Hardware Accelerated / Optimized Fallback (Score: 5.50):** Legacy GPU acceleration (Apple Metal/MPS), DSP/HVX vector processing, or unlisted NPUs on generic APIs.
* **Tier 4 (T4) - CPU/GPU Fallback (Score: 3.00):** Standard system CPU/GPU execution without specific acceleration (e.g., generic Android NNAPI, early iOS fallback).
* **Tier 5 (T5) - Minimal / None (Score: 0.00):** Feature phones or legacy/non-smart platforms lacking any ML execution framework.

| Device                                           | OS             | SoC Model                                     | Rule Triggered                     | Tier (Score) |
| :----------------------------------------------- | :------------- | :-------------------------------------------- | :--------------------------------- | :----------: |
| Alcatel Alcatel 1S (32GB/3GB RAM)                | Android        | Helio P22 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Apple iPhone (1st gen) (16GB/0.128GB RAM)        | iOS            | Samsung S5L8900 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone (1st gen) (4GB/0.128GB RAM)         | iOS            | Samsung S5L8900 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone (1st gen) (8GB/0.128GB RAM)         | iOS            | Samsung S5L8900 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 11 (128GB/4GB RAM)                  | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 (256GB/4GB RAM)                  | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 (64GB/4GB RAM)                   | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 Pro (256GB/4GB RAM)              | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 Pro (512GB/4GB RAM)              | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 Pro (64GB/4GB RAM)               | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 Pro Max (256GB/4GB RAM)          | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 Pro Max (512GB/4GB RAM)          | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 11 Pro Max (64GB/4GB RAM)           | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 (128GB/4GB RAM)                  | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 (256GB/4GB RAM)                  | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 (64GB/4GB RAM)                   | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Mini (128GB/4GB RAM)             | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Mini (256GB/4GB RAM)             | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Mini (64GB/4GB RAM)              | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Pro (128GB/6GB RAM)              | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Pro (256GB/6GB RAM)              | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Pro (512GB/6GB RAM)              | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Pro Max (128GB/6GB RAM)          | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Pro Max (256GB/6GB RAM)          | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 12 Pro Max (512GB/6GB RAM)          | iOS            | Apple A14 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 (128GB/4GB RAM)                  | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 (256GB/4GB RAM)                  | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 (512GB/4GB RAM)                  | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Mini (128GB/4GB RAM)             | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Mini (256GB/4GB RAM)             | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Mini (512GB/4GB RAM)             | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro (1024GB/6GB RAM)             | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro (128GB/6GB RAM)              | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro (256GB/6GB RAM)              | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro (512GB/6GB RAM)              | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro Max (1024GB/6GB RAM)         | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro Max (128GB/6GB RAM)          | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro Max (256GB/6GB RAM)          | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 13 Pro Max (512GB/6GB RAM)          | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 (128GB/6GB RAM)                  | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 (256GB/6GB RAM)                  | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 (512GB/6GB RAM)                  | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Plus (128GB/6GB RAM)             | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Plus (256GB/6GB RAM)             | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Plus (512GB/6GB RAM)             | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro (1024GB/6GB RAM)             | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro (128GB/6GB RAM)              | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro (256GB/6GB RAM)              | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro (512GB/6GB RAM)              | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro Max (1024GB/6GB RAM)         | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro Max (128GB/6GB RAM)          | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro Max (256GB/6GB RAM)          | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 14 Pro Max (512GB/6GB RAM)          | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 (128GB/6GB RAM)                  | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 (256GB/6GB RAM)                  | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 (512GB/6GB RAM)                  | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Plus (128GB/6GB RAM)             | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Plus (256GB/6GB RAM)             | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Plus (512GB/6GB RAM)             | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Pro (1024GB/8GB RAM)             | iOS            | Apple A17 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Pro (128GB/8GB RAM)              | iOS            | Apple A17 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Pro (256GB/8GB RAM)              | iOS            | Apple A17 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Pro (512GB/8GB RAM)              | iOS            | Apple A17 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Pro Max (1024GB/8GB RAM)         | iOS            | Apple A17 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Pro Max (256GB/8GB RAM)          | iOS            | Apple A17 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 15 Pro Max (512GB/8GB RAM)          | iOS            | Apple A17 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 (128GB/8GB RAM)                  | iOS            | Apple A18 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 (256GB/8GB RAM)                  | iOS            | Apple A18 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 (512GB/8GB RAM)                  | iOS            | Apple A18 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Plus (128GB/8GB RAM)             | iOS            | Apple A18 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Plus (256GB/8GB RAM)             | iOS            | Apple A18 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Plus (512GB/8GB RAM)             | iOS            | Apple A18 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Pro (1024GB/8GB RAM)             | iOS            | Apple A18 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Pro (256GB/8GB RAM)              | iOS            | Apple A18 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Pro (512GB/8GB RAM)              | iOS            | Apple A18 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Pro Max (1024GB/8GB RAM)         | iOS            | Apple A18 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Pro Max (256GB/8GB RAM)          | iOS            | Apple A18 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16 Pro Max (512GB/8GB RAM)          | iOS            | Apple A18 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16e (128GB/8GB RAM)                 | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16e (256GB/8GB RAM)                 | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 16e (512GB/8GB RAM)                 | iOS            | Apple A16 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 (128GB/8GB RAM)                  | iOS            | Apple A19 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 (256GB/8GB RAM)                  | iOS            | Apple A19 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 (512GB/8GB RAM)                  | iOS            | Apple A19 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Air (256GB/8GB RAM)              | iOS            | Apple A19 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Air (512GB/8GB RAM)              | iOS            | Apple A19 (Apple)                             | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Pro (1024GB/12GB RAM)            | iOS            | Apple A19 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Pro (256GB/12GB RAM)             | iOS            | Apple A19 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Pro (512GB/12GB RAM)             | iOS            | Apple A19 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Pro Max (1024GB/12GB RAM)        | iOS            | Apple A19 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Pro Max (256GB/12GB RAM)         | iOS            | Apple A19 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 17 Pro Max (512GB/12GB RAM)         | iOS            | Apple A19 Pro (Apple)                         | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 3G (16GB/0.128GB RAM)               | iOS            | Samsung S5L8900 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 3G (8GB/0.128GB RAM)                | iOS            | Samsung S5L8900 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 3GS (16GB/0.256GB RAM)              | iOS            | Samsung S5PC100 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 3GS (32GB/0.256GB RAM)              | iOS            | Samsung S5PC100 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 3GS (8GB/0.256GB RAM)               | iOS            | Samsung S5PC100 (Samsung)                     | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 4 (16GB/0.5GB RAM)                  | iOS            | Apple A4 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 4 (32GB/0.5GB RAM)                  | iOS            | Apple A4 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 4 (8GB/0.5GB RAM)                   | iOS            | Apple A4 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 4S (16GB/0.5GB RAM)                 | iOS            | Apple A5 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 4S (32GB/0.5GB RAM)                 | iOS            | Apple A5 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 4S (64GB/0.5GB RAM)                 | iOS            | Apple A5 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 4S (8GB/0.5GB RAM)                  | iOS            | Apple A5 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5 (16GB/1GB RAM)                    | iOS            | Apple A6 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5 (32GB/1GB RAM)                    | iOS            | Apple A6 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5 (64GB/1GB RAM)                    | iOS            | Apple A6 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5c (16GB/1GB RAM)                   | iOS            | Apple A6 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5c (32GB/1GB RAM)                   | iOS            | Apple A6 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5c (8GB/1GB RAM)                    | iOS            | Apple A6 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5s (16GB/1GB RAM)                   | iOS            | Apple A7 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5s (32GB/1GB RAM)                   | iOS            | Apple A7 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 5s (64GB/1GB RAM)                   | iOS            | Apple A7 (Apple)                              | iOS CPU/GPU Fallback               |  T4 (3.00)   |
| Apple iPhone 6 (128GB/1GB RAM)                   | iOS            | Apple A8 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6 (16GB/1GB RAM)                    | iOS            | Apple A8 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6 (64GB/1GB RAM)                    | iOS            | Apple A8 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6 Plus (128GB/1GB RAM)              | iOS            | Apple A8 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6 Plus (16GB/1GB RAM)               | iOS            | Apple A8 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6 Plus (64GB/1GB RAM)               | iOS            | Apple A8 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s (128GB/2GB RAM)                  | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s (16GB/2GB RAM)                   | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s (32GB/2GB RAM)                   | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s (64GB/2GB RAM)                   | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s Plus (128GB/2GB RAM)             | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s Plus (16GB/2GB RAM)              | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s Plus (32GB/2GB RAM)              | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 6s Plus (64GB/2GB RAM)              | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 7 (128GB/2GB RAM)                   | iOS            | Apple A10 Fusion (Apple)                      | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 7 (256GB/2GB RAM)                   | iOS            | Apple A10 Fusion (Apple)                      | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 7 (32GB/2GB RAM)                    | iOS            | Apple A10 Fusion (Apple)                      | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 7 Plus (128GB/3GB RAM)              | iOS            | Apple A10 Fusion (Apple)                      | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 7 Plus (256GB/3GB RAM)              | iOS            | Apple A10 Fusion (Apple)                      | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 7 Plus (32GB/3GB RAM)               | iOS            | Apple A10 Fusion (Apple)                      | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone 8 (256GB/2GB RAM)                   | iOS            | Apple A11 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 8 (64GB/2GB RAM)                    | iOS            | Apple A11 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 8 Plus (256GB/3GB RAM)              | iOS            | Apple A11 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone 8 Plus (64GB/3GB RAM)               | iOS            | Apple A11 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone SE (1st gen) (128GB/2GB RAM)        | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone SE (1st gen) (16GB/2GB RAM)         | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone SE (1st gen) (32GB/2GB RAM)         | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone SE (1st gen) (64GB/2GB RAM)         | iOS            | Apple A9 (Apple)                              | Apple GPU (Metal/MPS)              |  T3 (5.50)   |
| Apple iPhone SE (2nd gen) (128GB/3GB RAM)        | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone SE (2nd gen) (256GB/3GB RAM)        | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone SE (2nd gen) (64GB/3GB RAM)         | iOS            | Apple A13 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone SE (3rd gen) (128GB/4GB RAM)        | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone SE (3rd gen) (256GB/4GB RAM)        | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone SE (3rd gen) (64GB/4GB RAM)         | iOS            | Apple A15 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone X (256GB/3GB RAM)                   | iOS            | Apple A11 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone X (64GB/3GB RAM)                    | iOS            | Apple A11 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XR (128GB/3GB RAM)                  | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XR (256GB/3GB RAM)                  | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XR (64GB/3GB RAM)                   | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XS (256GB/4GB RAM)                  | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XS (512GB/4GB RAM)                  | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XS (64GB/4GB RAM)                   | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XS Max (256GB/4GB RAM)              | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XS Max (512GB/4GB RAM)              | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Apple iPhone XS Max (64GB/4GB RAM)               | iOS            | Apple A12 Bionic (Apple)                      | Apple NPU (Neural Engine)          |  T1 (10.00)  |
| Asus ROG Phone 8 Pro (1024GB/16GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus ROG Phone 8 Pro (512GB/16GB RAM)            | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus ROG Phone 9 (256GB/12GB RAM)                | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus ROG Phone 9 (512GB/12GB RAM)                | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus ROG Phone 9 Pro (1024GB/16GB RAM)           | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus ROG Phone 9 Pro (512GB/16GB RAM)            | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus Zenfone 10 (128GB/8GB RAM)                  | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus Zenfone 10 (256GB/8GB RAM)                  | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus Zenfone 10 (512GB/8GB RAM)                  | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus Zenfone 11 Ultra (256GB/12GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Asus Zenfone 11 Ultra (512GB/12GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| BLU BLU G91 Pro (128GB/6GB RAM)                  | Android        | Helio G90 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| BlackBerry BlackBerry Key2 (128GB/6GB RAM)       | Android        | Snapdragon 660 (Qualcomm)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| BlackBerry BlackBerry Key2 (64GB/6GB RAM)        | Android        | Snapdragon 660 (Qualcomm)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| BlackBerry Key2 LE (32GB/4GB RAM)                | Android        | Snapdragon 636 (Qualcomm)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| BlackBerry Key2 LE (64GB/4GB RAM)                | Android        | Snapdragon 636 (Qualcomm)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Blackview BL9000 Pro (512GB/12GB RAM)            | Android        | Dimensity 8020 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Blackview BV9300 Pro (256GB/12GB RAM)            | Android        | Helio G99 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Blackview Blackview BV9300 (256GB/12GB RAM)      | Android        | Helio G99 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Coolpad Coolpad Cool 20 (128GB/4GB RAM)          | Android        | Helio G80 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Coolpad Coolpad Cool 20 (64GB/4GB RAM)           | Android        | Helio G80 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Doogee DK10 (512GB/12GB RAM)                     | Android        | Dimensity 8020 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Doogee Doogee V Max (256GB/12GB RAM)             | Android        | Dimensity 1080 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Doogee V31 GT (256GB/12GB RAM)                   | Android        | Dimensity 1080 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Fairphone Fairphone 4 (128GB/6GB RAM)            | Android        | Snapdragon 750G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Fairphone Fairphone 4 (256GB/6GB RAM)            | Android        | Snapdragon 750G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Fairphone Fairphone 5 (256GB/8GB RAM)            | Android        | QCM6490 (Qualcomm)                            | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Gionee Gionee G13 Pro (32GB/4GB RAM)             | Android        | Tiger T310 (Unisoc)                           | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Google Pixel (128GB/4GB RAM)                     | Android        | Snapdragon 821 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel (32GB/4GB RAM)                      | Android        | Snapdragon 821 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 2 (128GB/4GB RAM)                   | Android        | Snapdragon 835 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 2 (64GB/4GB RAM)                    | Android        | Snapdragon 835 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 2 XL (128GB/4GB RAM)                | Android        | Snapdragon 835 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 2 XL (64GB/4GB RAM)                 | Android        | Snapdragon 835 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 3 (128GB/4GB RAM)                   | Android        | Snapdragon 845 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 3 (64GB/4GB RAM)                    | Android        | Snapdragon 845 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 3 XL (128GB/4GB RAM)                | Android        | Snapdragon 845 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 3 XL (64GB/4GB RAM)                 | Android        | Snapdragon 845 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 3a (64GB/4GB RAM)                   | Android        | Snapdragon 670 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 3a XL (64GB/4GB RAM)                | Android        | Snapdragon 670 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 4 (128GB/6GB RAM)                   | Android        | Snapdragon 855 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 4 (64GB/6GB RAM)                    | Android        | Snapdragon 855 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 4 XL (128GB/6GB RAM)                | Android        | Snapdragon 855 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 4 XL (64GB/6GB RAM)                 | Android        | Snapdragon 855 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 4a (128GB/6GB RAM)                  | Android        | Snapdragon 730G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 4a (5G) (128GB/6GB RAM)             | Android        | Snapdragon 765G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 5 (128GB/8GB RAM)                   | Android        | Snapdragon 765G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 5a (128GB/6GB RAM)                  | Android        | Snapdragon 765G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel 6 (128GB/8GB RAM)                   | Android        | Google Tensor (Google)                        | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 6 (256GB/8GB RAM)                   | Android        | Google Tensor (Google)                        | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 6 Pro (128GB/12GB RAM)              | Android        | Google Tensor (Google)                        | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 6 Pro (256GB/12GB RAM)              | Android        | Google Tensor (Google)                        | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 6 Pro (512GB/12GB RAM)              | Android        | Google Tensor (Google)                        | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 6a (128GB/6GB RAM)                  | Android        | Google Tensor (Google)                        | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 7 (128GB/8GB RAM)                   | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 7 (256GB/8GB RAM)                   | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 7 Pro (128GB/12GB RAM)              | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 7 Pro (256GB/12GB RAM)              | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 7 Pro (512GB/12GB RAM)              | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 7a (128GB/8GB RAM)                  | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8 (128GB/8GB RAM)                   | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8 (256GB/8GB RAM)                   | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8 Pro (1024GB/12GB RAM)             | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8 Pro (128GB/12GB RAM)              | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8 Pro (256GB/12GB RAM)              | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8 Pro (512GB/12GB RAM)              | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8a (128GB/8GB RAM)                  | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 8a (256GB/8GB RAM)                  | Android        | Google Tensor G3 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 (128GB/12GB RAM)                  | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 (256GB/12GB RAM)                  | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro (1024GB/16GB RAM)             | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro (128GB/16GB RAM)              | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro (256GB/16GB RAM)              | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro (512GB/16GB RAM)              | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro Fold (256GB/16GB RAM)         | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro Fold (512GB/16GB RAM)         | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro XL (1024GB/16GB RAM)          | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro XL (128GB/16GB RAM)           | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro XL (256GB/16GB RAM)           | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9 Pro XL (512GB/16GB RAM)           | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9a (128GB/8GB RAM)                  | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel 9a (256GB/8GB RAM)                  | Android        | Google Tensor G4 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel Fold (256GB/12GB RAM)               | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel Fold (512GB/12GB RAM)               | Android        | Google Tensor G2 (Google)                     | Google Tensor TPU (Native)         |  T1 (10.00)  |
| Google Pixel XL (128GB/4GB RAM)                  | Android        | Snapdragon 821 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Google Pixel XL (32GB/4GB RAM)                   | Android        | Snapdragon 821 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| HTC Desire 21 Pro 5G (128GB/8GB RAM)             | Android        | Snapdragon 690 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| HTC Desire 22 Pro (128GB/8GB RAM)                | Android        | Snapdragon 695 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| HTC HTC U23 Pro (256GB/8GB RAM)                  | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| HTC U23 Pro (256GB/8GB RAM)                      | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| HTC U24 Pro (256GB/12GB RAM)                     | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| HTC Wildfire E7 Plus (128GB/4GB RAM)             | Android        | Unisoc T606 (Unisoc)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Honor Honor 200 (256GB/8GB RAM)                  | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Honor 200 (512GB/8GB RAM)                  | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Honor 200 Pro (256GB/12GB RAM)             | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Honor 200 Pro (512GB/12GB RAM)             | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Honor 90 Smart (128GB/4GB RAM)             | Android        | Dimensity 6080 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Honor Magic 6 (256GB/12GB RAM)                   | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 6 (512GB/12GB RAM)                   | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 6 Pro (1024GB/12GB RAM)              | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 6 Pro (256GB/12GB RAM)               | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 6 Pro (512GB/12GB RAM)               | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 7 (1024GB/12GB RAM)                  | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 7 (256GB/12GB RAM)                   | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 7 (512GB/12GB RAM)                   | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 7 Pro (1024GB/12GB RAM)              | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 7 Pro (256GB/12GB RAM)               | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic 7 Pro (512GB/12GB RAM)               | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic V3 (1024GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic V3 (256GB/12GB RAM)                  | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic V3 (512GB/12GB RAM)                  | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic6 Ultimate (1024GB/16GB RAM)          | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Honor Magic6 Ultimate (512GB/16GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Mate 10 (64GB/4GB RAM)                    | HarmonyOS      | Kirin 970 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 10 Pro (128GB/6GB RAM)               | HarmonyOS      | Kirin 970 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 20 (128GB/4GB RAM)                   | HarmonyOS      | Kirin 980 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 20 Pro (128GB/6GB RAM)               | HarmonyOS      | Kirin 980 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 20 Pro (256GB/6GB RAM)               | HarmonyOS      | Kirin 980 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 30 (128GB/6GB RAM)                   | HarmonyOS      | Kirin 990 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 30 (256GB/6GB RAM)                   | HarmonyOS      | Kirin 990 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 30 Pro (128GB/8GB RAM)               | HarmonyOS      | Kirin 990 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 30 Pro (256GB/8GB RAM)               | HarmonyOS      | Kirin 990 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 40 (128GB/8GB RAM)                   | HarmonyOS      | Kirin 9000E (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 40 (256GB/8GB RAM)                   | HarmonyOS      | Kirin 9000E (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 40 Pro (128GB/8GB RAM)               | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 40 Pro (256GB/8GB RAM)               | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 40 Pro (512GB/8GB RAM)               | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 40 Pro Plus (256GB/12GB RAM)         | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 40 Pro Plus (512GB/12GB RAM)         | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 50 (128GB/8GB RAM)                   | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Mate 50 (256GB/8GB RAM)                   | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Mate 50 (512GB/8GB RAM)                   | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Mate 50 Pro (256GB/8GB RAM)               | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Mate 50 Pro (512GB/8GB RAM)               | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Mate 50 RS (512GB/12GB RAM)               | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Mate 60 (256GB/12GB RAM)                  | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 (512GB/12GB RAM)                  | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 Pro (256GB/12GB RAM)              | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 Pro (512GB/12GB RAM)              | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 Pro Plus (1024GB/16GB RAM)        | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 Pro Plus (256GB/16GB RAM)         | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 Pro Plus (512GB/16GB RAM)         | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 RS (1024GB/16GB RAM)              | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 60 RS (512GB/16GB RAM)               | HarmonyOS      | Kirin 9000s (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Mate 70 (256GB/12GB RAM)                  | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate 70 (512GB/12GB RAM)                  | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate 70 Pro (256GB/12GB RAM)              | HarmonyOS NEXT | Kirin 9020 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate 70 Pro (512GB/12GB RAM)              | HarmonyOS NEXT | Kirin 9020 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate 70 Pro Plus (1024GB/16GB RAM)        | HarmonyOS NEXT | Kirin 9020 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate 70 Pro Plus (512GB/16GB RAM)         | HarmonyOS NEXT | Kirin 9020 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate 70 RS (1024GB/16GB RAM)              | HarmonyOS NEXT | Kirin 9020 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate 70 RS (512GB/16GB RAM)               | HarmonyOS NEXT | Kirin 9020 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate XT Ultimate (1024GB/16GB RAM)        | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Mate XT Ultimate (512GB/16GB RAM)         | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Nova 12 Pro (256GB/12GB RAM)              | HarmonyOS      | Kirin 8000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Nova 12 Pro (512GB/12GB RAM)              | HarmonyOS      | Kirin 8000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Nova 12 Ultra (1024GB/12GB RAM)           | HarmonyOS      | Kirin 9000SL (HiSilicon)                      | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei Nova 12 Ultra (512GB/12GB RAM)            | HarmonyOS      | Kirin 9000SL (HiSilicon)                      | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P20 (128GB/4GB RAM)                       | HarmonyOS      | Kirin 970 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P20 Pro (128GB/6GB RAM)                   | HarmonyOS      | Kirin 970 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P20 Pro (256GB/6GB RAM)                   | HarmonyOS      | Kirin 970 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P30 (128GB/6GB RAM)                       | HarmonyOS      | Kirin 980 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P30 Pro (128GB/8GB RAM)                   | HarmonyOS      | Kirin 980 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P30 Pro (256GB/8GB RAM)                   | HarmonyOS      | Kirin 980 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P30 Pro (512GB/8GB RAM)                   | HarmonyOS      | Kirin 980 (HiSilicon)                         | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P40 (128GB/8GB RAM)                       | HarmonyOS      | Kirin 990 5G (HiSilicon)                      | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P40 Pro (256GB/8GB RAM)                   | HarmonyOS      | Kirin 990 5G (HiSilicon)                      | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P40 Pro (512GB/8GB RAM)                   | HarmonyOS      | Kirin 990 5G (HiSilicon)                      | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P40 Pro Plus (512GB/8GB RAM)              | HarmonyOS      | Kirin 990 5G (HiSilicon)                      | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P50 (128GB/8GB RAM)                       | HarmonyOS      | Snapdragon 888 4G (Qualcomm)                  | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P50 (256GB/8GB RAM)                       | HarmonyOS      | Snapdragon 888 4G (Qualcomm)                  | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P50 Pro (128GB/8GB RAM)                   | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P50 Pro (256GB/8GB RAM)                   | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P50 Pro (512GB/8GB RAM)                   | HarmonyOS      | Kirin 9000 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS      |  T1 (10.00)  |
| Huawei P60 (128GB/8GB RAM)                       | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P60 (256GB/8GB RAM)                       | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P60 (512GB/8GB RAM)                       | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P60 Art (1024GB/12GB RAM)                 | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P60 Art (256GB/12GB RAM)                  | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P60 Art (512GB/12GB RAM)                  | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P60 Pro (256GB/8GB RAM)                   | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei P60 Pro (512GB/8GB RAM)                   | HarmonyOS      | Snapdragon 8+ Gen 1 4G (Qualcomm)             | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Huawei Pocket 2 (1024GB/12GB RAM)                | HarmonyOS NEXT | Kirin 9000S (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pocket 2 (256GB/12GB RAM)                 | HarmonyOS NEXT | Kirin 9000S (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pocket 2 (512GB/12GB RAM)                 | HarmonyOS NEXT | Kirin 9000S (HiSilicon)                       | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 (256GB/12GB RAM)                  | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 (512GB/12GB RAM)                  | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 Pro (256GB/12GB RAM)              | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 Pro (512GB/12GB RAM)              | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 Pro Plus (1024GB/16GB RAM)        | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 Pro Plus (512GB/16GB RAM)         | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 Ultra (1024GB/16GB RAM)           | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Huawei Pura 70 Ultra (512GB/16GB RAM)            | HarmonyOS NEXT | Kirin 9010 (HiSilicon)                        | Huawei Kirin NPU on HarmonyOS NEXT |  T1 (10.00)  |
| Infinix GT 20 Pro (256GB/8GB RAM)                | Android        | Dimensity 8200 Ultimate (MediaTek)            | MediaTek NPU SDK                   |  T2 (8.00)   |
| Infinix Note 40 Pro (256GB/8GB RAM)              | Android        | Helio G99 Ultimate (MediaTek)                 | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Infinix Note 40 Pro+ 5G (256GB/12GB RAM)         | Android        | Dimensity 7020 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Infinix Zero 30 (256GB/8GB RAM)                  | Android        | Dimensity 8020 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Infinix Zero Ultra (256GB/8GB RAM)               | Android        | Dimensity 920 (MediaTek)                      | MediaTek NPU SDK                   |  T2 (8.00)   |
| Itel itel S24 (128GB/4GB RAM)                    | Android        | Helio G91 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Itel itel S24 (256GB/4GB RAM)                    | Android        | Helio G91 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Karbonn Karbonn Titanium X (16GB/1GB RAM)        | Android        | Quad-core 1.5 GHz (Unknown)                   | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Karbonn Titanium X (16GB/1GB RAM)                | Android        | Quad-core 1.5 GHz (Unknown)                   | Android CPU/GPU Fallback           |  T4 (3.00)   |
| LG K92 5G (128GB/6GB RAM)                        | Android        | Snapdragon 690 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| LG LG V60 ThinQ (128GB/8GB RAM)                  | Android        | Snapdragon 865 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| LG LG V60 ThinQ (256GB/8GB RAM)                  | Android        | Snapdragon 865 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| LG LG Velvet (128GB/6GB RAM)                     | Android        | Snapdragon 765G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| LG V60 ThinQ 5G (128GB/8GB RAM)                  | Android        | Snapdragon 865 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| LG V60 ThinQ 5G (256GB/8GB RAM)                  | Android        | Snapdragon 865 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| LG Velvet 5G (128GB/6GB RAM)                     | Android        | Snapdragon 765G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| LG W41 Pro (128GB/6GB RAM)                       | Android        | Helio G35 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| LG Wing (128GB/8GB RAM)                          | Android        | Snapdragon 765G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| LG Wing (256GB/8GB RAM)                          | Android        | Snapdragon 765G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Lava Agni 3 (128GB/8GB RAM)                      | Android        | Dimensity 7300X (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Lava Agni 3 (256GB/8GB RAM)                      | Android        | Dimensity 7300X (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Lava Curve 5G (128GB/8GB RAM)                    | Android        | Dimensity 7050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Lava Curve 5G (256GB/8GB RAM)                    | Android        | Dimensity 7050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Lava Lava Agni 2 (256GB/8GB RAM)                 | Android        | Dimensity 7050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| LeEco LeEco Le Pro 3 (32GB/4GB RAM)              | Android        | Snapdragon 821 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| LeEco LeEco Le Pro 3 (64GB/4GB RAM)              | Android        | Snapdragon 821 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Lenovo Lenovo Legion Y90 (256GB/12GB RAM)        | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Lenovo Lenovo Legion Y90 (512GB/12GB RAM)        | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Meizu Meizu 21 (256GB/8GB RAM)                   | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Meizu Meizu 21 (512GB/8GB RAM)                   | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Meizu Meizu 21 Note (256GB/16GB RAM)             | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Meizu Meizu 21 Note (512GB/16GB RAM)             | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Meizu Meizu 21 Pro (1024GB/12GB RAM)             | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Meizu Meizu 21 Pro (256GB/12GB RAM)              | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Meizu Meizu 21 Pro (512GB/12GB RAM)              | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Micromax In Note 2 (64GB/4GB RAM)                | Android        | Helio G95 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Micromax Micromax In Note 2 (64GB/4GB RAM)       | Android        | Helio G95 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Edge 40 (128GB/8GB RAM)                 | Android        | Dimensity 8020 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 40 (256GB/8GB RAM)                 | Android        | Dimensity 8020 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 40 Neo (128GB/8GB RAM)             | Android        | Dimensity 7030 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 40 Neo (256GB/8GB RAM)             | Android        | Dimensity 7030 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Fusion (256GB/8GB RAM)          | Android        | Snapdragon 7s Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Fusion (512GB/8GB RAM)          | Android        | Snapdragon 7s Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Neo (256GB/8GB RAM)             | Android        | Dimensity 7300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Neo (512GB/8GB RAM)             | Android        | Dimensity 7300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Pro (128GB/8GB RAM)             | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Pro (256GB/8GB RAM)             | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Pro (512GB/8GB RAM)             | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Ultra (1024GB/12GB RAM)         | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Edge 50 Ultra (512GB/12GB RAM)          | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Moto E13 (64GB/2GB RAM)                 | Android        | Unisoc T606 (Unisoc)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Moto G 5G (2024) (128GB/4GB RAM)        | Android        | Snapdragon 4 Gen 1 (Qualcomm)                 | DSP/HVX Acceleration               |  T3 (5.50)   |
| Motorola Moto G Play (2024) (64GB/4GB RAM)       | Android        | Snapdragon 680 (Qualcomm)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Moto G Power 5G (2024) (128GB/8GB RAM)  | Android        | Dimensity 7020 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Moto G Stylus 5G (2024) (128GB/8GB RAM) | Android        | Snapdragon 6 Gen 1 (Qualcomm)                 | DSP/HVX Acceleration               |  T3 (5.50)   |
| Motorola Moto G Stylus 5G (2024) (256GB/8GB RAM) | Android        | Snapdragon 6 Gen 1 (Qualcomm)                 | DSP/HVX Acceleration               |  T3 (5.50)   |
| Motorola Moto G53 (128GB/4GB RAM)                | Android        | Snapdragon 480+ (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Motorola Moto G53 (64GB/4GB RAM)                 | Android        | Snapdragon 480+ (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Motorola Moto G54 (128GB/8GB RAM)                | Android        | Dimensity 7020 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Moto G54 (256GB/8GB RAM)                | Android        | Dimensity 7020 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Moto G73 (128GB/8GB RAM)                | Android        | Dimensity 930 (MediaTek)                      | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Moto G73 (256GB/8GB RAM)                | Android        | Dimensity 930 (MediaTek)                      | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Motorola Moto G84 (256GB/12GB RAM)               | Android        | Snapdragon 695 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Motorola Moto G85 (256GB/8GB RAM)                | Android        | Snapdragon 6s Gen 3 (Qualcomm)                | DSP/HVX Acceleration               |  T3 (5.50)   |
| Motorola Razr 40 Ultra (256GB/8GB RAM)           | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Razr 40 Ultra (512GB/8GB RAM)           | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Razr 50 (256GB/8GB RAM)                 | Android        | Dimensity 7300X (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Razr 50 (512GB/8GB RAM)                 | Android        | Dimensity 7300X (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Motorola Razr 50 Ultra (256GB/8GB RAM)           | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Motorola Razr 50 Ultra (512GB/8GB RAM)           | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nokia HMD Skyline (128GB/8GB RAM)                | Android        | Snapdragon 7s Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nokia HMD Skyline (256GB/8GB RAM)                | Android        | Snapdragon 7s Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nokia Nokia G310 (128GB/4GB RAM)                 | Android        | Snapdragon 480+ (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Nokia Nokia G42 (128GB/6GB RAM)                  | Android        | Snapdragon 480+ (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Nokia Nokia G60 (128GB/4GB RAM)                  | Android        | Snapdragon 695 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Nokia Nokia G60 (64GB/4GB RAM)                   | Android        | Snapdragon 695 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Nokia Nokia X30 (128GB/6GB RAM)                  | Android        | Snapdragon 695 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Nokia Nokia X30 (256GB/6GB RAM)                  | Android        | Snapdragon 695 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Nokia Nokia XR21 (128GB/6GB RAM)                 | Android        | Snapdragon 695 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Nothing Phone (1) (128GB/8GB RAM)                | Android        | Snapdragon 778G+ (Qualcomm)                   | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nothing Phone (1) (256GB/8GB RAM)                | Android        | Snapdragon 778G+ (Qualcomm)                   | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nothing Phone (2) (128GB/8GB RAM)                | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nothing Phone (2) (256GB/8GB RAM)                | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nothing Phone (2) (512GB/8GB RAM)                | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nothing Phone (2a) (128GB/8GB RAM)               | Android        | Dimensity 7200 Pro (MediaTek)                 | MediaTek NPU SDK                   |  T2 (8.00)   |
| Nothing Phone (2a) (256GB/8GB RAM)               | Android        | Dimensity 7200 Pro (MediaTek)                 | MediaTek NPU SDK                   |  T2 (8.00)   |
| Nubia Nubia Z60 Ultra (256GB/12GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Nubia Nubia Z60 Ultra (512GB/12GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 11 (128GB/8GB RAM)               | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 11 (256GB/8GB RAM)               | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 11R (128GB/8GB RAM)              | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 11R (256GB/8GB RAM)              | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 12 (1024GB/12GB RAM)             | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 12 (256GB/12GB RAM)              | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 12 (512GB/12GB RAM)              | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 12R (128GB/8GB RAM)              | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 12R (256GB/8GB RAM)              | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 13 (1024GB/12GB RAM)             | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 13 (256GB/12GB RAM)              | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus 13 (512GB/12GB RAM)              | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus Nord 4 (128GB/8GB RAM)           | Android        | Snapdragon 7+ Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus Nord 4 (256GB/8GB RAM)           | Android        | Snapdragon 7+ Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus Nord 4 (512GB/8GB RAM)           | Android        | Snapdragon 7+ Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| OnePlus OnePlus Open (512GB/16GB RAM)            | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Oppo A3 Pro (256GB/8GB RAM)                      | Android        | Dimensity 7050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo A3 Pro (512GB/8GB RAM)                      | Android        | Dimensity 7050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find N3 (512GB/12GB RAM)                    | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Oppo Find N3 Flip (256GB/12GB RAM)               | Android        | Dimensity 9200 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find N3 Flip (512GB/12GB RAM)               | Android        | Dimensity 9200 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X7 (1024GB/12GB RAM)                   | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X7 (256GB/12GB RAM)                    | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X7 (512GB/12GB RAM)                    | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X7 Ultra (256GB/12GB RAM)              | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Oppo Find X7 Ultra (512GB/12GB RAM)              | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 (1024GB/12GB RAM)                   | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 (256GB/12GB RAM)                    | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 (512GB/12GB RAM)                    | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 Pro (1024GB/12GB RAM)               | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 Pro (256GB/12GB RAM)                | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 Pro (512GB/12GB RAM)                | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 Ultra (1024GB/16GB RAM)             | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 Ultra (256GB/16GB RAM)              | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Oppo Find X8 Ultra (512GB/16GB RAM)              | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Oppo Oppo F27 Pro+ 5G (128GB/8GB RAM)            | Android        | Dimensity 7050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Oppo F27 Pro+ 5G (256GB/8GB RAM)            | Android        | Dimensity 7050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Reno 12 (256GB/12GB RAM)                    | Android        | Dimensity 8250 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Reno 12 (512GB/12GB RAM)                    | Android        | Dimensity 8250 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Reno 12 FS (256GB/8GB RAM)                  | Android        | Dimensity 6300 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Oppo Reno 12 FS (512GB/8GB RAM)                  | Android        | Dimensity 6300 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Oppo Reno 12 Pro (256GB/12GB RAM)                | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oppo Reno 12 Pro (512GB/12GB RAM)                | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oukitel Oukitel WP21 (256GB/12GB RAM)            | Android        | Helio G99 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Oukitel WP30 Pro (512GB/12GB RAM)                | Android        | Dimensity 8020 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Oukitel WP33 Pro (256GB/8GB RAM)                 | Android        | Dimensity 6100+ (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Poco Poco F6 (256GB/8GB RAM)                     | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Poco Poco F6 (512GB/8GB RAM)                     | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Poco Poco M6 Pro (256GB/8GB RAM)                 | Android        | Helio G99 Ultra (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Poco Poco M6 Pro (512GB/8GB RAM)                 | Android        | Helio G99 Ultra (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Poco Poco X6 Neo (128GB/8GB RAM)                 | Android        | Dimensity 6080 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Poco Poco X6 Neo (256GB/8GB RAM)                 | Android        | Dimensity 6080 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Poco Poco X6 Pro (256GB/8GB RAM)                 | Android        | Dimensity 8300 Ultra (MediaTek)               | MediaTek NPU SDK                   |  T2 (8.00)   |
| Poco Poco X6 Pro (512GB/8GB RAM)                 | Android        | Dimensity 8300 Ultra (MediaTek)               | MediaTek NPU SDK                   |  T2 (8.00)   |
| Realme GT 6 (256GB/12GB RAM)                     | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT 6 (512GB/12GB RAM)                     | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT 6T (128GB/8GB RAM)                     | Android        | Snapdragon 7+ Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT 6T (256GB/8GB RAM)                     | Android        | Snapdragon 7+ Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT 6T (512GB/8GB RAM)                     | Android        | Snapdragon 7+ Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT Neo6 (1024GB/12GB RAM)                 | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT Neo6 (256GB/12GB RAM)                  | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT Neo6 (512GB/12GB RAM)                  | Android        | Snapdragon 8s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT5 Pro (1024GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT5 Pro (256GB/12GB RAM)                  | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT5 Pro (512GB/12GB RAM)                  | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT7 Pro (1024GB/12GB RAM)                 | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT7 Pro (256GB/12GB RAM)                  | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme GT7 Pro (512GB/12GB RAM)                  | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme Narzo 70 Turbo 5G (128GB/6GB RAM)         | Android        | Dimensity 7300 Energy (MediaTek)              | MediaTek NPU SDK                   |  T2 (8.00)   |
| Realme Narzo 70 Turbo 5G (256GB/6GB RAM)         | Android        | Dimensity 7300 Energy (MediaTek)              | MediaTek NPU SDK                   |  T2 (8.00)   |
| Realme Realme 13 Pro+ (256GB/8GB RAM)            | Android        | Snapdragon 7s Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Realme Realme 13 Pro+ (512GB/8GB RAM)            | Android        | Snapdragon 7s Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 8S Pro (128GB/8GB RAM)         | Android        | Snapdragon 8+ Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 8S Pro (256GB/8GB RAM)         | Android        | Snapdragon 8+ Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 8S Pro (512GB/8GB RAM)         | Android        | Snapdragon 8+ Gen 2 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 9 Pro (256GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 9 Pro (512GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 9S Pro (256GB/12GB RAM)        | Android        | Snapdragon 8 Gen 3 Leading Version (Qualcomm) | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 9S Pro (512GB/12GB RAM)        | Android        | Snapdragon 8 Gen 3 Leading Version (Qualcomm) | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 9S Pro+ (1024GB/16GB RAM)      | Android        | Snapdragon 8 Gen 3 Leading Version (Qualcomm) | Qualcomm NPU SDK                   |  T2 (8.00)   |
| RedMagic RedMagic 9S Pro+ (512GB/16GB RAM)       | Android        | Snapdragon 8 Gen 3 Leading Version (Qualcomm) | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy A05s (128GB/4GB RAM)              | Android        | Snapdragon 680 (Qualcomm)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A05s (64GB/4GB RAM)               | Android        | Snapdragon 680 (Qualcomm)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A06 (128GB/4GB RAM)               | Android        | Helio G85 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A06 (64GB/4GB RAM)                | Android        | Helio G85 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A14 (128GB/4GB RAM)               | Android        | Exynos 1330 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A14 (64GB/4GB RAM)                | Android        | Exynos 1330 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A15 (128GB/4GB RAM)               | Android        | MediaTek Helio G99 (MediaTek)                 | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A15 (256GB/4GB RAM)               | Android        | MediaTek Helio G99 (MediaTek)                 | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A16 (128GB/4GB RAM)               | Android        | Exynos 1330 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A16 (256GB/4GB RAM)               | Android        | Exynos 1330 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A24 4G (128GB/6GB RAM)            | Android        | Helio G99 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A25 (128GB/6GB RAM)               | Android        | Exynos 1280 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A25 (256GB/6GB RAM)               | Android        | Exynos 1280 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A26 (128GB/6GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A26 (256GB/6GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A33 (128GB/6GB RAM)               | Android        | Exynos 1280 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A34 (128GB/6GB RAM)               | Android        | Dimensity 1080 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy A34 (256GB/6GB RAM)               | Android        | Dimensity 1080 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy A35 (128GB/6GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A35 (256GB/6GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A36 (128GB/6GB RAM)               | Android        | Snapdragon 6s Gen 3 (Qualcomm)                | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy A36 (256GB/6GB RAM)               | Android        | Snapdragon 6s Gen 3 (Qualcomm)                | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy A51 (128GB/4GB RAM)               | Android        | Exynos 9611 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy A52 (128GB/6GB RAM)               | Android        | Snapdragon 720G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy A52 (256GB/6GB RAM)               | Android        | Snapdragon 720G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy A52s (128GB/6GB RAM)              | Android        | Snapdragon 778G (Qualcomm)                    | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy A52s (256GB/6GB RAM)              | Android        | Snapdragon 778G (Qualcomm)                    | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy A53 (128GB/6GB RAM)               | Android        | Exynos 1280 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A53 (256GB/6GB RAM)               | Android        | Exynos 1280 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A54 (128GB/8GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A54 (256GB/8GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A55 (128GB/8GB RAM)               | Android        | Exynos 1480 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A55 (256GB/8GB RAM)               | Android        | Exynos 1480 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A56 (128GB/8GB RAM)               | Android        | Exynos 1580 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A56 (256GB/8GB RAM)               | Android        | Exynos 1580 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy A71 (128GB/6GB RAM)               | Android        | Snapdragon 730 (Qualcomm)                     | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy A72 (128GB/6GB RAM)               | Android        | Snapdragon 720G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy A72 (256GB/6GB RAM)               | Android        | Snapdragon 720G (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy F15 (128GB/4GB RAM)               | Android        | Dimensity 6100+ (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy F54 (256GB/8GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy F55 (128GB/8GB RAM)               | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy F55 (256GB/8GB RAM)               | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy M15 (128GB/4GB RAM)               | Android        | Dimensity 6100+ (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy M35 (128GB/6GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy M35 (256GB/6GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy M54 (128GB/8GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy M54 (256GB/8GB RAM)               | Android        | Exynos 1380 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy M55 (128GB/8GB RAM)               | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy M55 (256GB/8GB RAM)               | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Note 10 (256GB/8GB RAM)           | Android        | Exynos 9825 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy Note 10 Plus (256GB/12GB RAM)     | Android        | Exynos 9825 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy Note 10 Plus (512GB/12GB RAM)     | Android        | Exynos 9825 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy Note 20 (128GB/8GB RAM)           | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Note 20 (256GB/8GB RAM)           | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Note 20 Ultra (128GB/12GB RAM)    | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Note 20 Ultra (256GB/12GB RAM)    | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Note 20 Ultra (512GB/12GB RAM)    | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Note 8 (128GB/6GB RAM)            | Android        | Exynos 8895 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy Note 8 (256GB/6GB RAM)            | Android        | Exynos 8895 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy Note 8 (64GB/6GB RAM)             | Android        | Exynos 8895 (Samsung)                         | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy Note 9 (128GB/6GB RAM)            | Android        | Exynos 9810 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy Note 9 (512GB/6GB RAM)            | Android        | Exynos 9810 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy Quantum 5 (128GB/8GB RAM)         | Android        | Exynos 1480 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S10 (128GB/8GB RAM)               | Android        | Exynos 9820 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy S10 (512GB/8GB RAM)               | Android        | Exynos 9820 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy S10 Plus (1024GB/8GB RAM)         | Android        | Exynos 9820 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy S10 Plus (128GB/8GB RAM)          | Android        | Exynos 9820 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy S10 Plus (512GB/8GB RAM)          | Android        | Exynos 9820 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy S10e (128GB/6GB RAM)              | Android        | Exynos 9820 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy S10e (256GB/6GB RAM)              | Android        | Exynos 9820 (Samsung)                         | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy S20 (128GB/8GB RAM)               | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S20 FE (128GB/6GB RAM)            | Android        | Snapdragon 865 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S20 FE (256GB/6GB RAM)            | Android        | Snapdragon 865 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S20 Plus (128GB/8GB RAM)          | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S20 Plus (256GB/8GB RAM)          | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S20 Plus (512GB/8GB RAM)          | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S20 Ultra (128GB/12GB RAM)        | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S20 Ultra (256GB/12GB RAM)        | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S20 Ultra (512GB/12GB RAM)        | Android        | Exynos 990 (Samsung)                          | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 (128GB/8GB RAM)               | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 (256GB/8GB RAM)               | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 FE (128GB/6GB RAM)            | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 FE (256GB/6GB RAM)            | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 Plus (128GB/8GB RAM)          | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 Plus (256GB/8GB RAM)          | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 Ultra (128GB/12GB RAM)        | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 Ultra (256GB/12GB RAM)        | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S21 Ultra (512GB/12GB RAM)        | Android        | Exynos 2100 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S22 (128GB/8GB RAM)               | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S22 (256GB/8GB RAM)               | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S22 Plus (128GB/8GB RAM)          | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S22 Plus (256GB/8GB RAM)          | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S22 Ultra (1024GB/12GB RAM)       | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S22 Ultra (128GB/12GB RAM)        | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S22 Ultra (256GB/12GB RAM)        | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S22 Ultra (512GB/12GB RAM)        | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S23 (128GB/8GB RAM)               | Android        | Snapdragon 8 Gen 2 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S23 (256GB/8GB RAM)               | Android        | Snapdragon 8 Gen 2 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S23 FE (128GB/8GB RAM)            | Android        | Exynos 2200 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S23 FE (256GB/8GB RAM)            | Android        | Exynos 2200 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S23 Plus (256GB/8GB RAM)          | Android        | Snapdragon 8 Gen 2 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S23 Plus (512GB/8GB RAM)          | Android        | Snapdragon 8 Gen 2 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S23 Ultra (1024GB/12GB RAM)       | Android        | Snapdragon 8 Gen 2 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S23 Ultra (256GB/12GB RAM)        | Android        | Snapdragon 8 Gen 2 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S23 Ultra (512GB/12GB RAM)        | Android        | Snapdragon 8 Gen 2 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 (128GB/8GB RAM)               | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 (256GB/8GB RAM)               | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 (512GB/8GB RAM)               | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 FE (128GB/8GB RAM)            | Android        | Exynos 2400e (Samsung)                        | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S24 FE (256GB/8GB RAM)            | Android        | Exynos 2400e (Samsung)                        | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy S24 Plus (256GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 Plus (512GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 Ultra (1024GB/12GB RAM)       | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 Ultra (256GB/12GB RAM)        | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S24 Ultra (512GB/12GB RAM)        | Android        | Snapdragon 8 Gen 3 for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 (128GB/12GB RAM)              | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 (256GB/12GB RAM)              | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 (512GB/12GB RAM)              | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 Edge (256GB/12GB RAM)         | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 Edge (512GB/12GB RAM)         | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 Plus (256GB/12GB RAM)         | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 Plus (512GB/12GB RAM)         | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 Ultra (1024GB/12GB RAM)       | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 Ultra (256GB/12GB RAM)        | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy S25 Ultra (512GB/12GB RAM)        | Android        | Snapdragon 8 Elite for Galaxy (Qualcomm)      | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy XCover 7 (128GB/6GB RAM)          | Android        | Dimensity 6100+ (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Samsung Galaxy Z Flip (256GB/8GB RAM)            | Android        | Snapdragon 855+ (Qualcomm)                    | DSP/HVX Acceleration               |  T3 (5.50)   |
| Samsung Galaxy Z Flip 3 (128GB/8GB RAM)          | Android        | Snapdragon 888 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 3 (256GB/8GB RAM)          | Android        | Snapdragon 888 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 4 (128GB/8GB RAM)          | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 4 (256GB/8GB RAM)          | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 4 (512GB/8GB RAM)          | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 5 (256GB/8GB RAM)          | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 5 (512GB/8GB RAM)          | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 5G (256GB/8GB RAM)         | Android        | Snapdragon 865+ (Qualcomm)                    | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 6 (256GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 6 (512GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Flip 7 (256GB/12GB RAM)         | Android        | Exynos 2500 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Z Flip 7 (512GB/12GB RAM)         | Android        | Exynos 2500 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Z Flip 7 FE (128GB/8GB RAM)       | Android        | Exynos 2400 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Z Flip 7 FE (256GB/8GB RAM)       | Android        | Exynos 2400 (Samsung)                         | Samsung NPU SDK                    |  T2 (8.00)   |
| Samsung Galaxy Z Fold 2 (256GB/12GB RAM)         | Android        | Snapdragon 865+ (Qualcomm)                    | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 3 (256GB/12GB RAM)         | Android        | Snapdragon 888 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 3 (512GB/12GB RAM)         | Android        | Snapdragon 888 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 4 (1024GB/12GB RAM)        | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 4 (256GB/12GB RAM)         | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 4 (512GB/12GB RAM)         | Android        | Snapdragon 8+ Gen 1 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 5 (1024GB/12GB RAM)        | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 5 (256GB/12GB RAM)         | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 5 (512GB/12GB RAM)         | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 6 (1024GB/12GB RAM)        | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 6 (256GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 6 (512GB/12GB RAM)         | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 7 (1024GB/12GB RAM)        | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 7 (256GB/12GB RAM)         | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold 7 (512GB/12GB RAM)         | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Samsung Galaxy Z Fold SE (512GB/16GB RAM)        | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Sony Xperia 1 V (256GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Sony Xperia 1 V (512GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Sony Xperia 1 VI (256GB/12GB RAM)                | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Sony Xperia 1 VI (512GB/12GB RAM)                | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Sony Xperia 10 VI (128GB/8GB RAM)                | Android        | Snapdragon 6 Gen 1 (Qualcomm)                 | DSP/HVX Acceleration               |  T3 (5.50)   |
| Sony Xperia 5 V (128GB/8GB RAM)                  | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Sony Xperia 5 V (256GB/8GB RAM)                  | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Sony Xperia Pro-I (512GB/12GB RAM)               | Android        | Snapdragon 888 (Qualcomm)                     | Qualcomm NPU SDK                   |  T2 (8.00)   |
| TCL TCL 50 Pro NXTPAPER 5G (256GB/8GB RAM)       | Android        | Dimensity 6300 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| TCL TCL 50 XL (128GB/6GB RAM)                    | Android        | Dimensity 6100+ (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| TCL TCL 50 XL 5G (128GB/6GB RAM)                 | Android        | Dimensity 6100+ (MediaTek)                    | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Tecno Camon 30 Premier (512GB/12GB RAM)          | Android        | Dimensity 8200 Ultimate (MediaTek)            | MediaTek NPU SDK                   |  T2 (8.00)   |
| Tecno Camon 30 Pro (256GB/8GB RAM)               | Android        | Dimensity 8200 Ultimate (MediaTek)            | MediaTek NPU SDK                   |  T2 (8.00)   |
| Tecno Camon 30 Pro (512GB/8GB RAM)               | Android        | Dimensity 8200 Ultimate (MediaTek)            | MediaTek NPU SDK                   |  T2 (8.00)   |
| Tecno Phantom V Flip (256GB/8GB RAM)             | Android        | Dimensity 8050 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Tecno Phantom V Fold (256GB/12GB RAM)            | Android        | Dimensity 9000+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Tecno Phantom V Fold (512GB/12GB RAM)            | Android        | Dimensity 9000+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Tecno Pova 6 Pro (256GB/8GB RAM)                 | Android        | Dimensity 6080 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Ulefone Armor 25 Pro (256GB/6GB RAM)             | Android        | Dimensity 6300 (MediaTek)                     | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Ulefone Armor 26 Ultra (512GB/12GB RAM)          | Android        | Dimensity 8020 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Ulefone Ulefone Armor 24 (256GB/12GB RAM)        | Android        | Helio G96 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Vivo T3 Ultra (128GB/8GB RAM)                    | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo T3 Ultra (256GB/8GB RAM)                    | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo V40 (128GB/8GB RAM)                         | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo V40 (256GB/8GB RAM)                         | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo V40 (512GB/8GB RAM)                         | Android        | Snapdragon 7 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo V40 Pro (256GB/8GB RAM)                     | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo V40 Pro (512GB/8GB RAM)                     | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X Fold3 (1024GB/12GB RAM)                   | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X Fold3 (256GB/12GB RAM)                    | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X Fold3 (512GB/12GB RAM)                    | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X Fold3 Pro (1024GB/16GB RAM)               | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X Fold3 Pro (512GB/16GB RAM)                | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X100 (1024GB/12GB RAM)                      | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X100 (256GB/12GB RAM)                       | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X100 (512GB/12GB RAM)                       | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X100 Pro (1024GB/12GB RAM)                  | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X100 Pro (256GB/12GB RAM)                   | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X100 Pro (512GB/12GB RAM)                   | Android        | Dimensity 9300 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X100 Ultra (1024GB/12GB RAM)                | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X100 Ultra (256GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X100 Ultra (512GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo X200 (1024GB/12GB RAM)                      | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X200 (256GB/12GB RAM)                       | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X200 (512GB/12GB RAM)                       | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X200 Pro (1024GB/12GB RAM)                  | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X200 Pro (256GB/12GB RAM)                   | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo X200 Pro (512GB/12GB RAM)                   | Android        | Dimensity 9400 (MediaTek)                     | MediaTek NPU SDK                   |  T2 (8.00)   |
| Vivo iQOO 13 (1024GB/12GB RAM)                   | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo iQOO 13 (256GB/12GB RAM)                    | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Vivo iQOO 13 (512GB/12GB RAM)                    | Android        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Wiko Wiko Hi Note 10 (128GB/8GB RAM)             | Android        | Dimensity 700 (MediaTek)                      | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Wiko Wiko Hi Note 10 (256GB/8GB RAM)             | Android        | Dimensity 700 (MediaTek)                      | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Wiko Wiko T50 (128GB/6GB RAM)                    | Android        | Helio G85 (MediaTek)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Mix Flip (1024GB/12GB RAM)                | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Mix Flip (256GB/12GB RAM)                 | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Mix Flip (512GB/12GB RAM)                 | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Mix Fold 4 (1024GB/12GB RAM)              | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Mix Fold 4 (256GB/12GB RAM)               | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Mix Fold 4 (512GB/12GB RAM)               | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Redmi 14C (128GB/4GB RAM)                 | HyperOS        | Helio G81 Ultra (MediaTek)                    | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi 14C (256GB/4GB RAM)                 | HyperOS        | Helio G81 Ultra (MediaTek)                    | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi A3 (128GB/3GB RAM)                  | HyperOS        | Helio G36 (MediaTek)                          | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi A3 (64GB/3GB RAM)                   | HyperOS        | Helio G36 (MediaTek)                          | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi Note 13 4G (128GB/6GB RAM)          | HyperOS        | Snapdragon 685 (Qualcomm)                     | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi Note 13 4G (256GB/6GB RAM)          | HyperOS        | Snapdragon 685 (Qualcomm)                     | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi Note 13 Pro 4G (256GB/8GB RAM)      | HyperOS        | Helio G99 Ultra (MediaTek)                    | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi Note 13 Pro 4G (512GB/8GB RAM)      | HyperOS        | Helio G99 Ultra (MediaTek)                    | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi Note 14 5G (128GB/6GB RAM)          | HyperOS        | Dimensity 7025 Ultra (MediaTek)               | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi Note 14 5G (256GB/6GB RAM)          | HyperOS        | Dimensity 7025 Ultra (MediaTek)               | HyperOS CPU/GPU Fallback           |  T4 (3.00)   |
| Xiaomi Redmi Note 14 Pro (128GB/8GB RAM)         | HyperOS        | Dimensity 7300 Ultra (MediaTek)               | MediaTek NPU SDK                   |  T2 (8.00)   |
| Xiaomi Redmi Note 14 Pro (256GB/8GB RAM)         | HyperOS        | Dimensity 7300 Ultra (MediaTek)               | MediaTek NPU SDK                   |  T2 (8.00)   |
| Xiaomi Redmi Note 14 Pro (512GB/8GB RAM)         | HyperOS        | Dimensity 7300 Ultra (MediaTek)               | MediaTek NPU SDK                   |  T2 (8.00)   |
| Xiaomi Redmi Note 14 Pro Plus (256GB/12GB RAM)   | HyperOS        | Snapdragon 7s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Redmi Note 14 Pro Plus (512GB/12GB RAM)   | HyperOS        | Snapdragon 7s Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 (128GB/8GB RAM)                 | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 (256GB/8GB RAM)                 | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 (512GB/8GB RAM)                 | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 Pro (128GB/8GB RAM)             | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 Pro (256GB/8GB RAM)             | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 Pro (512GB/8GB RAM)             | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 Ultra (1024GB/12GB RAM)         | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 Ultra (256GB/12GB RAM)          | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13 Ultra (512GB/12GB RAM)          | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13T Pro (1024GB/12GB RAM)          | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13T Pro (256GB/12GB RAM)           | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 13T Pro (512GB/12GB RAM)           | Android        | Dimensity 9200+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 (1024GB/8GB RAM)                | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 (256GB/8GB RAM)                 | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 (512GB/8GB RAM)                 | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 Pro (1024GB/12GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 Pro (256GB/12GB RAM)            | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 Pro (512GB/12GB RAM)            | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 SE (256GB/8GB RAM)              | HyperOS        | Snapdragon 7+ Gen 3 (Qualcomm)                | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 Ultra (1024GB/12GB RAM)         | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 Ultra (256GB/12GB RAM)          | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 14 Ultra (512GB/12GB RAM)          | HyperOS        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 (1024GB/12GB RAM)               | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 (256GB/12GB RAM)                | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 (512GB/12GB RAM)                | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 Pro (1024GB/12GB RAM)           | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 Pro (256GB/12GB RAM)            | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 Pro (512GB/12GB RAM)            | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 Ultra (1024GB/16GB RAM)         | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| Xiaomi Xiaomi 15 Ultra (512GB/16GB RAM)          | HyperOS        | Snapdragon 8 Elite (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Axon 40 Ultra (256GB/8GB RAM)                | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Axon 40 Ultra (512GB/8GB RAM)                | Android        | Snapdragon 8 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Axon 60 Ultra (256GB/12GB RAM)               | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Axon 60 Ultra (512GB/12GB RAM)               | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Nubia Flip 5G (256GB/8GB RAM)                | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Nubia Flip 5G (512GB/8GB RAM)                | Android        | Snapdragon 7 Gen 1 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Nubia Music (128GB/4GB RAM)                  | Android        | Unisoc T606 (Unisoc)                          | Android CPU/GPU Fallback           |  T4 (3.00)   |
| ZTE Nubia Z60S Pro (1024GB/12GB RAM)             | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Nubia Z60S Pro (256GB/12GB RAM)              | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| ZTE Nubia Z60S Pro (512GB/12GB RAM)              | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO 12 (256GB/12GB RAM)                    | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO 12 (512GB/12GB RAM)                    | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO 12 Pro (1024GB/16GB RAM)               | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO 12 Pro (256GB/16GB RAM)                | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO 12 Pro (512GB/16GB RAM)                | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO Neo 9 (256GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO Neo 9 (512GB/12GB RAM)                 | Android        | Snapdragon 8 Gen 2 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO Neo9S Pro+ (1024GB/12GB RAM)           | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO Neo9S Pro+ (256GB/12GB RAM)            | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO Neo9S Pro+ (512GB/12GB RAM)            | Android        | Snapdragon 8 Gen 3 (Qualcomm)                 | Qualcomm NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO Z9 Turbo+ (256GB/12GB RAM)             | Android        | Dimensity 9300+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
| iQOO iQOO Z9 Turbo+ (512GB/12GB RAM)             | Android        | Dimensity 9300+ (MediaTek)                    | MediaTek NPU SDK                   |  T2 (8.00)   |
