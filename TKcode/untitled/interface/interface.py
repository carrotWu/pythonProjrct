from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlutils.copy
import xlrd
from time import sleep
import cx_Oracle
import os
import random



data = '''
    <Header>
        <TRAN_CODE>100083</TRAN_CODE>
        <BANK_CODE>9906</BANK_CODE>
        <BRNO>99060000</BRNO>
        <TELLERNO/>
        <BK_ACCT_DATE>20171212</BK_ACCT_DATE>
        <BK_ACCT_TIME>17:00:38</BK_ACCT_TIME>
        <BK_SERIAL>jtlb_405321010</BK_SERIAL>
        <BK_TRAN_CHNL>WEB</BK_TRAN_CHNL>
        <REGION_CODE>000000</REGION_CODE>
        <BRANCH_CODE>151</BRANCH_CODE>
    </Header>
    <Request>
        <ahsPolicy>
            <policyBaseInfo>
                <createdBy>jiangtai</createdBy>
                <applyPersonnelNum>5</applyPersonnelNum>
                <relationshipWithInsured>7</relationshipWithInsured>
                <totalModalPremium>50</totalModalPremium>
                <currecyCode>01</currecyCode>
                <insuranceBeginTime>2017-12-13 00:00:00</insuranceBeginTime>
                <insuranceEndTime>2017-12-14 00:00:00</insuranceEndTime>
                <businessType>2</businessType>
                <applyDay>2</applyDay>
            </policyBaseInfo>
            <policyExtendInfo>
                <partnerSystemSeriesNo>2017121214593561264</partnerSystemSeriesNo>
            </policyExtendInfo>
           <insuranceApplicantInfo>
              <groupPersonnelInfo>
                    <groupName>江泰</groupName>
		    <groupCertificateType>05</groupCertificateType>
		    <groupCertificateNo>1234567</groupCertificateNo>
		    <groupLinkManName>张成</groupLinkManName>
		    <groupLinkManMobile>13045678935</groupLinkManMobile>
              </groupPersonnelInfo>
            </insuranceApplicantInfo>
            <subjectInfo>
                <subjectInfo>
                    <productInfo>
                        <productInfo>
                            <productCode>1110A00101</productCode>
                        </productInfo>
                    </productInfo>
                    <planInfo />
                    <insurantInfo>
                        <insurantInfo>
                            <personnelName>被保人姓名</personnelName>
                            <sexCode>M</sexCode>
                            <certificateType>01</certificateType>
                            <certificateNo>445101192611215842</certificateNo>
                            <birthday>1926-11-21</birthday>
                            <groupName>jt</groupName>
                        </insurantInfo>
                    </insurantInfo>
                </subjectInfo>
            </subjectInfo>
        </ahsPolicy>
    </Request>
</eaiAhsXml>
    '''






