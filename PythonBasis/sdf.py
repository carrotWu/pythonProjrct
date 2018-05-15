#encoding=utf-8
try:
    fileName=input("请输入文件名:")
    open("%s.txt" %fileName)
except FileNotFoundError:
    print("%s.txt文件不存在" %fileName)

try:
    print(stu)
except NameError:
    print('stu not found')

#BaseException是所有异常的父类
try:
    print(stu)
except BaseException:
    print('stu not found')