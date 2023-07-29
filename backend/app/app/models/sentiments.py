from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .sentiments import Sentiment  # noqa: F401


class Sentiment(Base):
    __tablename__ = "sentiments"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    color = Column(String, nullable=True)
