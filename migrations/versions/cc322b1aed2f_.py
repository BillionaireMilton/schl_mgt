"""empty message

Revision ID: cc322b1aed2f
Revises: 9a5c61ee4544
Create Date: 2022-11-28 14:34:03.567003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc322b1aed2f'
down_revision = '9a5c61ee4544'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.add_column(sa.Column('school_type', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.drop_column('school_type')

    # ### end Alembic commands ###
