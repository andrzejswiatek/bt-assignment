from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    model_config = {"from_attributes": True}
    id: Optional[int] = None
    title: str
    author: str
    pages: int
    rating: float
    price: float    
