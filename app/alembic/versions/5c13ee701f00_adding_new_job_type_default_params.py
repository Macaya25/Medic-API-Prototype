"""adding new job type default params

Revision ID: 5c13ee701f00
Revises: d66148e184f5
Create Date: 2022-04-28 13:11:05.902344

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '5c13ee701f00'
down_revision = 'd66148e184f5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('job_types', sa.Column(
        'default_params', postgresql.JSONB, default={}))


def downgrade():
    op.drop_column('job_types', 'default_params')
