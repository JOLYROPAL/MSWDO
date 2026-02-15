from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any


@dataclass
class BaseEntity:
    created_by: str
    branch_id: int | None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class Role(BaseEntity):
    name: str = "citizen"


@dataclass
class User(BaseEntity):
    email: str = ""
    full_name: str = ""
    role_name: str = "citizen"


@dataclass
class Branch(BaseEntity):
    code: str = ""
    name: str = ""
    city_municipality: str = ""


@dataclass
class Service(BaseEntity):
    name: str = ""
    slug: str = ""
    eligibility: str = ""
    processing_days: int = 3


@dataclass
class CitizenCharter(BaseEntity):
    service_id: int = 0
    standard_processing_time: str = ""
    requirements: str = ""


@dataclass
class Form(BaseEntity):
    service_id: int = 0
    name: str = ""


@dataclass
class DocumentUpload(BaseEntity):
    application_id: int = 0
    file_name: str = ""
    mime_type: str = ""


@dataclass
class WorkflowStep(BaseEntity):
    application_id: int = 0
    from_status: str = "Submitted"
    to_status: str = "Submitted"


@dataclass
class Application(BaseEntity):
    service_id: int = 0
    applicant_name: str = ""
    applicant_email: str = ""
    status: str = "Submitted"
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass
class Announcement(BaseEntity):
    title: str = ""
    body: str = ""


@dataclass
class LedgerEntry(BaseEntity):
    reference_no: str = ""
    amount: Decimal = Decimal("0.00")
    description: str = ""
