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
    def toubaochuli(self):
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


        self.driver.switch_to.frame("myFrame")
        #直接业务
        ser = Select(self.driver.find_element_by_css_selector("select[name='GuMainBusinessMode']"))
        ser.select_by_index(0)

        ej = 'var q = document.getElementsByName("GuMainChannelDetailCode");q[0].value = "%s";' % "0101"
        self.driver.execute_script(ej)

        self.driver.find_element_by_css_selector("input[name='GuMainChannelDetailCode']").send_keys(Keys.TAB)
        sj = 'var q = document.getElementsByName("GuMainChannelTip");q[0].value = "%s";' % "01010102"
        self.driver.execute_script(sj)

        ywgs = 'var q = document.getElementsByName("GuMainCompanyCode");q[0].value = "%s";' % "0104000001"
        self.driver.execute_script(ywgs)

        ywy = 'var q = document.getElementsByName("GuMainSalesmanCode");q[0].value = "%s";' % "S000000081"
        self.driver.execute_script(ywy)

        bdgs = 'var q = document.getElementsByName("GuMainCityCode");q[0].value = "%s";' % "110000"
        self.driver.execute_script(bdgs)

        bdgx = 'var q = document.getElementsByName("GuMainCountyCode");q[0].value = "%s";' % "110101"
        self.driver.execute_script(bdgx)


        #身份证采集
        __win = self.driver.current_window_handle
        self.driver.find_element_by_css_selector("input[name='buttonAppliIdentifyGenerate']").click()
        __all = self.driver.window_handles
        for h in __all:
            if h != __win:
                self.driver.switch_to.window(h)
                time.sleep(2)
                self.driver.find_element_by_css_selector("input[id='Text1']").send_keys(tbname)          #姓名
                self.driver.find_element_by_css_selector("input[id='Text2']").send_keys(sex)             #性别
                self.driver.find_element_by_css_selector("input[id='Text3']").send_keys(minzu)           #民族
                self.driver.find_element_by_css_selector("input[id='Text4']").send_keys(birday)          #出生日期
                self.driver.find_element_by_css_selector("TEXTAREA[name='Address']").send_keys(address)  #地址
                self.driver.find_element_by_css_selector("input[id='Text6']").send_keys(id)              #身份证
                self.driver.find_element_by_css_selector("input[id='Text7']").send_keys("北京市公安局")    #身份证签发机构
                self.driver.find_element_by_css_selector("input[id='Text8']").send_keys("2010.10.10")    #身份证有效期起期
                self.driver.find_element_by_css_selector("input[id='Text10']").send_keys("2020.10.10")   #身份证有效期止期
                self.driver.find_element_by_css_selector("input[value='确定']").click()
                self.driver.switch_to.window(__win)
                self.driver.switch_to.frame("mainFrame")
                self.driver.switch_to.frame("myFrame")
        self.driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyMobilePhone']").send_keys(tel)#电话
        self.driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyPostCode']").send_keys(postcode)
        self.driver.find_element_by_css_selector("input[name='buttonInsuredGuAppliPartyCustomerIdentify']").click()#客户识别
        self.alert_acc()

        self.driver.find_element_by_css_selector("input[name='buttonSaveCustomer']").click()#保存客户
        self.alert_acc()
        self.driver.find_element_by_css_selector("input[name='buttonCourierInfoCollect']").click()#配送信息
        self.driver.find_element_by_css_selector("input[value='关闭']").click()#关闭
        self.driver.find_element_by_css_selector("input[name='saveButton']").click()#保存
        #进入标的信息
        self.driver.switch_to_default_content()
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
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")

        self.driver.find_element_by_css_selector("input[name='GuItemMotorAttachNature']").send_keys("01")    #车主性质
        self.driver.find_element_by_css_selector("input[name='GuItemMotorVehicleCategory']").send_keys("K33")#交管车辆类型
        self.driver.find_elements_by_css_selector("input[name='ItemMotorCarCheckReason']")[4].click()        #协议免验
        self.driver.find_element_by_css_selector("body > div > form > div:nth-child(69) > input").click()
        #险种信息
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainFrame")
        self.driver.switch_to.frame("myFrame")
        self.driver.switch_to.frame("RiskFrame")
        self.driver.switch_to_frame("myFrame")
        self.driver.find_element_by_css_selector("input[value='带入投保人信息']").click()#带入投保人信息

    def run(self):
        self.toubaochuli()
if __name__ == '__main__':
    HeXinCheXian().toubaochuli()