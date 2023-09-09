"""adding status message column

Revision ID: d66148e184f5
Revises: 9651ef2b8af9
Create Date: 2022-04-26 11:50:25.443498

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd66148e184f5'
down_revision = '9651ef2b8af9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('jobs', sa.Column('status_message', sa.String()))


def downgrade():
    op.drop_column('status_message')
