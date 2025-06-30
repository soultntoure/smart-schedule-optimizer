from sqlalchemy.orm import Session
from .. import models, schemas

def get_schedule(db: Session, schedule_id: int):
    return db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()

def get_schedules_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Schedule).filter(models.Schedule.user_id == user_id).offset(skip).limit(limit).all()

def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(**schedule.model_dump())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule
