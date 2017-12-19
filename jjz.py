#!/bin/python
from urllib import request
from urllib import parse
from urllib import error
import sys
import gzip
import os 
import time

openUrl = "https://api.jinjingzheng.zhongchebaolian.com/enterbj/platform/enterbj/addcartype"
openUrl2 = "https://passport.hupu.com/m/login"
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"UM_distinctid=16043fa5ce086-0e43a1dcf93e59-5e183017-13c680-16043fa5ce13fe; CNZZDATA1259638683=908815487-1512964997-%7C1512964997",
"Host":"api.jinjingzheng.zhongchebaolian.com",
"If-Modified-Since":"Mon, 30 Oct 2017 08:00:54 GMT",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89",
}

reqData ={

}
enRequestData = parse.urlencode(reqData).encode("utf-8")
while 1:
    req = request.Request(openUrl,headers= headers)
    try:
        reqOpen = request.urlopen(req)
    except error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        else:
            print("unknown fail ")
        time.sleep(1)
        continue
    break
#succ 
print(reqOpen.status)

rspData = reqOpen.read()
rspData = rspData.decode('utf-8','ignore')
print(rspData)