from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.headlines import Headline 
from app.schemas.headline import HeadlineCreate, HeadlineUpdate, HeadlineBySentiment

from .crud_headline_favourite import headline_favourite
from .crud_coin import token
from .crud_user_favourite import user_favourite

class CRUDHeadline(CRUDBase[Headline, HeadlineCreate, HeadlineUpdate]):
    def get_headline_by_sentiment(
        self, db: Session, *, skip: int = 0, limit: int = 100, headline_filter: HeadlineBySentiment
    )-> List[Headline]:
        headlines = (db.query(self.model)
                    .filter(headline_filter.sentiment_id is None or Headline.sentiment_id==headline_filter.sentiment_id)
                    .offset(skip)
                    .limit(limit)
                    .all())
        
        user_favourite_ = user_favourite.get_favourite_by_userid(db, userid=headline_filter.user_id)
        
        favourite_list = [uf.favourite_id for uf in user_favourite_ if uf.visible] if user_favourite_ is not None else []

        if favourite_list:
            favourites = {headline.id: [token.get(db, favourite.favourite_id) for favourite in headline_favourite.get_headline_favourite(db, headline.id) if favourite.favourite_id in favourite_list] for headline in headlines}
        else:
            favourites = {headline.id: [token.get(db, favourite.favourite_id) for favourite in headline_favourite.get_headline_favourite(db, headline.id)] for headline in headlines}

        filterd_headlines = []
        for idx, headline in enumerate(headlines):
            try:
                headlines[idx].favourites = [_token for _token in favourites[headline.id] if _token is not None]
                if headlines[idx].favourites:
                    filterd_headlines.append(headlines[idx])
            except Exception as e:
                print(e)
        return filterd_headlines

headline = CRUDHeadline(Headline)
