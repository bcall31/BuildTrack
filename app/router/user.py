from fastapi import APIRouter, Depends #type: ignore
from sqlalchemy.orm import Session #type: ignore
from core.auth import get_current_user
from schemas.users import UserCreate
from core.db import get_db
from services.users import get_user, update_user, delete_user



router = APIRouter()

@router.get("/user/")
def get(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_user(user, db)

@router.post("/user/")
def update(data: UserCreate, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return update_user(user, db)

@router.delete("/user/")    
def delete(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    return delete_user(user, db)