from models import Student, StudentSchema
from flask import Blueprint, request
from exts import db
from sqlalchemy import and_, or_

student_opt = Blueprint('student_opt', __name__)


@student_opt.route('/insert')
def insert():
    stu1 = Student(name='张三', age=20)
    stu2 = Student(name='李四', age=20)
    stu3 = Student(name='小明', age=20)
    stu4 = Student(name='王二', age=20)
    stu5 = Student(name='麻子', age=20)
    stu6 = Student(name='小红', age=20)

    db.session.add(stu1)
    db.session.add(stu2)
    db.session.add(stu3)
    db.session.add(stu4)
    db.session.add(stu5)
    db.session.add(stu6)
    db.session.commit()

    return '添加成功'

@student_opt.route('/queryall')
def queryall():
    students = Student.query.all()
    json_data = StudentSchema(many=True).dumps(students, ensure_ascii=False)
    print(json_data)
    return json_data

@student_opt.route('/query')
def query():
    stu_name = request.args.get('name')
    # get() 获取指定id主键对象
    stu1 = Student.query.get(1)
    # print(stu1)

    # 判断数据是否存在
    stu3 = stu1.query.exists()

    # 结果集个数
    count = Student.query.count()
    # print(count)

    # filter、first() 过滤查询，选择第一个数据
    # filter_by 不支持比较查询
    stu2 = Student.query.filter(Student.name=='李四').first()
    stu4 = Student.query.filter_by(age=20).all()
    # print(stu4)

    # 模糊查询
    stus5 = Student.query.filter(Student.name.contains('小')).all()
    stus6 = Student.query.filter(Student.name.like('小%')).all()

    # in,not in,is null,is not null,and,or
    stu7 = Student.query.filter(Student.name.in_(['张三', '小明'])).all()
    stu8 = Student.query.filter(~Student.name.in_(['张三', '小明'])).all()
    stu9 = Student.query.filter(Student.name.is_(None)).all()
    stu10 = Student.query.filter(Student.name.isnot(None)).all()
    stu11 = Student.query.filter(and_(Student.name=='张三', Student.age<10)).all()
    stu12 = Student.query.filter(or_(Student.name=='李四', Student.age < 21)).all()

    print(stu11)
    print(stu12)
    return "query"

@student_opt.route('/update')
def update():
    # 修改单个数据
    # stu1 = Student.query.get(1)
    # stu1.age = 18
    # db.session.commit()

    # 批量更新数据
    # Student.query.filter(Student.name.like("小%")).update({'age': 17 },
    #                                                        synchronize_session=False)

    # 删除数据
    # 删除单条数据
    # stu2 = Student.query.get(2)
    # db.session.delete(stu2)

    # 删除多条数据
    # Student.query.filter(Student.name.like('王%')).delete(synchronize_session=False)

    # 过滤某些列
    stu3 = Student.query.with_entities(Student.age).all()
    print(stu3)

    # db.session.commit()

    return 'update'