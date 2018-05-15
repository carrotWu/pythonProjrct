from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import win32api
import win32con
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re
import xlrd
VK_CODE = {
    # 'spacebar': 0x20,
    # 'alt': 0x12,
    # 'n': 0x4E,
    # 'a': 0x41,
    'c': 0x43,
    'ctrl': 0x11,
    'win': 91,
    'm': 0x4D,
}

time_out=30

data=[
# '06000031360121800000064263',
# '06000031360321800000064238',
# '06000031360321800000064210',
# '06000031360321800000064211',
# '06000031360321800000064214',
# '06000031360321800000064215',
# '06000031360321800000064216',
# '06000031360321800000064217',
# '06000031360321800000064219',
# '06000031360321800000064220',
# '06000031360321800000064223',
# '06000031360321800000064225',
# '06000031360321800000064226',
# '06000031360321800000064227',
# '06000031360321800000064228',
# '06000031360321800000064229',
# '06000031360321800000064230',
# '06000031360321800000064231',
# '06000031360321800000064232',
# '06000031360321800000064234',
# '06000031360321800000064236',
# '06000031360321800000064238',
# '06000031360321800000064202',
# '06000031360321800000064203',
# '06000031360321800000064204',
# '06000031360321800000064208',
# '06000031360321800000064213',
# '06000031360321800000064218',
# '06000031360321800000064221',
# '06000031360321800000064233',
# '06000031360321800000064235',
# '06000031360321800000064237',
# '06000031360321800000064239',
# '06000031360321800000064240',
# '06000031360321800000064241',
# '06000031360321800000064242',
# '06000031360321800000064243',
# '06000031360321800000064246',
# '06000031360321800000064247',
# '06000031360321800000064249',
# '06000031360321800000064255',
# '06000031360321800000064256',
# '06000031360321800000064205',
# '06000031360321800000064206',
# '06000031360321800000064207',
# '06000031360321800000064222',
# '06000031360321800000064224',
# '06000031360321800000064244',
# '06000031360321800000064245',
# '06000031360321800000064248',
# '06000031360321800000064250',
# '06000031360321800000064251',
# '06000031360321800000064252',
# '06000031360321800000064253',
# '06000031360321800000064254',
# '06000031360321800000064257',
# '06000031360321800000064258',
# '06000031360321800000064259',
# '06000031360321800000064260',
# '06000031360321800000064261',
# '06000031360321800000064262',
# '06000031360321800000064263'
#

'06000031360121800000064263',
'06000031360321800000064231',
'06000031360321800000064238',
'06000031360321800000064233',
'06000031360321800000064235'
]


