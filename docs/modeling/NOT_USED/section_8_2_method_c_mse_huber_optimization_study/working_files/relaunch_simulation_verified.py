import sys
import os
import math
import time
import json
import numpy as np
from scipy.optimize import differential_evolution, minimize

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from benchmark_devices import BENCHMARK_DEVICES, T_MIN_BENCHMARK, T_MAX_BENCHMARK

PARAM_BOUNDS = [
    (0.00, 1.00),   # 0: eta_CCCV
    (0.00, 3.00),   # 1: C_thresh
    (0.00, 3.00),   # 2: s_low
    (0.00, 1.00),   # 3: eta_arch_single
    (0.00, 1.00),   # 4: eta_cp
    (0.00, 1.00),   # 5: eta_pps
    (0.00, 1.00),   # 6: eta_pd
    (0.00, 1.00),   # 7: eta_5v
    (0.00, 1.00),   # 8: eta_apple
    (0.00, 3.00),   # 9: k
    (0.00, 3.00),   # 10: p
]

PARAM_NAMES = [
    "eta_CCCV", "C_thresh", "s_low",
    "eta_arch_single", "eta_cp", "eta_pps", "eta_pd", "eta_5v", "eta_apple",
    "k", "p"
]

T_HANDSHAKE = 0.5000  # Fixed physical protocol handshake intercept (mins)

def predict_single(dev, params):
    eta_CCCV, C_thresh, s_low, eta_arch_single, eta_cp, eta_pps, eta_pd, eta_5v, eta_apple, k, p = params
    wh = dev["battery_wh"]
    p_peak = dev["peak_power_w"]
    arch = dev["architecture"]
    proto = dev["protocol"]
    
    C_rate = p_peak / wh
    
    # 1. CC/CV Efficiency (strictly eta_CCCV for C_rate > C_thresh, no secondary slope)
    if C_rate <= C_thresh:
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)
    else:
        eff_eta_CCCV = eta_CCCV
    eff_eta_CCCV = max(0.001, min(1.00, eff_eta_CCCV))
    
    # 2. Architecture Efficiency
    eta_arch = 1.0000 if arch == "dual" else eta_arch_single
    
    # 3. Protocol Efficiency
    if proto == "charge_pump":
        eta_proto = eta_cp
    elif proto == "pps":
        eta_proto = eta_pps
    elif proto == "fixed_pd":
        eta_proto = eta_pd
    elif proto == "legacy_5v":
        eta_proto = eta_5v
    elif proto == "apple_legacy":
        eta_proto = eta_apple
    else:
        eta_proto = 0.70
        
    # 4. Thermal Decay Kinetics (Model B: Stretched Exponential Decay)
    if C_rate > C_thresh:
        diff = C_rate - C_thresh
        eta_thermal = math.exp(-k * (diff ** p))
    else:
        eta_thermal = 1.0000
    eta_thermal = max(0.001, min(1.00, eta_thermal))
    
    # 5. Effective Power
    p_eff = p_peak * eff_eta_CCCV * eta_arch * eta_proto * eta_thermal
    p_eff = max(0.01, min(p_peak, p_eff))
    
    # 6. Duration
    t_pred = (wh / p_eff) * 60.0 + T_HANDSHAKE
    return {
        "t_pred": t_pred,
        "C_rate": C_rate,
        "eff_eta_CCCV": eff_eta_CCCV,
        "eta_arch": eta_arch,
        "eta_proto": eta_proto,
        "eta_thermal": eta_thermal,
        "p_eff": p_eff
    }

def huber_loss_calc(r, delta):
    abs_r = abs(r)
    if abs_r <= delta:
        return 0.5 * (r ** 2)
    else:
        return delta * (abs_r - 0.5 * delta)

def loss_evaluator(params, loss_type="mse", delta=10.0):
    total = 0.0
    for dev in BENCHMARK_DEVICES:
        res = predict_single(dev, params)
        r = res["t_pred"] - dev["t_actual_min"]
        if loss_type == "mse":
            total += r ** 2
        elif loss_type == "mae":
            total += abs(r)
        elif loss_type == "huber":
            total += huber_loss_calc(r, delta)
    return total / len(BENCHMARK_DEVICES)

