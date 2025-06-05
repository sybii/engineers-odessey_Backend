from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Engineers Odyssey – Realm of Control API",
    version="0.1.0"
)

# allow the JS frontend on http://localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class PIDInput(BaseModel):
    kp: float
    ki: float
    kd: float

@app.post("/control-system/pid-evaluate")
def evaluate_pid(data: PIDInput):
    """Return a score out of 100 and pass/fail flag."""
    score = 0
    if 1.5 < data.kp < 3.0:
        score += 30
    if 0.5 < data.ki < 1.5:
        score += 30
    if 0.1 < data.kd < 0.7:
        score += 40
    return {"score": score, "level_passed": score >= 80}
