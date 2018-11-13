# -*- coding:utf-8 -*-
#user zhangjunlei
import xlrd,os
class GetData():
    def get_dir(self):
        '''获取数据地址'''
        data_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dir_list = (os.path.join(data_dir,'data_file'),)
        return "/".join(dir_list)

    def getFile(self,index):
        '''通过索引读取txt文件'''
        with open(self.get_dir()+"/") as f:
            datas = f.readlines()
            return datas[index].strip()

    def getExcel(self,rowvalue,celvalue):
        with xlrd.open_workbook(self.get_dir()+'/;') as e:
            sheet = e.sheet_by_index(0)
            return sheet.cell_value(rowvalue,celvalue)

    def getExcels(self):
        with xlrd.open_workbook(self.get_dir()+'/login.xlsx','wb') as e:
            sheet = e.sheet_by_index(0)
            rows = []
            for row in range(1,sheet.nrows):

                rows.append(list(sheet.row_values(row,0,sheet.ncols)))

            return rows


