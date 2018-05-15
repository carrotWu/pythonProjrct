#coding=utf-8
#调用cmd命令查询关闭IE进程
#1.查询进程CMD命令： tasklist | find "firefox.exe"
#2.根据PID关闭进程： taskkill /F /pid 123

#re.findall  的简单用法（返回string中所有与pattern相匹配的全部字串，返回形式为数组）
#join()方法：
#（1）join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
#（2）os.path.join()：  将多个路径组合后返回
#str.split(str="", num=string.count(str))
#str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
#num -- 分割次数。


#str='12,33  33 sd       er'
#str.split()去除字符串中空字符 返回数组>>>['12,33', '33', 'sd', 'er']
#"".join(str.split())将字符数组无缝连接成字符串>>>12,3333sder
#''.join(str.split()).replace(',','')将字符串中逗号去掉>>>123333sder

import os
import re
d=os.popen(' tasklist | find "firefox.exe"').read()#查询火狐进程
print(d)
ss=re.findall('\d*\d',"".join(d.split()).replace(',',''))#查询火狐进程的PID值
if ss!=[]:
    try:
        os.system("taskkill /F /pid %d" % int(ss[0]))
    except:
        pass

