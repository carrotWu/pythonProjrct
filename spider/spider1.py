#coding=utf-8
import urllib
import urllib2

def loadPage(url,filename):
    """
    作用：根据url发送请求，获取服务器响应文件
    :param url: 要爬取的url地址
    """
    print u'正在下载'+filename
    headers={
        "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
    }
    request=urllib2.Request(url,headers=headers)
    return urllib2.urlopen(request).read()

def writePage(html, filename):
    """
        作用：将html内容写入到本地
        html：服务器相应文件内容
    """
    print u'正在保存'+ filename
    # 文件写入
    with open('c:\\'+filename,'w') as f:
        f.write(html)
    print "-" * 30

def tiebaSpider(url,beginPage,endPage):
    '''
    作用：贴吧爬虫调度器，负责组合处理每个页面的url
    :param url:贴吧url的前部分
    :param beginPage:起始页
    :param endPage:结束页
    '''
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50
        fileName=u'第'+str(page)+u'页.html'
        fulurl=url+"&pn="+str(pn)
        print fulurl
        html=loadPage(fulurl,fileName)
        writePage(html,fileName)
        print "下载完毕，谢谢使用！"

if __name__ == '__main__':
    kw=raw_input("请输入要爬取的贴吧名字：")
    beginPage=int(raw_input("输入起始页："))
    endPage=int(raw_input("请输入结束页"))
    url="http://tieba.baidu.com/f?"
    key=urllib.urlencode({"kw": kw})
    fulurl=url+key
    tiebaSpider(fulurl,beginPage,endPage)

