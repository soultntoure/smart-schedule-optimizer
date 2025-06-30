from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List, Dict, Any

# User Schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}

# Subject Schemas
class SubjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int

    model_config = {"from_attributes": True}

# Task Schemas
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    estimated_time_minutes: int = Field(..., gt=0)
    difficulty: int = Field(..., ge=1, le=5)
    priority: int = Field(..., ge=1, le=5)
    subject_id: Optional[int] = None

class TaskCreate(TaskBase):
    owner_id: int # In a real app, this would be inferred from auth

class Task(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = {"from_attributes": True}

# Schedule Schemas
class ScheduleBlock(BaseModel):
    type: str # e.g., 'study', 'break', 'extracurricular'
    start_time: datetime
    end_time: datetime
    task_id: Optional[int] = None # For study blocks
    subject_id: Optional[int] = None # For study blocks
    description: Optional[str] = None

class ScheduleBase(BaseModel):
    date: datetime
    schedule_data: List[ScheduleBlock] # The optimized blocks

class ScheduleCreate(ScheduleBase):
    user_id: int # In a real app, inferred from auth
    # Additional fields needed for generation logic might go here, e.g., available_hours_start, available_hours_end

class Schedule(ScheduleBase):
    id: int
    user_id: int
    generated_at: datetime

    model_config = {"from_attributes": True}

# Preference Schemas
class PreferenceBase(BaseModel):
    key: str
    value: str

class PreferenceCreate(PreferenceBase):
    user_id: int

class PreferenceUpdate(BaseModel):
    value: str

class Preference(PreferenceBase):
    id: int
    user_id: int

    model_config = {"from_attributes": True}
