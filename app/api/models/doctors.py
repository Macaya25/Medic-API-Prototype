import os
import sys
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, sql
from sqlalchemy.dialects.postgresql import JSONB, UUID
from ..database.conf import Base
from datetime import datetime

sys.path.append(os.getcwd())

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    genderMale = Column(Boolean, nullable=False)
    name = Column(String, nullable=False)
    specialty_id = Column(ForeignKey('specialties.id'))