import pytest
from test_book.common.utils import *

data = read_csv(data_path + '/test_login.csv')


@pytest.mark.skipif(data[5][1] != 'Y', reason='该版本测试用例不用测试，跳过该测试用例')
@pytest.mark.parametrize("case", data[7:])
def test_login(case):
    url = data[1][1]
    method = data[2][1]
    dd = get_test_data(case[1])
    r = request(url=url, method=method, data=dd)
    print(r.json())
    assert int(case[2]) == r.json()['code']  # 断言状态码
    assert case[3] == r.json()['message']  # 断言响应信息


