from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    created_at: Optional[str]

class Channel(BaseModel):
    name: str
    description : str
    admin: int
    created_at: Optional[str]



