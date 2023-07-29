from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .favourites import HeadlineFavourite  # noqa: F401


class HeadlineFavourite(Base):
    __tablename__="headlinefavourites"
    id = Column(Integer, primary_key=True, index=True)
    favourite_id = Column(Integer, nullable=False)
    headline_id = Column(Integer, nullable=False)
