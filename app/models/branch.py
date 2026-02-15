from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base
from app.models.base import AuditMixin


class Branch(AuditMixin, Base):
    __tablename__ = "branches"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    city_municipality: Mapped[str] = mapped_column(String(120), index=True)
    contact_email: Mapped[str] = mapped_column(String(150))
    contact_number: Mapped[str] = mapped_column(String(50))
    logo_url: Mapped[str | None] = mapped_column(String(300), nullable=True)
    announcement_theme: Mapped[str | None] = mapped_column(Text, nullable=True)
