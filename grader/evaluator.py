def evaluate(actions, solution):
    correct_steps = 0

    for i, act in enumerate(actions):
        if i < len(solution) and act == solution[i]:
            correct_steps += 1

    return round(correct_steps / len(solution), 2)