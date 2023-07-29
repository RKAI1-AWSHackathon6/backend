from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/filter", response_model=List[schemas.HeadlineWithFavourite])
def filter_headline(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    headline_filer: schemas.HeadlineBySentiment,

) -> Any:
    return crud.headline.get_headline_by_sentiment(db=db, skip=skip, limit=limit, headline_filter=headline_filer)

@router.get("/", response_model=List[schemas.Headline])
def read_headline(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    headline = crud.headline.get_multi(db, skip=skip, limit=limit)
    return headline


@router.post("/", response_model=schemas.Headline)
def create_headline(
    *,
    db: Session = Depends(deps.get_db),
    headline_in: schemas.HeadlineCreate,
) -> Any:
    """
    Create new item.
    """
    headline = crud.headline.create(db=db, obj_in=headline_in)
    return headline


@router.put("/{id}", response_model=schemas.Headline)
def update_headline(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.HeadlineUpdate,
) -> Any:
    """
    Update an item.
    """
    headline = crud.headline.get(db=db, id=id)
    if not headline:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    headline = crud.headline.update(db=db, db_obj=headline, obj_in=item_in)
    return headline


@router.get("/{id}", response_model=schemas.Headline)
def read_headline(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    headline = crud.headline.get(db=db, id=id)
    if not headline:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return headline


@router.delete("/{id}", response_model=schemas.Headline)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    headline = crud.headline.get(db=db, id=id)
    if not headline:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    headline = crud.headline.remove(db=db, id=id)
    return headline
