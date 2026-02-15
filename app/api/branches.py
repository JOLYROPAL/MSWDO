from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.branch import Branch
from app.models.user import User
from app.schemas.branch import BranchCreate, BranchRead
from core.repositories.branch_repository import BranchRepository


router = APIRouter(prefix="/branches", tags=["branches"])


@router.post("", response_model=BranchRead)
def create_branch(payload: BranchCreate, db: Session = Depends(get_db), _: User = Depends(require_role("super_admin"))):
    return BranchRepository(db).create(Branch(**payload.model_dump(), created_by="system"))


@router.get("", response_model=list[BranchRead])
def list_branches(db: Session = Depends(get_db)):
    return BranchRepository(db).list()
