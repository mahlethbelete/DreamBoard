from pydantic import BaseModel, Field


class SuggestRequest(BaseModel):
    prompt: str = Field(min_length=3, max_length=300)
    category_id: int


class Suggestion(BaseModel):
    title: str
    description: str


class SuggestResponse(BaseModel):
    suggestions: list[Suggestion]