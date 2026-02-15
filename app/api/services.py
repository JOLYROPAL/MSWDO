from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.service import Service
from app.models.user import User
from app.schemas.service import ServiceCreate, ServiceRead
from core.repositories.service_repository import ServiceRepository


router = APIRouter(prefix="/services", tags=["services"])


@router.post("", response_model=ServiceRead)
def create_service(payload: ServiceCreate, db: Session = Depends(get_db), _: User = Depends(require_role("super_admin", "branch_admin"))):
    return ServiceRepository(db).create(Service(**payload.model_dump(), created_by="system"))


@router.get("", response_model=list[ServiceRead])
def list_services(branch_code: str | None = None, db: Session = Depends(get_db)):
    return ServiceRepository(db).list_active(branch_code)
