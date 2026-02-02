class Environment:
    def __init__(self, agents):
        self.agents = agents

    def step(self):
        decisions = []

        # Phase 1: perception + reasoning
        for i, agent in enumerate(self.agents):
            front_agent = self.agents[i - 1] if i > 0 else None
            distance = agent.perceive(front_agent)
            action, thought = agent.reason(distance)
            decisions.append((agent, action, thought))

        # Phase 2: action
        logs = []
        for agent, action, thought in decisions:
            agent.act(action)
            logs.append({
                "agent": agent.id,
                "action": action,
                "thought": thought,
                "speed": agent.speed,
                "position": agent.position
            })

        return logs

