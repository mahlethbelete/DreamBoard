from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.category import CategoryCreate, CategoryResponse
from services.category import (
    create_category_service,
    get_category_by_id_service,
    get_categories_service,
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category_service(db, category)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return get_category_by_id_service(db, category_id)


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return get_categories_service(db)
