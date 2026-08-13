import json
import math
import numpy as np
from scipy.optimize import differential_evolution, minimize

with open("scratch/verified_44_devices.json") as f:
    DEVICES = json.load(f)

print(f"Loaded {len(DEVICES)} verified devices.")

PROTO_MAP = {
    'charge_pump': 0,
    'pps': 1,
    'fixed_pd': 2,
    'legacy_5v': 3,
    'apple_legacy': 4
}

def predict_duration(params, dev):
    eta_CCCV = params[0]
    C_threshold = params[1]
    s_low = params[2]
    eta_arch_single = params[3]
    eta_proto_cp = params[4]
    eta_proto_pps = params[5]
    eta_proto_fpd = params[6]
    eta_proto_5v = params[7]
    eta_proto_app = params[8]
    k = params[9]
    p = params[10]
    T_handshake = 0.5000 # fixed

    prot_etas = [eta_proto_cp, eta_proto_pps, eta_proto_fpd, eta_proto_5v, eta_proto_app]

    e_supply = dev['battery_wh']
    p_peak = dev['peak_power_w']
    c_rate = p_peak / e_supply

    if c_rate > C_threshold:
        eff_eta_CCCV = eta_CCCV
    else:
        eff_eta_CCCV = eta_CCCV + s_low * (C_threshold - c_rate)

    eta_arch = 1.0000 if dev['architecture'] == 'dual' else eta_arch_single
    eta_protocol = prot_etas[PROTO_MAP[dev['protocol']]]

    diff = max(0.0, c_rate - C_threshold)
    eta_thermal = math.exp(-k * (diff ** p))

    p_effective = p_peak * eff_eta_CCCV * eta_arch * eta_protocol * eta_thermal
    if p_effective <= 1e-6:
        return 1e6

    t_predicted = (e_supply / p_effective) * 60.0 + T_handshake
    return t_predicted

def score_s2(t):
    t_min = 9.0
    t_max = 241.0
    if t <= t_min:
        return 10.0
    if t >= t_max:
        return 0.0
    return 10.0 * (math.log(t_max) - math.log(t)) / (math.log(t_max) - math.log(t_min))

def evaluate_metrics(params):
    n = len(DEVICES)
    t_preds = [predict_duration(params, d) for d in DEVICES]
    t_acts = [d['benchmark_duration_mins'] for d in DEVICES]
    
    e_t = [t_act - t_pred for t_act, t_pred in zip(t_acts, t_preds)]
    mse_t = sum(e**2 for e in e_t) / n
    rmse_t = math.sqrt(mse_t)
    mae_t = sum(abs(e) for e in e_t) / n
    mean_dt = sum(e_t) / n
    
    s_preds_s2 = [score_s2(tp) for tp in t_preds]
    s_acts = [d['benchmark_speed_score'] for d in DEVICES]
    e_s2 = [sa - sp for sa, sp in zip(s_acts, s_preds_s2)]
    
    mse_s2 = sum(e**2 for e in e_s2) / n
    rmse_s2 = math.sqrt(mse_s2)
    mae_s2 = sum(abs(e) for e in e_s2) / n
    mean_ds2 = sum(e_s2) / n
    
    return {
        "MSE_T": mse_t,
        "RMSE_T": rmse_t,
        "MAE_T": mae_t,
        "Mean_dT": mean_dt,
        "MSE_S": mse_s2,
        "RMSE_S": rmse_s2,
        "MAE_S": mae_s2,
        "Mean_dS": mean_ds2,
        "t_preds": t_preds
    }

# Search domain bounds
bounds = [
    (0.00, 1.00), # eta_CCCV
    (0.00, 3.00), # C_threshold
    (0.00, 3.00), # s_low
    (0.00, 1.00), # eta_arch_single
    (0.00, 1.00), # eta_proto_cp
    (0.00, 1.00), # eta_proto_pps
    (0.00, 1.00), # eta_proto_fpd
    (0.00, 1.00), # eta_proto_5v
    (0.00, 1.00), # eta_proto_app
    (0.00, 3.00), # k
    (0.00, 3.00)  # p
]

def huber_loss(params, delta):
    total = 0.0
    for dev in DEVICES:
        t_pred = predict_duration(params, dev)
        t_act = dev['benchmark_duration_mins']
        err = abs(t_act - t_pred)
        if err <= delta:
            loss = 0.5 * (err ** 2)
        else:
            loss = delta * err - 0.5 * (delta ** 2)
        total += loss
    return total / len(DEVICES)

def optimize_huber(delta):
    # Run DE with multiple strategies/polishing
    res = differential_evolution(
        lambda p: huber_loss(p, delta),
        bounds=bounds,
        seed=42,
        popsize=40,
        maxiter=3500,
        tol=1e-9,
        polish=True
    )
    # Double check with an L-BFGS-B polish
    res_lbfgs = minimize(
        lambda p: huber_loss(p, delta),
        x0=res.x,
        bounds=bounds,
        method='L-BFGS-B'
    )
    best_x = res_lbfgs.x if res_lbfgs.fun < res.fun else res.x
    metrics = evaluate_metrics(best_x)
    return {
        "delta": delta,
        "loss": float(huber_loss(best_x, delta)),
        "params": [float(x) for x in best_x],
        "metrics": metrics
    }

deltas = [5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0, 40.0, 50.0]
print("Running Huber sensitivity sweep...")
results = []
for d in deltas:
    r = optimize_huber(d)
    m = r["metrics"]
    print(f"delta={d:4.1f} | Loss={r['loss']:8.4f} | MSE_T={m['MSE_T']:6.2f} | RMSE_T={m['RMSE_T']:5.2f} | MAE_T={m['MAE_T']:5.2f} | Mean_dT={m['Mean_dT']:+5.2f} | MAE_S={m['MAE_S']:.4f}")
    results.append(r)

with open("scratch/huber_sweep_verified.json", "w") as f:
    json.dump(results, f, indent=2)
print("Saved to scratch/huber_sweep_verified.json")
