import json

with open("scratch/optimization_results.json", "r") as f:
    data = json.load(f)

print("=" * 105)
print(f"{'Threshold (delta)':<22} | {'MSE_T (mins^2)':<16} | {'RMSE_T (mins)':<15} | {'MAE_T (mins)':<15} | {'Mean_dT (mins)':<15} | {'Time':<8}")
print("=" * 105)

for h in data["huber_sweep"]:
    d_str = f"delta = {h['delta']:4.1f} mins"
    print(f"{d_str:<22} | {h['MSE_T']:>13.2f} mins^2 | {h['RMSE_T']:>12.2f} mins | {h['MAE_T']:>12.2f} mins | {h['Mean_dT']:>+12.2f} mins | {h['elapsed_sec']:>5.1f}s")

print("\n" + "=" * 105)
print("COMPARATIVE MODEL SUMMARY MATRIX (SECTION 4.1)")
print("=" * 105)
print(f"{'Model Candidate':<32} | {'MSE_T (mins^2)':<16} | {'RMSE_T (mins)':<15} | {'MAE_T (mins)':<15} | {'Mean_dT (mins)':<15}")
print("-" * 105)

mse = data["mse"]
mae = data["mae"]
h10 = [h for h in data["huber_sweep"] if h["delta"] == 10.0][0]
h25 = [h for h in data["huber_sweep"] if h["delta"] == 25.0][0]
h30 = [h for h in data["huber_sweep"] if h["delta"] == 30.0][0]

print(f"{'Opt 1: Pure MSE Model':<32} | {mse['metrics']['MSE_T']:>13.2f} mins^2 | {mse['metrics']['RMSE_T']:>12.2f} mins | {mse['metrics']['MAE_T']:>12.2f} mins | {mse['metrics']['Mean_dT']:>+12.2f} mins")
print(f"{'Opt 2: Pure MAE Model':<32} | {mae['metrics']['MSE_T']:>13.2f} mins^2 | {mae['metrics']['RMSE_T']:>12.2f} mins | {mae['metrics']['MAE_T']:>12.2f} mins | {mae['metrics']['Mean_dT']:>+12.2f} mins")
print(f"{'Opt 3: Huber Model (delta=10.0)':<32} | {h10['metrics']['MSE_T']:>13.2f} mins^2 | {h10['metrics']['RMSE_T']:>12.2f} mins | {h10['metrics']['MAE_T']:>12.2f} mins | {h10['metrics']['Mean_dT']:>+12.2f} mins")
print(f"{'Opt 3: Huber Model (delta=25.0)':<32} | {h25['metrics']['MSE_T']:>13.2f} mins^2 | {h25['metrics']['RMSE_T']:>12.2f} mins | {h25['metrics']['MAE_T']:>12.2f} mins | {h25['metrics']['Mean_dT']:>+12.2f} mins")
print(f"{'Opt 3: Huber Model (delta=30.0)':<32} | {h30['metrics']['MSE_T']:>13.2f} mins^2 | {h30['metrics']['RMSE_T']:>12.2f} mins | {h30['metrics']['MAE_T']:>12.2f} mins | {h30['metrics']['Mean_dT']:>+12.2f} mins")

print("\n" + "=" * 105)
print("SPEED SCORE METRIC MATRIX (SECTION 5.2 - STRATEGY 2: BENCHMARK ALIGNED BOUNDS)")
print("=" * 105)
print(f"{'Model Candidate':<32} | {'MSE_S (pts^2)':<16} | {'RMSE_S (pts)':<15} | {'MAE_S (pts)':<15} | {'Mean_dS (pts)':<15}")
print("-" * 105)

s2_mse = mse['metrics']['Strategy_2']
s2_mae = mae['metrics']['Strategy_2']
s2_h10 = h10['metrics']['Strategy_2']
s2_h25 = h25['metrics']['Strategy_2']
s2_h30 = h30['metrics']['Strategy_2']

