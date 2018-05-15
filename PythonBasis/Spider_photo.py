#coding=utf-8
import urllib
import urllib.request
import re #正则表达式

#解析页面
def load_page(url):
    request=urllib.request.Request(url) #发送网络请求
    response=urllib.request.urlopen(request)#根据url打开页面
    data=response.read() #获取页面响应数据
    return data


#下载图片
def get_image(html):
    regx=r'http://[\S]*jpg'      #定义正则表达式，匹配页面图片元素
    pattern=re.compile(regx)         #编译表达式构造匹配模式
    get_image=re.findall(pattern,repr(html))  #进行正则匹配并返回结果

    num = 1
    #遍历获取的图片
    for img in get_image:
        image=load_page(img)
        #将图片存入到指定文件夹
        with open('E:\\Photo\\%s.jpg' %num,'wb') as fb:
            fb.write(image)
            print("正在下载第 %s张图片" %num)
            num = num + 1
    print("下载完成")


url='http://p.weather.com.cn/2017/06/2720826.shtml#p=1'
html=load_page(url)
get_image(html)
