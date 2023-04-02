"""empty message

Revision ID: cbc2c21c69ef
Revises: 2877d23c174a
Create Date: 2023-03-30 15:34:45.954714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbc2c21c69ef'
down_revision = '2877d23c174a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enterprise_rank',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eid', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('enterprise_rank')
    # ### end Alembic commands ###
