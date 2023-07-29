from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .article import Article  # noqa: F401


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    tag = Column(String, nullable=False)
    published_timestamp = Column(Integer, nullable=True)
    thumbnail_image_link = Column(String, nullable=False)
    origin_link = Column(String, nullable=False)
    created_at = Column(Integer, nullable=False)
    author = Column(String, nullable=True)
    description = Column(String, nullable=True)
    body_image = Column(String, nullable=True)
