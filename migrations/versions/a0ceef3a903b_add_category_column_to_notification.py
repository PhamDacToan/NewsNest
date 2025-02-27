"""Add category column to Notification

Revision ID: a0ceef3a903b
Revises: 
Create Date: 2024-12-13 03:56:06.076070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0ceef3a903b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=200), nullable=True))

    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.drop_column('category')

    with op.batch_alter_table('group', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
