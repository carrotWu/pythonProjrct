

import os ,time
from selenium import webdriver
from selenium.webdriver.support.ui  import Select

#create by Grape Shi

url = "http://10.130.201.36:7001/index.jsp"
un= "uwprpall@upic"
pw = "upic@123"
tbnumber="0330100112820170000451"
baodanhao =""



#任务处理2(ok)
def renwuchuli():

    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(url)
    driver.find_element_by_id("username").send_keys(un)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id("bt_submit").submit()

    time.sleep(4)
    driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理

    driver.find_element_by_link_text("审核平台子系统").click()
    driver.find_element_by_link_text("核保审核").click()
    driver.find_element_by_link_text("任务处理").click()

    driver.switch_to_default_content()  #需要切换回主页面

    driver.switch_to_frame("mainFrame")   #右边的frame

    #申请单号
    driver.find_element_by_name("GwWfLogDtoBusinessNo").send_keys(tbnumber)
    #保存
    driver.find_element_by_name("buttonQuery").click()
    driver.implicitly_wait(5)
    driver.switch_to_frame("QueryResultFrame")

    #业务号
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()

    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    driver.switch_to_frame("myFrame")

    #分保试算
    win1 = driver.current_window_handle

    driver.find_element_by_xpath('//*[@id="ResultTable"]/tfoot/tr/td[1]/input').click()


    time.sleep(4)
    all_h = driver.window_handles
    for h in all_h:
        if h !=win1:
            driver.switch_to_window(h)
            driver.close()
            driver.switch_to_window(win1)

    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    driver.switch_to_frame("myFrame")

    #审批片语：同意
    __sec = Select(driver.find_element_by_name("NotionContent"))
    __sec.select_by_index(2)

    #审核意见
    driver.find_element_by_xpath('/html/body/form/div/table[4]/tbody/tr/td[9]/input').click()
    allh=driver.window_handles
    for h in allh:
        if h != win1:
            driver.switch_to_window(h)
            driver.close()
            driver.switch_to_window(win1)

    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    driver.switch_to_frame("myFrame")
    time.sleep(3)
    #审核通过
    driver.find_element_by_xpath("/html/body/form/div/table[4]/tbody/tr/td[2]/input").click()
    time.sleep(1)
    driver.switch_to_alert().accept()

    #取保单号
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    time.sleep(5)
    retext = driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td").text
    baodanhao =retext[-22::]
    print (baodanhao)
    driver.quit()
    return baodanhao

renwuchuli()

##保单生效时间变更3(ok)
#update gupolicycopyrisk set startdate=to_date('2017-09-20 01:00:00','yyyy-mm-dd hh:mi:ss') where policyno='6330100112820170000042'
#update GuPolicyCopyEndorHead set VALIDDATE=to_date('2017-09-20 01:00:00','yyyy-mm-dd hh:mi:ss') where policyno='6330100112820170000042'