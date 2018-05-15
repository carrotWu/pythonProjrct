#coding=utf-8
def login(username,password):
    from selenium import webdriver
    driver=webdriver.Firefox()
    driver.get("http://www.xxx.com")#进入登录页面
    driver.find_element_by_id('username').send_keys("username")#输入账号
    driver.find_element_by_id('password').send_keys("password")#输入密码
    driver.find_element_by_id('submit').click()  # 点击登录
    #此处应该调用验证用户名和密码的方法
    if 1>0:#如果正确
        driver.get("http://xxxxx")#跳转到首页
    else:
    #验证不正确输出用户名或者密码错误
        print "用户名或密码错误"
    driver.quit()
