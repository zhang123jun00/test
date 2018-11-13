# -*- coding:utf-8 -*-
#user zhangjunlei
import unittest
import HTMLTestRunner
import os,time
def get_local_dir():
    dir_name = os.path.dirname(os.path.abspath(__file__))
    return dir_name
def get_suite():

    suite = unittest.defaultTestLoader.discover(get_local_dir()+'/test_case/',
                                                pattern='test_*.py',
                                              top_level_dir=None)
    return suite

def getnowtime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def run():
    filname = get_local_dir()+'/ui_report/'+getnowtime()+'test-result.html'
    fb = open(filname,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                           title='测试用例执行',
                                           description='登录自动化测试用例执行')

    runner.run(get_suite())

run()