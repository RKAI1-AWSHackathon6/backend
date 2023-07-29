from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import UserFavourite  # noqa: F401

class UserFavourite(Base):
    __tablename__="userfavourites"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    favourite_id = Column(Integer, nullable=False)
    visible = Column(Boolean(), nullable=False)
