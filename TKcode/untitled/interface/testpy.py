from __future__ import unicode_literals
from collections import OrderedDict
import collections
import time
import  requests
import json
import hashlib


import  json



d = OrderedDict()
d = {
            "head": {
                "proposalFormToken": "6596dd59c3b6d7e6673b8bfe1e94371e",
                "proposalFormId": "842261679568330752",
                "version": "01",
                "function": "carModelQuery",
                "transTime": "2017-05-24 00:00:00",
                "reqMsgId": "11111111111111",
                "channelId": "63469",
                "sign_type": "md5",
                "sign": ""
            },
            "apply_content": {
                "carInfo": {
                    "licenseNo": "鲁WS1568",
                    "engineNo": "07154830181",
                    "frameNo": "LSVFX6188E3457125",
                    "enrollDate": "2015-05-11",
                    "newVehicle": "0",
                    "ecdemicVehicle": "0",
                    "vehicleModel": "SVW7183AGi",
                    "chgOwnerFlag": "0",
                    "insuredCode": "420100",
                    "operateFlag": "1",
                    "effectStartTime": "201706151640",
                    "vehicleCode": "AKCACD0002",
                    "vehicleHyCode": "BYQMAMUA0006",
                    "seatCount": "5.0"
                }
            }
            }
# print (d)

# content2 = json.dumps(d, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',').replace('\\"','"')
content2 = json.dumps(d, ensure_ascii=False,sort_keys=True).replace(': ',':').replace(', ',',')
# pstr = json.dumps(str(d), ensure_ascii=False,sort_keys=False)
# print (pstr)
print((content2))
print (type(content2))

'''
#***初始车型查询数据***#
proposalFormToken="6596dd59c3b6d7e6673b8bfe1e94371e"							#交易TOKEN
proposalFormId= "842261679568330752"            #交易ID
version= "01"                                   #版本号
function= "carModelQuery"                       #接口代码
transTime= "2017-05-24 00:00:00"                #发送时间
reqMsgId= "11111111111111"                      #请求报文ID
channelId= "63469"                              #渠道ID
sign_type= "md5"                                #加签方式
licenseNo= "鲁WS1568"                           #车牌号
engineNo= "07154830181"                         #发动机号
frameNo= "LSVFX6188E3457125"                    #车架号
enrollDate= "2015-05-11"                        #初登日期
newVehicle= "0"                                 #新旧车标志
ecdemicVehicle= "0"                             #外地车标志
vehicleModel= "SVW7183AGi"                      #车辆型号
chgOwnerFlag= "0"                               #过户车标识
insuredCode= "420100"                           #投保地编码
operateFlag= "1"                                #车型查询操作类型
effectStartTime= "201706151640"                 #起保日期
vehicleCode= "AKCACD0002"                       #精友车型编码
vehicleHyCode= "BYQMAMUA0006"                   #行业车型编码
seatCount= "5.0"                                #座位数


def sortDictValue(addct,reverse=False):
    keys=addct.keys()
    keys.sort(reverse=reverse)
 return [addct[key] for key in keys]





    __sign = ""
    #####数据构成#####
    content = collections.OrderedDict()
    head = collections.OrderedDict()
    apply_content = collections.OrderedDict()
    carInfo = collections.OrderedDict()
    content['head'] = head
    content["apply_content"]= apply_content
    head["proposalFormToken"]=proposalFormToken
    head["proposalFormId"]=proposalFormId
    head["version"]=version
    head["function"]=function
    head["transTime"]=transTime
    head["reqMsgId"]=reqMsgId
    head["channelId"]=channelId
    head["sign_type"]=sign_type
    head["sign"]= __sign
    apply_content["carInfo"] = carInfo
    carInfo["licenseNo"]=licenseNo
    carInfo["engineNo"]=engineNo
    carInfo["frameNo"]=frameNo
    carInfo["enrollDate"]=enrollDate
    carInfo["newVehicle"]=newVehicle
    carInfo["ecdemicVehicle"]= ecdemicVehicle
    carInfo["vehicleModel"]=vehicleModel
    carInfo["chgOwnerFlag"]=chgOwnerFlag
    carInfo["insuredCode"]=insuredCode
    carInfo["operateFlag"]=operateFlag
    carInfo["effectStartTime"]=effectStartTime
    carInfo["vehicleCode"]=vehicleCode
    carInfo["vehicleHyCode"]=vehicleHyCode
    carInfo["seatCount"]=seatCount
    ###############
    content = json.dumps(content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')

chexing_chaxun()
'''