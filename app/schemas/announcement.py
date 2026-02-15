from datetime import datetime

from pydantic import BaseModel

from app.schemas.common import ORMModel


class AnnouncementCreate(BaseModel):
    title: str
    body: str
    target_scope: str = "province"
    target_branch_code: str | None = None
    audience: str = "public"
    publish_at: datetime | None = None
    expires_at: datetime | None = None


class AnnouncementRead(AnnouncementCreate, ORMModel):
    id: int
    is_active: bool
