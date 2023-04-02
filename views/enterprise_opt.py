from flask import Blueprint, render_template, request, redirect, url_for

from models import *

enterprise_opt = Blueprint('enterprise_opt', __name__)


# 验证登录信息
def verify():
    return request.cookies.get('username') != 'zhangsan'


'''首页'''


@enterprise_opt.route('/index')
def index():
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
        paginate = EnterpriseRank.query.filter(EnterpriseRank.format_name.contains(search)).paginate(page=page,                                                                                            per_page=10,                                                                                    error_out=False)

    enterpriseRanks = paginate.items
    return render_template('home/table_index.html', locals=locals())


'''详情页模板'''


@enterprise_opt.route('/detail/<int:id>')
def detail(id):
    # 验证cookie
    if verify():
        return redirect(url_for('login_opt.login'))
    else:
        enterprise = EnterpriseRank.query.get(id)
        return render_template('home/table_detail.html', locals=locals())


'''可视化大屏'''


@enterprise_opt.route('/ranking')
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

    return render_template('analysis/index.html', locals=locals())
