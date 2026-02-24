from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.db import get_db
from datetime import timedelta
from typing import List
from core.models import User, Post
from schema.schema import Token, UserCreate, UserResponse, TokenData
from fastapi import Depends, FastAPI, APIRouter, HTTPException, status
from internal.user import get_password_hash, get_current_active_user, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, create_refresh_token, get_all_users
user_router = APIRouter(tags=["System"])


@user_router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Email tekshirish
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email allaqachon ro'yxatdan o'tgan")

    # Yangi foydalanuvchi
    hashed_password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        name=user.name,
        username = user.username,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user_router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@user_router.get("/users", response_model=List[UserResponse])
def get_user(db:Session = Depends(get_db)):
    users = get_all_users(db=db)

    return users


@user_router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Noto'g'ri email yoki parol",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires
    )
    refresh_token = create_refresh_token(
        data={"sub": user.email}
    )

    return {"refresh_token":refresh_token,  "access_token": access_token, "token_type": "bearer"}

