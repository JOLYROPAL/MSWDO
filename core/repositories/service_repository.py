from app.models.service import Service
from core.repositories.base import BaseRepository


class ServiceRepository(BaseRepository):
    def create(self, service: Service) -> Service:
        self.db.add(service)
        self.db.commit()
        self.db.refresh(service)
        return service

    def list_active(self, branch_code: str | None):
        query = self.db.query(Service).filter(Service.is_active.is_(True))
        if branch_code:
            query = query.filter((Service.branch_code == branch_code) | (Service.branch_code.is_(None)))
        return query.order_by(Service.name.asc()).all()

    def get(self, service_id: int) -> Service | None:
        return self.db.query(Service).filter(Service.id == service_id).first()
