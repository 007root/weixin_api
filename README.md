# weixin_api
企业微信接口，目前只用到了发送文本的接口；官方文档https://work.weixin.qq.com/api/doc#10013

1. 安装  
```
  pip install -e git+https://github.com/007root/weixin_api.git#egg=weixin_api
```
2. 使用  
   创建配置文件/etc/weixin.conf，参考weixin.conf.example配置  
   发送消息  
```
   from weixin_api.ops import *  
   send_text(agentid, content)
```
