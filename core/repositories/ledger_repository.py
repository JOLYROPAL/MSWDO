from app.models.ledger import LedgerEntry
from core.repositories.base import BaseRepository


class LedgerRepository(BaseRepository):
    def create(self, entry: LedgerEntry) -> LedgerEntry:
        self.db.add(entry)
        return entry

    def list(self, branch_code: str | None):
        query = self.db.query(LedgerEntry)
        if branch_code:
            query = query.filter(LedgerEntry.branch_code == branch_code)
        return query.order_by(LedgerEntry.created_at.desc()).all()
