from infra_structure.db import db
from fastapi import HTTPException
from passlib.hash import bcrypt

async def authenticate_user(username: str, password: str):
    user_collection = db["users"]
    user = await user_collection.find_one({"username": username})
    if not user or not bcrypt.verify(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user
