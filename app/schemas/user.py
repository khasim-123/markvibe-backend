from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    number: str
    address: Optional[str] = None
    flattype: str
    budget: Optional[int] = None      


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True