from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.category import Category
from schemas.category import CategoryCreate
from repositories.category import (
    create_category,
    get_category_by_id,
    get_category_by_name,
    get_categories,
)


def create_category_service(db: Session, category: CategoryCreate):
    if get_category_by_name(db, category.name):
        raise HTTPException(status_code=409, detail="Category already exists")

    new_category = Category(name=category.name)

    return create_category(db, new_category)


def get_category_by_id_service(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


def get_categories_service(db: Session):
    return get_categories(db)
