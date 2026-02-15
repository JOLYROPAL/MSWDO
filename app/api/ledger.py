from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.user import User
from app.schemas.ledger import LedgerEntryRead
from core.repositories.ledger_repository import LedgerRepository


router = APIRouter(prefix="/ledger", tags=["ledger"])


@router.get("", response_model=list[LedgerEntryRead])
def list_ledger(branch_code: str | None = None, db: Session = Depends(get_db), _: User = Depends(require_role("super_admin", "auditor", "branch_admin"))):
    return LedgerRepository(db).list(branch_code)
