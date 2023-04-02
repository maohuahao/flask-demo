from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# 操作数据库的对象
db = SQLAlchemy()
# 数据序列化
ma = Marshmallow()