"""Initial migration

Revision ID: ec32b0be9e6e
Revises: 
Create Date: 2022-05-10 14:43:57.435460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec32b0be9e6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('incomes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('currency', sa.String(length=7), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('incomes')
    # ### end Alembic commands ###
