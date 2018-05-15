#coding=utf-8
#下拉菜单菜单元素定位
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get('http://www.51zxw.net')
sleep(2)
#根据option标签来定位
driver.find_elements_by_tag_name('option')[0].click()
driver.find_element_by_css_selector("[value='2']").click()
sleep(3)
driver.quit()
