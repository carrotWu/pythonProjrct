#coding=utf-8
import urllib2
#通过urllib2构造一个请求对象
#"User-Agent"用来模拟浏览器发送的请求，爬虫与返爬的第一步
ua_headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
}
request=urllib2.Request("http://www.baidu.com",headers=ua_headers)
response = urllib2.urlopen(request)
html = response.read()
print html
#返回http的响应码，成功就是200
print response.getcode()

#返回数据的实际url，防止重定向问题
print response.geturl()

#返回服务器响应的报头信息
print response.info()


