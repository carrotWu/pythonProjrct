
import os ,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#create by Grape Shi

__url  = "http://10.130.201.36:7001/index.jsp"
baodan = "6330100112820170000042"
__un = "0008054"
__pw = "upic@123"
__tbname = "虞姬"
__id = "140181198101010058"
__address = "山西省大同市"
__tel = "13901234567"
__baoannb=""


#报案新增4(ok)
def baoanxinzeng():

    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    time.sleep(4)
    driver.switch_to_frame("leftFrame")
    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("报案管理").click()
    driver.find_element_by_link_text("报案新增").click()

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")
    #报案人
    driver.find_element_by_name("registReportorName").send_keys(__tbname)
    #报案人电话
    driver.find_element_by_name("registReportorPhoneNumber").send_keys(__tel)

    #保单信息
    win1 = driver.current_window_handle
    driver.find_element_by_xpath('//*[@id="Query"]/tbody/tr/td/input').click()

    #
    all_h = driver.window_handles
    time.sleep(4)
    for h in all_h:
        if h !=win1:
            driver.switch_to_window(h)
            driver.implicitly_wait(4)
            driver.find_element_by_name("queryPolicyPolicyNo").send_keys(baodan)
            #查询
            driver.implicitly_wait(4)
            driver.find_element_by_css_selector("input[value='查询']").click()
            driver.implicitly_wait(30)
            driver.switch_to_frame("QueryResultFrame")

            driver.find_element_by_name("checkboxSelect").send_keys(Keys.SPACE)
            driver.find_element_by_css_selector("input[value='新增']").click()
            time.sleep(5)
            driver.close()
            driver.switch_to_window(win1)

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame") #切换到右边的frame
    #出险原因
    driver.find_element_by_name("registDamageCode").send_keys("109001")
    driver.find_element_by_name("registDamageCode").send_keys(Keys.TAB)

    #出险地点
    driver.find_element_by_name("registDamageAddress").send_keys(__address)

    #出险摘要
    driver.find_element_by_xpath('//*[@id="resume"]/tbody/tr/td/textarea').send_keys(__address)

    #提交
    driver.find_element_by_css_selector("input[value='提交']").click()
    time.sleep(5)
    driver.switch_to_alert().accept()
    time.sleep(5)

    #取报案号
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    webtext=driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[3]/td').text
    print (webtext)
    __baoannb =webtext[-9::]
    driver.quit()
    print (__baoannb)
    return __baoannb
baoanxinzeng()