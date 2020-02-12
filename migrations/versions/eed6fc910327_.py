"""empty message

Revision ID: eed6fc910327
Revises: 
Create Date: 2020-02-10 14:28:55.807591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eed6fc910327'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('elective_listv2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('electiveID', sa.String(length=64), nullable=True),
    sa.Column('electiveName', sa.String(length=64), nullable=True),
    sa.Column('electiveDescription', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_elective_listv2_electiveID'), 'elective_listv2', ['electiveID'], unique=True)
    op.create_index(op.f('ix_elective_listv2_electiveName'), 'elective_listv2', ['electiveName'], unique=True)
    op.create_table('faculty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('fac_id', sa.String(length=40), nullable=True),
    sa.Column('elective_id', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_faculty_elective_id'), 'faculty', ['elective_id'], unique=False)
    op.create_index(op.f('ix_faculty_fac_id'), 'faculty', ['fac_id'], unique=False)
    op.create_index(op.f('ix_faculty_user_id'), 'faculty', ['user_id'], unique=False)
    op.create_table('faculty_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fac_id', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('designation', sa.String(length=10), nullable=True),
    sa.Column('department', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_faculty_details_department'), 'faculty_details', ['department'], unique=False)
    op.create_index(op.f('ix_faculty_details_designation'), 'faculty_details', ['designation'], unique=False)
    op.create_index(op.f('ix_faculty_details_fac_id'), 'faculty_details', ['fac_id'], unique=True)
    op.create_index(op.f('ix_faculty_details_name'), 'faculty_details', ['name'], unique=False)
    op.create_table('initial_elective_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('electiveID', sa.String(length=64), nullable=True),
    sa.Column('electiveName', sa.String(length=64), nullable=True),
    sa.Column('electiveDescription', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_initial_elective_list_electiveID'), 'initial_elective_list', ['electiveID'], unique=True)
    op.create_index(op.f('ix_initial_elective_list_electiveName'), 'initial_elective_list', ['electiveName'], unique=True)
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('roll_number', sa.String(length=30), nullable=True),
    sa.Column('elective_id1', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_elective_id1'), 'student', ['elective_id1'], unique=False)
    op.create_index(op.f('ix_student_name'), 'student', ['name'], unique=False)
    op.create_index(op.f('ix_student_roll_number'), 'student', ['roll_number'], unique=False)
    op.create_index(op.f('ix_student_user_id'), 'student', ['user_id'], unique=False)
    op.create_table('student_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roll_no', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('batch', sa.String(length=10), nullable=True),
    sa.Column('section', sa.String(length=10), nullable=True),
    sa.Column('department', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_details_batch'), 'student_details', ['batch'], unique=False)
    op.create_index(op.f('ix_student_details_department'), 'student_details', ['department'], unique=False)
    op.create_index(op.f('ix_student_details_name'), 'student_details', ['name'], unique=False)
    op.create_index(op.f('ix_student_details_roll_no'), 'student_details', ['roll_no'], unique=True)
    op.create_index(op.f('ix_student_details_section'), 'student_details', ['section'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_student_details_section'), table_name='student_details')
    op.drop_index(op.f('ix_student_details_roll_no'), table_name='student_details')
    op.drop_index(op.f('ix_student_details_name'), table_name='student_details')
    op.drop_index(op.f('ix_student_details_department'), table_name='student_details')
    op.drop_index(op.f('ix_student_details_batch'), table_name='student_details')
    op.drop_table('student_details')
    op.drop_index(op.f('ix_student_user_id'), table_name='student')
    op.drop_index(op.f('ix_student_roll_number'), table_name='student')
    op.drop_index(op.f('ix_student_name'), table_name='student')
    op.drop_index(op.f('ix_student_elective_id1'), table_name='student')
    op.drop_table('student')
    op.drop_index(op.f('ix_initial_elective_list_electiveName'), table_name='initial_elective_list')
    op.drop_index(op.f('ix_initial_elective_list_electiveID'), table_name='initial_elective_list')
    op.drop_table('initial_elective_list')
    op.drop_index(op.f('ix_faculty_details_name'), table_name='faculty_details')
    op.drop_index(op.f('ix_faculty_details_fac_id'), table_name='faculty_details')
    op.drop_index(op.f('ix_faculty_details_designation'), table_name='faculty_details')
    op.drop_index(op.f('ix_faculty_details_department'), table_name='faculty_details')
    op.drop_table('faculty_details')
    op.drop_index(op.f('ix_faculty_user_id'), table_name='faculty')
    op.drop_index(op.f('ix_faculty_fac_id'), table_name='faculty')
    op.drop_index(op.f('ix_faculty_elective_id'), table_name='faculty')
    op.drop_table('faculty')
    op.drop_index(op.f('ix_elective_listv2_electiveName'), table_name='elective_listv2')
    op.drop_index(op.f('ix_elective_listv2_electiveID'), table_name='elective_listv2')
    op.drop_table('elective_listv2')
    # ### end Alembic commands ###
