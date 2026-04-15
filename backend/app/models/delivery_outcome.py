from __future__ import annotations

from datetime import datetime
from decimal import Decimal
import uuid

from sqlalchemy import DateTime, ForeignKey, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class DeliveryOutcome(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "delivery_outcomes"

    order_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"), unique=True, nullable=False)
    courier_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    tracking_number: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    shipped_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    first_delivery_attempt_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    delivered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    returned_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    outcome_status: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    outbound_shipping_cost: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    return_shipping_cost: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    cod_fee_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    remittance_fee_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    raw_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))

    order: Mapped["Order"] = relationship(back_populates="delivery_outcome")
