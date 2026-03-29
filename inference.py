from env.incident_env import IncidentEnv
from agent import simple_agent

env = IncidentEnv()

def run():
    state = env.reset()
    
    while not state.get("done", False):
        action = simple_agent(state)
        state, reward, done, info = env.step(action)
    
    return state