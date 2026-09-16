from fastapi import HTTPException
from sqlalchemy.orm import Session

from core.security import hash_password, verify_password
from models.user import User
from schemas.user import UserCreate
from repositories.user import (
    create_user,
    get_user_by_id,
    get_user_by_email,
    get_users,
)


def create_user_service(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=409, detail="Email already registered")

    new_user = User(
        name=user.name, email=user.email, password=hash_password(user.password)
    )

    return create_user(db, new_user)


def authenticate_user_service(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    return user


def get_user_by_id_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def get_users_service(db: Session):
    return get_users(db)
