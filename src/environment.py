class Environment:
    def __init__(self, agents, initial_positions, initial_speeds):
        self.agents = agents

        for agent, pos, spd in zip(self.agents, initial_positions, initial_speeds):
            agent.position = float(pos)
            agent.speed = float(spd)

    # ✅ پیدا کردن عامل جلویی بر اساس position (نه index)
    def get_front_agent(self, agent):
        front_agents = [a for a in self.agents if a.position > agent.position]
        if not front_agents:
            return None
        return min(front_agents, key=lambda a: a.position)

    def step(self):
        decisions = []

        # ---------- Phase 1: perception + reasoning ----------
        for agent in self.agents:
            front_agent = self.get_front_agent(agent)
            distance = agent.perceive(front_agent)
            action, thought = agent.reason(distance)
            front_position = front_agent.position if front_agent else None
            decisions.append((agent, action, thought, front_position))

        # ---------- Phase 2: action (simultaneous) ----------
        for agent, action, _, front_position in decisions:
            agent.act(action, front_position)

        # ---------- Phase 3: enforce single-lane ordering ----------
        self.agents.sort(key=lambda a: a.position)
        for i in range(1, len(self.agents)):
            if self.agents[i].position <= self.agents[i - 1].position:
                self.agents[i].position = self.agents[i - 1].position + 0.1
                self.agents[i].speed = min(
                    self.agents[i].speed,
                    self.agents[i - 1].speed
                )

        # ---------- logging ----------
        logs = []
        for agent, action, thought, _ in decisions:
            logs.append({
                "agent": agent.id,
                "action": action,
                "thought": thought,
                "speed": agent.speed,
                "position": round(agent.position, 2)
            })

        return logs
