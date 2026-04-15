"""Import all models for SQLAlchemy metadata discovery."""

from app.models.ad import Ad
from app.models.ad_account import AdAccount
from app.models.ad_campaign import AdCampaign
from app.models.ad_daily_insight import AdDailyInsight
from app.models.ad_set import AdSet
from app.models.alert import Alert
from app.models.cost_rule import CostRule
from app.models.daily_profit_snapshot import DailyProfitSnapshot
from app.models.delivery_outcome import DeliveryOutcome
from app.models.integration import Integration
from app.models.manual_expense import ManualExpense
from app.models.order import Order
from app.models.order_cost_breakdown import OrderCostBreakdown
from app.models.order_line_item import OrderLineItem
from app.models.product import Product
from app.models.product_cost_history import ProductCostHistory
from app.models.product_variant import ProductVariant
from app.models.raw_meta_insight import RawMetaInsight
from app.models.raw_shopify_event import RawShopifyEvent
from app.models.refund import Refund
from app.models.sku_profit_snapshot import SkuProfitSnapshot
from app.models.store import Store
from app.models.sync_run import SyncRun
from app.models.transaction import Transaction
from app.models.user import User

__all__ = [
    "Ad",
    "AdAccount",
    "AdCampaign",
    "AdDailyInsight",
    "AdSet",
    "Alert",
    "CostRule",
    "DailyProfitSnapshot",
    "DeliveryOutcome",
    "Integration",
    "ManualExpense",
    "Order",
    "OrderCostBreakdown",
    "OrderLineItem",
    "Product",
    "ProductCostHistory",
    "ProductVariant",
    "RawMetaInsight",
    "RawShopifyEvent",
    "Refund",
    "SkuProfitSnapshot",
    "Store",
    "SyncRun",
    "Transaction",
    "User",
]
