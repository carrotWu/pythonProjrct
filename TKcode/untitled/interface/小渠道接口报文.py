from __future__ import unicode_literals
import hashlib
import requests
import json
import base64
import urllib
import collections
import time


# 泰康在线小渠道平台接口类

content_1 = {
    "serialno": "7148623367679321",
    "applicantList": [
        {
            "identifyNumber": "632725199201180024",
            "identifyType": "01",
            "name": "张三一",
            "mobile": "13161084234",
            "birthday": "1992-01-18",
            "mail": "13903010001@163.com",
            "sex": "2"
        }
    ],
    "insuredList": [
        {
            "identifyNumber": "513322199201189419",
            "identifyType": "01",
            "name": "张久久",
            "mobile": "13903010001",
            "birthday": "1992-01-18",
            "sex": "1",
            "relatedperson": "10",
            "mail": "13903010001@163.com"
        }
    ],
    "issueDate": "2018-01-22 16:00:02",
    "startDate": "2018-01-23 00:00:00",
    "endDate": "2018-01-22 23:59:59",
    "comboId": "1007A01F03",
    "premium": "133",
    "amount": "250000"
}

transTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
serialno = str(int(time.time()*1000000))
print(transTime)
print(serialno)


#  报文解析
content = collections.OrderedDict()
applicantList = collections.OrderedDict()
insuredList = collections.OrderedDict()
content['serialno'] = serialno
content['applicantList'] = applicantList
applicantList['identifyNumber'] = '632725199201180024'
applicantList['identifyType'] = '01'
applicantList['name'] = '张三一'
applicantList['mobile'] = '13161084234'
applicantList['birthday'] = '1992-01-18'
applicantList['mail'] = '13903010001@163.com'
applicantList['sex'] = '2'
insuredList['identifyNumber'] = '450329199201186758'
insuredList['identifyType'] = '01'
insuredList['name'] = '张久久'
insuredList['mobile'] = '13903010001'
insuredList['birthday'] = '1992-01-18'
insuredList['sex'] = '1'
insuredList['relatedperson'] = '10'
insuredList['mail'] = '13903010001@163.com'
insuredList['career'] = '00101001'
content['insuredList'] = insuredList
content['issueDate'] =transTime
content['startDate'] ='2018-01-23 00:00:00'
content['endDate'] = "2018-01-22 23:59:59"
content['comboId'] ="1007A01F03"
content['fromId'] ="16104"
content['premium'] ="253"
content['amount'] ='400000'


proposalNo = ''
pstr = ''
applicant_str =''
insured_str = ''
# for key, val in content.items():
#     if key == 'applicantList':
#         for key_app, val in applicantList.items():
#             if key_app == 'sex':
#                 applicant_str += '"' + key_app + '"' + ':' + '"' + val + '"'
#             else:
#                 applicant_str += '"'+key_app + '"' + ':' +'"' + val +'"' + ','
#         applicant_str = '[{' + applicant_str + '}],'
#         pstr += '"' + 'applicantList' + '"' + ':' + applicant_str
#     elif key == 'insuredList':
#         for key_insured, val in insuredList.items():
#             if key_insured == 'career':
#                 insured_str += '"' + key_insured + '"' + ':' + '"' + val + '"'
#             else:
#                 insured_str += '"'+ key_insured + '"'+ ':' +'"' + val + '"' + ','
#         insured_str = '[{' + insured_str + '}],'
#         pstr += '"' + 'insuredList'+ '"' + ':' + insured_str
#     elif key == 'amount':
#         pstr += '"' + key + '"' + ':' + '"' + val + '"'
#     else:
#         pstr += '"'+key +'"'+ ':' +'"'+ val +'"'+ ','
# pstr = '{' + pstr + '}'
# print(pstr)
pstr = json.dumps(content, ensure_ascii=False)
print(pstr.replace(' ', ''))


# 编码报文
content_str =  urllib.parse.quote(pstr.encode('GBK')).replace('%20', '+').upper()
md5key = content_str + 'hzkey123'

# # MD5加密
m = hashlib.md5()
m.update(md5key.encode('GBK'))
sign = m.hexdigest()
print(sign)

# 发送报文
encypt_content_sign = base64.b64encode(pstr.encode('GBK'))
r = requests.post(
    'http://ecuat.tk.cn/tkcoop/service/proposalEntrance/proposalCreateEntrance?sign='+sign+'&comboid=1007A01F01&fromId=16104',
    data=encypt_content_sign)
result = base64.b64decode(r.content)
print(result.decode('GBK'))

content_result = json.loads(result.decode('GBK'))
if content_result['code'] == '200':
    print(content_result['result']['proposalNo'])
    proposalNo = content_result['result']['proposalNo']

chudan_content = {
    "serialno": "12341100101010010",
    "proposalNo": "001051107201714352316776614",
    "payMoney": "240",
    "comboId": "1007A01F01",
    "payTime": "2017-03-23 00:00:00",
    "payAccount": "7512489612@qq.com",
    "outTradeId": "5455555555555"
}

chudan_content = collections.OrderedDict()
chudan_content['serialno'] = serialno
chudan_content['proposalNo'] = proposalNo
chudan_content['payMoney'] = '253'
chudan_content['comboId'] = "1007A01F03"
chudan_content['payTime'] = transTime
chudan_content['payAccount'] = '13903010001@163.com'
chudan_content['outTradeId'] = "5455555555555"

print(chudan_content)
print (type(chudan_content))
chudan_str = ''
for key, val in chudan_content.items():
    if key == 'outTradeId':
        chudan_str += '"' + key + '"' + ':' + '"' + val + '"'
    else:
        chudan_str += '"'+key +'"'+ ':' +'"'+ val +'"'+ ','
chudan_str = '{' + chudan_str + '}'
print(chudan_str)
# 编码报文
content_chudan_str =  urllib.parse.quote(chudan_str.encode('GBK')).replace('%20', '+').upper()
md5key = content_chudan_str + 'hzkey123'

# # MD5加密
m = hashlib.md5()
m.update(md5key.encode('GBK'))
sign = m.hexdigest()
print(sign)

# 发送报文
encypt_content_sign = base64.b64encode(chudan_str.encode('GBK'))
r = requests.post(
    'http://ecuat.tk.cn/tkcoop/service/policyEntrance/policyCreateEntrance?sign=' + sign + '&comboid=1007A01F01&fromId=16104',
    data=encypt_content_sign)
result = base64.b64decode(r.content)
print(result.decode('GBK'))