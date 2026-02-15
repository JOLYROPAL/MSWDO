from app.models.application import Application, ApplicationStatusHistory
from core.repositories.base import BaseRepository


class ApplicationRepository(BaseRepository):
    def create(self, app: Application) -> Application:
        self.db.add(app)
        self.db.commit()
        self.db.refresh(app)
        return app

    def get(self, application_id: int) -> Application | None:
        return self.db.query(Application).filter(Application.id == application_id).first()

    def add_history(self, history: ApplicationStatusHistory) -> None:
        self.db.add(history)

    def save(self) -> None:
        self.db.commit()
