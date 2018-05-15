#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#根据id定位
driver.find_element_by_css_selector('#tj_login').send_keys("username")
#根据class定位
driver.find_element_by_css_selector('.s_ipt').send_keys('python')
#通过属性来定位
driver.find_element_by_css_selector("[autocomplete='off']").send_keys('pycharm')

sleep(3)
driver.find_element_by_id('su').click()
driver.get("http://www.51zxw.net")
sleep(3)
#通过元素层级来定位
# driver.find_element_by_css_selector("form#loginForm>ul>input").send_keys("51zxw")
sleep(5)
driver.quit()
