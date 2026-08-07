import json
import math

BENCHMARK_DEVICES = [
    (19.25, 240.0, 'single', 'charge_pump',  9.6, 10.00, "Realme GT3", "https://www.gsmarena.com/realme_gt3-review-2537p3.php"),
    (16.50, 210.0, 'single', 'charge_pump',  9.0, 10.00, "Redmi Note 12 Explorer", "https://www.gsmarena.com/redmi_note_12_explorer-review-2501p3.php"),
    (18.15, 200.0, 'dual',   'charge_pump', 12.0,  9.12, "iQOO 11 Pro", "https://www.gsmarena.com/iqoo_11_pro-review-2515p3.php"),
    (17.32, 125.0, 'single', 'charge_pump', 18.0,  7.89, "Motorola Edge 50 Pro", "https://www.gsmarena.com/motorola_edge_50_pro-review-2688p3.php"),
    (18.55, 120.0, 'single', 'charge_pump', 19.0,  7.73, "Xiaomi 13 Pro", "https://www.gsmarena.com/xiaomi_13_pro-review-2527p3.php"),
    (19.25, 120.0, 'single', 'charge_pump', 19.0,  7.73, "Xiaomi 12T Pro", "https://www.gsmarena.com/xiaomi_12t_pro-review-2486p3.php"),
    (18.10, 120.0, 'dual',   'charge_pump', 17.0,  8.07, "Poco F4 GT", "https://www.gsmarena.com/poco_f4_gt-review-2419p3.php"),
    (20.80, 100.0, 'single', 'pps',         31.0,  6.24, "Vivo X100 Pro", "https://www.gsmarena.com/vivo_x100_pro-review-2646p3.php"),
    (20.80, 100.0, 'single', 'pps',         26.0,  6.77, "OnePlus 12", "https://www.gsmarena.com/oneplus_12-review-2658p3.php"),
    (19.25, 100.0, 'dual',   'pps',         25.0,  6.89, "OnePlus 11", "https://www.gsmarena.com/oneplus_11-review-2524p3.php"),
    (17.75,  90.0, 'single', 'pps',         35.0,  5.87, "Xiaomi 14", "https://www.gsmarena.com/xiaomi_14-review-2675p3.php"),
    (21.56,  80.0, 'single', 'pps',         36.0,  5.78, "Honor Magic 6 Pro", "https://www.gsmarena.com/honor_magic6_pro-review-2673p3.php"),
    (21.17,  80.0, 'dual',   'pps',         32.0,  6.14, "OnePlus 12R", "https://www.gsmarena.com/oneplus_12r-review-2662p3.php"),
    (17.32,  68.0, 'single', 'fixed_pd',    44.0,  5.17, "Motorola Edge 40", "https://www.gsmarena.com/motorola_edge_40-review-2565p3.php"),
    (17.32,  67.0, 'single', 'fixed_pd',    42.0,  5.31, "Xiaomi 13", "https://www.gsmarena.com/xiaomi_13-review-2525p3.php"),
    (19.63,  66.0, 'single', 'fixed_pd',    48.0,  4.91, "Honor Magic 5 Pro", "https://www.gsmarena.com/honor_magic5_pro-review-2548p3.php"),
    (23.10,  65.0, 'dual',   'fixed_pd',    42.0,  5.31, "Asus ROG Phone 7", "https://www.gsmarena.com/asus_rog_phone_7-review-2550p3.php"),
    (19.25,  45.0, 'single', 'pps',         59.0,  4.28, "Samsung Galaxy S24 Ultra", "https://www.gsmarena.com/samsung_galaxy_s24_ultra-review-2659p3.php"),
    (19.25,  45.0, 'single', 'pps',         59.0,  4.28, "Samsung Galaxy S23 Ultra", "https://www.gsmarena.com/samsung_galaxy_s23_ultra-review-2526p3.php"),
    (19.25,  45.0, 'single', 'pps',         59.0,  4.28, "Samsung Galaxy S22 Ultra", "https://www.gsmarena.com/samsung_galaxy_s22_ultra-review-2382p3.php"),
    (18.10,  45.0, 'single', 'pps',         55.0,  4.49, "Nothing Phone (2)", "https://www.gsmarena.com/nothing_phone_(2)-review-2586p3.php"),
    (19.25,  45.0, 'single', 'fixed_pd',    65.0,  4.01, "Samsung Galaxy A55", "https://www.gsmarena.com/samsung_galaxy_a55-review-2680p3.php"),
    (19.25,  45.0, 'single', 'fixed_pd',    63.0,  4.10, "Samsung Galaxy A54", "https://www.gsmarena.com/samsung_galaxy_a54-review-2544p3.php"),
    (18.86,  45.0, 'single', 'pps',         56.0,  4.44, "Google Pixel 8 Pro", "https://www.gsmarena.com/google_pixel_8_pro-review-2628p3.php"),
    (19.25,  45.0, 'single', 'pps',         79.0,  3.43, "Google Pixel 9 Pro XL", "https://www.gsmarena.com/google_pixel_9_pro_xl-review-2736p3.php"),
    (18.10,  33.0, 'single', 'fixed_pd',    70.0,  3.78, "Poco X6", "https://www.gsmarena.com/poco_x6-review-2654p3.php"),
    (19.25,  33.0, 'single', 'fixed_pd',    75.0,  3.57, "Poco M6 Pro", "https://www.gsmarena.com/poco_m6_pro-review-2656p3.php"),
    (15.40,  27.0, 'single', 'apple_legacy', 75.0, 3.57, "Apple iPhone 15 Pro Max", "https://www.gsmarena.com/apple_iphone_15_pro_max-review-2618p3.php"),
    (16.94,  27.0, 'single', 'apple_legacy', 109.0, 2.39, "Apple iPhone 15 Plus", "https://www.gsmarena.com/apple_iphone_15_plus-review-2622p3.php"),
    (15.40,  27.0, 'single', 'apple_legacy', 93.0,  2.88, "Apple iPhone 14 Pro Max", "https://www.gsmarena.com/apple_iphone_14_pro_max-review-2483p3.php"),
    (15.40,  27.0, 'single', 'apple_legacy', 86.0,  3.14, "Apple iPhone 13 Pro Max", "https://www.gsmarena.com/apple_iphone_13_pro_max-review-2319p3.php"),
    (19.25,  25.0, 'single', 'fixed_pd',    82.0,  3.29, "Samsung Galaxy A35", "https://www.gsmarena.com/samsung_galaxy_a35-review-2682p3.php"),
    (19.25,  25.0, 'single', 'fixed_pd',    84.0,  3.21, "Samsung Galaxy A34", "https://www.gsmarena.com/samsung_galaxy_a34-review-2545p3.php"),
    (19.25,  25.0, 'single', 'fixed_pd',    85.0,  3.18, "Samsung Galaxy A25", "https://www.gsmarena.com/samsung_galaxy_a25-review-2650p3.php"),
    (19.25,  25.0, 'single', 'fixed_pd',    86.0,  3.14, "Samsung Galaxy A15 5G", "https://www.gsmarena.com/samsung_galaxy_a15_5g-review-2652p3.php"),
    (15.40,  25.0, 'single', 'pps',         75.0,  3.57, "Samsung Galaxy S24", "https://www.gsmarena.com/samsung_galaxy_s24-review-2661p3.php"),
    (15.01,  25.0, 'single', 'pps',         74.0,  3.61, "Samsung Galaxy S23", "https://www.gsmarena.com/samsung_galaxy_s23-review-2523p3.php"),
    (17.60,  27.0, 'single', 'pps',         77.0,  3.50, "Google Pixel 8", "https://www.gsmarena.com/google_pixel_8-review-2624p3.php"),
    (16.98,  18.0, 'single', 'fixed_pd',   100.0,  2.66, "Google Pixel 7a", "https://www.gsmarena.com/google_pixel_7a-review-2566p3.php"),
    (17.32,  18.0, 'single', 'fixed_pd',   110.0,  2.36, "Google Pixel 6a", "https://www.gsmarena.com/google_pixel_6a-review-2442p3.php"),
    (19.25,  15.0, 'single', 'legacy_5v',  130.0,  1.85, "Samsung Galaxy A05s", "https://www.gsmarena.com/samsung_galaxy_a05s-review-2630p3.php"),
    (19.25,  10.0, 'single', 'legacy_5v',  160.0,  1.21, "Samsung Galaxy A04", "https://www.gsmarena.com/samsung_galaxy_a04-review-2475p3.php"),
    (17.32,  10.0, 'single', 'legacy_5v',  155.0,  1.30, "Poco C65", "https://www.gsmarena.com/poco_c65-review-2640p3.php"),
    (17.32,   5.0, 'single', 'legacy_5v',  240.0,  0.02, "Nokia 2.4", "https://www.gsmarena.com/nokia_2_4-review-2180p3.php"),
    (19.25,  23.0, 'single', 'fixed_pd',   109.0,  2.41, "Google Pixel 7 Pro", "https://www.gsmarena.com/google_pixel_7_pro-review-2484p3.php"),
    (15.26,  18.0, 'single', 'apple_legacy', 120.0, 2.12, "Apple iPhone 11 Pro Max", "https://www.gsmarena.com/apple_iphone_11_pro_max-review-1991p3.php"),
    (11.55,  18.0, 'single', 'fixed_pd',   108.0,  2.44, "LG G7 ThinQ", "https://www.gsmarena.com/lg_g7_thinq-review-1763p3.php"),
    (12.08,  15.0, 'single', 'apple_legacy', 131.0, 1.85, "Apple iPhone XS Max", "https://www.gsmarena.com/apple_iphone_xs_max-review-1823p3.php"),
    (10.43,  15.0, 'single', 'apple_legacy', 125.0, 2.00, "Apple iPhone X", "https://www.gsmarena.com/apple_iphone_x-review-1681p3.php"),
    (13.09,  15.0, 'single', 'fixed_pd',   108.0,  2.44, "Samsung Galaxy S10", "https://www.gsmarena.com/samsung_galaxy_s10-review-1902p3.php"),
    (11.55,  15.0, 'single', 'legacy_5v',  107.0,  2.47, "Samsung Galaxy S9", "https://www.gsmarena.com/samsung_galaxy_s9-review-1734p3.php"),
    (11.55,  15.0, 'single', 'legacy_5v',  100.0,  2.68, "Samsung Galaxy S8", "https://www.gsmarena.com/samsung_galaxy_s8-review-1603p3.php"),
    (6.96,    5.0, 'single', 'apple_legacy', 148.0, 1.48, "Apple iPhone 8", "https://www.gsmarena.com/apple_iphone_8-review-1667p3.php"),
    (11.10,   5.0, 'single', 'apple_legacy', 241.0, 0.00, "Apple iPhone 7 Plus", "https://www.gsmarena.com/apple_iphone_7_plus-review-1502p3.php"),
    (19.25,   7.7, 'single', 'legacy_5v',  205.0,  0.49, "Samsung Galaxy A03 Core", "https://www.gsmarena.com/samsung_galaxy_a03_core-review-2371p3.php")
]

