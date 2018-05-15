from jpype import *
import json
import requests
from time import time
import random
import collections
import xlrd
import xlutils.copy
import string
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

#泰康top平台接口类
class TKInterface():
    def __init__(self,channel_id):
        super(TKInterface,self).__init__()
        self.check_url = 'http://10.130.202.171/api/validatePolicy'
        self.pay_url = 'http://10.130.202.171/api/pay'
        self.pay_callback_wechat = 'http://10.130.202.171/api/pay/weChatWapCallBack?channel_id='
        self.pay_callback_alipay = 'http://10.130.202.171/api/pay/aliPayWapCallBack?channel_id='
        self.invoice_url = 'http://10.130.202.171/api/policy'
        self.aes_key = "D21Uq65MzDF28PaEx7zO0dSM2WuG03z0"
        self.md5_key = "12344404K53N5571lz91673701u04321"
        self.channel_id = channel_id

    #AES加密，需要传入字典类型的报文体
    def en_aes(self,scr_dic,aes_key):

        scr_str = json.dumps(scr_dic).replace(': ',':')
        return encrypt_engie.encryptAES(scr_str,aes_key)

    #需要传入加密字符串
    def de_aes(self,scr,aes_key):

        return encrypt_engie.decryptAES(scr,aes_key)

    #生成请求流水号
    def request_num(self):
        return '78966697798' + str(random.randint(1,9999))

    #时间戳
    def time_stamp(self):
        return int(time() * 1000)

    #计算出生日期
    def calculate_birthday(self,start_date,age,days):
        #2000-01-02 00:00:00:00
        if age == '' or days == '':
            return ''
        year = str(int(start_date[:4]) - int(age))
        my_date = year + start_date[4:]
        print(my_date)
        d = datetime.datetime.strptime(my_date,'%Y-%m-%d %H:%M:%S')
        print(d)
        delta = datetime.timedelta(days = int(days))
        print(delta)
        date_delta = d + delta
        print(date_delta)
        return date_delta.strftime('%Y-%m-%d')

    #md5生成加密验签
    def en_md5(self,ordered_mess,md5_key):
        ordered_str = json.dumps(ordered_mess).replace(' ','')
        sign = ordered_str + md5_key
        return encrypt_engie.md5(sign)

    #从TXT文件读取报文,文件一般存在于：'D:/JettechAgent1.6.0/conf/testData/hebao.txt'
    def read_from_txt(self,path):
        try:
            with open(path,'r',encoding='utf-8') as read_obj:
                mess_dic = json.load(read_obj)
        except Exception as e:
            raise scriptError(str(e))
        return mess_dic


    #将返回的json报文序列化到TXT文件
    def write_to_txt(self,path,message):
        try:
            with open(path,'w',encoding='utf-8') as write_obj:
                # json.dump(write_obj,message)
                write_obj.write(message)
        except Exception as e:
            raise scriptError(str(e))

    #excel文件操作
    def open_excel(self,fileName):
        self.workbook = xlrd.open_workbook(fileName)
        self.wb = xlutils.copy.copy(self.workbook)



    def save_excel(self,fileName):
        self.wb.save(fileName)
        self.workbook.release_resources()

    def get_row_count(self,sheetName):
        return int(self.workbook.sheet_by_name(sheetName).nrows)

    def read_data_by_coordinate(self,sheetName,row,col):
        return self.workbook.sheet_by_name(sheetName).cell(int(row),int(col)).value

    def write_data_by_coordinate(self,sheetName,row,col,value):
        ws = self.wb.get_sheet(self.workbook.sheet_names().index(sheetName))
        ws.write(int(row),int(col),value)

    #修改json字典
    def modify_message_dic(self,dic,m_key,m_value):
        #dic 是一个字典类型，返回的也是字典类型
        dic[m_key] = m_value
        return dic

    #修改嵌套字典的值
    def modify_double_key_dic(self,dic,key1,key2,m_value):
        dic[key1][key2] = m_value
        return dic

    #修改字典中嵌套list
    def modify_key_index_dic(self,dic,m_key,index,m_value):
        dic[m_key][int(index)] = m_value
        return dic


    #修改list的方法,返回的也是list
    def modify_message_list(self,lis,index,value):
        lis[index] = value
        return lis



    #发送请求
    def http_post(self,url,param_dic):
        my_data = json.dumps(param_dic).replace(' ','')
        return requests.post(url,data=my_data)

    #核保
    def check_insurance(self,biz_content):
        #构造请求报文
        request_no = self.request_num()
        now_time = int(time() * 1000)
        biz = self.en_aes(biz_content,self.aes_key)
        message = {"channel_id": self.channel_id,"request_no": request_no,'biz_content':biz,'timestamp': now_time}
        #生成sign验签
        # dic_list = sorted(message.items(),key=lambda d:d[0])
        # order_message = collections.OrderedDict()
        # for k,v in dic_list:
        #     order_message[k] = v
        sign_str = json.dumps(message,sort_keys=True).replace(' ','')
        sign = sign_str + self.md5_key
        sign = encrypt_engie.md5(sign)
        message['sign'] = sign

        #post 发送请求
        mess = json.dumps(message).replace(' ','')
        r = requests.post(self.check_url,data =mess)
        result = r.json()
        if r.status_code == 200:
            #返回报文解密
            dec_str = encrypt_engie.decryptAES(result['biz_content'],self.aes_key)
            dec_dic = json.loads(dec_str)
            return dec_dic['result']
        else:
            #['err_msg']
            return result['err_msg']

    def generate_sign(self,content):
        return encrypt_engie.md5(content)
    #生成支付链接
    def generate_pay_url(self,path,dic):
        #生成验签
        sign = "total_fee="+dic['total_fee']+"&key=" + self.md5_key
        sign = encrypt_engie.md5(sign)
        dic["channel_id"] = self.channel_id
        dic["out_trade_no"] = self.request_num()
        dic["sign"] = sign
        #将发送的报文保存到TXT
        self.write_to_txt(path,str(dic))
        mess = json.dumps(dic).replace(': ',':')
        r = requests.post(self.pay_url,data = mess)
        result = r.json()
        if r.status_code == 200:
            #返回billno和request_token
            # billno = result['result']['billno']
            # request_token = re.findall(r"<request_token>(.+)</request_token>",result['result']['payUrl'])
            # return  billno,request_token
            return result['result']
        else:
            raise scriptError('支付链接失败：' + result['msg'])
    #根据key获取字典中的值
    def get_dic_value(self,dic,key):

        return dic[key]

    #回调支付链接
    def pay_callback(self,dic):
        mess = json.dumps(dic).replace(': ',':')
        url = ''
        if dic["paywayid"] == '01':
            url = self.pay_callback_wechat + self.channel_id
        if dic["paywayid"] == '02':
            url = self.pay_callback_alipay + self.channel_id
        if dic['paywayid'] == '32':
            url = self.pay_callback_wechat + self.channel_id
        r = requests.post(url,data=mess)
        result = r.json()
        if r.status_code == 200:
            return result['message']
        else:
            raise scriptError('执行失败：' + result['err_msg'])



    #出单
    def invoice(self,dic):

        dic = json.dumps(dic).replace(': ',':')

        biz = encrypt_engie.encryptAES(dic,self.aes_key)
        request_no = self.request_num()
        now_time = self.time_stamp()
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
            return encrypt_engie.decryptAES(result['biz_content'],self.aes_key)
        else:
            print(result)
            raise scriptError("出单失败：" + result['err_code'])




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
    #随机生成字符
    def random_letters(self,count):
        count = int(count)
        s = string.ascii_uppercase
        r = ''
        while count > 0:
            r += random.choice(s)
            count -= 1
        return r
    #生成随机数字字符串
    def random_num_str(self):
        return str(random.randint(1,9999)) + str(random.randint(1,9999)) + str(random.randint(1,9999))
    #随机生成数字
    def random_num(self,count):
        count = int(count)
        s = '0123456789'
        r = ''
        while count > 0:
            r += random.choice(s)
            count -= 1
        return r
    #随机生成汉字
    def random_gbk2312(self,count):
        random_CH = ''
        while count > 0:
            head = random.randint(0xB0, 0xCF)
            body = random.randint(0xA, 0xF)
            tail = random.randint(0,0xF)
            val = (head << 8) | (body << 4) | tail
            r_str = "%x" % val
            try:
                random_CH += bytes.fromhex(r_str).decode('gb2312')
            except Exception as e:
                #处理不能被gb2312解码的特殊字符
                count += 1
                print(str(e))
            count -= 1
        return random_CH
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
            self.rs.execute(sql)
            res = self.rs.fetchall()
            return res[0]
        except Exception as e:
            self.close_oracle()
            print(e)
    #更新数据库
    def update_oracle(self,sql):
        try:
            self.rs.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.close_oracle()
            print(e)

    def compare_ab(self,a,b):
        a = float(a)
        b = float(b)
        if a == b:
            return str(a) + '相等' + str(b)
        else:
            return str(a) + '不等' + str(b)

