from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.CoinToken])
def read_tokens(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    tokens = crud.token.get_multi(db, skip=skip, limit=limit)
    return tokens


@router.post("/", response_model=schemas.CoinToken)
def create_token(
    *,
    db: Session = Depends(deps.get_db),
    token_in: schemas.CoinTokenCreate,
) -> Any:
    """
    Create new item.
    """
    token = crud.token.create(db=db, obj_in=token_in)
    return token


@router.put("/{id}", response_model=schemas.CoinToken)
def update_token(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.CoinTokenUpdate,
) -> Any:
    """
    Update an item.
    """
    token = crud.token.get(db=db, id=id)
    if not token:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    token = crud.token.update(db=db, db_obj=token, obj_in=item_in)
    return token


@router.get("/{id}", response_model=schemas.CoinToken)
def read_token(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    token = crud.token.get(db=db, id=id)
    if not token:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    return token


@router.delete("/{id}", response_model=schemas.CoinToken)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    # current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    token = crud.token.get(db=db, id=id)
    if not token:
        raise HTTPException(status_code=404, detail="Item not found")
    # if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
    #     raise HTTPException(status_code=400, detail="Not enough permissions")
    token = crud.token.remove(db=db, id=id)
    return token
