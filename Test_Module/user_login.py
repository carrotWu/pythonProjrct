#coding=utf-8
#自动化测试模型
#自动化测试模型可以看作自动化测试框架与工具设计的思想。
#自动化测试模型分为：线性模型，模块化驱动测试、数据驱动、关键词驱动。

#(1)线性模型
#线性脚本中每个脚本都相互独立，且不会产生其他依赖与调用，其实就是简单模拟用户某个操作流程的脚本。
#案例：在帝国软件主页自动登录和退出操作
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://localhost")

#输入用户名
driver.find_element_by_name("username").click()
driver.find_element_by_name("username").send_keys("wuyubo")
#输入密码
driver.find_element_by_name("password").click()
driver.find_element_by_name("password").send_keys("123456")
#点击登录
driver.find_element_by_name("Submit").click()
sleep(3)

#退出
driver.find_element_by_link_text("退出").click()
sleep(2)
driver.switch_to_alert().accept()
sleep(2)
driver.quit()