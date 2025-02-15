from fastapi import HTTPException, status #type: ignore
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
    

def login_user(user: UserLogin, db: Session):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if not existing_user or not verify_password(user.password, existing_user.hashedpassword):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": existing_user.email})
    return {"access_token": token, "token_type": "bearer"}




    

