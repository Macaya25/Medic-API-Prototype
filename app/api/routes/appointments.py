from email import message
import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.appointments import Appointment

from ..auth.main import validate_token, UserSession
from ..schemas.appointments import AppointmentCreateSchema
#from ..schemas.jobs import JobTypeEnum, JobStatus, JobOutput
from ..database.conf import db
from typing import Optional
from jsonschema import SchemaError, ValidationError, validate

#temp
from sqlalchemy.orm import Session
from datetime import datetime


router = APIRouter()

@router.get('/appointments')
async def get_appointments(database: Session = Depends(db)):
    appointments = database.query(Appointment).all()
    print("Apps: " ,appointments)
    
    if appointments:
        return {'message': 'Appointments retrieved successfully', 'Appointments': appointments}
    else:
        return {'message': 'No appointments'}


@router.post('/appointments')
async def create_appointment(app_data: AppointmentCreateSchema, database: Session = Depends(db)):

    app = Appointment(date=app_data.date, medic_center_id=app_data.medic_center_id, doctor_id=app_data.doctor_id)
    
    database.add(app)
    database.commit()

    return {'message': 'Ye'}