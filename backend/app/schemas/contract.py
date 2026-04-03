"""Contract request/response schemas."""

from datetime import date, datetime
from pydantic import BaseModel, Field


class ContractCreate(BaseModel):
    contract_number: str
    title: str
    agency: str
    contracting_officer: str | None = None
    award_date: date | None = None
    period_of_performance_start: date | None = None
    period_of_performance_end: date | None = None
    renewal_deadline: date | None = None
    contract_value: str | None = None
    contract_type: str | None = None
    naics_code: str | None = None


class ContractResponse(ContractCreate):
    id: str
    tenant_id: str
    status: str
    health_score: str | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RenewalHealthSummary(BaseModel):
    total_contracts: int
    active: int
    expiring_30d: int
    expiring_90d: int
    expired: int
    avg_health_score: float
    critical_alerts: list[str] = Field(default_factory=list)
