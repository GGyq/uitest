from selenium import webdriver
from test_woniusales.common.con_db import Con_DB
import os, csv, time

# 各目录路径
browsers = ['chrome', 'firfox']
url = 'http://localhost:8080/woniusales/'
base_path = os.path.dirname(os.path.dirname(__file__))
case_path = os.path.join(base_path, 'case')
common_path = os.path.join(base_path, 'common')
data_path = os.path.join(base_path, 'data')
driver_path = os.path.join(base_path, 'driver')
img_path = os.path.join(base_path, 'img')
page_path = os.path.join(base_path, 'page')
report_path = os.path.join(base_path, 'report')
cd = Con_DB('root', '123456', 'testresult')
cd_cont = cd.con_db()


# 获取当前时间
def get_time():
    t = time.strftime('%Y-%m-%d %H-%M-%S')
    return t


# 创建目录
def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


# 读取测试用例CSV文件
def read_csv(file):
    if os.path.exists(file):
        with open(file, 'r')as f:
            d = csv.reader(f)
            new_data = list(d)[1:]
            return new_data
    else:
        print(f'文件{file}不存在')
        return False


# 获取测试数据
def get_test_data(s):
    data = []
    for i in s:
        r = i[3].split()
        data1 = [i.split('：')[1] for i in r if len(i.split('：')) == 2]
        data1.append(i[0])
        data1.append(i[4])
        data1.append(i[5])
        data1.append(i[1])
        data.append(data1)
    return data


# 打开浏览器
def open_browser(browser, url):
    """根据传入不同的浏览器名称，打开对应的浏览器"""
    driver = None
    if browser.lower() in ('chrome', '谷歌'):
        driver = webdriver.Chrome(executable_path=driver_path + '/chromedriver')
    elif browser.lower() in ('firfox', '火狐'):
        driver = webdriver.Firefox(executable_path=driver_path + '/geckodriver')
    elif browser.lower() in ('edge'):
        driver = webdriver.Edge(executable_path=driver_path + '/msedgedriver')
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(30)
    return driver

# 获取报告
def get_result(version):
    sql=f'select * from test_result where version="{version}"'
    res=cd.query_all(sql)
    total=len(res)
    summery_all={'Pass':0,'Fail':0,'Skip':0}   # 通过数，失败数，跳过数
    summery_module={}   # 每个模块用例数，通过数，失败数，跳过数
    for i in res:
        summery_all[i[4]]+=1
        if i[1] in summery_module:
            summery_module[i[1]]['Total']+=1
        else:
            summery_module[i[1]]={}
            summery_module[i[1]]['Total']=1
            summery_module[i[1]].update({'Pass':0,'Fail':0,'Skip':0})  # 字典的update方法，把另一个字典添加到这个字典中

        summery_module[i[1]][i[4]]+=1

    return total,summery_all,summery_module


# 编辑测试报告页
def summery_report(v,t,total,summery_all,summery_module,path):
    '''
    生成报告，用例统计，分模块的用例统计
    :param v: 版本号
    :param t: 测试人员
    :param total: 用例总数
    :param summery_all: 概要统计
    :param summery_module: 分模块的概要统计
    :param path: 保存报告路径
    :return:
    '''
    file=report_path+'/result_demo.html'
    s=None
    with open(file,'r',encoding='utf8') as f:
        s=f.read()
        s=s.replace('&version',v)    # 版本号
        s=s.replace('&data',get_time())  # 测试时间
        s=s.replace('&tester',t)  # 测试人员
        s=s.replace('&total',str(total))  # 用例总数
        s=s.replace('&pass',str(summery_all['Pass']))  # 通过数
        s=s.replace('&fail', str(summery_all['Fail']))   # 失败数
        s=s.replace('&skip', str(summery_all['Skip']))   # 跳过数
        r=f"{100*summery_all['Pass']/total:.2f}%"    # 通过率
        s=s.replace('&rate',r)     # 模块的统计
        detail=''
        n=1
        for i in summery_module:
            tmp=f'''
            <tr>
                <td class="bottom" width="100">{n}</td>
                <td class="bottom">{i}</td>
                <td class="bottom">{summery_module[i]['Total']}</td>
                <td class="bottom">{summery_module[i]['Pass']}</td>
                <td class="bottom">
                    <a href="{i}.html" style="color:red;">{summery_module[i]['Fail']}</a>
                </td>
                <td class="bottom">{summery_module[i]['Skip']}</td>
            </tr>
            '''
            n+=1
            detail+=tmp
        s=s.replace('&detail',detail)

    with open(path+'/summery.html','w',encoding='utf8') as f:
        f.write(s)



def module_report(v,module,summery_module,path):
    '''
    生成指定模块的报告
    :param v:     # 版本号
    :param module:    # 模块名
    :param summery_module:   # 模块用例统计
    :param path:      # 保存报告的路径
    :return:
    '''
    file = report_path + '/module_demo.html'
    s = None
    module_info=summery_module[module]  # 获取模块的信息
    with open(file, 'r', encoding='utf8') as f:
        s = f.read()
        s = s.replace('&module', module)  # 模块名
        s = s.replace('&total', str(module_info['Total']))  # 用例数
        s = s.replace('&pass', str(module_info['Pass']))  # 通过数
        s = s.replace('&fail', str(module_info['Fail']))  # 失败数
        s = s.replace('&skip', str(module_info['Skip']))  # 跳过数
        sql=f'select * from test_result where version="{v}" and module="{module}"'
        res=cd.query_all(sql)
        detail=''
        for i,j in enumerate(res):
            tmp=f'''<tr><td class="bottom">{i+1}</td>
                <td class="case">{j[2]}</td>
                <td class="bottom">{j[1]}</td>
                <td class="case">{j[3]}</td>
                <td class="bottom">{j[4]}</td>
            </tr>'''
            detail+=tmp
        s=s.replace('&detail',detail)
    with open(path+f'/{module}.html','w',encoding='utf8') as f:
        f.write(s)


if __name__ == '__main__':
    total,summery_all,summery_module=get_result('V1.1')
    rpath = report_path + '/V1.1'
    make_dir(rpath)
    r=module_report('V1.1','login',summery_module,rpath)


