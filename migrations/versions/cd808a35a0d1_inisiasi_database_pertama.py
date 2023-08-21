"""inisiasi database pertama

Revision ID: cd808a35a0d1
Revises: 
Create Date: 2023-08-21 10:49:31.609506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd808a35a0d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=90), nullable=True),
    sa.Column('email', sa.String(length=90), nullable=True),
    sa.Column('password', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
