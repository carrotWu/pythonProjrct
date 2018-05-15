#coding=utf-8
import requests
import json

url = 'http://www.xxxxx.com'
data = {'channelCode':'Wap','formID':'3306'}

headers = {
    'content-Type':'application/json;charset=UTF-8',
    'actionType':'00051'
}

rec_txt = requests.post(url,headers=headers,data=json.dumps(data)).text
returnJson = json.load(rec_txt)
print(returnJson)