from __future__ import annotations

from datetime import date, datetime
import uuid

from sqlalchemy import Date, DateTime, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import UUIDPrimaryKeyMixin


class RawMetaInsight(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "raw_meta_insights"

    store_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    ad_account_id: Mapped[str] = mapped_column(String(64), nullable=False)
    level: Mapped[str] = mapped_column(String(30), nullable=False)
    date_start: Mapped[date] = mapped_column(Date, nullable=False)
    date_stop: Mapped[date] = mapped_column(Date, nullable=False)
    payload_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    sync_run_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("sync_runs.id", ondelete="SET NULL"), nullable=True)

    store: Mapped["Store"] = relationship(back_populates="raw_meta_insights")
    sync_run: Mapped["SyncRun | None"] = relationship(back_populates="raw_meta_insights")
