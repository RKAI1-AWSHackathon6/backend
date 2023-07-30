from celery import Celery
from app.core.config import settings

celery_app = Celery("worker", 
                    broker=f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}/0",
                    backend=f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}/1",
                    )

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue",
                               "app.worker.send_telegram_message": "main-queue"}
