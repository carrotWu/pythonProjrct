import os
import sys
import logging
import requests
import hashlib
import random
from time import time
import datetime
import json
import cx_Oracle

class scriptError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Interface(object):
    def __init__(self):
        self.projectPath = "D:\\JettechAgent1.6.0\\execute\\"
        # self.params = params
        self.logConfig()

    #资源路径分隔符替换
    def urlReplace(self,path):
        return path.replace('\\',r'\\')

    #配置logger
    def logConfig(self):
        logger = logging.getLogger('pyLogging')
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.urlReplace(self.projectPath) + 'ProcessLog.txt')
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        self.loginfo = logger

    def log(self, msg):
        self.loginfo.info(msg)

    #-------------------------数据库操作----------------------
    #连接数据库
    def connect_oracle(self,u_name,p_word,url):
        try:
            self.conn = cx_Oracle.connect(u_name,p_word,url)
            self.rs = self.conn.cursor()
        except Exception:
            #出现异常后关闭连接
            self.close_oracle()
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')
    #关闭数据库
    def close_oracle(self):
        if self.rs != None:
            self.rs.close()
        if self.conn != None:
            self.conn.close()

    #查询数据库
    def find_data(self,sql):
        try:
            self.rs.execute(sql)
            res = self.rs.fetchall()
            return res[0]
        except Exception:
            self.close_oracle()
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')
    #更新数据库
    def update_oracle(self,sql):
        try:
            self.rs.execute(sql)
            self.conn.commit()
        except Exception:
            self.close_oracle()
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')

    def compare_ab(self,a,b):
        a = float(a)
        b = float(b)
        if a == b:
            return str(a) + '相等' + str(b)
        else:
            return str(a) + '不等' + str(b)


    #数据池存储数据方法
    def mem(self, memKey, memValue):
        contentMap = {}
        fileName = self.urlReplace(self.projectPath) + '/tempData.txt'
        try:
            if not os.path.exists(fileName):
                self.getFile(fileName, 'wt+')
            file = self.getFile(fileName, 'rt+')
            lines = file.readlines()
            for line in lines:
                key_value = line.strip().split("$-----$")
                contentMap[key_value[0]] = key_value[1]
            if memKey in contentMap:
                del contentMap[memKey]
            file.close()
            if os.path.exists(fileName):
                os.remove(fileName)
            contentMap[memKey] = memValue
            file = self.getFile(fileName, 'wt+')
            for key in contentMap.keys():
                file.write(key + '$-----$' + contentMap[key] + '\n')
            file.close()
        except Exception:
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----' + memKey + '--' + memValue + '----异常')

    #获取文件句柄
    def getFile(self, filePath, handle):
        try:
            file = open(filePath, mode=handle,
                    buffering=1, encoding='gbk', errors=None,
                    newline='\r\n', closefd=True, opener=None)
            return file
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #md5加密
    def encry_md5(self,body,key_md5):
        try:
            content = key_md5 + body
            m = hashlib.md5()
            m.update(content.encode('utf-8'))
            return m.hexdigest()
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #计算验签
    def generate_sign(self):
        try:
            return self.encry_md5(json.dumps(self.send_json('apply_content')),'1234567890ABCDEF')
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #身份证号，生成器
    def id_card_mum(self,birth,sex=1):
        try:
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
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #时间戳
    def time_stamp(self):
        try:
            return str(int(time() * 1000))
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #计算出生日期
    def calculate_birthday(self,start_date,age,days):
        try:
            if age == '' or days == '':
                return ''
            year = str(int(start_date[:4]) - int(age))
            my_date = year + start_date[4:]
            d = datetime.datetime.strptime(my_date,'%Y-%m-%d %H:%M:%S')
            delta = datetime.timedelta(days = int(days))
            date_delta = d + delta
            return date_delta.strftime('%Y-%m-%d')
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #随机字符
    def random_num_str(self):
        return '201712215' + str(random.randint(100,999)) + str(random.randint(100,999))


    #通过key取出value值,返回的是字符串类型，在武汉平台中用作md5加密的body（武汉平台的md5的key是：1234567890ABCDEF）
    def get_value_by_key(self,dic,key):
        try:
            apply_content = dic[key]
            return apply_content
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #发送报文
    def http_post(self,url,my_data):
        headers = {"Content-Type":"application/json;charset=utf-8","accept": "application/json","Accept-CharSet": "utf-8"}
        try:
            self.back_json = requests.post(url,json=my_data,headers=headers).json()
            return self.back_json
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #log发送报文
    def log_send_json(self):
        self.log('-----------发送报文------------')
        self.log(self.send_json)
    #接收报文
    def log_back_json(self):
        self.log('----------接收报文--------------')
        self.log(self.back_json)

    #初始化报文
    def json_conf(self):
        serial_no = self.random_num_str()
        sign = self.generate_sign()
        self.send_json['serial_no'] = serial_no
        self.send_json['sign'] = sign

    #报文拼接
    def json_File(self):
        self.send_json = {
        "coop_id": "hehuan_kbyz",
        "service_id": "01",
        "sign_type": "md5",
        "sign": "061f00a6715fd5c58baebb340a733493",
        "format": "json",
        "charset": "utf-8",
        "version": "1.0",
        "timestamp": "1459872000550",
        "serial_no": "2asd014444000010212",
        "product_type": "propertiesfour",
        "apply_content":
        {
        "holder_name": "小明",
        "holder_cid_type": "02",
        "holder_cid_number": "130825160311",
        "holder_mobile": "18346660318",
        "holder_email": "751240877@qq.com",
        "holder_birthday": "1960-01-16",
        "holder_sex": "1",
        "holder_insuredType": "1",
        "holder_insuredFlag": "1",
        "insurants_name": "小明",
        "insurants_cid_type": "02",
        "insurants_cid_number": "130825160311",
        "insurants_mobile": "18346660318",
        "insurants_birthday": "1960-01-16",
        "insurants_sex": "1",
        "insurants_insuredFlag": "2",
        "insurants_insuredType": "1",
        "relatedperson": "01",
        "issueDate": "2018-01-20 00:00:00",
        "startDate": "2018-01-20 00:00:00",
        "endDate": "2018-07-18 23:59:59",
        "amount": "60000",
        "premium": "499",
        "FieldAA": "1132A00601",
        "FieldAD": "0",
        "FieldBI": "医院名称",
        "FieldHO": "主刀医生姓名",
        "Office": "1",
        "FieldGZ": "骨科",
        "FieldGW": "手术或介入诊疗名称",
        "FieldGY": "2018-01-20",
        "comboId": "1132A00601",
        "salesmanCode": "S142011006",
        "channelTip": "1010106",
        "businessChannel": "05",
        "intermediarycode": "010000000000600220",
        "solutionCode": "0100000000006002200002",
        "fromId": "63368",
        "kindList":
            [
                    {
        "amount": "50000",
        "kindName": "泰康在线手术意外身故/伤残保险",
        "kindCode": "1132001"
                    },
			        {
        "amount": "10000",
        "kindName": "泰康在线手术意外并发症保险",
        "kindCode": "1132002"
                    }
                ]
            }
        }
        return self.send_json

    #执行过程的方法
    def run(self):
        # print(self.urlReplace(self.projectPath) + 'ProcessLog.txt')
        self.json_File()
        self.json_conf()
        self.log_send_json()
        #发送报文
        self.http_post('http://10.130.201.180:8080/tk-link/rest',self.send_json)
        self.log_back_json()
        print(self.back_json)
        #核保成功保存proposalNo
        self.mem('proposalNo',self.back_json['result_content']['proposalNo'])
        print(self.back_json['result_content']['proposalNo'])




if __name__ == '__main__':
    Interface().run()



