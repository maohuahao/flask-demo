"""empty message

Revision ID: c27fb6ce65ea
Revises: b57ee3ac4146
Create Date: 2023-04-07 09:20:29.151029

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c27fb6ce65ea'
down_revision = 'b57ee3ac4146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('new_job')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('new_job',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('eid', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('job_type', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('number', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('sex', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('welfare', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('education', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('size1', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('job_1st_class', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('years', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('salary', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('employer_type', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('industry', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('age', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('position', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('title_abbr', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('city_code', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('start_date', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
