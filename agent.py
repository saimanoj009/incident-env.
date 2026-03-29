def simple_agent(state):
    logs = state["logs"].lower()

    if "cpu" in logs:
        return "restart_service"
    elif "memory" in logs:
        return "clear_cache"
    else:
        return "analyze_logs"