from sqlalchemy import Column, String, Boolean, Integer

from models.base import BaseModel


class TeaModel(BaseModel):
    __tablename__ = "teas"

    name = Column(String, unique=True)
    in_stock = Column(Boolean)
    rating = Column(Integer)