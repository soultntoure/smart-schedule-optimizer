from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....database import get_db
from ....schemas import SubjectCreate, Subject
from ....crud import subject as crud_subject

router = APIRouter()

@router.post("/", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return crud_subject.create_subject(db=db, subject=subject)

@router.get("/", response_model=list[Subject])
def read_subjects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subjects = crud_subject.get_subjects(db, skip=skip, limit=limit)
    return subjects
