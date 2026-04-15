from __future__ import annotations

from datetime import datetime
from decimal import Decimal
import uuid

from sqlalchemy import DateTime, ForeignKey, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class OrderCostBreakdown(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "order_cost_breakdowns"

    order_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"), unique=True, nullable=False)
    calculation_version: Mapped[str] = mapped_column(String(50), nullable=False)
    profit_view: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    gross_revenue: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    discounts: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    taxes: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    net_sales: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    cogs_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    packaging_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    shipping_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    cod_fee_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    payment_fee_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    remittance_fee_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    allocated_ad_spend_blended: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    allocated_ad_spend_attributed: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    refund_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    rto_cost_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    overhead_allocated: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    manual_adjustments_total: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    true_profit_blended: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    true_profit_attributed_estimated: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    true_margin_blended: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False)
    true_margin_attributed_estimated: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False)
    explanation_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))
    calculated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)

    order: Mapped["Order"] = relationship(back_populates="cost_breakdown")
