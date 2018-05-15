#coding=utf-8
from selenium import webdriver
from time import sleep

class Login():
    def user_login(self,driver,username,password):
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)

        driver.find_element_by_name('Submit').click()

    def user_loginout(self,driver):
        driver.find_element_by_link_text('退出').click()
        sleep(3)
        driver.switch_to_alert().accept()

