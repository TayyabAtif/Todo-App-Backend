from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from user_controller.signup_service import signup_user
from user_controller.auth_service import authenticate_user
from typing import Optional
from fastapi import Header

router = APIRouter()

# Temporary in-memory token store for demo
tokens = {}

@router.post("/signup")
async def signup(form_data: OAuth2PasswordRequestForm = Depends()):
    return await signup_user(form_data.username, form_data.password)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    # We'll use username as a token (not safe, just for learning)
    tokens[user["username"]] = True
    return {"access_token": user["username"], "token_type": "bearer"}

def get_current_user(token: Optional[str] = Header(None, alias="Authorization")):
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token missing or invalid")
    
    token_value = token.split(" ")[1]
    if token_value not in tokens:
        raise HTTPException(status_code=401, detail="Invalid token")

    return token_value

@router.get("/profile")
async def get_profile(user=Depends(get_current_user)):
    return {"message": f"Hello {user}, this is your profile"}
