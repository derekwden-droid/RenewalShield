"""Contract data model."""

from datetime import datetime
from sqlalchemy import Column, String, Date, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(String, primary_key=True)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False, index=True)
    contract_number = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    agency = Column(String, nullable=False)
    contracting_officer = Column(String)
    award_date = Column(Date)
    period_of_performance_start = Column(Date)
    period_of_performance_end = Column(Date)
    renewal_deadline = Column(Date, index=True)
    contract_value = Column(String)
    contract_type = Column(String)
    naics_code = Column(String)
    status = Column(String, default="active")
    health_score = Column(String)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
