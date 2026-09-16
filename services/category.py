from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.category import Category
from schemas.category import CategoryCreate, CategoryUpdate
from repositories.category import (
    create_category,
    get_category_by_id,
    get_category_by_name,
    get_categories_by_user,
    update_category,
    delete_category,
)


def create_category_service(db: Session, category: CategoryCreate, user_id: int):
    if get_category_by_name(db, user_id, category.name):
        raise HTTPException(status_code=409, detail="Category already exists")

    new_category = Category(user_id=user_id, name=category.name)

    return create_category(db, new_category)


def get_owned_category(db: Session, category_id: int, user_id: int):
    category = get_category_by_id(db, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    if category.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not your category")

    return category


def get_categories_service(db: Session, user_id: int):
    return get_categories_by_user(db, user_id)


def update_category_service(
    db: Session, category_id: int, data: CategoryUpdate, user_id: int
):
    category = get_owned_category(db, category_id, user_id)

    existing = get_category_by_name(db, user_id, data.name)

    if existing and existing.id != category_id:
        raise HTTPException(status_code=409, detail="Category already exists")

    return update_category(db, category, data.model_dump(exclude_unset=True))


def delete_category_service(db: Session, category_id: int, user_id: int):
    category = get_owned_category(db, category_id, user_id)

    delete_category(db, category)
