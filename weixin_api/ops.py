from . import conf
from .http_url import HttpApi


corpid = conf.corpid
secret = conf.secret
agentid = conf.agentid
ha = HttpApi(corpid, secret)
    

def send_text(agentid, content):
    body = {
        "touser" : "@all",
        "msgtype" : "text",
        "agentid" : agentid,
        "text" : {
            "content" : content
        },
        "safe":0
    }
    return ha.http_call("SEND_MESSAGE", body)


