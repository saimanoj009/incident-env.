import random

class IncidentEnv:
    def __init__(self):
        self.state_data = None
        self.history = []

    def reset(self):
        scenarios = [
            {
                "id": "easy",
                "logs": "Warning: CPU usage increased to 85%, monitoring required",
                "metrics": {"cpu": random.randint(80, 90), "memory": random.randint(50, 70)}
            },
            {
                "id": "medium",
                "logs": "Alert: Memory leak detected in backend service, usage above 90%",
                "metrics": {"cpu": random.randint(60, 80), "memory": random.randint(85, 95)}
            },
            {
                "id": "hard",
                "logs": "Critical Failure: CPU spike and memory overload detected simultaneously",
                "metrics": {"cpu": random.randint(85, 98), "memory": random.randint(85, 98)}
            }
        ]

        self.current_scenario = random.choice(scenarios)

        self.state_data = {
            "task_id": self.current_scenario["id"],
            "logs": self.current_scenario["logs"],
            "metrics": self.current_scenario["metrics"],
            "attempts": 0,
            "done": False,
            "history": []
        }

        self.history = []
        return self.state_data

    def step(self, action):
        self.state_data["attempts"] += 1
        self.history.append(action)

        cpu = self.state_data["metrics"]["cpu"]
        memory = self.state_data["metrics"]["memory"]

        reward = 0
        done = False

        # 🔥 Action-based logic (realistic system behavior)

        if action == "scale_down_cpu":
            if cpu > 80:
                self.state_data["metrics"]["cpu"] -= 30
                reward += 0.8
            else:
                reward -= 0.2

        elif action == "restart_service":
            if memory > 80:
                self.state_data["metrics"]["memory"] -= 40
                reward += 0.8
            else:
                reward -= 0.2

        elif action == "clear_cache":
            if memory > 70:
                self.state_data["metrics"]["memory"] -= 25
                reward += 0.6
            else:
                reward -= 0.1

        elif action == "analyze_logs":
            reward += 0.3

        elif action == "scale_up":
            if cpu > 75:
                self.state_data["metrics"]["cpu"] -= 20
                reward += 0.5
            else:
                reward -= 0.2

        elif action == "monitor":
            reward += 0.2

        else:
            reward -= 0.3

        if self.state_data["metrics"]["cpu"] < 60 and self.state_data["metrics"]["memory"] < 60:
            done = True
            reward += 1.0
        self.state_data["done"] = done
        self.state_data["history"] = self.history

        return {
            "state": self.state_data,
            "reward": round(reward, 3),
            "done": done,
            "message": f"Action '{action}' processed"
        }

    def state(self):
        return self.state_data
