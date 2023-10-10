from pydantic import BaseModel
from typing import Optional, Dict
from uuid import UUID
from enum import Enum
from datetime import datetime


class AppointmentCreateSchema(BaseModel):
    location: str
    date: datetime = datetime.now()
    doctor_id: int