from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from enum import Enum as PyEnum

from .database import Base


class IncidentStatus(str, PyEnum):
    new = "new"
    in_progress = "in_progress"
    resolved = "resolved"


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.new)
    source = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
