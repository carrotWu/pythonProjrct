
from __future__ import unicode_literals
from collections import OrderedDict
import collections
import  requests
import hashlib
import requests
import json
import base64
import urllib
import collections
import time
import random
import logging
import  os,sys
import re

url = "http://10.130.201.180:8082/tk-link/rest"
headers = {"Content-Type":"application/json;charset=UTF-8"}

class scriptError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class TessInt:

    def __init__(self):
        self.touken = ""
        self.baowen = "" #拼好的报文
        self.data =""
        self.baowen_str =""
        self.projectPath = "D:\\JettechAgent1.6.0\\execute"
        self.logConfig()
    def encry_md5(self,zfc):
        m = hashlib.md5()
        m.update(zfc.encode("utf8"))
        return m.hexdigest()

    def get_sign(self,baowen):#报文
        self.baowen_str = json.dumps(baowen, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        jiaqian = ''.join(re.findall(r'apply_content":(.*)}',self.baowen_str))
        sign = self.encry_md5(self.touken+jiaqian)
        print (sign)
        return sign
    def all_baowen(self,baowen,sign):
        self.data = baowen.replace('"sign":""','"sign":'+'"'+str(sign)+'"')
        print (self.data)
    def getFile(self, filePath, handle):
        file = open(filePath, mode=handle,
                    buffering=1, encoding='gbk', errors=None,
                    newline='\r\n', closefd=True, opener=None)
        return file
    def urlReplace(self, grandpa_path):
        return grandpa_path.replace("\\", "/")

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

    def logConfig(self):
        logger = logging.getLogger('pyLogging')
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.urlReplace(self.projectPath) + '/ProcessLog.txt')
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        self.loginfo = logger

    def getToken(self):#2.2.1.获取TOKEN令牌接口

        __gettoken = {
                "head": {
                "version": "v1",
                "function": "getToken",
                "transTime": "2017-06-22 13:44:17",
                "channelId": "64350",
                "reqMsgId": "sdjfweotjgjiowjrtekljwre"
                    },
                "apply_content": {}
                }

        __linpai = json.loads(requests.post(url,headers=headers,data=json.dumps(__gettoken)).text, object_pairs_hook=OrderedDict)
        #**取得token**#

        self.touken = __linpai["apply_content"]["data"]["proposalFormToken"]
        print (self.touken)

    def post_message(self, content, message_url):
        fhbw = requests.post(url=url,headers=headers,data=self.data.encode('utf-8'))
        # print (json.loads(fhbw.text))
        return json.loads(fhbw.text)

    def parse_message(self):

        '''
        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()



        self.content['head'] = head
        self.content["apply_content"]= apply_content


        head["proposalFormToken"]="6596dd59c3b6d7e6673b8bfe1e94371e"
        head["proposalFormId"]="842261679568334521"
        head["version"]="v1"
        head["function"]="priceQuote"
        head["transTime"]="2017-08-24 14:16:00"
        head["reqMsgId"]="11111111111111"
        head["sign_type"]="md5"
        head["sign"]= ""
        head["channelId"]="64287"

        car = collections.OrderedDict()
        apply_content["car"] = car
        car["carModelKey"]="84226167956833452101"
        car["chgOwnerFlag"]="0"
        car["transferDate"]= "2017-05-20"
        car["certificateDateBJ"]="2017-06-20"
        car["certificateType"]=""
        car["certificateNo"]=""


        apply_content["riskList"] = []
        risk = OrderedDict()

        apply_content["riskList"].append(risk)
        check2 = OrderedDict()
        check2["riskCode"] = "0803"
        check2["effectStartTime"] = ""
        check2["effectEndTime"] = ""
        check2["kindList"] = []
        risk['risk'] = check2

        kong = OrderedDict()

        check2["kindList"].append(kong)
        kind = OrderedDict()
        kind["kindCode"] = "02"
        kind["amount"] = "200000"
        kind["quantity"] = "45"
        kind["unitAmount"] = "12"
        kind["kindFlag"] = "1"
        kong["kind"] = kind


        risk1 = OrderedDict()
        apply_content["riskList"].append(risk1)
        check3 = OrderedDict()
        check3["riskCode"] = "0807"
        check3["effectStartTime"] = ""
        check3["effectEndTime"] = ""
        check3["kindList"] = []
        risk1['risk'] = check3

        kong1 = OrderedDict()

        check3["kindList"].append(kong1)
        kind1 = OrderedDict()
        kind1["kindCode"] = "BZ"
        kind1["amount"] = "122000"
        kind1["quantity"] = "45"
        kind1["unitAmount"] = "12"
        kind1["kindFlag"] = "0"
        kong1["kind"] = kind1


        apply_content["privyList"] = []
        privy = OrderedDict()
        apply_content["privyList"].append(privy)
        add3 = OrderedDict()
        add3["insuredFlag"]="0010000"
        add3["insuredName"]="刘小六"
        add3["identifyType"]="01"
        add3["identifyNumber"]="370283198806208436"
        add3["mobile"]="17600298249"
        privy["privy"]=add3
        '''
        '''
        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()

        self.content['head'] = head
        self.content["apply_content"]= apply_content

        head["proposalFormToken"]="26f28f4f82072959421f021cbe2de417"
        head["proposalFormId"]="123456"
        head["version"]="1.0"
        head["function"]="doGetIssueCodeImpl"
        head["transTime"]="2017-03-05 00:00:00"
        head["reqMsgId"]="11"
        head["channelId"]="64287"
        head["sign"]= "ca8a9aecf388c4e0efbeb931ba5d4096"
        head["sign_type"]="md5"


        apply_content["proposalNo"] = "00412001360201700000000775"
        apply_content["issueCode"] = "WP7TP9"
        '''
        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()

        self.content['head'] = head
        self.content["apply_content"]= apply_content

        head["proposalFormToken"]="e145c7b815fabe96232694e2939fb499"
        head["proposalFormId"]="843322492923641856"
        head["version"]="v1"
        head["function"]="policyNotice"
        head["transTime"]="2017-03-05 00:00:00"
        head["reqMsgId"]="11111111111111"
        head["channelId"]=""
        head["sign_type"]=""
        head["sign"]=""

        apply_content["success"] =""
        apply_content["errorCode"] =""
        apply_content["errorMessage"] =""
        apply_content["policyNo"] =""
        apply_content["subPolicyNo_BI"] ="6370200080320170000589"
        apply_content["subPolicyNo_CI"] ="6370200080720170000613"
        return self.content

    def log(self, msg):
        self.loginfo.info(msg)

    def run(self):
        self.getToken()
        baowen_before = self.parse_message()
        su = self.get_sign(baowen_before)
        self.all_baowen(self.baowen_str,su)

        self.log('----------发送报文--------------')
        result = self.post_message(baowen_before, message_url=url)
        self.log(baowen_before)
        self.log('----------接收报文--------------')
        self.log(result)
        msg_info = result['apply_content']['messageBody']
        self.mem('proposalNo', msg_info)
if __name__ == '__main__':
    TessInt().run()