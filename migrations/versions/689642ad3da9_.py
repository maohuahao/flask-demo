"""empty message

Revision ID: 689642ad3da9
Revises: cbc2c21c69ef
Create Date: 2023-03-30 16:34:02.108455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '689642ad3da9'
down_revision = 'cbc2c21c69ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enterprise_rank', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shiyebx_num', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('yiliaobx_num', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('gongshangbx_num', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('dw_shiyebx_js', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('score', sa.Float(asdecimal=True), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enterprise_rank', schema=None) as batch_op:
        batch_op.drop_column('score')
        batch_op.drop_column('dw_shiyebx_js')
        batch_op.drop_column('gongshangbx_num')
        batch_op.drop_column('yiliaobx_num')
        batch_op.drop_column('shiyebx_num')

    # ### end Alembic commands ###
