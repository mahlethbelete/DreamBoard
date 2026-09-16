from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.dependency import get_current_user
from core.security import create_access_token
from database import get_db
from models.user import User
from schemas.user import UserResponse, Token
from services.user import authenticate_user_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user_service(
        db,
        form_data.username,
        form_data.password
    )

    return Token(access_token=create_access_token(user.id))


@router.get("/me", response_model=UserResponse)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user