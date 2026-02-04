class Agent:
    def __init__(self, agent_id, personality):
        self.id = agent_id
        self.personality = personality  # aggressive | cautious
        self.position = 0.0
        self.speed = 0.0
        self.memory = []  # ["danger", "move"]

    # ---------- Perception ----------
    def perceive(self, front_agent):
        if front_agent is None:
            return None
        return front_agent.position - self.position

    # ---------- Reasoning ----------
    def reason(self, distance):
        # observation
        if distance is not None and distance < 5:
            obs = "danger"
        else:
            obs = "move"

        # bounded memory (size = 3)
        self.memory.append(obs)
        if len(self.memory) > 3:
            self.memory.pop(0)

        danger = self.memory.count("danger")
        move = self.memory.count("move")

        if danger > move:
            if self.personality == "aggressive":
                action = "slow"
                thought = f"حافظه={self.memory} → خطر غالب، کاهش سرعت"
            else:
                action = "brake"
                thought = f"حافظه={self.memory} → خطر غالب، ترمز"
        else:
            action = "move"
            thought = f"حافظه={self.memory} → روند امن، حرکت"

        return action, thought

    # ---------- Action ----------
    def act(self, action, front_position=None):
        if action == "brake":
            self.speed = max(0, self.speed - 2)
        elif action == "slow":
            self.speed = max(0, self.speed - 1)
        elif action == "move":
            self.speed = min(5, self.speed + 1)

        new_position = self.position + self.speed

        # single-lane physical constraint
        if front_position is not None:
            new_position = min(new_position, front_position - 0.1)

        self.position = new_position
