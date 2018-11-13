# -*- coding:utf-8 -*-
#user zhangjunlei
import xlrd,os
class GetData():
    def get_dir(self):
        data_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return data_dir
    def getFile(self,index):
        with open(self.get_dir()+'/data_file/') as f:
            datas = f.readlines()
            return datas[index]

    def getExcel(self,rowvalue,celvalue):
        with xlrd.open_workbook(self.get_dir()+'/data_file/') as e:
            sheet = e.sheet_by_index(0)
            return sheet.cell_value(rowvalue,celvalue)

    def getExcels(self):
        with xlrd.open_workbook(self.get_dir()+'/data_file/login.xlsx','wb') as e:
            sheet = e.sheet_by_index(0)
            rows = []
            for row in range(1,sheet.nrows):

                rows.append(list(sheet.row_values(row,0,sheet.ncols)))

            return rows

