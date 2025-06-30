from sqlalchemy.orm import Session
from .. import models, schemas

def get_preference(db: Session, preference_id: int):
    return db.query(models.Preference).filter(models.Preference.id == preference_id).first()

def get_preferences_by_user(db: Session, user_id: int):
    return db.query(models.Preference).filter(models.Preference.user_id == user_id).all()

def create_preference(db: Session, preference: schemas.PreferenceCreate):
    db_preference = models.Preference(**preference.model_dump())
    db.add(db_preference)
    db.commit()
    db.refresh(db_preference)
    return db_preference

def update_preference(db: Session, preference_id: int, preference: schemas.PreferenceUpdate):
    db_preference = db.query(models.Preference).filter(models.Preference.id == preference_id).first()
    if db_preference:
        for key, value in preference.model_dump(exclude_unset=True).items():
            setattr(db_preference, key, value)
        db.add(db_preference)
        db.commit()
        db.refresh(db_preference)
    return db_preference
