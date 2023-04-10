from flask import Blueprint, request, render_template, make_response, url_for, jsonify

login_opt = Blueprint('login_opt', __name__)


@login_opt.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    elif request.method == 'POST':
        form = request.json
        if form.get('username') == 'zhangsan' and form.get('password') == '123456':
            response = make_response()
            response.headers['REDIRECT'] = 'REDIRECT'
            response.headers['CONTENTPATH'] = url_for('enterprise_opt.home')
            # 设置cookie认证
            # response.set_cookie('username', 'zhangsan', max_age = 3600)
            response.set_cookie('username', 'zhangsan')
            return response
        else:
            data = {
                'code': 200,
                'msg': '用户或密码错误'
            }
            return jsonify(data)
