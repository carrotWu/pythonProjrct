#coding=utf-8
import datetime
import time
import math
#1. 日期输出格式化 datetime => string (格式化输出当前系统时间）
now = datetime.datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str)

#\\a.输出当前时间毫秒值 (取毫秒值小数点后三位，向下取整）
print(math.floor(time.time()*1000))

#\\b.输出当前时间戳（Tue May 15 15:54:41 2018）
print(time.ctime())

#2. 日期输出格式化 string => datetime
t_str = '2018-05-07 19:11:21'
d = datetime.datetime.strptime(t_str, '%Y-%m-%d %H:%M:%S')
print(type(d))

#3. 日期比较操作
#在datetime模块中有timedelta类，这个类的对象用于表示一个时间间隔，比如两个日期或者时间的差别。
#构造方法：
datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
#所有的参数都有默认值0，这些参数可以是int或float，正的或负的。
#可以通过 timedelta.days、tiemdelta.seconds 等获取相应的时间值。
#timedelta 类的实例，支持加、减、乘、除等操作，所得的结果也是 timedelta 类的实例。比如：
year = datetime.timedelta(days=365)
ten_years = year *10
nine_years = ten_years - year
#同时，date、time和datetime类也支持与timedelta的加、减运算。
#datetime1 = datetime2 + timedelta
#timedelta = datetime1 - datetime2
#这样，可以很方便的实现一些功能。

#4. 两个日期相差多少天。
d1 = datetime.datetime.strptime('2015-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2015-03-02 17:41:20', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
print (delta.days) #>>>3 天

#5. 今天的n天后的日期。
now = datetime.datetime.now()
delta = datetime.timedelta(days=3)
n_days = now + delta
print (n_days.strftime('%Y-%m-%d %H:%M:%S'))

