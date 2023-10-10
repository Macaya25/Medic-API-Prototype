from pydantic import BaseModel
from typing import Optional, Dict
from uuid import UUID
from enum import Enum
from datetime import datetime


class AppointmentCreateSchema(BaseModel):
    date: datetime = datetime.now()
    doctor_id: int
    medic_center_id: int