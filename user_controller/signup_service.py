from infra_structure.db import db
from fastapi import HTTPException
from passlib.hash import bcrypt
from pymongo.errors import DuplicateKeyError

async def signup_user(username: str, password: str):
    user_collection = db["users"]
    existing_user = await user_collection.find_one({"username": username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = bcrypt.hash(password)
    user = {"username": username, "password": hashed_password}
    await user_collection.insert_one(user)
    return {"message": "User registered successfully"}
