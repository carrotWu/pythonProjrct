#coding=utf-8
import urllib2
#构建一个HttpHandler处理器对象，支持处理Http的请求
#http_handler=urllib2.HTTPHandler()

#在Http_handler中加入参数“debuglevel=1”，将会自动打开Debug模式
#程序在执行时候就会自动打印收发包信息
http_handler=urllib2.HTTPHandler(debuglevel=1)

#调用bulild_opener()方法构建一个自定义的opender对象，参数是构建的处理器对象
opener=urllib2.build_opener(http_handler)

request=urllib2.Request("http://www.baidu.com/")
response=opener.open(request)

#print response.read()