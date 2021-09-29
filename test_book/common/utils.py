# -*- coding: utf-8 -*-
import os, csv, time, requests,json

# 获取所有的路径
base_path = os.path.dirname(os.path.dirname(__file__))
case_path = os.path.join(base_path, 'case')
data_path = os.path.join(base_path, 'data')
report_path = os.path.join(base_path, 'report')

# 获取当前时间
def get_time():
    t = time.strftime('%Y-%m-%d %x')
    return t

# 读取csv文件的测试用例
def read_csv(file):
    if os.path.exists(file):
        with open(file, 'r', ) as f:
            d = csv.reader(f)
            return list(d)
    else:
        print(f'文件{file},不存在')
        return False

def get_test_data(data_dict):
    dd=json.loads(data_dict)
    return dd

# 请求模块
def request(url, method, data=None, header=None):

    rq = requests.session()
    if method in ('get', 'GET'):
        r = rq.get(url=url, params=data,header=header)
    elif method in ('post', 'POST'):
        r = rq.post(url=url, data=data,header=header)
    else:
        print('暂不支持该请求方式')
        return None
    return r




