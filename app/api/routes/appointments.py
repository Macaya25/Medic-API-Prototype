from email import message
import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.appointments import Appointment

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

@router.get('/appointment')
async def get_appointments(database: Session = Depends(db)):
    appointments = database.query(Appointment).all()
    print("Apps: " ,appointments)
    
    
    return {'message': 'No appointments'}


@router.post('/appointment')
async def create_appointment(database: Session = Depends(db)):

    app = Appointment(date=datetime.now,
                      location="Somewhere",
                      #medic=1,
                      )
    
    database.add(app)
    database.commit()

    return {'message': 'Ye'}