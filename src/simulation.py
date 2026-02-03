from src.agent import Agent
from src.environment import Environment

def run_simulation(steps=10):
    agents = [
        Agent(1, "cautious"),
        Agent(2, "aggressive"),
        Agent(3, "cautious")
    ]

    # ✅ تنظیمات مورد نظر تو
    initial_positions = [0, 2, 5]
    initial_speeds = [2, 1, 0]

    env = Environment(
        agents,
        initial_positions=initial_positions,
        initial_speeds=initial_speeds
    )

    all_logs = []

    for t in range(steps):
        logs = env.step()
        for log in logs:
            log["time"] = t
            all_logs.append(log)

    return all_logs
