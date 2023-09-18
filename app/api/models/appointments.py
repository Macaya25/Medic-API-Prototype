import os
import sys
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, sql
from sqlalchemy.dialects.postgresql import JSONB, UUID
from ..database.conf import Base
from datetime import datetime

sys.path.append(os.getcwd())

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True))
    location = Column(String, nullable=False)
    # Todo
    #medic = Column(ForeignKey('doctors.id'))
    

