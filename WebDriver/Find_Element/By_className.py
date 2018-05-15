#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
sleep(2)
s=driver.find_element_by_class_name('s_ipt').send_keys(u'豆瓣')
sleep(6)
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()