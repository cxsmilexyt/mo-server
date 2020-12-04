import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import logging


def hmac_sha256_sign(secret):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp, sign


def notify(config, messages):
    logging.info("enter dingtalk pushing.")
    headers = {'content-type': 'application/json'}
    webhook = config["webhook"]
    secret = config["secret"]
    timestamp, sign = hmac_sha256_sign(secret)
    data = {
        "msgtype": "text", 
        "text": {
            "content": messages
        }
    }
    try:
        # todo
        notify_ret = requests.post(url="%s&timestamp=%s&sign=%s" % (webhook, timestamp, sign), json=data, headers=headers)
        return True
    except Exception as e:
        logging.error("dingtalk notify failed. reason is %s" % str(e))
        return False
