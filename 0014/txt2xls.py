#! usr/bin/env python

import json
import xlwt
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

def txt2xls(filename,xlsname):

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("sheet1")

    txt = open(filename).read()
    json_txt = json.loads(txt)
    row = 0
    col = 0
    for k,v in json_txt.iteritems():
        ws.write(row,col,k)
        for item in v:
            col += 1
            ws.write(row,col,item)
        col = 0
        row += 1

    wb.save(xlsname+'.xls')

if __name__ =='__main__':
    filename = sys.argv[1]
    xlsname = sys.argv[2]
    txt2xls(filename,xlsname)