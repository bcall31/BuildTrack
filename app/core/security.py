from fastapi import HTTPException, status #type: ignore
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from core.config import SECRET_KEY

ALGORITHM = "HS256"

def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashedpassword: str):
    return bcrypt.checkpw(password.encode(), hashedpassword.encode())

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.now(timezone.utc) + expires_delta})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        print("🔹 Decoding token:", token)  # Debugging
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("🔹 Decoded payload:", payload)  # Debugging

        exp = payload.get("exp")
        if exp and datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc):
            raise HTTPException(status_code=401, detail="Token has expired")

        return payload

    except jwt.ExpiredSignatureError:
        print("🔹 Token expired")  # Debugging
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        print("🔹 Invalid token")  # Debugging
        raise HTTPException(status_code=401, detail="Invalid token")

