#coding=utf-8
#上传文件
#案例：在百度搜索上传本地图片进行搜索。
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector(".soutu-btn").click()
sleep(3)

driver.find_element_by_css_selector('.upload-pic').send_keys("C:\\360.png")
sleep(3)