def compute_full_metrics(params):
    device_results = []
    diffs_T = []
    
    for dev in BENCHMARK_DEVICES:
        res = predict_single(dev, params)
        tp = res["t_pred"]
        ta = dev["t_actual_min"]
        sa = dev["s_actual"]
        dT = tp - ta
        diffs_T.append(dT)
        
        dev_entry = {
            "name": dev["name"],
            "tier": dev["tier"],
            "battery_wh": dev["battery_wh"],
            "peak_power_w": dev["peak_power_w"],
            "architecture": dev["architecture"],
            "protocol": dev["protocol"],
            "t_actual": ta,
            "s_actual": sa,
            "t_pred": round(tp, 2),
            "dT": round(dT, 2),
            "C_rate": round(res["C_rate"], 2),
            "eff_eta_CCCV": round(res["eff_eta_CCCV"], 4),
            "eta_arch": round(res["eta_arch"], 4),
            "eta_proto": round(res["eta_proto"], 4),
            "eta_thermal": round(res["eta_thermal"], 4),
            "p_eff": round(res["p_eff"], 2),
            "gsmarena_url": dev["gsmarena_url"]
        }
        device_results.append(dev_entry)
        
    diffs_T = np.array(diffs_T)
    mse_T = float(np.mean(diffs_T ** 2))
    rmse_T = float(np.sqrt(mse_T))
    mae_T = float(np.mean(np.abs(diffs_T)))
    mean_dT = float(np.mean(diffs_T))
    
    t_preds = np.array([d["t_pred"] for d in device_results])
    t_min_C = float(np.min(t_preds))
    t_max_C = float(np.max(t_preds))
    
    diffs_S1 = []
    diffs_S2 = []
    for d in device_results:
        tp = d["t_pred"]
        sa = d["s_actual"]
        
        # Strategy 1 (dynamic bounds)
        s1 = 10.0 * (math.log(t_max_C / tp) / math.log(t_max_C / t_min_C))
        dS1 = s1 - sa
        d["s_pred_s1"] = round(s1, 4)
        d["dS_s1"] = round(dS1, 4)
        diffs_S1.append(dS1)
        
        # Strategy 2 (aligned benchmark bounds [9.0, 241.0])
        s2 = 10.0 * (math.log(T_MAX_BENCHMARK / tp) / math.log(T_MAX_BENCHMARK / T_MIN_BENCHMARK))
        dS2 = s2 - sa
        d["s_pred_s2"] = round(s2, 4)
        d["dS_s2"] = round(dS2, 4)
        diffs_S2.append(dS2)
        
    diffs_S1 = np.array(diffs_S1)
    diffs_S2 = np.array(diffs_S2)
    
    strat1_metrics = {
        "MSE_S": float(np.mean(diffs_S1 ** 2)),
        "RMSE_S": float(np.sqrt(np.mean(diffs_S1 ** 2))),
        "MAE_S": float(np.mean(np.abs(diffs_S1))),
        "Mean_dS": float(np.mean(diffs_S1))
    }
    strat2_metrics = {
        "MSE_S": float(np.mean(diffs_S2 ** 2)),
        "RMSE_S": float(np.sqrt(np.mean(diffs_S2 ** 2))),
        "MAE_S": float(np.mean(np.abs(diffs_S2))),
        "Mean_dS": float(np.mean(diffs_S2))
    }
    
    return {
        "MSE_T": mse_T,
        "RMSE_T": rmse_T,
        "MAE_T": mae_T,
        "Mean_dT": mean_dT,
        "T_min_C": t_min_C,
        "T_max_C": t_max_C,
        "Strategy_1": strat1_metrics,
        "Strategy_2": strat2_metrics,
        "device_predictions": device_results
    }

