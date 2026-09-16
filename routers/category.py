from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.dependency import get_current_user
from database import get_db
from models.user import User
from schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from services.category import (
    create_category_service,
    get_owned_category,
    get_categories_service,
    update_category_service,
    delete_category_service,
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_category_service(db, category, current_user.id)


@router.get("/", response_model=list[CategoryResponse])
def get_categories(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return get_categories_service(db, current_user.id)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_owned_category(db, category_id, current_user.id)


@router.patch("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_category_service(db, category_id, data, current_user.id)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_category_service(db, category_id, current_user.id)
