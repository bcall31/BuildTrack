from fastapi.security import OAuth2PasswordBearer #type: ignore
from fastapi import Depends, HTTPException, status # type: ignore
from core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload["sub"]

