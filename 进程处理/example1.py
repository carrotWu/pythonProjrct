#coding=utf-8
from selenium import webdriver
from time import sleep
import os
import re
class Process:
    driver=webdriver.Firefox()
    def Gozhihu(self):
        self.driver.get('https://www.baidu.com/')
        sleep(2)
        self.driver.find_element_by_css_selector('input[id="kw"]').send_keys('知乎')
        self.driver.find_element_by_css_selector("#su").click()
        self.driver.find_element_by_css_selector("sadasdasdasda").click()
        sleep(3)
        #self.driver.switch_to_window()
    def kill(self):
        d = os.popen(' tasklist | find "firefox.exe"').read()  # 查询火狐进程
        print(d)
        # re.findall  的简单用法（返回string中所有与pattern相匹配的全部字串，返回形式为数组）
        ss = re.findall('\d*\d', "".join(d.split()).replace(',', ''))  # 查询火狐进程的PID值
        if ss != []:
            try:
                os.system("taskkill /F /pid %d" % int(ss[0]))
            except:
                pass

if __name__ == '__main__':
    try:
        functionLibrary=Process()
        functionLibrary.Gozhihu()
    except:
        #浏览器中操作有异常就杀掉浏览器异常    
        functionLibrary.kill()

