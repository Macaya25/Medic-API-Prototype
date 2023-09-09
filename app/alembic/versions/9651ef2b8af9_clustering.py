"""clustering

Revision ID: 9651ef2b8af9
Revises: dc00479f74b7
Create Date: 2022-04-22 18:13:28.978606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9651ef2b8af9'
down_revision = 'dc00479f74b7'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("update job_types SET name='CLUSTERING' where name='CLUSTERIZATION'")


def downgrade():
    pass
