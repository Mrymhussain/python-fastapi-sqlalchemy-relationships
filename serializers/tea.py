from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from .comment import CommentSchema


class TeaSchema(BaseModel):
    id: Optional[int] = None
    name: str
    in_stock: bool
    rating: int
    comments: List[CommentSchema] = []

    model_config = ConfigDict(from_attributes=True)


class CreateTeaSchema(BaseModel):
    name: str
    in_stock: bool
    rating: int

    model_config = ConfigDict(from_attributes=True)


class UpdateTeaSchema(BaseModel):
    name: str
    in_stock: bool
    rating: int

    model_config = ConfigDict(from_attributes=True)