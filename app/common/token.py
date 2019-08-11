import logging
import requests
from datetime import datetime
from functools import lru_cache
from config import Config


@lru_cache(None)
def get_access_token():
    app_id = Config.APP_ID
    app_secret = Config.APP_SECRET
    logging.info("get access token app_id:%s, app_secret:%s", app_id, app_secret)
    if app_id is None or app_secret is None:
        logging.error("get access token app_id:%s, app_secret:%s", app_id, app_secret)
        return None
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' \
          '{0}&secret={1}'.format(app_id, app_secret)
    r = requests.get(url)
    logging.debug("get access token response:%s, url:%s", r.json(), url)
    access_token = r.json().get('access_token')
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info("get access token success at:%s", time_now)
    return access_token, datetime.now()


def get_token():
    token, t = get_access_token()
    if (datetime.now() - t).seconds > 3600:
        get_access_token.cache_clear()
        token, t = get_access_token()
        return token
    else:
        return token


@lru_cache(None)
def get_jsapi_ticket():
    url = 'https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={0}&type=jsapi \
          '.format(get_token())
    res = requests.get(url)
    logging.debug("get js api ticket response:%s, url:%s", res.json(), url)
    js_api_ticket = res.json().get('ticket')
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info("get access token success at:%s", time_now)
    return js_api_ticket, datetime.now()


def get_ticket():
    ticket, t = get_jsapi_ticket()
    if (datetime.now() - t).seconds > 3600:
        get_jsapi_ticket.cache_clear()
        ticket, t = get_jsapi_ticket()
        return ticket
    else:
        return ticket


def init_token():
    get_token()
    get_ticket()
