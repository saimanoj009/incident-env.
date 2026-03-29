from fastapi import FastAPI
from pydantic import BaseModel
from env.incident_env import IncidentEnv
from agent import simple_agent

app = FastAPI()
env = IncidentEnv()

class Action(BaseModel):
    action: str

@app.get("/")
def home():
    return {"message": "Incident Response OpenEnv Running"}

@app.get("/reset")
@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    return env.step(action.action)

@app.get("/state")
def get_state():
    return env.state()

@app.get("/auto-step")
def auto_step():
    state = env.state()
    action = simple_agent(state)
    result = env.step(action)

    return {
        "action": action,
        "result": result
    }
