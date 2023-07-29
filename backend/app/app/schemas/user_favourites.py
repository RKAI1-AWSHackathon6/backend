from typing import Optional
import time

from pydantic import BaseModel

class UserFavouriteBase(BaseModel):
    user_id: Optional[int]
    favourite_id: Optional[int]
    visible: Optional[bool]

class UserFavouriteCreate(UserFavouriteBase):
    favourite_id: int
    visible: int = True

class UserFavouriteUpdate(UserFavouriteBase):
    pass

class UserFavouriteInDBBase(UserFavouriteBase):
    id: int

    class Config:
        orm_mode = True

class UserFavourite(UserFavouriteInDBBase):
    pass

class UserFavouriteInDB(UserFavouriteInDBBase):
    pass
