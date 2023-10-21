import requests
import json

from fastapi import APIRouter, Depends, HTTPException

from ..utils.airflow import airflow_dag_trigger
from ..utils.jobs import job_formatted
from ..models.medic_center import MedicCenter
from ..models.specialties import Specialty
from ..models.doctors import Doctor
from ..models.appointments import Appointment

from ..auth.main import validate_token, UserSession
from ..schemas.medic_centers import CenterCreateSchema
#from ..schemas.jobs import JobTypeEnum, JobStatus, JobOutput
from ..database.conf import db
from typing import Optional
from jsonschema import SchemaError, ValidationError, validate

#temp
from sqlalchemy.orm import Session
from datetime import datetime

from ..routes.appointments import ConvertAppointment


router = APIRouter()

@router.post('/populate')
async def populate_database(database: Session = Depends(db)):

    s = [Specialty(name='Medicina General'),
         Specialty(name='Anestesiologia'), 
         Specialty(name='Cardiologia'), 
         Specialty(name='Pediatria'),
         ]

    for specialty in s:
        database.add(specialty)

    m = [MedicCenter(name='Vitacura', location='Vitacura 5951'),
         MedicCenter(name='La Dehesa', location='Avda. José Alcalde Délano 12205'),
         MedicCenter(name='Chicureo', location='Camino Chicureo, Lote A-2, s/n, Colina (Av. Chicureo con Av. El Valle)'),
         MedicCenter(name='Plaza Egaña', location='Edificio Egaña, Avenida Ossa 235, La Reina'),
         ]
    
    for center in m:
        database.add(center)

    d = [Doctor(name='Dr Andi', genderMale=True, specialty_id=1),
         Doctor(name='Dra Mari', genderMale=False, specialty_id=2),
         Doctor(name='Dr Profe', genderMale=True, specialty_id=3),
         ]
   
    for doc in d:
        database.add(doc)


    # Commit changes
    database.commit()

    return {'message': 'DB populated.'}

@router.post('/populate/appointments')
async def populate_apps(database: Session = Depends(db)):


    a = [Appointment(date=datetime(2023, 11, 25, 13, 30), doctor_id=1, medic_center_id=1),
         Appointment(date=datetime(2023, 11, 25, 14), doctor_id=1, medic_center_id=1),
         Appointment(date=datetime(2023, 11, 25, 14, 30), doctor_id=1, medic_center_id=1),
         Appointment(date=datetime(2023, 11, 25, 15), doctor_id=1, medic_center_id=1),
         Appointment(date=datetime(2023, 11, 25, 16, 30), doctor_id=1, medic_center_id=1),

         Appointment(date=datetime(2023, 11, 25, 13, 30), doctor_id=2, medic_center_id=2),
         Appointment(date=datetime(2023, 11, 25, 14), doctor_id=2, medic_center_id=2),
         Appointment(date=datetime(2023, 11, 25, 14, 30), doctor_id=2, medic_center_id=2),
         Appointment(date=datetime(2023, 11, 25, 15), doctor_id=2, medic_center_id=2),
         Appointment(date=datetime(2023, 11, 25, 16, 30), doctor_id=2, medic_center_id=2),

         Appointment(date=datetime(2023, 11, 25, 13, 30), doctor_id=3, medic_center_id=3),
         Appointment(date=datetime(2023, 11, 25, 14), doctor_id=3, medic_center_id=3),
         Appointment(date=datetime(2023, 11, 25, 14, 30), doctor_id=3, medic_center_id=3),
         Appointment(date=datetime(2023, 11, 25, 15), doctor_id=3, medic_center_id=3),
         Appointment(date=datetime(2023, 11, 25, 16, 30), doctor_id=3, medic_center_id=3),


         ]
    
    for app in a:
        database.add(app)

        # Send to OpenSearch
        converted_app = ConvertAppointment(database, app)
        data = json.loads(converted_app.json()) 
        requests.post('http://192.168.100.3:9200/appointments_index/_doc', json=data)
    
    



    # Commit changes
    database.commit()

    return {'message': 'Appointments populated'}