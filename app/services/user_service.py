from app.models.user import User
from app.db.session import SessionLocal

def create_user(user_data):
    db = SessionLocal()
    user = User(name=user_data.name, email=user_data.email,number=user_data.number,address=user_data.address,flattype=user_data.flattype,budget=user_data.budget)

    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()

    return user

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users