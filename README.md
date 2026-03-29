---
title: Incident Env
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# Incident Response OpenEnv

## Run Locally
uvicorn api.server:app --reload

## Endpoints
- /reset
- /step
- /state
- /auto-step
