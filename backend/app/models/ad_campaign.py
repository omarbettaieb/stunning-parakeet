from __future__ import annotations

from datetime import datetime
import uuid

from sqlalchemy import DateTime, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class AdCampaign(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "ad_campaigns"

    ad_account_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("ad_accounts.id", ondelete="CASCADE"), nullable=False)
    meta_campaign_id: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    objective: Mapped[str | None] = mapped_column(String(100), nullable=True)
    status: Mapped[str | None] = mapped_column(String(50), nullable=True)
    created_at_source: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    updated_at_source: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    raw_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))

    ad_account: Mapped["AdAccount"] = relationship(back_populates="campaigns")
    ad_sets: Mapped[list["AdSet"]] = relationship(back_populates="campaign", cascade="all, delete-orphan")
    daily_insights: Mapped[list["AdDailyInsight"]] = relationship(back_populates="campaign")
