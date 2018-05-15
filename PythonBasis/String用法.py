#coding=utf-8
#1.去除空格
# (1)str.strip():删除字符串两边的指定字符，括号的写入指定字符，默认为空格
a=' Hello '
print a.strip() #>>>Hello
b='eeeHelloe'
print b.strip('e')#>>>Hello
# (2)str.lstrip()：删除字符串左边的指定字符，括号的写入指定字符，默认为空格
# (3)str.rstrip()：删除字符串右边指定字符，默认为空格
#2.复制字符串
c='Hello'
d=a
print (c,d)#>>>('Hello', ' Hello ')
#3.连接字符串
#(1)+号连接.
#   注：此方法又称为 "万恶的加号",因为使用加号连接2个字符串会调用静态函数
#   string_concat(register PyStringObject *a ,register PyObject * b),
#   在这个函数中会开辟一块大小是a+b的内存的和的存储单元，然后将a,b字符串拷贝进去。
#   如果是n个字符串相连  那么会开辟n-1次内存，是非常耗费资源的。
a='hello'
b='world'
print (a+b)#>>>helloworld
#(2) str.join连接
#   连接2个字符串,可指定连接符号
a='Hello'
b='###'
print (a.join(b))#>>>#Hello#Hello#
#4.查找字符串
# (1)str.index:获取指定字符的下标。返回下标  JAVA中str.Index of()
a='Hello world'
print a.index('H')#>>>0
# (2)str.find 查找指定字符串中是否有某个字符，没有返回-1，有返回索引下标
a='Hello world'
print a.find('w')#>>>6
#5.是否包含指定字符串： in|not in
a='hello world'
b='hello'
print (b in a)#>>>True
print ('jack' not in a)#>>>True
#6.字符串长度 str.len
a='hello world'
print (len(a))#>>>11
#7.字符串字母大小写转换 str.lower() str.upper()
a='Hello World'
print a.lower()#>>>hello world
print a.upper()#>>>HELLO WORLD
#8.大小写互换 str.swapcase()
a='Hello World'
print a.swapcase()#>>>hELLO wORLD
#9.首字母大写 str.capitalize()
a='hello World'
print a.capitalize()#>>>Hello world
#10.将字符串放入中心位置可指定长度以及位置两边字符 str.center(int,str)
a='hello world'
print (a.center(40,'*'))#>>>**************hello world***************
#11.字符统计 str.count
a='Hello world'
print (a.count('l'))#>>>3
#11.字符串的测试、判断函数，这一类函数在string模块中没有，这些函数返回的都是bool值
# S.startswith(prefix[,start[,end]])   #是否以prefix开头
# S.endswith(suffix[,start[,end]])     #以suffix结尾
# S.isalnum()                          #是否全是字母和数字，并至少有一个字符
# S.isalpha()                          #是否全是字母，并至少有一个字符
# S.isdigit()                          #是否全是数字，并至少有一个字符
# S.isspace()                          #是否全是空白字符，并至少有一个字符
# S.islower()                          #S中的字母是否全是小写
# S.isupper()                          #S中的字母是否便是大写
# S.istitle()                          #S是否是首字母大写的
#12.字符串切片
str = "0123456789"
print str[0:3] #截取第一位到第三位的字符
print str[:] #截取字符串的全部字符
print str[6:] #截取第七个字符到结尾
print str[:-3] #截取从头开始到倒数第三个字符之前
print str[2] #截取第三个字符
print str[-1] #截取倒数第一个字符
print str[::-1] #创造一个与原字符串顺序相反的字符串
print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
print str[-3:] #截取倒数第三位到结尾
print str[:-5:-3] #逆序截取，截取倒数第五位数与倒数第三位数之间




