from raven import Client

from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.core.config import settings
from app import crud

from app import http_utils
from app.schemas import HeadlineCreate, HeadlineFavouriteCreate
from app.utils import build_message_content
from app.my_telegram import TelegramSender, TelegramMessage

client_sentry = Client(settings.SENTRY_DSN)

client_telegram = TelegramSender()

@celery_app.task()
def processing(news_id: int):
    try:
        db = SessionLocal()
        print("ID------: " + str(news_id))
        # Get the aricle from the db
        article = crud.article.get(db, news_id)

        if article is None:
            return
        
        _classify_json_param = {
                        "title": article.title,
                        "description": article.description,
                        "keywords": article.tag
                        }
        _classify_result = http_utils.text_classify(_classify_json_param)

        if _classify_result is None:
            return
        
        ## Check deplicate
        _is_duplicate = http_utils.text_embedding(_classify_json_param)
        # Return is false or the articles is duplicate
        if (_is_duplicate is None) or (_is_duplicate["data"] == False):
            return
        
        _text_summary_params = {
                                "content": article.body
                                }
        ### Summary
        _text_summary = http_utils.text_summary(_text_summary_params)
        if _text_summary is None:
            return
        
        ## Save the result and send notify to others apps
        _headline_result = HeadlineCreate(
                            sentiment_id=_text_summary["data"]["type"],
                            title=article.title,
                            hint=article.title,
                            thumbnail_image_link=article.thumbnail_image_link,
                            origin_link=article.origin_link,
                            publish_date=article.published_timestamp,
                            tag=article.tag,
                            body=_text_summary["data"]["summary"],
                            explain=_text_summary["data"]["explain"],
                            description = article.description
                            )

        headline_ = crud.headline.create(db, obj_in=_headline_result)

        ## Create the list of relate item
        for symbol in  _classify_result["data"]:
            headline_favourite = HeadlineFavouriteCreate(
                                    headline_id=headline_.id,
                                    favourite_id=symbol["id"]
                                )
            crud.headline_favourite.create(db, obj_in=headline_favourite)
                                    
    finally:
        db.close()

@celery_app.task(acks_late=True)
def send_telegram_message(headline_id):
    try:
        db = SessionLocal()
        headline = crud.headline.get(db, headline_id)
        if headline is None:
            return
        
        # Get all related coin for this headline
        related_tokens = crud.headline_favourite.get_headline_favourite(db, headline_id)
        if related_tokens is None:
            return  # This is not related to any coin
        
        related_token_id = [hf.favourite_id for hf in related_tokens if hf is not None]
        user_ids = crud.user_favourite.get_user_by_favourite(db, related_token_id)
        
        if user_ids is None:
            return # There are no user want this message

        message_content = build_message_content(headline)

        for user_id in user_ids:
            # Get user
            _user_info = crud.user.get(db, user_id.user_id)
            if _user_info is not None and _user_info.telegram_chat_id is not None:
                _telegram_message = TelegramMessage(message_content, _user_info.telegram_chat_id)
                client_telegram.send_message(_telegram_message)
        
    finally:
        db.close()

@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    return f"test task return {word}"
