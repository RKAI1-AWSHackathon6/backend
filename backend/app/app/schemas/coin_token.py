from typing import Optional

from pydantic import BaseModel


class CoinTokenBase(BaseModel):
    name: str
    symbol: str
    icon: str
    rank: Optional[str] = None

class CoinTokenCreate(CoinTokenBase):
    pass

class CoinTokenUpdate(CoinTokenBase):
    pass


class CoinTokenInDBBase(CoinTokenBase):
    id: int

    class Config:
        orm_mode = True

class CoinToken(CoinTokenInDBBase):
    pass

class CoinTokenInDB(CoinTokenInDBBase):
    pass