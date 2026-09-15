from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.vision_item import VisionItem
from schemas.vision_item import VisionItemCreate
from repositories.category import get_category_by_id
from repositories.vision_item import (
    create_vision_item,
    get_vision_item_by_id,
    get_vision_items,
    get_vision_items_by_user,
    get_vision_items_by_category,
)


def create_vision_item_service(
    db: Session, vision_item: VisionItemCreate, user_id: int
):
    if not get_category_by_id(db, vision_item.category_id):
        raise HTTPException(status_code=404, detail="Category not found")

    new_vision_item = VisionItem(
        user_id=user_id,
        category_id=vision_item.category_id,
        title=vision_item.title,
        description=vision_item.description,
        image_url=vision_item.image_url,
        target_date=vision_item.target_date,
        status=vision_item.status,
    )

    return create_vision_item(db, new_vision_item)


def get_vision_item_by_id_service(db: Session, vision_item_id: int):
    item = get_vision_item_by_id(db, vision_item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Vision item not found")

    return item


def get_vision_items_service(db: Session):
    return get_vision_items(db)


def get_vision_items_by_user_service(db: Session, user_id: int):
    return get_vision_items_by_user(db, user_id)


def get_vision_items_by_category_service(db: Session, category_id: int):
    return get_vision_items_by_category(db, category_id)
