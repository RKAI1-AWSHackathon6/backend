import requests
from app.core.config import settings

def send_post_request(_url, _json):
    try:
        res = requests.post(_url, json=_json)
        
        if res.status_code != 200:
            print("Error while request: " + res.text)
            return None
        
        return res.json()
    except Exception as e:
        print("Error while request: " + str(e))
    
    return None

def text_classify(_json):
    return send_post_request(settings.CLASSIFY_TEXT_URL, _json)
    
def text_embedding(_json):
    return send_post_request(settings.CHECK_EMBEDDING_URL, _json)

def text_summary(_json):
    return send_post_request(settings.SUMMARY_URL, _json)