def run_opt_robust(loss_type="mse", delta=10.0):
    t0 = time.time()
    best_res = None
    best_fun = float("inf")
    
    # Try seeds 42, 123, 999 to guarantee global optimum
    for seed in [42, 123, 999]:
        res = differential_evolution(
            loss_evaluator,
            bounds=PARAM_BOUNDS,
            args=(loss_type, delta),
            strategy='best1bin',
            maxiter=3000,
            popsize=35,
            tol=1e-9,
            mutation=(0.5, 1.0),
            recombination=0.9,
            seed=seed,
            polish=True,
            workers=1
        )
        if res.fun < best_fun:
            best_fun = res.fun
            best_res = res
            
    # Final L-BFGS-B polish
    res_lbfgs = minimize(
        loss_evaluator,
        x0=best_res.x,
        args=(loss_type, delta),
        bounds=PARAM_BOUNDS,
        method='L-BFGS-B'
    )
    if res_lbfgs.fun < best_fun:
        final_x = res_lbfgs.x
        final_fun = res_lbfgs.fun
    else:
        final_x = best_res.x
        final_fun = best_fun
        
    elapsed = time.time() - t0
    params = final_x.tolist()
    param_dict = {name: round(val, 4) for name, val in zip(PARAM_NAMES, params)}
    eval_res = compute_full_metrics(params)
    
    return {
        "loss_type": loss_type,
        "delta": delta if loss_type == "huber" else None,
        "loss_val": float(final_fun),
        "params": param_dict,
        "raw_params": params,
        "metrics": {
            "MSE_T": eval_res["MSE_T"],
            "RMSE_T": eval_res["RMSE_T"],
            "MAE_T": eval_res["MAE_T"],
            "Mean_dT": eval_res["Mean_dT"],
            "T_min_C": eval_res["T_min_C"],
            "T_max_C": eval_res["T_max_C"],
            "Strategy_1": eval_res["Strategy_1"],
            "Strategy_2": eval_res["Strategy_2"],
        },
        "device_predictions": eval_res["device_predictions"],
        "elapsed_sec": round(elapsed, 2)
    }

def main():
    results = {}
    deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]
    results["huber_sweep"] = []
    
    print("=== Relaunching Robust Multi-Seed Huber Sensitivity Sweep ===")
    for d in deltas:
        res = run_opt_robust(loss_type="huber", delta=d)
        m = res["metrics"]
        print(f"delta = {d:4.1f} mins | Loss: {res['loss_val']:8.4f} | MSE_T: {m['MSE_T']:6.2f} | RMSE_T: {m['RMSE_T']:5.2f} | MAE_T: {m['MAE_T']:5.2f} | Mean_dT: {m['Mean_dT']:+6.2f} | Score MAE_S: {m['Strategy_2']['MAE_S']:.4f}")
        results["huber_sweep"].append({
            "delta": d,
            "loss_val": round(res["loss_val"], 4),
            "MSE_T": round(m["MSE_T"], 2),
            "RMSE_T": round(m["RMSE_T"], 2),
            "MAE_T": round(m["MAE_T"], 2),
            "Mean_dT": round(m["Mean_dT"], 2),
            "elapsed_sec": res["elapsed_sec"],
            "params": res["params"],
            "metrics": m,
            "device_predictions": res["device_predictions"]
        })
        
    print("\n=== Robust Pure MSE ===")
    opt_mse = run_opt_robust(loss_type="mse")
    m_mse = opt_mse["metrics"]
    print(f"Pure MSE     | Loss: {opt_mse['loss_val']:8.4f} | MSE_T: {m_mse['MSE_T']:6.2f} | RMSE_T: {m_mse['RMSE_T']:5.2f} | MAE_T: {m_mse['MAE_T']:5.2f} | Mean_dT: {m_mse['Mean_dT']:+6.2f} | Score MAE_S: {m_mse['Strategy_2']['MAE_S']:.4f}")
    results["mse"] = opt_mse
    
    print("\n=== Robust Pure MAE ===")
    opt_mae = run_opt_robust(loss_type="mae")
    m_mae = opt_mae["metrics"]
    print(f"Pure MAE     | Loss: {opt_mae['loss_val']:8.4f} | MSE_T: {m_mae['MSE_T']:6.2f} | RMSE_T: {m_mae['RMSE_T']:5.2f} | MAE_T: {m_mae['MAE_T']:5.2f} | Mean_dT: {m_mae['Mean_dT']:+6.2f} | Score MAE_S: {m_mae['Strategy_2']['MAE_S']:.4f}")
    results["mae"] = opt_mae
    
    with open("scratch/robust_optimization_results.json", "w") as f:
        json.dump(results, f, indent=2)
        
    print("\nSaved to scratch/robust_optimization_results.json")

if __name__ == "__main__":
    main()
