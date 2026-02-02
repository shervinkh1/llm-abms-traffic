from src.simulation import run_simulation

logs = run_simulation(steps=10)

for log in logs:
    print(log)
