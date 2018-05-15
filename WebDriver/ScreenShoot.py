#coding=utf-8
#网页截图操作
#案例：分别打开我要自学网页面和百度页面，然后进行截图
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
#打开我爱自学网并截图
driver.get("http://www.51zxw.net")
driver.get_screenshot_as_file("F:\\pythonProjrct\\python_SchreenShoot\\51zx.jpg")

#打开百度并截图
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file("F:\\pythonProjrct\\python_SchreenShoot\\baidu.jpg")
sleep(2)
driver.quit()