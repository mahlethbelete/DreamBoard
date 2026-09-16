from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class VisionItemCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    image_url: str | None = None
    target_date: datetime | None = None
    category_id: int
    status: str = "not_started"


class VisionItemUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    image_url: str | None = None
    target_date: datetime | None = None
    category_id: int | None = None
    status: str | None = None


class VisionItemResponse(BaseModel):
    id: int
    user_id: int
    category_id: int
    title: str
    description: str | None
    image_url: str | None
    target_date: datetime | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)