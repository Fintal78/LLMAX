import math
import time
import json
import numpy as np
from scipy.optimize import differential_evolution
from benchmark_devices import BENCHMARK_DEVICES, T_MIN_BENCHMARK, T_MAX_BENCHMARK

T_HANDSHAKE = 0.5000  # Fixed physical protocol handshake intercept (mins)

PARAM_BOUNDS = [
    (0.30, 0.95),   # eta_CCCV
    (0.50, 3.00),   # C_thresh
    (0.00, 1.50),   # s_low
    (0.00, 1.00),   # s_high
    (0.0001, 1.00), # k
    (0.50, 3.00),   # p
    (0.60, 1.00),   # eta_arch_single
    (0.70, 1.00),   # eta_cp
    (0.60, 1.00),   # eta_pps
    (0.50, 0.95),   # eta_pd
    (0.50, 0.95),   # eta_5v
    (0.50, 0.95),   # eta_apple
]

PARAM_NAMES = [
    "eta_CCCV", "C_thresh", "s_low", "s_high", "k", "p",
    "eta_arch_single", "eta_cp", "eta_pps", "eta_pd", "eta_5v", "eta_apple"
]

def predict_device(dev, params):
    eta_CCCV, C_thresh, s_low, s_high, k, p, eta_arch_single, eta_cp, eta_pps, eta_pd, eta_5v, eta_apple = params
    
    wh = dev["battery_wh"]
    p_peak = dev["peak_power_w"]
    arch = dev["architecture"]
    proto = dev["protocol"]
    
    C_rate = p_peak / wh
    
    # 1. CC/CV Efficiency
    if C_rate <= C_thresh:
        eff_eta_CCCV = eta_CCCV + s_low * (C_thresh - C_rate)
    else:
        eff_eta_CCCV = eta_CCCV + s_high * (C_thresh - C_rate)
    eff_eta_CCCV = max(0.05, min(1.00, eff_eta_CCCV))
    
    # 2. Architecture Efficiency
    if arch == "dual":
        eta_arch = 1.0000
    else:
        eta_arch = eta_arch_single
        
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
        
    # 4. Thermal Decay Efficiency
    if C_rate > C_thresh:
        diff = C_rate - C_thresh
        eta_thermal = math.exp(-k * (diff ** p))
    else:
        eta_thermal = 1.0000
    eta_thermal = max(0.05, min(1.00, eta_thermal))
    
    # 5. Effective Power
    p_eff = p_peak * eff_eta_CCCV * eta_arch * eta_proto * eta_thermal
    p_eff = max(0.1, min(p_peak, p_eff))
    
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

def huber_element(r, delta):
    abs_r = abs(r)
    if abs_r <= delta:
        return 0.5 * (r ** 2)
    else:
        return delta * (abs_r - 0.5 * delta)

def loss_func(params, loss_type="mse", delta=10.0):
    total_loss = 0.0
    N = len(BENCHMARK_DEVICES)
    for dev in BENCHMARK_DEVICES:
        res = predict_device(dev, params)
        r = res["t_pred"] - dev["t_actual_min"]
        if loss_type == "mse":
            total_loss += (r ** 2)
        elif loss_type == "mae":
            total_loss += abs(r)
        elif loss_type == "huber":
            total_loss += huber_element(r, delta)
    return total_loss / N

def compute_all_metrics(params):
    N = len(BENCHMARK_DEVICES)
    device_results = []
    diffs_T = []
    
    for dev in BENCHMARK_DEVICES:
        res = predict_device(dev, params)
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
    
    # Compute Strategy 1 and Strategy 2 scores
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

def optimize_model(loss_type="mse", delta=10.0, seed=42):
    t0 = time.time()
    res = differential_evolution(
        loss_func,
        bounds=PARAM_BOUNDS,
        args=(loss_type, delta),
        strategy='best1bin',
        maxiter=2000,
        popsize=25,
        tol=1e-7,
        mutation=(0.5, 1.0),
        recombination=0.9,
        seed=seed,
        polish=True
    )
    elapsed = time.time() - t0
    params = res.x.tolist()
    param_dict = {name: round(val, 4) for name, val in zip(PARAM_NAMES, params)}
    eval_res = compute_all_metrics(params)
    
    return {
        "loss_type": loss_type,
        "delta": delta if loss_type == "huber" else None,
        "loss_val": float(res.fun),
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
    print("================================================================================")
    print("STARTING DETERMINISTIC GLOBAL OPTIMIZATION (Differential Evolution, seed=42)")
    print("================================================================================")
    
    results = {}
    
    # 1. Delta sweep for Huber
    deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]
    results["huber_sweep"] = []
    
    print("\n--- Running Huber Delta Grid Sweep (12 values) ---")
    for d in deltas:
        print(f"Optimizing Huber delta = {d:4.1f} mins ...", end="", flush=True)
        res = optimize_model(loss_type="huber", delta=d, seed=42)
        print(f" Done ({res['elapsed_sec']}s) | MSE_T: {res['metrics']['MSE_T']:.2f} | MAE_T: {res['metrics']['MAE_T']:.2f} | Mean_dT: {res['metrics']['Mean_dT']:+.2f}")
        results["huber_sweep"].append({
            "delta": d,
            "MSE_T": round(res["metrics"]["MSE_T"], 2),
            "RMSE_T": round(res["metrics"]["RMSE_T"], 2),
            "MAE_T": round(res["metrics"]["MAE_T"], 2),
            "Mean_dT": round(res["metrics"]["Mean_dT"], 2),
            "elapsed_sec": res["elapsed_sec"],
            "params": res["params"],
            "metrics": res["metrics"],
            "device_predictions": res["device_predictions"]
        })
        
    # 2. Pure MSE (Option 1)
    print("\n--- Running Option 1: Pure Mean Squared Error (MSE) ---")
    opt_mse = optimize_model(loss_type="mse", seed=42)
    print(f"MSE Done ({opt_mse['elapsed_sec']}s) | MSE_T: {opt_mse['metrics']['MSE_T']:.2f} | MAE_T: {opt_mse['metrics']['MAE_T']:.2f} | Mean_dT: {opt_mse['metrics']['Mean_dT']:+.2f}")
    results["mse"] = opt_mse
    
    # 3. Pure MAE (Option 2)
    print("\n--- Running Option 2: Pure Mean Absolute Error (MAE) ---")
    opt_mae = optimize_model(loss_type="mae", seed=42)
    print(f"MAE Done ({opt_mae['elapsed_sec']}s) | MSE_T: {opt_mae['metrics']['MSE_T']:.2f} | MAE_T: {opt_mae['metrics']['MAE_T']:.2f} | Mean_dT: {opt_mae['metrics']['Mean_dT']:+.2f}")
    results["mae"] = opt_mae
    
    # 4. Save results to JSON
    with open("scratch/optimization_results.json", "w") as f:
        json.dump(results, f, indent=2)
        
    print("\nAll optimizations completed successfully! Saved to scratch/optimization_results.json")

if __name__ == "__main__":
    main()
