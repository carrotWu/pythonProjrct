
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
# __lisuanhao = "12330111282017000001"
__skname = "宫本武藏" #收款人
__yinhangmingcheng = "中国银行" #账户名称
__tel = "13901234567"
__id = "140423198001010010"
__retext = ""

#支付录入10(ok)
def zhifuluru():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    time.sleep(3)
    driver.switch_to_frame("leftFrame")

    driver.find_element_by_link_text("理赔子系统").click()
    driver.find_element_by_link_text("单证收集管理").click()
    driver.find_element_by_link_text("支付录入").click()

    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")


    #报案号码
    driver.find_element_by_name('queryAdjustmentRegistNo').send_keys(__baoanhao)

    #查询
    driver.find_elements_by_css_selector('input[value="查询"]')[1].click()
    #点击报案号码
    driver.switch_to_frame('QueryResultFrame')
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()


    #alert
    time.sleep(3)
    driver.switch_to_alert().accept()

    #赔付信息点击
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    driver.find_elements_by_tag_name('NOBR')[1].click()

    #收款人姓名
    # nm = 'var p p= document.getElementByN'
    driver.find_elements_by_name('adjustmentFeePayeeView')[1].send_keys(__skname)

    #银行名称
    driver.find_elements_by_name('adjustmentFeePayeeBankAccountNameView')[1].send_keys(__yinhangmingcheng)

    #支付机构
    js3 = 'var q = document.getElementsByName("adjustmentFeePaymentComNameView");q[1].value = "01";'
    driver.execute_script(js3)

    #
    driver.find_elements_by_name('imgShowFeeDetail')[1].click()

    # driver.find_elements_by_name('adjustmentFeePayee')[1].send_keys("156")

    #支付机构
    zfjg = driver.find_elements_by_name('adjustmentFeePaymentComCode')[1]
    ActionChains(driver).double_click(zfjg).perform()
    zfjg.send_keys(Keys.ENTER)
    zfjg.send_keys(Keys.ENTER)

    #联系人电话
    lxdh = driver.find_elements_by_name('adjustmentFeePayeeMobile')[1]
    lxdh.send_keys(__tel)

    #证件号码
    zjhm = driver.find_elements_by_name('adjustmentFeeIdNo')[1]
    zjhm.send_keys(__id)

    #确定
    driver.find_elements_by_css_selector('input[value="确定"]')[2].click()

    #提交
    driver.find_element_by_css_selector('input[value="提交"]').click()

    #
    time.sleep(2)
    driver.switch_to_alert().accept()


    #取值
    driver.switch_to_default_content()
    driver.switch_to_frame('mainFrame')
    time.sleep(4)
    __fi = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
    __retext = __fi[0:4]
    print (__retext)
    driver.quit()
    return (__retext)

zhifuluru()

###########
#操作成功！
#该案需提交核赔专员一级核赔审核!理算号码：12330111282017000001序号：001提交双核成功
###########