print(f"{'Opt 1: Pure MSE Model':<32} | {s2_mse['MSE_S']:>13.4f} pts^2 | {s2_mse['RMSE_S']:>12.4f} pts | {s2_mse['MAE_S']:>12.4f} pts | {s2_mse['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 2: Pure MAE Model':<32} | {s2_mae['MSE_S']:>13.4f} pts^2 | {s2_mae['RMSE_S']:>12.4f} pts | {s2_mae['MAE_S']:>12.4f} pts | {s2_mae['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 3: Huber Model (delta=10.0)':<32} | {s2_h10['MSE_S']:>13.4f} pts^2 | {s2_h10['RMSE_S']:>12.4f} pts | {s2_h10['MAE_S']:>12.4f} pts | {s2_h10['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 3: Huber Model (delta=25.0)':<32} | {s2_h25['MSE_S']:>13.4f} pts^2 | {s2_h25['RMSE_S']:>12.4f} pts | {s2_h25['MAE_S']:>12.4f} pts | {s2_h25['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 3: Huber Model (delta=30.0)':<32} | {s2_h30['MSE_S']:>13.4f} pts^2 | {s2_h30['RMSE_S']:>12.4f} pts | {s2_h30['MAE_S']:>12.4f} pts | {s2_h30['Mean_dS']:>+12.4f} pts")

print("\n" + "=" * 105)
print("SPEED SCORE METRIC MATRIX (SECTION 5.2 - STRATEGY 1: DYNAMIC BOUNDS)")
print("=" * 105)
print(f"{'Model Candidate':<32} | {'MSE_S (pts^2)':<16} | {'RMSE_S (pts)':<15} | {'MAE_S (pts)':<15} | {'Mean_dS (pts)':<15}")
print("-" * 105)

s1_mse = mse['metrics']['Strategy_1']
s1_mae = mae['metrics']['Strategy_1']
s1_h10 = h10['metrics']['Strategy_1']
s1_h25 = h25['metrics']['Strategy_1']
s1_h30 = h30['metrics']['Strategy_1']

print(f"{'Opt 1: Pure MSE Model':<32} | {s1_mse['MSE_S']:>13.4f} pts^2 | {s1_mse['RMSE_S']:>12.4f} pts | {s1_mse['MAE_S']:>12.4f} pts | {s1_mse['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 2: Pure MAE Model':<32} | {s1_mae['MSE_S']:>13.4f} pts^2 | {s1_mae['RMSE_S']:>12.4f} pts | {s1_mae['MAE_S']:>12.4f} pts | {s1_mae['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 3: Huber Model (delta=10.0)':<32} | {s1_h10['MSE_S']:>13.4f} pts^2 | {s1_h10['RMSE_S']:>12.4f} pts | {s1_h10['MAE_S']:>12.4f} pts | {s1_h10['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 3: Huber Model (delta=25.0)':<32} | {s1_h25['MSE_S']:>13.4f} pts^2 | {s1_h25['RMSE_S']:>12.4f} pts | {s1_h25['MAE_S']:>12.4f} pts | {s1_h25['Mean_dS']:>+12.4f} pts")
print(f"{'Opt 3: Huber Model (delta=30.0)':<32} | {s1_h30['MSE_S']:>13.4f} pts^2 | {s1_h30['RMSE_S']:>12.4f} pts | {s1_h30['MAE_S']:>12.4f} pts | {s1_h30['Mean_dS']:>+12.4f} pts")

print("\n" + "=" * 105)
print("OPTIMIZED PARAMETERS (SECTION 4.2)")
print("=" * 105)
for name, m in [("Opt 1 (MSE)", mse), ("Opt 2 (MAE)", mae), ("Opt 3 (Huber d=10.0)", h10), ("Opt 3 (Huber d=30.0)", h30)]:
    print(f"\n{name}:")
    for k, v in m["params"].items():
        print(f"  {k:<18}: {v:>8.4f}")
