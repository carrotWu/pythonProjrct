#coding=utf-8
from selenium import webdriver
from time import sleep
class Login():
    def user_login(self,driver):
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('wuyubo')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('123456')

        driver.find_element_by_name('Submit').click()

    def user_logout(self, driver):
        driver.find_element_by_link_text('退出').click()
        sleep(2)
        driver.switch_to_alert().accept()

#调试
if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://localhost")
    driver.implicitly_wait(10)

    Login().user_login(driver)
    Login().user_logout(driver)



