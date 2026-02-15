from pydantic import BaseModel

from app.schemas.common import ORMModel


class ServiceCreate(BaseModel):
    name: str
    slug: str
    description: str
    eligibility: str
    processing_days: int = 3
    branch_code: str | None = None


class ServiceRead(ServiceCreate, ORMModel):
    id: int
    is_active: bool
