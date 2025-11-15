from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_session
from ..crud import create_incident, get_incidents, update_incident_status
from ..schemas import IncidentCreate, IncidentOut, IncidentUpdate

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post("/", response_model=IncidentOut)
async def create(data: IncidentCreate, db: AsyncSession = Depends(get_session)):
    return await create_incident(db, data)


@router.get("/", response_model=list[IncidentOut])
async def list_incidents(status: str | None = None, db: AsyncSession = Depends(get_session)):
    return await get_incidents(db, status)


@router.patch("/{incident_id}", response_model=IncidentOut)
async def update(incident_id: int, data: IncidentUpdate, db: AsyncSession = Depends(get_session)):
    incident = await update_incident_status(db, incident_id, data.status)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident
