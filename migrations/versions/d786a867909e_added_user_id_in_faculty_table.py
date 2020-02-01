"""Added user_id in Faculty Table

Revision ID: d786a867909e
Revises: 48fd099f659d
Create Date: 2020-01-25 19:22:04.950132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd786a867909e'
down_revision = '48fd099f659d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('faculty', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_faculty_user_id'), 'faculty', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_faculty_user_id'), table_name='faculty')
    op.drop_column('faculty', 'user_id')
    # ### end Alembic commands ###