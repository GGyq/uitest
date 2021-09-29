"""
页面类，继承页面基类，主要封装与业务流程相关元素的操作方法
"""
from test_woniusales.page.base_page import Base_Page
from selenium.webdriver.common.by import By


class LoginPage(Base_Page):
    username_ele = (By.ID, "username")  # 账号元素
    pwd_ele = (By.ID, "password")  # 密码元素
    code_ele = (By.ID, "verifycode")  # 验证码元素
    login_ele = (By.XPATH, '/html/body/div[4]/div/form/div[6]/button')  # 登录按钮元素
    logout_ele = (By.LINK_TEXT, '注销')

    # 输入账号
    def input_name(self, name_value):
        self.input(name_value, *self.username_ele)

    # 输入密码
    def input_pwd(self, pwd_value):
        self.input(pwd_value, *self.pwd_ele)

    # 输入验证码
    def input_code(self, code_value):
        self.input(code_value, *self.code_ele)

    # 点击登录
    def click_login(self):
        self.click(*self.login_ele)

    def click_logout(self):
        self.click(*self.logout_ele)
