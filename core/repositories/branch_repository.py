from app.models.branch import Branch
from core.repositories.base import BaseRepository


class BranchRepository(BaseRepository):
    def create(self, branch: Branch) -> Branch:
        self.db.add(branch)
        self.db.commit()
        self.db.refresh(branch)
        return branch

    def list(self):
        return self.db.query(Branch).order_by(Branch.name.asc()).all()

    def get(self, branch_id: int) -> Branch | None:
        return self.db.query(Branch).filter(Branch.id == branch_id).first()

    def set_logo(self, branch: Branch, logo_url: str, updated_by: str) -> Branch:
        branch.logo_url = logo_url
        branch.created_by = updated_by
        self.db.commit()
        self.db.refresh(branch)
        return branch
