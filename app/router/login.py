from fastapi import APIRouter, Depends #type: ignore
from sqlalchemy.orm import Session 
from core.db import get_db
from schemas.users import UserCreate, UserLogin, UserLogout
from services.users import register_user, login_user

router = APIRouter()

@router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)

@router.post("/logout/")
def logout(user: UserLogout, db: Session = Depends(get_db)):
    return 