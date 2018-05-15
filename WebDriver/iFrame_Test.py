#coding=utf-8
#frame嵌套页面元素定位
#案例：在Frame.html文件中定位搜狗搜索页面，进行搜索操作。
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
file_path="F:\\pythonProjrct\\WebDriver\\iFrame.html"
driver.get(file_path)

#切換到frame頁面
driver.switch_to.frame("search")
#定位到搜索按鈕輸入关键词
driver.find_element_by_css_selector("#query").send_keys("selenium")
sleep(3)
driver.find_element_by_css_selector("#stb").click()
sleep(3)
driver.quit()
