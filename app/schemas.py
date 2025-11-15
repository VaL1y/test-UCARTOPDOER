from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class IncidentStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    resolved = "resolved"


class IncidentCreate(BaseModel):
    description: str
    source: str
    status: IncidentStatus = IncidentStatus.new


class IncidentUpdate(BaseModel):
    status: IncidentStatus


class IncidentOut(BaseModel):
    id: int
    description: str
    status: IncidentStatus
    source: str
    created_at: datetime

    model_config = {"from_attributes": True}
