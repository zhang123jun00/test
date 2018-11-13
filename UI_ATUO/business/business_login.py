#-*- coding:utf-8
#user zhangjunlei
from page.page_login import Page_Login
from base_fuction.page import Page
class Business_Login(Page_Login,Page):
    def send_use(self,usr):
        self.sleep_little
        self.find(*self.username()).send_keys(usr)

    def send_pwd(self,pwd):
        self.sleep_little
        self.find(*self.password()).send_keys(pwd)

    def click_out_login(self):
        self.sleep_little
        self.find(*self.out_login_button()).click()

    def click_inner_login(self):
        self.sleep_little
        self.find(*self.inner_login()).click()
    def get_error_text(self):
        self.sleep_little
        return self.find(*self.get_error()).text

    def login(self,usr,pwd):
        self.click_out_login()
        self.send_use(usr)
        self.send_pwd(pwd)
        self.click_inner_login()