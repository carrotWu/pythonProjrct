#encoding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys(u'豆瓣')
driver.find_element_by_name('wd').send_keys('selenium')
sleep(2)
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()

