#coding=utf-8
#解析TXT文件
import json
#TXT文件目录
txtFile="F:\\pythonProjrct\\stu_info.txt"
class TXT:
    def readTxt(self,txtFile):
        #找到打开txt文件
        f=open(txtFile,'r')
        #逐行读取TXT内容存入数组
        linesList=f.readlines()
        print(linesList)
        strJson='  '
        if linesList:
            strJson=linesList[0]
            print (strJson)
            #将json字符串转化为Json对象
            jsonData=json.loads(strJson)
            print (jsonData['fullname'])#json字典格式对象的取值
            jsonData['fullname']='Jack Spack'#赋值
            print (jsonData['full name'])
            print (jsonData['telephones'][0]['value'])#嵌套字典取值
        else:
            print("文本内无数据")

    def read_text(self,f_name):
        with open(f_name,'r',encoding='utf8') as f_obj:
            mess_txt=f_obj.read()
        return mess_txt

    def write_txt(self,f_name,content):
        with open(f_name,'w',encoding='utf8') as f_obj:
            f_obj.write(content)

if __name__ == '__main__':
    TXT().readTxt(txtFile)