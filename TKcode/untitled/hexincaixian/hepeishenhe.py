
from selenium import webdriver
from selenium.webdriver.support.ui  import Select
import  time
#create by Grape Shi

__url ="http://10.130.201.36:7001/index.jsp"
__un  ="0008054"
__pw = "upic@123"
__baoanhao ="170512234"
__jieanhao =""

#核赔审核待处理任务查询11()

def hepeishenhe():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(__url)
    driver.find_element_by_id("username").send_keys(__un)
    driver.find_element_by_id("password").send_keys(__pw)
    driver.find_element_by_id("bt_submit").submit()
    driver.implicitly_wait(10)
    driver.switch_to_frame("leftFrame")

    driver.find_element_by_link_text("审核平台子系统").click()
    driver.find_element_by_link_text("核赔审核").click()
    driver.find_element_by_link_text("待处理任务查询").click()

    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")

    #报案号
    driver.find_element_by_name('GwWfLogDtoContractNo').send_keys(__baoanhao)

    #点击查询
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[1]/td/input').click()

    #报案号

    driver.switch_to_frame("QueryResultFrame")
    driver.find_element_by_xpath('//*[@id="ResultTable"]/tbody/tr/td[1]/a').click()
    time.sleep(5)
    #选择同意
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    __win1 = driver.current_window_handle
    ser = Select(driver.find_element_by_name('NotionContent'))
    ser.select_by_index(7)
    time.sleep(3)


    #点击审核意见


    driver.find_element_by_name('butViewTranceInfo').click()
    time.sleep(4)
    __allwin = driver.window_handles
    for hand in __allwin:
        if hand != __win1:
            driver.switch_to_window(hand)
            time.sleep(2)
            driver.close()
            driver.switch_to_window(__win1)
    #点击审核通过
    time.sleep(3)
    driver.switch_to_default_content()
    driver.switch_to_frame("mainFrame")
    driver.find_element_by_name('passBtn').click()
    #确定
    time.sleep(2)
    driver.switch_to_alert().accept()

    #确定
    time.sleep(1)
    driver.switch_to_alert().accept()


    #取结案号
    time.sleep(2)
    driver.switch_to_default_content()
    driver.switch_to_frame('mainFrame')
    time.sleep(3)

    __fi = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[1]/tbody/tr[2]/td').text
    print (__fi)
    __jieanhao = __fi[-20::]
    print (__jieanhao)
    driver.quit()
    return  __jieanhao
hepeishenhe()