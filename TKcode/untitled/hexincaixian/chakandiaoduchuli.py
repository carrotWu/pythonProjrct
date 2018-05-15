

import  sys
import os ,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#create by Grape Shi


__url = "http://10.130.201.36:7001/index.jsp"
__un= "0008054"
__pw = "upic@123"
__baoanhao ="170512234"
__retext = ""

#查勘调度处理5(ok)
def chakandiaodu():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    time.sleep(4)
    driver.switch_to_frame("leftFrame")

    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("调度管理").click()
    driver.find_element_by_link_text("查勘调度").click()
    driver.find_element_by_link_text("查勘调度处理").click()

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")

    #报案号码
    driver.find_element_by_xpath('//*[@id="BeforeOverViewMain1"]/tbody/tr[1]/td[2]/input').send_keys(__baoanhao)
    #点击查询
    driver.find_element_by_xpath('//*[@id="BeforeOverViewResult"]/tbody/tr[2]/td/input').click()

    driver.switch_to_frame("QueryResultFrame")

    #点击报案号码
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[2]/a').click()

    #
    driver.switch_to_alert().accept()


    time.sleep(5)
    driver.switch_to_default_content()
    driver.implicitly_wait(4)
    driver.switch_to_frame("mainFrame")

    #对象类型
    driver.find_element_by_name('DelegateDtoObjectType').send_keys("004")

    #调度单位
    driver.find_element_by_name('DelegateDtoCheckUnitCode').send_keys("01")
    driver.find_element_by_name('DelegateDtoCheckUnitCode').send_keys(Keys.TAB)
    #第一查勘人
    driver.find_element_by_name('DelegateDtoCheckerCode1').click()
    driver.find_element_by_name('DelegateDtoCheckerCode1').send_keys("0008054")

    #选择
    driver.find_element_by_xpath('//*[@id="changePerson"]/tbody/tr/td[1]/input[1]').send_keys(Keys.SPACE)

    #任务指派
    driver.find_element_by_css_selector('input[value="任务指派"]').click()

    #提交
    driver.find_element_by_css_selector('input[value="提交"]').click()
    time.sleep(5)

    #取报案号
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    su = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
    __retext = su[0:4]
    print (__retext)
    driver.quit()
    return  __retext
chakandiaodu()

'''

操作成功！
'''