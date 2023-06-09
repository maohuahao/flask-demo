#config.py
user = 'root'
password = '123456'
database = 'flask01'
host = '8.130.111.128'
port = '3306'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(user, password, host, port,database)
# 设置sqlalchemy自动更跟踪数据库
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO = False
# 禁止自动提交数据处理
SQLALCHEMY_COMMIT_ON_TEARDOWN = False


SQLALCHEMY_BINDS = {
    'localhost': 'mysql+pymysql://root:123456@localhost:3306/data?charset=utf8'
}