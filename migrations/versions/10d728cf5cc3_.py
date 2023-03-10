"""empty message

Revision ID: 10d728cf5cc3
Revises: 2fde5c640499
Create Date: 2022-11-28 14:24:17.542180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d728cf5cc3'
down_revision = '2fde5c640499'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.add_column(sa.Column('school_password', sa.String(), nullable=True, default_value='password'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.drop_column('school_password')

    # ### end Alembic commands ###
