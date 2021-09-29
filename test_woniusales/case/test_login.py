from test_woniusales.common.utils import *
from test_woniusales.page.login_page import LoginPage
from test_woniusales.page.base_page import Base_Page



class Test_Login:
    url = 'http://localhost:8080/woniusales/'

    def __init__(self, path):
        file = data_path + '/wn_login.csv'
        self.rdata = read_csv(file)
        self.driver = None
        self.img_path_in = path

    def login(self, n, p, c, b):
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
        self.basePage = Base_Page(self.driver)
        self.lp.input_name(n)
        self.lp.input_pwd(p)
        self.lp.input_code(c)
        self.lp.click_login()
        return self.driver

    def test(self, b):
        data = get_test_data(self.rdata)
        for i in data:
            result = 'Pass'

            if i[5] in 'Y':
                self.login(i[0], i[1], i[2], b)
                if i[4] == 'login success':  # 登录成功的用例断言
                    try:
                        assert '注销' in self.driver.page_source  # 断言元素是否在页面中
                        assert i[0] in self.driver.page_source
                    except Exception:
                        self.basePage.save_img(f'{self.img_path_in}/{i[3]}.png')
                        result = 'Fail'
                    finally:
                        self.driver.quit()
                        self.driver = None

                else:  # 登录失败的用例断言
                    try:
                        assert '首页' in self.driver.title  # 断言页面标题包含首页
                    except Exception:
                        self.basePage.save_img(f'{self.img_path_in}/{i[3]}.png')
                        result = 'Fail'
                    finally:
                        self.driver.refresh()
            else:
                result = 'skip'

            sql = [f'''insert into test_result(module,cases,datas,result,run_time,type,version,browser) 
            values ("{i[6]}","{i[3]}","{i[0:3]}","{result}","{get_time()}","UI","V1.1","{b}");''']
            cd.dml(sql)
            print(f'{b}--{i[3]}--{result}', end='\n')

        self.driver.quit()
