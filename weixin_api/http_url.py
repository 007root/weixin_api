# coding:utf-8
import requests
import json


base_url = "https://qyapi.weixin.qq.com"
URL_TYPE = {
    "SEND_MESSAGE" : ["/cgi-bin/message/send?access_token=ACCESS_TOKEN", "POST"],
    "UPLOAD_TMP_IMAGE" : ["/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=image", "POST"],
    "ACCESS_TOKEN" : ["/cgi-bin/gettoken", "GET"]
}


class HttpApi():
    def __init__(self, corpid, secret):
        self.corpid = corpid
        self.secret = secret
        self.token = None
    
    def get_token(self):
        if not self.token:
            args = {
                "corpid": self.corpid,
                "corpsecret": self.secret
            }
            ret = self.http_call("ACCESS_TOKEN", **args)
            if ret["errcode"] == 0:
                self.token = ret["access_token"]
                return self.token
            else:
                return ret
        else:
            return self.token

    def refresh_token(self):
        self.token = None
        return self.get_token()
        
    def http_call(self, url_type, **args):
        url = base_url + URL_TYPE[url_type][0]
        method = URL_TYPE[url_type][1]
        if method == "GET":
            return self.http_get(url, args)
        if method == "POST":
            return self.http_post(url, args)

    def http_get(self, url, args):
        if isinstance(args, dict):
            for k,v in args.items():
                if "?" in url:
                    url += ('&' + k + '=' + v) 
                else:
                    url += ('?' + k + '=' + v) 
        return requests.get(url).json()

    def http_post(self, url, args):
        headers = args.get('headers', None)
        files = args.get('files', None)
        data = args.get('data', None)
        if data:
            data = json.dumps(data).encode('utf8')
        token = self.get_token()
        if not isinstance(token, dict):
            whole_url = url.replace("ACCESS_TOKEN", token)
            ret = requests.post(whole_url, headers=headers, data=data, files=files).json()
            if ret["errcode"] == 42001:
                whole_url = url.replace("ACCESS_TOKEN", self.refresh_token())
                return requests.post(whole_url, headers=headers, data=data, files=files).json()
            else:
                return ret
        else:
            return token


