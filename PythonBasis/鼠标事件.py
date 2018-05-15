#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
#ActionChains类提供了鼠标操作的常见方法
# perform()             执行所有ActonChains中存储的行为
# context_click()       右击
# double_click()        双击
# drag_and_drop()       拖动
# move_to_element()     鼠标悬停
driver = webdriver.Firefox()
class Mouse_Click:
    #右击
    def Rclick(self,css):
        driver.get("http://www.runoob.com/")
        driver.maximize_window()
        #先定位到要操作的元素
        tag=driver.find_element_by_css_selector(css).click()
        #对目标元素进行右击操作
        ActionChains(driver).context_click(tag).perform()
    #悬停
    def move_to_Elemnt(self,css):
        driver.get("http://www.baidu.com/")
        #先定位到要操作的元素
        mov=driver.find_element_by_css_selector(css)
        #对该元素进行悬停操作
        ActionChains(driver).move_to_element(mov).perform()
        #点击悬停下拉菜单的元素
        driver.find_element_by_link_text("搜索设置").click()
    #双击
    def DbClick(self,css):
        driver.get("url")
        #先定位到要操作的元素
        dbTag=driver.find_element_by_name(css)
        #对该元素进行双击操作
        ActionChains(driver).double_click(dbTag).perform()
    #拖放
    def Drag_drop(self,css1,css2):
        driver.get("url")
        # 要拖动的源元素
        sourceTag = driver.find_element_by_css_selector(css1)
        #要拖到的目标地元素
        targetTag=driver.find_element_by_css_selector(css2)
        # 对该元素进行拖放操作
        ActionChains(driver).drag_and_drop(sourceTag,targetTag).perform()

if __name__ == '__main__':
    functionLibrary=Mouse_Click()
    #functionLibrary.Rclick('h4')
    functionLibrary.move_to_Elemnt('a[name="tj_settingicon"]')
