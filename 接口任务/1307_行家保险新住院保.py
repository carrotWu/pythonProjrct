from selenium import webdriver
from time import sleep
import xlrd
from xlutils.copy import copy
import random
import time
import json
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

time_out=30 #EC超时时间
excelPath = r'E:\武郁博\1307_行家保险新住院保\1307_行家保险新住院保.xls'
sheetName = "SheetA"
TB_url = 'http://ecuat.tk.cn/tkcoop/xgninsure.jsp'
CD_url = 'http://ecuat.tk.cn/tkcoop/xgninsure_policy.jsp'

start = 15  #起始行
end = 17    #结束行

return_code_col = 32           #报文返回码在excell中存储列数
return_PolicyNumMsg_col = 34   #保单号或者报错信息在excell中存储列数


TB_json = {
    "serialno": "11122aas11asdf40000006",
    "applicantList": [{
            "identifyNumber": "350503198812170025",
            "identifyType": "01",
            "name": "小明",
            "mobile": "18346660318",
            "birthday": "1988-12-17",
            "mail": "751240877@qq.com",
            "sex": "2"
            }],
    "insuredList": [{
            "identifyNumber": "350503198812170025",
            "identifyType": "01",
            "name": "小明",
            "mobile": "18346660318",
            "birthday": "1988-12-17",
            "sex": "2",
            "relatedperson": "01",
            "mail": "751240877@qq.com",
            "career": "00101001"
            }],
    "kindList":
        [
        {
            "amount": "100000",
            "kindCode": "1122031"
        },
        {
            "amount": "10000",
            "kindCode": "1122032"
        },
        {
            "amount": "20000",
            "kindCode": "100019"
        }
    ],
    "issueDate": "2018-3-27 15:25:50",
    "comboId": "1307A02401",
    "fromId": "60085",
    "premium": "249",
    "amount": "130000",
    "renewalFlag": "0",
    "careerAll": "00101001-国家机关、党政团体单位负责人（不从事风险工作）"
}

#未成年人
# "career": "02001006"
# "careerAll": "02001006-自由职业人员"

CD_json={
    "serialno": "1112as11aaasdf111aa1",
    "proposalNo": "001021109201717228052163436",
    "payMoney": "374",
    "comboId": "1307A02401",
    "fromId": "60085  ",
    "payTime": "2018-03-27 15:58:00",
    "payAccount": "7512489612@qq.com",
    "outTradeId": "54555555555555555555"
}