class TKInterface():

    #身份证号，生成器
    def id_card_mum(self,birth,sex=1):
        #生成身份证号1991-01-01
        birth = str(birth)
        year = birth[0:4]
        month = birth[5:7]
        day = birth[8:]
        cid_list = ['110101', '110102', '110105', '110106', '110107', '110108', '110109', '110111', '110112', '110113', '110114', '110115',\
        '110116', '110117', '110228', '110229', '120106', '120107', '120108', '120109', '120110', '120111', '120112', '120113', '120114', '120115', \
        '120200', '120221', '120223', '120225', '130100', '130101', '130104', '130105', '130107', '130108', '130121', '130123', '130124', '130125', \
        '140100', '140105', '140106', '140107', '140108', '140109', '140110', '140121', '140122', '140123', '140181', '140200', '140202', '140203', \
        '320100', '320102', '320104', '320105', '320106', '320111', '320113', '320114', '320115', '320116', '320124', '320125', '320200', '320202']
        last = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
        cid = random.choice(cid_list) + str(year) + str(month).zfill(2) + str(day).zfill(2) + str(random.randrange(int(sex),999,2)).zfill(3)
        #计算校验码
        sum_mum = int(cid[0])*7 + int(cid[1])*9 + int(cid[2])*10 + int(cid[3])*5 + int(cid[4])*8 + int(cid[5])*4 + int(cid[6])*2+int(cid[7])*1 \
        + int(cid[8])*6 + int(cid[9])*3 + int(cid[10])*7 + int(cid[11])*9 + int(cid[12])*10 + int(cid[13])*5 + int(cid[14])*8 + int(cid[15])*4 + int(cid[16])*2
        cid = cid + last[sum_mum%11]
        return cid
    #启动浏览器
    def open_chrome(self,url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)

    def close_browser(self):
        self.driver.close()


    #--------------------------点击----------------------
    #id点击操作
    def click_by_id(self,ele_id):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,ele_id)))
        element.click()

    #name点击
    def click_by_name(self,name):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.NAME,name)))
        element.click()

    #xpath点击
    def click_by_xpath(self,xpath):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        element.click()

    #css点击
    def click_by_css(self,css_selector):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css_selector)))
        element.click()
    #--------------------------发送----------------------

    #id 发送
    def send_keys_by_id(self,ele_id,content):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,ele_id)))
        element.clear()
        element.send_keys(content)

    #name 发送
    def send_keys_by_name(self,name,content):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.NAME,name)))
        element.clear()
        element.send_keys(content)

    #xpath 发送
    def send_keys_by_xpath(self,xpath,content):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        element.clear()
        element.send_keys(content)

    #css 发送
    def send_keys_by_css(self,css_selector,content):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css_selector)))
        element.clear()
        element.send_keys(content)

    #通过js输入
    def set_value_useJS_id(self,ele_id,content):
        js = 'var q=document.getElementById("%s");q.value = "%s"'%(ele_id,content)
        self.driver.execute_script(js)

    #-------------------------------文件操作-----------------------------------
    #打开excel文件
    def open_excel(self,f_name):
        self.workbook = xlrd.open_workbook(f_name)
        self.wb = xlutils.copy.copy(self.workbook)
    #保存excel文件
    def save_excel(self,f_name):
        self.wb.save(f_name)
        self.workbook.release_resources()
    #读取excel数据
    def read_data_by_coordinate(self,sheet_name,row,col):
        return self.workbook.sheet_by_name(sheet_name).cell(int(row),int(col)).value
    #写入excel数据
    def write_data_by_coordinate(self,sheet_name,row,col,content):
        ws = self.wb.get_sheet(self.workbook.sheet_names().index(sheet_name))
        ws.write(int(row),int(col),content)


    #读取TXT文件
    def read_txt(self,f_name):
        with open(f_name,'r',encoding='gbk') as f_obj:
            mess_txt = f_obj.read()
        return mess_txt
    #写入TXT文件
    def write_txt(self,f_name):
        if not os.path.exists(f_name):
            os.makedirs(f_name)
        with open(f_name,'w',encoding='gbk') as f_obj:
            f_obj.write(f_name)

    #-------------------------数据库操作----------------------
    #连接数据库
    def connect_oracle(self,u_name,p_word,url):
        try:
            self.conn = cx_Oracle.connect(u_name,p_word,url)
            self.rs = self.conn.cursor()
        except Exception as e:
            #出现异常后关闭连接
            self.close_oracle()
            print(e)
    #关闭数据库
    def close_oracle(self):
        if self.rs != None:
            self.rs.close()
        if self.conn != None:
            self.conn.close()

    #查询数据库
    def find_data(self,sql):
        try:
            self.rs.excute(sql)
            res = self.rs.fetchall()
            return res
        except Exception as e:
            self.close_oracle()
            print(e)
    #更新数据库
    def update_oracle(self,sql):
        try:
            self.rs.excute(sql)
            self.conn.commit()
        except Exception as e:
            self.close_oracle()
            print(e)

    #-------------------------报文整理----------------------------


if __name__ == "__main__":
    tki = TKInterface()
    tki.open_chrome('http://ecuat.taikang.com/tkcoop_20171102/insurejt.jsp')
    #读取报文
    mess = tki.read_txt('D:/JettechAgent1.6.0/conf/testData/江泰北分旅出单.txt')
    print(mess)
    # tki.send_keys_by_name('jsons',mess)
    tki.driver.find_element_by_xpath('html/body/form/textarea').send_keys(data)
    # tki.send_keys_by_xpath('html/body/form/textarea',mess)
    # tki.close_browser()























