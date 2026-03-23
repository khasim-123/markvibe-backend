from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user_service import create_user, get_users

router = APIRouter()

@router.post("/users")
def create(user: UserCreate):
    return create_user(user)

@router.get("/users")
def read_users():
    return get_users()