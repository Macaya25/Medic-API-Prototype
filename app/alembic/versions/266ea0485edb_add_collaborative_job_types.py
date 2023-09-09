"""add COLLABORATIVE job types

Revision ID: 266ea0485edb
Revises: ea0c2e7e3031
Create Date: 2022-04-14 16:14:17.298480

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '266ea0485edb'
down_revision = 'ea0c2e7e3031'
branch_labels = None
depends_on = None

job_types_table = sa.sql.table('job_types',
                               sa.sql.column('id', sa.BigInteger),
                               sa.sql.column('name', sa.String()),
                               sa.sql.column('dag_name', sa.String()),
                               sa.sql.column('params_schema',
                                             postgresql.JSONB),

                               sa.Column('created_at', sa.DateTime(
                                   timezone=True), nullable=False, default=datetime.now),
                               sa.Column('updated_at', sa.DateTime(
                                   timezone=True), nullable=False, default=datetime.now, onupdate=datetime.now)
                               )


def upgrade():
    op.bulk_insert(
        job_types_table,
        [
            {'id': 2, 'name': 'COLLABORATIVE_RETRIEVAL',
             'dag_name': 'datasource_from_collaborative_session_v2', 'params_schema': {}},
            {'id': 3, 'name': 'COLLABORATIVE_SESSION',
             'dag_name': 'google_drive_upload', 'params_schema': {}},
            {'id': 4, 'name': 'COLLABORATIVE_SPLIT',
             'dag_name': 'dag_split_datasources', 'params_schema': {}},
        ]
    )


def downgrade():
    op.execute(job_types_table.delete().where(job_types_table.c.id == 2))
    op.execute(job_types_table.delete().where(job_types_table.c.id == 3))
    op.execute(job_types_table.delete().where(job_types_table.c.id == 4))
