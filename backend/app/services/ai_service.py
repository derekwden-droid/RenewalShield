"""AI service for past performance narratives and renewal analysis."""

import anthropic
from app.core.config import settings

PAST_PERFORMANCE_PROMPT = """You are an expert government contracting writer specializing in past performance narratives for federal contract renewals. Generate compelling, evidence-based narratives addressing quality, schedule, cost control, management, and staffing. Output 400-600 words."""

RENEWAL_RISK_PROMPT = """You are a federal contract compliance analyst. Evaluate contract and certification data to produce: health score (0-100), risk factors with severity, recommended actions, and renewal readiness checklist. Return structured JSON."""


class AIService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.model = "claude-sonnet-4-20250514"

    async def generate_past_performance(self, contract_data: dict) -> str:
        msg = self.client.messages.create(
            model=self.model, max_tokens=2048,
            system=PAST_PERFORMANCE_PROMPT,
            messages=[{"role": "user", "content": f"Generate narrative for: {contract_data}"}],
        )
        return msg.content[0].text

    async def assess_renewal_risk(self, contract_data: dict, certs: list[dict]) -> dict:
        msg = self.client.messages.create(
            model=self.model, max_tokens=2048,
            system=RENEWAL_RISK_PROMPT,
            messages=[{"role": "user", "content": f"Contract: {contract_data}\nCertifications: {certs}"}],
        )
        return {"analysis": msg.content[0].text}


ai_service = AIService()
