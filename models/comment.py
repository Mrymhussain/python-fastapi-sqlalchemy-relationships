from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class CommentModel(BaseModel):
    __tablename__ = "comments"

    content = Column(String, nullable=False)

    tea_id = Column(
        Integer,
        ForeignKey("teas.id"),
        nullable=False
    )

    tea = relationship(
        "TeaModel",
        back_populates="comments"
    )