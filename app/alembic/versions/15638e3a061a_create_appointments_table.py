"""create_appointments_table

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
        'appointments',
        sa.Column('id', sa.BigInteger, nullable=False, primary_key=True),
        sa.Column("date", sa.DateTime(timezone=True)),
        sa.Column('location', sa.String(), nullable=False),
    )


def downgrade():
    pass
