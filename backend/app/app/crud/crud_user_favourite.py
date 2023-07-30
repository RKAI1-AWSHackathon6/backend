from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.crud.base import CRUDBase
from app.models.user_favourites import UserFavourite
from app.schemas.user_favourites import UserFavouriteCreate, UserFavouriteUpdate


class CRUDCoinToken(CRUDBase[UserFavourite, UserFavouriteCreate, UserFavouriteUpdate]):
    def get_favourite_by_userid(
            self,
            db: Session,
            userid: int
    )->List[UserFavourite]:
        return (
            db.query(self.model)
              .filter(and_(UserFavourite.user_id == userid, UserFavourite.visible == True))
              .all()
        )
    
    def get_user_by_favourite(
            self,
            db: Session,
            favourite_id: List[int]
    )->List[UserFavourite]:
        return (
            db.query(self.model)
              .filter(and_(UserFavourite.favourite_id.in_(favourite_id), UserFavourite.visible == True))
              .distinct()
              .all()
        )


user_favourite = CRUDCoinToken(UserFavourite)
