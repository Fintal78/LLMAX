# Scoring Constants

> [!IMPORTANT]
> **Naming Convention:**
> *   `_Min` = The **Mathematical Minimum** value of the range.
> *   `_Max` = The **Mathematical Maximum** value of the range.
>
> **Score Mapping:**
> *   **Higher-is-Better Metrics** (e.g., Battery Wh, PPI): Score 0 = `_Min`, Score 10 = `_Max`.
> *   **Lower-is-Better Metrics** (e.g., Price, Weight, Thickness): Score 0 = `_Max`, Score 10 = `_Min`.


**1. Design & Build**

### 1.4 Dimensions (Thickness)
*   `Thickness_mm_Min` = 6.0 (Score 10), `Thickness_mm_Max` = 10.0 (Score 0)

### 1.5 Weight
*   `Weight_g_Min` = 140 (Score 10), `Weight_g_Max` = 250 (Score 0)

### 1.6 Ergonomics (Width)
*   `Width_mm_Min` = 67.3 (Score 10), `Width_mm_Max` = 79.0 (Score 0)


**2. Display**

### 2.2 Brightness (Peak & HBM)
*   `Display_Brightness_Nits_Min` = 400 (Score 0), `Display_Brightness_Nits_Max` = 4500 (Score 10)
*   `Display_HBM_Nits_Min` = 400 (Score 0), `Display_HBM_Nits_Max` = 2500 (Score 10)

### 2.3 Color Gamut
*   `Display_P3_Coverage_Percent_Min` = 65 (Score 0), `Display_P3_Coverage_Percent_Max` = 100 (Score 10)

### 2.5 Resolution Density
*   `Display_PPI_Min` = 200 (Score 0), `Display_PPI_Max` = 600 (Score 10)

### 2.6 Motion Smoothness
*   `Display_Refresh_Rate_Hz_Min` = 45 (Score 0), `Display_Refresh_Rate_Hz_Max` = 165 (Score 10)

### 2.7 Touch Responsiveness
*   `Display_Touch_Sampling_Hz_Min` = 60 (Score 0), `Display_Touch_Sampling_Hz_Max` = 960 (Score 10)

### 2.8 Screen-to-Body Ratio
*   `Display_SBR_Percent_Min` = 60 (Score 0), `Display_SBR_Percent_Max` = 93 (Score 10)

### 2.9 Screen Size
*   `Display_Size_Inch_Min` = 4.5 (Score 0), `Display_Size_Inch_Max` = 7.6 (Score 10)

### 2.10 Eye Comfort
*   `Display_PWM_Hz_Min` = 120 (Score 0), `Display_PWM_Hz_Max` = 3840 (Score 10)

### 2.11 Display Benchmark
*   `Display_DXO_Score_Min` = 60 (Score 0), `Display_DXO_Score_Max` = 160 (Score 10)


**4. Camera Systems**

### 4.1 Main Sensor Size
*   `Camera_Main_Sensor_Inch_Min` = 0.25 (Score 0), `Camera_Main_Sensor_Inch_Max` = 1.0 (Score 10)

### 4.2 Main Camera Aperture
*   `Camera_Main_Aperture_f_Min` = 1.4 (Score 10), `Camera_Main_Aperture_f_Max` = 2.4 (Score 0)

### 4.3 Main Camera Resolution
*   `Camera_Main_Resolution_MP_Min` = 12 (Score 0), `Camera_Main_Resolution_MP_Max` = 200 (Score 10)

### 4.5 Ultrawide Camera
*   `Camera_Ultrawide_FOV_Deg_Min` = 100 (Score 0), `Camera_Ultrawide_FOV_Deg_Max` = 130 (Score 10)
*   `Camera_Ultrawide_Sensor_Inch_Min` = 0.25 (Score 0), `Camera_Ultrawide_Sensor_Inch_Max` = 0.5 (Score 10)

### 4.6 Zoom Capability
*   `Camera_Zoom_Optical_x_Min` = 1 (Score 0), `Camera_Zoom_Optical_x_Max` = 10 (Score 10)

### 4.7 Macro Capability
*   `Camera_Macro_Dist_cm_Min` = 1.5 (Score 10), `Camera_Macro_Dist_cm_Max` = 10 (Score 0)

### 4.9 Rear Video Frame Rate
*   `Camera_Video_FPS_Min` = 5 (Score 0), `Camera_Video_FPS_Max` = 120 (Score 10)

### 4.12 High Frame Rate (Slow Motion)
*   `Camera_SlowMo_MPs_Min` = 32 (Score 0), `Camera_SlowMo_MPs_Max` = 1000 (Score 10)

### 4.13 Front Camera Sensor Resolution
*   `Camera_Front_Resolution_MP_Min` = 5 (Score 0), `Camera_Front_Resolution_MP_Max` = 32 (Score 10)

