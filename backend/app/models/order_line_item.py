from __future__ import annotations

from decimal import Decimal
import uuid

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import text

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class OrderLineItem(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "order_line_items"

    order_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="SET NULL"), nullable=True)
    variant_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("product_variants.id", ondelete="SET NULL"), nullable=True)
    shopify_line_item_id: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    sku: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    line_discount_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    line_tax_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    net_line_revenue: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    applied_cogs_unit: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)
    applied_packaging_unit: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)
    raw_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))

    order: Mapped["Order"] = relationship(back_populates="line_items")
    product: Mapped["Product | None"] = relationship(back_populates="order_line_items")
    variant: Mapped["ProductVariant | None"] = relationship(back_populates="order_line_items")
