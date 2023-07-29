from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .headlines import Headline  # noqa: F401


class Headline(Base):
    __tablename__="headlines"
    id = Column(Integer, primary_key=True, index=True)
    sentiment_id = Column(Integer, nullable=False)
    title = Column(String, nullable=True)
    hint = Column(String, nullable=True)
    thumbnail_image_link = Column(String, nullable=False)
    origin_link = Column(String, nullable=True)
    publish_date = Column(Integer, nullable=True)
    tag = Column(Integer, nullable=True)
    created_at = Column(Integer, nullable=False)

    body = Column(String, nullable=True)
    explain = Column(String, nullable=True)
    description = Column(String, nullable=True)

    favourites = []


