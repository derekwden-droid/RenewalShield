"""API v1 router."""

from fastapi import APIRouter
from app.api.v1.contracts import router as contracts_router
from app.api.v1.certifications import router as certs_router
from app.api.v1.dashboard import router as dashboard_router

router = APIRouter()
router.include_router(contracts_router, prefix="/contracts", tags=["Contracts"])
router.include_router(certs_router, prefix="/certifications", tags=["Certifications"])
router.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
