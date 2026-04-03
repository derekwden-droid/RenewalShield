"""Contract management endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_user
from app.schemas.contract import ContractCreate, ContractResponse
from app.services.ai_service import ai_service

router = APIRouter()


@router.get("/")
async def list_contracts(user: dict = Depends(get_current_user)):
    return []


@router.post("/", status_code=201)
async def create_contract(contract: ContractCreate, user: dict = Depends(get_current_user)):
    raise HTTPException(status_code=501, detail="Supabase integration pending")


@router.post("/{contract_id}/past-performance")
async def generate_past_performance(contract_id: str, user: dict = Depends(get_current_user)):
    narrative = await ai_service.generate_past_performance({"contract_id": contract_id})
    return {"contract_id": contract_id, "narrative": narrative}


@router.get("/{contract_id}/risk-assessment")
async def risk_assessment(contract_id: str, user: dict = Depends(get_current_user)):
    result = await ai_service.assess_renewal_risk({"contract_id": contract_id}, [])
    return {"contract_id": contract_id, **result}
