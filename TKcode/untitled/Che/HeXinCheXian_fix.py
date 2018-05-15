import time
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
skname = "宫本武藏"                      #收款人
bankname = "中国银行"                    #收款银行
chejiahao = "LSGPC52U7AF127561"
carnb = "鲁A74110"
engnb = "246764K"
caricon = "凯迪拉克"
minzu = "汉"
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
class HeXinCheXian:
    def __init__(self):
        self.toubaodan = ""
        self.baodan    = ""
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
                self.driver.find_element_by_css_selector("input[value='查询(Q)']").click()
                self.driver.switch_to.frame("QueryResultFrame")
                time.sleep(2)
                self.driver.find_element_by_css_selector("input[name='GuItemMotorLicenseTypeCode']").send_keys("02")
                self.driver.find_element_by_css_selector("input[name='GuItemMotorCarBrand']").send_keys(caricon)#车辆品牌
                self.driver.find_element_by_css_selector("input[name='GuItemMotorCarKindBCode']").send_keys("A")#车辆大类
                self.driver.find_element_by_css_selector("input[name='GuItemMotorCarKindCode']").send_keys("A0")#车辆种类
                self.driver.find_element_by_css_selector("input[name='GuItemMotorUseNatureShow']").send_keys("8A")#使用性质
                self.driver.find_element_by_css_selector("input[name='GuItemMotorEnrollDate']").send_keys("2015-12-12")#车辆日期日期
                self.driver.find_element_by_css_selector("input[name='checkboxSelect']").click()
                self.driver.find_element_by_css_selector("input[value='查询(Q)']").click()
                time.sleep(2)
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
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[value='带入投保人信息']").click()                      #带入投保人信息
        self.driver.find_element_by_css_selector("input[name='GuRiskQueryedArea']").send_keys("370000")      #制定区域
        self.driver.find_elements_by_css_selector("input[value='险别汇总计算']")[1].click()                    #险别汇总计算
        time.sleep(10)
        self.alert_acc()
        #0803
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_elements_by_css_selector("input[value='详细信息']")[2].click()
        time.sleep(2)
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[value='带入投保人信息']").click()                      #带入投保人信息
        self.driver.find_element_by_css_selector("input[name='GuRiskQueryedArea']").send_keys("370000")      #制定区域
        self.driver.find_elements_by_css_selector("input[value='新增']")[2].click()#增加
        self.driver.find_elements_by_css_selector("input[name='GuItemKindKindCode']")[1].send_keys("01")#主险
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
                '''
                00400001360201800000000141
                01000000201801000124
                60400001360201800000000002
                2040000136020180000001
                '''
                self.driver.find_element_by_css_selector("input[value='确定']").click()
                self.alert_acc()
                self.driver.switch_to.window(__win2)
        time.sleep(2)
        self.driver.quit()
        time.sleep(2)
    def hebaochuli(self):
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
    def run(self):
        self.toubaochuli()
        # self.yancheguanli()
        # self.hebaochuli()
if __name__ == '__main__':
    HeXinCheXian().run()