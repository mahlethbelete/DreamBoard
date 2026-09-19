from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    color: str = Field(default="plum", max_length=20)


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    color: str | None = Field(default=None, max_length=20)


class CategoryResponse(BaseModel):
    id: int
    user_id: int
    name: str
    color: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)