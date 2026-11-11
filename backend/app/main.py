from fastapi import FastAPI, Depends

from app.api.auth import router as auth_router
from app.dependencies import get_current_user


app = FastAPI(
    title="Student Course Planner",
    description="A university degree planning and course scheduling system",
    version="1.0.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Student Course Planner!",
        "status": "Application is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/auth/me")
def get_my_profile(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Authenticated user",
        "user": current_user
    }
