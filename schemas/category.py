from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)


class CategoryUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=50)


class CategoryResponse(BaseModel):
    id: int
    user_id: int
    name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
