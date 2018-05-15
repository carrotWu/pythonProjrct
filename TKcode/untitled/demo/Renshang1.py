import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select
import cx_Oracle
import xlrd
from xlutils.copy import copy
from decimal import Decimal
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

class a:
    def __init__(self):
        self.baoanhao=170514042

    def renshenggenzongxinzeng(self):  # 人伤跟踪新增7(ok)
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

        # 报案号码
        self.driver.find_element_by_name('gcRegistPolicyDtoRegistNo').send_keys(self.baoanhao)

        # 查询
        self.driver.find_elements_by_css_selector('input[value="查询"]')[1].click()

        # 点击报案号码
        self.driver.switch_to_frame('QueryResultFrame')
        self.driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
        time.sleep(2)

        self.driver.switch_to_default_content()
        self.driver.switch_to_frame("mainFrame")
        # 点+号
        time.sleep(2)
        self.driver.find_element_by_css_selector('input[value="+"]').click()

        # change code to doubleclick,feiyong mingxi

        fy = self.driver.find_elements_by_name("gcCarEvaluateFeeDtoKindCode")[1]
        ActionChains(self.driver).double_click(fy).perform()
        fy.send_keys(Keys.ENTER)
        fy.send_keys(Keys.ENTER)

        # 点位金额
        je = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoUnitLossAmount");q[1].value = %d;' % 200
        self.driver.execute_script(je)

        # 点数量
        sl = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoLossQuantity");q[1].value = %d;' % 1
        self.driver.execute_script(sl)

        time.sleep(5)

        # 损失
        ss = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoSumLoss");q[1].value = %d;' % 200
        self.driver.execute_script(ss)

        # 定损
        ds = 'var q = document.getElementsByName("gcCarEvaluateFeeDtoSumDefLoss");q[1].value = %d;' % 200
        self.driver.execute_script(ds)

        #意健险信息
        self.driver.find_element_by_css_selector('td[title="acci"]').click()
        self.driver.find_element_by_css_selector("[tabIndex='302']").click()
        self.driver.find_element_by_css_selector("[tabIndex='303']").send_keys("2017-12-25")
        self.driver.find_element_by_name('GcMedicalFeeMainDtoDetailAdress').send_keys("东城区")
        self.driver.find_element_by_name('GcMedicalFeeMainDtoHospitalName').send_keys("朝阳区左家庄街道新源里西社区卫生服务站")
        
        ser = Select(self.driver.find_element_by_name('GcMedicalFeeMainDtoClaimInvestigation'))
        ser.select_by_index(1)

        self.driver.find_element_by_name('imgShowCommonMedicone').click()
        #点+好
        self.driver.find_element_by_name('buttonCommonMediconeListInfoInsert').click()
        #点西医

        se = Select(self.driver.find_elements_by_name('GcMedicalClinicDetailDtoDiseaseType')[9])
        se.select_by_index(1)

        #病按照从左到右顺序输入
        zb1 = 'var q = document.getElementsByName("GcMedicalClinicDetailDtoDisease1");q[9].value = "%s";' % "K00-K93"
        self.driver.execute_script(zb1)

        zb2 = 'var q = document.getElementsByName("Disease1Name");q[9].value = "%s";' % "消化系统疾病"
        self.driver.execute_script(zb2)

        zb3 = 'var q = document.getElementsByName("GcMedicalClinicDetailDtoDisease2");q[9].value = "%s";' % "K00-K14"
        self.driver.execute_script(zb3)

        zb4 = 'var q = document.getElementsByName("Disease2Name");q[9].value = "%s";' % "口腔、涎腺和颌疾病"
        self.driver.execute_script(zb4)

        zb5 = 'var q = document.getElementsByName("GcMedicalClinicDetailDtoDisease3");q[9].value = "%s";' % "K01"
        self.driver.execute_script(zb5)

        zb6 = 'var q = document.getElementsByName("Disease3Name");q[9].value = "%s";' % "埋伏牙和阻生牙"
        self.driver.execute_script(zb6)

        zb7 = 'var q = document.getElementsByName("GcMedicalClinicDetailDtoDiseaseCode");q[9].value = "%s";' % "K01.1"
        self.driver.execute_script(zb7)

        zb8 = 'var q = document.getElementsByName("DiseaseCodeName");q[9].value = "%s";' % "阻生牙"
        self.driver.execute_script(zb8)


        #临床诊断
        self.driver.find_elements_by_css_selector("input[name='GcMedicalClinicDetailDtoDiagnosisType']")[63].click()

        #确定
        self.driver.find_elements_by_css_selector("input[value='确定']")[11].click()

        self.driver.find_element_by_css_selector('input[value="提交"]').click()
        self.driver.switch_to_alert().accept()

        # 取值
        time.sleep(4)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        fi = self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
        __retext = fi[0:4]
        print (__retext)
        self.driver.quit()
        return __retext


if __name__ == '__main__':
    a().renshenggenzongxinzeng()
