from selenium import webdriver
import time
from time import sleep
import xlrd
from xlutils.copy import copy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import re
url="http://10.130.201.36:7001/index.jsp"
#投保人信息表位置
excellPath="D:\\JettechAgent1.6.0\\身份证.xls"
#工作表名称
sheetName="Sheet1"
#财险投保账户
username='policy3@upic'
#核保账户
hebaoName="uwprpall@upic"
#账户密码
password='upic@123'
#险种代码
riskCode='1107'

#读取excell投保人信息表
def readExcell():
    rowList = []
    # 读取Excell文件数据
    xlsData = xlrd.open_workbook(excellPath)
    # 读取指定工作表数据
    table = xlsData.sheet_by_name(sheetName)
    # 获取工作表总行数
    nrows = table.nrows
    # 遍历获取每行数据
    if nrows:
        for line in range(nrows):
            rowData = table.row_values(line)
            if rowData[4] == "":
                rowList.append(rowData)
                wb = copy(xlsData)
                ws = wb.get_sheet(0)
                ws.write(line, 4, '1')
                ws.write(line, 5, time.ctime())
                wb.save(excellPath)
                break
        if rowList == 0:
            return "读取数据完毕!"
        else:
            return rowList

exlData=readExcell()
#投保人信息：
id=exlData[0][0]
name=exlData[0][1]
sex=exlData[0][2]
print(id,name,sex)

