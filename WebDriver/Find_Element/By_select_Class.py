#coding=utf-8
#使用select类定位
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
sleep(2)
#使用select类定位
select=Select(driver.find_element_by_css_selector("[name='CookieDate']"))
# select.select_by_index(2)
# select.select_by_visible_text("留一年")
select.select_by_value('1')
sleep(2)
driver.quit()