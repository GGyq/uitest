from test_woniusales.common.utils import *
import threading, os, sys

path = f'{img_path}/{get_time()}'
make_dir(path)
files = os.listdir(data_path)


def run(path, b):
    for i in files:
        data = read_csv(f'{data_path}/{i}')
        __import__(f'test_woniusales.case.test_{data[0][1]}')   # 动态导包
        m = sys.modules[f'test_woniusales.case.test_{data[0][1]}']  # 将导入的模块加载到内存中
        t = f'test_{data[0][1]}'.title()   #将字符中每个字母的首个字符变大写
        if hasattr(m, t):
            tc = getattr(m, t)   # 在导入的模块中获取测试类
            obj = tc(path)
            obj.test(b)


for i in browsers:
    t = threading.Thread(target=run, args=(path, i))
    t.start()
