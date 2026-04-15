from __future__ import annotations

from datetime import date
from decimal import Decimal
import uuid

from sqlalchemy import Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class AdDailyInsight(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "ad_daily_insights"

    ad_account_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("ad_accounts.id", ondelete="CASCADE"), nullable=False)
    report_date: Mapped[date] = mapped_column(Date, index=True, nullable=False)
    level: Mapped[str] = mapped_column(String(30), index=True, nullable=False)
    campaign_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("ad_campaigns.id", ondelete="SET NULL"), nullable=True)
    adset_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("ad_sets.id", ondelete="SET NULL"), nullable=True)
    ad_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("ads.id", ondelete="SET NULL"), nullable=True)
    impressions: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    clicks: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    spend: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, server_default="0")
    reach: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    cpm: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False, server_default="0")
    cpc: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False, server_default="0")
    ctr: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False, server_default="0")
    purchases_reported: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    conversion_value_reported: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False, server_default="0")

    ad_account: Mapped["AdAccount"] = relationship(back_populates="daily_insights")
    campaign: Mapped["AdCampaign | None"] = relationship(back_populates="daily_insights")
    adset: Mapped["AdSet | None"] = relationship(back_populates="daily_insights")
    ad: Mapped["Ad | None"] = relationship(back_populates="daily_insights")
