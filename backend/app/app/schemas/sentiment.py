from typing import Optional

from pydantic import BaseModel


class SentimentBase(BaseModel):
    type: int
    name: str
    color: Optional[str] = None

class SentimentCreate(SentimentBase):
    pass

class SentimentUpdate(SentimentBase):
    pass


class SentimentInDBBase(SentimentBase):
    id: int

    class Config:
        orm_mode = True

class Sentiment(SentimentInDBBase):
    pass

class SentimentInDB(SentimentInDBBase):
    pass