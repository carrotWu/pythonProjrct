#coding=utf-8
#多敞口切换操作
#案例：带来我要自学网Selenium课程主页,然后打开课程详情页面
#再回到课程主页打开3-1课程详情页面

from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
#打开selenium课程主页
driver.get("http://www.51zxw.net/list.aspx?cid=615")
#获取课程主页的句柄(标记)
selenium_index=driver.current_window_handle
sleep(2)
#点击2-1课程连接，进入课程详情页面
driver.find_element_by_partial_link_text('2-1').click()
sleep(4)
#跳转的主页窗口，点击3-1课程
driver.switch_to_window(selenium_index)
sleep(3)
driver.find_element_by_partial_link_text('3-1').click()
sleep(3)
driver.quit()
