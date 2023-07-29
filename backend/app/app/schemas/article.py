from typing import Optional

from pydantic import BaseModel


class ArticleBase(BaseModel):
    # id = Column(Integer, primary_key=True, index=True)
    # source_id = Column(Integer, nullable=False)
    # title = Column(String, nullable=False)
    # body = Column(String, nullable=False)
    # tag = Column(String, nullable=False)
    # published_timestamp = Column(Integer, nullable=True)
    # thumbnail_image_link = Column(String, nullable=False)
    # origin_link = Column(String, nullable=False)
    # created_at = Column(Integer, nullable=False)
    # author = Column(String, nullable=True)
    # description = Column(String, nullable=True)
    # body_image = Column(String, nullable=True)
    source_id: Optional[int]
    title: Optional[str]
    body: Optional[str]
    tag: Optional[str]
    published_timestamp: Optional[int]
    thumbnail_image_link: Optional[str]
    origin_link: Optional[str]
    created_at: Optional[int]
    author: Optional[str]
    description: Optional[str]
    body_image: Optional[str]

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleBase):
    pass


class ArticleInDBBase(ArticleBase):
    id: int

    class Config:
        orm_mode = True

class Article(ArticleInDBBase):
    pass

class ArticleInDB(ArticleInDBBase):
    pass