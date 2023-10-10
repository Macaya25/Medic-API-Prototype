from email import message
import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.medic_center import MedicCenter

from ..auth.main import validate_token, UserSession
from ..schemas.medic_centers import CenterCreateSchema
#from ..schemas.jobs import JobTypeEnum, JobStatus, JobOutput
from ..database.conf import db
from typing import Optional
from jsonschema import SchemaError, ValidationError, validate

#temp
from sqlalchemy.orm import Session
from datetime import datetime


router = APIRouter()


@router.get('/centers')
async def get_centers(database: Session = Depends(db)):
    centers = database.query(MedicCenter).all()
    
    if centers:
        # If specialties are found, return them as a JSON response
        return {'message': 'Medic centers retrieved successfully', 'Medic centers': centers}
    else:
        # If no specialties are found, return a message indicating that
        return {'message': 'No Medic centers found'}

@router.post('/centers')
async def create_center(data: CenterCreateSchema, database: Session = Depends(db)):
    center = MedicCenter(name= data.name, location=data.location)

    database.add(center)
    database.commit()
    return {'message': 'Medic centers created.'}
