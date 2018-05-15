#encoding=utf-8
#模块
import time
print(time.ctime())#当期日期时间戳格式
print(time.time())#毫秒数时间
print(time.localtime())#转换时间格式用
print(time.strftime('%Y-%m-%d %I:%M:%S',time.localtime(time.time())))

import random
num=random.randint(0,10)
print(num)

for i in range(3):
    print(i)
#random.randint(0,10) 生成0到10(包含10)的随机整数
#range(10) 加for循环生成0到9以内连续整数

#from...import... 从...中导入...
from time import sleep
num=random.randint(10,20)
print(num)
sleep(5)#sleep(0)参数单位是秒
print("sleep over")


ad=[1,2,3]
print(sum(ad)) #输出数组中元素和(前提是元素都为int)

#从Student文件中导入Student类
from Student import Student
#直接调用Student中的方法
stu1=Student('jack','BeiJing')
stu1.talk()


