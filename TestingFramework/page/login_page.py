from selenium.webdriver.common.by import By
from TestingFramework.page.base_page import BasePage


class LoginPage(BasePage):
    username_ele = (By.ID, "username")  # 账号元素
    pwd_ele = (By.ID, "password")  # 密码元素
    code_ele = (By.ID, "verifycode")  # 验证码元素
    login_ele = (By.XPATH, '/html/body/div[4]/div/form/div[6]/button')  # 登录按钮元素
    logout_ele = (By.LINK_TEXT, '注销')

    # 输入账号
    def input_username(self, username_value):
        self.input(username_value, *self.username_ele)

    # 输入密码
    def input_password(self, password_value):
        self.input(password_value, *self.pwd_ele)

    # 输入验证码
    def input_code(self, code_value):
        self.input(code_value, *self.code_ele)

    # 点击登录按钮
    def click_login(self):
        self.input(*self.login_ele)

    # 点击注销按钮
    def click_logout(self):
        self.input(*self.logout_ele)



