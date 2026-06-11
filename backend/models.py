from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String)
    last_name = Column(String)

    email = Column(
        String,
        unique=True,
        index=True
    )

    password = Column(String)


class Mood(Base):
    __tablename__ = "moods"

    id = Column(Integer, primary_key=True)

    email = Column(String)

    mood = Column(String)

    notes = Column(String)


class Sleep(Base):
    __tablename__ = "sleep"

    id = Column(Integer, primary_key=True)

    email = Column(String)

    sleep_hours = Column(Integer)


class EmergencyContact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)

    email = Column(String)

    contact_name = Column(String)

    contact_phone = Column(String)

    relationship = Column(String)
