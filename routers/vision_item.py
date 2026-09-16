from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.dependency import get_current_user
from database import get_db
from models.user import User
from schemas.vision_item import (
    VisionItemCreate,
    VisionItemUpdate,
    VisionItemResponse,
)
from services.vision_item import (
    create_vision_item_service,
    get_vision_item_by_id_service,
    get_vision_items_by_user_service,
    get_vision_items_by_category_service,
    update_vision_item_service,
    delete_vision_item_service,
)

router = APIRouter(prefix="/vision-items", tags=["Vision Items"])


@router.post("/", response_model=VisionItemResponse, status_code=201)
def create_vision_item(
    vision_item: VisionItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_vision_item_service(db, vision_item, current_user.id)


@router.get("/", response_model=list[VisionItemResponse])
def get_vision_items(
    category_id: int | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if category_id:
        return get_vision_items_by_category_service(db, category_id)

    return get_vision_items_by_user_service(db, current_user.id)


@router.get("/{vision_item_id}", response_model=VisionItemResponse)
def get_vision_item(
    vision_item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_vision_item_by_id_service(db, vision_item_id)


@router.patch("/{vision_item_id}", response_model=VisionItemResponse)
def update_vision_item(
    vision_item_id: int,
    data: VisionItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_vision_item_service(db, vision_item_id, data, current_user.id)


@router.delete("/{vision_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vision_item(
    vision_item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    delete_vision_item_service(db, vision_item_id, current_user.id)
