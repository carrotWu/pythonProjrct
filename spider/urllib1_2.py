#coding=utf-8
import urllib,urllib2
url="http://www/baidu.com/s"
keyword=raw_input("请输入要查询的关键字：")
wd={"wd":keyword}
#通过urllib.encode()将汉字转码
wd=urllib.urlencode(wd)

fullUrl=url

headers={"User-Agent":"Mozilla..."}
request=urllib2.Request(fullUrl,headers=headers)
response=urllib2.urlopen(request)

print response.read()

