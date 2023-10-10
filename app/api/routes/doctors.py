from email import message
import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.doctors import Doctor

from ..auth.main import validate_token, UserSession
from ..schemas.doctors import DoctorCreateSchema
#from ..schemas.jobs import JobTypeEnum, JobStatus, JobOutput
from ..database.conf import db
from typing import Optional
from jsonschema import SchemaError, ValidationError, validate

#temp
from sqlalchemy.orm import Session
from datetime import datetime


router = APIRouter()

@router.get('/doctors')
async def get_doctors(database: Session = Depends(db)):
    doctors = database.query(Doctor).all()
    
    if doctors:
        # If specialties are found, return them as a JSON response
        return {'message': 'Doctors retrieved successfully', 'doctors': doctors}
    else:
        # If no specialties are found, return a message indicating that
        return {'message': 'No doctors found'}
    

@router.post('/doctors')
async def create_doctor(doctor_data: DoctorCreateSchema, database: Session = Depends(db)):
    doctor = Doctor(name= doctor_data.name, genderMale=doctor_data.genderMale, specialty_id=doctor_data.specialty_id)
    database.add(doctor)
    database.commit()
    database.refresh(doctor)

    return {'message': 'Doctor created.', 'doctor': doctor}