from fastapi import APIRouter, Response, Depends #type: ignore
from sqlalchemy.orm import Session #type: ignore
from core.db import get_db
from schemas.users import UserCreate, UserLogin, UserLogout
from services.users import register_user, login_user, logout_user

router = APIRouter()

@router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user, db)

@router.post("/login/")
def login(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    return login_user(user, response, db)

@router.post("/logout/")
def logout(response: Response):
    return logout_user(response)