driver = webdriver.Ie()
class caiXianChudan:
    #登录
    def Login(self):
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_css_selector('#username').send_keys(username)
        driver.find_element_by_css_selector('#password').send_keys(password)
        driver.find_element_by_css_selector('#bt_submit').click()
    #基本信息
    def jiBenXinxi(self):
        sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame("leftFrame")
        driver.find_element_by_link_text("承保子系统").click()
        driver.find_element_by_link_text("投保管理").click()
        driver.find_element_by_link_text("投保处理").click()
        sleep(2)
        driver.switch_to.default_content()
        driver.implicitly_wait(5)
        driver.switch_to.frame("mainFrame")
        driver.implicitly_wait(5)
        driver.find_element_by_css_selector("input[name='riskCode']").send_keys(riskCode)
        driver.find_element_by_css_selector("input[name='riskCode']").send_keys(Keys.TAB)
        driver.find_element_by_css_selector("input[name='buttonNextStep']").click()
        #中介人协议
        sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame("mainFrame")
        driver.switch_to.frame("myFrame")  # 切换到里面的frame
        sleep(1)
        driver.find_element_by_css_selector("input[name='GuMainAgreementNo']").send_keys('010000000000600052')
        driver.find_element_by_css_selector("input[name='GuMainAgreementNo']").send_keys(Keys.TAB)
        #子协议
        driver.find_element_by_css_selector("input[name='GuMainSolutionCode']").send_keys('0100000000006000520001')
        #投保人姓名
        driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyInsuredName']").send_keys(name)
        #身份证号
        driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyIdentifyNumber']").send_keys(id)
        #出生日期
        driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyBirthDate']").click()
        #增值服务类
        selectTag=driver.find_element_by_css_selector("select[name='AppliGuRelatedPartyStarLevel']")
        Select(selectTag).select_by_index(1)
        sleep(2)
        #客户识别
        driver.find_element_by_css_selector("input[name='buttonInsuredGuAppliPartyCustomerIdentify']").click()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(2)
        #地址
        driver.find_element_by_css_selector("textarea[name='AppliGuRelatedPartyInsuredAddress']").send_keys("北京市昌平区生命科学园")
        #邮政编码
        driver.find_element_by_css_selector("input[name='AppliGuRelatedPartyPostCode']").send_keys("100000")
        sleep(2)
        #保存客户
        driver.find_element_by_css_selector("input[name='buttonSaveCustomer']").click()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(2)
        driver.find_element_by_css_selector("#saveButton").click()
        sleep(3)
    #险种信息
    def xZhongXinXi(self):
        driver.switch_to.default_content()
        driver.switch_to.frame("mainFrame")
        sleep(1)
        driver.switch_to.frame("myFrame")
        sleep(1)
        driver.switch_to.frame("riskFrame")
        sleep(1)
        driver.switch_to.frame("myFrame")
        #方案代码/方案名称
        driver.find_element_by_css_selector("input[name='GuRiskDynamicFieldAI']").send_keys("1107G103")
        driver.find_element_by_css_selector("input[name='GuRiskDynamicFieldAI']").send_keys(Keys.TAB)
        #健康告知
        driver.find_element_by_css_selector("textarea[name='GuRiskDynamicFieldAK']").send_keys("健康告知")
        sleep(2)
        driver.find_element_by_css_selector("input[name='saveButton']").click()
        driver.implicitly_wait(6)
    #标的信息
    def biaoDi(self):
        driver.switch_to.default_content()
        driver.switch_to.frame("mainFrame")
        driver.implicitly_wait(3)
        driver.switch_to.frame("myFrame")
        driver.implicitly_wait(3)
        driver.switch_to.frame("RiskFrame")
        driver.implicitly_wait(3)
        driver.find_elements_by_css_selector("#mySubTD")[1].click()
        driver.switch_to.frame("myFrame")
        driver.implicitly_wait(3)
        #增加保障
        driver.find_element_by_css_selector("input[name='button_ItemKind_Insert']").click()
        #险别
        driver.find_elements_by_css_selector("input[name='GuItemKindKindName']")[1].send_keys("1107001")
        driver.find_elements_by_css_selector("input[name='GuItemKindKindName']")[1].send_keys(Keys.TAB)
        sleep(1)
        #每份赔偿限额
        driver.find_elements_by_css_selector("input[name='GuItemKindUnitInsured']")[1].send_keys("30000")
        #费率
        rate_js='var t=document.getElementsByName("GuItemKindRate");' \
               't[1].value=%s;' %"0.3"
        driver.execute_script(rate_js)
        sleep(2)
        #方案代码
        driver.find_element_by_css_selector("input[name='GuItemAcciProjectCode']").send_keys('1107001')
        driver.find_element_by_css_selector("input[name='GuItemAcciProjectName']").send_keys('人身意外伤害险')
        #职业大类
        driver.find_element_by_css_selector("input[name='GuItemAcciOccupationType']").send_keys('00101')
        driver.find_element_by_css_selector("input[name='GuItemAcciOccupationType']").send_keys(Keys.TAB)
        #职业工种代码
        double_click_tag=driver.find_element_by_css_selector("input[name='GuItemAcciOccupationCode']")
        ActionChains(driver).double_click(double_click_tag).perform()
        driver.find_element_by_css_selector("input[name='GuItemAcciOccupationCode']").send_keys(Keys.ENTER)
        driver.find_element_by_css_selector("input[name='GuItemAcciOccupationCode']").send_keys(Keys.ENTER)
        sleep(3)
        #保存
        driver.find_element_by_css_selector("input[name='saveButton']").click()
    #人员列表
    def renYuanlist(self):
        sleep(5)
        #获取当前窗口handle
        handle1=driver.current_window_handle
        #点击人员列表按钮
        driver.find_element_by_css_selector("input[name='buttonSummaryAcciListInfo']").click()
        sleep(2)
        #弹出人员列表窗口，获取所有handle
        all_handle=driver.window_handles
        #切换到人员列表handle
        for handle in all_handle:
            if handle!= handle1:
                driver.switch_to.window(handle)
                #点击增加
                driver.find_element_by_css_selector("input[name='buttonInsert']").click()
                driver.switch_to.frame("QueryResultFrame")
                sleep(2)
                #被保险人姓名
                driver.find_element_by_css_selector("input[name='GuItemAcciListClientCName']").send_keys(name)
                #证件号码
                driver.find_element_by_css_selector("input[name='GuItemAcciListIdentifyNoA']").send_keys(id)
                #详细地址
                driver.find_element_by_css_selector("input[name='GuItemAcciListHomeAddress']").send_keys("北京市昌平区")
                #生存受益人名字
                driver.find_element_by_css_selector("input[name='GuItemAcciBenefitClientCName']").send_keys(name)
                #证件号码
                driver.find_element_by_css_selector("input[name='GuItemAcciBenefitIdentifyNo']").send_keys(id)
                sleep(2)
                #确定
                driver.find_element_by_css_selector("input[value='确定']").click()
                sleep(2)
                driver.switch_to_alert().accept()
                sleep(5)
                driver.close()
                driver.switch_to.window(handle1)
                driver.implicitly_wait(5)
                driver.switch_to.default_content()
                driver.implicitly_wait(5)
                driver.switch_to.frame("mainFrame")
                #提交复核
                driver.find_element_by_css_selector("input[name='Save']").click()
                sleep(3)
                driver.implicitly_wait(5)
                #获取投保单号
                getText=driver.find_element_by_css_selector("body > form > table > tbody > tr:nth-child(1) > td").text
                pattern = '\d*\d'
                toubaodanhao=re.search(pattern,getText).group()
                print(toubaodanhao)
                #注销账户
                driver.switch_to.default_content()
                driver.implicitly_wait(5)
                driver.switch_to.frame("topFrame")
                driver.implicitly_wait(5)
                driver.find_element_by_css_selector(".right_02").click()
                sleep(2)
                driver.quit()

    def run(self):
        self.Login()
        self.jiBenXinxi()
        self.xZhongXinXi()
        self.biaoDi()
        self.renYuanlist()
class renWuChuLi:
    # 登录
    def login(self):
        driver.get(url)
        driver.maximize_window()
        driver.find_element_by_css_selector('#username').send_keys(hebaoName)
        driver.find_element_by_css_selector('#password').send_keys(password)
        driver.find_element_by_css_selector('#bt_submit').click()



if __name__ == '__main__':
    functionLibrary=caiXianChudan()
    functionLibrary.run()




