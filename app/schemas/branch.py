from pydantic import BaseModel, EmailStr

from app.schemas.common import ORMModel


class BranchCreate(BaseModel):
    code: str
    name: str
    city_municipality: str
    contact_email: EmailStr
    contact_number: str
    logo_url: str | None = None


class BranchRead(BranchCreate, ORMModel):
    id: int
