#coding=utf-8
#元素等待
#a.显示等待是对某一元素进行相关等待判定；
#b.隐式等待不针对某一元素进行等待，全局元素等待。

#相关模块
#a.WebdriverWait 显示等待针对元素必用
#b.expected condtions预期条件类（里面包含方法可以调用，用于显示等待）
#c.NoSuchElementException 用于隐式等待抛出异常
#d.By 用于元素定位

#1.显示等待
#案例：检测百度页面搜索按钮是否存在，
# 存在就输入关键词“自学网 Selenium” 然后点击搜索
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

time_out=30
driver.find_element_by_css_selector("#kw").send_keys("Selenium")

sleep(2)

#显示等待--判断搜索按钮是否存在
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"su")))
element.click()
sleep(3)



def click_by_css(css):
    ele=WebDriverWait(driver,time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))
    '''等待元素加载完毕可见'''
    ele.click()
def click_by_id(id):
    ele=WebDriverWait(driver,time_out).until((EC.visibility_of_element_located((By.ID,id))))
    ele.click()
def send_by_css(css,content):
    ele=WebDriverWait(driver,time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))
    ele.send_keys(content)
def click_by_css_elements(css):
    ele=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.mnav')))
    '''判断是否至少有一个元素在页面中可见，如果定位 到就返回列表'''
    ele[0].click()

#等待Frame并且切入
def switch_to_frame(frame_id):
    WebDriverWait(driver, 10, 0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,frame_id)))
    '''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''

#等待alert窗口出现再处理
def allert_accept():
    instance = WebDriverWait(driver, 10).until(EC.alert_is_present())
    '''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
    driver.switch_to_alert().accept()
    return instance

#等待标签隐藏
def invisibility_of_element():
    WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR,'#sdf')))
    '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''







driver.quit()


