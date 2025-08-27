from typing import Optional
from pydantic import BaseModel, Field


class BookInput(BaseModel):
    id: int
    title: str
    author: str
    pages: int = Field(..., gt=0, le=5000)
    rating: float = Field(..., ge=0, le=5)
    price: float = Field(..., gt=0)


class BookOutput(BookInput):
    ...


class BookUpdateModel(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    pages: Optional[int] = Field(None, gt=0, le=5000)
    rating: Optional[float] = Field(None, ge=0, le=5)
    price: Optional[float] = Field(None, gt=0)