PARAM_KEYS = [
    "C_threshold", "k", "p", "eta_base", "s_low", "T_handshake",
    "F_charge_pump", "F_pps", "F_fixed_pd", "F_legacy_5v", "F_apple", "F_arch"
]

# REALISTIC PHYSICALLY SOUND SEARCH DOMAINS
PARAM_BOUNDS = [
    (0.50, 3.50),   # C_threshold
    (0.001, 1.00),  # k
    (0.05, 1.50),   # p
    (0.20, 0.85),   # eta_base
    (0.05, 1.00),   # s_low
    (0.00, 15.00),  # T_handshake (0 to 15 mins)
    (0.95, 1.65),   # F_charge_pump (up to 1.65)
    (0.90, 1.40),   # F_pps
    (0.80, 1.25),   # F_fixed_pd
    (0.65, 1.35),   # F_legacy_5v
    (0.65, 1.35),   # F_apple
    (0.95, 1.65),   # F_arch
]

BASELINE_PARAMS = [1.5000, 0.1200, 0.3000, 0.4500, 0.3200, 0.5000, 1.1000, 1.0500, 0.9500, 0.8500, 0.8800, 1.2500]

def predict_duration(wh, max_power_w, arch_type, protocol_type, params):
    (C_thresh, k, p, eta_base, s_low, T_handshake,
     F_cp, F_pps, F_fpd, F_5v, F_app, F_arch) = params
    
    proto_map = {
        'charge_pump': F_cp,
        'pps': F_pps,
        'fixed_pd': F_fpd,
        'legacy_5v': F_5v,
        'apple_legacy': F_app
    }
    F_proto = proto_map.get(protocol_type, 1.0)
    F_a = F_arch if arch_type == 'dual' else 1.0
    
    c_rate = max_power_w / max(1.0, wh)
    
    eff = eta_base * F_proto * F_a
    if c_rate > C_thresh:
        eff -= k * math.pow(c_rate - C_thresh, p)
    eff = max(0.15, min(0.95, eff))
    
    eff_power_w = max_power_w * eff
    T_cc_cv_mins = (wh / max(1.0, eff_power_w)) * 60.0
    T_predicted_mins = T_cc_cv_mins + T_handshake
    return T_predicted_mins

