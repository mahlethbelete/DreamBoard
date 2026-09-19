from sqlalchemy.orm import Session

from models.vision_item import VisionItem


def create_vision_item(db: Session, vision_item: VisionItem):
    db.add(vision_item)
    db.commit()
    db.refresh(vision_item)

    return vision_item


def get_vision_item_by_id(db: Session, vision_item_id: int):
    return db.query(VisionItem).filter(VisionItem.id == vision_item_id).first()


def get_vision_items_by_user(db: Session, user_id: int):
    return (
        db.query(VisionItem)
        .filter(VisionItem.user_id == user_id)
        .order_by(VisionItem.created_at.desc())
        .all()
    )


def get_vision_items_by_category(db: Session, category_id: int):
    return (
        db.query(VisionItem)
        .filter(VisionItem.category_id == category_id)
        .order_by(VisionItem.created_at.desc())
        .all()
    )


def get_vision_items(db: Session):
    return db.query(VisionItem).order_by(VisionItem.created_at.desc()).all()


def update_vision_item(db: Session, vision_item: VisionItem, data: dict):
    for field, value in data.items():
        setattr(vision_item, field, value)

    db.commit()
    db.refresh(vision_item)

    return vision_item


def delete_vision_item(db: Session, vision_item: VisionItem):
    db.delete(vision_item)
    db.commit()
