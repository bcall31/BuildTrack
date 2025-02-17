from fastapi.security import OAuth2PasswordBearer #type: ignore
from fastapi import Depends, HTTPException, Request, status # type: ignore
from core.security import decode_token

def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    # Decode the token (ensure it's valid and not expired)
    payload = decode_token(token)
    print(" 🔹 Payload:", payload)
    return payload

