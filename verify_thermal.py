import math

def calculate_stability(name, footprint_m2, frame_area_m2, mass_kg, p_peak, k_back, k_frame, thickness_back, thickness_frame, beta_back, sigma_pcm, p_base_heat):
    h = 10.0
    cp = 850
    t_window = 1200
    delta_t_limit = 20
    gamma = 0.33
    e_front = 1.0
    e_frame = 1.0
    e_back = 0.30
    
    # Path 1: Front (Glass k=1.1, Beta=0.25, E=1.0)
    beta_front = 0.25
    area_front = footprint_m2 * beta_front * e_front
    r_cond_front = 0.0006 / (1.1 * area_front)
    r_conv_front = 1 / (h * area_front)
    r_path_front = r_cond_front + r_conv_front
    
    # Path 2: Frame
    area_frame = frame_area_m2 * 1.0 * e_frame
    r_cond_frame = thickness_frame / (k_frame * area_frame)
    r_conv_frame = 1 / (h * area_frame)
    r_path_frame = r_cond_frame + r_conv_frame
    
    # Path 3: Back
    area_back = footprint_m2 * beta_back * e_back
    r_cond_back = thickness_back / (k_back * area_back)
    r_conv_back = 1 / (h * area_back)
    r_path_back = r_cond_back + r_conv_back
    
    # Total Resistance
    r_total = 1 / (1/r_path_front + 1/r_path_frame + 1/r_path_back)
    
    # Capacitance
    c = mass_kg * cp + (sigma_pcm * 25 if sigma_pcm else 0)
    tau = r_total * c
    
    # Z_th
    z_th = r_total * (1 - math.exp(-t_window / tau))
    
    # P_adm
    p_adm = delta_t_limit / z_th
    
    # P_adm_soc
    p_adm_soc = p_adm - p_base_heat
    
    # Ratio
    ratio = min(1.0, p_adm_soc / p_peak)
    
    # Stability
    stability = (ratio ** gamma) * 100
    
    print(f"--- {name} ---")
    print(f"R_path_front: {r_path_front:.2f}")
    print(f"R_path_frame: {r_path_frame:.2f}")
    print(f"R_path_back: {r_path_back:.2f}")
    print(f"R_total: {r_total:.2f}")
    print(f"C: {c:.2f}")
    print(f"Tau: {tau:.1f}")
    print(f"Z_th: {z_th:.2f}")
    print(f"P_adm: {p_adm:.2f}")
    print(f"P_base_heat: {p_base_heat:.2f}")
    print(f"P_adm_soc: {p_adm_soc:.2f}")
    print(f"P_peak: {p_peak:.2f}")
    print(f"Ratio: {ratio:.3f}")
    print(f"Stability: {stability:.1f}%")

# Nord 4
# Footprint: 122 cm2 = 0.0122 m2 (from study)
# Frame: 0.0038 m2 (from study)
# Area_screen: ~110 cm2? Let's use 107 cm2 from rules.
# P_base_heat = 0.40 + 0.0075 * 107 = 1.20
calculate_stability(
    name="OnePlus Nord 4",
    footprint_m2=0.0122,
    frame_area_m2=0.0038,
    mass_kg=0.1995,
    p_peak=5.7,
    k_back=200,
    k_frame=200,
    thickness_back=0.0006,
    thickness_frame=0.002,
    beta_back=0.95,
    sigma_pcm=0,
    p_base_heat=1.20
)

# S24 Ultra
# Footprint: 128 cm2 = 0.0128 m2 (from study)
# Frame: 0.00415 m2 (from study)
# Area_screen: 114 cm2
# P_base_heat = 0.40 + 0.0075 * 114 = 1.255 ≈ 1.26
calculate_stability(
    name="S24 Ultra",
    footprint_m2=0.0128,
    frame_area_m2=0.00415,
    mass_kg=0.232,
    p_peak=13.3,
    k_back=1.1,
    k_frame=17,
    thickness_back=0.0006,
    thickness_frame=0.002,
    beta_back=0.90,
    sigma_pcm=0,
    p_base_heat=1.26
)
