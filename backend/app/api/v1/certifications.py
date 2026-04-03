"""Certification tracking endpoints."""

from fastapi import APIRouter, Depends
from app.core.security import get_current_user

router = APIRouter()


@router.get("/")
async def list_certifications(user: dict = Depends(get_current_user)):
    return []


@router.get("/expiring")
async def expiring(days: int = 90, user: dict = Depends(get_current_user)):
    return {"window_days": days, "expiring": []}
