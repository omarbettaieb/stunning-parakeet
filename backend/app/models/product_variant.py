from __future__ import annotations

import uuid
from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class ProductVariant(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "product_variants"

    product_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    shopify_variant_id: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    sku: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    barcode: Mapped[str | None] = mapped_column(String(100), nullable=True)
    title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    option1: Mapped[str | None] = mapped_column(String(255), nullable=True)
    option2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    option3: Mapped[str | None] = mapped_column(String(255), nullable=True)
    current_price: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)
    compare_at_price: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="true")
    raw_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))

    product: Mapped["Product"] = relationship(back_populates="variants")
    cost_history: Mapped[list["ProductCostHistory"]] = relationship(back_populates="variant", cascade="all, delete-orphan")
    order_line_items: Mapped[list["OrderLineItem"]] = relationship(back_populates="variant")
    sku_profit_snapshots: Mapped[list["SkuProfitSnapshot"]] = relationship(back_populates="variant")
