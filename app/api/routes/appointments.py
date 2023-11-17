from email import message
import logging
import uuid
import http.client
import json

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.appointments import Appointment
from ..models.doctors import Doctor
from ..models.medic_center import MedicCenter
from ..models.specialties import Specialty

from ..auth.main import validate_token, UserSession
from ..schemas.appointments import AppointmentCreateSchema, AppointmentsReturnedSchema
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
    returnAppointments = []

    if appointments:
        for app in appointments:
            converted_app = ConvertAppointment(database, app)
            returnAppointments.append(converted_app)

        return {'message': 'Appointments retrieved successfully', 'Appointments': returnAppointments}
    else:
        return {'message': 'No appointments'}


@router.post('/appointments')
async def create_appointment(app_data: AppointmentCreateSchema, database: Session = Depends(db)):

    app = Appointment(date=app_data.date, medic_center_id=app_data.medic_center_id, doctor_id=app_data.doctor_id)
    converted_app = ConvertAppointment(database, app)
    data = json.loads(converted_app.json())
    headers = {"Content-type": "application/json"}

    # Create a connection to the server
    conn = http.client.HTTPConnection('https://vpc-iaps-medics-domain-4om4eyngnbu4bbphyscl3hy46y.us-west-2.es.amazonaws.com')
    endpoint = '/appointments_index/_doc'

    # response = httpx.post(, data=data)
    # print("Response: ", response)
    conn.request('POST', endpoint, data, headers)
    response = conn.getresponse()

    # Print the response status code and data
    print("Status:", response.status)
    print("Data:", response.read().decode())

    # Close the connection
    conn.close()
    
    database.add(app)
    database.commit()

    return {'message': 'Ye'}

def ConvertAppointment(database, app):
    doc = database.query(Doctor).get(app.doctor_id)
    spec = database.query(Specialty).get(doc.specialty_id).name
    center = database.query(MedicCenter).get(app.medic_center_id)

    appointment = AppointmentsReturnedSchema(date=app.date, 
                                    doctor_name=doc.name,
                                    specialty= spec, 
                                    medic_center=center.name,
                                    location=center.location)
    return appointment
