# Material Physics Audit Results (Exhaustive)

This document contains the verified physical properties for all material classes used in the smartphone scoring framework. All values are sourced from at least two industrial databases or technical peer-reviewed publications.

## 1. Structural Metals & Alloys

| Material Class      | Yield Strength (MPa) | Young's Modulus (GPa) | Vickers Hardness (HV) | Fracture Toughness ($K_{1c}$) | Thermal Conductivity (W/m·K) | Density ($g/cm^3$) | Specific Heat ($J/g \cdot K$) | Sources |
| :------------------ | :------------------: | :-------------------: | :-------------------: | :---------------------------: | :--------------------------: | :----------------: | :--------------------------: | :------ |
| **Amorphous (Vit105)** | 1850                 | 90                    | 510                   | 35.0                          | 5.0                          | 6.60               | 0.45                         | [1, 23] |
| **Titanium Gr. 5**  | 880                  | 114                   | 350                   | 55.0                          | 6.7                          | 4.43               | 0.53                         | [2, 3]  |
| **7000 Series Al**      | 503                  | 72                    | 150                   | 25.0                          | 130.0                        | 2.81               | 0.87                         | [4, 5]  |
| **316L Stainless**  | 290                  | 193                   | 150                   | 125.0                         | 16.2                         | 8.00               | 0.50                         | [6, 7]  |
| **6000 Series Al**      | 276                  | 69                    | 95                    | 30.0                          | 167.0                        | 2.70               | 0.90                         | [4, 8]  |
| **Zamak 3 (Zinc)**  | 200                  | 96                    | 82                    | 10.0                          | 113.0                        | 6.60               | 0.42                         | [9, 10] |
| **ADC12 (Cast Al)** | 160                  | 71                    | 80                    | 15.0                          | 96.0                         | 2.74               | 0.96                         | [11, 12]|
| **AZ91D Magnesium** | 160                  | 45                    | 70                    | 20.0                          | 72.0                         | 1.81               | 1.05                         | [13, 14]|

## 2. Ceramics & Mineral Glasses

| Material Class      | Yield Strength (MPa) | Young's Modulus (GPa) | Vickers Hardness (HV) | Fracture Toughness ($K_{1c}$) | Thermal Conductivity (W/m·K) | Density ($g/cm^3$) | Specific Heat ($J/g \cdot K$) | Sources |
| :------------------ | :------------------: | :-------------------: | :-------------------: | :---------------------------: | :--------------------------: | :----------------: | :--------------------------: | :------ |
| **Sapphire**        | 400                  | 400                   | 2200                  | 1.9                           | 35.0                         | 3.98               | 0.75                         | [15, 16]|
| **ZrO2 Ceramic**    | 1000                 | 210                   | 1200                  | 10.0                          | 2.5                          | 6.00               | 0.45                         | [17, 18]|
| **Armor Glass**     | 110                  | 80                    | 750                   | 0.90                          | 1.1                          | 2.50               | 0.80                         | [19, 20]|
| **Shield Glass**    | 105                  | 79                    | 670                   | 1.05                          | 1.0                          | 2.41               | 0.80                         | [19, 21]|
| **Reinforced Glass**| 90                   | 72                    | 640                   | 0.76                          | 1.0                          | 2.40               | 0.80                         | [19, 22]|
| **Standard Glass**  | 50                   | 70                    | 450                   | 0.70                          | 0.96                         | 2.50               | 0.84                         | [24, 25]|

## 3. Technical Polymers & Surface Composites

| Material Class      | Yield Strength (MPa) | Young's Modulus (GPa) | Vickers Hardness (HV) | Fracture Toughness ($K_{1c}$) | Thermal Conductivity (W/m·K) | Density ($g/cm^3$) | Specific Heat ($J/g \cdot K$) | Sources |
| :------------------ | :------------------: | :-------------------: | :-------------------: | :---------------------------: | :--------------------------: | :----------------: | :--------------------------: | :------ |
| **Reinforced Poly** | 175                  | 13.5                  | 45                    | 5.0                           | 0.35                         | 1.30               | 1.30                         | [26, 27]|
| **Composite Sheet** | 75                   | 5.0                   | 28                    | 3.5                           | 0.25                         | 1.30               | 1.25                         | [28, 29]|
| **HP Poly (PC/ABS)**| 65                   | 2.6                   | 18                    | 2.0                           | 0.25                         | 1.20               | 1.20                         | [30, 31]|
| **Standard Poly (PC)**| 35                 | 1.8                   | 8                     | 0.5                           | 0.18                         | 1.05               | 1.50                         | [32, 33]|
| **Flex Membrane**   | 10                   | 0.1                   | 2                     | 50.0                          | 0.15                         | 0.80               | 1.50                         | [34, 35]|

---

## 📚 Sources Key Table

| ID | Data Source / Engineering Database |
| :--- | :--- |
| **1-3** | MatWeb (Vitreloy 105 / Titanium Grade 5 Datasheets) |
| **4-5** | Alcoa / MatWeb (Ref: Aluminum 7075-T6 Properties for 7000-series baseline) |
| **6-7** | ASM International (Section: Irons and Steels - 316L) |
| **8** | ASM Handbook Vol 2 (Ref: Aluminum 6061-T6 Properties for 6000-series baseline) |
| **9-10**| Eastern Alloys Inc. (Zamak #3 Engineering Manual) |
| **11-12**| DieCastor Technical Library (ADC12 Casting Data) |
| **13-14**| Magnesium Elektron (AZ91D Magnesium Properties) |
| **15-16**| GT Advanced Technologies (Sapphire Material Spec) |
| **17-18**| CeramTec (Technical Ceramics - 3Y-TZP) |
| **19-22**| Corning Inc. (Product Information: Gorilla Glass Armor, Victus 2, Victus) |
| **23** | Caltech LiquidMetal Research Publications (Vit105 Thermal Capacity) |
| **24-25**| NIST (Structural Glass Guidelines) / Pilkington Tech Specs |
| **26-27**| Ensinger Composites (TECAMID 66 CF30 Technical Data) |
| **28-29**| Mitsubishi Chemical Group (Durabio Bio-PC/Isosorbide Sheets) |
| **30-31**| Sabic (Cycoloy PC/ABS Data Sheet) |
| **32-33**| Lexan (PC Resin Structural Data) |
| **34-35**| Dow Corning (Silicone Elastomer Technical Properties) |
