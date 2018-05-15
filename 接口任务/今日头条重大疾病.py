from selenium import webdriver
from time import sleep
import xlrd
from xlutils.copy import copy
import random
import time
import json


excelPath = r'E:\武郁博\今日头条重大疾病\今日头条重大疾病数据.xls'
sheetName = "SheetA"
url = 'http://ecuat.tk.cn/tkcoop/1029_policy.jsp'

jsonData = {
    "serialno": "111221111aaa123aa11111009",
    "applicantList": [
        {
            "identifyNumber": "440184198009121708",
            "identifyType": "01",
            "name": "小明",
            "mobile": "18346660318",
            "birthday": "1980-09-12",
            "mail": "751240877@qq.com",
            "sex": "2",
        }
        ],
    "insuredList": [
        {
            "identifyNumber": "440184198009121708",
            "identifyType": "01",
            "name": "小明",
            "birthday": "1980-09-12",
            "sex": "2",
            "mobile": "18346660318",
            "relatedperson": "01",
            "mail": "751240877@qq.com",
        }
        ],
"kindList": [
        {
            "kindCode": "1029001",
            "amount": "2500",
        }
        ],

"issueDate": "2018-04-01 15:25:50",
    "fromId": "64773",
 "premium": "2.01",
 "amount": "2500",
    "businessChannel": "02",
    "comboId": "1029A00001"
}


class touTiao:

    #从数据表中读取(案例数据)每行数据
    def getDataFromSheet(self):
        self.rowList = []
        # 读取excel数据
        data = xlrd.open_workbook(excelPath)
        # 获取一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取工作表的总行数
        nrows = table.nrows
        if nrows:
            for line in range(nrows):
                rowData = table.row_values(line)
                if rowData[27] == '':
                    self.rowList.append(rowData)
                    wb = copy(data)
                    ws = wb.get_sheet(0)
                    ws.write(line, 27, time.ctime())
                    wb.save(excelPath)
                    break
            return self.rowList[0]
        else:
            print("读取数据完毕！")

    #返回结果写入数据表
    def write_to_excell(self,col,return_info):
        data = xlrd.open_workbook(excelPath)
        # 获取一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取工作表的总行数
        nrows = table.nrows
        for line in range(nrows):
            rowData = table.row_values(line)
            if rowData[26] == '':
                wb = copy(data)
                ws = wb.get_sheet(0)
                ws.write(line, col, return_info)
                wb.save(excelPath)
                break

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



    #初始化报文
    def confJson(self,rowList):
        #投保人
        jsonData['serialno']=self.random_num(26)
        jsonData['applicantList'][0]['identifyNumber']=rowList[3]
        jsonData['applicantList'][0]['identifyType']=rowList[2]
        jsonData['applicantList'][0]['name']=rowList[1]
        jsonData['applicantList'][0]['mobile']=rowList[5]
        jsonData['applicantList'][0]['birthday']=rowList[4]
        jsonData['applicantList'][0]['mail']=rowList[6]
        jsonData['applicantList'][0]['sex']=rowList[7]
        #被保人
        jsonData['insuredList'][0]['identifyNumber']=rowList[11]
        jsonData['insuredList'][0]['identifyType']=rowList[10]
        jsonData['insuredList'][0]['name']=rowList[9]
        jsonData['insuredList'][0]['mobile']=rowList[13]
        jsonData['insuredList'][0]['birthday']=rowList[12]
        jsonData['insuredList'][0]['mail']=rowList[14]
        jsonData['insuredList'][0]['sex']=rowList[15]
        #险种信息
        jsonData['kindList'][0]['kindCode'] = rowList[17]
        jsonData['kindList'][0]['amount'] = rowList[19]
        jsonData['issueDate']=rowList[18]
        jsonData['fromId']=rowList[21]
        jsonData['premium']=rowList[20]
        jsonData['amount']=rowList[19]
        jsonData['businessChannel']=rowList[22]
        jsonData['comboId']=rowList[23]

        return jsonData

    #发送报文
    def sendJson(self):
        str_json=json.dumps(jsonData,ensure_ascii=False)
        print("发送报文：%s" % str_json)
        #保存发送报文到txt文件
        self.write_txt('E:\武郁博\今日头条重大疾病\收发报文\%s_send.txt' %self.rowList[0][0],str_json)
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_css_selector('textarea[name="content"]').send_keys(str_json)
        sleep(2)
        self.driver.find_element_by_css_selector('input[value="提交"]').click()
        sleep(2)
        #获取返回信息
        return_info=self.driver.find_element_by_css_selector('textarea[name="aaaa"]').text
        print("返回报文：%s" %return_info)
        #保存返回报文到txt文件
        self.write_txt('E:\武郁博\今日头条重大疾病\收发报文\%s_received.txt' % self.rowList[0][0], return_info)
        return_json=json.loads(return_info)
        if return_json['code'] == '200':
            self.write_to_excell(26,return_json['policyNo'])
        else:
            self.write_to_excell(26,return_json['msg'])
        self.driver.quit()

    def run(self):
        for i in range(1):
            rowList = self.getDataFromSheet()
            self.confJson(rowList)
            self.sendJson()


if __name__ == '__main__':
   functionLibrary=touTiao()
   functionLibrary.run()
