#coding=utf-8
from selenium import webdriver
#数据驱动测试
#模块驱动的模型虽然解决了脚本的重复问题，但是需要测试不同数据的用例时，
# 模块驱动的方式就不很适合了。 数据驱动就是数据的改变从而驱动自动化测试的执行，
# 最终引起测试结果的改变。 装载数据的方式可以是列表、字典或是外部文件（txt、csv、xml、excel）
# 目的就是实现数据和脚本的分离。

from LoginClass_para import *
driver=webdriver.Firefox()
driver.get("http://localhost")
Login().user_login(driver,'wuyubo','123456')
sleep(3)
Login().user_loginout(driver)
sleep(3)
driver.quit()