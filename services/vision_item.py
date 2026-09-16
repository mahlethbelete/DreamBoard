from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.vision_item import VisionItem
from schemas.vision_item import VisionItemCreate, VisionItemUpdate
from services.category import get_owned_category
from repositories.vision_item import (
    create_vision_item,
    get_vision_item_by_id,
    get_vision_items,
    get_vision_items_by_user,
    get_vision_items_by_category,
    update_vision_item,
    delete_vision_item,
)


def create_vision_item_service(
    db: Session, vision_item: VisionItemCreate, user_id: int
):
    get_owned_category(db, vision_item.category_id, user_id)

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


def get_owned_vision_item(db: Session, vision_item_id: int, user_id: int):
    item = get_vision_item_by_id_service(db, vision_item_id)

    if item.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not your vision item")

    return item


def update_vision_item_service(
    db: Session, vision_item_id: int, data: VisionItemUpdate, user_id: int
):
    item = get_owned_vision_item(db, vision_item_id, user_id)

    changes = data.model_dump(exclude_unset=True)

    if "category_id" in changes:
        get_owned_category(db, changes["category_id"], user_id)

    return update_vision_item(db, item, changes)


def delete_vision_item_service(db: Session, vision_item_id: int, user_id: int):
    item = get_owned_vision_item(db, vision_item_id, user_id)

    delete_vision_item(db, item)


def get_vision_items_service(db: Session):
    return get_vision_items(db)


def get_vision_items_by_user_service(db: Session, user_id: int):
    return get_vision_items_by_user(db, user_id)


def get_vision_items_by_category_service(db: Session, category_id: int):
    return get_vision_items_by_category(db, category_id)
