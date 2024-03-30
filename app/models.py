from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    email: str
    password: str

class Note(BaseModel):
    title: str
    content: str
