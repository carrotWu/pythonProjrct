#coding=utf-8
from  selenium import webdriver
from time import sleep
#获取火狐浏览器驱动对象
driver=webdriver.Firefox()
#访问百度首页
driver.get('http://www.baidu.com')
#窗口最大化
driver.maximize_window()
sleep(2)
#访问虾米首页
driver.get("https://www.zhihu.com")
#调节窗口大小
driver.set_window_size(400,800)
#刷新窗口
driver.refresh()
sleep(2)
#返回到上一个网页
driver.back()
sleep(2)
#前进网页
driver.forward()
sleep(2)
#关闭浏览器
driver.quit()