from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    number: str
    address: str = None
    flattype: str
    budget: int = None      
    

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True