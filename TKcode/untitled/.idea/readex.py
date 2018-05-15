import xlrd
from xlutils.copy import copy
import time

'''
# 从excel中获取数据
def getDataFromSheet(execlpath,sheet_name):

    data  = xlrd.open_workbook(execlpath)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows

    dataList = []
    for line in range(nrows):
        rowData = table.row_values(line)
        if rowData[3] == 0:
            dataList.append(rowData)
            wb = copy(data)
            ws = wb.get_sheet(0)
            ws.write(line, 3, "1")
            ws.write(line, 4, time.ctime())
            wb.save(execlpath)
            break
    if len(dataList) == 0:
        return "数据读取完毕"
    else:
        indentityId = dataList[0][0]
        name = dataList[0][1]
        sex = dataList[0][2]
        # print (indentityId, name, sex)

        return indentityId, name, sex
'''
# 从excel中获取数据
def getDataFromSheet(self,execlpath,sheet_name):

    data  = xlrd.open_workbook(execlpath)
    table = data.sheet_by_name(sheet_name)
    nrows = table.nrows

    dataList = []
    for line in range(nrows):
        rowData = table.row_values(line)
        if rowData[3] == 0:
            dataList.append(rowData)
            wb = copy(data)
            ws = wb.get_sheet(0)
            ws.write(line, 3, "1")
            ws.write(line, 4, time.ctime())
            wb.save(execlpath)
            break
    if len(dataList) == 0:
        return "数据读取完毕"
    else:
        indentityId = dataList[0][0]
        name = dataList[0][1]
        sex = dataList[0][2]
        return indentityId, name, sex


