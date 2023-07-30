from pydantic import BaseModel


class Msg(BaseModel):
    msg: str

class Telegram(BaseModel):
    headline_id: int