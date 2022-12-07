"""empty message

Revision ID: 521ed55cba53
Revises: 18bd3614021e
Create Date: 2022-05-12 05:20:55.271056

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '521ed55cba53'
down_revision = '18bd3614021e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('views',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('projectId', sa.Integer(), nullable=False),
    sa.Column('viewCount', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['projectId'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
        # ... logic to create tables

    if environment == "production":
        op.execute(f"ALTER TABLE views SET SCHEMA {SCHEMA};")
        #  add an ALTER TABLE command here for each table created in the file


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('views')
    # ### end Alembic commands ###
