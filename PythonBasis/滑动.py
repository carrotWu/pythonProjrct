#coding=utf-8
#滚动条操作
from  selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
#1.滑动到底端端、顶端
#2.定向滑动到标签
url="http://www.runoob.com/python/python-intro.html"
class ScrollBar:
    #滑动到底端
    def ScrollTo_Buttom(self):
        driver.get(url)
        driver.maximize_window()
        # 将滚动调拖到最底部
        js = "var action=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
    #滑动到顶部
    def ScrollTo_Top(self):
        js="var action=document.documentElement.scrollTop=0"
        driver.execute_script(js)

    #滑动到具体标签
    def ScrollTo_Focus(self,value):
        dr=driver.find_element_by_css_selector(value)
        driver.execute_script("arguments[0].scrollIntoView()",dr)

if __name__ == '__main__':
    functionLibrary=ScrollBar()
    functionLibrary.ScrollTo_Buttom()
    sleep(3)
    # functionLibrary.ScrollTo_Top()
    # sleep(3)
    # driver.quit()
    #functionLibrary.ScrollTo_Focus('a[href="/python/python-modules.html"]')
    driver.find_element_by_css_selector('a[href="/python/python-modules.html"]').click()
