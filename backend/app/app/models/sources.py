from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .sources import Source  # noqa: F401


class Source(Base):
    __tablename__="newspapersites"
    id = Column(Integer, primary_key=True, index=True)
    source_url = Column(String, nullable=False)
    source_rss = Column(String, nullable=False)
