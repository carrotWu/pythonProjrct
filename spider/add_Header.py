#coding=utf-8
import random,urllib2
ua_list=[
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
]
url="http://www.baidu.com"
#在UserAgent列表里随机选择一个User-Agent
user_agent=random.choice(ua_list)

#构造一个请求
request=urllib2.Request(url)

#add_header()方法，添加/修改一个HTTP报头
request.add_header('User-Agent',user_agent)

#get_header() 获取一个已有的HTTP报头的值，注意只能是第一个字母大写其他字母小写
print request.get_header('User-agent')
