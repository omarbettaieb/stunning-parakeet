from __future__ import annotations

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin, UUIDPrimaryKeyMixin


class Store(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "stores"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    shopify_shop_domain: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    currency_code: Mapped[str] = mapped_column(String(3), nullable=False, server_default="TND")
    timezone: Mapped[str] = mapped_column(String(64), nullable=False, server_default="Africa/Tunis")
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="true")

    integrations: Mapped[list["Integration"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    raw_shopify_events: Mapped[list["RawShopifyEvent"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    raw_meta_insights: Mapped[list["RawMetaInsight"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    products: Mapped[list["Product"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    orders: Mapped[list["Order"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    ad_accounts: Mapped[list["AdAccount"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    cost_rules: Mapped[list["CostRule"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    manual_expenses: Mapped[list["ManualExpense"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    daily_profit_snapshots: Mapped[list["DailyProfitSnapshot"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    sku_profit_snapshots: Mapped[list["SkuProfitSnapshot"]] = relationship(back_populates="store", cascade="all, delete-orphan")
    alerts: Mapped[list["Alert"]] = relationship(back_populates="store", cascade="all, delete-orphan")
