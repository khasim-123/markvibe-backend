from app.db.session import engine
from app.db.base import Base

# 👇 VERY IMPORTANT (force import)
from app.models.user import User  

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done ✅")

if __name__ == "__main__":
    init_db()