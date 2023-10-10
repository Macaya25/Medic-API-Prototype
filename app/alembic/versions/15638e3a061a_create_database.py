"""create_database

Revision ID: 15638e3a061a
Revises: 
Create Date: 2023-09-16 01:53:08.242874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15638e3a061a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'specialties',
        sa.Column('id', sa.BigInteger, nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
    )

    op.create_table(
        'doctors',
        sa.Column('id', sa.BigInteger, nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('genderMale', sa.Boolean, nullable=False),
        sa.Column('specialty_id', sa.BigInteger, sa.ForeignKey('specialties.id')),
    )

    op.create_table(
        'appointments',
        sa.Column('id', sa.BigInteger, nullable=False, primary_key=True),
        sa.Column("date", sa.DateTime(timezone=True)),
        sa.Column('location', sa.String(), nullable=False),
        sa.Column('doctor_id', sa.BigInteger, sa.ForeignKey('doctors.id')),
    )
    


def downgrade():
    op.drop_table('appointments')
    op.drop_table('doctors')
    op.drop_table('specialties')
