from datetime import datetime, timezone

from app.models.announcement import Announcement
from core.repositories.base import BaseRepository


class AnnouncementRepository(BaseRepository):
    def create(self, announcement: Announcement) -> Announcement:
        self.db.add(announcement)
        self.db.commit()
        self.db.refresh(announcement)
        return announcement

    def list_visible(self, branch_code: str | None):
        now = datetime.now(timezone.utc)
        query = self.db.query(Announcement).filter(Announcement.is_active.is_(True), Announcement.publish_at <= now)
        if branch_code:
            query = query.filter((Announcement.target_branch_code == branch_code) | (Announcement.target_scope == "province"))
        return query.filter((Announcement.expires_at.is_(None)) | (Announcement.expires_at >= now)).all()
