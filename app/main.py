from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.user import router as user_router

app = FastAPI()

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # your React app
    allow_credentials=True,
    allow_methods=["*"],   # IMPORTANT (enables OPTIONS)
    allow_headers=["*"],
)

# existing router
app.include_router(user_router)