if __name__ == "__main__":
    tki = TKInterface('100000000143')

    print(tki.calculate_birthday('2018-01-31 00:00:00','0','-1'))
    '''
    #--------------------------校验保额保费-----------------------------
    #打开excel
    excel_path = 'D:/JettechAgent1.6.0/conf/testData/萨摩耶恶性肿瘤轻症组合/萨摩耶恶性肿瘤轻症组合.xls'
    tki.open_excel(excel_path)
    tki.connect_oracle('upiccore','sinosoft','10.130.201.118:1521/tkpi')
    #计算根据保单号校验保额和保费
    for x in range(1,49):
        po_num = tki.read_data_by_coordinate('Sheet1',x,6)
        amount = tki.read_data_by_coordinate('Sheet1',x,3)
        perm = tki.read_data_by_coordinate('Sheet1',x,4)
        if po_num != '':
            sql = "select SUMINSURED,SUMGROSSPREMIUM from gupolicycopymain where policyno='%s'" %po_num
            data = tki.find_data(sql)
            print(data)
            re1 = tki.compare_ab(amount,data[0])
            re2 = tki.compare_ab(perm,data[1])
            tki.write_data_by_coordinate('Sheet1',x,13,re1)
            tki.write_data_by_coordinate('Sheet1',x,14,re2)
            tki.wb.save(excel_path)
    tki.save_excel(excel_path)
    tki.close_oracle()

    #--------------------------核保出单---------------------------------
    # hebao_mess = tki.read_from_txt('D:/JettechAgent1.6.0/conf/testData/圣源祥个人中高端/hebao.txt')
    hebao_mess = {
	"amount":"100000",
	"end_date":"2019-01-29 23:59:59",
	"insured":{

		"birthday":"1990-10-14",
		"phone":"13161084234",
		"sex":"1",
		"email":"adf@165.com",
		"name":"张朝杰",
		"relation":"40",
		"certi_type":"01",
		"type":"1",
		"certi_no":"350583199010143398"
	},

	"product_id":"1007A01R01",
	"insure_date":"2018-01-29 09:50:32",
	"premium":"78",
	"applicant":{

		"birthday":"1990-10-14",
		"sex":"1",
		"phone":"13161084234",
		"certi_type":"01",
		"type":"1",
		"email":"adf@165.com",
		"certi_no":"350583199010143398",
		"name":"张朝杰"
	},

	"kind_list":[

		{
			"amount":"50000",
			"kind_code":"1007015",
			"premium":"62.4"
		},

		{
			"amount":"50000",
			"kind_code":"1007009",
			"premium":"15.6"
		}
	],

	"start_date":"2018-01-30 00:00:00",
	"extend_params":{

		"FieldEI":"1",
		"beneficiary_is_legal":"1"
	}
}
    zflj = {
	"total_fee":"78",
	"out_trade_no":"1502352544545774114",
	"callbackurl":"http://www.tk.cn",
	"notifyurl":"http://xxx.com/api/policy",
	"productname":"泰康在线保险",
	"failurl":"http://www.tk.cn",
	"sign":"+LUfnwTvXXXXXprVazzw==",
	"channel_id":"common",
	"payType":"02"
}
    zfhd = {
        "amount":'total_fee',
        "billno":'billno',
        "customerinfo":"13751449549",
        "isdistort":False,
        "paywayid":"32",
        "reason":"%25E6%2594",
        "requestType":"1",
        "result":True,
        "token":"26392a3976c0d3b8d85c01c3158bd39f"
        }

    #打开excel
    excel_path = 'D:/JettechAgent1.6.0/conf/testData/萨摩耶恶性肿瘤轻症组合/萨摩耶恶性肿瘤轻症组合.xls'
    tki.open_excel(excel_path)
    for x in range(9,49):
        #读取excel文件数据140/155/196
        test_no = tki.read_data_by_coordinate('Sheet1',x,0)
        amount = tki.read_data_by_coordinate('Sheet1',x,3)
        premium = tki.read_data_by_coordinate('Sheet1',x,4)
        amount1 = tki.read_data_by_coordinate('Sheet1',x,7)
        amount2 = tki.read_data_by_coordinate('Sheet1',x,8)
        premium1 = tki.read_data_by_coordinate('Sheet1',x,9)
        premium2 = tki.read_data_by_coordinate('Sheet1',x,10)
        b_y = tki.read_data_by_coordinate('Sheet1',x,11)
        b_d = tki.read_data_by_coordinate('Sheet1',x,12)

        t_cer = tki.id_card_mum('1990-10-14')
        b_birthday = tki.calculate_birthday('2018-01-30 00:00:00',b_y,b_d)
        b_cer = tki.id_card_mum(b_birthday)
        #构造报文
        hebao_mess['amount'] = amount
        hebao_mess['premium'] = premium
        hebao_mess['applicant']['certi_no'] = t_cer
        hebao_mess['insured']['certi_no'] = b_cer
        hebao_mess['insured']['birthday'] = b_birthday
        hebao_mess['kind_list'][0]['amount'] = amount1
        hebao_mess['kind_list'][1]['amount'] = amount2
        hebao_mess['kind_list'][0]['premium'] = premium1
        hebao_mess['kind_list'][1]['premium'] = premium2

        #将字典类型转换成字符串
        hebao_str = str(hebao_mess)
        tki.write_to_txt('D:/JettechAgent1.6.0/conf/testData/萨摩耶恶性肿瘤轻症组合/核保/send/' + test_no + 'send.txt',hebao_str)
        #核保
        hebao_result = tki.check_insurance(hebao_mess)
        print(hebao_result)
        tki.write_to_txt('D:/JettechAgent1.6.0/conf/testData/萨摩耶恶性肿瘤轻症组合/核保/receive/' + test_no + 'receive.txt',str(hebao_result))
        #将核保返回的提示信息保存到excel中
        tki.write_data_by_coordinate('Sheet1',x,5,hebao_result)
        tki.wb.save(excel_path)
        if '核保成功' in hebao_result:
            #进行生成支付链接操作
            zflj['total_fee'] = premium
            zf_path = 'D:/JettechAgent1.6.0/conf/testData/萨摩耶恶性肿瘤轻症组合/生成支付链接/send/' + test_no + 'send.txt'
            zf_result = tki.generate_pay_url(zf_path,zflj)
            billno = zf_result['billno']
            if billno != '':
                #支付回调
                zfhd['amount'] = premium
                zfhd['billno'] = billno
                tki.pay_callback(zfhd)
                #进行出单操作
                cd_mess = hebao_mess
                cd_mess['trade_no'] = billno
                tki.write_to_txt('D:/JettechAgent1.6.0/conf/testData/萨摩耶恶性肿瘤轻症组合/出单/send/' + test_no + 'send.txt',str(cd_mess))
                cd_result = tki.invoice(cd_mess)
                print(cd_result)
                #保存返回信息到TXT
                tki.write_to_txt('D:/JettechAgent1.6.0/conf/testData/萨摩耶恶性肿瘤轻症组合/出单/receive/' + test_no + 'receive.txt',str(cd_result))
                cd_dic = json.loads(cd_result)
                #获取保单号
                policy_no = cd_dic['policy_no']
                #保存保单号
                tki.write_data_by_coordinate('Sheet1',x,6,policy_no)
                tki.wb.save(excel_path)
    #保存excel
    tki.save_excel(excel_path)'''



