 import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select
# import cx_Oracle

#create by grape Shi

#####basic infora#####
url = "http://10.130.201.36:7001/index.jsp"
tbun = "policy3@upic"                   #投保用户名
heun= "uwprpall@upic"                   #核保用户名
lpun= "0008054"                         #理赔用户名
pw  ="upic@123"
uwpw = "upic@1234567"                   #密码
# tbname = "玉皇大帝"                        #
tbname = "投保人"                        #
id = "14050119800101019X"               #
address = "北海道查干湖"
postcode = "047500"
tel = "13601234567"
skname = "宫本武藏"                      #收款人
bankname = "中国银行"                    #收款银行
########################

##oracle##
orcle_url= "upiccore/sinosoft@10.130.201.118:1521/tkpi"
####


#100130320180000005
class HeXinPiGai:
    def __init__(self):

        self.toubaodanhao = "" #投保单号
        self.baodanhao    = "" #保单号
        self.pidanshen    = ""#批单申请号
        self.pidanhao     = ""#批单号
        self.operasucc   = "操作成功"                 #
    #捕获弹窗
    def alert_acc(self):
        time.sleep(1)
        try:
            if self.driver.switch_to.alert:
                self.driver.switch_to_alert().accept()
        except:
            pass
    #判断元素是否存在(xpath)
    def isEleExi(self,ele):
        try:
            ifele = self.driver.find_element_by_xpath(ele)
            ifele.click()
        except:
            pass
    #判断元素是否存在(name)
    def isNameExi(self,ele):
        try:
            ifele = self.driver.find_element_by_name(ele)
            ifele.click()
        except:
            pass
    #判断元素是否存在(xpath)
    def isExistAndClick(self,ele):
        df = self.driver.find_elements_by_xpath(ele)
        print (len(df))
        if len(df) != 0:
            df[0].click()
        else:
            pass
    def toubaochuli(self,riskcode):#投保处理1(ok)
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()

        time.sleep(4)
        self.driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理
        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("投保管理").click()
        self.driver.find_element_by_link_text("投保处理").click()

        self.driver.switch_to_default_content()  #需要切换回主页面
        self.driver.switch_to_frame("mainFrame")   #右边的frame
        self.driver.find_element_by_xpath(".//*[@id='RiskArea']/table[1]/tbody/tr/td[4]/input[1]").send_keys(riskcode)
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
        self.driver.find_element_by_name("GuMainAgreementNo").send_keys("010000000000600052")
        self.driver.find_element_by_name("GuMainAgreementNo").send_keys(Keys.TAB)
        time.sleep(1)
        #子协议代码
        self.driver.find_element_by_name("GuMainSolutionCode").send_keys("0100000000006000520001")
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
        self.alert_acc()
        time.sleep(1)
        #保存客户
        self.driver.find_element_by_name('buttonSaveCustomer').click()
        self.alert_acc()

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

        #特别约定代码
        self.driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys('0117')#0326
        self.driver.find_elements_by_name("GuRiskSpecialClausesClauseCode")[1].send_keys(Keys.TAB)
        time.sleep(1)
        #产品方案代码/名称
        self.driver.find_element_by_name("GuRiskDynamicFieldAI").send_keys("1107G103")#1128A00001
        self.driver.find_element_by_name("GuRiskDynamicFieldAI").send_keys(Keys.TAB)
        time.sleep(1)

        #
        self.driver.find_element_by_name('GuRiskDynamicFieldAK').send_keys("健康告知")
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
        #险别
        self.driver.find_elements_by_name("GuItemKindKindName")[1].send_keys("1107001")#1128001
        self.driver.find_elements_by_name("GuItemKindKindName")[1].send_keys(Keys.TAB)
        #每份赔偿限额
        self.driver.find_elements_by_name("GuItemKindUnitInsured")[1].send_keys("100000")
        #费率
        fl = 'var q = document.getElementsByName("GuItemKindRate");q[1].value=%s;' % "0.056"
        self.driver.execute_script(fl)
        #方案代码/名称
        self.driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[1]").send_keys("1107A00001")#1128A00001
        self.driver.find_element_by_xpath("//*[@id='ItemAcci']/tbody[2]/tr/td[2]/input[3]").send_keys("美团骑手意外险")#体育运动个人意外险
        #风险等级
        fxdj = 'var q = document.getElementsByName("GuItemAcciOccupationLevel");q[0].value=%d;' % 1
        self.driver.execute_script(fxdj)
        #保存
        self.driver.find_element_by_id('saveButton').click()
        time.sleep(4)
        #取当前的窗口句柄
        __win1 = self.driver.current_window_handle
        time.sleep(4)
        #人员列表 (弹出新窗口)
        self.driver.find_element_by_xpath("//*[@id='ItemAcci']/thead/tr/td[16]/input").click()
        all_handle = self.driver.window_handles
        for handle in all_handle:
            if handle != __win1:
                self.driver.switch_to_window(handle) #进入到新的窗口
                self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input").click()#点击增加
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
                self.alert_acc()
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
        self.driver.switch_to_frame("leftFrame")

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

        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("myFrame")


        win1 = self.driver.current_window_handle
        #分保试算
        # self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tfoot/tr/td[1]/input').click()
        self.isEleExi('//*[@id="ResultTable"]/tfoot/tr/td[1]/input')
        # self.isEleExi('//*[@id="ResultTable"]/tfoot/tr/td[1]/input/excle')
        time.sleep(2)
        all_h = self.driver.window_handles
        for h in all_h:
            if h !=win1:
                self.driver.switch_to_window(h)
                self.driver.close()
                self.driver.switch_to_window(win1)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("myFrame")
        #审批片语：同意
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
        self.alert_acc()
        self.alert_acc()

        #取保单号
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        time.sleep(5)
        retext = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td").text
        self.baodanhao =retext[-22::]
        print (retext)
        self.driver.quit()
        time.sleep(3)
    #批改申请处理
    def pigailianxiren(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理

        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("批改管理").click()
        self.driver.find_element_by_link_text("批改申请处理").click()

        self.driver.switch_to_default_content()  #需要切换回主页面
        self.driver.switch_to_frame("mainFrame")   #右边的frame
        self.driver.find_element_by_name('PolicyNo').send_keys(self.baodanhao)
        self.driver.find_element_by_css_selector('input[value="下一步"]').click()

        #01批改关系人
        ser = Select(self.driver.find_element_by_name("endorType"))
        ser.select_by_index(0)
        # >>
        self.driver.find_element_by_css_selector('input[value=">>"]').click()
        time.sleep(1)
        #下一步
        self.driver.find_element_by_css_selector('input[value="下一步"]').click()
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        self.driver.switch_to_frame('myFrame')

        self.driver.find_element_by_name('AppliGuRelatedPartyInsuredName').clear()
        self.driver.find_element_by_name('AppliGuRelatedPartyInsuredName').send_keys("玉皇大帝")
        time.sleep(10)
        #保存
        self.driver.find_element_by_id("saveButton").click()
        self.alert_acc()
        self.alert_acc()
        #点批文信息
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.switch_to_frame("myFrame") #切换到里面的frame
        self.driver.switch_to_frame("RiskFrame")

        self.driver.find_elements_by_id('mySubTD')[4].click()
        self.driver.switch_to_frame("myFrame")
        #点击生成默认批文
        self.driver.find_element_by_css_selector("input[value='生成默认批文']").click()
        time.sleep(1)
        #点击保存
        self.driver.find_element_by_id('saveButton').click()
        #点击提交复核
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        self.driver.find_element_by_name("Save").click()
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        tbdan = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td").text

        self.pidanshen = tbdan[6:28]
        print (self.pidanshen)
        print (tbdan)
        time.sleep(2)
        self.driver.quit()
        time.sleep(3)
    #保单注销
    def baodanzhuxiao(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理

        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("批改管理").click()
        self.driver.find_element_by_link_text("批改申请处理").click()

        self.driver.switch_to_default_content()  #需要切换回主页面
        self.driver.switch_to_frame("mainFrame")   #右边的frame
        self.driver.find_element_by_name('PolicyNo').send_keys(self.baodanhao)
        self.driver.find_element_by_css_selector('input[value="下一步"]').click()

        #15保单注销
        ser = Select(self.driver.find_element_by_name("endorType"))
        ser.select_by_index(4)
        # >>
        self.driver.find_element_by_css_selector('input[value=">>"]').click()
        time.sleep(1)
        #下一步
        self.driver.find_element_by_css_selector('input[value="下一步"]').click()
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        self.driver.switch_to_frame('myFrame')

        #保存
        self.driver.find_element_by_id("saveButton").click()
        self.alert_acc()
        self.alert_acc()
        #点保单费用信息
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.find_elements_by_id('myTD')[2].click()
        self.driver.switch_to_frame("myFrame")
        #帐户名称
        self.driver.find_element_by_name('adjustmentFeePayeeBankAccountName').send_keys(tbname)
        #银行账号
        self.driver.find_element_by_name('adjustmentFeeAccountNo').send_keys("23210215555555")
        #银行
        self.driver.find_element_by_name('adjustmentFeePayeeBankCode').send_keys('102')
        time.sleep(1)
        self.driver.find_element_by_name('adjustmentFeePayeeBankCode').send_keys(Keys.TAB)

        #分支行
        fenzhi = self.driver.find_element_by_name('adjustmentFeeBankBranchName')
        ActionChains(self.driver).double_click(fenzhi).perform()
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys(Keys.ENTER)
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys(Keys.ENTER)

        '''
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys('102100000021')
        time.sleep(1)
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys(Keys.TAB)
        '''
        #保存
        self.driver.find_element_by_name('saveButton').click()
        time.sleep(3)
        #险种信息
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.find_elements_by_id('myTD')[1].click()
        #点批文信息

        self.driver.switch_to_frame("myFrame") #切换到里面的frame
        self.driver.switch_to_frame("RiskFrame")

        self.driver.find_elements_by_id('mySubTD')[4].click()
        self.driver.switch_to_frame("myFrame")
        #点击生成默认批文
        self.driver.find_element_by_css_selector("input[value='生成默认批文']").click()
        time.sleep(1)
        #点击保存
        self.driver.find_element_by_id('saveButton').click()
        #点击提交复核
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        self.driver.find_element_by_name("Save").click()

        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        tbdan = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td").text

        self.pidanshen = tbdan[6:28]
        print (tbdan)
        time.sleep(2)
        self.driver.quit()
        time.sleep(3)
    #全单退保
    def quandantuibao(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element_by_id("username").send_keys(tbun)
        self.driver.find_element_by_id("password").send_keys(pw)
        self.driver.find_element_by_id("bt_submit").submit()
        time.sleep(2)
        self.driver.switch_to_frame("leftFrame") #切换到左边的frame，选择投保处理

        self.driver.find_element_by_link_text("承保子系统").click()
        self.driver.find_element_by_link_text("批改管理").click()
        self.driver.find_element_by_link_text("批改申请处理").click()

        self.driver.switch_to_default_content()  #需要切换回主页面
        self.driver.switch_to_frame("mainFrame")   #右边的frame
        self.driver.find_element_by_name('PolicyNo').send_keys(self.baodanhao)
        self.driver.find_element_by_css_selector('input[value="下一步"]').click()

        #16全单退保
        ser = Select(self.driver.find_element_by_name("endorType"))
        ser.select_by_index(5)
        # >>
        self.driver.find_element_by_css_selector('input[value=">>"]').click()
        time.sleep(1)

        #修改时间
        sj = 'var q = document.getElementsByName("GuEndorHeadValidDate");q[0].value ="%s";' % "2017-12-17"
        self.driver.execute_script(sj)

        #下一步
        self.driver.find_element_by_css_selector('input[value="下一步"]').click()
        self.alert_acc()
        # self.alert_acc()
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        self.driver.switch_to_frame('myFrame')

        #保存
        self.driver.find_element_by_id("saveButton").click()
        self.alert_acc()
        self.alert_acc()
        #点保单费用信息
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.find_elements_by_id('myTD')[2].click()
        self.driver.switch_to_frame("myFrame")
        #帐户名称
        self.driver.find_element_by_name('adjustmentFeePayeeBankAccountName').send_keys(tbname)
        #银行账号
        self.driver.find_element_by_name('adjustmentFeeAccountNo').send_keys("23210215555555")
        #银行
        self.driver.find_element_by_name('adjustmentFeePayeeBankCode').send_keys('102')
        time.sleep(1)
        self.driver.find_element_by_name('adjustmentFeePayeeBankCode').send_keys(Keys.TAB)

        #分支行
        fenzhi = self.driver.find_element_by_name('adjustmentFeeBankBranchName')
        ActionChains(self.driver).double_click(fenzhi).perform()
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys(Keys.ENTER)
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys(Keys.ENTER)

        '''
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys('102100000021')
        time.sleep(1)
        self.driver.find_element_by_name('adjustmentFeeBankBranchName').send_keys(Keys.TAB)
        '''
        #保存
        self.driver.find_element_by_name('saveButton').click()
        time.sleep(3)
        #险种信息
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame") #切换到右边的frame
        self.driver.find_elements_by_id('myTD')[1].click()
        #点批文信息

        self.driver.switch_to_frame("myFrame") #切换到里面的frame
        self.driver.switch_to_frame("RiskFrame")

        self.driver.find_elements_by_id('mySubTD')[4].click()
        self.driver.switch_to_frame("myFrame")
        #点击生成默认批文
        self.driver.find_element_by_css_selector("input[value='生成默认批文']").click()
        time.sleep(1)
        #点击保存
        self.driver.find_element_by_id('saveButton').click()
        #点击提交复核
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("mainFrame")
        self.driver.find_element_by_name("Save").click()
        #取值
        time.sleep(2)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        tbdan = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td").text

        self.pidanshen = tbdan[6:28]
        print (tbdan)
        time.sleep(2)
        self.driver.quit()
    #任务处理_生成批单号
    def renwuchulis(self):#任务处理2(ok)
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
        self.driver.find_element_by_name("GwWfLogDtoBusinessNo").send_keys(self.pidanshen)
        #查询
        self.driver.find_element_by_name("buttonQuery").click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame("QueryResultFrame")

        #业务号
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()

        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("myFrame")

        #分保试算
        win1 = self.driver.current_window_handle

        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tfoot/tr/td[1]/input').click()

        time.sleep(2)
        all_h = self.driver.window_handles
        for h in all_h:
            if h !=win1:
                self.driver.switch_to_window(h)
                self.driver.close()
                self.driver.switch_to_window(win1)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        self.driver.switch_to_frame("myFrame")
        #审批片语：同意
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
        time.sleep(2)
        #审核通过
        self.driver.find_element_by_xpath("/html/body/form/div/table[4]/tbody/tr/td[2]/input").click()
        time.sleep(1)
        self.alert_acc()
        self.alert_acc()

        #取保单号
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        time.sleep(5)
        # retext = self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[1]/table[1]/tbody/tr[2]/td").text
        retext = self.driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[1]/td/table[1]/tbody/tr[2]/td').text

        self.pidanhao =retext[-26::]
        print (self.pidanhao)
        print (retext)
        self.driver.quit()
    def run(self):
        self.toubaochuli('1107')
        self.renwuchuli()
        self.pigailianxiren()
        # self.baodanzhuxiao()
        # self.quandantuibao()
        # self.renwuchulis()
if __name__ == '__main__':
    HeXinPiGai().run()
