#! usr/bin/env python

import json
import xlwt
import sys

def txt2xls(filename,xlsname):

    wb = xlwt.Workbook()
    ws = wb.add_sheet("sheet1")

    txt = open(filename).read()
    json_txt = json.loads(txt)
    row = 0
    col = 0
    for item in json_txt:
        for number in item:
            ws.write(row,col,number)
            col += 1
        row += 1
        col = 0

    wb.save(xlsname+'.xls')

if __name__ =='__main__':
    filename = sys.argv[1]
    xlsname = sys.argv[2]
    txt2xls(filename,xlsname)