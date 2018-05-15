from sys import stdout
from xml.dom import minidom
#打开xml文件
dom=minidom.parse('Class.xml')
#root=dom.documentElement
#print(root.nodeName)
#print(root.nodeValue)
#print(root.nodeType)

#获取文档对象元素
root=dom.documentElement
names=root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')
#分别打印显示xml文档标签里的内容
for i in range(4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)

#获取标签属性的值

logins=root.getElementsByTagName('login')
for i in range(2):
     usernaem=logins[i].getAttribute('username')
     password=logins[i].getAttribute('password')
     print(usernaem)
     print(password)

     