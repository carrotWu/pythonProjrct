#coding=utf-8
#隐式等待
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep,ctime

driver=webdriver.Firefox()
driver.get("http://www.sogou.com")
sleep(2)

driver.implicitly_wait(5) #隐式等待时间设定5秒
#检测搜索框是否存在
try:
    print(ctime())
    driver.find_element_by_css_selector("#kw").send_keys("Python")
    driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
    print (msg)
finally:
    print (ctime())

sleep(3)
driver.quit()