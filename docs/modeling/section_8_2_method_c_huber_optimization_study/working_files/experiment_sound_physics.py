import numpy as np
from recalibrate_with_corrected_data import parse_and_correct_dataset, huber_loss
from scipy.optimize import differential_evolution

dataset_all = parse_and_correct_dataset()
dataset_android = [d for d in dataset_all if not d['name'].startswith('Apple') and d['name'] != 'LG G7 ThinQ']

print(f"Full Dataset: {len(dataset_all)} devices | Android/Standard Dataset: {len(dataset_android)} devices")

def fit_model(dataset, delta=5.0, min_p=0.40):
    bounds = [
        (0.70, 1.00),   # eta_low
        (0.00, 15.00),  # c0_single
        (0.00, 15.00),  # c0_dual
        (0.00, 10.00),  # k
        (min_p, 3.00)   # p constrained to physical realism
    ]
    
    def obj(params):
        eta_low, c0_s, c0_d, k, p = params
        errs = []
        for d in dataset:
            c_rate = d['p_peak'] / d['battery_wh']
            c0 = c0_d if d['arch'] == 'dual' else c0_s
            diff = max(0.0, c_rate - c0)
            f_sys = min(1.0, max(0.01, eta_low / (1.0 + k * (diff**p))))
            p_eff = d['p_peak'] * f_sys
            tc = (d['battery_wh'] / p_eff) * 60.0 + 0.5
            errs.append(tc - d['t_a'])
        return np.mean(huber_loss(np.array(errs), delta))

    res = differential_evolution(obj, bounds, maxiter=4000, popsize=40, seed=42)
    p_val = res.x
    
    # Calculate metrics
    errs = []
    for d in dataset:
        c_rate = d['p_peak'] / d['battery_wh']
        c0 = p_val[2] if d['arch'] == 'dual' else p_val[1]
        diff = max(0.0, c_rate - c0)
        f_sys = min(1.0, max(0.01, p_val[0] / (1.0 + p_val[3] * (diff**p_val[4]))))
        p_eff = d['p_peak'] * f_sys
        tc = (d['battery_wh'] / p_eff) * 60.0 + 0.5
        errs.append(tc - d['t_a'])
        
    errs = np.array(errs)
    mae = np.mean(np.abs(errs))
    rmse = np.sqrt(np.mean(errs**2))
    max_err = np.max(np.abs(errs))
    
    return p_val, mae, rmse, max_err

if __name__ == "__main__":
    print("\n--- EXPERIMENT 1: Full 44-Device Dataset with Physically Sound Exponent (p >= 0.40) ---")
    p_all, mae_all, rmse_all, max_err_all = fit_model(dataset_all, delta=5.0, min_p=0.40)
    print(f"eta_low={p_all[0]:.4f} | C0_single={p_all[1]:.4f} | C0_dual={p_all[2]:.4f} | k={p_all[3]:.4f} | p={p_all[4]:.4f}")
    print(f"MAE_T: {mae_all:.2f} mins | RMSE_T: {rmse_all:.2f} mins | Max_Err: {max_err_all:.2f} mins")

    print("\n--- EXPERIMENT 2: Pure Standard/Android Sub-Dataset (34 devices, p >= 0.40) ---")
    p_and, mae_and, rmse_and, max_err_and = fit_model(dataset_android, delta=5.0, min_p=0.40)
    print(f"eta_low={p_and[0]:.4f} | C0_single={p_and[1]:.4f} | C0_dual={p_and[2]:.4f} | k={p_and[3]:.4f} | p={p_and[4]:.4f}")
    print(f"MAE_T: {mae_and:.2f} mins | RMSE_T: {rmse_and:.2f} mins | Max_Err: {max_err_and:.2f} mins")