class Procedure:
    #从excell中读取保单号
    def getDataFromSheet(self,excelPath,sheetName):
        dataList = []
        # 读取excel数据
        data = xlrd.open_workbook(excelPath)
        # 获取一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取工作表的总行数
        nrows = table.nrows
        if nrows:
            for line in range(nrows):
                rowData = table.row_values(line)
                dataList.append(rowData[0])
            return dataList
        else:
            print("读取数据完毕！")

    #双击
    def DoublieClickByNamesAndIndex(self, name, index):
        fy = self.driver.find_elements_by_name(name)[index]
        ActionChains(self.driver).double_click(fy).perform()
        time.sleep(1)
        fy.send_keys(Keys.ENTER)
        time.sleep(1)
        fy.send_keys(Keys.ENTER)

    #通过css单击
    def click_by_css_selector(self,css):
        WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css))).click()

    #通过link_text单击
    def click_by_link_text(self,link_text):
        WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text))).click()

    #通过css填写内容
    def send_by_css_selector(self,css,content):
        ele = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        ele.clear()
        ele.send_keys(content)

    #通过js填写内容
    def send_use_js_by_namesAndIndex(self,names,index,content):
        js = 'var q=document.getElementsByName("%s");q[%d].value ="%s"' % (names, index, content)
        self.driver.execute_script(js)

    #根据classname点击
    def ClickByClassName(self, className):
        el = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
        el.click()

    #通过css获取标签文本
    def getTextByCss(self, css):
        ele = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        return ele.text

    #等待frame并切入（通过name）
    def switch_to_frame_by_name(self,name):
        WebDriverWait(self.driver, time_out).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,name)))

    #等待frame并切入（id）
    def switch_to_frame_by_id(self,id):
        WebDriverWait(self.driver, time_out).until(EC.frame_to_be_available_and_switch_to_it((By.ID,id)))

    #等待frame并切入（通过css）
    def switch_to_frame_by_css(self,css):
        WebDriverWait(self.driver, time_out).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,css)))

    #等待alert窗口出现并确定
    def alert_accept(self):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present()).accept()


    # 通过遍历窗口方式切入新窗口
    def switch_newWindow(self,handle1,all_handles):
        for handle in all_handles:
            if handle != handle1:
                self.driver.switch_to.window(handle)

    #批改退保申请
    def piGaiTuiBaoShenQing(self,baodanhao):
        win32api.keybd_event(VK_CODE['win'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['m'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['m'], 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(VK_CODE['win'], 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(2)
        self.driver = webdriver.Ie()
        self.driver.get("http://10.130.201.229:7011/index.jsp")
        self.driver.maximize_window()
        self.send_by_css_selector('#username','manager@upic')
        self.send_by_css_selector('#password','upic@123')
        self.click_by_css_selector('#bt_submit')
        sleep(2)
        self.driver.switch_to_frame('leftFrame')
        self.click_by_link_text('承保子系统')
        self.click_by_link_text('批改管理')
        self.click_by_link_text('批改申请处理')
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('mainFrame')
        self.send_by_css_selector('input[name="PolicyNo"]',baodanhao)
        self.click_by_css_selector('input[value="下一步"]')
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('mainFrame')
        sleep(1)
        Select(self.driver.find_element_by_name('endorType')).select_by_index(1)
        self.send_use_js_by_namesAndIndex('GuEndorHeadValidDate', 0, '2018-05-01')
        sleep(1)
        self.click_by_css_selector('input[value=">>"]')
        self.click_by_css_selector('input[value="下一步"]')
        sleep(1)
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('mainFrame')
        self.click_by_css_selector('input[value="下一步(N)"]')
        self.send_by_css_selector("textarea[name='GuEndorTextEndorseTextByInput']",'同意')
        self.send_by_css_selector("input[name='adjustmentFeePayeeBankAccountName']",'张建歌')
        self.send_by_css_selector("input[name='adjustmentFeeAccountNo']",'11223344')
        self.send_use_js_by_namesAndIndex('adjustmentFeePayeeBankProvinceCode',0,'110000')
        self.send_use_js_by_namesAndIndex('adjustmentFeePayeeBankProvince',0,'北京市')
        self.send_use_js_by_namesAndIndex('adjustmentFeePayeeBankCityCode',0,'110100')
        self.send_use_js_by_namesAndIndex('adjustmentFeePayeeBankCity',0,'市辖区')
        self.send_use_js_by_namesAndIndex('adjustmentFeePayeeBankCode',0,'102')
        self.send_use_js_by_namesAndIndex('adjustmentFeeBankCode',0,'中国工商银行')
        self.send_use_js_by_namesAndIndex('adjustmentFeeBankBranchCode',0,'102100000021')
        self.send_use_js_by_namesAndIndex('adjustmentFeeBankBranchName',0,'中国工商银行股份有限公司北京通州支行新华分理处')
        self.send_use_js_by_namesAndIndex('adjustmentFeePayeeBankName',0,'中国工商银行')
        # self.DoublieClickByNamesAndIndex("adjustmentFeePayeeBankProvinceCode", 0)
        # sleep(1)
        # self.DoublieClickByNamesAndIndex("adjustmentFeePayeeBankCityCode", 0)
        # sleep(1)
        # self.DoublieClickByNamesAndIndex("adjustmentFeePayeeBankCode", 0)
        # sleep(1)
        # self.DoublieClickByNamesAndIndex("adjustmentFeeBankBranchCode", 0)
        # sleep(1)
        self.click_by_css_selector('input[value="提交核保"]')
        #self.driver.switch_to_alert().accept()
        sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('mainFrame')
        getText = self.getTextByCss("td[align='center']")
        print("保单号:"+baodanhao+getText)
        pattern = '\d*\d'
        pdsqh = re.search(pattern, getText).group()
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('topFrame')
        self.ClickByClassName("right_02")
        sleep(2)
        self.driver.quit()
        return pdsqh

    #批改退保申请审核确认
    def tuiBaoShenQingQueRen(self, pdsqh):
        win32api.keybd_event(VK_CODE['win'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['m'], 0, 0, 0)
        win32api.keybd_event(VK_CODE['m'], 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(VK_CODE['win'], 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(2)
        self.driver = webdriver.Ie()
        self.driver.get("http://10.130.201.229:7011/index.jsp")
        self.driver.maximize_window()
        self.send_by_css_selector('#username','hebao1@upic.com')
        self.send_by_css_selector('#password','upic@123')
        self.click_by_css_selector('#bt_submit')
        sleep(2)
        self.driver.switch_to_frame('leftFrame')
        self.click_by_link_text('审核平台子系统')
        self.click_by_link_text('核保审核')
        self.click_by_link_text('任务处理')
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('mainFrame')
        self.send_by_css_selector("input[name='GwWfLogDtoBusinessNo']",pdsqh)
        self.click_by_css_selector("input[name='buttonQuery']")
        self.driver.switch_to_frame('QueryResultFrame')
        sleep(1)
        handle1=self.driver.current_window_handle
        self.click_by_css_selector("a[href='#']")
        all_handles=self.driver.window_handles
        self.switch_newWindow(handle1,all_handles)
        self.driver.close()
        self.driver.switch_to_window(handle1)
        self.driver.switch_to_frame('mainFrame')
        self.driver.switch_to_frame('myFrame')
        self.send_by_css_selector('textarea[name="HandleText"]',"同意")
        Select(self.driver.find_element_by_name('NotionContent')).select_by_index(2)
        self.click_by_css_selector("input[name='butViewTranceInfo']")
        all_handles2=self.driver.window_handles
        self.switch_newWindow(handle1,all_handles2)
        self.driver.close()
        self.driver.switch_to_window(handle1)
        self.driver.switch_to_frame('mainFrame')
        self.driver.switch_to_frame('myFrame')
        self.click_by_css_selector("input[name='passBtn']")
        sleep(2)
        self.driver.switch_to_alert().accept()
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame('mainFrame')
        pdsqh = self.getTextByCss("td[class='tishi']")
        print(pdsqh)
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('topFrame')
        self.ClickByClassName("right_02")
        sleep(2)
        self.driver.quit()



    def run(self):
        bdh_list=self.getDataFromSheet(r'D:\JettechAgent1.6.0\baodanhao.xls',"Sheet1")
        for i in data:
            try:
                pdsqh= self.piGaiTuiBaoShenQing(i)
                self.tuiBaoShenQingQueRen(pdsqh)
            except:
                print("保单:%s has error" % i)
                self.driver.quit()


if __name__ == '__main__':
    functionLibrary = Procedure()
    functionLibrary.run()





