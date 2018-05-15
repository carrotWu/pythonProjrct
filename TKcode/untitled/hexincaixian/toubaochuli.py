
import  sys
import os ,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select

url = "http://10.130.201.36:7001/index.jsp"
un= "policy3@upic"
pw = "upic@123"
tbname = "奔驰"
id = "14092419800101009X"
address = "山西省大同市"
tbnumber=""

#投保处理1(ok)
def toubaochuli():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(url)
    driver.find_element_by_id("username").send_keys("policy3@upic")
    driver.find_element_by_id("password").send_keys("upic@123")
    driver.find_element_by_id("bt_submit").submit()

    time.sleep(4)
    driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理

    driver.find_element_by_link_text("承保子系统").click()
    driver.find_element_by_link_text("投保管理").click()
    driver.find_element_by_link_text("投保处理").click()

    driver.switch_to_default_content()  #需要切换回主页面

    driver.switch_to_frame("mainFrame")   #右边的frame
    driver.find_element_by_xpath(".//*[@id='RiskArea']/table[1]/tbody/tr/td[4]/input[1]").send_keys("1128")
    driver.find_element_by_xpath(".//*[@id='RiskArea']/table[1]/tbody/tr/td[4]/input[1]").send_keys(Keys.TAB)
    driver.find_element_by_xpath("/html/body/form/table[5]/tbody/tr/td/input[1]").send_keys(Keys.ENTER)
    time.sleep(2)

    #进入输入框

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame") #切换到右边的frame
    driver.implicitly_wait(4)
    driver.switch_to_frame("myFrame") #切换到里面的frame

    #中介人协议
    driver.find_element_by_name("GuMainAgreementNo").send_keys("010000000000400009")
    driver.find_element_by_name("GuMainAgreementNo").send_keys(Keys.TAB)
    time.sleep(1)

    #子协议代码
    driver.find_element_by_name("GuMainSolutionCode").send_keys("0100000000004000090004")
    driver.find_element_by_name("GuMainSolutionCode").send_keys(Keys.TAB)

    #投保人名称
    time.sleep(3)
    driver.find_element_by_name("AppliGuRelatedPartyInsuredName").send_keys(tbname)
    #证件号码

    driver.find_element_by_name("AppliGuRelatedPartyIdentifyNumber").send_keys(id)

    #增值服务类型,定位下拉框

    ser = Select(driver.find_element_by_name("AppliGuRelatedPartyStarLevel"))
    ser.select_by_index(1)

    #地址
    driver.find_element_by_xpath('//*[@id="InsuredGuAppliPartyCorInsuredAddress"]/td[3]/textarea').send_keys("山西省长治市")
    #邮政编码
    driver.find_element_by_xpath('//*[@id="InsuredGuAppliPartyCorInsuredPostCodeOP"]/td[2]/input').send_keys("047500")
    #客户识别
    driver.find_element_by_name('buttonInsuredGuAppliPartyCustomerIdentify').click()
    time.sleep(2)
    driver.switch_to_alert().accept() #用户重复时主调
    time.sleep(1)
    #保存客户

    driver.find_element_by_name('buttonSaveCustomer').click()
    time.sleep(1)
    driver.switch_to_alert().accept()
    #确定
    driver.find_element_by_id("saveButton").click()
    time.sleep(2)
    #产品方案代码/名称

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame") #切换到右边的frame
    driver.implicitly_wait(5)
    driver.switch_to_frame("myFrame") #切换到里面的frame
    driver.implicitly_wait(5)
    driver.switch_to_frame("RiskFrame")
    driver.switch_to_frame("myFrame")
    #特别约定

    driver.find_element_by_link_text("特别约定").click()
    driver.find_element_by_name("buttonMyClausesAdd").click()  #点+号
    time.sleep(2)

    #设置特别约定代码
    driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys('0326')
    driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys(Keys.TAB)
    time.sleep(1)

    driver.find_element_by_name("GuRiskDynamicFieldAI").send_keys("1128A00001")
    driver.find_element_by_name("GuRiskDynamicFieldAI").send_keys(Keys.TAB)
    time.sleep(1)
    #保存
    driver.find_element_by_id("saveButton").click()
    time.sleep(5)

    #进入标的里面的险别
    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame") #切换到右边的frame
    driver.implicitly_wait(5)
    driver.switch_to_frame("myFrame") #切换到里面的frame
    driver.implicitly_wait(5)
    driver.switch_to_frame("RiskFrame")
    driver.implicitly_wait(5)
    driver.find_elements_by_id("mySubTD")[1].click()
    driver.switch_to_frame("myFrame")
    driver.implicitly_wait(10)

    #增加保障
    driver.find_element_by_name("button_ItemKind_Insert").click()

    #险别
    driver.find_elements_by_name("GuItemKindKindName")[1].send_keys("1128001")
    driver.find_elements_by_name("GuItemKindKindName")[1].send_keys(Keys.TAB)

    #每份赔偿限额

    driver.find_elements_by_name("GuItemKindUnitInsured")[1].send_keys("100000")

    #费率
    fl = 'var q = document.getElementsByName("GuItemKindRate");q[1].value=%d;' % 0.056
    driver.execute_script(fl)

    #方案代码/名称
    driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[1]").send_keys("1128A00001")
    driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[3]").send_keys("体育运动个人意外险")

    #风险等级

    fxdj = 'var q = document.getElementsByName("GuItemAcciOccupationLevel");q[0].value=%d;' % 1
    driver.execute_script(fxdj)

    #保存
    driver.find_element_by_id('saveButton').click()
    time.sleep(5)
    #取当前的窗口句柄
    __win1 = driver.current_window_handle
    time.sleep(5)
    #人员列表 (弹出新窗口)
    driver.find_element_by_xpath("//*[@id='ItemAcci']/thead/tr/td[16]/input").click()

    all_handle = driver.window_handles
    for handle in all_handle:
        if handle != __win1:
            driver.switch_to_window(handle) #进入到新的窗口

            driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input").click()#点击增加

            driver.switch_to_frame("QueryResultFrame")
            #被保险人名称
            driver.find_element_by_xpath("//*[@id='ItemAcciList']/tbody/tr[2]/td[2]/input").send_keys(tbname)

            #证件号码
            driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[3]/td[4]/input').send_keys(id)
            #详细地址
            driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[7]/td[4]/input').send_keys(address)

            #生存受益人名称
            driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[13]/td[2]/input').send_keys(tbname)
            #证件号码
            driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[14]/td[4]/input').send_keys(id)

            #保存
            driver.find_element_by_xpath('//*[@id="saveBackTr"]/td/input').click()

            #单击确定
            driver.switch_to_alert().accept()
            time.sleep(3)
            driver.close()
            driver.switch_to_window(__win1)

    for handle in all_handle:
        if handle == __win1:
            #提交复合
            driver.switch_to_default_content()
            driver.implicitly_wait(5)
            driver.switch_to_frame("mainFrame")
            driver.find_element_by_name("Save").click()
            time.sleep(2)
            tbdan = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td").text
            tbnumber = tbdan[6:28]
            print (tbnumber)

            time.sleep(2)
            driver.quit()

    return tbnumber
toubaochuli()