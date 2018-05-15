
import  re
s='{"apply_content":{"carInfo":{"chgOwnerFlag":"0","ecdemicVehicle":"0","effectStartTime":"201706151640","engineNo":"07154830181","enrollDate":"2015-05-11","frameNo":"LSVFX6188E3457125","insuredCode":"420100","licenseNo":"鲁WS1568","newVehicle":"0","operateFlag":"1","seatCount":"5.0","vehicleCode":"AKCACD0002","vehicleHyCode":"BYQMAMUA0006","vehicleModel":"SVW7183AGi"}},"head":{"channelId":"63469","function":"carModelQuery","proposalFormId":"842261679568330752","proposalFormToken":"6596dd59c3b6d7e6673b8bfe1e94371e","reqMsgId":"11111111111111","sign":"","sign_type":"md5","transTime":"2017-05-24 00:00:00","version":"01"}}'

print (s)
# sd = (re.findall(r'apply_content":(.+?),',s))非贪婪模式
sd = (re.findall(r'apply_content":(.*}}),',s))#贪婪模式
# print (type(re.findall(r'apply_content":(.+?)}',s)))

str = ''.join(sd)
print (str)