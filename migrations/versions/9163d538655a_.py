"""empty message

Revision ID: 9163d538655a
Revises: cb860438f34b
Create Date: 2024-03-09 02:29:25.735858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9163d538655a'
down_revision = 'cb860438f34b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'questions', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
