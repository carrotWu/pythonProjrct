
import  sys
import os ,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select

#create by Grape Shi
__url ="http://10.130.201.36:7001/index.jsp"
__un  ="0008054"
__pw = "upic@123"
__baoanhao ="170512234"
__retext = ""

##查勘新增6(ok)
def chakanxinzeng():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    time.sleep(3)
    driver.switch_to_frame("leftFrame")

    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("查勘管理").click()
    driver.find_element_by_link_text("查勘新增").click()


    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")

    #报案号码
    driver.find_element_by_name('GcSurveyMainDtoRegistNo').send_keys(__baoanhao)

    #查询
    driver.find_element_by_xpath('//*[@id="BeforeOverViewResult"]/tbody/tr[2]/td/input').click()

    driver.switch_to_frame("QueryResultFrame")
    #报案号码
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[2]/a').click()
    time.sleep(4)
    driver.switch_to_alert().accept()
    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")

    time.sleep(3)


    #人伤信息(class动态变化)
    driver.find_element_by_css_selector('td[title="personInfomation"]').click()
    #+
    driver.find_element_by_xpath('//*[@id="person"]/tfoot/tr[1]/td/p/input').click()
    time.sleep(3)

    #点击详细信息

    driver.find_elements_by_css_selector('input[value="详细信息"]')[1].click()
    time.sleep(2)
    driver.switch_to_frame("detailFrame")

    #姓名
    xingming = driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[1]/td[4]/input[2]')
    ActionChains(driver).double_click(xingming).perform()
    driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[1]/td[4]/input[2]').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[1]/td[4]/input[2]').send_keys(Keys.ENTER)
    driver.implicitly_wait(4)

    #性别
    __xb = Select(driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[2]/td[2]/select'))
    __xb.select_by_index(2)


    #职业大类
    driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[6]/td[2]/input[1]').send_keys("00101")
    driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[6]/td[2]/input[1]').send_keys(Keys.TAB)
    time.sleep(2)
    #意外伤害
    driver.find_element_by_link_text("意外伤害").click()
    driver.find_element_by_css_selector('input[value="IC017"]').click()
    #保存
    driver.find_element_by_xpath('/html/body/form/table[8]/tbody/tr/td[1]/input').click()

    #基本信息
    time.sleep(3)
    driver.switch_to_default_content()
    driver.switch_to_frame('mainFrame')
    driver.find_element_by_css_selector('td[title="main"]').click()
    time.sleep(3)

    #财产查勘
    #点+号 ?
    driver.find_element_by_xpath('//*[@id="propFee"]/tfoot/tr/td/p/input').click()
    driver.implicitly_wait(5)

    #险别
    __xb = driver.find_elements_by_name('GcSurveyPropDtoKindCode')[1]
    ActionChains(driver).double_click(__xb).perform()
    __xb.send_keys(Keys.ENTER)
    __xb.send_keys(Keys.ENTER)


    #险别估损金额
    driver.find_elements_by_name('GcSurveyPropDtoSumLoss')[1].send_keys("200")

    #人伤查勘估损
    driver.find_element_by_xpath('//*[@id="injured"]/tfoot/tr/td/p/input').click()
    time.sleep(2)
    #姓名
    __xm =driver.find_elements_by_name('GcSurveyPersonFeeDtoPersonCName')[1]
    ActionChains(driver).double_click(__xm).perform()
    __xb.send_keys(Keys.ENTER)
    __xb.send_keys(Keys.ENTER)


    #险别
    __xb1 = driver.find_elements_by_name('GcSurveyPersonFeeDtoKindCode')[1]
    ActionChains(driver).double_click(__xb1).perform()
    __xb1.send_keys(Keys.ENTER)
    __xb1.send_keys(Keys.ENTER)

    #险别估损金额
    driver.find_elements_by_name('GcSurveyPersonFeeDtoSumLoss')[1].send_keys("200")

    #查勘报告
    # driver.find_element_by_name('GcSurveyMainDtoDamageDescription').click()
    driver.find_element_by_id('img2').click()
    #出现经过
    driver.find_element_by_name('GcSurveyMainDtoDamageDescription').send_keys("Me Against the World")

    #查勘新增
    driver.find_element_by_name('GcSurveyMainDtoContext').send_keys("让世界感受痛楚")
    #报损及损失核定
    driver.find_element_by_name('GcSurveyMainDtoExt1').send_keys("没人知道我的痛苦有多深")


    #处理意见
    driver.find_element_by_id('img1').click()
    driver.find_element_by_name('GcSurveyMainDtoExt6').send_keys("同意")

    #点提交
    driver.find_element_by_xpath('//*[@id="button"]/tbody/tr/td/input[4]').click()
    driver.switch_to_alert().accept()

    #取文本
    time.sleep(5)
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    succ = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
    __retext = succ[0:4]
    print (__retext)
    driver.quit()
    return  __retext
chakanxinzeng()