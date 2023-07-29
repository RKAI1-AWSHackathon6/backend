from .crud_item import item
from .crud_user import user
from .crud_coin import token
from .crud_sentiment import sentiment
from .crud_headline import headline
from .crud_headline_favourite import headline_favourite
from .crud_user_favourite import user_favourite
from .crud_article import article
# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
