import os
import logging
import hashlib
from jpype import *
import json
import requests
from time import time
import random
import datetime
import cx_Oracle
startJVM(getDefaultJVMPath(),"-Xmx256m", "-Djava.class.path=D:\JettechAgent1.6.0\lib\\AESTool.jar")
JDClass = JClass("com.Demo")
encrypt_engie = JDClass()


class scriptError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Interface(object):
    # def __init__(self):
    #     self.projectPath = "D:\\JettechAgent1.6.0\\execute\\"
    #     self.logConfig()
    def __init__(self,channel_id):
        super(Interface,self).__init__()
        self.projectPath = "D:\\JettechAgent1.6.0\\execute\\"
        self.logConfig()
        self.check_url = 'http://10.130.202.171/api/validatePolicy'
        self.pay_url = 'http://10.130.202.171/api/pay'
        self.pay_callback_wechat = 'http://10.130.202.171/api/pay/weChatWapCallBack?channel_id='
        self.pay_callback_alipay = 'http://10.130.202.171/api/pay/aliPayWapCallBack?channel_id='
        self.invoice_url = 'http://10.130.202.171/api/policy'
        self.aes_key = "D21Uq65MzDF28PaEx7zO0dSM2WuG03z0"
        self.md5_key = "12344404K53N5571lz91673701u04321"
        self.channel_id = channel_id
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
            raise scriptError(str(a) + '不等' + str(b))


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

    # AES加密，需要传入字典类型的报文体
    def en_aes(self, scr_dic, aes_key):
        scr_str = json.dumps(scr_dic).replace(': ', ':')
        return encrypt_engie.encryptAES(scr_str, aes_key)

    # 需要传入加密字符串
    def de_aes(self, scr, aes_key):
        return encrypt_engie.decryptAES(scr, aes_key)

    #生成请求流水号
    def request_num(self):
        return '78966697798' + str(random.randint(1, 9999))

    #时间戳
    def time_stamp(self):
        try:
            return str(int(time() * 1000))
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #md5加密
    def encry_md5(self,send_json,key_md5):
        try:
            content = key_md5 + send_json
            m = hashlib.md5()
            m.update(content.encode('utf-8'))
            return m.hexdigest()
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')

    #计算验签
    def generate_sign(self):
        try:
            return self.encry_md5(json.dumps(self.send_json),'1234567890ABCDEF')
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

    #log发送报文
    def log_send_json(self):
        self.log('-----------发送报文------------')
        self.log(self.send_json)
    #log接收报文
    def log_back_json(self):
        self.log('----------接收报文--------------')
        self.log(self.back_json)
    #报文拼接
    def json_File(self):
        self.send_json = {
	"amount":"50000",
	"end_date":"2019-02-05 23:59:59",
	"insured":
        {

		"occupation_code":"0101003",
		"birthday":"1990-10-14",
		"sex":"1",
		"name":"张朝杰",
		"relation":"01",
		"certi_type":"01",
		"type":"1",
		"certi_no":"350128199010143113"
	}
   ,
	"product_id":"1013A00W01",
	"insure_date":"2018-02-02 10:00:00",
	"premium":"200",
	"applicant":
        {

		"birthday":"1990-10-14",
		"sex":"1",
		"phone":"13161084234",
		"certi_type":"01",
		"type":"1",
		"email":"adf@165.com",
		"certi_no":"350128199010143113",
		"name":"张朝杰"
	}
            ,

    "kind_list":
        [

		{
			"amount":"50000",
			"kind_code":"1013001",
			"premium":"200"
		},

		{
			"amount":"50000",
			"kind_code":"1013002",
			"premium":"200"
		}
            ,

		{
			"amount":"50000",
			"kind_code":"1013003",
			"premium":"200"
		}
        ]
            ,

	"start_date":"2018-02-06 00:00:00",
	"extend_params":
        {

		"FieldAE":"1",
		"FieldAC":"1"
	    }
        }
        return self.send_json
    #初始化报文
    def json_conf(self):
        serial_no = self.random_num_str()
        sign = self.generate_sign()
        self.send_json['serial_no'] = serial_no
        self.send_json['sign'] = sign
        t_id_cardNum=self.id_card_mum('2018-02-06',sex=1)
        b_id_cardNum=self.id_card_mum('2018-02-06',sex=1)
        t_birthday = self.calculate_birthday('2018-02-06 00:00:00', 't_y', 't_d')
        b_birthday = self.calculate_birthday('2018-02-06 00:00:00', 'b_y', 'b_d')
        self.send_json['insured']['certi_no']=t_id_cardNum
        self.send_json['applicant']['certi_no']=b_id_cardNum
        self.send_json['insured']['birthday']=t_birthday
        self.send_json['applicant']['birthday']=b_birthday

        self.send_json['trade_no'] = 'billno'

    #加密报文
    def encrypt(self):
        now_time = int(time() * 1000)
        request_no = str(now_time)
        biz = self.en_aes(self.send_json, self.aes_key)
        message = {"channel_id": self.channel_id, "request_no": request_no, 'biz_content': biz, 'timestamp': now_time}
        # 生成sign验签
        sign_str = json.dumps(message, sort_keys=True).replace(' ', '')
        sign = sign_str + self.md5_key
        sign = encrypt_engie.md5(sign)
        message['sign'] = sign
        return message

    #发送核保报文
    def http_postHeBao(self):
        #加密报文
        message=self.encrypt()
        #post 发送请求
        mess = json.dumps(message).replace(' ','')
        r = requests.post(self.check_url,data =mess)
        result = r.json()
        if r.status_code == 200:
            #返回报文解密
            self.back_json = encrypt_engie.decryptAES(result['biz_content'],self.aes_key)
            dec_dic = json.loads(self.back_json)
            result_info=dec_dic['result']
            return result_info
        else:
            return result['err_msg']
    #生成支付链接
    def generate_pay_url(self):
            sign = "total_fee=" + self.send_json['total_fee'] + "&key=" + self.md5_key
            sign = encrypt_engie.md5(sign)
            self.send_json["channel_id"] = self.channel_id
            self.send_json["out_trade_no"] = self.request_num()
            self.send_json["sign"] = sign
            mess = json.dumps(self.send_json).replace(': ', ':')
            r = requests.post(self.pay_url, data=mess)
            self.back_json = r.json()
            if r.status_code == 200:
                return self.back_json['billno']
            else:
                raise scriptError('支付链接失败：' + self.back_json['msg'])

    # 回调支付链接
    def pay_callback(self):
        mess = json.dumps(self.send_json).replace(': ', ':')
        url = ''
        if self.send_json["paywayid"] == '01':
            url = self.pay_callback_wechat + self.channel_id
        if self.send_json["paywayid"] == '02':
            url = self.pay_callback_alipay + self.channel_id
        if self.send_json['paywayid'] == '32':
            url = self.pay_callback_wechat + self.channel_id
        r = requests.post(url, data=mess)
        self.back_json = r.json()
        if r.status_code == 200:
            return self.back_json['message']
        else:
            raise scriptError('执行失败：' + self.back_json['err_msg'])

    #出单
    def invoice(self):
        self.send_json = json.dumps(self.send_json).replace(': ',':')
        request_no = self.request_num()
        now_time = self.time_stamp()
        biz = encrypt_engie.encryptAES(self.send_json, self.aes_key)
        message = {"channel_id": self.channel_id,"request_no": request_no,'biz_content':biz,'timestamp': now_time}
        dic_list = sorted(message.items(),key=lambda d:d[0])
        order_message = collections.OrderedDict()
        for k,v in dic_list:
            order_message[k] = v
        sign = json.dumps(order_message).replace(' ','') + self.md5_key
        scr_sign = encrypt_engie.md5(sign)
        message["sign"] = scr_sign
        mess = json.dumps(message).replace(' ','')
        r = requests.post(self.invoice_url,data=mess)
        result = r.json()
        if r.status_code == 200:
            #返回报文解密
            self.back_json=encrypt_engie.decryptAES(result['biz_content'],self.aes_key)
            return self.back_json['policy_no']
        else:
            print(result)
            raise scriptError("出单失败：" + result['err_code'])

    # 查保额保费
    def findAmount_pre(self,po_num,amount,perm):
        self.connect_oracle('upiccore', 'sinosoft', '10.130.201.118:1521/tkpi')
        # 计算根据保单号校验保额和保费'''
        if po_num != '':
            sql = "select SUMINSURED,SUMGROSSPREMIUM from gupolicycopymain where policyno='%s'" % po_num
            data = self.find_data(sql)
            re1 = self.compare_ab(amount, data[0])
            re2 = self.compare_ab(perm, data[1])
            self.log(re1)
            self.log(re2)
        self.close_oracle()
    #执行过程的方法
    def run(self):
        # print(self.urlReplace(self.projectPath) + 'ProcessLog.txt')
        self.json_File()
        self.json_conf()
        self.log_send_json()
        #发送报文
        self.http_postHeBao('http://10.130.201.180:8080/tk-link/rest')
        self.log_back_json()
        print(self.back_json)
        #核保成功保存proposalNo
        self.mem('proposalNo',self.back_json['result_content']['proposalNo'])
        print(self.back_json['result_content']['proposalNo'])


if __name__ == '__main__':
    Interface().run()



