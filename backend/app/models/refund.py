from __future__ import annotations

from datetime import datetime
from decimal import Decimal
import uuid

from sqlalchemy import DateTime, ForeignKey, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class Refund(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "refunds"

    order_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    shopify_refund_id: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    refunded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
    total_refund_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    restock_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    raw_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))

    order: Mapped["Order"] = relationship(back_populates="refunds")
