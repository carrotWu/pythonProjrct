#coding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#绝对路径
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]'
                             '/div/form/span[1]/input').send_keys('51zxw')

#相对定位--定位到input标签中为wd的元素
driver.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')

#相对定位定位input标签中name属性为wd的元素
driver.find_element_by_xpath("//input[@name='wd']").send_keys('selenium')

#相对定位所有标签元素中,class属性为s_ipt的元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys('python3')

sleep(3)
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()


