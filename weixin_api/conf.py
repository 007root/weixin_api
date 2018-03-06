import json


agentid = None
secret = None
corpid = None


if not agentid or not secret or not corpid:
    try:
        config = json.load(open('/etc/weixin.conf'))
        agentid = config['agentid']
        secret = config['secret']
        corpid = config['corpid']
    except Exception as e:
        raise e
