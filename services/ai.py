import json

from fastapi import HTTPException
from google import genai

from core.config import GEMINI_API_KEY
from schemas.ai import Suggestion

SYSTEM = """You help people fill a personal vision board.
Given a goal area, return 6 concrete, specific things someone might want.
Each needs a short title (under 8 words) and one sentence of description.
Return ONLY a JSON array, no markdown, no preamble:
[{"title": "...", "description": "..."}]"""


def suggest_items_service(prompt: str, category_name: str) -> list[Suggestion]:
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=503, detail="AI is not configured")

    client = genai.Client(api_key=GEMINI_API_KEY)

    try:
        result = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"{SYSTEM}\n\nCategory: {category_name}\nThey said: {prompt}",
        )
        text = result.text.strip()
    except Exception:
        raise HTTPException(status_code=502, detail="Could not reach the AI")
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]

    try:
        data = json.loads(text.strip())
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="AI returned something unusable")

    return [
        Suggestion(title=str(d["title"])[:100], description=str(d["description"])[:300])
        for d in data
        if isinstance(d, dict) and "title" in d and "description" in d
    ][:6]