def predict_all_durations(params):
    return [predict_duration(d[0], d[1], d[2], d[3], params) for d in BENCHMARK_DEVICES]

def compute_loss(loss_type, params, delta=10.0):
    T_C = predict_all_durations(params)
    total_loss = 0.0
    N = len(BENCHMARK_DEVICES)
    for i, d in enumerate(BENCHMARK_DEVICES):
        err = d[4] - T_C[i]
        abs_err = abs(err)
        if loss_type == "mse":
            total_loss += err * err
        elif loss_type == "mae":
            total_loss += abs_err
        elif loss_type == "huber":
            if abs_err <= delta:
                total_loss += 0.5 * abs_err * abs_err
            else:
                total_loss += delta * abs_err - 0.5 * delta * delta
    return total_loss / N

def fine_coordinate_descent(loss_type, initial_params, delta=10.0, max_outer_iter=800):
    params = list(initial_params)
    n_params = len(params)
    step_size = 0.04
    min_step = 1e-6
    current_loss = compute_loss(loss_type, params, delta)
    for iteration in range(max_outer_iter):
        improved = False
        for j in range(n_params):
            low, high = PARAM_BOUNDS[j]
            best_val = params[j]
            best_param_loss = current_loss
            for mult in [1.0, 0.5, 0.25]:
                effective_step = step_size * mult
                for direction in [+1.0, -1.0]:
                    candidate_val = params[j] + direction * effective_step
                    candidate_val = max(low, min(high, candidate_val))
                    params[j] = candidate_val
                    cand_loss = compute_loss(loss_type, params, delta)
                    if cand_loss < best_param_loss - 1e-7:
                        best_param_loss = cand_loss
                        best_val = candidate_val
                        improved = True
            params[j] = best_val
            current_loss = best_param_loss
        if not improved:
            step_size *= 0.5
            if step_size < min_step:
                break
    return params, current_loss

def main():
    p_huber10, l_huber10 = fine_coordinate_descent("huber", BASELINE_PARAMS, delta=10.0)
    p_mse, l_mse = fine_coordinate_descent("mse", BASELINE_PARAMS)
    p_mae, l_mae = fine_coordinate_descent("mae", BASELINE_PARAMS)
    
    print("\n--- UNCONSTRAINED OPTIMAL PARAMETER ESTIMATES ---")
    print(f"{'Parameter':<25} | {'Baseline':<8} | {'Pure MSE':<8} | {'Pure MAE':<8} | {'Huber 10':<8} | {'Domain Bounds':<16}")
    print("-" * 95)
    for i, name in enumerate(PARAM_KEYS):
        print(f"{name:<25} | {BASELINE_PARAMS[i]:<8.4f} | {p_mse[i]:<8.4f} | {p_mae[i]:<8.4f} | {p_huber10[i]:<8.4f} | {str(PARAM_BOUNDS[i]):<16}")

if __name__ == "__main__":
    main()
