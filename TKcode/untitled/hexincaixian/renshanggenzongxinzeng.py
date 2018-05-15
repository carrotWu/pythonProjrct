
import os ,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create by Grape Shi

__url = "http://10.130.201.36:7001/index.jsp"
__un= "0008054"
__pw = "upic@123"
tbnumber="0330100112820170000417"
__baoanhao = "170512234"
__retext =""


#人伤跟踪新增7(ok)
def renshenggenzongxinzeng():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    driver.implicitly_wait(10)
    driver.switch_to_frame("leftFrame")

    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("人伤跟踪管理").click()
    driver.find_element_by_link_text("人伤跟踪新增").click()

    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")

    #报案号码
    driver.find_element_by_name('gcRegistPolicyDtoRegistNo').send_keys(__baoanhao)

    #查询
    driver.find_elements_by_css_selector('input[value="查询"]')[1].click()

    #点击报案号码
    driver.switch_to_frame('QueryResultFrame')
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
    time.sleep(2)


    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    #点+号
    driver.find_element_by_css_selector('input[value="+"]').click()

    #险别
    xb = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoKindCode");q[1].value = "1128001";'
    driver.execute_script(xb)

    #费用
    fy = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoFeeTypeCode");q[1].value = "04";'
    driver.execute_script(fy)

    #点位金额
    je = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoUnitLossAmount");q[1].value = 200;'
    driver.execute_script(je)

    #点数量
    sl = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoLossQuantity");q[1].value = 1;'
    driver.execute_script(sl)

    time.sleep(5)

    #损失
    ss= 'var q = document.getElementsByName("gcCarEvaluateFeeDtoSumLoss");q[1].value = 200;'
    driver.execute_script(ss)

    #定损
    ds= 'var q = document.getElementsByName("gcCarEvaluateFeeDtoSumDefLoss");q[1].value = 200;'
    driver.execute_script(ds)

    driver.find_element_by_css_selector('input[value="提交"]').click()
    driver.switch_to_alert().accept()

    #取值
    time.sleep(4)
    driver.switch_to_default_content()
    driver.switch_to_frame('mainFrame')
    fi = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
    __retext = fi[0:4]
    print (__retext)
    driver.quit()
    return  __retext

renshenggenzongxinzeng()