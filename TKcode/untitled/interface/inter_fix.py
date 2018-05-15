from __future__ import unicode_literals
from collections import OrderedDict
import collections
import time
import  requests
import json
import hashlib

#***连接参数***#
url = "http://10.130.201.180:8082/tk-link/rest"
headers = {"Content-Type":"application/json;charset=UTF-8"}
#***连接参数***#

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
'''
proposalFormToken=""							#交易TOKEN
proposalFormId= ""            					#交易ID
version= ""                                   #版本号
function= ""                       				#接口代码
transTime= ""                #发送时间
reqMsgId= ""                      			#请求报文ID
channelId= ""                              #渠道ID
sign_type= ""                                #加签方式
licenseNo= ""                           	#车牌号
engineNo= ""                         		#发动机号
frameNo= ""                    				#车架号
enrollDate= ""                        #初登日期
newVehicle= ""                                 #新旧车标志
ecdemicVehicle= ""                             #外地车标志
vehicleModel= ""                      			#车辆型号
chgOwnerFlag= ""                               #过户车标识
insuredCode= ""                           	#投保地编码
operateFlag= ""                                #车型查询操作类型
effectStartTime= ""                 		#起保日期
vehicleCode= ""                       		#精友车型编码
vehicleHyCode= ""                   			#行业车型编码
seatCount= ""                                #座位数

#***初始险别初始化数据***#
carModelKey = ""
carOwner = ""
carOwnerIdentifyType = ""
carOwnerIdentifyNumber = ""
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
        self.touken = ""
        self.baowen_ys = "" #拼好的报文
        self.data =""
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

    def baowenpinjie(self,baowenleixing):

        if baowenleixing == "查询":
            #####车型查询接口数据构成#####
            content = collections.OrderedDict()
            head = collections.OrderedDict()
            apply_content = collections.OrderedDict()
            carInfo = collections.OrderedDict()


            __sign = ""
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
            self.baowen_ys = json.dumps(content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
            print (self.baowen_ys)

            #
            # content['head']['sign'] = md5(self.touken + content1[271:-1])
            # self.baowen = content
            # print (self.baowen)
        elif baowenleixing == "初始化":
            content = collections.OrderedDict()
            head = collections.OrderedDict()
            apply_content = collections.OrderedDict()
            cars = collections.OrderedDict()

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
            check1 = OrderedDict()

            apply_content["checks"].append(check1)
            check2 = OrderedDict()
            check2["querySequenceNo"] = ""
            check2["checkCode"] = ""
            check2["checkFlag"] = ""
            check1['check'] = check2

            ###############

            conte1 = json.dumps(content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
            print (conte1)
            print (conte1[281:-1])
            print (len(conte1))

            #取sign
            jiaqian =  (conte1[281:-1])
            print (jiaqian)
            print (self.touken + jiaqian)
            newsign = md5(self.touken + jiaqian)
            #把sign 复制给sign
            content['head']['sign'] = newsign
    def fuzhi(self,key,val): #替换里面的参数

        self.baowen_ys = self.baowen_ys.replace(str(key)+'":""',str(key)+'":"'+str(val)+'"')
        # print (self.baowen_ys)

    def encrypt_bw(self):

        #1,拼好的报文，取apply_conten。后面的加密,加密后的报文用来
        content2 = json.dumps(self.baowen_ys, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',').replace('\\"','"')
        print (";;;")
        print (content2)
        con1 = content2[1:-1]
        #取sign

        jiaqian =  (con1[271:-1])
        print (jiaqian)
        newsign = md5(self.touken + jiaqian)
        print (newsign)
        self.data = self.baowen_ys.replace('"sign":""','"sign":'+'"'+str(newsign)+'"')
        print (self.data)
        # print (self.baowen_ys)
        # self.baowen_ys = self.baowen_ys.replace('"sign":""','"sign":'+'"'+str(newsign)+'"'))
    def sendBaowen(self):

        fhbw = requests.post(url=url,headers=headers,data=self.data.encode('utf-8'))
        print (json.loads(fhbw.text))

    def run(self):
        self.getToken()
        self.baowenpinjie("查询")
        self.fuzhi("proposalFormToken","6596dd59c3b6d7e6673b8bfe1e94371e")
        self.fuzhi("proposalFormId","842261679568330752")
        self.fuzhi("version","01")
        self.fuzhi("function","carModelQuery")
        self.fuzhi("transTime","2017-05-24 00:00:00")
        self.fuzhi("reqMsgId","11111111111111")
        self.fuzhi("channelId","63469")
        self.fuzhi("sign_type","md5")
        self.fuzhi("licenseNo","鲁WS1568")
        self.fuzhi("engineNo","07154830181")
        self.fuzhi("frameNo","LSVFX6188E3457125")
        self.fuzhi("enrollDate","2015-05-11")
        self.fuzhi("newVehicle","0")
        self.fuzhi("ecdemicVehicle","0")
        self.fuzhi("vehicleModel","SVW7183AGi")
        self.fuzhi("chgOwnerFlag","0")
        self.fuzhi("insuredCode","420100")
        self.fuzhi("operateFlag","1")
        self.fuzhi("effectStartTime","201706151640")
        self.fuzhi("vehicleCode","AKCACD0002")
        self.fuzhi("vehicleHyCode","BYQMAMUA0006")
        self.fuzhi("seatCount","5.0")
        self.encrypt_bw()
        self.sendBaowen()
if __name__ == '__main__':
    Car_Insurance().run()
