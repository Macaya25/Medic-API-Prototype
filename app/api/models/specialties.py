import os
import sys
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, sql
from sqlalchemy.dialects.postgresql import JSONB, UUID
from ..database.conf import Base
from datetime import datetime

sys.path.append(os.getcwd())

class Specialty(Base):
    __tablename__ = 'specialties'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)