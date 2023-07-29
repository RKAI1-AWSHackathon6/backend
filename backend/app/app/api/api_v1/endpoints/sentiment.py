from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Sentiment])
def read_sentiment(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    sentiment = crud.sentiment.get_multi(db, skip=skip, limit=limit)
    return sentiment


@router.post("/", response_model=schemas.Sentiment)
def create_sentiment(
    *,
    db: Session = Depends(deps.get_db),
    sentiment_in: schemas.SentimentCreate,
) -> Any:
    """
    Create new item.
    """
    sentiment = crud.sentiment.create(db=db, obj_in=sentiment_in)
    return sentiment


@router.put("/{id}", response_model=schemas.Sentiment)
def update_sentiment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.SentimentUpdate,
) -> Any:
    """
    Update an item.
    """
    sentiment = crud.sentiment.get(db=db, id=id)
    if not sentiment:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    sentiment = crud.sentiment.update(db=db, db_obj=sentiment, obj_in=item_in)
    return sentiment


@router.get("/{id}", response_model=schemas.Sentiment)
def read_sentiment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    sentiment = crud.sentiment.get(db=db, id=id)
    if not sentiment:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return sentiment


@router.delete("/{id}", response_model=schemas.Sentiment)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    sentiment = crud.sentiment.get(db=db, id=id)
    if not sentiment:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    sentiment = crud.sentiment.remove(db=db, id=id)
    return sentiment
