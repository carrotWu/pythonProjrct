import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select
import cx_Oracle
import xlrd
from xlutils.copy import copy
from decimal import Decimal
#create by grape Shi

#####basic infora#####
url = "http://10.130.201.229:7011/index.jsp"
tbun = "manager@upic"                   #投保用户名
heun= "hebao1@upic.com"                 #核保用户名
lpun= "payment@upic.com"                #收付用户
pw = "upic@123"                         #密码
hbpw="upic@12345"

address = "山西省"
postcode = "047500"
tel = "13613552859"
caricon = "雷克萨斯"
area    = "370000"
#######################

##oracle##
orcle_url= "upiccore/sinosoft@10.130.201.118:1521/tkpi"
####


def getDataFromSheet(excelPath=r'D:\JettechAgent1.6.0\身份证.xls', sheetName="Sheet1"):
    dataList = []
    # 读取excel数据
    data = xlrd.open_workbook(excelPath)
    # 获取一个工作表
    table = data.sheet_by_name(sheetName)
    # 获取工作表的总行数
    nrows = table.nrows
    for line in range(nrows):
        rowData = table.row_values(line)
        if rowData[3] == "":
            dataList.append(rowData)
            wb = copy(data)
            ws = wb.get_sheet(0)
            ws.write(line, 3, "1")
            ws.write(line, 4, time.ctime())
            wb.save(excelPath)
            break
    if len(dataList) == 0:
        return "数据读取完毕"
    else:
        indentityId = dataList[0][0]
        name = dataList[0][1]
        sex = dataList[0][2]
        return indentityId, name, sex
