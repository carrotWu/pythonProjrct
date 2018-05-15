import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select
import cx_Oracle
import xlrd
from xlutils.copy import copy
#create by grape Shi

#####basic infora#####
url = "http://10.130.201.36:7001/index.jsp"
tbun = "policy3@upic"                   #投保用户名
heun= "uwprpall@upic"                   #核保用户名
lpun= "0008054"                         #理赔用户
pw = "upic@123"                         #密码
tbname = "凌志名"                        #
id = "140501198001011598"               #
address = "山西省"
postcode = "047500"
tel = "13601234567"
skname = "宫本武藏"                      #收款人
bankname = "中国银行"                    #收款银行
#######################

##oracle##
orcle_url= "upiccore/sinosoft@10.130.201.118:1521/tkpi"
####

def t9901():#投保处理1(ok)
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(url)
    driver.find_element_by_id("username").send_keys(tbun)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id("bt_submit").submit()
    time.sleep(2)
    driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理
    driver.find_element_by_link_text("承保子系统").click()
    driver.find_element_by_link_text("投保管理").click()
    driver.find_element_by_link_text("投保处理").click()
    driver.switch_to_default_content()  #需要切换回主页面
    driver.switch_to_frame("mainFrame")   #右边的frame
    driver.find_element_by_xpath(".//*[@id='RiskArea']/table[1]/tbody/tr/td[4]/input[1]").send_keys("9901")
    driver.find_element_by_xpath(".//*[@id='RiskArea']/table[1]/tbody/tr/td[4]/input[1]").send_keys(Keys.TAB)
    driver.find_element_by_xpath("/html/body/form/table[5]/tbody/tr/td/input[1]").send_keys(Keys.ENTER)
    time.sleep(2)
    #进入输入框
    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame") #切换到右边的frame
    driver.implicitly_wait(4)
    driver.switch_to_frame("myFrame") #切换到里面的frame


    #业务方式
    ser = Select(driver.find_element_by_name("GuMainBusinessMode"))
    ser.select_by_index(0)


    #业务归属
    driver.find_element_by_name('GuMainCompanyCode').send_keys('0104000001')
    time.sleep(1)
    driver.find_element_by_name('GuMainCompanyCode').send_keys(Keys.TAB)
    time.sleep(1)

    #业务员
    fl = 'var q = document.getElementsByName("GuMainSalesmanCode");q[0].value="%s";' % "S000000081"
    driver.execute_script(fl)

    #渠道小类
    fl = 'var q = document.getElementsByName("GuMainChannelTip");q[0].value="%s";' % "01010101"
    driver.execute_script(fl)


    time.sleep(3)
    driver.find_element_by_name("AppliGuRelatedPartyInsuredName").send_keys(tbname)
    #证件号码
    driver.find_element_by_name("AppliGuRelatedPartyIdentifyNumber").send_keys(id)
    #增值服务类型,定位下拉框
    ser = Select(driver.find_element_by_name("AppliGuRelatedPartyStarLevel"))
    ser.select_by_index(1)
    #地址
    driver.find_element_by_xpath('//*[@id="InsuredGuAppliPartyCorInsuredAddress"]/td[3]/textarea').send_keys(address)
    #邮政编码
    driver.find_element_by_xpath('//*[@id="InsuredGuAppliPartyCorInsuredPostCodeOP"]/td[2]/input').send_keys(postcode)
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
    driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys('0083')
    driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys(Keys.TAB)
    time.sleep(1)
    #产品方案代码名称
    driver.find_element_by_name("GuRiskDynamicFieldAI").send_keys("1109A01I01")
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
    driver.find_elements_by_name("GuItemKindKindName")[1].send_keys("1109016")
    driver.find_elements_by_name("GuItemKindKindName")[1].send_keys(Keys.TAB)
    #每份赔偿限额
    driver.find_elements_by_name("GuItemKindUnitInsured")[1].send_keys("100000")
    #费率
    fl = 'var q = document.getElementsByName("GuItemKindRate");q[1].value=%s;' % "0.056"
    driver.execute_script(fl)
    #方案代码/名称
    driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[1]").send_keys("1109A01I01")
    driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[3]").send_keys("中民泰康住院宝（2017升级版）-少儿版-方案一")
    #风险等级
    fxdj = 'var q = document.getElementsByName("GuItemAcciOccupationLevel");q[0].value=%d;' % 1
    driver.execute_script(fxdj)
    #保存
    driver.find_element_by_id('saveButton').click()
    time.sleep(2)
    #应收保费1
    # yxbf = 'var q = document.getElementsByName("GuItemKindGrossPremium");alert(q.length);'
    yxbf = 'var q = document.getElementsByName("GuItemKindGrossPremium");alert(q[1].innerText);'
    driver.execute_script(yxbf)
    # zhi = driver.find_elements_by_name('GuItemKindGrossPremium')[1].get_attribute('value')
    zhi = driver.find_elements_by_name('GuItemKindGrossPremium')[1].text
    print (zhi)
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
            # driver.find_element_by_css_selector("input[value='增加(A)']").click()
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
        if handle == __win1: #提交复合
            driver.switch_to_default_content()
            driver.implicitly_wait(5)
            driver.switch_to_frame("mainFrame")
            driver.find_element_by_name("Save").click()
            time.sleep(2)
            tbdan = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td").text
            toubaodanhao = tbdan[6:28]
            print (tbdan)
            time.sleep(2)
            driver.quit()
            time.sleep(3)

t9901()