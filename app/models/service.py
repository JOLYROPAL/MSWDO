from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base
from app.models.base import AuditMixin


class Service(AuditMixin, Base):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(180), index=True)
    slug: Mapped[str] = mapped_column(String(180), unique=True, index=True)
    description: Mapped[str] = mapped_column(Text)
    eligibility: Mapped[str] = mapped_column(Text)
    processing_days: Mapped[int] = mapped_column(Integer, default=3)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    branch_code: Mapped[str | None] = mapped_column(String(20), nullable=True, index=True)


class ServiceForm(AuditMixin, Base):
    __tablename__ = "service_forms"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), index=True)
    form_name: Mapped[str] = mapped_column(String(180))
    online_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    downloadable_url: Mapped[str | None] = mapped_column(String(300), nullable=True)