lianxiren = getDataFromSheet()
tbname =lianxiren[1]
id     =lianxiren[0]
sex    =lianxiren[2]
birday = lianxiren[0][6:14]
chejiahao = "LSGPC52U7AF1"+id[-5::]
carnb = "冀G"+ id[-5::]
engnb = id[-7::]
class HeXinCheXian:
    def __init__(self):
        self.toubaodan = ""
        self.liushuihao= ""
        self.baodanhao = ""
        self.pidanshenqing = ""
        self.jyliushuihao = ""
        self.piwan = ""
    #捕获弹窗
    def alert_acc(self):
        time.sleep(1)
        try:
            if self.driver.switch_to.alert:
                self.driver.switch_to_alert().accept()
        except:
            pass
    def toubaochuli(self):#任务处理
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("投保管理").click()
        self.driver.find_element_by_link_text("投保处理").click()

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_elements_by_name('planrisk')[1].click()

        self.driver.find_element_by_css_selector("input[name='planCode']").send_keys("1360")
        self.driver.find_element_by_css_selector("input[value='下一步']").click()

        #**投保页面**#
        self.driver.switch_to.frame("myFrame") #切换到里面的frame
        #直接业务
        ser = Select(self.driver.find_element_by_css_selector("select[name='GuMainBusinessMode']"))
        ser.select_by_index(0)

        #二级渠道
        __ej =self.driver.find_element_by_name('GuMainChannelDetailCode')
        ActionChains(self.driver).double_click(__ej).perform()
        __ej.send_keys(Keys.ENTER)
        __ej.send_keys(Keys.ENTER)
        time.sleep(1)
        #三级渠道
        __sj = self.driver.find_element_by_name("GuMainChannelTip")
        ActionChains(self.driver).double_click(__sj).perform()
        __sj.send_keys(Keys.ENTER)
        __sj.send_keys(Keys.ENTER)
        time.sleep(2)
        sj = 'var q = document.getElementsByName("GuMainChannelTip");q[0].value = "%s";' % "01010102"
        self.driver.execute_script(sj)
        time.sleep(1)
        #业务归属

        __yw =self.driver.find_element_by_name('GuMainCompanyCode')
        ActionChains(self.driver).double_click(__yw).perform()
        __yw.send_keys(Keys.ENTER)
        __yw.send_keys(Keys.ENTER)
        time.sleep(2)
        sj = 'var q = document.getElementsByName("GuMainCompanyCode");q[0].value = "%s";' % "0104010002"
        self.driver.execute_script(sj)
        time.sleep(1)
        #业务员
        __ywy =self.driver.find_element_by_name('GuMainSalesmanCode')
        ActionChains(self.driver).double_click(__ywy).perform()
        __ywy.send_keys(Keys.ENTER)
        __ywy.send_keys(Keys.ENTER)
        time.sleep(1)
        #保单归属地(市)
        __bs =self.driver.find_element_by_name('GuMainCityCode')
        ActionChains(self.driver).double_click(__bs).perform()
        __bs.send_keys(Keys.ENTER)
        __bs.send_keys(Keys.ENTER)
        time.sleep(1)
        #保单归属地(县)110000
        __bd =self.driver.find_element_by_name('GuMainCountyCode')
        ActionChains(self.driver).double_click(__bd).perform()
        __bd.send_keys(Keys.ENTER)
        __bd.send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyInsuredName']").send_keys(tbname)
        self.driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyIdentifyNumber']").send_keys(id)
        self.driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyMobilePhone']").send_keys(tel)#电话
        self.driver.find_element_by_css_selector("TEXTAREA[name='AppliGuRelatedPartyInsuredAddress']").send_keys(address)
        self.driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyPostCode']").send_keys(postcode)
        self.driver.find_element_by_css_selector("input[name='buttonInsuredGuAppliPartyCustomerIdentify']").click()#客户识别
        self.alert_acc()
        self.driver.find_element_by_css_selector("input[name='buttonSaveCustomer']").click()#保存客户
        time.sleep(2)
        self.alert_acc()
        self.driver.find_element_by_css_selector("input[name='buttonCourierInfoCollect']").click()#配送信息
        self.driver.find_element_by_css_selector("input[value='关闭']").click()#关闭
        self.driver.find_element_by_css_selector("input[name='saveButton']").click()#保存

        #**标的信息**#
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[name='GuItemMotorPhoneNumber']").send_keys(tel)#车主手机电话
        self.driver.find_element_by_css_selector("input[name='GuItemMotorLicenseNo']").send_keys(carnb)#号牌号码

        __win1 = self.driver.current_window_handle
        self.driver.find_element_by_css_selector("input[name='detailQuery']").click() #车型查询
        __all1 = self.driver.window_handles
        for h in __all1:
            if h != __win1:
                self.driver.switch_to.window(h)
                self.driver.find_element_by_css_selector("input[name='GuItemMotorLicenseNo']").send_keys(carnb)
                self.driver.find_element_by_css_selector("input[name='GuItemMotorFrameNo']").send_keys(chejiahao)
                self.driver.find_element_by_css_selector("input[name='GuItemMotorCarBrand']").send_keys(caricon)
                self.driver.find_element_by_css_selector("input[value='查询(Q)']").click()
                self.driver.switch_to.frame("QueryResultFrame")
                time.sleep(2)
                self.driver.find_element_by_css_selector("input[name='GuItemMotorLicenseTypeCode']").send_keys("02")
                self.driver.find_element_by_css_selector("input[name='GuItemMotorEngineNo']").send_keys(engnb)#发动机号
                self.driver.find_element_by_css_selector("input[name='GuItemMotorCarKindBCode']").send_keys("A")#车辆大类
                self.driver.find_element_by_css_selector("input[name='GuItemMotorCarKindCode']").send_keys("A0")#车辆种类
                self.driver.find_element_by_css_selector("input[name='GuItemMotorUseNatureShow']").send_keys("8A")#使用性质
                self.driver.find_element_by_css_selector("input[name='GuItemMotorEnrollDate']").send_keys("2015-12-12")#车辆日期日期
                self.driver.find_element_by_css_selector("input[name='checkboxSelect']").click()
                self.driver.find_element_by_css_selector("input[value='查询(Q)']").click()
                time.sleep(3)
                self.driver.find_element_by_css_selector("input[name='checkboxSelect']").click()
                self.driver.find_element_by_css_selector("input[value='选择']").click()
                self.driver.switch_to.window(__win1)
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[name='GuItemMotorAttachNature']").send_keys("01")               #车主性质
        self.driver.find_element_by_css_selector("input[name='GuItemMotorVehicleCategory']").send_keys("K33")           #交管车辆类型
        self.driver.find_element_by_css_selector("input[name='GuItemMotorCertificateDate']").send_keys("2015-12-25")    #发证日期
        self.driver.find_elements_by_css_selector("input[name='ItemMotorCarCheckReason']")[4].click()                   #协议免验
        self.driver.find_element_by_css_selector("body > div > form > div:nth-child(69) > input").click()

        #**险种信息**#
        #0807
        time.sleep(4)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[value='带入投保人信息']").click()                      #带入投保人信息
        self.driver.find_element_by_css_selector("input[name='GuRiskQueryedArea']").send_keys(area)      #制定区域
        self.driver.find_elements_by_css_selector("input[value='险别汇总计算']")[1].click()                    #险别汇总计算
        time.sleep(10)
        self.alert_acc()
        #0803
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_elements_by_css_selector("input[value='详细信息']")[2].click()
        self.driver.implicitly_wait(30)
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[value='带入投保人信息']").click()                      #带入投保人信息
        self.driver.find_element_by_css_selector("input[name='GuRiskQueryedArea']").send_keys(area)      #制定区域
        self.driver.find_elements_by_css_selector("input[value='新增']")[2].click()#增加
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[1].send_keys("01")    #主险
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[1].send_keys(Keys.TAB)
        self.driver.find_elements_by_css_selector("input[name='itemKindClauseType']")[1].click()
        self.driver.find_elements_by_css_selector("input[value='新增']")[2].click()#增加
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[2].send_keys("02")
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[2].send_keys(Keys.TAB)
        self.driver.find_elements_by_css_selector("input[name='GuItemKindSumInsured']")[2].send_keys("50000")
        self.driver.find_elements_by_css_selector("input[name='itemKindClauseType']")[2].click()
        self.driver.find_elements_by_css_selector("input[value='新增']")[2].click()#增加
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[3].send_keys("03")
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[3].send_keys(Keys.TAB)
        self.driver.find_elements_by_css_selector("input[name='GuItemKindSumInsured']")[3].send_keys("50000")
        self.driver.find_elements_by_css_selector("input[name='itemKindClauseType']")[3].click()
        self.driver.find_elements_by_css_selector("input[value='险别汇总计算']")[1].click()
        time.sleep(8)
        self.alert_acc()
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        dr = self.driver.find_element_by_css_selector("body > div > form > div:nth-child(71) > input:nth-child(1)")
        self.driver.execute_script("arguments[0].scrollIntoView();", dr)
        time.sleep(2)
        dr.click()                                                                          #保存
        time.sleep(5)

        #**保单费用信息**#
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_elements_by_css_selector("TD[id='myTD']")[3].click()               #保单费用信息
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        time.sleep(2)
        self.driver.find_element_by_css_selector("input[name='saveButton']").click()
        time.sleep(3)

        #**提交核保**#
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[value='提交核保']").click()
        self.alert_acc()

        #**投保单号**#
        time.sleep(6)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        tbdan = self.driver.find_element_by_css_selector("td[class='white']").text
        self.toubaodan = tbdan[6:32]
        print (self.toubaodan)
        time.sleep(2)
        self.driver.quit()
        time.sleep(2)
    def yancheguanli(self):#验车管理
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        # cooki = self.driver.get_cookies()
        # print (cooki)
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("验车管理").click()
        self.driver.find_element_by_link_text("验车照片上传").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='GwWfLogbusinessNo']").send_keys(self.toubaodan)
        Select(self.driver.find_element_by_name("GwWfLogIsCoreflag")).select_by_index(0)    #是
        self.driver.find_element_by_css_selector("input[name='buttonQuery']").click()       #查询
        self.driver.switch_to.frame("QueryResultFrame")
        self.driver.find_element_by_css_selector("input[name='checkboxSelect']").click()    #选择单号
        __win2 = self.driver.current_window_handle
        self.driver.find_element_by_css_selector("input[name='upload_button']").click()     #影响提交
        #**影像提交**#
        __all2 = self.driver.window_handles
        for h in __all2:
            if h != __win2:
                self.driver.switch_to.window(h)
                time.sleep(2)
                os.system("D:\\up.exe")
                time.sleep(3)
                self.driver.find_element_by_css_selector("input[value='确定']").click()
                self.alert_acc()
                self.alert_acc()
                self.driver.switch_to.window(__win2)
        time.sleep(2)
        self.driver.quit()
        time.sleep(2)
    def hebaochuli(self):#核保处理
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(heun)
        self.driver.find_element_by_id("password").send_keys(hbpw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("审核平台子系统").click()
        self.driver.find_element_by_link_text("核保审核").click()
        self.driver.find_element_by_link_text("任务处理").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='GwWfLogDtoBusinessNo']").send_keys(self.toubaodan)#
        self.driver.find_element_by_css_selector("input[name='buttonQuery']").click()#查询
        self.driver.switch_to.frame("QueryResultFrame")
        time.sleep(1)
        __win3 = self.driver.current_window_handle
        self.driver.find_element_by_css_selector("a[href='#']").click()#投保号
        __all3 = self.driver.window_handles
        for h in __all3:
            if h!=__win3:
                self.driver.switch_to.window(h)
                self.driver.close()
                self.driver.switch_to.window(__win3)
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        Select(self.driver.find_element_by_name("NotionContent")).select_by_index(2)    #同意
        self.driver.find_element_by_css_selector("input[name='butViewTranceInfo']").click()#审核意见
        __all4 = self.driver.window_handles
        for h in __all4:
            if h != __win3:
                self.driver.switch_to.window(h)
                self.driver.close()
                self.driver.switch_to.window(__win3)
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[name='passBtn']").click() #审核通过
        self.alert_acc()
        self.alert_acc()
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        su = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td').text
        __retext = su[0:4]
        print (__retext)    #操作成功
        self.driver.quit()
        time.sleep(3)
    def jianfeichudanjiaofei(self):#见费出单缴费
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("收付子系统").click()
        self.driver.find_element_by_link_text("见费出单处理").click()
        self.driver.find_element_by_link_text("见费出单缴费").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='gpPayFeeInfoDtoBusinessNo']").send_keys(self.toubaodan)#业务号
        self.driver.find_element_by_css_selector("input[name='buttonQuery']").click()#查询
        self.driver.switch_to.frame("QueryResultFrame")
        self.driver.find_element_by_css_selector("input[name='selectCheckbox']").click()#选择
        self.driver.find_element_by_css_selector("input[value='其他方式登记(O)']").click()
        self.driver.find_element_by_css_selector("input[value='确定(F)']").click()
        self.driver.find_element_by_css_selector("input[value='获取验证码']").click()
        self.alert_acc()
        self.alert_acc()
        time.sleep(60)
        '''
        无法自动获取验证码
        '''
        self.driver.find_element_by_css_selector("input[value='确定']").click()
        self.alert_acc()
        self.alert_acc()
        #**其他支付**#
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[value='登记确认']").click()
        liushuihao = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/table/tbody/tr[2]/td").text
        self.liushuihao = liushuihao[-20::]
        print (self.liushuihao)
        self.driver.quit()
        time.sleep(3)
    def jianfeichudanqueren(self):#见费出单确认
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("收付子系统").click()
        self.driver.find_element_by_link_text("见费出单处理").click()
        self.driver.find_element_by_link_text("见费出单收付确认").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='gpTradeInfoDtoTradeNo']").send_keys(self.liushuihao)#业务号
        self.driver.find_element_by_css_selector("input[name='buttonQuery']").click()#查询
        self.driver.switch_to.frame("QueryResultFrame")
        self.driver.find_element_by_css_selector("input[name='selectCheckbox']").click()#选择
        self.driver.find_element_by_css_selector("input[value='其他方式收付确认(V)']").click()
        #**其他支付**#
        time.sleep(6)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        time.sleep(2)
        bdh = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td").text
        # print (bdh)
        self.baodanhao = bdh[29:55]
        print (self.baodanhao)
        self.driver.quit()
        time.sleep(3)
    def pigaiguanli(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("批改管理").click()
        self.driver.find_element_by_link_text("批改申请处理").click()
        #**批改处理**#
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='PolicyNo']").send_keys(self.baodanhao)#保单号码
        self.driver.find_element_by_css_selector("input[value='下一步']").click() #下一步
        #**批单处理**#
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        ser = Select(self.driver.find_element_by_css_selector("SELECT[name='endorType']"))
        ser.select_by_index(10)
        self.driver.find_element_by_css_selector("input[value='>>']").click()
        self.driver.find_element_by_css_selector("input[value='下一步']").click()
        #**基本信息**#
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame('myFrame')
        self.driver.find_element_by_css_selector("input[value='配送信息']").click()#配送信息
        self.driver.find_element_by_css_selector("input[value='关闭']").click()#关闭
        dr = self.driver.find_element_by_css_selector("input[name='saveButton']")
        self.driver.execute_script("arguments[0].scrollIntoView();", dr)
        time.sleep(1)
        dr.click()
        #*险种信息*#
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_elements_by_css_selector("td[id='myTD']")[2].click()
        self.driver.switch_to.frame("myFrame")
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_elements_by_css_selector("input[value='险别汇总计算']")[1].click()   #险别汇总计算

        time.sleep(2)
        self.alert_acc()
        self.alert_acc()
        #
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        __dr = self.driver.find_element_by_css_selector("input[name='saveButton']")
        self.driver.execute_script("arguments[0].scrollIntoView();", __dr)
        time.sleep(1)
        __dr.click()                                                                      #保存

        #
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_elements_by_css_selector("input[value='详细信息']")[2].click()
        time.sleep(2)
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        # self.driver.find_elements_by_css_selector("input[value='删除']")[7].click()

        time.sleep(2)
        self.driver.find_elements_by_css_selector("input[value='新增']")[3].click()#增加
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[7].send_keys("11")
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[7].send_keys(Keys.TAB)
        self.driver.find_elements_by_css_selector("input[value='险别汇总计算']")[1].click()  #险别汇总计算
        time.sleep(4)
        self.alert_acc()
        self.alert_acc()

        #
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        __dr1 = self.driver.find_element_by_css_selector("input[name='saveButton']")
        self.driver.execute_script("arguments[0].scrollIntoView();", __dr1)
        time.sleep(1)
        __dr1.click()                                                                        #保存

        #**保单费用信息**#
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_elements_by_css_selector("TD[id='myTD']")[3].click()               #保单费用信息
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        time.sleep(2)
        self.driver.find_element_by_css_selector("input[name='saveButton']").click()

        #**批文信息**#
        time.sleep(5)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_elements_by_css_selector("TD[id='myTD']")[4].click()                   #批文信息
        time.sleep(1)
        self.driver.switch_to.frame("myFrame")
        time.sleep(2)
        self.driver.find_element_by_css_selector("TEXTAREA[name='GuEndorTextEndorseTextByInput']").send_keys("同意") #手工批文
        time.sleep(2)
        self.driver.find_element_by_css_selector("input[name='saveButton']").click()                                #同意
        #**提交核保**#
        time.sleep(8)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='Save']").click()#提交核保
        #**文本**#
        time.sleep(10)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")

        pdsqh = self.driver.find_element_by_css_selector("td[align='center']").text
        print (pdsqh)
        self.pidanshenqing = pdsqh[6:28]
        print (self.pidanshenqing)
        self.driver.quit()
        time.sleep(3)
    def hebao_last(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(heun)
        self.driver.find_element_by_id("password").send_keys(hbpw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("审核平台子系统").click()
        self.driver.find_element_by_link_text("核保审核").click()
        self.driver.find_element_by_link_text("任务处理").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='GwWfLogDtoBusinessNo']").send_keys(self.pidanshenqing)#
        self.driver.find_element_by_css_selector("input[name='buttonQuery']").click()#查询
        self.driver.switch_to.frame("QueryResultFrame")
        time.sleep(1)
        __win3 = self.driver.current_window_handle
        self.driver.find_element_by_css_selector("a[href='#']").click()#投保号
        __all3 = self.driver.window_handles
        for h in __all3:
            if h!=__win3:
                self.driver.switch_to.window(h)
                self.driver.close()
                self.driver.switch_to.window(__win3)
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        Select(self.driver.find_element_by_name("NotionContent")).select_by_index(2)    #同意
        self.driver.find_element_by_css_selector("input[name='butViewTranceInfo']").click()#审核意见
        __all4 = self.driver.window_handles
        for h in __all4:
            if h != __win3:
                self.driver.switch_to.window(h)
                self.driver.close()
                self.driver.switch_to.window(__win3)
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[name='passBtn']").click() #审核通过
        time.sleep(2)
        self.alert_acc()
        self.alert_acc()
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        se

        su = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td').text
        __retext = su[0:4]
        print (__retext)    #操作成功
        self.driver.quit()
        time.sleep(3)
    def pgjianfeichudan(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("收付子系统").click()
        self.driver.find_element_by_link_text("见费出单处理").click()
        self.driver.find_element_by_link_text("见费出单缴费").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='gpPayFeeInfoDtoBusinessNo']").send_keys(self.pidanshenqing)#业务号
        self.driver.find_element_by_css_selector("input[name='buttonQuery']").click()#查询
        self.driver.switch_to.frame("QueryResultFrame")
        self.driver.find_element_by_css_selector("input[name='selectCheckbox']").click()#选择
        self.driver.find_element_by_css_selector("input[value='其他方式登记(O)']").click()
        self.driver.find_element_by_css_selector("input[value='确定(F)']").click()
        self.alert_acc()
        self.alert_acc()
        #**其他支付**#
        time.sleep(6)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[value='登记确认']").click()
        liushuihao = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/table/tbody/tr[2]/td").text
        self.jyliushuihao = liushuihao[-20::]
        print (self.jyliushuihao)
        self.driver.quit()
        time.sleep(3)
    def pgjianfeichudanqueren(self):#见费出单确认
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to.frame("leftFrame")
        self.driver.find_element_by_link_text("收付子系统").click()
        self.driver.find_element_by_link_text("见费出单处理").click()
        self.driver.find_element_by_link_text("见费出单收付确认").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.find_element_by_css_selector("input[name='gpTradeInfoDtoTradeNo']").send_keys(self.jyliushuihao)#业务号
        self.driver.find_element_by_css_selector("input[name='buttonQuery']").click()#查询
        self.driver.switch_to.frame("QueryResultFrame")
        self.driver.find_element_by_css_selector("input[name='selectCheckbox']").click()#选择
        self.driver.find_element_by_css_selector("input[value='其他方式收付确认(V)']").click()
        #**其他支付**#
        time.sleep(8)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        bdh = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[1]/tbody/tr[1]/td").text
        print (bdh)
        self.piwan = bdh[22:55]
        print (self.piwan)
        self.driver.quit()
        time.sleep(3)
    def run(self):
        self.toubaochuli()
        self.yancheguanli()
        self.hebaochuli()
        self.jianfeichudanjiaofei()
        self.jianfeichudanqueren()
        self.pigaiguanli()
        self.hebao_last()
        self.pgjianfeichudan()
        self.pgjianfeichudanqueren()
if __name__ == '__main__':
    HeXinCheXian().run()