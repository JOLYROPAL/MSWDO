from app.models.citizen_charter import CitizenCharter
from core.repositories.base import BaseRepository


class CitizenCharterRepository(BaseRepository):
    def list(self, branch_id: int | None = None):
        query = self.db.query(CitizenCharter)
        if branch_id is not None:
            query = query.filter(CitizenCharter.branch_id == branch_id)
        return query.order_by(CitizenCharter.service_id.asc()).all()

    def create(self, item: CitizenCharter) -> CitizenCharter:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item
