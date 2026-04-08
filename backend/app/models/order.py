from __future__ import annotations

from datetime import datetime
from decimal import Decimal
import uuid

from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class Order(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "orders"

    store_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("stores.id", ondelete="CASCADE"), nullable=False)
    shopify_order_id: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    order_number: Mapped[str | None] = mapped_column(String(64), nullable=True)
    customer_email: Mapped[str | None] = mapped_column(String(320), index=True, nullable=True)
    currency_code: Mapped[str] = mapped_column(String(3), nullable=False)
    order_created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
    order_updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True, nullable=False)
    financial_status: Mapped[str | None] = mapped_column(String(50), index=True, nullable=True)
    fulfillment_status: Mapped[str | None] = mapped_column(String(50), index=True, nullable=True)
    cancel_reason: Mapped[str | None] = mapped_column(String(255), nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    source_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    landing_site: Mapped[str | None] = mapped_column(String(500), nullable=True)
    referring_site: Mapped[str | None] = mapped_column(String(500), nullable=True)
    customer_locale: Mapped[str | None] = mapped_column(String(20), nullable=True)
    subtotal_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    total_discounts: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    total_tax: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    total_shipping_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    total_price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    is_cod: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="false")
    cod_lifecycle_status: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    delivered_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    remitted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    marketing_source: Mapped[str | None] = mapped_column(String(100), index=True, nullable=True)
    attributed_campaign_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    attributed_campaign_id: Mapped[str | None] = mapped_column(String(64), index=True, nullable=True)
    attributed_adset_id: Mapped[str | None] = mapped_column(String(64), index=True, nullable=True)
    attributed_ad_id: Mapped[str | None] = mapped_column(String(64), index=True, nullable=True)
    raw_json: Mapped[dict] = mapped_column(JSONB, nullable=False, server_default=text("'{}'::jsonb"))

    store: Mapped["Store"] = relationship(back_populates="orders")
    line_items: Mapped[list["OrderLineItem"]] = relationship(back_populates="order", cascade="all, delete-orphan")
    refunds: Mapped[list["Refund"]] = relationship(back_populates="order", cascade="all, delete-orphan")
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="order", cascade="all, delete-orphan")
    delivery_outcome: Mapped["DeliveryOutcome | None"] = relationship(back_populates="order", uselist=False, cascade="all, delete-orphan")
    cost_breakdown: Mapped["OrderCostBreakdown | None"] = relationship(back_populates="order", uselist=False, cascade="all, delete-orphan")
