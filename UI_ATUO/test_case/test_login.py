#-*- coding:utf-8 -*-
#user zhangjunlei
from UI_ATUO.tool.setting import Brower
from UI_ATUO.tool import read
from UI_ATUO.business.business_login import Business_Login
import unittest,os
from ddt import ddt,data,unpack
@ddt
class Login(Brower,Business_Login):
    '''登陆失败测试'''
    @data(*read.GetData().getExcels())
    @unpack
    def test_001(self,usr,pwd,excpet):
        self.login(usr,pwd)

        self.assertEqual(excpet,self.error_text())

