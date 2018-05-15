#coding=utf-8
#基于Cookie绕过验证码自动登录
#案例：使用Cookie绕过百度验证码自动登录账户。
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
#手动添加cookie
