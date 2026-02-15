from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.core.deps import require_role
from app.db.session import get_db
from app.models.user import User
from app.schemas.branding import LogoUploadRead, ThemeRead
from core.repositories.branch_repository import BranchRepository
from core.services.theme_service import ThemeService
from security.branding_policy import BrandingPolicy


router = APIRouter(prefix="/branding", tags=["branding"])


@router.get("/theme", response_model=ThemeRead)
def get_theme():
    return ThemeService(BrandingPolicy()).get_locked_theme()


@router.post("/branches/{branch_id}/logo", response_model=LogoUploadRead)
def upload_branch_logo(
    branch_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(require_role("super_admin", "branch_admin")),
):
    raw = file.file.read()
    try:
        BrandingPolicy().validate_logo(file.content_type or "", raw)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    branch_repo = BranchRepository(db)
    branch = branch_repo.get(branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    suffix = ".png" if file.content_type == "image/png" else ".jpg"
    upload_dir = Path("static/uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)
    output_path = upload_dir / f"branch_{branch_id}_logo{suffix}"
    output_path.write_bytes(raw)

    logo_url = f"/{output_path.as_posix()}"
    branch_repo.set_logo(branch, logo_url=logo_url, updated_by=user.email)
    return LogoUploadRead(branch_id=branch_id, logo_url=logo_url)
