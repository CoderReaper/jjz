#!/bin/python
from urllib import request
from urllib import parse
import os 

openUrl = "https://api.jinjingzheng.zhongchebaolian.com/enterbj/platform/enterbj/addcartype"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89",
    "Origin": "https://api.jinjingzheng.zhongchebaolian.com",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://api.jinjingzheng.zhongchebaolian.com/enterbj/jsp/enterbj/index.jsp",
    #"Accept-Language":" zh-cn",
    #"Accept-Encoding": "gzip, deflate",
    "Cookie":"UM_distinctid=16043fa5ce086-0e43a1dcf93e59-5e183017-13c680-16043fa5ce13fe; CNZZDATA1259638683=908815487-1512964997-%7C151296499",
    "Content-Length": "182"
}

reqData ={

}
enRequestData = parse.urlencode(reqData).encode("utf-8")

req = request.Request(openUrl,headers= headers)

reqOpen = request.urlopen(req)
print(reqOpen.status)

rspData = reqOpen.read()
rspData = rspData.decode('utf-8','ignore')

print(rspData)