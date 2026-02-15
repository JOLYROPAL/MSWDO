from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.user import User
from app.schemas.citizen_charter import CitizenCharterCreate, CitizenCharterRead
from core.repositories.charter_repository import CitizenCharterRepository
from core.services.citizen_charter_service import CitizenCharterService


router = APIRouter(prefix="/citizen-charter", tags=["citizen-charter"])


@router.post("", response_model=CitizenCharterRead)
def create_item(payload: CitizenCharterCreate, db: Session = Depends(get_db), user: User = Depends(require_role("super_admin", "branch_admin"))):
    data = payload.model_dump()
    data["created_by"] = user.email
    return CitizenCharterService(CitizenCharterRepository(db)).create(data)


@router.get("", response_model=list[CitizenCharterRead])
def list_items(branch_id: int | None = None, db: Session = Depends(get_db)):
    return CitizenCharterService(CitizenCharterRepository(db)).list(branch_id)
