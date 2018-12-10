from . import conf
import json
from .http_url import HttpApi


corpid = conf.corpid
secret = conf.secret
agentid = conf.agentid
ha = HttpApi(corpid, secret)
    

def send_text(agentid, content):
    '''
        content: text
    '''
    body = {
        "data":{
            "touser" : "@all",
            "msgtype" : "text",
            "agentid" : agentid,
            "text" : {
                "content" : content
            },
            "safe":0
        }
    }
    return ha.http_call("SEND_MESSAGE", **body)


def send_image(agentid, content):
    '''
        content:
            ret = requests.get(url)
            content = ret.content

            f = open(filename, 'rb')
            coontent = f.read()
    '''
    body = {
        "files": {
            "imgFile": ("test.jpg", content, "image/png")
        }
    }
    ret = ha.http_call("UPLOAD_TMP_IMAGE", **body)
    if ret.get('errcode') == 0:
        media_id = ret.get('media_id')
        body = {
            "data": {
                "touser" : "@all",
                "msgtype" : "image",
                "agentid" : agentid,
                "image" : {
                    "media_id" : media_id
                },
                "safe":0
            }
        }
        return ha.http_call("SEND_MESSAGE", **body)
    else:
        send_text(agentid, ret.get('errmsg'))


