from src.agent import Agent
from src.environment import Environment

def run_simulation(steps=10):
    agents = [
        Agent(1, "aggressive"),
        Agent(2, "cautious"),
        Agent(3, "cautious")
    ]

    env = Environment(agents)
    all_logs = []

    for t in range(steps):
        logs = env.step()
        for log in logs:
            log["time"] = t
            all_logs.append(log)

    return all_logs
