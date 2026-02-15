from pydantic import BaseModel, EmailStr, Field

from app.schemas.common import ORMModel


class ApplicationCreate(BaseModel):
    service_id: int
    applicant_name: str
    applicant_email: EmailStr
    branch_code: str
    payload: dict = Field(default_factory=dict)


class ApplicationStatusUpdate(BaseModel):
    to_status: str
    remarks: str | None = None


class ApplicationRead(ORMModel):
    id: int
    reference_no: str
    service_id: int
    applicant_name: str
    applicant_email: EmailStr
    branch_code: str
    status: str
    payload: dict
