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
        print ("###")
        print (content2)
        print ("###")
        sd = requests.post(self.__url,headers=self.__headers,data=content2.encode('utf-8'))
        ad = json.loads(sd.text)
        print (ad)
    def xianbie_chushi(self):#险别初始化接口

        #####数据构成#####
        __content = collections.OrderedDict()
        __head = collections.OrderedDict()
        __apply_content = collections.OrderedDict()
        __cars = collections.OrderedDict()

        __content['head'] = __head
        __content["apply_content"]= __apply_content

        __head["proposalFormToken"]=proposalFormToken
        __head["proposalFormId"]="b938e534dcd749589d3ddf8df675d8fc"
        __head["version"]=version
        __head["function"]="KindsInit"
        __head["transTime"]=transTime
        __head["reqMsgId"]=reqMsgId
        __head["channelId"]="64190"
        __head["sign_type"]=sign_type
        __head["sign"]= ""

        __apply_content["cars"] = __cars
        __cars["carModelKey"]=carModelKey
        __cars["chgOwnerFlag"]=chgOwnerFlag
        __cars["carOwner"]=carOwner
        __cars["carOwnerIdentifyType"]=carOwnerIdentifyType
        __cars["carOwnerIdentifyNumber"]=carOwnerIdentifyNumber
        __cars["transferDate"]= transferDate
        __cars["certificateDateBJ"]=certificateDateBJ
        __cars["certificateType"]=certificateType
        __cars["certificateNo"]=certificateNo



        __apply_content["checks"] = []
        check1 = OrderedDict()

        __apply_content["checks"].append(check1)
        check2 = OrderedDict()
        check2["querySequenceNo"] = ""
        check2["checkCode"] = ""
        check2["checkFlag"] = ""
        check1['check'] = check2

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
    def xiadan(self):#下单报文
        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()

        self.content['head'] = head
        self.content["apply_content"]= apply_content

        head["proposalFormToken"]="26f28f4f82072959421f021cbe2de417"
        head["proposalFormId"]="842261679568334521"
        head["version"]="v1"
        head["function"]="quoteToProposal"
        head["transTime"]="2017-03-05 00:00:00"
        head["reqMsgId"]="11111111111111"
        head["channelId"]="64287"
        head["sign"]= ""
        head["sign_type"]="md5"

        apply_content["privyList"] = []
        privy = OrderedDict()

        apply_content["privyList"].append(privy)
        check2 = OrderedDict()
        check2["insuredFlag"] = "1000000"
        check2["insuredName"] = "刘小六"
        check2["identifyType"] = "01"
        check2["identifyNumber"] = "370283198806208436"
        check2["mobile"] = "17600298249"
        check2["carinsureDrelation"] = "01"
        check2["email"] = "153688@qq.com"
        check2["nation"] = "汉"
        check2["issuer"] = "河南省太康县"
        check2["certiStartDate"] = "2000-09-04"
        check2["certiEndDate"] = "2020-09-04"
        check2["sex"] = "1"
        check2["birthDate"] = "1988-06-20"
        privy['privy'] = check2


        privy1 = OrderedDict()
        apply_content["privyList"].append(privy1)
        check3 = OrderedDict()
        check3["insuredFlag"] = "0100000"
        check3["insuredName"] = "刘小六"
        check3["identifyType"] = "01"
        check3["identifyNumber"] = "370283198806208436"
        check3["mobile"] = "17600298249"
        check3["carinsureDrelation"] = "01"
        check3["email"] = "153688@qq.com"
        check3["nation"] = "汉"
        check3["issuer"] = "河南省太康县"
        check3["certiStartDate"] = "2000-09-04"
        check3["certiEndDate"] = "2020-09-04"
        check3["sex"] = "1"
        check3["birthDate"] = "1988-06-20"
        privy1['privy'] = check3

        privy2 = OrderedDict()
        apply_content["privyList"].append(privy2)
        check4 = OrderedDict()
        check4["insuredFlag"] = "0010000"
        check4["insuredName"] = "刘小六"
        check4["identifyType"] = "01"
        check4["identifyNumber"] = "370283198806208436"
        check4["mobile"] = "17600298249"
        check4["carinsureDrelation"] = "01"
        check4["email"] = "153688@qq.com"
        check4["nation"] = "汉"
        check4["issuer"] = "河南省太康县"
        check4["certiStartDate"] = "2000-09-04"
        check4["certiEndDate"] = "2020-09-04"
        check4["sex"] = "1"
        check4["birthDate"] = "1988-06-20"
        privy2['privy'] = check4


        courierInfo =OrderedDict()
        apply_content["courierInfo"] = courierInfo
        courierInfo["contacts"] = "张散"
        courierInfo["phoneNumber"] = "18612179128"
        courierInfo["adress"] = "北京市海淀区西二旗"

        apply_content["quotationNoBI"] = "QBI010400000000128367"
        apply_content["quotationNoCI"] = "QCI010400000000128368"
        __conte1 = json.dumps(self.content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
    def yanzhengma(self):
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
        __conte1 = json.dumps(self.content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
    def zhifubaojiekou(self):
        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()

        self.content['head'] = head
        self.content["apply_content"]= apply_content

        head["proposalFormToken"]="e145c7b815fabe96232694e2939fb499"
        head["proposalFormId"]="8433224929236418561"
        head["version"]="v1"
        head["function"]="SPtoGetPayUrl"
        head["transTime"]="2017-03-05 00:00:00"
        head["reqMsgId"]="11111111111111"
        head["channelId"]="64191"
        apply_content["jsondata"] = "FT18qOR4TnGNY%2BnlqbEw7cjVHkQGIg%2FCAapQv8epLzIGyHtc7H4k7t%2Bn1wWZAqiiWDufDRlnaFbx%0D%0AOSXGp2GgorKYWgr9ljqkzF%2FuFaA9PqHT%2B6h%2BYUzs94ZymWSkw7DZJn%2FcgtDRORrumfrnMfevtmZk%0D%0AwXfZQfZH9nq2nxPPsp7MW3gM91LK32yasppm5hrdy8B2c%2ByymrXCQdjmcPqmpidzy3orIBU9Ette%0D%0A8qHP7r%2FU1ER3VxlximBUBUku%2BKdL%2Bqatbj7kK3TKjZFplLREXMLtC45Apzj4xte3FK8ZQ2bWtJkC%0D%0AQrlrV8KMi1vHSkDg"

        __conte1 = json.dumps(self.content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
    def weixinjiekou(self):
        self.content = collections.OrderedDict()
        head = collections.OrderedDict()
        apply_content = collections.OrderedDict()

        self.content['head'] = head
        self.content["apply_content"]= apply_content

        head["proposalFormToken"]="e145c7b815fabe96232694e2939fb499"
        head["proposalFormId"]="843322492923641856"
        head["version"]="v1"
        head["function"]="SPpayByWap"
        head["transTime"]="2017-03-05 00:00:00"
        head["reqMsgId"]="11111111111111"
        head["channelId"]="64191"

        apply_content["jsondata"] ="FT18qOR4TnEx9bkyKbWkbNjomgKlM5M8ift5zM9gMHV4H00MpOfYDVSWss8dUw0iJt5MBu%2FqDorQ%0D%0AOmc63CfdJVNo9bImCTL5PSM1Zb8ZONV78zbasSjgPL204ZvD7SJhKZR%2FksR6TQvNhKQVwI6lL110%0D%0AVXembrP1654HnUcPgwHHG4UqiOmhhTVdcojuq4UAZerVqRLlASy%2FpL8E0lO6kYy4pu7jJsdWU2j1%0D%0AsiYJMvk9IzVlvxk41XvzNtqxKOA8vbThm8PtImEplH%2BSxHpNC82EpBXAjqUvXXRVd6Zus%2FXrnged%0D%0ARw%2BDAccbhSqI6aGFNV1yiO6rhQBl6tWpEuUBLL%2BkvwTSU7qRzWfw5WEheBZInoqRwbPgf%2BPJGiMi%0D%0A4IiVF5QNE06mNY9K9PAQIWaTfi%2FWvAc1hzgPDsINEzg%2FXJeD4rei0un0SQwywoJ7JK3CMingQiev%0D%0AXmvALZeSE%2BmaVZCH2L7SoEwcyiQ1RPuvC%2BPV%2Fl9FqP%2B2yRY6AzOqpORYqJXAqwGrRLtx6obIcEfG%0D%0AshOt8xWUiAuM0eRLD49ue%2FpHOB5QfR5eJ8qODFTA0bVp"
        __conte1 = json.dumps(self.content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
    def querenchudan(self):
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
        __conte1 = json.dumps(self.content, ensure_ascii=False,sort_keys=False).replace(': ',':').replace(', ',',')
        print (__conte1)
if __name__ == '__main__':
    Car_Insurance = Car_Insurance()
    # Car_Insurance.chexing_chaxun()
    # Car_Insurance.xianbie_chushi()
    # Car_Insurance.xiadan()
    # Car_Insurance.xun_jia()
    # Car_Insurance.yanzhengma()
    # Car_Insurance.zhifubaojiekou()
    # Car_Insurance.weixinjiekou()
    Car_Insurance.querenchudan()