
# Scoring Constants & Parameters

## 1. Design & Ergonomics
*   `Weight_Heaviest_Phone` = 250 (grams)
*   `Weight_Lightest_Phone` = 140 (grams)
*   `Thickness_Max_Penalty` = 7.0 (mm)
*   `Thickness_Min_Penalty` = 10.0 (mm)

## 2. Display
*   (No constants currently defined, uses direct formulas)

## 3. Performance (SoC & Memory)
*   `GB6_Multi_Best_Phone` = 7500  (Snapdragon 8 Gen 3 / A17 Pro baseline)
*   `GB6_Multi_Worst_Phone` = 1500 (Entry level)
*   `PTS_Best_Phone` = 140 (Best multi-thread: Sum(FACS) at maximum)
*   `PTS_Worst_Phone` = 5 (Worst multi-thread: Sum(FACS) at minimum)
*   `STRS_Best_Phone` = 12 (Best single-thread: FACS of Prime Core [10 × 1.2])
*   `STRS_Worst_Phone` = 5 (Worst single-thread: FACS of Cortex-A76 [5 × 1.0])
*   `RC_Best_Phone` = 12.5 (Best GPU: GAS × FSF × AFM at maximum)
*   `RC_Worst_Phone` = 0.5 (Worst GPU: GAS × FSF × AFM at minimum)
*   `Process_Node_Best_nm` = 3 (Latest TSMC)
*   `Process_Node_Worst_nm` = 20 (Legacy)
*   `RAM_Max_GB` = 24
*   `RAM_Min_GB` = 2
*   `Storage_Max_GB` = 1024
*   `Storage_Min_GB` = 16
*   `AI_GB_Quant_Max` = 4500 (Snapdragon 8 Gen 3 / A17 Pro)
*   `AI_GB_Quant_Min` = 500  (Legacy/Entry)
*   `GPU_SteelNomad_Max` = 1800 (Snapdragon 8 Gen 3)
*   `GPU_SteelNomad_Min` = 500 (Mainstream)

## 2. Display
*   `DXO_Display_Max` = 160
*   `DXO_Display_Min` = 60

## 4. Camera Systems
*   `Main_Sensor_Max_Inch` = 1.0
*   `Main_Sensor_Min_Inch` = 0.25
*   `Main_Pixel_Max_MP` = 200
*   `Main_Pixel_Min_MP` = 12
*   `Aperture_Max_Score_f` = 1.4
*   `Aperture_Min_Score_f` = 2.4
*   `Zoom_Max_Optical_x` = 10
*   `Zoom_Min_Optical_x` = 1
*   `Ultrawide_FOV_Max_Deg` = 130
*   `Ultrawide_FOV_Min_Deg` = 100
*   `Macro_Min_Dist_cm` = 2
*   `Macro_Max_Dist_cm` = 10
*   `Macro_Dedicated_Max_MP` = 5
*   `Macro_Dedicated_Min_MP` = 0
*   `Video_FPS_Max_Score` = 120
*   `Video_FPS_Min_Score` = 5
*   `SlowMo_MPs_Max_Score` = 1000 (4K @ 120fps)
*   `SlowMo_MPs_Min_Score` = 32 (~720p @ 30fps)
*   `Front_Cam_Max_MP` = 32
*   `Front_Cam_Min_MP` = 5
*   `Front_Video_Max_Res_Px` = 3840 (4K)
*   `Front_Video_Min_Res_Px` = 1280 (720p)
*   `Front_Video_Max_FPS` = 60
*   `Front_Video_Min_FPS` = 24

## 5. Battery & Charging
*   `Wired_Charging_Max_W` = 120
*   `Wired_Charging_Min_W` = 5
*   `Wireless_Charging_Max_W` = 50
*   `Wireless_Charging_Min_W` = 7.5
*   `Reverse_Wireless_Max_W` = 10
*   `Reverse_Wireless_Min_W` = 4.5
*   `Reverse_Wired_Max_W` = 10
*   `Reverse_Wired_Min_W` = 4.5
*   `DXO_Battery_Max` = 160
*   `DXO_Battery_Min` = 50

## 6. Software & Support
*   `Support_Years_Max` = 7
*   `Support_Years_Min` = 1

## 7. Connectivity & Audio
*   `Bitrate_kbps_Best_Device` = 1200 (Baseline: aptX Lossless)

## 9. Financial & Value
*   `Price_Anchor_Best_USD` = 100
*   `Price_Anchor_Worst_USD` = 1600
