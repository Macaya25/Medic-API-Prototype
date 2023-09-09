from email import message
import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.jobs import Job, Job_Type

from ..auth.main import validate_token, UserSession
from ..schemas.jobs import GenericJob
from ..schemas.jobs import JobTypeEnum, JobStatus, JobOutput
from ..database.conf import db
from typing import Optional
from jsonschema import SchemaError, ValidationError, validate

router = APIRouter()
