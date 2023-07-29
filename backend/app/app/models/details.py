from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .details import Detail  # noqa: F401


class Detail(Base):
    id = Column(Integer, primary_key=True, index=True)
    headline_id = Column(Integer, ForeignKey("headline.id"))
    body = Column(String, nullable=True)
