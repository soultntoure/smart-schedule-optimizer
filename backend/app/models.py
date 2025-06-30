from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    tasks = relationship("Task", back_populates="owner")
    schedules = relationship("Schedule", back_populates="user")
    preferences = relationship("Preference", back_populates="user")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    estimated_time_minutes = Column(Integer)
    difficulty = Column(Integer) # 1-5 scale
    priority = Column(Integer) # 1-5 scale
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())

    owner = relationship("User", back_populates="tasks")
    subject = relationship("Subject")

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, index=True) # Date for which the schedule is generated
    schedule_data = Column(JSON) # Stores the intelligent schedule structure (e.g., blocks, tasks, breaks)
    generated_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="schedules")

class Preference(Base):
    __tablename__ = "preferences"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    key = Column(String, index=True) # e.g., 'morning_focus_subject', 'preferred_break_duration'
    value = Column(String) # e.g., 'math', '15_minutes'
    # Potentially add a 'type' column for validation (e.g., 'enum', 'int', 'bool')

    user = relationship("User", back_populates="preferences")
