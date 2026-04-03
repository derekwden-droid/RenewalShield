"""Executive dashboard endpoints."""

from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.schemas.contract import RenewalHealthSummary

router = APIRouter()


@router.get("/health", response_model=RenewalHealthSummary)
async def portfolio_health(user: dict = Depends(get_current_user)):
    return RenewalHealthSummary(
        total_contracts=0, active=0, expiring_30d=0,
        expiring_90d=0, expired=0, avg_health_score=0.0,
    )
