from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import TestDB
from app.schemas import TestDBCreate, TestDBResponse
from app.database import get_db

router = APIRouter(prefix="/test_db", tags=["test_db"])

@router.post("/",response_model=TestDBResponse)
def create_entry(entry: TestDBCreate, db : Session = Depends(get_db)):
    new_entry = TestDB(운용사명=entry.운용사명,
                       tickers=entry.tickers,
                       가격=entry.가격)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@router.get("/{운용사명}", response_model=list[TestDBResponse])
def read_entries(운용사명: str, db: Session = Depends(get_db)):
    entries = db.query(TestDB).filter(TestDB.운용사명.contains(운용사명)).all()
    if not entries:
        raise HTTPException(status_code=404, detail="No entries found")
    return entries

    