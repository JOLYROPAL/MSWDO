from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.application import Application
from app.models.user import User

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db), _: User = Depends(require_role("super_admin", "branch_admin", "auditor"))):
    submitted = db.query(Application).count()
    pending = db.query(Application).filter(Application.status != "Closed").count()
    return {"total_applications": submitted, "pending_applications": pending}
