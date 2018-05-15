
import  sys
import os ,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui  import Select

#create by Grape Shi
__url ="http://10.130.201.36:7001/index.jsp"
__un  ="0008054"
__pw = "upic@123"
__baoanhao ="170512234"
__lisuan = ""

#理算新增9(ok)
def lisuanxinzeng():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    time.sleep(3)
    driver.switch_to_frame("leftFrame")

    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("理算管理").click()
    driver.find_element_by_link_text("理算新增").click()

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")
    driver.implicitly_wait(5)

    #报案号码
    driver.find_element_by_name('queryClaimRegistNo').send_keys(__baoanhao)

    #查询
    driver.find_elements_by_css_selector('input[value="查询"]')[1].click()

    #点击报案号码
    driver.switch_to_frame('QueryResultFrame')
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
    time.sleep(2)

    #点击确定
    driver.switch_to_alert().accept()

    driver.switch_to_default_content()
    driver.implicitly_wait(5)
    driver.switch_to_frame("mainFrame")
    driver.implicitly_wait(5)


    #交易特征--经识别未发现
    jiaoyitezheng = Select(driver.find_element_by_name('adjustmentMainSuspiciousInd'))
    jiaoyitezheng.select_by_index(4)
    time.sleep(5)

    #赔付信息点击
    driver.find_elements_by_tag_name('NOBR')[1].click()

    #理算计算过程
    driver.find_element_by_id('contextImg45').click()

    #生成计算书
    driver.find_element_by_css_selector('input[value="生成计算书"]').click()

    #提交
    driver.find_element_by_css_selector('input[value="提交"]').click()
    time.sleep(3)

    driver.switch_to_alert().accept()

    #理算号码

    #操作成功！
    time.sleep(4)
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    te = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
    __lisuan = te[0:4]
    print (__lisuan)

    '''
    #理算号码
    lisuanhao = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[3]/td/text()').text
    print (lisuanhao)
    '''
    driver.quit()
    return __lisuan
lisuanxinzeng()

###
#操作成功！
#理算号码：12330111282017000001序号：001 操作成功，下一步请做支付录入！
###