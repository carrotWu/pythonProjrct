

import os ,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

__url = "http://10.130.201.36:7001/index.jsp"
__un  = "0008054"
__pw  = "upic@123"
__baoanhao = "170512234"
__retext = ""

#非车定损管理定核损新增8 (ok)
def feichedingsunguan():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    driver.implicitly_wait(10)
    driver.switch_to_frame("leftFrame")

    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("非车定损管理").click()
    driver.find_element_by_link_text("定核损新增").click()


    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")
    driver.implicitly_wait(5)
    #报案号码
    driver.find_element_by_name('GcEvaluateMainDtoRegistNo').send_keys(__baoanhao)

    #查询
    driver.find_elements_by_css_selector('input[value="查询"]')[1].click()

    #点击报案号码
    driver.switch_to_frame('QueryResultFrame')
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
    time.sleep(4)
    # driver.implicitly_wait(5)
    driver.switch_to_alert().accept()
    time.sleep(4)
    driver.switch_to_alert().accept()

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")
    driver.implicitly_wait(5)
    time.sleep(5)

    #点击定损信息
    driver.find_element_by_css_selector('td[title="Loss"]').click()
    time.sleep(1)
    #财产相关定损信息
    driver.find_element_by_css_selector('input[value="+"]').click()

    #险别
    ele = driver.find_elements_by_name("gcEvaluatePropDtoKindCode")[1]
    ActionChains(driver).double_click(ele).perform()
    ele.send_keys(Keys.ENTER)
    ele.send_keys(Keys.ENTER)
    driver.implicitly_wait(3)
    #提交
    driver.find_element_by_css_selector('input[value="提交"]').click()


    #取操作成功
    time.sleep(4)
    driver.switch_to_default_content()
    driver.switch_to_frame('mainFrame')
    __fi = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
    __retext = __fi[0:4]
    print (__retext)
    driver.quit()
    return (__retext)

feichedingsunguan()


'''
操作成功！
该案需提交人工核损1级定损审核!报案号码：170511877定损号码：170511877#0#1定损序号：8提交审核成功！
'''