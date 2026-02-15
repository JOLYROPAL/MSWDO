from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.user import User
from app.schemas.announcement import AnnouncementCreate, AnnouncementRead
from core.repositories.announcement_repository import AnnouncementRepository
from core.services.announcement_service import AnnouncementService


router = APIRouter(prefix="/announcements", tags=["announcements"])


@router.post("", response_model=AnnouncementRead)
def create_announcement(
    payload: AnnouncementCreate,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("super_admin", "branch_admin", "communications_officer")),
):
    return AnnouncementService(AnnouncementRepository(db)).schedule(payload.model_dump())


@router.get("", response_model=list[AnnouncementRead])
def list_active_announcements(branch_code: str | None = None, db: Session = Depends(get_db)):
    return AnnouncementService(AnnouncementRepository(db)).list_visible(branch_code)
