from flask import Flask, url_for
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_cors import CORS

from exts import db, ma
from views import student_opt, enterprise_opt, login_opt

app = Flask(__name__, template_folder='./templates')
app.config.from_pyfile('config.py')
db.init_app(app)
ma.init_app(app)
csrf = CSRFProtect(app)
app.secret_key = '123456'
# 开启全局跨域
CORS(app, supports_credentials=True)

# 注册蓝图
app.register_blueprint(student_opt.student_opt, url_prefix='/student')
app.register_blueprint(enterprise_opt.enterprise_opt, url_prefix='/enterprise')
app.register_blueprint(login_opt.login_opt, url_prefix='/')
'''
创建数据迁移仓库 flask db init
数据迁移
    1. 生成迁移脚本，并不会执行
    flask db migrate -m '可选'
    2. 执行数据库创建脚本
    flask db upgrade
'''
migrate = Migrate(app, db)

with app.test_request_context():
    # 练习
    # print(url_for('student_opt.insert'))
    # print(url_for('student_opt.queryall'))
    # print(url_for('student_opt.query'))
    # print(url_for('student_opt.update'))

    ##
    print(url_for('enterprise_opt.home'))
    print(url_for('enterprise_opt.detail', id=1))
    print(url_for('enterprise_opt.analysis'))
    print(url_for('login_opt.login'))

if __name__ == '__main__':
    app.run()