from TestingFramework.common.utils import *
from TestingFramework.page.login_page import LoginPage
from TestingFramework.page.base_page import BasePage


class TestLogin:
    def __init__(self, path):
        self.file = data_path + '/wn_login.csv'
        self.rdata = read_csv(self.file)
        self.driver = None
        self.img_path_in = path

    def login(self, b, n, p, c):
        """
        登录方法
        :param n：账号
        :param p：密码
        :param c：验证码
        :param b：浏览器
        :return：浏览器对象
        """
        if not self.driver:
            self.driver = open_browser(b, url)
        self.lp = LoginPage(self.driver)
        self.basePage = BasePage(self.driver)
        self.lp.input_name(n)
        self.lp.input_pwd(p)
        self.lp.input_code(c)
        self.lp.click_login()
        return self.driver

    def test(self):
        data=get_test_data()

