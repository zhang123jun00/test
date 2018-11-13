#-*- coding:utf-8
#user zhangjunlei
from UI_ATUO.page.page_login import Page_Login
from UI_ATUO.tool.element import Page
class Business_Login(Page_Login,Page):
    def switch_login(self):
        '''跳转登录页面'''
        self.sleep_little
        self.find(*self.clikc_login_loc()).click()
        self.sleep_little
        self.find(*self.user_login_loc()).click()

    def input_usr(self,usr):
        self.sleep_little
        self.find(*self.username_loc()).send_keys(usr)

    def input_pwd(self,pwd):
        self.sleep_little
        self.find(*self.password_loc()).send_keys(pwd)

    def click_login(self):

        self.find(*self.login_button_loc()).click()
        self.sleep_little
    def login(self,usr,pwd):
        self.switch_login()
        self.input_usr(usr)
        self.input_pwd(pwd)
        self.click_login()
    def error_text(self):
        return self.find(*self.error_text_loc()).text