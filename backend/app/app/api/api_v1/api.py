from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, token, sentiment, headline, userfavourite

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(token.router, prefix="/tokens", tags=["tokens"])
api_router.include_router(sentiment.router, prefix="/sentiments", tags=["sentiments"])
api_router.include_router(headline.router, prefix="/headlines", tags=["headlines"])
api_router.include_router(userfavourite.router, prefix="/favourite", tags=["favourite"])