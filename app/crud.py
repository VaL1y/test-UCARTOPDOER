from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Incident


async def create_incident(db: AsyncSession, data):
    incident = Incident(**data.model_dump())
    db.add(incident)
    await db.commit()
    await db.refresh(incident)
    return incident


async def get_incidents(db: AsyncSession, status: str | None = None):
    query = select(Incident)
    if status:
        query = query.where(Incident.status == status)
    result = await db.execute(query)
    return result.scalars().all()


async def update_incident_status(db: AsyncSession, incident_id: int, status: str):
    result = await db.execute(select(Incident).where(Incident.id == incident_id))
    incident = result.scalars().first()
    if not incident:
        return None

    incident.status = status
    await db.commit()
    await db.refresh(incident)
    return incident
