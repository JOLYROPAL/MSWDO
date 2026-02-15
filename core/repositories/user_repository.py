from app.models.user import User
from core.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()
