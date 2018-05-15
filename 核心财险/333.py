import xlrd
from xlutils.copy import copy
import time

excelPath = r'E:\武郁博\1307_行家保险新住院保\1307_行家保险新住院保.xls'
sheetName = "SheetA"
# 从数据表中读取(案例数据)每行数据
# 返回结果写入数据表
def getDataFromSheet(start, end):
    rowList = []
    # 读取excel数据
    data = xlrd.open_workbook(excelPath)
    # 获取一个工作表
    table = data.sheet_by_name(sheetName)
    # 获取工作表的总行数
    nrows = table.nrows
    if nrows:
        for line in range(start, end):
            rowData = table.row_values(line)
            rowList.append(rowData)
            # wb = copy(data)
            # ws = wb.get_sheet(0)
            # ws.write(line, 32, time.ctime())
            # wb.save(excelPath)
        return rowList
    else:
        print("读取数据完毕！")


if __name__ == '__main__':
    print(getDataFromSheet(25,34))
