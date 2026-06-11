from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal
from database import engine

import models
import schemas

app = FastAPI(
    title="LifeGuard AI"
)
@app.get("/vikesh-test")
def vikesh_test():
    return {
        "status": "SUCCESS",
        "message": "This is the REAL backend/main.py"
    }

models.Base.metadata.create_all(
    bind=engine
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "VIKESH TEST VERSION 999"
    }


@app.post("/register")
def register_user(
    user: schemas.UserCreate
):
    db = SessionLocal()

    new_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User Registered Successfully"
    }


@app.post("/mood")
def save_mood(
    mood: schemas.MoodCreate
):
    db = SessionLocal()

    new_mood = models.Mood(
        email=mood.email,
        mood=mood.mood,
        notes=mood.notes
    )

    db.add(new_mood)
    db.commit()

    return {
        "message": "Mood Saved"
    }


@app.post("/sleep")
def save_sleep(
    sleep: schemas.SleepCreate
):
    db = SessionLocal()

    new_sleep = models.Sleep(
        email=sleep.email,
        sleep_hours=sleep.sleep_hours
    )

    db.add(new_sleep)
    db.commit()

    return {
        "message": "Sleep Saved"
    }


@app.post("/emergency-contact")
def save_contact(
    contact: schemas.ContactCreate
):
    db = SessionLocal()

    new_contact = models.EmergencyContact(
        email=contact.email,
        contact_name=contact.contact_name,
        contact_phone=contact.contact_phone,
        relationship=contact.relationship
    )

    db.add(new_contact)
    db.commit()

    return {
        "message": "Emergency Contact Saved"
    }


@app.get("/wellness-score/{email}")
def wellness_score(
    email: str
):
    db = SessionLocal()

    mood_count = (
        db.query(models.Mood)
        .filter(models.Mood.email == email)
        .count()
    )

    sleep_count = (
        db.query(models.Sleep)
        .filter(models.Sleep.email == email)
        .count()
    )

    score = 50

    score += mood_count * 10
    score += sleep_count * 10

    if score > 100:
        score = 100

    return {
        "email": email,
        "wellness_score": score
    }


@app.post("/sos")
def emergency_sos(
    request: schemas.SOSRequest
):
    return {
        "status": "SOS Activated",
        "email": request.email,
        "latitude": request.latitude,
        "longitude": request.longitude,
        "zipcode": "45231"
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


@app.get("/ai-assistant")
def ai_assistant(
    question: str
):
    q = question.lower()

    if "stress" in q:
        return {
            "response":
            "Take a walk, hydrate and practice deep breathing."
        }

    if "sleep" in q:
        return {
            "response":
            "Aim for 7-8 hours of quality sleep."
        }

    return {
        "response":
        "LifeGuard AI recommends maintaining healthy daily habits."
    }
