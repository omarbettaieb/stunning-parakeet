from __future__ import annotations

from datetime import datetime
import uuid

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class CostRule(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "cost_rules"

    store_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    rule_type: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    rule_name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="true")
    priority: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    conditions_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    value_type: Mapped[str] = mapped_column(String(50), nullable=False)
    value_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    effective_from: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
    effective_to: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), index=True, nullable=True)

    store: Mapped["Store"] = relationship(back_populates="cost_rules")
