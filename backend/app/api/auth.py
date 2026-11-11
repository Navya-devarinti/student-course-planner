from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import create_access_token
from app.database import get_db
from app.models.user import User
from app.schemas.auth import UserLogin, UserRegister
from app.security import hash_password, verify_password


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered."
        )

    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        role="student",
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(
        data={
            "user_id": new_user.id,
            "role": new_user.role
        }
    )

    return {
        "message": "Student registered successfully.",
        "user_id": new_user.id,
        "full_name": new_user.full_name,
        "email": new_user.email,
        "role": new_user.role,
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/login", response_model=dict)
def login_user(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if not user or not verify_password(
        user_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive."
        )

    access_token = create_access_token(
        data={
            "user_id": user.id,
            "role": user.role
        }
    )

    return {
        "message": "Login successful.",
        "user_id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "role": user.role,
        "access_token": access_token,
        "token_type": "bearer"
    }
