import json
import re
from typing import List

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import func

from models import *

enterprise_opt = Blueprint('enterprise_opt', __name__)


# 验证登录信息
def verify():
    return request.cookies.get('username') != 'zhangsan'


'''首页'''


@enterprise_opt.route('/home/')
def home():
    # 验证cookie
    if verify():
        return redirect(url_for('login_opt.login'))

    if not request.args.get('search'):
        page = request.args.get('page', 1, type=int)
        paginate = EnterpriseRank.query.paginate(page=page, per_page=10, error_out=False)
    else:
        search = request.args.get('search').strip()
        print(search)
        page = request.args.get('page', 1, type=int)
        paginate = EnterpriseRank.query.filter(EnterpriseRank.format_name.contains(search)).paginate(page=page,
                                                                                                     per_page=10,
                                                                                                     error_out=False)

    enterpriseRanks = paginate.items
    return render_template('home/table_index.html', locals=locals())


'''详情页模板'''


@enterprise_opt.route('/home/detail/<int:id>')
def detail(id):
    # 验证cookie
    if verify():
        return redirect(url_for('login_opt.login'))
    else:
        enterprise = EnterpriseRank.query.get(id)
        return render_template('home/table_detail.html', locals=locals())


'''可视化大屏'''


@enterprise_opt.route('/ranking/')
def ranking():
    # 验证cookie
    if verify():
        return redirect(url_for('login_opt.login'))
    else:
        serious_illegal = seriousIllegalTemp.query.order_by(-seriousIllegalTemp.count).limit(5).all()
        abnormal = AbnormalCountTemp.query.order_by(-AbnormalCountTemp.count).limit(5).all()
        executedpersons = ExecutedpersonsTemp.query.order_by(-ExecutedpersonsTemp.count).limit(5).all()
        executions = ExecutionsTemp.query.order_by(-ExecutionsTemp.count).limit(5).all()

        serious_illegal_dump = seriousIllegalTempSchema(many=True)
        abnormal_dump = AbnormalCountTempSchema(many=True)
        executedpersons_dump = ExecutedpersonsTempSchema(many=True)
        executions_dump = ExecutedpersonsTempSchema(many=True)

        serious_illegal_json = serious_illegal_dump.dumps(serious_illegal, ensure_ascii=False)
        abnormal_json = abnormal_dump.dumps(abnormal, ensure_ascii=False)
        executedpersons_json = executedpersons_dump.dumps(executedpersons, ensure_ascii=False)
        executions_json = executions_dump.dumps(executions, ensure_ascii=False)

    return render_template('ranking/index.html', locals=locals())


@enterprise_opt.route('/analysis/')
def analysis():
    if verify():
        return redirect(url_for('login_opt.login'))
    else:
        enterprises = EnterpriseRank.query.with_entities(EnterpriseRank.format_name, EnterpriseRank.longitude,
                                                         EnterpriseRank.latitude)
        enterprise_rank_dump = EnterpriseRankSchema(many=True)
        enterprise_json = enterprise_rank_dump.dumps(enterprises, ensure_ascii=False)

    return render_template('analysis/index.html', enterprises=enterprise_json)


def get_industry():
    industry = LocalNewJob().query.with_entities(LocalNewJob.industry).all()
    industry_list = []
    for item in industry:
        for str in item[0].split('/'):
            if str == '\\N':
                continue
            industry_list.append(str)

    industry_list_clear = []
    for item in industry_list:
        for str in item.split('|'):
            industry_list_clear.append(str)

    return industry_list_clear


def get_education() -> List:
    education = LocalNewJob.query.with_entities(LocalNewJob.education).all()
    education_list = []
    for item in education:
        if item[0] == '\\N':
            continue

        if re.search('初中|小学', item[0]):
            education_list.append('高中以下')
        elif re.search('高中|中专', item[0]):
            education_list.append('高中或中专')
        elif re.search('专科|大专', item[0]):
            education_list.append('专科')
        elif re.search('本科', item[0]):
            education_list.append('本科')
        elif re.search('硕士', item[0]):
            education_list.append('硕士')
        elif re.search('博士', item[0]):
            education_list.append('博士')

    return education_list


@enterprise_opt.route('/bigScreen/')
def big_screen():
    # 行业分布
    industry_list_clear = get_industry()

    # 学历分布
    education_list_clear = get_education()

    # 企业规模分布
    enterprise_size = db.session.query(LocalNewJob.size1, func.count(1)).filter(LocalNewJob.size1!='\\N').group_by(LocalNewJob.size1).order_by(func.count(1).desc()).limit(5).all()
    enterprise_dict_size = json.dumps([{"name":item[0], "value":item[1]} for item in enterprise_size])

    # 年龄分布
    enterprise_age = db.session.query(LocalNewJob.age, func.count(1)).filter(LocalNewJob.age!='\\N').group_by(LocalNewJob.age).order_by(func.count(1).desc()).limit(5).all()
    enterprise_dict_age = json.dumps([{"name":item[0], "value":item[1]} for item in enterprise_age])

    # 职位描述
    enterprise_title_abbr = db.session.query(LocalNewJob.title_abbr, func.count(1)).filter(LocalNewJob.title_abbr != '\\N').group_by(LocalNewJob.title_abbr).order_by(func.count(1).desc()).limit(5).all()
    enterprise_dict_title = json.dumps([{"name":item[0], "value":item[1]} for item in enterprise_title_abbr])


    return render_template("bigScreen/index.html", locals=locals())
