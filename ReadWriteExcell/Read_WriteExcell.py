#coding=utf-8
import xlrd
import time
from xlutils.copy import copy
#Excell路径
excellPath="F:\\pythonProjrct\\Excell1.xls"
#工作表名称
sheetName="Data"
xlutils.copy.copy()

class REC:
    def ReadExcel(self,excellPath,sheetName):
        rowList=[]
        #读取Excell文件数据
        xlsData=xlrd.open_workbook(excellPath)
        #读取指定工作表数据
        table=xlsData.sheet_by_name(sheetName)
        #获取工作表总行数
        nrows=table.nrows
        #遍历行获取每行数据
        if nrows:
            for line in range(nrows):
                rowData=table.row_values(line)
                if rowData[4]=="":
                    rowList.append(rowData)
                    wb=copy(xlsData)
                    ws=wb.get_sheet(0)
                    ws.write(line,4,'1')
                    ws.write(line,5,time.ctime())
                    wb.save(excellPath)
                    break
            if len(rowList)!=0:
                ID=rowList[0][0]
                name=rowList[0][1]
                sex=rowList[0][2]
            return ID,name,sex

    def get_dataFromExcell(self,start,end):
        self.rowList = []
        data = xlrd.open_workbook(excellPath)
        table = data.sheet_by_name(sheetName)
        nRows = table.nrows
        if nRows :
            for line in range(start,end):
                rowData = table.row_values(line)
                self.rowList.append(rowData)
            return self.rowList
        else:
            print("数据读取完毕")

    def write_to_excell(self,row,col,content):
        data = xlrd.open_workbook(excellPath)
        wb = copy(data)
        ws = wb.get_sheet(0)
        ws.write(row,col,content)
        wb.save(excellPath)

if __name__ == '__main__':
    functionLibrary=REC()
    list=functionLibrary.ReadExcel(excellPath,sheetName)
    print (list)