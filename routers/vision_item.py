from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.vision_item import VisionItemCreate, VisionItemResponse
from services.vision_item import (
    create_vision_item_service,
    get_vision_item_by_id_service,
    get_vision_items_service,
    get_vision_items_by_user_service,
    get_vision_items_by_category_service,
)

router = APIRouter(prefix="/vision-items", tags=["Vision Items"])


@router.post("/", response_model=VisionItemResponse)
def create_vision_item(vision_item: VisionItemCreate, db: Session = Depends(get_db)):
    return create_vision_item_service(db, vision_item, user_id=1)


@router.get("/{vision_item_id}", response_model=VisionItemResponse)
def get_vision_item(vision_item_id: int, db: Session = Depends(get_db)):
    return get_vision_item_by_id_service(db, vision_item_id)


@router.get("/", response_model=list[VisionItemResponse])
def get_vision_items(
    user_id: int | None = None,
    category_id: int | None = None,
    db: Session = Depends(get_db),
):
    if user_id:
        return get_vision_items_by_user_service(db, user_id)

    if category_id:
        return get_vision_items_by_category_service(db, category_id)

    return get_vision_items_service(db)
