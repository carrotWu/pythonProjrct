#coding=utf-8
#模块化驱动测试
#线性模型虽然每个用例都可以拿出来独立运行，但是会有重复代码
#把重复的操作代码封装成公用的模块，直接调用。

from loginClass import *
driver=webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)
Login().user_login(driver)
Login().user_logout(driver)

