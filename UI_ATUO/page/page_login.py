# -*- coding:utf-8 -*-
#user zhangjunlei
from selenium.webdriver.common.by import By
class Page_Login():
    '''页面的元素'''
    def clikc_login_loc(self):
        '''登录'''
        return (By.LINK_TEXT,'登录')
    def user_login_loc(self):
        return (By.ID,"TANGRAM__PSP_10__footerULoginBtn")

    def username_loc(self):
        return (By.ID,'TANGRAM__PSP_10__userName')

    def password_loc(self):
        return (By.ID,"TANGRAM__PSP_10__password")

    def login_button_loc(self):
        return (By.ID,"TANGRAM__PSP_10__submit")

    def error_text_loc(self):
        return (By.ID,"TANGRAM__PSP_10__error")


