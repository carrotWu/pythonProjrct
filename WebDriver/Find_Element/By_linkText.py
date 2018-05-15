#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://www.baidu.com')
sleep(3)
driver.find_element_by_id('kw').send_keys(u'豆瓣')
driver.find_element_by_id('su').click()
sleep(3)
driver.find_element_by_link_text(u'豆瓣读书').click()
sleep(6)
driver.find_element_by_partial_link_text('购物').click()
sleep(7)
driver.quit()

