import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from core.dependency import get_current_user
from models.user import User

router = APIRouter(prefix="/uploads", tags=["Uploads"])

UPLOAD_DIR = Path("uploads")
ALLOWED = {"image/jpeg", "image/png", "image/webp", "image/gif"}
MAX_BYTES = 5 * 1024 * 1024

EXT = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif",
}


@router.post("/image")
async def upload_image(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    if file.content_type not in ALLOWED:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG, WEBP or GIF images are allowed",
        )

    data = await file.read()

    if len(data) > MAX_BYTES:
        raise HTTPException(status_code=400, detail="Image must be under 5MB")

    UPLOAD_DIR.mkdir(exist_ok=True)

    name = f"{uuid.uuid4().hex}{EXT[file.content_type]}"
    (UPLOAD_DIR / name).write_bytes(data)

    return {"url": f"/uploads/{name}"}