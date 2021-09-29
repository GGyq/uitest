from selenium import webdriver
import time, os, csv

# 各个文件目录
url = 'http://localhost:8080/woniusales/'
base_path = os.path.dirname(os.path.dirname(__file__))  # 基础路径
data_path = os.path.join(base_path, 'data')  # 数据目录路径
driver_path = os.path.join(base_path, 'driver')  # driver目录路径
case_path = os.path.join(base_path, 'case')  # 测试用例目录路径
common_path = os.path.join(base_path, 'common')  # 普通类目录路径
img_path = os.path.join(base_path, 'img')  # 截图目录路径
report_path = os.path.join(base_path, 'report')  # 报告目录路径
page_path = os.path.join(base_path, 'page')  # 页面元素目录路径


# 获取时间
def get_time():
    t = time.strftime('%Y-%m-%d %H-%M-%S')
    return t


# 读取CSV文件
def read_csv(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            d = csv.reader(f)
            new_data = list(d)[1:]
            return new_data
    else:
        print('文件不存在')
        return False


# 从读取的csv文件中获取测试数据
def get_test_data(d):
    data = []
    for i in d:
        r = i[3].split()
        indata = [i.split('：')[1] for i in r if len(i.split('：')) == 2]
        indata.append(i[0])
        indata.append(i[4])
        indata.append(i[5])
        indata.append(i[1])
        data.append(indata)
    return data


# 打开浏览器
def open_browser(browser, url):
    '''根据传入不同的浏览器打开不同的浏览器'''
    driver = None
    if browser.lower() in ('chrome', '谷歌'):
        driver = webdriver.Chrome(executable_path=driver_path + '/chromedriver.exe')
    elif browser.lower() in ('firfox', '火狐'):
        driver = webdriver.Firefox(executable_path=driver_path + '/geckodriver.exe')
    else:
        print('暂不支持该浏览器')
        return False
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(30)
    return driver


