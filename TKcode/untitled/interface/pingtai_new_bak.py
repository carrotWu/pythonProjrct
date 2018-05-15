
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

        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()
        cars = collections.OrderedDict()

        self.content['head'] = head
        self.content["apply_content"]= apply_content

        head["proposalFormToken"]="1234567890ABCDEF"
        head["proposalFormId"]="6affbc43e89743cb9206955002a3322b"
        head["version"]="01"
        head["function"]="KindsInit"
        head["transTime"]="2017-05-24 00:00:00"
        head["reqMsgId"]="11111111111111"
        head["channelId"]="64190"
        head["sign_type"]="md5"
        head["sign"]= ""

        apply_content["cars"] = cars
        cars["carModelKey"]="6affbc43e89743cb9206955002a3322b01"
        cars["chgOwnerFlag"]="0"
        cars["carOwner"]="刘艳"
        cars["carOwnerIdentifyType"]="01"
        cars["carOwnerIdentifyNumber"]="542330200501261734"
        # cars["transferDate"]= ""
        # cars["certificateDateBJ"]=""
        # cars["certificateType"]=""
        # cars["certificateNo"]=""


        '''
        apply_content["checks"] = []
        check1 = OrderedDict()
        apply_content["checks"].append(check1)
        check2 = OrderedDict()
        check2["querySequenceNo"] = ""
        check2["checkCode"] = ""
        check2["checkFlag"] = ""
        check1['check'] = check2
        '''
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