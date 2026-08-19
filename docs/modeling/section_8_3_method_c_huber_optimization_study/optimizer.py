import numpy as np
from scipy.optimize import least_squares
import matplotlib.pyplot as plt
import pandas as pd

# Validation Dataset
# Based on real-world test data for wireless charging 0-100% times
data = [
    {
        "name": "Xiaomi 14 Ultra",
        "capacity_mah": 5000,
        "p_wireless_max": 80,
        "f_transfer": 0.83, # Proprietary High-Power w/ active cooling stand
        "actual_time_mins": 46
    },
    {
        "name": "OnePlus 12",
        "capacity_mah": 5400,
        "p_wireless_max": 50,
        "f_transfer": 0.83, # Proprietary High-Power w/ active cooling stand
        "actual_time_mins": 55
    },
    {
        "name": "iPhone 15 Pro Max",
        "capacity_mah": 4422,
        "p_wireless_max": 15,
        "f_transfer": 0.82, # Qi2 Magnetic
        "actual_time_mins": 135
    },
    {
        "name": "Samsung Galaxy S24 Ultra",
        "capacity_mah": 5000,
        "p_wireless_max": 15,
        "f_transfer": 0.78, # Qi EPP
        "actual_time_mins": 125
    },
    {
        "name": "Google Pixel 8 Pro",
        "capacity_mah": 5050,
        "p_wireless_max": 23,
        "f_transfer": 0.83, # Proprietary w/ active cooling (Pixel Stand 2)
        "actual_time_mins": 140 # approximate
    }
]

df = pd.DataFrame(data)
df['e_supply_wh'] = df['capacity_mah'] * 3.85 / 1000
df['c_rate'] = df['p_wireless_max'] / df['e_supply_wh']

# Current Model (wired stats applied to wireless)
k_current = 0.35
p_current = 0.70
c0_current = 0.80

def predict_time(c_rate, e_supply, p_max, f_trans, k, p, c0):
    # Calculate thermal throttling factor
    base = np.maximum(0, c_rate - c0)
    f_thermal = 1 / (1 + k * (base ** p))
    
    # Calculate predicted time
    t_pred = 60 * (e_supply / (p_max * f_trans * f_thermal))
    return t_pred, f_thermal

# Calculate current predictions
current_preds = []
for _, row in df.iterrows():
    t_pred, f_th = predict_time(row['c_rate'], row['e_supply_wh'], row['p_wireless_max'], row['f_transfer'], k_current, p_current, c0_current)
    current_preds.append(t_pred)

df['pred_time_current'] = current_preds

print("Current Model Performance:")
print(df[['name', 'actual_time_mins', 'pred_time_current']])
print(f"Mean Absolute Error: {np.mean(np.abs(df['actual_time_mins'] - df['pred_time_current'])):.2f} mins\n")

# Objective function for optimization
def residuals(params, c_rate, e_supply, p_max, f_trans, actual_time):
    k, p, c0 = params
    t_pred, _ = predict_time(c_rate, e_supply, p_max, f_trans, k, p, c0)
    return t_pred - actual_time

# Initial guess
initial_guess = [0.35, 0.70, 0.80]

# Bounds for parameters
bounds = ([0.0, 0.1, 0.1], [5.0, 2.0, 1.0])

# Run optimization
result = least_squares(
    residuals, 
    initial_guess, 
    bounds=bounds,
    args=(df['c_rate'].values, df['e_supply_wh'].values, df['p_wireless_max'].values, df['f_transfer'].values, df['actual_time_mins'].values),
    loss='huber',
    f_scale=10.0
)

k_opt, p_opt, c0_opt = result.x

print("\nOptimization Complete.")
print(f"Optimized Parameters:")
print(f"k  = {k_opt:.4f} (Original: {k_current})")
print(f"p  = {p_opt:.4f} (Original: {p_current})")
print(f"c0 = {c0_opt:.4f} (Original: {c0_current})\n")

# Calculate optimized predictions
opt_preds = []
opt_f_th = []
for _, row in df.iterrows():
    t_pred, f_th = predict_time(row['c_rate'], row['e_supply_wh'], row['p_wireless_max'], row['f_transfer'], k_opt, p_opt, c0_opt)
    opt_preds.append(t_pred)
    opt_f_th.append(f_th)

df['pred_time_opt'] = opt_preds
df['f_thermal_opt'] = opt_f_th

print("Optimized Model Performance:")
print(df[['name', 'p_wireless_max', 'actual_time_mins', 'pred_time_current', 'pred_time_opt', 'f_thermal_opt']])
print(f"Mean Absolute Error (Current): {np.mean(np.abs(df['actual_time_mins'] - df['pred_time_current'])):.2f} mins")
print(f"Mean Absolute Error (Optimized): {np.mean(np.abs(df['actual_time_mins'] - df['pred_time_opt'])):.2f} mins")

plt.figure(figsize=(10, 6))
c_rate_range = np.linspace(0, 5, 100)
f_th_current = 1 / (1 + k_current * (np.maximum(0, c_rate_range - c0_current) ** p_current))
f_th_opt = 1 / (1 + k_opt * (np.maximum(0, c_rate_range - c0_opt) ** p_opt))

plt.plot(c_rate_range, f_th_current, label=f'Current (k={k_current}, p={p_current}, c0={c0_current})', linestyle='--')
plt.plot(c_rate_range, f_th_opt, label=f'Optimized (k={k_opt:.3f}, p={p_opt:.3f}, c0={c0_opt:.3f})')
plt.title('Thermal Throttle Factor (F_thermal_wireless) vs C-Rate')
plt.xlabel('Wireless C-Rate')
plt.ylabel('F_thermal_wireless')
plt.legend()
plt.grid(True)
plt.savefig('thermal_curve_comparison.png')
print("\nPlot saved to thermal_curve_comparison.png")
