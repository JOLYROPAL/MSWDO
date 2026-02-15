from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base
from app.models.base import AuditMixin


class CitizenCharter(AuditMixin, Base):
    __tablename__ = "citizen_charter"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), index=True)
    title: Mapped[str] = mapped_column(String(180))
    requirements: Mapped[str] = mapped_column(Text)
    steps: Mapped[str] = mapped_column(Text)
    standard_processing_hours: Mapped[int] = mapped_column(Integer, default=72)
