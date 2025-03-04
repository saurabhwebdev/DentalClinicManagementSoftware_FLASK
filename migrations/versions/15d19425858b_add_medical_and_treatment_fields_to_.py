"""Add medical and treatment fields to patient

Revision ID: 15d19425858b
Revises: 5398c65aa3ca
Create Date: 2024-12-08 18:26:49.861683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15d19425858b'
down_revision = '5398c65aa3ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chief_complaint', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('medical_dental_history', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('on_examination', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('diagnosis', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('treatment_plan', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('treatment_done', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('recall', sa.Text(), nullable=True))
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patient', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
        batch_op.drop_column('recall')
        batch_op.drop_column('treatment_done')
        batch_op.drop_column('treatment_plan')
        batch_op.drop_column('diagnosis')
        batch_op.drop_column('on_examination')
        batch_op.drop_column('medical_dental_history')
        batch_op.drop_column('chief_complaint')

    # ### end Alembic commands ###
