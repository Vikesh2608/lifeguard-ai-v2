from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class MoodCreate(BaseModel):
    email: str
    mood: str
    notes: str = ""


class SleepCreate(BaseModel):
    email: str
    sleep_hours: int


class ContactCreate(BaseModel):
    email: str
    contact_name: str
    contact_phone: str
    relationship: str


class SOSRequest(BaseModel):
    email: str
    latitude: float
    longitude: float
