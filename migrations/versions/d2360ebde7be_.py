"""empty message

Revision ID: d2360ebde7be
Revises: 521ed55cba53
Create Date: 2022-06-23 20:15:19.229727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2360ebde7be'
down_revision = '521ed55cba53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('supplies', 'supply')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplies', sa.Column('supply', sa.VARCHAR(length=150), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
