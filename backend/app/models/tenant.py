"""Multi-tenant organization model."""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from app.models.contract import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    domain = Column(String, unique=True)
    sam_uei = Column(String)
    cage_code = Column(String)
    is_active = Column(Boolean, default=True)
    subscription_tier = Column(String, default="starter")
    created_at = Column(DateTime, default=datetime.utcnow)
