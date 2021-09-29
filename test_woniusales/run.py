from test_woniusales.common.utils import *
from test_woniusales.case.test_login import Test_Login
from test_woniusales.case.test_add_page import Test_Add_Page
import threading, os

path = f'{img_path}/{get_time()}'
make_dir(path)
files = os.listdir(data_path)


def run(path, b):
    for i in files:
        data = read_csv(f'{data_path}/{i}')
        if data[0][1] == "login":
            obj = Test_Login(path)

        elif data[0][1] == "add_page":
            obj = Test_Add_Page(path)

        obj.test(b)


for i in browsers:
    t = threading.Thread(target=run, args=(path, i))
    t.start()


