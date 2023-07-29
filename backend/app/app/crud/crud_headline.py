from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.headlines import Headline 
from app.schemas.headline import HeadlineCreate, HeadlineUpdate, HeadlineBySentiment

from .crud_headline_favourite import headline_favourite
from .crud_coin import token

class CRUDHeadline(CRUDBase[Headline, HeadlineCreate, HeadlineUpdate]):
    def get_headline_by_sentiment(
        self, db: Session, *, skip: int = 0, limit: int = 100, headline_filter: HeadlineBySentiment
    )-> List[Headline]:
        headlines = (db.query(self.model)
                    .filter(headline_filter.sentiment_id is None or Headline.sentiment_id==headline_filter.sentiment_id)
                    .offset(skip)
                    .limit(limit)
                    .all())
        
        # for favourite in headline_favourite.get_headline_favourite(db, 2):
        #     print(favourite.favourite_id)
        #     print(token.get(db, favourite.favourite_id))

        favourites = {headline.id: [token.get(db, favourite.favourite_id) for favourite in headline_favourite.get_headline_favourite(db, headline.id)] for headline in headlines}
        # print(favourites)
        # print(headlines)

        for idx, headline in enumerate(headlines):
            try:
                # print(idx)
                # print(headline.id)
                # print(favourites[headline.id])
                headlines[idx].favourites = [_token for _token in favourites[headline.id] if _token is not None]
            except Exception as e:
                print(e)
        # print(headlines[0].favourites)
        return headlines

headline = CRUDHeadline(Headline)
