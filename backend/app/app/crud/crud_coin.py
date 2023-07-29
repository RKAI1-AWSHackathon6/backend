from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.favourites import Favourite
from app.schemas.coin_token import CoinTokenCreate, CoinTokenUpdate


class CRUDCoinToken(CRUDBase[Favourite, CoinTokenCreate, CoinTokenUpdate]):
    pass


token = CRUDCoinToken(Favourite)
