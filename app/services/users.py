from fastapi import HTTPException, Response, status #type: ignore
from fastapi.responses import JSONResponse #type: ignore
from sqlalchemy.orm import Session #type: ignore
from models.users import User
from schemas.users import UserCreate, UserLogout, UserLogin
from core.security import hash_password, verify_password, create_access_token

def register_user(user: UserCreate, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    try:
        new_user = User(email=user.email, username=user.username, hashedpassword=hash_password(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        result = login_user(new_user, db)
        return {"message": "User created and logged in successfully: ", "result": result}
    except Exception as e:
        return {"error": str(e)}
    

def login_user(user: UserLogin, response: Response, db: Session):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user or not verify_password(user.password, existing_user.hashedpassword):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": existing_user.email})
    response.set_cookie(key="access_token", value=token, httponly=True, secure=True, samesite="Strict")
    return {"access_token": token, "token_type": "Bearer"}

def logout_user(response: Response):
    response.delete_cookie(key="access_token", httponly=True, secure=True, samesite="Strict")
    return {"message": "User logged out"}

def get_user(user: dict, db: Session):
    email = user["sub"]
    existing_user = db.query(User).filter(User.email == email).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return existing_user

def delete_user(user: dict, db: Session):
    email = user["sub"]
    existing_user = db.query(User).filter(User.email == email).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(existing_user)
    db.commit()
    return {"message": "User deleted"}

def update_user(data: UserCreate, user: dict, db: Session):
    email = user["sub"]
    existing_user = db.query(User).filter(User.email == email).first()
    if data.username:
        existing_user.username = data.username
    if data.email:
        existing_user.email = data.email
    if data.password:
        existing_user.hashedpassword = hash_password(data.password)
    db.commit()
        
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return existing_user



    

