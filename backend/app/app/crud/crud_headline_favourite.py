from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.headlines_favourites import HeadlineFavourite
from app.schemas.headline_favourite import HeadlineFavouriteCreate, HeadlineFavouriteUpdate


class CRUDCoinToken(CRUDBase[HeadlineFavourite, HeadlineFavouriteCreate, HeadlineFavouriteUpdate]):
    def get_headline_favourite(
            self,
            db: Session,
            headline_id: int
    ):
        return (
            db.query(self.model)
              .filter(HeadlineFavourite.headline_id==headline_id)
              .all()
        )
    
    def get_lastest_headline_by_favourite(
            self,
            db: Session,
            favourite_id: List[int]
    ):
        return (
            db.query(self.model)
              .filter(HeadlineFavourite.favourite_id.in_(favourite_id))
              .order_by(self.model.id.desc())
              .first()
        )


headline_favourite = CRUDCoinToken(HeadlineFavourite)
