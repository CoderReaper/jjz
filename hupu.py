#/bin/bash
# -*- coding: UTF-8 -*-
import os
import urllib
import urllib.request
import http.cookiejar
def hupu():
	print("helo hupu")
cookiefile = "hupu.cj"
cookie = http.cookiejar.MozillaCookieJar(cookiefile)

handler = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
beforeloginret = handler.open("https://passport.hupu.com/pc/login");

beforedata = beforeloginret.read().decode("utf-8")

print(beforedata);
index = beforedata.find("/seccode/?")




data =urllib.parse.urlencode({
	"username":"holyreaper",
	"password":"Xiaodian123",
	"seccode":"true"}).encode("utf-8")

head = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"}
print(cookie)
req = urllib.request.Request("https://passport.hupu.com/pc/login",data,head)
for item in cookie:
	print("name:",item.name)
	print("value:",item.value)
cookie.save()
#print("",dir(ret))
ret  = handler.open(req)
print(ret.getcode())
res = ret.read()
#print ("helo : ", dir(res))

res2 = res.decode("utf-8","ignore")
try:
	fileobj = open("./hupu.xml","w")
except Exception as e:
	print("error:",e)             
else:
	res2 = res2.replace('\u200b',"helo")
	fileobj.write(str(res2));
	fileobj.close()

	#pass
finally:
	pass
