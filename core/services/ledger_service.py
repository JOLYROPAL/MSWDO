from decimal import Decimal

from app.models.ledger import LedgerEntry
from core.repositories.ledger_repository import LedgerRepository


class LedgerService:
    def __init__(self, ledger_repo: LedgerRepository):
        self.ledger_repo = ledger_repo

    def append_release_entry(self, reference_no: str, branch_code: str, created_by: str) -> LedgerEntry:
        entry = LedgerEntry(
            entry_type="disbursement",
            reference_no=reference_no,
            branch_code=branch_code,
            amount=Decimal("0.00"),
            description="Auto-generated release entry",
            created_by=created_by,
        )
        return self.ledger_repo.create(entry)
