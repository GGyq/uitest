"""
POM(Page Object Module),实现页面元素与测试用例分离，从而提高代码的可读性，可维护性
页面基类，封装页面上元素操作的相应方法，（实现对webdriver api的二次封装），是所有页面类的父类
"""
from selenium.webdriver.support.select import Select


class Base_Page:
    def __init__(self, driver):
        self.driver = driver

    # 定位单个元素
    def find_element(self, *args):
        try:
            return self.driver.find_element(*args)
        except Exception as e:
            print(e)
            return False

    # 定位一组元素
    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    # 向input输入框输入内容
    def input(self, value, *args):
        ele = self.find_element(*args)
        if ele:
            ele.clear()
            ele.send_keys(value)

    # 点击
    def click(self, *args):
        ele = self.find_element(*args)
        if ele:
            ele.click()

    # 获取标题
    def get_title(self):
        return self.driver.title

    # 获取URL
    def get_url(self):
        return self.driver.currle_url

    # 截图
    def save_img(self, path):
        return self.driver.save_screenshot(path)

    # 警告框——接受确定
    def alert_accept(self):
        self.driver.swtch_to.alert.accept()

    # 警告过——取消
    def alert_dismiss(self):
        self.driver.swtch_to.alert.dismiss()

    # 警告框——输入内容
    def alert_sendkey(self, value):
        self.driver.swtch_to.alert.send_key(value)

    # 下拉框选择内容
    def select_option(self, *args, value):
        ele = self.find_element(*args)
        if ele:
            Select(ele).select_by_value(value)

    # 调用JS
    def execute_js(self, js):
        self.driver.execute_script(js)

    # 切换到指定框架
    def switch_frame(self, *args):
        ele = self.find_element(*args)
        if ele:
            self.driver.swtch_to.frame(ele)

    # 切换到最外层框架
    def switch_default(self):
        self.driver.swtch_to.default_content()
