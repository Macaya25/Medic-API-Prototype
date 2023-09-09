"""adding new job types

Revision ID: 5e0ba7db5fcb
Revises: 266ea0485edb
Create Date: 2022-04-21 15:42:48.127549

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '5e0ba7db5fcb'
down_revision = '266ea0485edb'
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
            {'id': 5, 'name': 'CLUSTERING',
             'dag_name': 'clustering_preprocess', 'params_schema': {}},
            {'id': 6, 'name': 'TESTING_GENERIC',
             'dag_name': 'none', 'params_schema': {}},
            {'id': 7, 'name': 'CLASSIFICATION',
             'dag_name': 'classification_preprocess', 'params_schema': {}},
            {'id': 8, 'name': 'PREDICTION',
             'dag_name': 'prediction_preprocess', 'params_schema': {}}
        ]
    )
    op.execute("update job_types SET dag_name='optimization_preprocess' where name='OPTIMIZATION'")
    op.execute("update job_types SET dag_name='datasource_from_collaborative_session_v2' where name='COLLABORATIVE_RETRIEVAL'")
    op.execute("update job_types SET dag_name='google_drive_upload' where name='COLLABORATIVE_SESSION'")
    op.execute("update job_types SET dag_name='dag_split_datasources' where name='COLLABORATIVE_SPLIT'")

def downgrade():
    op.execute(job_types_table.delete().where(job_types_table.c.id == 5))
    op.execute(job_types_table.delete().where(job_types_table.c.id == 6))
    op.execute(job_types_table.delete().where(job_types_table.c.id == 7))
    op.execute(job_types_table.delete().where(job_types_table.c.id == 8))
