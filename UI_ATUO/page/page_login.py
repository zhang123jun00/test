# -*- coding:utf-8 -*-
#user zhangjunlei
from selenium.webdriver.common.by import By
class Page_Login():
    '''页面的元素'''
    def out_login_button(self):
        out_button = (By.LINK_TEXT,'登录')
        return out_button
    def username(self):
        usrname = (By.ID,'logusername')
        return usrname
    def password(self):
        pwd = (By.ID,'logpassword')
        return pwd
    def inner_login(self):
        inner_button = (By.XPATH,"//a[@class='login-button logReg_btn1']")
        return inner_button

    def get_error(self):
        error = (By.CLASS_NAME,'error-mes')
        return error
