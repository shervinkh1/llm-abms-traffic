class Agent:
    def __init__(self, agent_id, personality):
        self.id = agent_id
        self.personality = personality  # aggressive | cautious
        self.speed = 3
        self.position = 0
        self.memory = []

    def perceive(self, front_agent):
        if front_agent is None:
            return None
        return front_agent.position - self.position

    def reason(self, distance):
        recent_memory = self.memory[-2:]
        recently_in_danger = any("خطر" in m for m in recent_memory)

        if distance is not None and distance < 5:
            if self.personality == "aggressive":
                action = "slow"
                thought = "فاصله کمه ولی عجولم، کمی ترمز می‌کنم"
            else:
                action = "brake"
                thought = "خطر زیاده، ترمز کامل"

        elif recently_in_danger:
            action = "slow"
            thought = "اخیراً خطر حس کردم، محتاط‌تر حرکت می‌کنم"

        else:
            action = "move"
            thought = "شرایط امنه، حرکت می‌کنم"

        self.memory.append(thought)
        if len(self.memory) > 3:  # memory decay
            self.memory.pop(0)

        return action, thought

    def act(self, action):
        if action == "brake":
            self.speed = max(0, self.speed - 2)
        elif action == "slow":
            self.speed = max(0, self.speed - 1)
        elif action == "move":
            self.speed = min(5, self.speed + 1)

        self.position += self.speed
