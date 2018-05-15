import hashlib
import requests
import json
import base64
import urllib
import collections
import time
import random
import logging
import os
import sys


class scriptError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class TK_LITTLE_CHANNEL():
    # 泰康在线小渠道平台接口类


    def __init__(self):
        # 初始化生成随机号和格式化时间
        self.serialno = str(int(time.time() * 1000000))
        self.transTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.projectPath = "D:\\JettechAgent1.6.0\\execute"
        # self.params = params
        self.logConfig()
    def id_card_mum(self, birth, sex=1):
        # 生成身份证号1991-01-01
        birth = str(birth)
        year = birth[0:4]
        month = birth[4:6]
        day = birth[6:]
        cid_list = ['110101', '110102', '110105', '110106', '110107', '110108', '110109', '110111', '110112',
                    '110113', '110114', '110115',
                    '110116', '110117', '110228', '110229', '120106', '120107', '120108', '120109', '120110',
                    '120111', '120112', '120113', '120114', '120115',
                    '120200', '120221', '120223', '120225', '130100', '130101', '130104', '130105', '130107',
                    '130108', '130121', '130123', '130124', '130125',
                    '140100', '140105', '140106', '140107', '140108', '140109', '140110', '140121', '140122',
                    '140123', '140181', '140200', '140202', '140203',
                    '320100', '320102', '320104', '320105', '320106', '320111', '320113', '320114', '320115',
                    '320116', '320124', '320125', '320200', '320202']
        last = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
        cid = random.choice(cid_list) + str(year) + str(month).zfill(2) + str(day).zfill(2) + str(
            random.randrange(int(sex), 999, 2)).zfill(3)
        # 计算校验码
        sum_mum = int(cid[0]) * 7 + int(cid[1]) * 9 + int(cid[2]) * 10 + int(cid[3]) * 5 + int(
            cid[4]) * 8 + int(cid[5]) * 4 + int(cid[6]) * 2 + int(cid[7]) * 1 \
                  + int(cid[8]) * 6 + int(cid[9]) * 3 + int(cid[10]) * 7 + int(cid[11]) * 9 + int(
            cid[12]) * 10 + int(cid[13]) * 5 + int(cid[14]) * 8 + int(cid[15]) * 4 + int(cid[16]) * 2
        cid = cid + last[sum_mum % 11]
        return cid
    def time_format(self, birthday):
        # 将6位数转换时间格式：19880325转换为1988-03-25
        year = birthday[0:4]
        month = birthday[4:6]
        day = birthday[6:]
        birthday = year + "-" + month + "-" + day
        return birthday
    def joint_url(self, sign, url_type, url_type_text, comboId, fromId):
        # 组装核保、出单url
        url = 'http://ecuat.tk.cn/tkcoop/service/' + url_type + '/' + url_type_text + \
              '?sign=' + sign + '&comboid=' + comboId + '&fromId=' + fromId
        return url
    def gain_md5Sign(self, content, md5_key):
        # 生成MD5标签，replace('%20', '+')为了是编码后的字符串和java编码后一致

        message = json.dumps(content, ensure_ascii=False)
        content_str = urllib.parse.quote(message.encode('GBK')).replace('%20', '+').upper()
        md5key = content_str + md5_key
        m = hashlib.md5()
        m.update(md5key.encode('GBK'))
        sign = m.hexdigest()
        return sign
    def post_message(self, content, message_url):
        # 发送报文
        message = json.dumps(content, ensure_ascii=False)
        encypt_content_sign = base64.b64encode(message.encode('GBK'))
        r = requests.post(message_url, data=encypt_content_sign)
        result = base64.b64decode(r.content)
        content_result = json.loads(result.decode('GBK'))
        return content_result
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
    def getFile(self, filePath, handle):
        # 获取文件句柄
        try:
            file = open(filePath, mode=handle,
                        buffering=1, encoding='gbk', errors=None,
                        newline='\r\n', closefd=True, opener=None)
            return file
        except Exception:
            funName = sys._getframe().f_code.co_name
            raise scriptError(funName + '-----异常')
    def urlReplace(self, path):
        # 资源路径分隔符替换
        return path.replace('\\', r'\\')
    def logConfig(self):
        logger = logging.getLogger('pyLogging')
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.urlReplace(self.projectPath) + '/ProcessLog.txt')
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        self.loginfo = logger
    def log(self, msg):
        self.loginfo.info(msg)

    def parse_message(self):
        self.content = collections.OrderedDict()
        applicantList = collections.OrderedDict()
        insuredList = collections.OrderedDict()
        self.content['serialno'] = self.serialno
        self.content['applicantList'] = []
        self.content['insuredList'] = []
        applicantList['identifyNumber'] = self.id_card_mum('19920118', 2)
        applicantList['identifyType'] = '01'
        applicantList['name'] = '张三一'
        applicantList['mobile'] = '13161084234'
        applicantList['birthday'] = self.time_format('19920118')
        applicantList['mail'] = '13903010001@163.com'
        applicantList['sex'] = '2'
        self.content['applicantList'].append(applicantList)
        insuredList['identifyNumber'] = self.id_card_mum('19920118', 1)
        insuredList['identifyType'] = '01'
        insuredList['name'] = '张久久'
        insuredList['mobile'] = '13161084234'
        insuredList['birthday'] = self.time_format('19920118')
        insuredList['sex'] = '1'
        insuredList['relatedperson'] = '10'
        insuredList['mail'] = '13903010001@163.com'
        insuredList['career'] = '00101001'
        self.content['insuredList'].append(insuredList)
        self.content['issueDate'] = '2018-01-30 00:00:00'
        self.content['startDate'] = '2018-01-30 00:00:00'
        self.content['endDate'] = '2018-01-29 23:59:59'
        self.content['comboId'] = '1007A01F03'
        self.content['fromId'] = '16104'
        self.content['premium'] = '253'
        self.content['amount'] = '400000'
        return self.content
    def run(self):
        str = self.parse_message()
        sign = self.gain_md5Sign(str, 'hzkey123')
        url = self.joint_url(url_type='proposalEntrance', url_type_text='proposalCreateEntrance', sign=sign,
                                   fromId='16104', comboId='1007A01F01')
        self.log('----------发送报文--------------')
        result = self.post_message(str, message_url=url)
        self.log(str)
        self.log('----------接收报文--------------')
        self.log(result)
        msg_info = result['result']['proposalNo']
        self.mem('proposalNo', msg_info)
if __name__ == '__main__':
    TK_LITTLE_CHANNEL().run()


##**imagePath=D:\\JettechAgent1.6.0\\execute/result/image/TC-T20170869715-0001/TC-T20170869715-0001-01
