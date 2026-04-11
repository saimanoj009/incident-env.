def simple_agent(state):
    cpu = state.get("metrics", {}).get("cpu", 0)
    memory = state.get("metrics", {}).get("memory", 0)
    logs = state.get("logs", "").lower()
    history = state.get("history", [])
    last_action = history[-1] if history else None

    if cpu > 90 and last_action != "scale_down_cpu":
        return "scale_down_cpu"

    elif memory > 90 and last_action != "restart_service":
        return "restart_service"

    elif "memory leak" in logs and last_action != "clear_cache":
        return "clear_cache"

    elif cpu > 80 and last_action != "scale_up":
        return "scale_up"

    elif cpu > 70 and memory > 70:
        return "scale_down_cpu"

    elif "error" in logs:
        return "analyze_logs"

    else:
        return "monitor"
