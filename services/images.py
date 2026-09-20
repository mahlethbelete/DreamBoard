import httpx
from fastapi import HTTPException

from core.config import PEXELS_API_KEY
from schemas.images import ImageResult

ENDPOINT = "https://api.pexels.com/v1/search"


def search_images_service(query: str) -> list[ImageResult]:
    if not PEXELS_API_KEY:
        raise HTTPException(status_code=503, detail="Image search is not configured")

    try:
        res = httpx.get(
            ENDPOINT,
            headers={"Authorization": PEXELS_API_KEY},
            params={"query": query, "per_page": 12, "orientation": "portrait"},
            timeout=10,
        )
        res.raise_for_status()
        data = res.json()
    except Exception:
        raise HTTPException(status_code=502, detail="Could not reach the image service")

    return [
        ImageResult(
            url=p["src"]["large"],
            thumb=p["src"]["tiny"],
            alt=p.get("alt") or query,
        )
        for p in data.get("photos", [])
    ]