class Production:

    #从数据表中读取案例数据(start-end行)
    def getDataFromSheet(self):
        self.start = start
        self.end = end
        self.rowList = []
        # 读取excel数据
        data = xlrd.open_workbook(excelPath)
        # 获取一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取工作表的总行数
        nrows = table.nrows
        if nrows:
            for line in range(self.start,self.end):
                rowData = table.row_values(line)
                self.rowList.append(rowData)
                # wb = copy(data)
                # ws = wb.get_sheet(0)
                # ws.write(line, 32, time.ctime())
                # wb.save(excelPath)
            return self.rowList
        else:
            print("读取数据完毕！")

    #返回结果写入数据表
    def write_to_excell(self,row, col, content):
        data = xlrd.open_workbook(excelPath)
        wb = copy(data)
        ws = wb.get_sheet(0)
        ws.write(row, col, content)
        wb.save(excelPath)

    #读取TXT文件
    def read_txt(self,f_name):
        with open(f_name,'r',encoding='utf8') as f_obj:
            mess_txt = f_obj.read()
        return mess_txt

    # 写入TXT文件
    def write_txt(self, f_name, content):
        # if not os.path.exists(f_name):
        #     os.makedirs(f_name)
        with open(f_name, 'w', encoding='utf8') as f_obj:
            f_obj.write(content)


    #生成随机数
    def random_num(self,count):
        count = int(count)
        s = '0123456789'
        r = ''
        while count > 0:
            r += random.choice(s)
            count -= 1
        return r

    #身份证号，生成器
    def id_card_mum(self,birth, sex=1):
        # 生成身份证号1991-01-01
        birth = str(birth)
        year = birth[0:4]
        month = birth[5:7]
        day = birth[8:]
        # print(year)
        # print(month)
        # print(day)
        # print(birth)
        cid_list = ['110101', '110102', '110105', '110106', '110107', '110108', '110109', '110111', '110112', '110113',
                    '110114', '110115', \
                    '110116', '110117', '110228', '110229', '120106', '120107', '120108', '120109', '120110', '120111',
                    '120112', '120113', '120114', '120115', \
                    '120200', '120221', '120223', '120225', '130100', '130101', '130104', '130105', '130107', '130108',
                    '130121', '130123', '130124', '130125', \
                    '140100', '140105', '140106', '140107', '140108', '140109', '140110', '140121', '140122', '140123',
                    '140181', '140200', '140202', '140203', \
                    '320100', '320102', '320104', '320105', '320106', '320111', '320113', '320114', '320115', '320116',
                    '320124', '320125', '320200', '320202']
        last = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
        cid = random.choice(cid_list) + str(year) + str(month).zfill(2) + str(day).zfill(2) + str(
            random.randrange(int(sex), 999, 2)).zfill(3)
        # 计算校验码
        sum_mum = int(cid[0]) * 7 + int(cid[1]) * 9 + int(cid[2]) * 10 + int(cid[3]) * 5 + int(cid[4]) * 8 + int(
            cid[5]) * 4 + int(cid[6]) * 2 + int(cid[7]) * 1 \
                  + int(cid[8]) * 6 + int(cid[9]) * 3 + int(cid[10]) * 7 + int(cid[11]) * 9 + int(cid[12]) * 10 + int(
            cid[13]) * 5 + int(cid[14]) * 8 + int(cid[15]) * 4 + int(cid[16]) * 2
        cid = cid + last[sum_mum % 11]
        return cid

    # 计算出生日期
    def calculate_birthday(start_date, age, days):
        if age == '' or days == '':
            return ''
        year = str(int(start_date[:4]) - int(age))
        my_date = year + start_date[4:]
        d = datetime.datetime.strptime(my_date, '%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=int(days))
        date_delta = d + delta
        return date_delta.strftime('%Y-%m-%d')
    # birthday = calculate_birthday('2018-02-09 00:00:00','3',"-1")

    # 通过css填写内容
    def send_by_css_selector(self, css, content):
        WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css))).send_keys(content)

    # 通过css单击
    def click_by_css_selector(self, css):
        WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css))).click()

    #通过css获取标签内容
    def get_tex_by_Css(self,css):
        return WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css))).text

    def gsds(self):
        WebDriverWait(self.driver, time_out).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'mainFrame')))#等待frame可切入
        self.driver.switch_to_frame('mainFrame')
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())#等待allert窗口出现
        self.driver.switch_to_alert().accept()

    #初始化投保报文
    def confTB_json(self,rowList):
        #取值
        self.caseNo = rowList[0]
        self.t_name = rowList[1]
        self.t_identifyType = rowList[2]
        self.t_identifyNumber = rowList[3]
        self.t_birthday = rowList[4]
        self.t_mobile = rowList[5]
        self.t_mail = rowList[6]
        self.t_sex = rowList[7]
        self.b_name = rowList[9]
        self.b_identifyType = rowList[10]
        self.b_identifyNumber = rowList[11]
        self.b_birthday = rowList[12]
        self.b_mobile = rowList[13]
        self.b_mail = rowList[14]
        self.b_sex = rowList[15]
        self.b_relatedPerson = rowList[16]
        self.issueDate = rowList[17]
        self.amount1 = rowList[18]
        self.kindCode1 = rowList[19]
        self.amount2 = rowList[20]
        self.kindCode2 = rowList[21]
        self.amount3 = rowList[22]
        self.kindCode3 = rowList[23]
        self.amount = rowList[24]
        self.premium = rowList[25]
        self.comboId = rowList[26]
        self.fromId = rowList[27]
        self.career = rowList[28]
        self.renewalFlag = rowList[29]
        self.careerAll = rowList[30]

        #赋值
        ###投保人
        TB_json['serialno'] = self.random_num(26)
        TB_json['applicantList'][0]['name'] = self.t_name
        TB_json['applicantList'][0]['identifyType'] = self.t_identifyType
        #判断是否生成投保人身份证号
        if self.t_identifyType == "01" and self.t_identifyNumber == '' :
            TB_json['applicantList'][0]['identifyNumber'] = self.id_card_mum(self.t_birthday, self.t_sex)

        #判断是否生成护照号
        if self.t_identifyType == '02' and self.t_identifyNumber == '' :
            TB_json['applicantList'][0]['identifyNumber'] = self.random_num(10)

        TB_json['applicantList'][0]['mobile'] = self.t_mobile
        TB_json['applicantList'][0]['birthday'] = self.t_birthday
        TB_json['applicantList'][0]['mail'] = self.t_mail
        TB_json['applicantList'][0]['sex'] = self.t_sex

        ###被保人
        TB_json['insuredList'][0]['name'] = self.b_name
        TB_json['insuredList'][0]['identifyType'] = self.b_identifyType
        # 判断是否为同一人。是：引用投保人身份证，否：生成新身份证
        if self.b_identifyNumber == "" and self.b_relatedPerson == '01':
            TB_json['insuredList'][0]['identifyNumber'] = TB_json['applicantList'][0]['identifyNumber']
        if self.b_identifyNumber == "" and self.b_relatedPerson != '01':
            TB_json['insuredList'][0]['identifyNumber'] = self.id_card_mum(self.b_birthday,self.b_sex)

        # 判断是否生成护照号
        if self.b_identifyType == '02' and self.b_identifyNumber == '':
            TB_json['insuredList'][0]['identifyNumber'] = self.random_num(10)

        TB_json['insuredList'][0]['mobile'] = self.b_mobile
        TB_json['insuredList'][0]['birthday'] = self.b_birthday
        TB_json['insuredList'][0]['mail'] = self.b_mail
        TB_json['insuredList'][0]['sex'] = self.b_sex
        TB_json['insuredList'][0]['relatedperson'] = self.b_relatedPerson
        TB_json['insuredList'][0]['career'] = self.career

        ###险种信息
        TB_json['kindList'][0]['kindCode'] = self.kindCode1
        TB_json['kindList'][0]['amount'] = self.amount1
        TB_json['kindList'][1]['kindCode'] = self.kindCode2
        TB_json['kindList'][1]['amount'] = self.amount2
        TB_json['kindList'][2]['kindCode'] = self.kindCode3
        TB_json['kindList'][2]['amount'] = self.amount3

        ###扩展字段
        TB_json['issueDate'] = self.issueDate
        TB_json['comboId'] = self.comboId
        TB_json['fromId'] = self.fromId
        TB_json['premium'] = self.premium
        TB_json['amount'] = self.amount
        TB_json['renewalFlag'] = self.renewalFlag
        TB_json['careerAll'] = self.careerAll

        return TB_json


    #发送投保报文
    def sendTB_json(self):
        #row 返回信息写入数据表所需的行序号
        str_json=json.dumps(TB_json,ensure_ascii=False)
        print("投保报文：%s" % str_json)
        #保存发送报文到txt文件
        self.write_txt(r'E:\武郁博\1307_行家保险新住院保\收发报文\%s_sen1.txt' %self.caseNo,str_json)
        self.driver=webdriver.Chrome()
        self.driver.get(TB_url)
        self.driver.maximize_window()
        self.send_by_css_selector('textarea[name="content"]',str_json)
        self.click_by_css_selector('input[value="提交"]')
        #获取返回信息
        return_info=self.get_tex_by_Css('textarea[name="aaaa"]')
        print("投保返回报文：%s" %return_info)
        #保存返回报文到txt文件
        self.write_txt(r'E:\武郁博\1307_行家保险新住院保\收发报文\%s_rec1.txt' % self.caseNo, return_info)
        return_json=json.loads(return_info)
        self.TB_RecCode = return_json['code']
        if self.TB_RecCode == '200':
            self.proposalNo = return_json['result']['proposalNo']
            # self.write_to_excell(33, '200')
            # self.write_to_excell(35,return_json['policyNo'])
        else:
            self.write_to_excell(self.start,return_code_col, return_json['code'])
            self.write_to_excell(self.start,return_PolicyNumMsg_col, return_json['msg'])
        self.driver.quit()


    #初始化出单报文
    def confCD_json(self):
        CD_json['serialno'] = TB_json['serialno']
        CD_json['proposalNo'] = self.proposalNo
        CD_json['payMoney'] = self.premium
        CD_json['comboId'] = self.comboId
        CD_json['fromId'] = self.fromId

    #发送出单报文
    def send_CD_json(self):
        # row 返回信息写入数据表所需的行序号
        str_json = json.dumps(CD_json, ensure_ascii=False)
        print("出单报文：%s" % str_json)
        # 保存出单报文到txt文件
        self.write_txt(r'E:\武郁博\1307_行家保险新住院保\收发报文\%s_sen2.txt' % self.caseNo, str_json)
        self.driver = webdriver.Chrome()
        self.driver.get(CD_url)
        self.driver.maximize_window()
        self.send_by_css_selector('textarea[name="content"]', str_json)
        self.click_by_css_selector('input[value="提交"]')
        # 获取返回信息
        return_info = self.get_tex_by_Css('textarea[name="aaaa"]')
        print("出单返回报文：%s" % return_info)
        # 保存返回报文到txt文件
        self.write_txt(r'E:\武郁博\1307_行家保险新住院保\收发报文\%s_rec2.txt' % self.caseNo, return_info)
        return_json = json.loads(return_info)
        if return_json['code'] == '200':
            self.write_to_excell(self.start,return_code_col, '200')
            self.write_to_excell(self.start,return_PolicyNumMsg_col,return_json['result']['policyNo'])
        else:
            self.write_to_excell(self.start,return_code_col, return_json['code'])
            self.write_to_excell(self.start,return_PolicyNumMsg_col, return_json['msg'])
        self.driver.quit()



    def run(self):

        rowList = self.getDataFromSheet()
        try :
            for i in rowList :
                # print(i)
                self.confTB_json(i)
                self.sendTB_json()
                if self.TB_RecCode == '200' :
                    self.confCD_json()
                    self.send_CD_json()
                self.start += 1
        except :
            self.driver.quit()



if __name__ == '__main__':
   functionLibrary=Production()
   functionLibrary.run()
