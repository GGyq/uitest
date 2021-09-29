from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 定位单个元素
    def position(self, *args):
        try:
            return self.driver.find_element(*args)

        except Exception as e:
            print(e)
            return False

    # 定位一组元素
    def positions(self, *args):
        try:
            return self.driver.find_elements(*args)

        except Exception as e:
            print(e)
            return False

    # 输入框输入内容
    def input(self, *args, value):
        ele = self.position(*args)
        if ele:
            ele.clear()
            ele.send_keys(value)

    # 点击
    def click(self, *args):
        ele = self.position(*args)
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

    # 警告框-接受确定
    def alert_accept(self):
        self.driver.swtch_to.alert.accept()

    # 警告框-取消
    def alert_dismiss(self):
        self.driver.swtch_to.alert.dismiss()

    # 警告框-输入内容
    def alert_send(self, value):
        self.driver.swtch_to.alert.send_key(value)

    # 调用JS
    def execute_js(self, js):
        self.driver.execute_script(js)

    # 切换到指定框架
    def switch_frame(self, *args):
        ele = self.position(*args)
        if ele:
            self.driver.switch_to.frame(ele)

    # 切换到最外层框架
    def switch_default(self):
        self.driver.switch_to.default_content()

    # 下拉框选择
    def select_option(self, *args, value):
        ele = self.position(*args)
        if ele:
            Select(ele).select_by_value(value)
