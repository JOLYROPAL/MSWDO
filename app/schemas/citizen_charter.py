from pydantic import BaseModel

from app.schemas.common import ORMModel


class CitizenCharterCreate(BaseModel):
    service_id: int
    title: str
    requirements: str
    steps: str
    standard_processing_hours: int = 72
    branch_id: int | None = None


class CitizenCharterRead(CitizenCharterCreate, ORMModel):
    id: int
