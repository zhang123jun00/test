# -*- coding:utf-8 -*-
#user zhangjunlei
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
class Page():
    '''
    封装定位元素的方法
    '''
    def __init__(self,driver):
        self.driver = driver
    def find(self,*args):
        try:
            return self.driver.find_element(*args)
        except(NoSuchElementException,KeyError,ValueError,Exception) as f:
            print("ERROR DETAIL:%s"%(f.args[0]))

    def finds(self,*args):
        try:
            return self.driver.find_elements(*args)
        except(NoSuchElementException, KeyError, ValueError, Exception) as f:
            print("ERROR DETAIL:%s" % (f.args[0]))
    @property
    def sleep_little(self):
        time.sleep(2)

    def action(self,*loc):
        return ActionChains(self.driver).perform()
