from raven import Client

from app.core.celery_app import celery_app
from app.db.session import SessionLocal
from app.core.config import settings
from app import crud

from app import http_utils
from app.schemas import HeadlineCreate, HeadlineFavouriteCreate

client_sentry = Client(settings.SENTRY_DSN)


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
def test_celery(word: str) -> str:
    return f"test task return {word}"
