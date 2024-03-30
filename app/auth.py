from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from .models import User
from .db import database
from pydantic import BaseModel
from .authkey import create_access_token

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup/")
async def signup(user: User):
    hashed_password = pwd_context.hash(user.password)
    user_obj = {"username": user.username, "email": user.email, "password": hashed_password}
    await database.users.insert_one(user_obj)
    return {"message": "User registered successfully"}

class UserInLogin(BaseModel):
    email: str
    password: str

@router.post("/login/")
async def login(user_data: UserInLogin):
    user = await database.users.find_one({"email": user_data.email})
    if not user or not pwd_context.verify(user_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_access_token(data={"email": user_data.email})
    return {"access_token": access_token, "token_type": "bearer"}
