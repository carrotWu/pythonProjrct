#coding=utf-8
#警告弹窗处理
#案例：点击百度首页设置按钮，然后进入搜索设置页面，点击“保存设置”或“恢复默认”按钮，处理警告弹窗窗口
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_link_text('设置').click()
sleep(2)
driver.find_element_by_link_text('搜索设置').click()
sleep(3)
driver.find_element_by_link_text('保存设置').click()
sleep(3)

#处理警告窗口
alert=driver.switch_to_alert()
alert.accept()
sleep(2)

sleep(2)
driver.quit()
