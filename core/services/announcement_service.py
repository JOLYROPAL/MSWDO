from datetime import datetime, timezone

from app.models.announcement import Announcement
from core.repositories.announcement_repository import AnnouncementRepository


class AnnouncementService:
    def __init__(self, repo: AnnouncementRepository):
        self.repo = repo

    def schedule(self, payload: dict) -> Announcement:
        if not payload.get("publish_at"):
            payload["publish_at"] = datetime.now(timezone.utc)
        return self.repo.create(Announcement(**payload))

    def list_visible(self, branch_code: str | None):
        return self.repo.list_visible(branch_code)
