#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://www.51zxw.net/')
sleep(3)
driver.find_element_by_tag_name('input').send_keys('selenium')
sleep(2)
driver.find_elements_by_tag_name('input')[1].send_keys('selenium')
sleep(3)
driver.quit()
