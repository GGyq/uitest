from flask import Flask
from flask import jsonify
from flask import request
import make_response

users_info = {
    '1001': ['123456', '张三', 9000],
    '1002': ['123456', '李四', 9000],
    '1003': ['123456', '王五', 9000],
    '1004': ['123456', '赵六', 9000],
    '1005': ['123456', '王老七', 9000]
}
app = Flask(__name__)  # 创建对象




# 编写路由，构建url与函数的映射关系，（将函数与URL绑定）
@app.route('/users', methods=['GET'])
def all_users():
    return jsonify({"code": 1000, "message": "success", "data": users_info})


#
@app.route('/users/account', methods=['GET'])  # 动态路由
def get_users():
    account = request.args.get('account')
    if account:
        if account in users_info:
            info = users_info[account]
            return jsonify({"code": 1000, "message": "success", "data": {"name": info[1], "bannec": info[2]}})
        else:
            return jsonify({"code": 1001, "message": "account does not exist"})
    else:
        return jsonify({"code": 1002, "message": "param is error"})


@app.route('/login', methods=['POST'])  # 设置路由
def login():
    if request.method == 'GET':
        return jsonify({"code": 1001, "message": "method error"})
    else:
        account = request.form.get('account')  # 获取账号
        passwd = request.values.get('password')  # 获取密码
        if account and passwd:
            aql = f
            # 判断账号密码参数是否存在
            if account in users_info:
                info = users_info[account]
                if passwd == info[0]:
                    return jsonify({"code": 1000, "message": "success", "data": {"name": info[1], "bannec": info[2]}})
                else:
                    return jsonify({"code": 1003, "message": "password error"})
            else:
                return jsonify({"code": 1002, "message": "account does not exist"})
        else:
            return jsonify({"code": 1001, "message": "param error"})


if __name__ == '__main__':
    #  app.run()    #以默认方式启动项目
    app.run(host='0.0.0.0', port=5566, debug=True)
# host='0.0.0.0'：表示可以以127.0.0.1，localhost，以及本机IP10.0.0.159去访问
