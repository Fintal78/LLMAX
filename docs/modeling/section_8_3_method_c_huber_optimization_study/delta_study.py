import numpy as np
from scipy.optimize import least_squares
import pandas as pd

data = [
    {'name': 'Xiaomi 14 Ultra', 'cap': 5000, 'p_max': 80, 'f_tr': 0.83, 'actual': 46},
    {'name': 'OnePlus 12', 'cap': 5400, 'p_max': 50, 'f_tr': 0.83, 'actual': 55},
    {'name': 'iPhone 15 Pro Max', 'cap': 4422, 'p_max': 15, 'f_tr': 0.82, 'actual': 135},
    {'name': 'Samsung Galaxy S24 Ultra', 'cap': 5000, 'p_max': 15, 'f_tr': 0.78, 'actual': 125},
    {'name': 'Google Pixel 8 Pro', 'cap': 5050, 'p_max': 23, 'f_tr': 0.83, 'actual': 140}
]

df = pd.DataFrame(data)
df['e_supply'] = df['cap'] * 3.85 / 1000.0
df['c_rate'] = df['p_max'] / df['e_supply']

def predict_time(c_rate, e_supply, p_max, f_trans, k, p, c0):
    base = np.maximum(0, c_rate - c0)
    f_th = 1.0 / (1.0 + k * (base ** p))
    t_pred = 60.0 * (e_supply / (p_max * f_trans * f_th))
    return t_pred

def residuals(params, c_rate, e_supply, p_max, f_trans, actual):
    k, p, c0 = params
    t_pred = predict_time(c_rate, e_supply, p_max, f_trans, k, p, c0)
    return t_pred - actual

initial_guess = [0.35, 0.70, 0.80]
bounds = ([0.0, 0.1, 0.1], [5.0, 2.0, 1.0])

deltas = [0.0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0]

print("| Huber Delta | `k`    | `p`    | `c0`   | Bias (mins) | MAE (mins) | RMSE (mins) | Max Err (mins) |")
print("| :---------- | :----- | :----- | :----- | :---------- | :--------- | :---------- | :------------- |")

for d in deltas:
    f_scale = d if d > 0 else 1e-5
    res = least_squares(
        residuals, initial_guess, bounds=bounds,
        args=(df['c_rate'].values, df['e_supply'].values, df['p_max'].values, df['f_tr'].values, df['actual'].values),
        loss='huber', f_scale=f_scale
    )
    k_opt, p_opt, c0_opt = res.x
    
    t_preds = []
    for _, row in df.iterrows():
        t_preds.append(predict_time(row['c_rate'], row['e_supply'], row['p_max'], row['f_tr'], k_opt, p_opt, c0_opt))
    
    errs = np.array(t_preds) - df['actual'].values
    abs_errs = np.abs(errs)
    
    bias = np.mean(errs)
    mae = np.mean(abs_errs)
    rmse = np.sqrt(np.mean(errs**2))
    max_err = np.max(abs_errs)
    
    delta_str = "0.0 (L1)" if d == 0.0 else f"{d:.1f}"
    
    delta_pad = f"{delta_str:<11}"
    k_pad = f"{k_opt:.4f}"
    p_pad = f"{p_opt:.4f}"
    c0_pad = f"{c0_opt:.4f}"
    bias_pad = f"{bias:+.2f}"
    bias_pad = f"{bias_pad:<11}"
    mae_pad = f"{mae:.2f}"
    mae_pad = f"{mae_pad:<10}"
    rmse_pad = f"{rmse:.2f}"
    rmse_pad = f"{rmse_pad:<11}"
    max_pad = f"{max_err:.2f}"
    max_pad = f"{max_pad:<14}"
    
    print(f"| {delta_pad} | {k_pad} | {p_pad} | {c0_pad} | {bias_pad} | {mae_pad} | {rmse_pad} | {max_pad} |")
