from __future__ import annotations

from datetime import date
from decimal import Decimal
import uuid

from sqlalchemy import Date, ForeignKey, Integer, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class SkuProfitSnapshot(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "sku_profit_snapshots"

    store_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    variant_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False)
    snapshot_date: Mapped[date] = mapped_column(Date, index=True, nullable=False)
    units_sold: Mapped[int] = mapped_column(Integer, nullable=False)
    net_sales: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    cogs_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    allocated_ad_spend: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    refund_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    estimated_profit: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)

    store: Mapped["Store"] = relationship(back_populates="sku_profit_snapshots")
    variant: Mapped["ProductVariant"] = relationship(back_populates="sku_profit_snapshots")
