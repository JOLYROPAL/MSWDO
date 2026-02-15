from decimal import Decimal

from pydantic import BaseModel

from app.schemas.common import ORMModel


class LedgerEntryCreate(BaseModel):
    entry_type: str
    reference_no: str
    branch_code: str
    amount: Decimal
    description: str


class LedgerEntryRead(LedgerEntryCreate, ORMModel):
    id: int
    created_by: str
