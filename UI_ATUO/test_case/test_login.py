#-*- coding:utf-8 -*-
#user zhangjunlei
from base_fuction.brower_setting import Brower
from base_fuction import read_file
from business.business_login import Business_Login
import unittest,os
from ddt import ddt,data,unpack
@ddt
class Login(Brower,Business_Login):
    '''登陆失败测试'''
    @data(*read_file.GetData().getExcels())
    @unpack
    def test_001(self,usr,pwd,result):
        self.login(usr,pwd)
        print(self.get_error_text())
        self.assertEqual(result,self.get_error_text())

