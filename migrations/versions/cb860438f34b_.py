"""empty message

Revision ID: cb860438f34b
Revises: 8c66cfb7b86e
Create Date: 2024-03-08 02:00:13.085271

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cb860438f34b'
down_revision = '8c66cfb7b86e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('themes', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=300),
               nullable=True)
        batch_op.drop_index('title')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('themes', schema=None) as batch_op:
        batch_op.create_index('title', ['title'], unique=True)
        batch_op.alter_column('title',
               existing_type=mysql.VARCHAR(length=300),
               nullable=False)

    # ### end Alembic commands ###
