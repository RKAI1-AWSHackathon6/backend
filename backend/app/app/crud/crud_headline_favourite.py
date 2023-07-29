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


headline_favourite = CRUDCoinToken(HeadlineFavourite)
