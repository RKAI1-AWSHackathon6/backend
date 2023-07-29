from typing import Optional
import time

from pydantic import BaseModel


class HeadlineFavouriteBase(BaseModel):
    favourite_id: Optional[int]
    headline_id: Optional[int]

class HeadlineFavouriteCreate(HeadlineFavouriteBase):
    favourite_id: int
    headline_id: int

class HeadlineFavouriteUpdate(HeadlineFavouriteBase):
    pass

class HeadlineFavouriteInDBBase(HeadlineFavouriteBase):
    id: int

    class Config:
        orm_mode = True

class HeadlineFavourite(HeadlineFavouriteInDBBase):
    pass

class HeadlineFavouriteInDB(HeadlineFavouriteInDBBase):
    pass
