from pydantic import BaseModel


class ImageResult(BaseModel):
    url: str
    thumb: str
    alt: str


class ImageSearchResponse(BaseModel):
    results: list[ImageResult]