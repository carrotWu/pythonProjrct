#coding=utf-8
from selenium import webdriver
from time import sleep
#加载浏览器驱动
driver=webdriver.Firefox()

#打开百度页面
driver.get('http://www.baidu.com')
print(driver.title)
sleep(3)
# 关闭浏览器
driver.quit()

