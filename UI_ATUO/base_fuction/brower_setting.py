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
        self.driver.get('https://www.wdzj.com/')
        self.driver.implicitly_wait(3)

    def test_001(self):
        import time
        time.sleep(2)
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(2)
        self.driver.find_element_by_id('logusername').send_keys('1')
        time.sleep(2)
        self.driver.find_element_by_id('logpassword').send_keys('2')
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='login-button logReg_btn1']").click()
        time.sleep(10)
    def test_002(self):
        a = self.driver.find_element_by_xpath("//a[@class='login-button logReg_btn1']")
        ActionChains(self.driver).move_to_element(a).perform()
        ActionChains(self.driver).click_and_hold(a)


    def tearDown(self):

        self.driver.quit()