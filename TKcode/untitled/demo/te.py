import time
from selenium import webdriver
import re
import cx_Oracle,sys
url = "http://10.130.201.36:7001/index.jsp"
tbun = "policy3@upic"                   #投保用户名
heun= "uwprpall@upic"                   #核保用户名
lpun= "0008054"                         #理赔用户
pw = "upic@123"                         #密码
tbname = "凌志保"                        #
id = "142427198001010034"               #
address = "山西省"
postcode = "047500"
tel = "13601234567"
skname = "宫本武藏"                      #收款人
bankname = "中国银行"                    #收款银行
######################

def baoanxinzeng():#报案新增4(ok)
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(url)
    driver.find_element_by_id("username").send_keys(lpun)
    driver.find_element_by_id("password").send_keys(pw)
    driver.find_element_by_id("bt_submit").submit()
    time.sleep(2)
    driver.switch_to_frame("leftFrame")
    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("报案管理").click()
    driver.find_element_by_link_text("报案新增").click()
    driver.switch_to_default_content()
    time.sleep(2)
    driver.switch_to_frame("mainFrame")
    # js = "var q=document.getElementById('tabMain').scrollTop=10000"
    # js = "var q=document.documentElement.scrollTop=10000"
    # js = "window.scrollTo(0,document.body.scrollHeight)"
    # driver.execute_script(js)
    time.sleep(1)
    dr = driver.find_element_by_css_selector("input[value='提交']")
    driver.execute_script("arguments[0].scrollIntoView();",dr)

# abc = "cadi"
# s = '{"head":{"proposalFormToken":"token","proposalFormId":"842261679568330752","version":"01","function":"carModelQuery","transTime":"2017-05-24 00:00:00","reqMsgId":"11111111111111","channelId":"63469","sign_type":"md5","sign":""},"apply_content":{"carInfo":{"licenseNo":"鲁WS1568","engineNo":"07154830181","frameNo":"LSVFX6188E3457125","enrollDate":"2015-05-11","newVehicle":"0","ecdemicVehicle":"0","vehicleModel":"SVW7183AGi","chgOwnerFlag":"0","insuredCode":"420100","operateFlag":"1","effectStartTime":"201706151640","vehicleCode":"AKCACD0002","vehicleHyCode":"BYQMAMUA0006","seatCount":"5.0"}}}'
#
# print (s.replace('"sign":""','"sign":"'+abc+'"'))

# bd = "4564564156"
# print (bd[0:3])

s = '"sign":"","fuck":"sd"'

print (s)
# def re(key,val):
se = "sdfsefwfw"
print(s.replace('"sign":""','"sign":'+'"'+str(se)+'"'))
# re("sign","sing")

        # print(s.replace('"sign":""','"sign":'+'"'+str(se)+'"'))
