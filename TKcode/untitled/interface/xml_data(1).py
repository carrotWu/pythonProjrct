import os
import sys
import pymysql
import logging
import urllib.request as r
import xml.dom.minidom as xd

class scriptError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Interface(object):

    def logSendXml(self):
        self.log("--------------发送报文--------------")
        self.log(self.reqxmlfile.strip().decode("utf8"))

    def logBackXml(self):
        self.log("--------------接收报文--------------")
        self.log(self.esbxml)

    def saveMEM(self, value):
        if value.find("{") == 0 and value.find("}") > 0:
            k_v = value[1:len(value) - 1].split("==")
            memvalue = self.getXmlTagValue(self.esbxml, k_v[1])
            self.mem(k_v[0], memvalue)
        else:
            k_v = value.split("==")
            self.mem(k_v[0], k_v[1])

    def numc(self, num):
        r = 0
        try:
            if num.find("+") > 0:
                n = num.split("+")
                r = int(n[0].strip()) + int(n[1].strip())
            else:
                n = num.split("-")
                r = int(n[0].strip()) - int(n[1].strip())
            self.log("[numc  " + num + " = " + str(r) + "  通过]")
            return str(r)
        except Exception:
            funcName = sys._getframe().f_code.co_name
            self.log("[numc  " + num + " = " + str(r) + "  不通过]")
            raise scriptError(funcName + '----异常')

    def firstMethod(self):
        length = len(self.params)
        self.logConfig()
        if length == 7:
            if ((self.params.get("savemem") == None or self.params.get("savemem") == "")
                and (self.params.get("saveDBname") == None or self.params.get("saveDBname") == "")):
                raise scriptError("参数异常")
            self.sqlSersver()
            self.saveData()
            if self.params.get("savemem") != "true":
                self.close()
        else:
            self.reqxmlfile = self.xmlFile()
            self.esbxml = self.sendXml(self.reqxmlfile)
        self.runFunc()

    def saveData(self):
        sql = "select * from %s where id>=%s and id<=%s" \
              % (self.params.get("tablename"), self.params.get("startindex"), self.params.get("endindex"))
        result = self.select(sql)
        for row in result:
            self.reqxmlfile = self.xmlFile(row[self.params.get("replacename")])
            self.esbxml = self.sendXml(self.reqxmlfile)
            if self.params.get("savemem") != "true":
                saveDBvalue = self.getXmlTagValue(self.esbxml, self.params.get("saveDBname"))
                sql = "update %s set %s='%s' where id=%d" \
                      % (self.params.get("tablename"), self.params.get("saveDBname"), saveDBvalue, row['id'])
                self.execSql(sql)

    def checkValue(self, v1, v2):
        v3 = self.getXmlTagValue(self.esbxml, v2)
        if v1 == v3:
            self.log("[checkValue  " + v1 + " = " + v3 + "  通过]")
        else:
            self.log("[checkValue  " + v1 + " = " + v3 + "  不通过]")
            raise scriptError(v1 + " != " + v3)

    def getXmlTagValue(self, xml, tagname):
        tagvalue = ""
        try:
            dom = xd.parseString(xml)
            name = dom.getElementsByTagName(tagname)[0]
            for textNode in name.childNodes:
                tagvalue = textNode.data
            return tagvalue.strip()
        except Exception:
            raise scriptError("返回报文没有【 %s 】标签"%tagname)

    def sendXml(self, xml):
        try:
            req = r.Request(
                url=self.params.get("httpurl"),
                headers={"Content-type": "application/xml", "charset": "utf-8"},
                data=xml
            )
            resp = r.urlopen(req)
            return resp.read().decode()
        except Exception:
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')

    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception:
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')

    def sqlSersver(self):
        try:
            self.conn = pymysql.connect(
                db='dataserver', host='10.6.91.51', user='ds', passwd='ds',charset="utf8")
            self.cursor = self.conn.cursor()
        except Exception:
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            desc = self.cursor.description
            rows = []
            for cloumn in result:
                row = {}
                for i in range(0, len(cloumn)):
                    row[desc[i][0]] = cloumn[i]
                rows.append(row)
            return rows
        except Exception:
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')

    def execSql(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception:
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----异常')

    def logConfig(self):
        logger = logging.getLogger("pyLogging")
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(self.urlReplace(self.projectPath) + '/' + 'ProcessLog.txt')
        formatter = logging.Formatter('%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        self.loginfo = logger

    def log(self, msg):
        self.loginfo.info(msg)

    def mem(self, memKey, memValue):
        contentMap = {}
        fileName = self.urlReplace(self.projectPath) + '/tempData.txt'
        try:
            if not os.path.exists(fileName):
                self.getFile(fileName, 'wt+')
            file = self.getFile(fileName, 'rt+')
            lines = file.readlines();
            for line in lines:
                key_value = line.strip().split("$-----$")
                contentMap[key_value[0]] = key_value[1]
            if memKey in contentMap:
                del contentMap[memKey]
            file.close()
            if os.path.exists(fileName):
                os.remove(fileName)
            contentMap[memKey] = memValue
            file = self.getFile(fileName, 'wt+')
            for key in contentMap.keys():
                file.write(key + '$-----$' + contentMap[key] + '\n')
            file.close()
        except Exception:
            funcName = sys._getframe().f_code.co_name
            raise scriptError(funcName + '----' + memKey + '--' + memValue + '----异常')

    def getFile(self, filePath, handle):
        file = open(filePath, mode=handle,
                    buffering=1, encoding='gbk', errors=None,
                    newline='\r\n', closefd=True, opener=None)
        return file

    def returnDir(self, fileDir, n):
        fileDir = os.path.abspath(os.path.join(fileDir, os.path.pardir))
        if n == 1:
            return fileDir
        return self.returnDir(fileDir, n - 1)

    def urlReplace(self, grandpa_path):
        return grandpa_path.replace("\\", "/")

    def __init__(self,params):
        self.projectPath = "D:\\JettechAgent\\execute"
        # "savemem":"true"  true用men保存 不用数据库保存
        self.params = params

    def readFile(self,num):
        file=self.getFile("D:\\JettechAgent\\execute\\kahao.txt", 'rt+')
        lines = file.readlines()
        file.close()
        for line in lines:
            num1=line.strip()
            if num1.find(num)==0:
                return num1
        return None

    def CardInfo(self, fileInfo, pingzheng):
        for line in fileInfo:
            # print(lines)
            num1 = line.strip()
            # print(num1)
            if num1.find(pingzheng) == 0:
                num2 = num1.split('|')
                return [num2[0], num2[1]]
        return None
    def GetCardInfo(self,num,array):
        file = self.getFile("D:\\JettechAgent\\GetTagInfo.txt", 'rt+')
        lines = file.readlines()
        f = str(len(lines))
        file.close()
        infoarray = self.CardInfo(lines, num)
        # print(infoarray)
        memKey = infoarray[array]
        return memKey

    def xmlFile(self, replaceValue=""):
        sendxml = '''
            <?xml version='1.0' encoding='UTF-8'?>
            <service package_type='xml'>
            <SYS_HEAD>
            <SvcCd>500130005</SvcCd>
            <SrcSysTmnlNo>12</SrcSysTmnlNo>
            <TranDt>20170331</TranDt>
            <ChnlTp>0</ChnlTp>
            <TranMd>ONLINE</TranMd>
            <CnsmSysId>020102</CnsmSysId>
            <SrcSysId>020102</SrcSysId>
            <CnsmSysSeqNo>20181020020101623477020101623477</CnsmSysSeqNo>
            <TmnlNo>12</TmnlNo>
            <SrcSysSeqNo>020102</SrcSysSeqNo>
            <TranTm>095117319</TranTm>
            <SvcScn>15</SvcScn>
            </SYS_HEAD>
            <APP_HEAD>
            <TlrLvl>6</TlrLvl>
            <AprvFlg>E</AprvFlg>
            <TlrTp></TlrTp>
            <TlrNo>0001693</TlrNo>
            <TlrPswd></TlrPswd>
            <BranchId>27002</BranchId>
            <AuthFlg>0</AuthFlg>
            </APP_HEAD>
            <BODY>
            <BsnNo></BsnNo>
            <Rsrv2></Rsrv2>
            <Rsrv1></Rsrv1>
            <HOprlSeatInd>012</HOprlSeatInd>
            <CoreTxnUUIDNo>02010220170331000000000001357633</CoreTxnUUIDNo>
            <HPblcTxnFlg1>0</HPblcTxnFlg1>
            <CoreTmlTp>0</CoreTmlTp>
            <CoreTxnTpCd>0</CoreTxnTpCd>
            <SeqNo>20181020020101624091</SeqNo>
            <SubBsnKnd></SubBsnKnd>
            <CoreTxnCd>029168</CoreTxnCd>
            <CoreAtmPcsInd></CoreAtmPcsInd>
            <HCntnFlg>0</HCntnFlg>
            <BckFld></BckFld>
            <ProvCd>62</ProvCd>
            <ImprtBlkVchrTp>0302</ImprtBlkVchrTp>
            <ImprtBlkVchrSt>05</ImprtBlkVchrSt>
            <UsrNo>0001693</UsrNo>
            </BODY>
            </service>
        '''
        return sendxml.encode()

    def runFunc(self):
        self.logSendXml()
        self.logBackXml()
        self.log("--------------数据存储及比较--------------")
        self.saveMEM("leixing==0302")
        self.saveMEM("{FileNm==FileNm}")
        self.checkValue("000000", "RetCd")

params = {
    "httpurl": "http://10.6.94.68:38001/cts"
    }

if __name__ == '__main__':
    Interface(params).firstMethod()

