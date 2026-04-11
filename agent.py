def simple_agent(state):
    cpu = state.get("metrics", {}).get("cpu", 0)
    memory = state.get("metrics", {}).get("memory", 0)
    logs = state.get("logs", "").lower()

    # Intelligent decision making
    if cpu > 90:
        return "scale_down_cpu"

    elif memory > 90:
        return "restart_service"

    elif "memory leak" in logs:
        return "clear_memory"

    elif "cpu spike" in logs:
        return "optimize_process"

    elif cpu > 70 and memory > 70:
        return "balance_load"

    elif "error" in logs:
        return "analyze_logs"

    else:
        return "monitor"
