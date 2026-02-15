from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.user import User
from app.schemas.application import ApplicationCreate, ApplicationRead, ApplicationStatusUpdate
from core.repositories.application_repository import ApplicationRepository
from core.repositories.ledger_repository import LedgerRepository
from core.repositories.service_repository import ServiceRepository
from core.services.application_service import ApplicationService
from core.services.ledger_service import LedgerService
from core.services.workflow_service import WorkflowService


router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=ApplicationRead)
def submit_application(payload: ApplicationCreate, db: Session = Depends(get_db)):
    svc = ApplicationService(
        application_repo=ApplicationRepository(db),
        service_repo=ServiceRepository(db),
        workflow_service=WorkflowService(),
        ledger_service=LedgerService(LedgerRepository(db)),
    )
    return svc.submit(payload.model_dump())


@router.patch("/{application_id}/status", response_model=ApplicationRead)
def update_status(
    application_id: int,
    payload: ApplicationStatusUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(require_role("super_admin", "branch_admin", "case_worker")),
):
    svc = ApplicationService(
        application_repo=ApplicationRepository(db),
        service_repo=ServiceRepository(db),
        workflow_service=WorkflowService(),
        ledger_service=LedgerService(LedgerRepository(db)),
    )
    try:
        result = svc.transition(application_id, payload.to_status, payload.remarks, user.email)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    if not result:
        raise HTTPException(status_code=404, detail="Application not found")
    return result
