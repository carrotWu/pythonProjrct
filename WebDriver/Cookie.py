#coding=utf-8
#案例：查看访问我要自学网时的Cookie内容
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/")
#获取cookie全部内容
cookie=driver.get_cookies()
#打印cookie信息
print(cookie)
#打印cookie第一组信息
print (cookie[0])

#添加cookie
driver.add_cookie({'name':'51zxw','value':'www.51zxw.net'})
for cookie in driver.get_cookies():
    print ("%s---%s"%(cookie['name'],cookie['value']))
sleep(3)
driver.quit()