### 4.15 Front Camera Video Performance
*   `Camera_Front_Video_Res_Width_Min` = 1280 (Score 0), `Camera_Front_Video_Res_Width_Max` = 3840 (Score 10)
*   `Camera_Front_Video_FPS_Min` = 24 (Score 0), `Camera_Front_Video_FPS_Max` = 60 (Score 10)


**5. Software & Longevity**

### 5.1 Support Longevity
*   `Support_Years_Min` = 1 (Score 0), `Support_Years_Max` = 7 (Score 10)


**6. Processing Power**

### 6.1 CPU Multi-Core
*   `CPU_GB6_Multi_Score_Min` = 1500 (Score 0), `CPU_GB6_Multi_Score_Max` = 7500 (Score 10)
*   `CPU_PTS_Score_Min` = 5 (Score 0), `CPU_PTS_Score_Max` = 140 (Score 10)

### 6.2 CPU Architecture & Single-Core Efficiency
*   `CPU_GB6_Single_Score_Min` = 400 (Score 0), `CPU_GB6_Single_Score_Max` = 3000 (Score 10)
*   `CPU_STRS_Score_Min` = 5 (Score 0), `CPU_STRS_Score_Max` = 12 (Score 10)

### 6.3 GPU Performance
*   `GPU_SteelNomad_Score_Min` = 500 (Score 0), `GPU_SteelNomad_Score_Max` = 1800 (Score 10)
*   `GPU_RC_Score_Min` = 0.5 (Score 0), `GPU_RC_Score_Max` = 12.5 (Score 10)

### 6.4 AI Hardware
*   `AI_GB_Quant_Score_Min` = 500 (Score 0), `AI_GB_Quant_Score_Max` = 4500 (Score 10)

### 6.6 RAM Capacity
*   `RAM_GB_Min` = 2 (Score 0), `RAM_GB_Max` = 24 (Score 10)

### 6.8 Storage Capacity
*   `Storage_GB_Min` = 16 (Score 0), `Storage_GB_Max` = 1024 (Score 10)

### 6.10 Thermal Dissipation & Stability Index (TDSI)
*   `SoC_Process_Node_nm_Min` = 3 (Score 10 for Node component), `SoC_Process_Node_nm_Max` = 20 (Score 0 for Node component)
*   `Thermal_Weight_g_Min` = 140 (Score 0), `Thermal_Weight_g_Max` = 250 (Score 10) (*Heavier is better for thermal mass*)
*   `Thermal_Surface_Area_mm2_Min` = 6000 (Score 0), `Thermal_Surface_Area_mm2_Max` = 9000 (Score 10)
*   `Thermal_Thickness_mm_Min` = 6.0 (Score 0), `Thermal_Thickness_mm_Max` = 10.0 (Score 10) (*Thicker is better for thermal mass*)


**7. Connectivity & Sensors**

### 7.4 Bluetooth & Audio Codecs
*   `Audio_Bitrate_kbps_Max` = 1200 (Score 10)


**8. Battery & Charging**

### 8.1 Battery Endurance (Model)
*   `Battery_Energy_Wh_Min` = 8 (Score 0), `Battery_Energy_Wh_Max` = 25 (Score 10)
*   `Battery_Refresh_Effective_Hz_Min` = 30 (Score 10), `Battery_Refresh_Effective_Hz_Max` = 165 (Score 0) (*Lower is better for efficiency*)
*   `Battery_Resolution_MP_Min` = 1.0 (Score 10), `Battery_Resolution_MP_Max` = 8.3 (Score 0) (*Lower is better for efficiency*)
*   `Battery_GSMArena_Hours_Min` = 7.8 (Score 0), `Battery_GSMArena_Hours_Max` = 23.12 (Score 10)
*   `Battery_PhoneArena_Hours_Min` = 3.6 (Score 0), `Battery_PhoneArena_Hours_Max` = 11.42 (Score 10)
*   `Battery_DXO_Score_Min` = 50 (Score 0), `Battery_DXO_Score_Max` = 160 (Score 10)

### 8.2 Wired Charging
*   `Battery_Wired_Charging_W_Min` = 5 (Score 0), `Battery_Wired_Charging_W_Max` = 120 (Score 10)

### 8.3 Wireless Charging
*   `Battery_Wireless_Charging_W_Min` = 7.5 (Score 0), `Battery_Wireless_Charging_W_Max` = 50 (Score 10)

### 8.4 Wired Reverse Charging
*   `Battery_Reverse_Wired_W_Max` = 10 (Score 10)

### 8.5 Wireless Reverse Charging
*   `Battery_Reverse_Wireless_W_Max` = 10 (Score 10)


**9. Financial & Value**

### 9.1 Price
*   `Price_USD_Min` = 100 (Score 10), `Price_USD_Max` = 1600 (Score 0)
