"""empty message

Revision ID: badceaabd9ea
Revises: 
Create Date: 2022-02-13 16:19:39.310100

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'badceaabd9ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('titleImage', sa.Text(), nullable=False),
    sa.Column('overview', sa.Text(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('projectId', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['projectId'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instructions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('projectId', sa.Integer(), nullable=False),
    sa.Column('stepOrder', sa.Integer(), nullable=False),
    sa.Column('stepTitle', sa.String(length=100), nullable=True),
    sa.Column('instructions', sa.Text(), nullable=True),
    sa.Column('photoUrl', sa.Text(), nullable=True),
    sa.Column('videoUrl', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['projectId'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('projectId', sa.Integer(), nullable=False),
    sa.Column('supply', sa.String(length=150), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['projectId'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
        # ... logic to create tables

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE projects SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE comments SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE instructions SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE supplies SET SCHEMA {SCHEMA};")
        #  add an ALTER TABLE command here for each table created in the file


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplies')
    op.drop_table('instructions')
    op.drop_table('comments')
    op.drop_table('projects')
    op.drop_table('users')
    # ### end Alembic commands ###
