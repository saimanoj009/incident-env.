import random

class IncidentEnv:
    def __init__(self):
        self.state_data = None
        self.current_scenario = None
        self.history = []

    def reset(self):
        scenarios = [
            {
                "id": "easy",
                "logs": "High CPU usage detected",
                "metrics": {"cpu": 95, "memory": 60},
                "solution": ["analyze_logs", "restart_service"]
            },
            {
                "id": "medium",
                "logs": "Memory leak detected",
                "metrics": {"cpu": 60, "memory": 92},
                "solution": ["analyze_logs", "clear_cache", "restart_service"]
            },
            {
                "id": "hard",
                "logs": "Multiple failures: CPU + Memory",
                "metrics": {"cpu": 90, "memory": 90},
                "solution": ["analyze_logs", "scale_up", "clear_cache", "restart_service"]
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

        reward = 0
        done = False
        solution = self.current_scenario["solution"]

        if action not in solution:
            reward -= 0.3

        if len(self.history) <= len(solution) and action == solution[len(self.history)-1]:
            reward += 0.5
        else:
            reward -= 0.1

        if self.history == solution:
            reward += 1.0
            done = True

        if done and self.state_data["attempts"] <= len(solution):
            reward += 0.5

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