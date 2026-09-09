from sqlalchemy import Column, Integer, String, Boolean, Text
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    password_hash = Column(String(255), nullable=False)
    score = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

class Dialogue(Base):
    __tablename__ = "dialogues"

    id = Column(Integer, primary_key=True, index=True)
    dialogue_text = Column(Text, nullable=False)
    option_accept = Column(String(255), nullable=False)
    option_decline = Column(String(255), nullable=False)
    correct_answer = Column(String(50), nullable=False)
    explanation = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)