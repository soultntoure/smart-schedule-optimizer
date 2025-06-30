from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....database import get_db
from ....schemas import PreferenceCreate, PreferenceUpdate, Preference
from ....crud import preference as crud_preference

router = APIRouter()

@router.post("/", response_model=Preference)
def create_preference(preference: PreferenceCreate, db: Session = Depends(get_db)):
    return crud_preference.create_preference(db=db, preference=preference)

@router.get("/user/{user_id}", response_model=list[Preference])
def read_user_preferences(user_id: int, db: Session = Depends(get_db)):
    preferences = crud_preference.get_preferences_by_user(db, user_id=user_id)
    if not preferences:
        raise HTTPException(status_code=404, detail="Preferences not found for this user")
    return preferences

@router.put("/{preference_id}", response_model=Preference)
def update_preference(preference_id: int, preference: PreferenceUpdate, db: Session = Depends(get_db)):
    db_preference = crud_preference.update_preference(db, preference_id=preference_id, preference=preference)
    if not db_preference:
        raise HTTPException(status_code=404, detail="Preference not found")
    return db_preference
