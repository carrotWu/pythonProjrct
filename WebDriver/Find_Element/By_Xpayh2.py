#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")

#层级和属性结合定位--自学网输入用户名和密码
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys('51zxw')
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys('123456')
sleep(5)
#逻辑运算结合定位(and or)
driver.find_element_by_xpath("//input[@type='text' and @name='username']").send_keys('51zxw')
sleep(3)
driver.quit()