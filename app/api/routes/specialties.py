from email import message
import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.specialties import Specialty

from ..auth.main import validate_token, UserSession
#from ..schemas.jobs import GenericJob
#from ..schemas.jobs import JobTypeEnum, JobStatus, JobOutput
from ..database.conf import db
from typing import Optional
from jsonschema import SchemaError, ValidationError, validate

#temp
from sqlalchemy.orm import Session
from datetime import datetime


router = APIRouter()


@router.get('/specialties')
async def get_specialties(database: Session = Depends(db)):
    specialties = database.query(Specialty).all()
    
    if specialties:
        # If specialties are found, return them as a JSON response
        return {'message': 'Specialties retrieved successfully', 'specialties': specialties}
    else:
        # If no specialties are found, return a message indicating that
        return {'message': 'No specialties found'}

@router.post('/specialties')
async def create_specialty(name: str, database: Session = Depends(db)):
    spec = Specialty(name= name)

    database.add(spec)
    database.commit()
    return {'message': 'Specialty created.'}
