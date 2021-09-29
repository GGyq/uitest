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





if __name__ == '__main__':
    print('欢迎使用自动化测试平台'.center(30,'*'))
    print('1-执行测试     2-生成报告'.center(30,"*"))
    serivce=input('请选择服务：')
    if serivce=='1':
        v=input('请输入版本号（Vx.x）：')
        for i in browsers:
            t = threading.Thread(target=run, args=(path, i))
            t.start()

    elif serivce=='2':
        v=input('请输入版本号（Vx.x）:')
        rpath=report_path+f'/{v}'
        make_dir(rpath)
        total,summery_all,summery_module=get_result(v)
        for i in summery_module:
            module_report(v,i,summery_module,rpath)
        summery_report(v,'Mr.Ge',total,summery_all,summery_module,rpath)

    else:
        exit('再见')