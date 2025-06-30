from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ....database import get_db
from ....schemas import UserCreate, User
from ....crud import user as crud_user
from ....core.security import get_password_hash

router = APIRouter()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    return crud_user.create_user(db=db, user=user.model_dump(), hashed_password=hashed_password)

# Placeholder for other user endpoints (e.g., get_current_user, login)
