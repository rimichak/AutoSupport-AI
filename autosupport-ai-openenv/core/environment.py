from core.rewards import calculate_reward
from core.state_manager import update_state


class SupportEnv:
    def __init__(self):
        self.state_data = None

    def reset(self, task):
        self.state_data = {
            "ticket": task["ticket"],
            "status": "open",
            "history": [],
            "customer_mood": task["customer_mood"],
            "order_status": task["order_status"],
            "time_left": 3
        }
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        self.state_data = update_state(self.state_data, action)
        self.state_data["history"].append(action)

        reward = calculate_reward(self.state_data, action)

        self.state_data["time_left"] -= 1

        done = False

        if self.state_data["status"] in ["closed", "escalated"]:
            done = True

        if self.state_data["time_left"] <= 0:
            done = True
            reward -= 0.5

        return self.state(), reward, done