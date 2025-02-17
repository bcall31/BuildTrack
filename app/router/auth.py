from fastapi import APIRouter, Depends #type: ignore
from core.auth import get_current_user

router = APIRouter()

@router.get("/token/")
def get_user(user: str = Depends(get_current_user)):
    return user