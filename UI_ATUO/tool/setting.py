# -*- coding:utf-8 -*-
#user zhangjunlei
from selenium import webdriver
import unittest,os
from selenium.webdriver.common.action_chains import ActionChains
class Brower(unittest.TestCase):
    '''
    浏览器的初始化
    '''
    def setUp(self):
        driver_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.driver = webdriver.Chrome(driver_dir+'/brower_driver/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(3)
    def tearDown(self):

        self.driver.quit()