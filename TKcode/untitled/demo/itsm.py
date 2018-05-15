import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select
import cx_Oracle
import xlrd
from xlutils.copy import copy
from decimal import Decimal
#create by grape Shi



url = "https://itsm.taikang.com/"
un = "itw_shict"
pw = "pass123456"


'''
demo模式
'''

driver = webdriver.Ie()
driver.maximize_window()
driver.get(url)
driver.find_element_by_id("username").send_keys(un)
driver.find_element_by_id("password").send_keys(pw)
driver.find_element_by_css_selector("input[value='登录']").click()

time.sleep(3)
driver.switch_to.frame("content-000001")
s = driver.find_elements_by_css_selector("font[color='white']")[1].text #欢迎字
if s == "欢迎您，":
    print ("login succ")
else:
    print ("login fail")
time.sleep(1)
driver.find_elements_by_css_selector("a[href='javascript:;']")[8].click()# 推出
driver.quit()