from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .favourites import Favourite  # noqa: F401


class Favourite(Base):
    __tablename__="favourites"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    rank = Column(Integer, nullable=True)
