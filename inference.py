import requests

BASE_URL = "https://saimanoj1405-incident-env.hf.space"

def run_task(task_name):
    print(f"[START] {task_name}", flush=True)

    # Reset environment (POST required)
    res = requests.post(f"{BASE_URL}/reset")
    state = res.json()

    total_reward = 0

    for step in range(10):
        # Auto agent step
        res = requests.get(f"{BASE_URL}/auto-step")
        data = res.json()

        result = data.get("result", {})
        reward = result.get("reward", 0)
        done = result.get("done", False)

        total_reward += reward

        print(f"[STEP] step={step+1} reward={reward}", flush=True)

        if done:
            break

    print(f"[END] {task_name} score={total_reward}", flush=True)


if __name__ == "__main__":
    tasks = ["easy", "medium", "hard"]

    for task in tasks:
        run_task(task)
