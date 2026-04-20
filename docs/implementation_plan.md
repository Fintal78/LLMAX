# Implementation Plan - Material Scoring (Anti-Double-Counting Optimization)

Consolidate the score values within Section 1.1.A and Section 6.10.A1 independently. This update focuses on **isolating pure material properties** (Yield Strength, Rigidity, Thermal Conductivity) while strictly excluding the **Weight/Mass** factor, which is already independently scored in Section 1.5 and Section 6.10.A2.

## Proposed Changes

### Documentation (Framework & Guidelines)

#### [MODIFY] [scoring_rules.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/scoring_rules.md)
- Update numeric scores in Section 1.1.A based on **Mechanical Merit** (Yield Strength/Modulus).
- Update numeric scores in Section 6.10.A1 based on **Thermal Efficiency** (Conductivity).
- Maintain all material rows as separate items to ensure **atomic traceability**.
- Update rationales to explicitly state that "Mass/Weight" is excluded to prevent double-counting.

#### [MODIFY] [proposed_data_structure.md](file:///c:/Users/Ion/.gemini/antigravity/scratch/smartphone_db/docs/proposed_data_structure.md)
- Synchronize guideline scores with the revised "Property-Pure" logic.
- Ensure identification examples (e.g., "Glasstic") and authority rules (BOM) remain intact.

### Scoring Alignment & Justification

#### Section 1.1.A — Structural Class (Merit: Strength & Rigidity)
- **10.0**: **Titanium Alloy / Exotic Alloy** (Peak Yield Strength >800 MPa).
- **9.0**: **Stainless Steel** (Highest Young's Modulus ~200 GPa).
- **8.0**: **7000 Series Armor Aluminum** (Superior Yield Strength ~500 MPa vs 6000 series).
- **7.0**: **6000 Series Standard Aluminum** (Standard Structural Metal; yield ~240 MPa).
- **6.5**: **Magnesium Alloy** (Balanced lightweight rigidity; yield ~150 MPa).
- **6.0**: **Ceramic** (High hardness/rigidity but penalized for fracture risk/brittleness).

#### Section 6.10.A1 — Thermal Capacity (Merit: Conductivity)
*Note: Weight/Mass is already scored in Part A2. Part A1 now evaluates purely the material's transfer speed.*
- **10.0**: **6000 Series Standard Aluminum** (Highest Conductivity ~200 W/m·K).
- **9.0**: **7000 Series Armor Aluminum** (High Conductivity ~130 W/m·K).
- **7.5**: **Magnesium Alloy** (Moderate Conductivity ~70 W/m·K).
- **4.0**: **Stainless Steel / Titanium / Exotic Alloy** (Aligned: Poor Conductors <20 W/m·K).
- **3.0**: **Ceramic** (Insulator ~3 W/m·K).
- **1.0**: **Polymers (PC / TPU / Reinforced)** (Insulators ~0.2 W/m·K).

## Verification Plan

### Manual Verification
- Verify that Titanium scores high in 1.1 (Strength) but lower in 6.10 (Thermal), reflecting its objective physical properties when mass is excluded.
- Ensure every material has a unique atomic row (Traceability check).
- Check that A2 (Weight) remains unchanged as the primary mass-soak differentiator.
