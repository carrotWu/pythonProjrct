from __future__ import unicode_literals
from collections import OrderedDict
import collections
import time
import  requests
import json
import hashlib


#latest pythonfile


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
        # print (type(__gettoken))
        __fanhui = requests.post(self.__url,headers=self.__headers,data=json.dumps(__gettoken))
        __linpai = json.loads(__fanhui.text, object_pairs_hook=OrderedDict)
        #**取得token**#
        # print (__linpai)
        self.touken = __linpai["apply_content"]["data"]["proposalFormToken"]
        print (self.touken)

    def chexing_chaxun(self):#车型查询接口


        #####数据构成#####
        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()
        carInfo = collections.OrderedDict()

        self.content['head'] = head
        self.content["apply_content"]= apply_content

        head["proposalFormToken"]="1234567890ABCDEF"
        head["proposalFormId"]="6affbc43e89743cb9206955002a3322b"
        head["version"]="1.0"
        head["function"]="carModelQuery"
        head["transTime"]="2018-01-25 13:54:20"
        head["reqMsgId"]="2018012513542067349203665250"
        head["channelId"]="64467"
        head["sign_type"]="md5"
        head["sign"]= ""

        apply_content["carInfo"] = carInfo
        carInfo["licenseNo"]="鲁A6YIUG"
        carInfo["engineNo"]="ENG7HJ45SGG5YYS8H"
        carInfo["frameNo"]="VNNUFN69N59P8XCC8"
        carInfo["enrollDate"]="2015-12-20"
        carInfo["newVehicle"]="0"
        carInfo["ecdemicVehicle"]= "0"
        carInfo["vehicleModel"]="帕萨特SVW7183MJi 标准型"
        carInfo["replacementValue"]="50000"
        # carInfo["chgOwnerFlag"]=chgOwnerFlag
        carInfo["insuredCode"]="420100"
        carInfo["operateFlag"]="4"
        # carInfo["effectStartTime"]=effectStartTime
        carInfo["vehicleCode"]=""
        carInfo["vehicleHyCode"]="BSHCPTUB0004"
        carInfo["seatCount"]="5"
        ###############
        content1 = json.dumps(self.content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        #取sign


    def xianbie_chushi(self):#险别初始化接口

        #####数据构成#####
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

        ###############

        __conte1 = json.dumps(__content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
        print (__conte1[281:-1])
        print (len(__conte1))

        #取sign
        __jiaqian =  (__conte1[281:-1])
        print (__jiaqian)
        print (self.touken + __jiaqian)
        __newsign = md5(self.touken + __jiaqian)
        #把sign 复制给sign
        __content['head']['sign'] = __newsign
        #要发送的完整报文
        __conte2 = json.dumps(__content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        __rt = requests.post(self.__url,headers=self.__headers,data=__conte2.encode('utf-8'))
        __rtsj = json.loads(__rt.text)
        print (__rtsj)
    def xun_jia(self):#询价接口
        __content = collections.OrderedDict()
        __head = collections.OrderedDict()
        __apply_content = collections.OrderedDict()



        __content['head'] = __head
        __content["apply_content"]= __apply_content


        __head["proposalFormToken"]=proposalFormToken
        __head["proposalFormId"]="842261679568334521"
        __head["version"]="v1"
        __head["function"]="priceQuote"
        __head["transTime"]="2017-08-24 14:16:00"
        __head["reqMsgId"]=reqMsgId
        __head["sign_type"]=sign_type
        __head["sign"]= ""
        __head["channelId"]="64287"

        __car = collections.OrderedDict()
        __apply_content["car"] = __car
        __car["carModelKey"]="84226167956833452101"
        __car["chgOwnerFlag"]=chgOwnerFlag
        # __car["carOwner"]=carOwner
        # __car["carOwnerIdentifyType"]=carOwnerIdentifyType
        # __car["carOwnerIdentifyNumber"]=carOwnerIdentifyNumber
        __car["transferDate"]= "2017-05-20"
        __car["certificateDateBJ"]="2017-06-20"
        __car["certificateType"]=certificateType
        __car["certificateNo"]=certificateNo


        __apply_content["riskList"] = []
        risk = OrderedDict()

        __apply_content["riskList"].append(risk)
        __check2 = OrderedDict()
        __check2["riskCode"] = "0803"
        __check2["effectStartTime"] = ""
        __check2["effectEndTime"] = ""
        __check2["kindList"] = []
        risk['risk'] = __check2

        __kong = OrderedDict()

        __check2["kindList"].append(__kong)
        __kind = OrderedDict()
        __kind["kindCode"] = "02"
        __kind["amount"] = "200000"
        __kind["quantity"] = "45"
        __kind["unitAmount"] = "12"
        __kind["kindFlag"] = "1"
        __kong["kind"] = __kind


        risk1 = OrderedDict()
        __apply_content["riskList"].append(risk1)
        __check3 = OrderedDict()
        __check3["riskCode"] = "0807"
        __check3["effectStartTime"] = ""
        __check3["effectEndTime"] = ""
        __check3["kindList"] = []
        risk1['risk'] = __check3

        __kong1 = OrderedDict()

        __check3["kindList"].append(__kong1)
        __kind1 = OrderedDict()
        __kind1["kindCode"] = "BZ"
        __kind1["amount"] = "122000"
        __kind1["quantity"] = "45"
        __kind1["unitAmount"] = "12"
        __kind1["kindFlag"] = "0"
        __kong1["kind"] = __kind1





        __apply_content["privyList"] = []
        __privy = OrderedDict()
        __apply_content["privyList"].append(__privy)
        __add3 = OrderedDict()
        __add3["insuredFlag"]="0010000"
        __add3["insuredName"]="刘小六"
        __add3["identifyType"]="01"
        __add3["identifyNumber"]="370283198806208436"
        __add3["mobile"]="17600298249"
        __privy["privy"]=__add3

        '''
        __conte1 = json.dumps(__content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
        '''
        __conte1 = json.dumps(__content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
        print (__conte1[281:-1])
        print (len(__conte1))

        #取sign
        __jiaqian =  (__conte1[268:-1])
        print (__jiaqian)
        print (self.touken + __jiaqian)
        __newsign = md5(self.touken + __jiaqian)
        #把sign 复制给sign
        __content['head']['sign'] = __newsign
        #要发送的完整报文
        __conte2 = json.dumps(__content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        __rt = requests.post(self.__url,headers=self.__headers,data=__conte2.encode('utf-8'))
        __rtsj = json.loads(__rt.text)
        print (__rtsj)
if __name__ == '__main__':
    Car_Insurance = Car_Insurance()
    Car_Insurance.getToken()
    Car_Insurance.chexing_chaxun()
    Car_Insurance.xianbie_chushi()
    Car_Insurance.xun_jia()