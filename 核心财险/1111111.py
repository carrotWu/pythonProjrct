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
    '06000031360361800000000028'
]

class Procedure:
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
        WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css))).send_keys(content)
    #通过js填写内容
    def send_use_js_by_namesAndIndex(self,names,index,content):
        js = 'var q=document.getElementsByName("%s");q[%d].value ="%s"' % (names, index, content)
        self.driver.execute_script(js)
    def ClickByClassName(self, className):
        '''
        根据classname点击
        '''
        el = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CLASS_NAME, className)))
        el.click()
    def getTextByCss(self, css):
        ele = WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        return ele.text

    # 通过遍历窗口方式切入新窗口
    def switch_newWindow(self,handle1,all_handles):
        for handle in all_handles:
            if handle != handle1:
                self.driver.switch_to.window(handle)


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
        self.send_by_css_selector("input[name='adjustmentFeePayeeBankAccountName']",'山东静静静有限责任公司')
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
        print(getText)
        pattern = '\d*\d'
        pdsqh = re.search(pattern, getText).group()
        sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to_frame('topFrame')
        self.ClickByClassName("right_02")
        sleep(2)
        self.driver.quit()
        return pdsqh

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
        for i in data:
            #try:
            pdsqh= self.piGaiTuiBaoShenQing(i)
            self.tuiBaoShenQingQueRen(pdsqh)
            #except:
                #print("%s has error" % i)
            # finally:
            #      self.driver.quit()




if __name__ == '__main__':
    functionLibrary = Procedure()
    functionLibrary.run()





