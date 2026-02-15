from uuid import uuid4

from app.models.application import Application, ApplicationStatusHistory
from core.repositories.application_repository import ApplicationRepository
from core.repositories.service_repository import ServiceRepository
from core.services.ledger_service import LedgerService
from core.services.workflow_service import WorkflowService


class ApplicationService:
    def __init__(
        self,
        application_repo: ApplicationRepository,
        service_repo: ServiceRepository,
        workflow_service: WorkflowService,
        ledger_service: LedgerService,
    ):
        self.application_repo = application_repo
        self.service_repo = service_repo
        self.workflow_service = workflow_service
        self.ledger_service = ledger_service

    def submit(self, payload: dict) -> Application:
        app = Application(reference_no=f"MSWDO-{uuid4().hex[:10].upper()}", **payload)
        return self.application_repo.create(app)

    def transition(self, application_id: int, to_status: str, remarks: str | None, actor_email: str) -> Application | None:
        app = self.application_repo.get(application_id)
        if not app:
            return None

        service = self.service_repo.get(app.service_id)
        service_slug = service.slug if service else None
        if not self.workflow_service.validate_transition(app.status, to_status, service_slug=service_slug):
            raise ValueError(f"Invalid transition from {app.status} to {to_status}")

        previous = app.status
        app.status = to_status
        self.application_repo.add_history(
            ApplicationStatusHistory(
                application_id=application_id,
                from_status=previous,
                to_status=to_status,
                remarks=remarks,
                changed_by=actor_email,
                created_by=actor_email,
                branch_id=app.branch_id,
            )
        )
        if to_status == "Released":
            self.ledger_service.append_release_entry(app.reference_no, app.branch_code, actor_email)
        self.application_repo.save()
        return app
