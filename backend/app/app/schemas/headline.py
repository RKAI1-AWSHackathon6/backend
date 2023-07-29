from typing import Optional, List
import time

from pydantic import BaseModel
from .coin_token import CoinToken

class HeadlineBase(BaseModel):
    sentiment_id: Optional[int]
    title: Optional[str]
    hint: Optional[str]
    thumbnail_image_link: Optional[str]
    origin_link: Optional[str]		
    publish_date: Optional[int] = None
    tag: Optional[str]
    body: Optional[str]
    explain: Optional[str]
    description: Optional[str]
    created_at: Optional[int]

class HeadlineCreate(HeadlineBase):
    sentiment_id: int
    title: str
    hint: str
    thumbnail_image_link: str
    origin_link: str
    created_at: Optional[int] = int(time.time())

class HeadlineUpdate(HeadlineBase):
    pass

class HeadlineInDBBase(HeadlineBase):
    id: int

    class Config:
        orm_mode = True

class Headline(HeadlineInDBBase):
    pass

class HeadlineWithFavourite(HeadlineInDBBase):
    favourites: List[CoinToken]

class HeadlineInDB(HeadlineInDBBase):
    pass

class HeadlineBySentiment(BaseModel):
    sentiment_id: Optional[int]
    user_id: Optional[int]