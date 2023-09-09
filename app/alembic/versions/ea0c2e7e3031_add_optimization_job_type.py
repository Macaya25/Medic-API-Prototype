"""add OPTIMIZATION job type

Revision ID: ea0c2e7e3031
Revises: b3a862b4287a
Create Date: 2022-04-14 12:31:38.875171

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'ea0c2e7e3031'
down_revision = '7b886cabd0fb'
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
            {
                'id': 1, 'name': 'OPTIMIZATION', 'dag_name': 'optimization_preprocess',
                'params_schema': {
                    'type': 'object',
                    'required': ['base_datasources', 'base_merge_relationships', 'values_column', 'costs_column', 'priorities_column', 'groupable_columns', 'budget_datasource'],
                    'properties': {
                        'base_datasources': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'base_merge_relationships': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'required': ['source_datasource', 'target_datasource', 'columns'],
                                'properties': {
                                    'source_datasource': {'type': 'string'},
                                    'target_datasource': {'type': 'string'},
                                    'columns': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'object',
                                            'required': ['source_column', 'target_column'],
                                            'properties': {
                                                'source_column': {'type': 'string'},
                                                'target_column': {'type': 'string'}
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        'values_column': {
                            'type': 'object',
                            'required': ['source_datasource', 'column_name'],
                            'properties': {
                                'source_datasource': {'type': 'string'},
                                'column_name': {'type': 'string'},
                            }
                        },
                        'costs_column': {
                            'type': 'object',
                            'required': ['source_datasource', 'column_name'],
                            'properties': {
                                'source_datasource': {'type': 'string'},
                                'column_name': {'type': 'string'},
                            }
                        },
                        'priorities_column': {
                            'type': 'object',
                            'required': ['source_datasource', 'column_name'],
                            'properties': {
                                'source_datasource': {'type': 'string'},
                                'column_name': {'type': 'string'},
                            }
                        },
                        'groupable_columns': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'required': ['source_datasource', 'column_name'],
                                'properties': {
                                    'source_datasource': {'type': 'string'},
                                    'column_name': {'type': 'string'},
                                }
                            }
                        },
                        'budget_datasource': {'type': 'string'}
                    }
                }
            }
        ]
    )


def downgrade():
    op.execute(job_types_table.delete().where(job_types_table.c.id == 1))
