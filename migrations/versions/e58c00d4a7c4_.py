"""empty message

Revision ID: e58c00d4a7c4
Revises: 836b5839fd10
Create Date: 2022-11-28 15:23:28.315853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e58c00d4a7c4'
down_revision = '836b5839fd10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.add_column(sa.Column('school_password', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schools', schema=None) as batch_op:
        batch_op.drop_column('school_password')

    # ### end Alembic commands ###
