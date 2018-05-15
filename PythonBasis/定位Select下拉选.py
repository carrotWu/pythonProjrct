#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
url='F:\\pythonProjrct\\Select.html'
class focusSelect:
    def Sselect(self,url):
        driver.get(url)
        #先定位到Select标签
        selectTag=driver.find_element_by_css_selector('#status')
        #1、通过index选择
        Select(selectTag).select_by_index(1)
        sleep(3)
        #2、通过value选择
        Select(selectTag).select_by_value("2")
if __name__ == '__main__':
    functionLibrary=focusSelect()
    functionLibrary.Sselect(url)
