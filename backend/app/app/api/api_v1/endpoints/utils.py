from typing import Any

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from sqlalchemy.orm import Session
from app import models, schemas
from app.api import deps
from app.core.celery_app import celery_app
from app.utils import send_test_email
from app import crud

router = APIRouter()


@router.post("/test-celery/", response_model=schemas.Msg, status_code=201)
def test_celery(
    msg: schemas.Msg
    ) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.test_celery", args=[msg.msg])
    return {"msg": "Word received"}


@router.post("/test-telegram/", response_model=schemas.Msg, status_code=201)
def test_telegram(
    msg: schemas.Telegram,
) -> Any:
    """
    Test Celery worker.
    """
    celery_app.send_task("app.worker.send_telegram_message", args=[msg.headline_id])
    return {"msg": "Word received"}

@router.post("/send-telegrram-notify/", status_code=201)
def test_telegram(
    *,
    db: Session = Depends(deps.get_db),
    msg: schemas.Telegram,
) -> Any:
    """
    Test Celery worker.
    """
    latest_headline = crud.headline.get_latest_headline(db=db, user_id=1)
    celery_app.send_task("app.worker.send_telegram_message", args=[latest_headline.id])
    return latest_headline

@router.post("/test-email/", response_model=schemas.Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}
