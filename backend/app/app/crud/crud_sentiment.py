from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.sentiments import Sentiment
from app.schemas.sentiment import SentimentCreate, SentimentUpdate


class CRUDCoinToken(CRUDBase[Sentiment, SentimentCreate, SentimentUpdate]):
    pass


sentiment = CRUDCoinToken(Sentiment)
