"""empty message

Revision ID: ed75a5bc0ff1
Revises: e3d5d4126969
Create Date: 2023-03-30 21:56:02.379238

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ed75a5bc0ff1'
down_revision = 'e3d5d4126969'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_enterprise')
    op.drop_table('executedpersons_temp')
    with op.batch_alter_table('abnormal_count_temp', schema=None) as batch_op:
        batch_op.alter_column('format_name',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('abnormal_count_temp', schema=None) as batch_op:
        batch_op.alter_column('format_name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)

    op.create_table('executedpersons_temp',
    sa.Column('ep_count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('format_name', mysql.VARCHAR(length=255), nullable=True),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('t_enterprise',
    sa.Column('eid', mysql.CHAR(length=36), nullable=True),
    sa.Column('reg_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('credit_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('org_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('format_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('category', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('province', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('econ_kind', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('scope', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('term_start', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('term_end', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('check_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('belong_org', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('oper_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('oper_type', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('oper_name_id', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('start_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('end_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('status', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('type', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('type_desc', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('longitude', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('latitude', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('gd_longitude', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('gd_latitude', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('obj_id', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('source', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('url', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('row_update_time', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('province_code', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('district_code', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('title_code', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('econ_kind_code', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('regist_capi_new', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('currency_unit', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('belong_org_code', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('credit_area_code', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('new_status_code', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('type_new', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('category_new', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('out_time', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('diaoxiao_time', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('regist_capi', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('created_time1', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('last_update_time1', mysql.VARCHAR(length=100), nullable=True),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
