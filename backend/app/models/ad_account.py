from __future__ import annotations

import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class AdAccount(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "ad_accounts"

    store_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    meta_account_id: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    account_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    currency_code: Mapped[str | None] = mapped_column(String(3), nullable=True)
    timezone_name: Mapped[str | None] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False)

    store: Mapped["Store"] = relationship(back_populates="ad_accounts")
    campaigns: Mapped[list["AdCampaign"]] = relationship(back_populates="ad_account", cascade="all, delete-orphan")
    daily_insights: Mapped[list["AdDailyInsight"]] = relationship(back_populates="ad_account", cascade="all, delete-orphan")
