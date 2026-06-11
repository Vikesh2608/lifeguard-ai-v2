from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LifeGuard AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "LifeGuard AI Backend Running"
    }

@app.get("/mental-health")
def mental_health():
    return {
        "status": "healthy",
        "message": "Mental Health Module Active"
    }

@app.get("/elder-safety")
def elder_safety():
    return {
        "status": "active",
        "message": "Elder Safety Monitoring Active"
    }

@app.get("/family-safety")
def family_safety():
    return {
        "status": "active",
        "message": "Family Safety Center Active"
    }
