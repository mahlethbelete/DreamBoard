from fastapi import APIRouter, Depends, Query

from core.dependency import get_current_user
from models.user import User
from schemas.images import ImageSearchResponse
from services.images import search_images_service

router = APIRouter(prefix="/images", tags=["Images"])


@router.get("/search", response_model=ImageSearchResponse)
def search_images(
    q: str = Query(min_length=2, max_length=80),
    current_user: User = Depends(get_current_user),
):
    return ImageSearchResponse(results=search_images_service(q))