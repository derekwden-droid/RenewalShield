"""Certification tracking model."""

from datetime import datetime
from sqlalchemy import Column, String, Date, DateTime, Boolean, ForeignKey
from app.models.contract import Base


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(String, primary_key=True)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False, index=True)
    cert_type = Column(String, nullable=False)
    cert_number = Column(String)
    issuing_authority = Column(String, nullable=False)
    issue_date = Column(Date)
    expiration_date = Column(Date, nullable=False, index=True)
    auto_renew = Column(Boolean, default=False)
    renewal_lead_days = Column(String, default="90")
    status = Column(String, default="active")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
