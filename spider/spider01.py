#coding=utf-8
#requests最简单的爬虫模块之一
import requests
import re

def getMovieList():#获取电影列表信息
    res=requests.get('http://www.dytt8.net/html/gndy/dyzz/index.html')#post/get
    res.encoding='gb2312'
    result=res.text
    reg=r'<a href="(.*?)" class="ulink">(.*?)</a>'

    reg=re.compile(reg)
    print (len(re.findall(reg,result)))
    return re.findall(reg,result)

def getMovieContent(url,title):#获取具体电影信息
    res=requests.get('http://www.dytt8.net{}'.format(url))
    res.encoding='gb2312'
    result=res.text




for url,title in getMovieList():
    print (url,title)


