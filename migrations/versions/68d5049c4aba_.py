"""empty message

Revision ID: 68d5049c4aba
Revises: a14f704522ad
Create Date: 2022-11-30 15:25:24.878002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68d5049c4aba'
down_revision = 'a14f704522ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_added', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.drop_column('date_added')

    # ### end Alembic commands ###
