
# Scoring Constants & Parameters

## 1. Design & Ergonomics
*   `Weight_Heaviest_Phone` = 250 (grams)
*   `Weight_Lightest_Phone` = 140 (grams)
*   `Thickness_Max_Penalty` = 6.0 (mm)
*   `Thickness_Min_Penalty` = 10.0 (mm)
*   `Bezel_Max_Penalty` = 4.0 (mm)
*   `Bezel_Min_Penalty` = 1.0 (mm)
*   `Screen_Size_Max_Score` = 6.8 (inches)
*   `Screen_Size_Min_Score` = 5.5 (inches)

## 2. Display
*   (No constants currently defined, uses direct formulas)

## 3. Performance (SoC & Memory)
*   `GB6_Multi_Best_Phone` = 7500  (Snapdragon 8 Gen 3 / A17 Pro baseline)
*   `GB6_Multi_Worst_Phone` = 1500 (Entry level)
*   `Max_Freq_GHz_Best_Phone` = 3.8 (High performance core)
*   `Max_Freq_GHz_Worst_Phone` = 1.8 (Efficiency core only)
*   `PTS_Best_Phone` = 900 (Best multi-thread: CPS × AES × FSF at maximum)
*   `PTS_Worst_Phone` = 18 (Worst multi-thread: CPS × AES × FSF at minimum)
*   `STRS_Best_Phone` = 20 (Best single-thread: CAS × FSF of 10 × 2.0)
*   `STRS_Worst_Phone` = 9 (Worst single-thread: CAS × FSF of 9 × 1.0)
*   `Process_Node_Best_nm` = 3 (Latest TSMC)
*   `Process_Node_Worst_nm` = 20 (Legacy)
*   `RAM_Max_GB` = 24
*   `RAM_Min_GB` = 2
*   `Storage_Max_GB` = 1024
*   `Storage_Min_GB` = 16

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

## 6. Software & Support
*   `Support_Years_Max` = 7
*   `Support_Years_Min` = 1

## 7. Connectivity & Audio
*   `Bitrate_kbps_Best_Device` = 1200 (Baseline: aptX Lossless)

## 9. Financial & Value
*   `Price_Anchor_Best_USD` = 100
*   `Price_Anchor_Worst_USD` = 1600
