from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

# @router.post("/filter", response_model=List[schemas.HeadlineWithFavourite])
# def filter_headline(
#     *,
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     headline_filer: schemas.HeadlineBySentiment,

# ) -> Any:
#     return crud.user_favourite.get_headline_by_sentiment(db=db, skip=skip, limit=limit, headline_filter=headline_filer)

@router.get("/", response_model=List[schemas.UserFavourite])
def read_headline(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    user_favourite = crud.user_favourite.get_multi(db, skip=skip, limit=limit)
    return user_favourite


@router.post("/", response_model=schemas.UserFavourite)
def create_headline(
    *,
    db: Session = Depends(deps.get_db),
    userfavourite_in: schemas.UserFavouriteCreate,
) -> Any:
    """
    Create new item.
    """
    userfavourite_in.user_id = 1
    user_favourite = crud.user_favourite.create(db=db, obj_in=userfavourite_in)
    return user_favourite


@router.put("/{id}", response_model=schemas.UserFavourite)
def update_headline(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.UserFavouriteUpdate,
) -> Any:
    """
    Update an item.
    """
    item_in.user_id = 1
    user_favourite = crud.user_favourite.get(db=db, id=id)
    if not user_favourite:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    user_favourite = crud.user_favourite.update(db=db, db_obj=user_favourite, obj_in=item_in)
    return user_favourite


@router.get("/{id}", response_model=schemas.UserFavourite)
def read_headline(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    user_favourite = crud.user_favourite.get(db=db, id=id)
    if not user_favourite:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return user_favourite


@router.delete("/{id}", response_model=schemas.UserFavourite)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    user_favourite = crud.user_favourite.get(db=db, id=id)
    if not user_favourite:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    user_favourite = crud.user_favourite.remove(db=db, id=id)
    return user_favourite
