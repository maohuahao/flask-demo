"""empty message

Revision ID: 50ff4f3fdde3
Revises: ed75a5bc0ff1
Create Date: 2023-03-31 09:46:32.247928

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '50ff4f3fdde3'
down_revision = 'ed75a5bc0ff1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('executedpersons_temp', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('executedpersons_temp', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###
