from app.models.citizen_charter import CitizenCharter
from core.repositories.charter_repository import CitizenCharterRepository


class CitizenCharterService:
    def __init__(self, repo: CitizenCharterRepository):
        self.repo = repo

    def create(self, payload: dict) -> CitizenCharter:
        return self.repo.create(CitizenCharter(**payload))

    def list(self, branch_id: int | None):
        return self.repo.list(branch_id)
