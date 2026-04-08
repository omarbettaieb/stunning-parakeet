from __future__ import annotations

from datetime import datetime
import uuid

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin


class SyncRun(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "sync_runs"

    integration_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("integrations.id", ondelete="CASCADE"), nullable=False)
    sync_type: Mapped[str] = mapped_column(String(50), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cursor_from: Mapped[str | None] = mapped_column(String(255), nullable=True)
    cursor_to: Mapped[str | None] = mapped_column(String(255), nullable=True)
    records_processed: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    metadata_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    integration: Mapped["Integration"] = relationship(back_populates="sync_runs")
    raw_meta_insights: Mapped[list["RawMetaInsight"]] = relationship(back_populates="sync_run")
