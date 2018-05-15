from __future__ import unicode_literals
from collections import OrderedDict
import collections
import time
import  requests
import json
import hashlib

#***连接参数***#
__url = "http://10.130.201.180:8082/tk-link/rest"
__headers = {"Content-Type":"application/json;charset=UTF-8"}



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
#*************#

#***初始险别初始化数据***#
carModelKey = "b938e534dcd749589d3ddf8df675d8fc01"
carOwner = "刘艳"
carOwnerIdentifyType = "01"
carOwnerIdentifyNumber = "542330200501261734"
transferDate =""
certificateDateBJ = ""
certificateType = ""
certificateNo = ""

#*************#


def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()
class Car_Insurance:

    def __init__(self):
        self.__url = "http://10.130.201.180:8082/tk-link/rest"
        self.__headers = {"Content-Type":"application/json;charset=UTF-8"}
        self.touken = ""
    def getToken(self):

        #2.2.1.获取TOKEN令牌接口

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
        # print (type(__gettoken))
        __fanhui = requests.post(self.__url,headers=self.__headers,data=json.dumps(__gettoken))
        __linpai = json.loads(__fanhui.text, object_pairs_hook=OrderedDict)
        #**取得token**#
        # print (__linpai)
        self.touken = __linpai["apply_content"]["data"]["proposalFormToken"]
        print (self.touken)

    def chexingchaxun(self):
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
        content1 = json.dumps(content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        #取sign

        jiaqian =  (content1[271:-1])
        print (jiaqian)
        __newsign = md5(self.touken + jiaqian)


        #把sign 复制给sign
        content['head']['sign'] = __newsign

        #要发送的完整报文
        content2 = json.dumps(content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        sd = requests.post(self.__url,headers=self.__headers,data=content2.encode('utf-8'))
        ad = json.loads(sd.text)
        print (ad)
    def xianbie_chushi(self):#险别初始化接口

        #####数据构成#####
        content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()
        cars = collections.OrderedDict()
        check = collections.OrderedDict()

        content['head'] = head
        content["apply_content"]= apply_content

        head["proposalFormToken"]=proposalFormToken
        head["proposalFormId"]="b938e534dcd749589d3ddf8df675d8fc"
        head["version"]=version
        head["function"]="KindsInit"
        head["transTime"]=transTime
        head["reqMsgId"]=reqMsgId
        head["channelId"]="64190"
        head["sign_type"]=sign_type
        head["sign"]= ""

        apply_content["cars"] = cars
        cars["carModelKey"]=carModelKey
        cars["chgOwnerFlag"]=chgOwnerFlag
        cars["carOwner"]=carOwner
        cars["carOwnerIdentifyType"]=carOwnerIdentifyType
        cars["carOwnerIdentifyNumber"]=carOwnerIdentifyNumber
        cars["transferDate"]= transferDate
        cars["certificateDateBJ"]=certificateDateBJ
        cars["certificateType"]=certificateType
        cars["certificateNo"]=certificateNo

        apply_content["checks"] = []
        apply_content["checks"].append(check)
        apply_content["check"] = check
        check["querySequenceNo"] = ""
        check["checkCode"] = ""
        check["checkFlag"] = ""

        ###############

        conte = json.dumps(content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (conte)
    def xianbie_chaxun1(self):
        baowen = ""
        with open('D:\car_inter\险别初始化.txt',encoding='utf-8') as f:
            try:
                while True:
                    line = f.readline()
                    baowen +=line
                    # print (line)
                    # print (type(line))
                    if len(line) <=0 :
                        break
            finally:
                f.close()
        print (baowen)
if __name__ == '__main__':
    Car_Insurance = Car_Insurance()
    # Car_Insurance.getToken()
    # Car_Insurance.chexingchaxun()
    Car_Insurance.xianbie_chushi()
    # Car_Insurance.xianbie_chaxun1()