# Configure archetypes
phones = [
    {"name": "Ultra Gaming Flagship", "a_score": 10.0, "b_score": 10.0, "perf": 10.0, "node": 10.0},
    {"name": "Standard Flagship (S24 U)", "a_score": 7.0, "b_score": 7.0, "perf": 10.0, "node": 10.0},
    {"name": "Flagship (Hot Chip)", "a_score": 6.5, "b_score": 7.0, "perf": 9.5, "node": 5.0},
    {"name": "Premium Mid-Range", "a_score": 5.0, "b_score": 4.0, "perf": 6.0, "node": 8.0},
    {"name": "Budget Plastic", "a_score": 3.0, "b_score": 0.0, "perf": 3.0, "node": 6.0},
    {"name": "Ultra Budget", "a_score": 1.0, "b_score": 0.0, "perf": 1.0, "node": 4.0},
    {"name": "Impossible Max All", "a_score": 10.0, "b_score": 10.0, "perf": 0.0, "node": 10.0},
    {"name": "Realistic Cool Midrange", "a_score": 6.0, "b_score": 5.0, "perf": 5.0, "node": 8.0},
]

def simulate(bonus_divisor, phys_weight):
    print(f"--- Divisor: {bonus_divisor}, Phys Weight: {phys_weight} ---")
    print(f"{'Name':<30} | {'Phys':>5} | {'Mitig':>5} | {'Bonus':>5} | {'Tot(U)':>6} | {'Tot(C)':>6} | {'Wasted':>6}")
    print("-" * 75)
    for p in phones:
        phys = (0.5 * p["a_score"]) + (0.5 * p["b_score"])
        mitigation = (10.0 - p["perf"]) + p["node"]
        bonus = mitigation / bonus_divisor
        
        total_unclamped = (phys * phys_weight) + bonus
        total_clamped = min(10.0, max(0.0, total_unclamped))
        wasted = max(0, total_unclamped - 10.0)
        
        print(f"{p['name']:<30} | {phys:5.2f} | {mitigation:5.2f} | {bonus:5.2f} | {total_unclamped:6.2f} | {total_clamped:6.2f} | {wasted:6.2f}")
    print("\n")

simulate(bonus_divisor=5.0, phys_weight=0.8)
simulate(bonus_divisor=4.0, phys_weight=0.8)
simulate(bonus_divisor=5.0, phys_weight=1.0)
