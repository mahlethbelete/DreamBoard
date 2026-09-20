from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.dependency import get_current_user
from database import get_db
from models.user import User
from schemas.ai import SuggestRequest, SuggestResponse
from services.ai import suggest_items_service
from services.category import get_owned_category

router = APIRouter(prefix="/ai", tags=["AI"])


@router.post("/suggest", response_model=SuggestResponse)
def suggest(
    body: SuggestRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    category = get_owned_category(db, body.category_id, current_user.id)

    return SuggestResponse(
        suggestions=suggest_items_service(body.prompt, category.name)
    )