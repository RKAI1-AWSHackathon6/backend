from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user_favourites import UserFavourite
from app.schemas.user_favourites import UserFavouriteCreate, UserFavouriteUpdate


class CRUDCoinToken(CRUDBase[UserFavourite, UserFavouriteCreate, UserFavouriteUpdate]):
    def get_favourite_by_userid(
            self,
            db: Session,
            userid: int
    ):
        return (
            db.query(self.model)
              .filter(UserFavourite.user_id == userid)
              .all()
        )


user_favourite = CRUDCoinToken(UserFavourite)
