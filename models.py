from exts import db
from marshmallow import fields, Schema


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self): return f'Student(name = {self.name}, age = {self.age})'

    def __str__(self): return f'Student(name = {self.name}, age = {self.age})'


class StudentSchema(Schema):
    name = fields.String()
    age = fields.Integer()


# 企业被执行次数表
class Executedpersons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.String(36))
    ep_count = db.Column(db.Integer)


class ExecutedpersonsSchema(Schema):
    id = fields.Integer()
    eid = fields.String()
    ep_count = fields.Integer()


# 企业失信次数表
class Executions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.String(36))
    executions_count = db.Column(db.Integer)


class ExecutionsSchema(Schema):
    id = fields.Integer()
    eid = fields.String()
    executions_count = fields.Integer()


# 经营异常工商公示次数表
class Abnormal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.String(36))
    abnormal_count = db.Column(db.Integer)


class AbnormalSchema(Schema):
    id = fields.Integer()
    eid = fields.String()
    abnormal_count = fields.Integer()


# 严重违法工商公示表
class SeriousIllegal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.String(36))
    count = db.Column(db.Integer)


class SeriousIllegalSchema(Schema):
    id = fields.Integer()
    eid = fields.String()
    count = fields.Integer()


# -------------------------------------------------------

class seriousIllegalTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    name = db.Column(db.String(100))


class seriousIllegalTempSchema(Schema):
    id = fields.Integer()
    count = fields.Integer()
    name = fields.String()


class AbnormalCountTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    name = db.Column(db.String(100))


class AbnormalCountTempSchema(Schema):
    id = fields.Integer()
    count = fields.Integer()
    name = fields.String()


class ExecutedpersonsTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    name = db.Column(db.String(100))

class ExecutedpersonsTempSchema(Schema):
    id = fields.Integer()
    count = fields.Integer()
    name = fields.String()

# 企业被执行次数表
class ExecutionsTemp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    name = db.Column(db.String(100))

class ExecutionsTempSchema(Schema):
    id = fields.Integer()
    count = fields.Integer()
    name = fields.String()


# 企业排名表
class EnterpriseRank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.String(36))
    reg_no = db.Column(db.String(255))
    credit_no = db.Column(db.String(255))
    org_no = db.Column(db.String(255))
    format_name = db.Column(db.String(255))
    category = db.Column(db.String(10))
    econ_kind = db.Column(db.String(255))
    scope = db.Column(db.String(255))
    term_start = db.Column(db.String(255))
    term_end = db.Column(db.String(255))
    check_date = db.Column(db.String(255))
    belong_org = db.Column(db.String(255))
    oper_name = db.Column(db.String(255))
    oper_type = db.Column(db.String(255))
    oper_name_id = db.Column(db.String(50))
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))
    status = db.Column(db.String(50))
    type = db.Column(db.Integer)
    type_desc = db.Column(db.String(255))
    title = db.Column(db.String(255))
    longitude = db.Column(db.Float(asdecimal=True))
    latitude = db.Column(db.Float(asdecimal=True))
    gd_longitude = db.Column(db.Float(asdecimal=True))
    gd_latitude = db.Column(db.Float(asdecimal=True))
    obj_id = db.Column(db.String(50))
    province_code = db.Column(db.String(10))
    district_code = db.Column(db.String(10))
    title_code = db.Column(db.String(255))
    econ_kind_code = db.Column(db.String(255))
    regist_capi_new = db.Column(db.String(255))
    currency_unit = db.Column(db.String(10))
    belong_org_code = db.Column(db.String(255))
    credit_area_code = db.Column(db.String(255))
    new_status_code = db.Column(db.String(255))
    type_new = db.Column(db.String(20))
    category_new = db.Column(db.String(20))
    out_time = db.Column(db.String(100))
    diaoxiao_time = db.Column(db.String(100))
    regist_capi = db.Column(db.Float(asdecimal=True))
    created_time = db.Column(db.String(100))
    shiyebx_num = db.Column(db.Integer)  # 失业保险人数
    yiliaobx_num = db.Column(db.Integer)  # 职工基本医疗保险人数
    gongshangbx_num = db.Column(db.Float)  # 工伤保险人数
    dw_shiyebx_js = db.Column(db.Float)  # 单位参加失业保险缴费基数
    score = db.Column(db.Float(asdecimal=True))

    def __repr__(self): return f'EnterpriseRank(eid={self.eid})'

    def __str__(self): return f'EnterpriseRank(eid={self.eid})'


class EnterpriseRankSchema(Schema):
    id = fields.Integer()
    eid = fields.String()
    reg_no = fields.String()
    credit_no = fields.String()
    org_no = fields.String()
    name = fields.String()
    category = fields.String()
    econ_kind = fields.String()
    scope = fields.String()
    term_start = fields.String()
    term_end = fields.String()
    check_date = fields.String()
    belong_org = fields.String()
    oper_name = fields.String()
    oper_type = fields.String()
    oper_name_id = fields.String()
    start_date = fields.String()
    end_date = fields.String()
    status = fields.String()
    type = fields.Integer()
    type_desc = fields.String()
    title = fields.String()
    longitude = fields.Float()
    latitude = fields.Float()
    gd_longitude = fields.Float()
    gd_latitude = fields.Float()
    obj_id = fields.String()
    province_code = fields.String()
    district_code = fields.String()
    title_code = fields.String()
    econ_kind_code = fields.String()
    regist_capi_new = fields.String()
    currency_unit = fields.String()
    belong_org_code = fields.String()
    credit_area_code = fields.String()
    new_status_code = fields.String()
    type_new = fields.String()
    category_new = fields.String()
    out_time = fields.String()
    diaoxiao_time = fields.String()
    regist_capi = fields.Float()
    created_time = fields.String()
    yiliaobx_num = fields.Integer()  # 职工基本医疗保险人数
    gongshangbx_num = fields.Float()  # 工伤保险人数
    dw_shiyebx_js = fields.Float()  # 单位参加失业保险缴费基数
    score = fields.Float()
