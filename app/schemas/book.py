from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime
    category: Optional["CategoryRead"] = None  # строка!

    class Config:
        from_attributes = True  # вместо orm_mode в Pydantic v2

from app.schemas.category import CategoryRead
BookRead.model_rebuild()
