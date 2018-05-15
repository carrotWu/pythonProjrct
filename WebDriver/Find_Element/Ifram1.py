#coding=utf-8
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.126.com")
driver.switch_to_frame("x-URS-iframe")  #需先跳转到iframe框架
#driver.find_element_by_class_name("j-inputtext dlemail")
time.sleep(3)
driver.find_element_by_name("email").send_keys("123")
time.sleep(3)
driver.find_element_by_name("password").send_keys("12345")
time.sleep(3)
driver.find_element_by_id("dologin").click()
time.sleep(3)
driver.quit()