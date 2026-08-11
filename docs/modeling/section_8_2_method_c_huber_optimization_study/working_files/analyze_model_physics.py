import numpy as np
from recalibrate_with_corrected_data import parse_and_correct_dataset, huber_loss
from scipy.optimize import differential_evolution

dataset = parse_and_correct_dataset()

def run_fixed_p_comparison(p_fixed=None, delta=10.0):
    if p_fixed is None:
        bounds = [(0.50, 1.00), (0.00, 15.00), (0.00, 15.00), (0.00, 10.00), (0.01, 5.00)]
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
    else:
        bounds = [(0.50, 1.00), (0.00, 15.00), (0.00, 15.00), (0.00, 10.00)]
        def obj(params):
            eta_low, c0_s, c0_d, k = params
            p = p_fixed
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
    p_val = list(res.x) + [p_fixed] if p_fixed is not None else list(res.x)
    
    device_details = []
    for d in dataset:
        c_rate = d['p_peak'] / d['battery_wh']
        c0 = p_val[2] if d['arch'] == 'dual' else p_val[1]
        diff = max(0.0, c_rate - c0)
        f_sys = min(1.0, max(0.01, p_val[0] / (1.0 + p_val[3] * (diff**p_val[4]))))
        p_eff = d['p_peak'] * f_sys
        tc = (d['battery_wh'] / p_eff) * 60.0 + 0.5
        err = tc - d['t_a']
        device_details.append((d['name'], d['p_peak'], d['battery_wh'], d['arch'], d['t_a'], tc, err))
        
    errs = np.array([x[6] for x in device_details])
    mae = np.mean(np.abs(errs))
    rmse = np.sqrt(np.mean(errs**2))
    max_err = np.max(np.abs(errs))
    
    return p_val, mae, rmse, max_err, device_details

if __name__ == "__main__":
    print(f"{'p_config':<12} | {'eta_low':<8} | {'C0_sing':<8} | {'C0_dual':<8} | {'k':<8} | {'p':<8} | {'MAE_T':<8} | {'RMSE_T':<8} | {'Max_Err':<8}")
    print("-" * 95)

    configs = [None, 0.50, 0.80, 1.00]
    all_runs = {}

    for p_cfg in configs:
        p_val, mae, rmse, max_err, details = run_fixed_p_comparison(p_cfg, delta=10.0)
        cfg_name = f"Free (p={p_val[4]:.2f})" if p_cfg is None else f"Fixed p={p_cfg:.2f}"
        print(f"{cfg_name:<12} | {p_val[0]:<8.4f} | {p_val[1]:<8.4f} | {p_val[2]:<8.4f} | {p_val[3]:<8.4f} | {p_val[4]:<8.4f} | {mae:<8.2f} | {rmse:<8.2f} | {max_err:<8.2f}")
        all_runs[cfg_name] = details
