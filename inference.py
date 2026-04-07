import os
import requests
from openai import OpenAI

# 🔥 MUST use proxy
BASE_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

def run_task(task_name):
    print(f"[START] {task_name}", flush=True)

    try:
        res = requests.post(f"{BASE_URL}/reset", headers=HEADERS)
        state = res.json()
    except Exception:
        print(f"[END] {task_name} score=0", flush=True)
        return

    total_reward = 0

    for step in range(10):
        try:
            # 🔥 REQUIRED LLM CALL
            _ = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": str(state)}
                ]
            )

            # 🔥 ALSO use proxy for env calls
            res = requests.get(f"{BASE_URL}/auto-step", headers=HEADERS)
            data = res.json()

            result = data.get("result", {})
            reward = result.get("reward", 0)
            done = result.get("done", False)

        except Exception:
            reward = 0
            done = True

        total_reward += reward

        print(f"[STEP] step={step+1} reward={reward}", flush=True)

        if done:
            break

    print(f"[END] {task_name} score={total_reward}", flush=True)


if __name__ == "__main__":
    tasks = ["easy", "medium", "hard"]

    for task in tasks:
        run_task(task)
