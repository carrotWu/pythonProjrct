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
url = "http://10.130.201.36:7001/index.jsp"
tbun = "policy3@upic"                   #投保用户名
heun= "uwprpall@upic"                   #核保用户名
lpun= "0008054"                         #理赔用户
pw = "upic@123"                         #密码
            #
address = "山西省"
postcode = "047500"
tel = "13601234567"
skname = "宫本武藏"                      #收款人
bankname = "中国银行"                    #收款银行

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

#计算保费
def calcbf(str,str1):
    s = float(str.replace(',','')) * float(str1.replace(',','')) / 1000
    print (s)
    return  s

lianxiren = getDataFromSheet()
tbname =lianxiren[1]
id     =lianxiren[0]

class HeXinCaiXian_D:
    def __init__(self):
        self.toubaodanhao = "" #投保单号
        self.baodanhao    = "6750100110920170000165" #保单号
        self.baoanhao     = "170513065" #报案号
        self.operasucc   = "操作成功" #

    def calcrate(self):
        total = 0
        for i in range(1,20):
            try:
                if self.driver.find_elements_by_name('GuItemKindUnitInsured')[i].is_displayed() is True:
                    #取每份赔偿限额1
                    xe = self.driver.find_elements_by_name('GuItemKindUnitInsured')[i].get_attribute('value')
                    print (xe)
                    #费率1
                    fl = self.driver.find_elements_by_name('GuItemKindRate')[i].get_attribute('value')
                    print (fl)
                    #应收保费1
                    bf = self.driver.find_elements_by_name('GuItemKindGrossPremium')[i].get_attribute("value")
                    print (bf)
                    s = (float(xe.replace(',','')) * float(fl.replace(',','')) / 1000)
                    print (s)
                    s = ('{:.2f}'.format(Decimal(str(s))))
                    print (s)
                    if  float(s)== float(bf):
                        print (str(i)+"\t"+("pass"))
                        total += float(bf)
                        print (bf)
                        print (total)
                    else:
                        raise Exception()
                        # raise scriptError(funcName+'--------异常')
            except:
                break
                #总保费
        total_q = self.driver.find_element_by_name('GuItemAcciGrossPremium').get_attribute("value")
        if total == float(total_q):
            print ("保费正常")
            print (float(total_q))
        else:
            print ("保费异常")
            raise Exception()

    def fenbao(self):
        win1 = self.driver.current_window_handle
        try:
            if self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tfoot/tr/td[1]/input').is_displayed() is True:
                self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tfoot/tr/td[1]/input').click()
                time.sleep(3)
                all_h = self.driver.window_handles
                for h in all_h:
                    if h !=win1:
                        self.driver.switch_to_window(h)
                        self.driver.close()
                        self.driver.switch_to_window(win1)
                self.driver.switch_to_default_content()
                self.driver.switch_to_frame("mainFrame")
                self.driver.switch_to_frame("myFrame")
        except:
            print ("ele not esixt")
        '''
        #取每份赔偿限额1


        qxe1 = self.driver.find_elements_by_name('GuItemKindUnitInsured')[1].get_attribute('value')
        #费率1
        qfl = self.driver.find_elements_by_name('GuItemKindRate')[1].get_attribute('value')
        print(qfl)
        #应收保费1
        bf_1 = self.driver.find_elements_by_name('GuItemKindGrossPremium')[1].get_attribute("value")
        if calcbf(qxe1,qfl) == float(bf_1):
            print ("suc")

        #*****************#
        #取每份赔偿限额2
        qxe2 = self.driver.find_elements_by_name('GuItemKindUnitInsured')[2].get_attribute('value')
        print (qxe2)
        #费率2
        qfl2 = self.driver.find_elements_by_name('GuItemKindRate')[2].get_attribute('value')
        #应收保费2
        bf_2 = self.driver.find_elements_by_name('GuItemKindGrossPremium')[2].get_attribute("value")
        if calcbf(qxe2,qfl2) == float(bf_2):
            print ("suc")
        #*****************#
        #总保费
        total_q = self.driver.find_element_by_name('GuItemAcciGrossPremium').get_attribute("value")
        print ("取出来的总保费"+total_q)

        #算出来的总保费
        total_s= calcbf(qxe1,qfl) + calcbf(qxe2,qfl2)
        print ("算出来的总保费"+str(total_s))
        #险别2的保费
        '''
    def toubaochuli(self):#投保处理1(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()

        time.sleep(2)
        self.driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理
        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("投保管理").click()
        self.driver.find_element_by_link_text("投保处理").click()

        self.driver.switch_to_default_content()  #需要切换回主页面
        self.driver.switch_to_frame("mainFrame")   #右边的frame
        self.driver.find_element_by_xpath(".//*[@id='RiskArea']/table[1]/tbody/tr/td[4]/input[1]").send_keys("1109")
        self.driver.find_element_by_xpath(".//*[@id='RiskArea']/table[1]/tbody/tr/td[4]/input[1]").send_keys(Keys.TAB)
        self.driver.find_element_by_xpath("/html/body/form/table[5]/tbody/tr/td/input[1]").send_keys(Keys.ENTER)
        time.sleep(2)
        #进入输入框
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.implicitly_wait(4)
        self.driver.switch_to_frame("myFrame") #切换到里面的frame
        #中介人协议
        self.driver.find_element_by_name("GuMainAgreementNo").send_keys("010000000000400059")
        self.driver.find_element_by_name("GuMainAgreementNo").send_keys(Keys.TAB)
        time.sleep(1)
        #子协议代码
        self.driver.find_element_by_name("GuMainSolutionCode").send_keys("0100000000004000590001")
        self.driver.find_element_by_name("GuMainSolutionCode").send_keys(Keys.TAB)
        #投保人名称
        time.sleep(3)
        self.driver.find_element_by_name("AppliGuRelatedPartyInsuredName").send_keys(tbname)
        #证件号码
        self.driver.find_element_by_name("AppliGuRelatedPartyIdentifyNumber").send_keys(id)
        #增值服务类型,定位下拉框
        ser = Select(self.driver.find_element_by_name("AppliGuRelatedPartyStarLevel"))
        ser.select_by_index(1)
        #地址
        self.driver.find_element_by_xpath('//*[@id="InsuredGuAppliPartyCorInsuredAddress"]/td[3]/textarea').send_keys(address)

        #邮政编码
        self.driver.find_element_by_xpath('//*[@id="InsuredGuAppliPartyCorInsuredPostCodeOP"]/td[2]/input').send_keys(postcode)
        #客户识别
        self.driver.find_element_by_name('buttonInsuredGuAppliPartyCustomerIdentify').click()
        time.sleep(2)
        self.driver.switch_to_alert().accept() #用户重复时主调
        time.sleep(1)
        #保存客户
        self.driver.find_element_by_name('buttonSaveCustomer').click()
        time.sleep(1)
        self.driver.switch_to_alert().accept()
        #确定
        self.driver.find_element_by_id("saveButton").click()
        time.sleep(2)
        #产品方案代码/名称
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("myFrame") #切换到里面的frame
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("RiskFrame")
        self.driver.switch_to_frame("myFrame")
        #特别约定
        self.driver.find_element_by_link_text("特别约定").click()
        self.driver.find_element_by_name("buttonMyClausesAdd").click()  #点+号

        time.sleep(2)

        #设置特别约定代码
        self.driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys('0083')
        self.driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys(Keys.TAB)
        time.sleep(1)
        #产品方案代码名称
        self.driver.find_element_by_name("GuRiskDynamicFieldAI").send_keys("1109A01I01")
        self.driver.find_element_by_name("GuRiskDynamicFieldAI").send_keys(Keys.TAB)
        time.sleep(1)
        #保存
        self.driver.find_element_by_id("saveButton").click()
        time.sleep(5)
        #进入标的里面的险别
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("myFrame") #切换到里面的frame
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("RiskFrame")
        self.driver.implicitly_wait(5)
        self.driver.find_elements_by_id("mySubTD")[1].click()
        self.driver.switch_to_frame("myFrame")
        self.driver.implicitly_wait(10)

        #增加保障
        self.driver.find_element_by_name("button_ItemKind_Insert").click()
        #险别1
        self.driver.find_elements_by_name("GuItemKindKindName")[1].send_keys("1109016")
        self.driver.find_elements_by_name("GuItemKindKindName")[1].send_keys(Keys.TAB)
        #每份赔偿限额1
        self.driver.find_elements_by_name("GuItemKindUnitInsured")[1].send_keys(str(100000))
        #费率1
        fl = 'var q = document.getElementsByName("GuItemKindRate");q[1].value=%s;' % "0.05678"
        self.driver.execute_script(fl)

        #增加保障
        self.driver.find_element_by_name("button_ItemKind_Insert").click()
        #险别2
        self.driver.find_elements_by_name("GuItemKindKindName")[2].send_keys("1109002")
        self.driver.find_elements_by_name("GuItemKindKindName")[2].send_keys(Keys.TAB)
        #每份赔偿限额2
        self.driver.find_elements_by_name("GuItemKindUnitInsured")[2].send_keys(str(100000))
        #费率2
        fl = 'var q = document.getElementsByName("GuItemKindRate");q[2].value=%s;' % "0.06857"
        self.driver.execute_script(fl)

        #增加保障
        self.driver.find_element_by_name("button_ItemKind_Insert").click()
        #险别3
        self.driver.find_elements_by_name("GuItemKindKindName")[3].send_keys("1109003")
        self.driver.find_elements_by_name("GuItemKindKindName")[3].send_keys(Keys.TAB)
        #每份赔偿限额3
        self.driver.find_elements_by_name("GuItemKindUnitInsured")[3].send_keys(str(100000))
        #费率3
        fl = 'var q = document.getElementsByName("GuItemKindRate");q[3].value=%s;' % "0.0524"
        self.driver.execute_script(fl)

        #增加保障
        self.driver.find_element_by_name("button_ItemKind_Insert").click()
        #险别2
        self.driver.find_elements_by_name("GuItemKindKindName")[4].send_keys("1109004")
        self.driver.find_elements_by_name("GuItemKindKindName")[4].send_keys(Keys.TAB)
        #每份赔偿限额2
        self.driver.find_elements_by_name("GuItemKindUnitInsured")[4].send_keys(str(100000))
        #费率2
        fl = 'var q = document.getElementsByName("GuItemKindRate");q[4].value=%s;' % "0.0457"
        self.driver.execute_script(fl)


        #方案代码/名称
        self.driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[1]").send_keys("1109A01I01")
        self.driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[3]").send_keys("中民泰康住院宝（2017升级版）-少儿版-方案一")
        #风险等级
        fxdj = 'var q = document.getElementsByName("GuItemAcciOccupationLevel");q[0].value=%d;' % 1
        self.driver.execute_script(fxdj)


        #保存
        self.driver.find_element_by_id('saveButton').click()
        time.sleep(2)


        self.calcrate()

        #取当前的窗口句柄
        __win1 = self.driver.current_window_handle
        time.sleep(3)
        #人员列表 (弹出新窗口)
        self.driver.find_element_by_xpath("//*[@id='ItemAcci']/thead/tr/td[16]/input").click()
        all_handle = self.driver.window_handles
        for handle in all_handle:
            if handle != __win1:
                self.driver.switch_to_window(handle) #进入到新的窗口
                self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input").click()#点击增加
                # self.driver.find_element_by_css_selector("input[value='增加(A)']").click()

                self.driver.switch_to_frame("QueryResultFrame")
                #被保险人名称
                self.driver.find_element_by_xpath("//*[@id='ItemAcciList']/tbody/tr[2]/td[2]/input").send_keys(tbname)
                #证件号码
                self.driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[3]/td[4]/input').send_keys(id)
                #详细地址
                self.driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[7]/td[4]/input').send_keys(address)
                #生存受益人名称
                self.driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[13]/td[2]/input').send_keys(tbname)
                #证件号码
                self.driver.find_element_by_xpath('//*[@id="ItemAcciList"]/tbody/tr[14]/td[4]/input').send_keys(id)
                #保存
                self.driver.find_element_by_xpath('//*[@id="saveBackTr"]/td/input').click()
                #单击确定
                self.driver.switch_to_alert().accept()
                time.sleep(3)
                self.driver.close()
                self.driver.switch_to_window(__win1)
        for handle in all_handle:
            if handle == __win1: #提交复合
                self.driver.switch_to_default_content()
                self.driver.implicitly_wait(5)
                self.driver.switch_to_frame("mainFrame")
                self.driver.find_element_by_name("Save").click()
                time.sleep(2)
                tbdan = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td").text
                self.toubaodanhao = tbdan[6:28]
                print (tbdan)
                time.sleep(2)
                self.driver.quit()
                time.sleep(3)

    def renwuchuli(self):#任务处理2(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(heun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(4)
        self.driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理

        self.driver.find_element_by_link_text("审核平台子系统").click()
        self.driver.find_element_by_link_text("核保审核").click()
        self.driver.find_element_by_link_text("任务处理").click()

        self.driver.switch_to_default_content()  #需要切换回主页面

        self.driver.switch_to_frame("mainFrame")   #右边的frame

        #申请单号
        self.driver.find_element_by_name("GwWfLogDtoBusinessNo").send_keys(self.toubaodanhao)
        #保存
        self.driver.find_element_by_name("buttonQuery").click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("QueryResultFrame")

        #业务号
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
        time.sleep(2)

        #滑动到审核通过
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("myFrame")

        self.driver.execute_script("arguments[0].scrollIntoView();",self.driver.find_element_by_xpath("/html/body/form/div/table[4]/tbody/tr/td[2]/input"))
        #分保试算(在有些险种里面可能会出现不存在的问题)


        win1 = self.driver.current_window_handle
        try:
            if self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tfoot/tr/td[1]/input').is_displayed() is True:
                self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tfoot/tr/td[1]/input').click()
                time.sleep(3)
                all_h = self.driver.window_handles
                for h in all_h:
                    if h !=win1:
                        self.driver.switch_to_window(h)
                        self.driver.close()
                        self.driver.switch_to_window(win1)
                self.driver.switch_to_default_content()
                self.driver.switch_to_frame("mainFrame")
                self.driver.switch_to_frame("myFrame")
        except:
            print ("ele not esixt")

        #审批片语：同意
        win1 = self.driver.current_window_handle
        __sec = Select(self.driver.find_element_by_name("NotionContent"))
        __sec.select_by_index(2)
        #审核意见
        self.driver.find_element_by_xpath('/html/body/form/div/table[4]/tbody/tr/td[9]/input').click()
        allh=self.driver.window_handles
        for h in allh:
            if h != win1:
                self.driver.switch_to_window(h)
                self.driver.close()
                self.driver.switch_to_window(win1)

        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("myFrame")
        time.sleep(3)
        #审核通过
        self.driver.find_element_by_xpath("/html/body/form/div/table[4]/tbody/tr/td[2]/input").click()
        time.sleep(1)
        self.driver.switch_to_alert().accept()

        #取保单号
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        time.sleep(5)
        retext = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td").text
        self.baodanhao =retext[-22:-2]#67501001109201700001
        print (self.baodanhao)
        print (retext)
        self.driver.quit()

    def baodanshengxiaoshijianbiangeng(self):#保单生效时间变更3(no)
        sql_1 = "update gupolicycopyrisk set startdate=to_date('2017-09-20 01:00:00','yyyy-mm-dd hh:mi:ss') where policyno='%s'" % self.baodanhao
        sql_2 = "update GuPolicyCopyEndorHead set VALIDDATE=to_date('2017-09-20 01:00:00','yyyy-mm-dd hh:mi:ss') where policyno='%s'" % self.baodanhao

        self.conn = cx_Oracle.connect(orcle_url)
        self.cursor = self.conn.cursor()
        # self.cursor.execute(sql_1)
        # self.cursor.execute(sql_2)
        self.cursor.close()

    def baoanxinzeng(self):#报案新增4(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to_frame("leftFrame")
        self.driver.find_element_by_link_text("理赔子系统").click()
        self.driver.find_element_by_link_text("报案管理").click()
        self.driver.find_element_by_link_text("报案新增").click()

        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        #报案人
        self.driver.find_element_by_name("registReportorName").send_keys(tbname)
        #报案人电话
        self.driver.find_element_by_name("registReportorPhoneNumber").send_keys(tel)
        time.sleep(2)

        # self.driver.find_element_by_xpath('//*[@id="tabMain"]/center/div/table[38]/tbody/tr/td/input[2]').click()


        #保单信息
        win1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//*[@id="Query"]/tbody/tr/td/input').click()
        all_h = self.driver.window_handles
        time.sleep(3)
        for h in all_h:
            if h !=win1:
                self.driver.switch_to_window(h)
                time.sleep(2)
                self.driver.find_element_by_name("queryPolicyPolicyNo").send_keys(self.baodanhao)
                #查询
                time.sleep(1)
                self.driver.find_element_by_css_selector("input[value='查询']").click()
                time.sleep(2)
                self.driver.switch_to_frame("QueryResultFrame")

                self.driver.find_element_by_name("checkboxSelect").send_keys(Keys.SPACE)

                self.driver.find_element_by_css_selector("input[value='新增']").click()
                time.sleep(5)
                self.driver.close()
                self.driver.switch_to_window(win1)

        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        #出险原因
        self.driver.find_element_by_name("registDamageCode").send_keys("109001")
        self.driver.find_element_by_name("registDamageCode").send_keys(Keys.TAB)
        #出险地点
        self.driver.find_element_by_name("registDamageAddress").send_keys(address)
        #出险摘要
        self.driver.find_element_by_xpath('//*[@id="resume"]/tbody/tr/td/textarea').send_keys(address)
        time.sleep(2)
        self.driver.find_element_by_name('registCatastropheName').click()
        time.sleep(1)


        #提交
        dr = self.driver.find_element_by_css_selector("input[value='提交']")
        self.driver.execute_script("arguments[0].scrollIntoView();",dr)
        time.sleep(2)
        self.driver.find_element_by_css_selector("input[value='提交']").click()
        time.sleep(2)
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        #取报案号
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        webtext=self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[3]/td').text
        print (webtext)
        self.baoanhao =webtext[-9::]
        self.driver.quit()
        time.sleep(2)

    def chakandiaoduchuli(self): #查堪调度处理5(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(3)
        self.driver.switch_to_frame("leftFrame")

        self.driver.find_element_by_link_text("理赔子系统").click()
        self.driver.find_element_by_link_text("调度管理").click()
        self.driver.find_element_by_link_text("查勘调度").click()
        self.driver.find_element_by_link_text("查勘调度处理").click()

        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")

        #报案号码
        self.driver.find_element_by_xpath('//*[@id="BeforeOverViewMain1"]/tbody/tr[1]/td[2]/input').send_keys(self.baoanhao)
        #点击查询
        self.driver.find_element_by_xpath('//*[@id="BeforeOverViewResult"]/tbody/tr[2]/td/input').click()

        self.driver.switch_to_frame("QueryResultFrame")

        #点击报案号码
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[2]/a').click()

        #
        self.driver.switch_to_alert().accept()


        time.sleep(5)
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(4)
        self.driver.switch_to_frame("mainFrame")


        #对象类型
        self.driver.find_element_by_name('DelegateDtoObjectType').send_keys("004")

        #调度单位
        self.driver.find_element_by_name('DelegateDtoCheckUnitCode').send_keys("01")
        time.sleep(1)
        self.driver.find_element_by_name('DelegateDtoCheckUnitCode').send_keys(Keys.TAB)
        #第一查勘人
        self.driver.find_element_by_name('DelegateDtoCheckerCode1').click()
        self.driver.find_element_by_name('DelegateDtoCheckerCode1').send_keys("0008054")

        #选择
        self.driver.find_element_by_css_selector("input[name='selectPolicy']").click()

        #任务指派
        self.driver.find_element_by_css_selector('input[value="任务指派"]').click()

        #提交
        self.driver.find_element_by_css_selector('input[value="提交"]').click()
        time.sleep(5)

        ##取文本
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        su = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        __retext = su[0:4]
        print (__retext)
        self.driver.quit()

    def chakanxinzeng(self):#查勘新增6(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(3)
        self.driver.switch_to_frame("leftFrame")

        self.driver.find_element_by_link_text("理赔子系统").click()
        self.driver.find_element_by_link_text("查勘管理").click()
        self.driver.find_element_by_link_text("查勘新增").click()


        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")

        #报案号码
        self.driver.find_element_by_name('GcSurveyMainDtoRegistNo').send_keys(self.baoanhao)

        #查询
        self.driver.find_element_by_xpath('//*[@id="BeforeOverViewResult"]/tbody/tr[2]/td/input').click()

        self.driver.switch_to_frame("QueryResultFrame")
        #报案号码
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[2]/a').click()
        time.sleep(4)
        self.driver.switch_to_alert().accept()
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")

        time.sleep(3)


        #人伤信息
        self.driver.find_element_by_css_selector('td[title="personInfomation"]').click()
        #+
        self.driver.find_element_by_xpath('//*[@id="person"]/tfoot/tr[1]/td/p/input').click()
        time.sleep(3)

        #点击详细信息

        self.driver.find_elements_by_css_selector('input[value="详细信息"]')[1].click()
        time.sleep(2)
        self.driver.switch_to_frame("detailFrame")

        #姓名
        self.driver.find_element_by_name('GcSurveyPersonDtoPersonCName').send_keys(tbname)

        # xingming = self.driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[1]/td[4]/input[2]')
        # ActionChains(self.driver).double_click(xingming).perform()
        # self.driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[1]/td[4]/input[2]').send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[1]/td[4]/input[2]').send_keys(Keys.ENTER)
        time.sleep(2)

        #职业大类
        self.driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[6]/td[2]/input[1]').send_keys("00101")
        self.driver.find_element_by_xpath('//*[@id="personInfo"]/tbody/tr[6]/td[2]/input[1]').send_keys(Keys.TAB)
        time.sleep(2)


        #性别
        __xb = Select(self.driver.find_element_by_xpath("//*[@id='personInfo']/tbody/tr[2]/td[2]/select"))
        __xb.select_by_value("1")
        # __xb.select_by_index(1)

        #意外伤害
        self.driver.find_element_by_link_text("意外伤害").click()
        self.driver.find_element_by_css_selector('input[value="IC017"]').click()
        #保存
        self.driver.find_element_by_xpath('/html/body/form/table[8]/tbody/tr/td[1]/input').click()

        #基本信息
        time.sleep(3)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        self.driver.find_element_by_css_selector("td[title='main']").click()
        time.sleep(3)

        #财产查勘
        #点+号
        self.driver.find_element_by_xpath('//*[@id="propFee"]/tfoot/tr/td/p/input').click()
        self.driver.implicitly_wait(5)

        #险别
        # __xb = self.driver.find_elements_by_name('GcSurveyPropDtoKindCode')[1]
        # ActionChains(self.driver).double_click(__xb).perform()
        # __xb.send_keys(Keys.ENTER)
        # __xb.send_keys(Keys.ENTER)

        # xb = 'var q = document.getElementsByName("GcSurveyPropDtoKindCode");q[1].value ="%s";'% "1128001"#1109016
        # self.driver.execute_script(xb)
        self.driver.find_elements_by_name('GcSurveyPropDtoKindCode')[1].send_keys("1109016")
        self.driver.find_elements_by_name('GcSurveyPropDtoKindCode')[1].send_keys(Keys.TAB)
        #险别估损金额
        self.driver.find_elements_by_name('GcSurveyPropDtoSumLoss')[1].send_keys("200")

        #人伤查勘估损
        self.driver.find_element_by_xpath('//*[@id="injured"]/tfoot/tr/td/p/input').click()
        time.sleep(2)
        #姓名
        __xm =self.driver.find_elements_by_name('GcSurveyPersonFeeDtoPersonCName')[1]
        ActionChains(self.driver).double_click(__xm).perform()
        __xb.send_keys(Keys.ENTER)
        __xb.send_keys(Keys.ENTER)


        #险别
        __xb1 = self.driver.find_elements_by_name('GcSurveyPersonFeeDtoKindCode')[1]
        ActionChains(self.driver).double_click(__xb1).perform()
        __xb1.send_keys(Keys.ENTER)
        __xb1.send_keys(Keys.ENTER)

        #险别估损金额
        self.driver.find_elements_by_name('GcSurveyPersonFeeDtoSumLoss')[1].send_keys("200")

        #查勘报告
        self.driver.find_element_by_id('img2').click()
        #出现经过
        self.driver.find_element_by_name('GcSurveyMainDtoDamageDescription').send_keys("Me Against the World")

        #查勘新增
        self.driver.find_element_by_name('GcSurveyMainDtoContext').send_keys("让世界感受痛楚")
        #报损及损失核定
        self.driver.find_element_by_name('GcSurveyMainDtoExt1').send_keys("没人知道我的痛苦有多深")


        #处理意见
        self.driver.find_element_by_id('img1').click()
        self.driver.find_element_by_name('GcSurveyMainDtoExt6').send_keys("同意")

        #点提交
        self.driver.find_element_by_xpath('//*[@id="button"]/tbody/tr/td/input[4]').click()
        self.driver.switch_to_alert().accept()

        #取文本
        time.sleep(5)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        succ = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        __retext = succ[0:4]
        print (__retext)
        self.driver.quit()
        return  __retext

    def renshenggenzongxinzeng(self):#人伤跟踪新增7(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to_frame("leftFrame")

        self.driver.find_element_by_link_text("理赔子系统").click()
        self.driver.find_element_by_link_text("人伤跟踪管理").click()
        self.driver.find_element_by_link_text("人伤跟踪新增").click()

        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")

        #报案号码
        self.driver.find_element_by_name('gcRegistPolicyDtoRegistNo').send_keys(self.baoanhao)

        #查询
        self.driver.find_elements_by_css_selector('input[value="查询"]')[1].click()

        #点击报案号码
        self.driver.switch_to_frame('QueryResultFrame')
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
        time.sleep(2)


        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        #点+号
        time.sleep(2)
        self.driver.find_element_by_css_selector('input[value="+"]').click()

        #change code to doubleclick,feiyong mingxi

        fy = self.driver.find_elements_by_name("gcCarEvaluateFeeDtoKindCode")[1]
        ActionChains(self.driver).double_click(fy).perform()
        fy.send_keys(Keys.ENTER)
        fy.send_keys(Keys.ENTER)

        '''
        #险别
        xb = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoKindCode");q[1].value ="%s";'% "1128001"
        self.driver.execute_script(xb)
        #费用
        fy = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoFeeTypeCode");q[1].value = "%s";'% "04"
        self.driver.execute_script(fy)
        '''
        #点位金额
        je = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoUnitLossAmount");q[1].value = %d;' % 200
        self.driver.execute_script(je)

        #点数量
        sl = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoLossQuantity");q[1].value = %d;' % 1
        self.driver.execute_script(sl)

        time.sleep(5)

        #损失
        ss= 'var q = document.getElementsByName("gcCarEvaluateFeeDtoSumLoss");q[1].value = %d;' % 200
        self.driver.execute_script(ss)

        #定损
        ds= 'var q = document.getElementsByName("gcCarEvaluateFeeDtoSumDefLoss");q[1].value = %d;' % 200
        self.driver.execute_script(ds)

        self.driver.find_element_by_css_selector('input[value="提交"]').click()
        self.driver.switch_to_alert().accept()

        #取值
        time.sleep(4)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        fi = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        __retext = fi[0:4]
        print (__retext)
        self.driver.quit()
        return  __retext

    def feichedingsunguan(self):#非车定损管理定核损新增8 (ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to_frame("leftFrame")

        self.driver.find_element_by_link_text("理赔子系统").click()
        self.driver.find_element_by_link_text("非车定损管理").click()
        self.driver.find_element_by_link_text("定核损新增").click()


        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        self.driver.implicitly_wait(5)
        #报案号码
        self.driver.find_element_by_name('GcEvaluateMainDtoRegistNo').send_keys(self.baoanhao)

        #查询
        self.driver.find_elements_by_css_selector('input[value="查询"]')[1].click()

        #点击报案号码
        self.driver.switch_to_frame('QueryResultFrame')
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
        time.sleep(4)
        # self.driver.implicitly_wait(5)
        self.driver.switch_to_alert().accept()
        time.sleep(4)
        self.driver.switch_to_alert().accept()

        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        self.driver.implicitly_wait(5)
        time.sleep(5)

        #点击定损信息
        self.driver.find_element_by_css_selector('td[title="Loss"]').click()
        time.sleep(1)
        #财产相关定损信息
        self.driver.find_element_by_css_selector('input[value="+"]').click()

        #险别
        ele = self.driver.find_elements_by_name("gcEvaluatePropDtoKindCode")[1]
        ActionChains(self.driver).double_click(ele).perform()
        ele.send_keys(Keys.ENTER)
        ele.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(3)


        #提交
        self.driver.find_element_by_css_selector('input[value="提交"]').click()


        #取操作成功
        time.sleep(4)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        __fi = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        __retext = __fi[0:4]
        print (__retext)
        self.driver.quit()
        return (__retext)

    def lisuanxinzeng(self):#理算新增9(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(3)
        self.driver.switch_to_frame("leftFrame")

        self.driver.find_element_by_link_text("理赔子系统").click()
        self.driver.find_element_by_link_text("理算管理").click()
        self.driver.find_element_by_link_text("理算新增").click()

        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        self.driver.implicitly_wait(5)

        #报案号码
        self.driver.find_element_by_name('queryClaimRegistNo').send_keys(self.baoanhao)

        #查询
        self.driver.find_elements_by_css_selector('input[value="查询"]')[1].click()

        #点击报案号码
        self.driver.switch_to_frame('QueryResultFrame')
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
        time.sleep(2)

        #点击确定
        self.driver.switch_to_alert().accept()

        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        self.driver.implicitly_wait(5)


        #交易特征--经识别未发现
        jiaoyitezheng = Select(self.driver.find_element_by_name('adjustmentMainSuspiciousInd'))
        jiaoyitezheng.select_by_index(4)
        time.sleep(5)

        #赔付信息点击
        self.driver.find_elements_by_tag_name('NOBR')[1].click()

        #理算计算过程
        self.driver.find_element_by_id('contextImg45').click()

        #生成计算书
        self.driver.find_element_by_css_selector('input[value="生成计算书"]').click()

        #提交
        self.driver.find_element_by_css_selector('input[value="提交"]').click()
        time.sleep(3)

        self.driver.switch_to_alert().accept()

        #理算号码

        #操作成功！
        time.sleep(4)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        te = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        __lisuan = te[0:4]
        print (__lisuan)
        self.driver.quit()

    def zhifuluru(self):#支付录入10(ok)
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.get(url)
        driver.find_element_by_id("username").send_keys(lpun)
        driver.find_element_by_id("password").send_keys(pw)
        driver.find_element_by_id("bt_submit").submit()
        time.sleep(3)
        driver.switch_to_frame("leftFrame")

        driver.find_element_by_link_text("理赔子系统").click()
        driver.find_element_by_link_text("单证收集管理").click()
        driver.find_element_by_link_text("支付录入").click()

        driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")


        #报案号码
        driver.find_element_by_name('queryAdjustmentRegistNo').send_keys(self.baoanhao)

        #查询
        driver.find_elements_by_css_selector('input[value="查询"]')[1].click()
        #点击报案号码
        driver.switch_to_frame('QueryResultFrame')
        driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()


        #alert
        time.sleep(3)
        driver.switch_to_alert().accept()

        #赔付信息点击
        driver.switch_to_default_content()
        driver.switch_to_frame("mainFrame")
        driver.find_elements_by_tag_name('NOBR')[1].click()

        #拉到最下面
        dr = driver.find_element_by_xpath('//*[@id="vewFeeInfoInfo"]/tbody/tr[1]/td[4]/input')
        driver.execute_script("arguments[0].scrollIntoView();", dr)
        #收款人姓名

        driver.find_elements_by_name('adjustmentFeePayeeView')[1].send_keys(skname)

        #银行名称
        driver.find_elements_by_name('adjustmentFeePayeeBankAccountNameView')[1].send_keys(bankname)

        #支付机构
        js3 = 'var q = document.getElementsByName("adjustmentFeePaymentComNameView");q[1].value = "%s";' % "01"
        driver.execute_script(js3)

        #详细
        driver.find_elements_by_name('imgShowFeeDetail')[1].click()

        #支付机构
        zfjg = driver.find_elements_by_name('adjustmentFeePaymentComCode')[1]
        ActionChains(driver).double_click(zfjg).perform()
        zfjg.send_keys(Keys.ENTER)
        zfjg.send_keys(Keys.ENTER)

        #联系人电话
        lxdh = driver.find_elements_by_name('adjustmentFeePayeeMobile')[1]
        lxdh.send_keys(tel)

        #证件号码
        zjhm = driver.find_elements_by_name('adjustmentFeeIdNo')[1]
        zjhm.send_keys(id)

        #确定
        driver.find_elements_by_css_selector('input[value="确定"]')[2].click()

        #提交
        driver.find_element_by_css_selector('input[value="提交"]').click()

        #
        time.sleep(2)
        driver.switch_to_alert().accept()


        #取值
        driver.switch_to_default_content()
        driver.switch_to_frame('mainFrame')
        time.sleep(4)
        __fi = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        __retext = __fi[0:4]
        print (__retext)
        driver.quit()

    def hepeishenhe(self):#核赔审核待处理任务查询11(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(lpun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to_frame("leftFrame")

        self.driver.find_element_by_link_text("审核平台子系统").click()
        self.driver.find_element_by_link_text("核赔审核").click()
        self.driver.find_element_by_link_text("待处理任务查询").click()

        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")

        #报案号
        self.driver.find_element_by_name('GwWfLogDtoContractNo').send_keys(self.baoanhao)

        #点击查询
        self.driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[1]/td/input').click()

        #报案号

        self.driver.switch_to_frame("QueryResultFrame")
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
        time.sleep(5)
        #选择同意
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        __win1 = self.driver.current_window_handle
        ser = Select(self.driver.find_element_by_name('NotionContent'))
        ser.select_by_index(7)
        time.sleep(3)


        #点击审核意见


        self.driver.find_element_by_name('butViewTranceInfo').click()
        time.sleep(4)
        __allwin = self.driver.window_handles
        for hand in __allwin:
            if hand != __win1:
                self.driver.switch_to_window(hand)
                time.sleep(2)
                self.driver.close()
                self.driver.switch_to_window(__win1)
        #点击审核通过
        time.sleep(3)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        self.driver.find_element_by_name('passBtn').click()
        #确定
        time.sleep(2)
        self.driver.switch_to_alert().accept()

        #确定
        time.sleep(1)
        self.driver.switch_to_alert().accept()


        #取结案号
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        time.sleep(3)

        __fi = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        print (__fi)
        __jieanhao = __fi[-20::]
        print (__jieanhao)
        self.driver.quit()

    def run(self):
        self.toubaochuli()
        self.renwuchuli()
        self.baodanshengxiaoshijianbiangeng()
        self.baoanxinzeng()
        self.chakandiaoduchuli()
        self.chakanxinzeng()
        self.renshenggenzongxinzeng()
        self.feichedingsunguan()
        self.lisuanxinzeng()
        self.zhifuluru()
        self.hepeishenhe()

if __name__ == '__main__':
    HeXinCaiXian_D().run()