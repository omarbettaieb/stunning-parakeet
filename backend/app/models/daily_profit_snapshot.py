from __future__ import annotations

from datetime import date
from decimal import Decimal
import uuid

from sqlalchemy import Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class DailyProfitSnapshot(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "daily_profit_snapshots"

    store_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    snapshot_date: Mapped[date] = mapped_column(Date, index=True, nullable=False)
    profit_view: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    orders_count: Mapped[int] = mapped_column(Integer, nullable=False)
    delivered_orders_count: Mapped[int] = mapped_column(Integer, nullable=False)
    rto_orders_count: Mapped[int] = mapped_column(Integer, nullable=False)
    revenue_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    ad_spend_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    cogs_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    shipping_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    fees_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    refund_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    overhead_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    true_profit_blended: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    mer_blended: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False)
    break_even_roas: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False)

    store: Mapped["Store"] = relationship(back_populates="daily_profit_snapshots")
